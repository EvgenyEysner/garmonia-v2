<script setup lang="ts">
import { ArrowRight, Sparkles } from "@lucide/vue";
import type { MonthlyOfferItem } from "@/types";
import { onMounted, ref } from "vue";
import { websiteApi } from "@/api/client.ts";
import { resolveMediaUrl } from "@/utils.ts";

const scrollToContact = () => {
  document.querySelector("#contact")?.scrollIntoView({ behavior: "smooth" });
};

const offers = ref<MonthlyOfferItem[]>([]);
const isLoading = ref(true);
const errorMessage = ref<string | null>(null);

async function MonthlyOffer() {
  isLoading.value = true;
  errorMessage.value = null;

  try {
    const { data } = await websiteApi.getMonthlyOffer();
    offers.value = data;
    console.log("Data: ", offers.value);
  } catch {
    errorMessage.value =
      "Monatsangebot konnte nicht geladen werden. Bitte versuchen Sie es später erneut.";
  } finally {
    isLoading.value = false;
  }
}

onMounted(MonthlyOffer);
</script>

<template>
  <section id="monthly-offer" class="py-24 bg-white scroll-mt-nav">
    <div v-if="isLoading" class="text-center text-sand-600 py-12">
      Monatsangebote werden geladen…
    </div>
    <div
      v-else-if="errorMessage"
      class="text-center bg-red-50 text-red-700 rounded-2xl p-8 border border-red-200"
    >
      {{ errorMessage }}
    </div>

    <div v-else-if="offers.length === 0" class="text-center text-sand-600 py-12">
      Aktuell sind keine Angebote vorhanden.
    </div>
    <div
      v-else
      class="mt-16 bg-gradient-to-br from-gold-400 to-gold-600 rounded-3xl p-8 md:p-12 text-center text-white shadow-xl"
    >
      <div class="max-w-3xl mx-auto" v-for="offer in offers" :key="offer.id">
        <Sparkles class="w-12 h-12 mx-auto mb-4" aria-hidden="true" />
        <h3 class="text-3xl font-bold mb-4">Monatsangebot im Juni</h3>
        <p class="text-xl mb-2">{{ offer.title }}</p>
        <div class="flex items-center justify-center gap-4 mb-6">
          <span class="text-2xl line-through opacity-75"
            >{{ offer.treatment.price }}€</span
          >
          <span class="text-4xl font-bold">{{ offer.price }}€</span>
        </div>
        <div class="aspect-square overflow-hidden">
          <img
            :src="resolveMediaUrl(offer.image)"
            :alt="offer.title"
            loading="lazy"
            class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
          />
        </div>
        <p class="text-lg opacity-90 mb-6">
          {{ offer.description }}
        </p>
        <a
          href="#contact"
          class="inline-flex items-center justify-center gap-2 bg-white text-gold-600 px-8 py-4 rounded-xl font-semibold hover:bg-sand-50 transition-colors duration-200"
          @click.prevent="scrollToContact"
        >
          <span>Jetzt Termin sichern</span>
          <ArrowRight class="w-5 h-5 shrink-0" aria-hidden="true" />
        </a>
      </div>
    </div>
  </section>
</template>
