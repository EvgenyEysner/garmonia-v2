<script setup lang="ts">
import { Award } from "@lucide/vue";
import { brands } from "@/content";
</script>

<template>
  <section id="brands" class="py-24 bg-white scroll-mt-nav">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <div
          class="inline-flex items-center gap-2 bg-gold-100 px-4 py-2 rounded-full mb-4"
        >
          <Award class="w-4 h-4 text-gold-600 shrink-0" aria-hidden="true" />
          <span class="text-gold-600 font-semibold text-sm uppercase tracking-wider">
            Unsere Partner
          </span>
        </div>

        <h2 class="text-4xl md:text-5xl font-bold text-sand-900 mb-6">
          Premium <span class="text-gold-500">Marken</span>
        </h2>

        <p class="text-lg text-sand-600 max-w-2xl mx-auto">
          Wir arbeiten ausschließlich mit hochwertigen Produkten führender Beauty-Marken
        </p>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-8">
        <div
          v-for="(brand, index) in brands"
          :key="`${brand.name}-${index}`"
          class="group bg-gradient-to-br from-sand-50 to-gold-50 rounded-2xl p-8 text-center hover:shadow-xl transition-all duration-300 border border-sand-200 hover:border-gold-300"
        >
          <div
            class="w-20 h-20 mx-auto mb-4 bg-white rounded-full flex items-center justify-center shadow-md group-hover:shadow-lg transition-shadow overflow-hidden p-2"
          >
            <img
              :src="brand.img"
              :alt="brand.name"
              class="w-full h-full object-contain"
              loading="lazy"
            />
          </div>
          <h3 class="text-xl font-bold text-sand-900 mb-2">{{ brand.name }}</h3>
          <p class="text-sm text-sand-600">{{ brand.description }}</p>
        </div>
      </div>

      <div
        class="mt-16 bg-gradient-to-br from-gold-50 to-sand-50 rounded-3xl p-8 md:p-12 border border-gold-200"
      >
        <div class="grid md:grid-cols-2 gap-8 items-center">
          <div>
            <h3 class="text-3xl font-bold text-sand-900 mb-4">
              Qualität, die Sie spüren
            </h3>
            <p class="text-lg text-sand-700 mb-6">
              Alle unsere Produkte sind dermatologisch getestet, hochkonzentriert und auf
              die individuellen Bedürfnisse Ihrer Haut abgestimmt.
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
            <div class="bg-white rounded-2xl p-6 shadow-lg">
              <div class="text-4xl font-bold text-gold-500 mb-2">100%</div>
              <p class="text-sm text-sand-600">Original Produkte</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-lg">
              <div class="text-4xl font-bold text-gold-500 mb-2">5+</div>
              <p class="text-sm text-sand-600">Premium Marken</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-lg">
              <div class="text-4xl font-bold text-gold-500 mb-2">10+</div>
              <p class="text-sm text-sand-600">Jahre Erfahrung</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-lg">
              <div class="text-4xl font-bold text-gold-500 mb-2">500+</div>
              <p class="text-sm text-sand-600">Zufriedene Kunden</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
