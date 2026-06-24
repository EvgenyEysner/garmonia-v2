import { computed, reactive, readonly } from "vue";

/**
 * DSGVO/TTDSG-konformes Cookie-Consent-Management.
 *
 * Prinzipien:
 * - Notwendige Cookies sind immer aktiv und nicht abwählbar.
 * - Optionale Kategorien (z. B. externe Medien wie Google Maps) sind erst nach
 *   aktiver Einwilligung erlaubt (kein Vorab-Opt-in).
 * - Die Entscheidung wird mit Version + Zeitstempel gespeichert; eine
 *   Versionserhöhung erzwingt eine erneute Einwilligung.
 */

const STORAGE_KEY = "garmonia_cookie_consent";
const CONSENT_VERSION = 1;

export type ConsentCategory = "externalMedia";

interface StoredConsent {
  version: number;
  timestamp: string;
  categories: Record<ConsentCategory, boolean>;
}

interface ConsentState {
  decided: boolean;
  bannerOpen: boolean;
  settingsOpen: boolean;
  categories: Record<ConsentCategory, boolean>;
}

const state = reactive<ConsentState>({
  decided: false,
  bannerOpen: false,
  settingsOpen: false,
  categories: {
    externalMedia: false,
  },
});

function loadFromStorage(): void {
  if (typeof window === "undefined") return;

  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) {
      state.bannerOpen = true;
      return;
    }

    const parsed = JSON.parse(raw) as StoredConsent;
    if (parsed.version !== CONSENT_VERSION) {
      state.bannerOpen = true;
      return;
    }

    state.categories.externalMedia = Boolean(parsed.categories?.externalMedia);
    state.decided = true;
    state.bannerOpen = false;
  } catch {
    state.bannerOpen = true;
  }
}

function persist(): void {
  if (typeof window === "undefined") return;

  const payload: StoredConsent = {
    version: CONSENT_VERSION,
    timestamp: new Date().toISOString(),
    categories: { ...state.categories },
  };

  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
  } catch {
    /* localStorage nicht verfügbar – Entscheidung gilt nur für die Session. */
  }
}

let initialized = false;

function init(): void {
  if (initialized) return;
  initialized = true;
  loadFromStorage();
}

export function useCookieConsent() {
  init();

  function acceptAll(): void {
    state.categories.externalMedia = true;
    finishDecision();
  }

  function acceptEssentialOnly(): void {
    state.categories.externalMedia = false;
    finishDecision();
  }

  function savePreferences(categories: Record<ConsentCategory, boolean>): void {
    state.categories.externalMedia = Boolean(categories.externalMedia);
    finishDecision();
  }

  function finishDecision(): void {
    state.decided = true;
    state.bannerOpen = false;
    state.settingsOpen = false;
    persist();
  }

  function openSettings(): void {
    state.settingsOpen = true;
    state.bannerOpen = true;
  }

  function closeSettings(): void {
    state.settingsOpen = false;
    if (state.decided) {
      state.bannerOpen = false;
    }
  }

  return {
    consent: readonly(state),
    isAllowed: (category: ConsentCategory) => computed(() => state.categories[category]),
    acceptAll,
    acceptEssentialOnly,
    savePreferences,
    openSettings,
    closeSettings,
  };
}
