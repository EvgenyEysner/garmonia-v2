<script setup lang="ts">
import { Clock, Star, TrendingUp } from "@lucide/vue";

const treatments = [
  {
    name: "Hydra Facial",
    category: "Kosmetik",
    price: "125€",
    duration: "60 Min",
    rating: 5,
    reviews: 124,
    description: "Intensive Tiefenreinigung und Hydration für strahlende Haut",
    image:
      "https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxiZWF1dHklMjB0cmVhdG1lbnQlMjBmYWNpYWwlMjBza2luY2FyZXxlbnwxfHx8fDE3ODA0NzUyMTl8MA&ixlib=rb-4.1.0&q=80&w=1080",
  },
  {
    name: "Permanent Make-Up Augenbrauen",
    category: "PMU",
    price: "250€",
    duration: "120 Min",
    rating: 5,
    reviews: 89,
    description: "Natürlich aussehende, perfekt geformte Augenbrauen",
    image:
      "https://images.unsplash.com/photo-1643684391140-c5056cfd3436?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwzfHxiZWF1dHklMjB0cmVhdG1lbnQlMjBmYWNpYWwlMjBza2luY2FyZXxlbnwxfHx8fDE3ODA0NzUyMTl8MA&ixlib=rb-4.1.0&q=80&w=1080",
  },
  {
    name: "Wimpernlifting",
    category: "Wimpern",
    price: "55€",
    duration: "45 Min",
    rating: 5,
    reviews: 156,
    description: "Perfekt geschwungene Wimpern ganz ohne Mascara",
    image:
      "https://images.unsplash.com/photo-1731514771613-991a02407132?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHw1fHxiZWF1dHklMjB0cmVhdG1lbnQlMjBmYWNpYWwlMjBza2luY2FyZXxlbnwxfHx8fDE3ODA0NzUyMTl8MA&ixlib=rb-4.1.0&q=80&w=1080",
  },
  {
    name: "Gel-Modellage",
    category: "Nägel",
    price: "45€",
    duration: "60 Min",
    rating: 5,
    reviews: 201,
    description: "Perfekte Nägel mit langanhaltender Gel-Modellage",
    image:
      "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwyfHxiZWF1dHklMjB0cmVhdG1lbnQlMjBmYWNpYWwlMjBza2luY2FyZXxlbnwxfHx8fDE3ODA0NzUyMTl8MA&ixlib=rb-4.1.0&q=80&w=1080",
  },
];

const scrollToContact = () => {
  document.querySelector("#contact")?.scrollIntoView({ behavior: "smooth" });
};
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
          class="group bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 border border-sand-100 hover:border-gold-300"
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
              <span
                class="text-xs text-white/90 bg-gold-500/90 px-2 py-1 rounded-full"
              >
                {{ treatment.category }}
              </span>
            </div>
          </div>

          <div class="p-6">
            <h3 class="text-xl font-bold text-sand-900 mb-2">{{ treatment.name }}</h3>
            <p class="text-sand-600 text-sm mb-4">{{ treatment.description }}</p>

            <div class="flex items-center justify-between mb-4">
              <div class="flex items-center gap-1">
                <Star
                  v-for="i in treatment.rating"
                  :key="`${treatment.name}-star-${i}`"
                  class="w-4 h-4 fill-gold-500 text-gold-500 shrink-0"
                  aria-hidden="true"
                />
                <span class="text-xs text-sand-500 ml-1">({{ treatment.reviews }})</span>
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
        </article>
      </div>
    </div>
  </section>
</template>
