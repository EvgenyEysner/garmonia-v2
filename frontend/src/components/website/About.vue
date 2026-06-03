<script setup lang="ts">
import { Award, Heart, Sparkles, Users } from "@lucide/vue";

const features = [
  {
    id: 1,
    icon: Award,
    title: "Staatl. geprüfte Kosmetikerin",
    description: "Professionelle Ausbildung und kontinuierliche Weiterbildung",
  },
  {
    id: 2,
    icon: Heart,
    title: "Individuelle Beratung",
    description: "Persönliche Behandlungskonzepte für Ihre Bedürfnisse",
  },
  {
    id: 3,
    icon: Users,
    title: "Erfahrung seit 2014",
    description: "Über 10 Jahre Expertise in der Schönheitspflege",
  },
  {
    id: 4,
    icon: Sparkles,
    title: "Premium Produkte",
    description: "Hochwertige Markenprodukte für optimale Ergebnisse",
  },
];
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
            Mit über 10 Jahren Erfahrung und höchsten Qualitätsstandards verwöhnen wir Sie
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
            ))}
          </div>
        </div>

        <div class="relative">
          <div class="grid grid-cols-2 gap-4">
            <div class="space-y-4">
              <div class="rounded-2xl overflow-hidden shadow-lg">
                <img
                  src="https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxiZWF1dHklMjB0cmVhdG1lbnQlMjBmYWNpYWwlMjBza2luY2FyZXxlbnwxfHx8fDE3ODA0NzUyMTl8MA&ixlib=rb-4.1.0&q=80&w=1080"
                  alt="Facial Treatment"
                  class="w-full h-64 object-cover"
                />
              </div>
              <div class="rounded-2xl overflow-hidden shadow-lg">
                <img
                  src="https://images.unsplash.com/photo-1676536162793-faa565d976d4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwyfHxsdXh1cnklMjBiZWF1dHklMjBzYWxvbiUyMHNwYSUyMGludGVyaW9yfGVufDF8fHx8MTc4MDQ3NTIxOHww&ixlib=rb-4.1.0&q=80&w=1080"
                  alt="Salon Interior"
                  class="w-full h-48 object-cover"
                />
              </div>
            </div>
            <div class="space-y-4 pt-8">
              <div class="rounded-2xl overflow-hidden shadow-lg">
                <img
                  src="https://images.unsplash.com/photo-1643684391140-c5056cfd3436?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwzfHxiZWF1dHklMjB0cmVhdG1lbnQlMjBmYWNpYWwlMjBza2luY2FyZXxlbnwxfHx8fDE3ODA0NzUyMTl8MA&ixlib=rb-4.1.0&q=80&w=1080"
                  alt="Massage Treatment"
                  class="w-full h-48 object-cover"
                />
              </div>
              <div class="rounded-2xl overflow-hidden shadow-lg">
                <img
                  src="https://images.unsplash.com/photo-1758188753373-5b01a0fc6d9d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwzfHxsdXh1cnklMjBiZWF1dHklMjBzYWxvbiUyMHNwYSUyMGludGVyaW9yfGVufDF8fHx8MTc4MDQ3NTIxOHww&ixlib=rb-4.1.0&q=80&w=1080"
                  alt="Beauty Products"
                  class="w-full h-64 object-cover"
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
