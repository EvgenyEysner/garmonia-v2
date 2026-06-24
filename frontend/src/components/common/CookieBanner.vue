<script setup lang="ts">
import { ref, watch } from "vue";
import { Cookie, X } from "@lucide/vue";
import { useCookieConsent } from "@/composables/useCookieConsent";

const {
  consent,
  acceptAll,
  acceptEssentialOnly,
  savePreferences,
  openSettings,
  closeSettings,
} = useCookieConsent();

const externalMedia = ref(consent.categories.externalMedia);

watch(
  () => consent.settingsOpen,
  (open) => {
    if (open) externalMedia.value = consent.categories.externalMedia;
  }
);

function saveSelection() {
  savePreferences({ externalMedia: externalMedia.value });
}
</script>

<template>
  <Transition
    enter-active-class="transition duration-300 ease-out"
    enter-from-class="opacity-0 translate-y-8"
    enter-to-class="opacity-100 translate-y-0"
    leave-active-class="transition duration-200 ease-in"
    leave-from-class="opacity-100 translate-y-0"
    leave-to-class="opacity-0 translate-y-8"
  >
    <div
      v-if="consent.bannerOpen"
      class="fixed inset-x-0 bottom-0 z-[60] px-4 pb-4 sm:px-6 sm:pb-6"
      role="dialog"
      aria-modal="false"
      aria-labelledby="cookie-banner-title"
      aria-describedby="cookie-banner-desc"
    >
      <div
        class="mx-auto max-w-3xl rounded-2xl border border-sand-200 bg-white p-5 shadow-2xl shadow-sand-900/10 sm:p-6"
      >
        <!-- Standardansicht -->
        <div v-if="!consent.settingsOpen">
          <div class="flex items-start gap-3">
            <div
              class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-gold-100 text-gold-600"
            >
              <Cookie class="h-5 w-5" aria-hidden="true" />
            </div>
            <div>
              <h2
                id="cookie-banner-title"
                class="text-lg font-semibold text-sand-900"
              >
                Datenschutz &amp; Cookies
              </h2>
              <p
                id="cookie-banner-desc"
                class="mt-1 text-sm leading-relaxed text-sand-600"
              >
                Wir verwenden notwendige Cookies, damit diese Website funktioniert.
                Optional binden wir externe Dienste und Inhalte ein, die Daten an
                Drittanbieter übertragen können. Sie entscheiden, was Sie zulassen.
                Mehr dazu in unserer
                <a
                  href="/datenschutz"
                  class="font-medium text-gold-600 underline underline-offset-2 hover:text-gold-700"
                  >Datenschutzerklärung</a
                >.
              </p>
            </div>
          </div>

          <div
            class="mt-5 flex flex-col gap-2 sm:flex-row sm:flex-wrap sm:justify-end"
          >
            <button
              type="button"
              class="order-3 rounded-lg px-5 py-2.5 text-sm font-medium text-sand-600 transition-colors hover:bg-sand-100 sm:order-1 sm:mr-auto"
              @click="openSettings"
            >
              Einstellungen
            </button>
            <button
              type="button"
              class="order-2 rounded-lg border border-sand-300 bg-white px-5 py-2.5 text-sm font-semibold text-sand-800 transition-colors hover:bg-sand-100"
              @click="acceptEssentialOnly"
            >
              Nur notwendige
            </button>
            <button
              type="button"
              class="order-1 rounded-lg bg-gold-500 px-5 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-gold-600 sm:order-3"
              @click="acceptAll"
            >
              Alle akzeptieren
            </button>
          </div>
        </div>

        <!-- Einstellungen -->
        <div v-else>
          <div class="flex items-start justify-between gap-3">
            <h2 class="text-lg font-semibold text-sand-900">
              Cookie-Einstellungen
            </h2>
            <button
              type="button"
              class="-mr-1 -mt-1 rounded-lg p-1.5 text-sand-500 transition-colors hover:bg-sand-100 hover:text-sand-700"
              aria-label="Einstellungen schließen"
              @click="closeSettings"
            >
              <X class="h-5 w-5" aria-hidden="true" />
            </button>
          </div>

          <div class="mt-4 space-y-3">
            <!-- Notwendig -->
            <div
              class="flex items-start justify-between gap-4 rounded-xl border border-sand-200 bg-sand-50 p-4"
            >
              <div>
                <p class="text-sm font-semibold text-sand-900">Notwendig</p>
                <p class="mt-0.5 text-sm text-sand-600">
                  Erforderlich für den Betrieb der Website (z. B. Sicherheit,
                  Formulare). Immer aktiv.
                </p>
              </div>
              <span
                class="mt-0.5 shrink-0 rounded-full bg-sand-200 px-3 py-1 text-xs font-medium text-sand-600"
              >
                Aktiv
              </span>
            </div>

            <!-- Externe Medien -->
            <label
              class="flex cursor-pointer items-start justify-between gap-4 rounded-xl border border-sand-200 p-4 transition-colors hover:border-sand-300"
            >
              <div>
                <p class="text-sm font-semibold text-sand-900">Externe Medien</p>
                <p class="mt-0.5 text-sm text-sand-600">
                  Erlaubt das Einbinden externer Dienste und Inhalte. Dabei können
                  Daten an Drittanbieter übertragen werden.
                </p>
              </div>
              <input
                v-model="externalMedia"
                type="checkbox"
                class="peer sr-only"
              />
              <span
                class="relative mt-0.5 h-6 w-11 shrink-0 rounded-full bg-sand-300 transition-colors after:absolute after:left-0.5 after:top-0.5 after:h-5 after:w-5 after:rounded-full after:bg-white after:shadow after:transition-transform peer-checked:bg-gold-500 peer-checked:after:translate-x-5"
                aria-hidden="true"
              />
            </label>
          </div>

          <div class="mt-5 flex flex-col gap-2 sm:flex-row sm:justify-end">
            <button
              type="button"
              class="rounded-lg border border-sand-300 bg-white px-5 py-2.5 text-sm font-semibold text-sand-800 transition-colors hover:bg-sand-100"
              @click="saveSelection"
            >
              Auswahl speichern
            </button>
            <button
              type="button"
              class="rounded-lg bg-gold-500 px-5 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-gold-600"
              @click="acceptAll"
            >
              Alle akzeptieren
            </button>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>
