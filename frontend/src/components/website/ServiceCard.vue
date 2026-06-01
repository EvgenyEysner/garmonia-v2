<script setup lang="ts">
defineProps<{
  title: string;
  description: string;
  imageSrc: string;
  imageAlt: string;
}>();
</script>

<template>
  <article
    class="group relative flex flex-col items-center text-center bg-white rounded-2xl shadow-soft px-6 pb-8 pt-20 h-full mx-2 transition-shadow duration-300 hover:shadow-medium"
  >
    <div
      class="absolute -top-14 left-1/2 -translate-x-1/2 shrink-0 rounded-full overflow-hidden ring-4 ring-white shadow-medium transition-shadow group-hover:ring-gold-100"
    >
      <img
        :src="imageSrc"
        :alt="imageAlt"
        class="w-28 h-28 sm:w-32 sm:h-32 object-cover rounded-full"
        loading="lazy"
        width="128"
        height="128"
      />
    </div>
    <h3 class="text-lg sm:text-xl font-bold text-sand-800 mb-3 font-serif mt-2">
      {{ title }}
    </h3>
    <p class="text-sand-500 leading-relaxed text-sm sm:text-base font-sans">
      {{ description }}
    </p>
  </article>
</template>
