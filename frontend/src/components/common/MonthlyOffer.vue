<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { ArrowRight, Sparkles, Tag } from "@lucide/vue";
import { websiteApi } from "@/api/client";
import type { MonthlyOfferItem } from "@/types";
import { resolveMediaUrl, scrollToContact } from "@/utils";

const offers = ref<MonthlyOfferItem[]>([]);
const isLoading = ref(true);
const errorMessage = ref<string | null>(null);

const monthLabel = computed(() => {
  const name = new Intl.DateTimeFormat("de-DE", { month: "long" }).format(new Date());
  return name.charAt(0).toUpperCase() + name.slice(1);
});

const activeOffer = computed(() => offers.value.find((offer) => offer.active) ?? null);

function formatPrice(price: string | null | undefined): string {
  if (!price) return "—";
  const trimmed = price.trim();
  if (trimmed.includes("€")) return trimmed;

  const value = Number.parseFloat(trimmed.replace(",", "."));
  if (Number.isNaN(value)) return `${trimmed}€`;

  return Number.isInteger(value) ? `${value}€` : `${value.toFixed(2).replace(".", ",")}€`;
}

async function loadMonthlyOffer() {
  isLoading.value = true;
  errorMessage.value = null;

  try {
    const { data } = await websiteApi.getMonthlyOffer();
    offers.value = data;
  } catch {
    errorMessage.value =
      "Monatsangebot konnte nicht geladen werden. Bitte versuchen Sie es später erneut.";
  } finally {
    isLoading.value = false;
  }
}

onMounted(loadMonthlyOffer);
</script>

<template>
  <div v-if="isLoading" class="mt-16 text-center text-sand-600 py-12">
    Monatsangebot wird geladen…
  </div>

  <div
    v-else-if="errorMessage"
    class="mt-16 text-center bg-red-50 text-red-700 rounded-2xl p-8 border border-red-200"
    role="alert"
  >
    {{ errorMessage }}
  </div>

  <article
    v-else-if="activeOffer"
    id="monthly-offer"
    class="mt-16 scroll-mt-nav overflow-hidden rounded-3xl bg-gradient-to-br from-gold-400 via-gold-500 to-gold-600 shadow-xl shadow-gold-200/60 ring-1 ring-gold-300/40"
    aria-labelledby="monthly-offer-heading"
  >
    <div class="grid lg:grid-cols-2">
      <!-- Inhalt -->
      <div class="relative flex flex-col justify-center p-8 md:p-10 lg:p-12 text-white">
        <div
          class="pointer-events-none absolute -top-16 -left-16 h-48 w-48 rounded-full bg-white/10 blur-3xl"
          aria-hidden="true"
        />
        <div
          class="pointer-events-none absolute -bottom-12 right-0 h-40 w-40 rounded-full bg-gold-300/30 blur-2xl"
          aria-hidden="true"
        />

        <div
          class="relative inline-flex w-fit items-center gap-2 rounded-full bg-white/15 px-4 py-1.5 text-sm font-semibold backdrop-blur-sm border border-white/20 mb-6"
        >
          <Sparkles class="h-4 w-4 shrink-0" aria-hidden="true" />
          <span>Monatsangebot · {{ monthLabel }}</span>
        </div>

        <h3
          id="monthly-offer-heading"
          class="relative text-3xl md:text-4xl font-bold leading-tight mb-3"
        >
          {{ activeOffer.title }}
        </h3>

        <p class="relative text-gold-50/90 font-medium mb-4">
          {{ activeOffer.treatment.name }}
          <span class="text-white/60">·</span>
          {{ activeOffer.treatment.category.name }}
        </p>

        <p class="relative text-lg text-white/90 leading-relaxed mb-8 max-w-xl">
          {{ activeOffer.description }}
        </p>

        <div class="relative flex flex-wrap items-end gap-4 mb-8">
          <div class="flex items-baseline gap-3">
            <span
              v-if="activeOffer.treatment.price"
              class="text-xl text-white/70 line-through decoration-white/50"
            >
              {{ formatPrice(activeOffer.treatment.price) }}
            </span>
            <span class="text-4xl md:text-5xl font-bold tracking-tight">
              {{ formatPrice(activeOffer.price) }}
            </span>
          </div>
          <span
            class="inline-flex items-center gap-1.5 rounded-full bg-white text-gold-700 px-3 py-1 text-sm font-bold shadow-sm"
          >
            <Tag class="h-3.5 w-3.5 shrink-0" aria-hidden="true" />
            Angebot
          </span>
        </div>

        <a
          href="#contact"
          class="relative inline-flex w-fit items-center justify-center gap-2 rounded-xl bg-white px-8 py-4 font-semibold text-gold-700 shadow-lg shadow-gold-900/10 transition-all duration-200 hover:bg-sand-50 hover:shadow-xl hover:-translate-y-0.5"
          @click.prevent="scrollToContact"
        >
          <span>Jetzt Termin sichern</span>
          <ArrowRight class="h-5 w-5 shrink-0" aria-hidden="true" />
        </a>
      </div>

      <!-- Bild -->
      <div class="relative min-h-[280px] lg:min-h-full">
        <img
          :src="resolveMediaUrl(activeOffer.image)"
          :alt="activeOffer.title"
          loading="lazy"
          class="absolute inset-0 h-full w-full object-cover"
        />
        <div
          class="absolute inset-0 bg-gradient-to-t from-gold-900/50 via-transparent to-transparent lg:bg-gradient-to-l lg:from-gold-600/80 lg:via-gold-500/20 lg:to-transparent"
          aria-hidden="true"
        />
      </div>
    </div>
  </article>
</template>
