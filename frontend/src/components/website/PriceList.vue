<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { Check } from "@lucide/vue";
import { websiteApi } from "@/api/client";
import type { PriceCategoryGroup, TreatmentItem } from "@/types";

const treatments = ref<TreatmentItem[]>([]);
const isLoading = ref(true);
const errorMessage = ref<string | null>(null);

function formatPrice(price: string | null): string {
  if (!price) return "—";
  return price.includes("€") ? price : `${price}€`;
}

function groupByCategory(items: TreatmentItem[]): PriceCategoryGroup[] {
  const map = new Map<string, PriceCategoryGroup["services"]>();

  for (const item of items) {
    const categoryName = item.category.name;
    const list = map.get(categoryName) ?? [];
    list.push({
      id: item.id,
      name: item.name,
      price: formatPrice(item.price),
    });
    map.set(categoryName, list);
  }

  return Array.from(map.entries()).map(([category, services]) => ({
    category,
    services,
  }));
}

const priceCategories = computed(() => groupByCategory(treatments.value));

async function loadTreatments() {
  isLoading.value = true;
  errorMessage.value = null;

  try {
    const { data } = await websiteApi.getTreatments();
    treatments.value = data;
  } catch {
    errorMessage.value =
      "Preisliste konnte nicht geladen werden. Bitte versuchen Sie es später erneut.";
  } finally {
    isLoading.value = false;
  }
}

const scrollToContact = () => {
  document.querySelector("#contact")?.scrollIntoView({ behavior: "smooth" });
};

onMounted(loadTreatments);
</script>

<template>
  <section
    id="pricing"
    class="py-24 bg-gradient-to-b from-sand-50 to-white scroll-mt-nav"
    aria-labelledby="pricing-heading"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <div class="inline-block">
          <span class="text-gold-500 font-semibold text-sm uppercase tracking-wider">
            Preisliste
          </span>
          <div class="h-1 w-16 bg-gold-400 mt-2 rounded-full mx-auto" />
        </div>

        <h2
          id="pricing-heading"
          class="text-4xl md:text-5xl font-bold text-sand-900 mt-4 mb-6"
        >
          Transparente <span class="text-gold-500">Preise</span>
        </h2>

        <p class="text-lg text-sand-600 max-w-2xl mx-auto">
          Alle Preise auf einen Blick – keine versteckten Kosten
        </p>
      </div>

      <div v-if="isLoading" class="text-center text-sand-600 py-12">
        Preisliste wird geladen…
      </div>

      <div
        v-else-if="errorMessage"
        class="text-center bg-red-50 text-red-700 rounded-2xl p-8 border border-red-200"
      >
        {{ errorMessage }}
      </div>

      <div
        v-else-if="priceCategories.length === 0"
        class="text-center text-sand-600 py-12"
      >
        Aktuell sind keine Behandlungen hinterlegt.
      </div>

      <div v-else class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div
          v-for="category in priceCategories"
          :key="category.category"
          class="bg-white rounded-2xl p-8 shadow-lg border border-sand-100 hover:border-gold-200 transition-all duration-300"
        >
          <h3
            class="text-2xl font-bold text-sand-900 mb-6 pb-4 border-b-2 border-gold-400"
          >
            {{ category.category }}
          </h3>

          <ul class="space-y-4">
            <li
              v-for="service in category.services"
              :key="service.id"
              class="flex items-center justify-between gap-4"
            >
              <div class="flex items-start gap-2 flex-1 min-w-0">
                <Check
                  class="w-4 h-4 text-gold-500 shrink-0 mt-1"
                  aria-hidden="true"
                />
                <span class="text-sand-700">{{ service.name }}</span>
              </div>
              <span class="font-bold text-gold-600 shrink-0">{{ service.price }}</span>
            </li>
          </ul>
        </div>
      </div>

      <div
        class="mt-12 text-center bg-gold-50 rounded-2xl p-8 border border-gold-200"
      >
        <p class="text-sand-700 mb-4">
          <span class="font-semibold">Hinweis:</span> Alle Preise verstehen sich als
          Richtwerte. Der genaue Preis wird nach individueller Beratung festgelegt.
        </p>
        <a
          href="#contact"
          class="inline-flex items-center justify-center gap-2 bg-gold-500 text-white px-6 py-3 rounded-lg hover:bg-gold-600 transition-colors font-semibold"
          @click.prevent="scrollToContact"
        >
          Kostenlose Beratung vereinbaren
        </a>
      </div>
    </div>
  </section>
</template>
