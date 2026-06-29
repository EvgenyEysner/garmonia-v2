<script setup lang="ts">
import { features } from "@/content";
import about1 from "@/assets/images/about/about-1.webp";
import about2 from "@/assets/images/about/about-2.webp";
import about3 from "@/assets/images/about/about-3.webp";
import about4 from "@/assets/images/about/about-4.webp";
</script>
<template>
  <section id="about" class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid md:grid-cols-2 gap-16 items-center">
        <div class="space-y-6">
          <div class="inline-block">
            <span class="text-gold-500 font-semibold text-sm uppercase tracking-wider"
              >Über uns</span
            >
            <div class="h-1 w-16 bg-gold-400 mt-2 rounded-full"></div>
          </div>

          <h2 class="text-4xl md:text-5xl font-bold text-sand-900 leading-tight">
            Ihr Partner für <br />
            <span class="text-gold-500">Schönheit & Pflege</span>
          </h2>

          <p class="text-lg text-sand-600 leading-relaxed">
            Willkommen bei Schönheitsecke Oldenburg! In unserem exklusiven Kosmetikstudio
            am Bahnhofsplatz bieten wir Ihnen ein umfassendes Angebot an professionellen
            Beauty-Behandlungen.
          </p>

          <p class="text-lg text-sand-600 leading-relaxed">
            Mit über 15 Jahren Erfahrung und höchsten Qualitätsstandards verwöhnen wir Sie
            mit modernsten Behandlungsmethoden und hochwertigen Produkten. Ihre
            Zufriedenheit und Ihr Wohlbefinden stehen bei uns an erster Stelle.
          </p>

          <div class="grid grid-cols-2 gap-4 pt-6">
            <div v-for="feature in features" :key="feature.id" class="space-y-2">
              <div
                class="w-12 h-12 bg-gold-100 rounded-xl flex items-center justify-center"
              >
                <component :is="feature.icon" class="w-6 h-6 text-gold-600" />
              </div>
              <h3 class="font-semibold text-sand-900">{{ feature.title }}</h3>
              <p class="text-sm text-sand-600">{{ feature.description }}</p>
            </div>
          </div>
        </div>

        <div class="relative">
          <div class="grid grid-cols-2 gap-4">
            <div class="space-y-4">
              <div class="rounded-2xl overflow-hidden shadow-lg">
                <img
                  :src="about1"
                  alt="Gesichtsbehandlung im Kosmetikstudio Oldenburg"
                  class="w-full h-64 object-cover"
                  width="380"
                  height="380"
                  loading="lazy"
                  decoding="async"
                />
              </div>
              <div class="rounded-2xl overflow-hidden shadow-lg">
                <img
                  :src="about2"
                  alt="Innenansicht des Kosmetikstudios in Oldenburg"
                  class="w-full h-48 object-cover"
                  width="512"
                  height="512"
                  loading="lazy"
                  decoding="async"
                />
              </div>
            </div>
            <div class="space-y-4 pt-8">
              <div class="rounded-2xl overflow-hidden shadow-lg">
                <img
                  :src="about3"
                  alt="Entspannende Beauty-Behandlung im Studio Oldenburg"
                  class="w-full h-48 object-cover"
                  width="512"
                  height="732"
                  loading="lazy"
                  decoding="async"
                />
              </div>
              <div class="rounded-2xl overflow-hidden shadow-lg">
                <img
                  :src="about4"
                  alt="Hochwertige Kosmetikprodukte im Kosmetikstudio Oldenburg"
                  class="w-full h-64 object-cover"
                  width="640"
                  height="426"
                  loading="lazy"
                  decoding="async"
                />
              </div>
            </div>
          </div>

          <div
            class="absolute -top-4 -left-4 w-24 h-24 bg-gold-400 rounded-full blur-2xl opacity-40"
          ></div>
          <div
            class="absolute -bottom-4 -right-4 w-32 h-32 bg-gold-300 rounded-full blur-2xl opacity-40"
          ></div>
        </div>
      </div>
    </div>
  </section>
</template>
