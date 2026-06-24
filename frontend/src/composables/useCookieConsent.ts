import { computed, reactive, readonly } from "vue";
import { disableAnalytics, enableAnalytics } from "@/services/analytics";

/**
 * DSGVO/TTDSG-konformes Cookie-Consent-Management.
 *
 * Prinzipien:
 * - Notwendige Cookies sind immer aktiv und nicht abwählbar.
 * - Optionale Kategorien (Analytics, externe Medien) erst nach Einwilligung.
 */

const STORAGE_KEY = "garmonia_cookie_consent";
const CONSENT_VERSION = 2;

export type ConsentCategory = "analytics" | "externalMedia";

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
    analytics: false,
    externalMedia: false,
  },
});

function applyCategorySideEffects(): void {
  if (state.categories.analytics) {
    enableAnalytics();
  } else {
    disableAnalytics();
  }
}

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

    state.categories.analytics = Boolean(parsed.categories?.analytics);
    state.categories.externalMedia = Boolean(parsed.categories?.externalMedia);
    state.decided = true;
    state.bannerOpen = false;
    applyCategorySideEffects();
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
    state.categories.analytics = true;
    state.categories.externalMedia = true;
    finishDecision();
  }

  function acceptEssentialOnly(): void {
    state.categories.analytics = false;
    state.categories.externalMedia = false;
    finishDecision();
  }

  function savePreferences(categories: Record<ConsentCategory, boolean>): void {
    state.categories.analytics = Boolean(categories.analytics);
    state.categories.externalMedia = Boolean(categories.externalMedia);
    finishDecision();
  }

  function finishDecision(): void {
    state.decided = true;
    state.bannerOpen = false;
    state.settingsOpen = false;
    persist();
    applyCategorySideEffects();
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
