<script setup lang="ts">
import { onMounted, ref } from "vue";
import { websiteApi } from "@/api/client";
import type { GalleryItem } from "@/types";
import { resolveMediaUrl } from "@/utils";

const images = ref<GalleryItem[]>([]);
const isLoading = ref(true);
const errorMessage = ref<string | null>(null);

async function loadGallery() {
  isLoading.value = true;
  errorMessage.value = null;

  try {
    const { data } = await websiteApi.getGalleryImages();
    images.value = data;
  } catch {
    errorMessage.value =
      "Galerie konnte nicht geladen werden. Bitte versuchen Sie es später erneut.";
  } finally {
    isLoading.value = false;
  }
}

onMounted(loadGallery);
</script>

<template>
  <section
    id="gallery"
    class="py-24 bg-white scroll-mt-nav"
    aria-labelledby="gallery-heading"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <div class="inline-block">
          <span class="text-gold-500 font-semibold text-sm uppercase tracking-wider">
            Galerie
          </span>
          <div class="h-1 w-16 bg-gold-400 mt-2 rounded-full mx-auto" />
        </div>

        <h2
          id="gallery-heading"
          class="text-4xl md:text-5xl font-bold text-sand-900 mt-4 mb-6"
        >
          Einblicke in unser <span class="text-gold-500">Studio</span>
        </h2>

        <p class="text-lg text-sand-600 max-w-2xl mx-auto">
          Erleben Sie die Atmosphäre unseres exklusiven Beauty-Studios und lassen Sie sich
          inspirieren.
        </p>
      </div>

      <div v-if="isLoading" class="text-center text-sand-600 py-12">
        Galerie wird geladen…
      </div>

      <div
        v-else-if="errorMessage"
        class="text-center bg-red-50 text-red-700 rounded-2xl p-8 border border-red-200"
      >
        {{ errorMessage }}
      </div>

      <div v-else-if="images.length === 0" class="text-center text-sand-600 py-12">
        Noch keine Bilder in der Galerie.
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <article
          v-for="image in images"
          :key="image.id"
          class="group relative overflow-hidden rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300"
        >
          <div class="aspect-square overflow-hidden">
            <img
              :src="resolveMediaUrl(image.image)"
              :alt="image.description"
              loading="lazy"
              class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
            />
          </div>
          <div
            class="absolute inset-0 bg-gradient-to-t from-sand-900/80 via-sand-900/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"
          >
            <div class="absolute bottom-0 left-0 right-0 p-6">
              <h3 class="text-xl font-semibold text-white">
                {{ image.description.toUpperCase() }}
              </h3>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>
