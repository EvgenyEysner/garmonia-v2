<script setup lang="ts">
import { Clock, Star, TrendingUp } from "@lucide/vue";
import { scrollToContact } from "@/utils";
import { treatments } from "@/content";
</script>

<template>
  <section class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <div
          class="inline-flex items-center gap-2 bg-gold-100 px-4 py-2 rounded-full mb-4"
        >
          <TrendingUp class="w-4 h-4 text-gold-600 shrink-0" aria-hidden="true" />
          <span class="text-gold-600 font-semibold text-sm uppercase tracking-wider">
            Beliebte Behandlungen
          </span>
        </div>

        <h2 class="text-4xl md:text-5xl font-bold text-sand-900 mb-6">
          Unsere <span class="text-gold-500">Top-Favoriten</span>
        </h2>

        <p class="text-lg text-sand-600 max-w-2xl mx-auto">
          Die am meisten gebuchten und beliebtesten Behandlungen unserer Kundinnen
        </p>
      </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
        <article
          v-for="(treatment, index) in treatments"
          :key="`${treatment.name}-${index}`"
          class="group flex flex-col h-full bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 border border-sand-100 hover:border-gold-300"
        >
          <div class="relative h-64 overflow-hidden">
            <img
              :src="treatment.image"
              :alt="treatment.name"
              class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
              loading="lazy"
            />
            <div
              class="absolute top-4 right-4 bg-white/95 backdrop-blur-sm px-3 py-1 rounded-full"
            >
              <span class="text-gold-600 font-bold">{{ treatment.price }}</span>
            </div>
            <div
              class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-sand-900/80 to-transparent p-4"
            >
              <span class="text-xs text-white/90 bg-gold-500/90 px-2 py-1 rounded-full">
                {{ treatment.category }}
              </span>
            </div>
          </div>

          <div class="flex flex-col flex-1 p-6">
            <h3 class="text-xl font-bold text-sand-900 mb-2">{{ treatment.name }}</h3>
            <p class="text-sand-600 text-sm mb-4">{{ treatment.description }}</p>

            <div class="mt-auto">
              <div class="flex items-center justify-between mb-4">
                <div class="flex items-center gap-1">
                  <Star
                    v-for="i in treatment.rating"
                    :key="`${treatment.name}-star-${i}`"
                    class="w-4 h-4 fill-gold-500 text-gold-500 shrink-0"
                    aria-hidden="true"
                  />
                  <span class="text-xs text-sand-500 ml-1"
                    >({{ treatment.reviews }})</span
                  >
                </div>
                <div class="flex items-center gap-1 text-sand-500">
                  <Clock class="w-4 h-4 shrink-0" aria-hidden="true" />
                  <span class="text-xs">{{ treatment.duration }}</span>
                </div>
              </div>

              <a
                href="#contact"
                class="block w-full text-center bg-gold-500 text-white px-4 py-3 rounded-lg hover:bg-gold-600 transition-colors font-semibold"
                @click.prevent="scrollToContact"
              >
                Jetzt buchen
              </a>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>
