<script setup lang="ts">
import { brands } from "@/content";
</script>

<template>
  <section
    id="brands"
    class="py-24 bg-gold-50 scroll-mt-nav"
    aria-labelledby="brands-heading"
  >
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <header class="text-center mb-14 md:mb-16">
        <h2
          id="brands-heading"
          class="text-gold-500 font-semibold text-sm uppercase tracking-wider"
        >
          Unsere Marken
        </h2>
        <div class="h-1 w-16 bg-gold-400 mt-1 rounded-full mx-auto" />
      </header>

      <ul
        class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-5 md:gap-6 lg:gap-8 justify-items-center list-none p-0 m-0"
      >
        <li
          v-for="(brand, index) in brands"
          :key="`${brand.name}-${index}`"
          class="w-full max-w-[10.5rem] sm:max-w-[11.5rem] md:max-w-[12.5rem]"
        >
          <div
            class="group aspect-square bg-white rounded-[1.75rem] shadow-[0_4px_18px_rgba(28,25,23,0.08)] flex items-center justify-center p-6 sm:p-7 md:p-8 transition-all duration-300 hover:shadow-[0_10px_28px_rgba(28,25,23,0.12)] hover:-translate-y-0.5"
            :title="brand.name"
          >
            <img
              :src="brand.img"
              :alt="`${brand.name} Logo`"
              class="max-w-full max-h-full w-auto h-auto object-contain transition-transform duration-300 group-hover:scale-[1.03]"
              loading="lazy"
            />
          </div>
        </li>
      </ul>

      <div
        class="mt-16 md:mt-20 bg-white/70 backdrop-blur-sm rounded-3xl p-8 md:p-12 border border-gold-200/80 shadow-soft"
      >
        <div class="grid md:grid-cols-2 gap-8 items-center">
          <div>
            <h3 class="text-2xl md:text-3xl font-bold text-sand-900 mb-4">
              Qualität, die Sie spüren
            </h3>
            <p class="text-lg text-sand-700 mb-6 leading-relaxed">
              Alle unsere Produkte sind dermatologisch getestet und auf die individuellen
              Bedürfnisse Ihrer Haut abgestimmt.
            </p>
            <ul class="space-y-3">
              <li class="flex items-center gap-2 text-sand-700">
                <div class="w-2 h-2 bg-gold-500 rounded-full shrink-0" />
                <span>Dermatologisch getestet</span>
              </li>
              <li class="flex items-center gap-2 text-sand-700">
                <div class="w-2 h-2 bg-gold-500 rounded-full shrink-0" />
                <span>Ohne Tierversuche</span>
              </li>
              <li class="flex items-center gap-2 text-sand-700">
                <div class="w-2 h-2 bg-gold-500 rounded-full shrink-0" />
                <span>Hochwertige Wirkstoffe</span>
              </li>
              <li class="flex items-center gap-2 text-sand-700">
                <div class="w-2 h-2 bg-gold-500 rounded-full shrink-0" />
                <span>Professionelle Anwendung</span>
              </li>
            </ul>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="bg-white rounded-2xl p-6 shadow-soft border border-sand-100">
              <div class="text-4xl font-bold text-gold-500 mb-2">100%</div>
              <p class="text-sm text-sand-600">Original Produkte</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-soft border border-sand-100">
              <div class="text-4xl font-bold text-gold-500 mb-2">5+</div>
              <p class="text-sm text-sand-600">Premium Marken</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-soft border border-sand-100">
              <div class="text-4xl font-bold text-gold-500 mb-2">15+</div>
              <p class="text-sm text-sand-600">Jahre Erfahrung</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-soft border border-sand-100">
              <div class="text-4xl font-bold text-gold-500 mb-2">500+</div>
              <p class="text-sm text-sand-600">Zufriedene Kunden</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
