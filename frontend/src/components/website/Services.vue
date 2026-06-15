<script setup lang="ts">
import { services } from "@/content";
import { ArrowRight } from "@lucide/vue";
import MonthlyOffer from "@/components/common/MonthlyOffer.vue";
import { scrollToContact } from "@/utils.ts";
</script>

<template>
  <section
    id="services"
    class="py-24 bg-gradient-to-b from-sand-50 to-white scroll-mt-nav"
    aria-labelledby="services-heading"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <div class="inline-block">
          <span class="text-gold-500 font-semibold text-sm uppercase tracking-wider">
            Unsere Leistungen
          </span>
          <div class="h-1 w-16 bg-gold-400 mt-2 rounded-full mx-auto" />
        </div>

        <h2
          id="services-heading"
          class="text-4xl md:text-5xl font-bold text-sand-900 mt-4 mb-6"
        >
          Professionelle <span class="text-gold-500">Beauty-Behandlungen</span>
        </h2>

        <p class="text-lg text-sand-600 max-w-2xl mx-auto">
          Von Anti-Aging über Permanent Make-Up bis zur verschiedener Fußpflege Angeboten
          – entdecken Sie unser umfassendes Behandlungsangebot.
        </p>
      </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <article
          v-for="service in services"
          :key="service.id"
          class="group flex flex-col bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 border border-sand-100 hover:border-gold-200"
        >
          <!-- Bild-Header + Icon-Badge -->
          <div class="relative h-48 sm:h-52 overflow-visible shrink-0">
            <div class="absolute inset-0 overflow-hidden">
              <img
                :src="service.image"
                :alt="service.imageAlt"
                class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                loading="lazy"
              />
              <div
                class="absolute inset-0 bg-gradient-to-t from-sand-900/30 to-transparent"
              />
            </div>
            <div
              :class="[
                'absolute -bottom-8 left-8 w-16 h-16 bg-gradient-to-br rounded-2xl flex items-center justify-center shadow-lg ring-4 ring-white group-hover:scale-110 transition-transform duration-300',
                service.color,
              ]"
            >
              <component
                :is="service.icon"
                class="w-8 h-8 text-white shrink-0"
                aria-hidden="true"
              />
            </div>
          </div>

          <div class="flex flex-col flex-1 p-8 pt-12">
            <h3 class="text-2xl font-bold text-sand-900 mb-3">{{ service.title }}</h3>
            <p class="text-sand-600 mb-6">{{ service.description }}</p>

            <div class="space-y-2 mb-6 flex-1">
              <div
                v-for="(treatment, idx) in service.treatments"
                :key="`${service.id}-treatment-${idx}`"
                class="flex items-center gap-2 text-sm text-sand-600"
              >
                <div class="w-1.5 h-1.5 bg-gold-400 rounded-full shrink-0" />
                <span>{{ treatment }}</span>
              </div>
            </div>

            <a
              href="#contact"
              class="inline-flex items-center gap-2 text-gold-600 font-semibold hover:gap-3 transition-all duration-200 mt-auto"
              @click.prevent="scrollToContact"
            >
              <span>Termin buchen</span>
              <ArrowRight class="w-4 h-4 shrink-0" aria-hidden="true" />
            </a>
          </div>
        </article>
      </div>
      <MonthlyOffer />
    </div>
  </section>
</template>
