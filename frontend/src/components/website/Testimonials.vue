<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { Quote, Star } from "@lucide/vue";
import { websiteApi } from "@/api/client";
import { googleReviews } from "@/content";
import type { TestimonialItem } from "@/types";

const DISPLAY_COUNT = 6;

const testimonials = ref<TestimonialItem[]>([]);
const isLoading = ref(true);
const errorMessage = ref<string | null>(null);

const reviewCountLabel = computed(() => {
  const count = googleReviews.count;
  if (count === 1) return "aus 1 Google-Bewertung";
  return `aus ${count} Google-Bewertungen`;
});

const headerRatingLabel = computed(() =>
  googleReviews.rating.toLocaleString("de-DE", {
    minimumFractionDigits: 1,
    maximumFractionDigits: 1,
  })
);

function starCount(rating: number): number {
  return Math.max(1, Math.min(5, Math.round(rating)));
}

async function loadTestimonials() {
  isLoading.value = true;
  errorMessage.value = null;

  try {
    const { data } = await websiteApi.getTestimonials();
    testimonials.value = data.slice(0, DISPLAY_COUNT);
  } catch {
    errorMessage.value =
      "Bewertungen konnten nicht geladen werden. Bitte versuchen Sie es später erneut.";
  } finally {
    isLoading.value = false;
  }
}

onMounted(loadTestimonials);
</script>

<template>
  <section
    id="testimonials"
    class="py-24 bg-gradient-to-b from-white to-sand-50 scroll-mt-nav"
    aria-labelledby="testimonials-heading"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <div class="inline-block">
          <span class="text-gold-500 font-semibold text-sm uppercase tracking-wider">
            Bewertungen
          </span>
          <div class="h-1 w-16 bg-gold-400 mt-2 rounded-full mx-auto" />
        </div>

        <h2
          id="testimonials-heading"
          class="text-4xl md:text-5xl font-bold text-sand-900 mt-4 mb-6"
        >
          Was unsere <span class="text-gold-500">Kunden sagen</span>
        </h2>

        <div class="flex flex-wrap items-center justify-center gap-2 mb-4">
          <Star
            v-for="i in 5"
            :key="`header-star-${i}`"
            class="w-6 h-6 fill-gold-500 text-gold-500 shrink-0"
            aria-hidden="true"
          />
          <span class="text-lg font-semibold text-sand-900 ml-2">{{ headerRatingLabel }}</span>
          <span class="text-sand-600">{{ reviewCountLabel }}</span>
        </div>
      </div>

      <div v-if="isLoading" class="text-center text-sand-600 py-12">
        Bewertungen werden geladen…
      </div>

      <div
        v-else-if="errorMessage"
        class="text-center bg-red-50 text-red-700 rounded-2xl p-8 border border-red-200"
      >
        {{ errorMessage }}
      </div>

      <div
        v-else-if="testimonials.length === 0"
        class="text-center text-sand-600 py-12"
      >
        Noch keine Bewertungen vorhanden.
      </div>

      <div v-else class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <article
          v-for="testimonial in testimonials"
          :key="testimonial.id"
          class="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-shadow duration-300 border border-sand-100"
        >
          <Quote class="w-10 h-10 text-gold-400 mb-4 shrink-0" aria-hidden="true" />

          <div class="flex gap-1 mb-4">
            <Star
              v-for="i in starCount(testimonial.rating)"
              :key="`${testimonial.id}-star-${i}`"
              class="w-5 h-5 fill-gold-500 text-gold-500 shrink-0"
              aria-hidden="true"
            />
          </div>

          <p class="text-sand-700 leading-relaxed mb-6">{{ testimonial.text }}</p>

          <div class="pt-4 border-t border-sand-100">
            <p class="font-semibold text-sand-900">{{ testimonial.full_name }}</p>
          </div>
        </article>
      </div>

      <div class="mt-12 text-center">
        <p class="text-sand-600 mb-4">Folgen Sie uns für mehr Inspiration</p>
        <div class="flex flex-wrap items-center justify-center gap-4">
          <a
            href="https://www.instagram.com/olga.eisner/"
            target="_blank"
            rel="noopener noreferrer"
            class="flex items-center gap-2 bg-white px-6 py-3 rounded-lg hover:bg-sand-50 transition-colors border border-sand-200"
          >
            <svg
              class="w-5 h-5 text-gold-600 shrink-0"
              fill="currentColor"
              viewBox="0 0 24 24"
              aria-hidden="true"
            >
              <path
                d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"
              />
            </svg>
            <span class="font-semibold text-sand-900">Instagram</span>
          </a>
          <a
            href="https://www.facebook.com/evgeny.eisner/"
            target="_blank"
            rel="noopener noreferrer"
            class="flex items-center gap-2 bg-white px-6 py-3 rounded-lg hover:bg-sand-50 transition-colors border border-sand-200"
          >
            <svg
              class="w-5 h-5 text-gold-600 shrink-0"
              fill="currentColor"
              viewBox="0 0 24 24"
              aria-hidden="true"
            >
              <path
                d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"
              />
            </svg>
            <span class="font-semibold text-sand-900">Facebook</span>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>
