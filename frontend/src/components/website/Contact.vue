<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, reactive, ref } from "vue";
import { CheckCircle, Clock, Mail, MapPin, Phone, Send } from "@lucide/vue";
import type { Map as LeafletMap } from "leaflet";
import { websiteApi } from "@/api/client";
import type { ApiErrorResponse, PriceCategoryGroup, TreatmentItem } from "@/types";
import { contact } from "@/content";

const DEFAULT_STUDIO_LOCATION: [number, number] = [53.1428031, 8.2226412];

function parseStudioLocation(value: unknown): [number, number] {
  if (typeof value !== "string") return DEFAULT_STUDIO_LOCATION;
  const parts = value.split(",");
  const lat = Number.parseFloat((parts[0] ?? "").trim());
  const lng = Number.parseFloat((parts[1] ?? "").trim());
  return Number.isFinite(lat) && Number.isFinite(lng)
    ? [lat, lng]
    : DEFAULT_STUDIO_LOCATION;
}

const STUDIO_LOCATION: [number, number] = parseStudioLocation(
  import.meta.env.VITE_STUDIO_LOCATION
);

const mapContainer = ref<HTMLElement | null>(null);
let map: LeafletMap | null = null;

async function initMap() {
  if (!mapContainer.value || map || import.meta.env.SSR) return;

  const { default: L } = await import("leaflet");
  await import("leaflet/dist/leaflet.css");

  const [markerIcon, markerIcon2x, markerShadow] = await Promise.all([
    import("leaflet/dist/images/marker-icon.png"),
    import("leaflet/dist/images/marker-icon-2x.png"),
    import("leaflet/dist/images/marker-shadow.png"),
  ]);

  map = L.map(mapContainer.value, {
    center: STUDIO_LOCATION,
    zoom: 16,
    scrollWheelZoom: false,
  });

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19,
  }).addTo(map);

  const icon = L.icon({
    iconUrl: markerIcon.default,
    iconRetinaUrl: markerIcon2x.default,
    shadowUrl: markerShadow.default,
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41],
  });

  L.marker(STUDIO_LOCATION, { icon })
    .addTo(map)
    .bindPopup(`${contact.addressLine1}<br>${contact.addressLine2}`);
}

const formData = reactive({
  name: "",
  email: "",
  phone: "",
  treatmentId: "",
  message: "",
});

const treatments = ref<TreatmentItem[]>([]);
const isLoadingTreatments = ref(true);
const treatmentsError = ref<string | null>(null);
const isSubmitting = ref(false);
const submitted = ref(false);
const submitError = ref<string | null>(null);

function groupByCategory(items: TreatmentItem[]): PriceCategoryGroup[] {
  const map = new Map<string, PriceCategoryGroup["services"]>();

  for (const item of items) {
    const categoryName = item.category.name;
    const list = map.get(categoryName) ?? [];
    list.push({
      id: item.id,
      name: item.name,
      price: item.price ?? "",
    });
    map.set(categoryName, list);
  }

  return Array.from(map.entries()).map(([category, services]) => ({
    category,
    services,
  }));
}

const treatmentGroups = computed(() => groupByCategory(treatments.value));

async function loadTreatments() {
  isLoadingTreatments.value = true;
  treatmentsError.value = null;

  try {
    const { data } = await websiteApi.getTreatments();
    treatments.value = data;
  } catch {
    treatmentsError.value =
      "Behandlungen konnten nicht geladen werden. Bitte versuchen Sie es später erneut.";
  } finally {
    isLoadingTreatments.value = false;
  }
}

function resetForm() {
  formData.name = "";
  formData.email = "";
  formData.phone = "";
  formData.treatmentId = "";
  formData.message = "";
}

async function handleSubmit() {
  if (isSubmitting.value) return;

  isSubmitting.value = true;
  submitError.value = null;

  try {
    await websiteApi.sendContactForm({
      name: formData.name.trim(),
      email: formData.email.trim(),
      phone: formData.phone.trim(),
      treatment_id: Number(formData.treatmentId),
      message: formData.message.trim() || undefined,
    });

    submitted.value = true;
    resetForm();
    setTimeout(() => {
      submitted.value = false;
    }, 5000);
  } catch (error) {
    const apiError = error as ApiErrorResponse;
    submitError.value =
      apiError.message ??
      "Ihre Anfrage konnte nicht gesendet werden. Bitte versuchen Sie es später erneut.";
  } finally {
    isSubmitting.value = false;
  }
}

onMounted(() => {
  loadTreatments();
  void initMap();
});

onBeforeUnmount(() => {
  map?.remove();
  map = null;
});
</script>

<template>
  <section
    id="contact"
    class="py-24 bg-white scroll-mt-nav"
    aria-labelledby="contact-heading"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <div class="inline-block">
          <span class="text-gold-500 font-semibold text-sm uppercase tracking-wider">
            Kontakt
          </span>
          <div class="h-1 w-16 bg-gold-400 mt-2 rounded-full mx-auto" />
        </div>

        <h2
          id="contact-heading"
          class="text-4xl md:text-5xl font-bold text-sand-900 mt-4 mb-6"
        >
          Jetzt <span class="text-gold-500">Termin buchen</span>
        </h2>

        <p class="text-lg text-sand-600 max-w-2xl mx-auto">
          Vereinbaren Sie noch heute Ihren persönlichen Termin und lassen Sie sich von uns
          verwöhnen.
        </p>
      </div>

      <div class="grid md:grid-cols-2 gap-12">
        <div class="space-y-8">
          <div
            class="bg-gradient-to-br from-gold-50 to-sand-50 rounded-2xl p-8 border border-gold-200"
          >
            <h3 class="text-2xl font-bold text-sand-900 mb-6">Kontaktinformationen</h3>

            <div class="space-y-6">
              <div class="flex items-start gap-4">
                <div
                  class="w-12 h-12 bg-gold-500 rounded-xl flex items-center justify-center shrink-0"
                >
                  <MapPin class="w-6 h-6 text-white" aria-hidden="true" />
                </div>
                <div>
                  <h4 class="font-semibold text-sand-900 mb-1">Adresse</h4>
                  <p class="text-sand-600">{{ contact.addressLine1 }}</p>
                  <p class="text-sand-600">{{ contact.addressLine2 }}</p>
                </div>
              </div>

              <div class="flex items-start gap-4">
                <div
                  class="w-12 h-12 bg-gold-500 rounded-xl flex items-center justify-center shrink-0"
                >
                  <Phone class="w-6 h-6 text-white" aria-hidden="true" />
                </div>
                <div>
                  <h4 class="font-semibold text-sand-900 mb-1">Telefon</h4>
                  <a :href="contact.phoneHref" class="text-gold-600 hover:text-gold-700">
                    {{ contact.phone }}
                  </a>
                </div>
              </div>

              <div class="flex items-start gap-4">
                <div
                  class="w-12 h-12 bg-gold-500 rounded-xl flex items-center justify-center shrink-0"
                >
                  <Mail class="w-6 h-6 text-white" aria-hidden="true" />
                </div>
                <div>
                  <h4 class="font-semibold text-sand-900 mb-1">E-Mail</h4>
                  <a :href="contact.emailHref" class="text-gold-600 hover:text-gold-700">
                    {{ contact.email }}
                  </a>
                </div>
              </div>

              <div class="flex items-start gap-4">
                <div
                  class="w-12 h-12 bg-gold-500 rounded-xl flex items-center justify-center shrink-0"
                >
                  <Clock class="w-6 h-6 text-white" aria-hidden="true" />
                </div>
                <div>
                  <h4 class="font-semibold text-sand-900 mb-1">Öffnungszeiten</h4>
                  <p class="text-sand-600">{{ contact.hoursWeekdays }}</p>
                  <p class="text-sand-600">{{ contact.hoursNote }}</p>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-sand-100 rounded-2xl overflow-hidden">
            <div
              ref="mapContainer"
              class="h-[300px] w-full"
              role="application"
              aria-label="Standortkarte Schönheitsecke Oldenburg"
            />
          </div>
        </div>

        <div class="bg-sand-50 rounded-2xl p-8 border border-sand-200">
          <h3 class="text-2xl font-bold text-sand-900 mb-6">Terminanfrage</h3>

          <div
            v-if="submitted"
            class="flex flex-col items-center justify-center py-12 text-center"
          >
            <CheckCircle class="w-16 h-16 text-gold-500 mb-4" aria-hidden="true" />
            <h4 class="text-2xl font-bold text-sand-900 mb-2">Vielen Dank!</h4>
            <p class="text-sand-600">
              Ihre Nachricht wurde erfolgreich gesendet. Wir melden uns schnellstmöglich
              bei Ihnen.
            </p>
          </div>

          <form v-else class="space-y-6" @submit.prevent="handleSubmit">
            <div
              v-if="submitError"
              class="rounded-lg bg-red-50 text-red-700 px-4 py-3 border border-red-200 text-sm"
              role="alert"
            >
              {{ submitError }}
            </div>

            <div>
              <label
                for="contact-name"
                class="block text-sm font-semibold text-sand-900 mb-2"
              >
                Name *
              </label>
              <input
                id="contact-name"
                v-model="formData.name"
                type="text"
                name="name"
                required
                autocomplete="name"
                class="w-full px-4 py-3 rounded-lg border border-sand-300 bg-white focus:ring-2 focus:ring-gold-500 focus:border-transparent outline-none transition-all"
                placeholder="Ihr Name"
              />
            </div>

            <div>
              <label
                for="contact-email"
                class="block text-sm font-semibold text-sand-900 mb-2"
              >
                E-Mail *
              </label>
              <input
                id="contact-email"
                v-model="formData.email"
                type="email"
                name="email"
                required
                autocomplete="email"
                class="w-full px-4 py-3 rounded-lg border border-sand-300 bg-white focus:ring-2 focus:ring-gold-500 focus:border-transparent outline-none transition-all"
                placeholder="ihre@email.de"
              />
            </div>

            <div>
              <label
                for="contact-phone"
                class="block text-sm font-semibold text-sand-900 mb-2"
              >
                Telefon *
              </label>
              <input
                id="contact-phone"
                v-model="formData.phone"
                type="tel"
                name="phone"
                required
                autocomplete="tel"
                class="w-full px-4 py-3 rounded-lg border border-sand-300 bg-white focus:ring-2 focus:ring-gold-500 focus:border-transparent outline-none transition-all"
                placeholder="+49 123 456789"
              />
            </div>

            <div>
              <label
                for="contact-treatment"
                class="block text-sm font-semibold text-sand-900 mb-2"
              >
                Gewünschte Behandlung *
              </label>

              <div
                v-if="isLoadingTreatments"
                class="w-full px-4 py-3 rounded-lg border border-sand-300 bg-white text-sand-500"
              >
                Behandlungen werden geladen…
              </div>

              <div
                v-else-if="treatmentsError"
                class="rounded-lg bg-red-50 text-red-700 px-4 py-3 border border-red-200 text-sm"
              >
                {{ treatmentsError }}
              </div>

              <select
                v-else
                id="contact-treatment"
                v-model="formData.treatmentId"
                name="treatment_id"
                required
                class="w-full px-4 py-3 rounded-lg border border-sand-300 bg-white text-sand-900 focus:ring-2 focus:ring-gold-500 focus:border-transparent outline-none transition-all"
                :class="{ 'text-sand-500': !formData.treatmentId }"
              >
                <option value="" disabled>Bitte wählen…</option>
                <optgroup
                  v-for="group in treatmentGroups"
                  :key="group.category"
                  :label="group.category"
                >
                  <option
                    v-for="treatment in group.services"
                    :key="treatment.id"
                    :value="String(treatment.id)"
                  >
                    {{ treatment.name }}
                  </option>
                </optgroup>
              </select>
            </div>

            <div>
              <label
                for="contact-message"
                class="block text-sm font-semibold text-sand-900 mb-2"
              >
                Nachricht
              </label>
              <textarea
                id="contact-message"
                v-model="formData.message"
                name="message"
                rows="4"
                class="w-full px-4 py-3 rounded-lg border border-sand-300 bg-white focus:ring-2 focus:ring-gold-500 focus:border-transparent outline-none transition-all resize-none"
                placeholder="Ihre Nachricht oder Terminwünsche…"
              />
            </div>

            <button
              type="submit"
              :disabled="isSubmitting || isLoadingTreatments || !!treatmentsError"
              class="w-full bg-gold-500 text-white px-8 py-4 rounded-lg hover:bg-gold-600 transition-all duration-200 shadow-lg shadow-gold-200 hover:shadow-xl hover:shadow-gold-300 flex items-center justify-center gap-2 font-semibold disabled:opacity-60 disabled:cursor-not-allowed border-0"
            >
              <span>{{ isSubmitting ? "Wird gesendet…" : "Anfrage senden" }}</span>
              <Send class="w-5 h-5 shrink-0" aria-hidden="true" />
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Leaflet nutzt intern hohe z-index-Werte – per Stacking-Context kapseln,
   damit Navbar und Cookie-Banner darüber bleiben. */
:deep(.leaflet-container) {
  position: relative;
  z-index: 0;
  font: inherit;
}
</style>
