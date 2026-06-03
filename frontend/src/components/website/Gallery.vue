<script setup lang="ts">
const images = [
  {
    url: "https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxiZWF1dHklMjB0cmVhdG1lbnQlMjBmYWNpYWwlMjBza2luY2FyZXxlbnwxfHx8fDE3ODA0NzUyMTl8MA&ixlib=rb-4.1.0&q=80&w=1080",
    title: "Gesichtsbehandlung",
  },
  {
    url: "https://images.unsplash.com/photo-1643684391140-c5056cfd3436?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwzfHxiZWF1dHklMjB0cmVhdG1lbnQlMjBmYWNpYWwlMjBza2luY2FyZXxlbnwxfHx8fDE3ODA0NzUyMTl8MA&ixlib=rb-4.1.0&q=80&w=1080",
    title: "Massage",
  },
  {
    url: "https://images.unsplash.com/photo-1731514771613-991a02407132?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHw1fHxiZWF1dHklMjB0cmVhdG1lbnQlMjBmYWNpYWwlMjBza2luY2FyZXxlbnwxfHx8fDE3ODA0NzUyMTl8MA&ixlib=rb-4.1.0&q=80&w=1080",
    title: "Entspannung",
  },
  {
    url: "https://images.unsplash.com/photo-1630835425197-50feeba99ecd?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxsdXh1cnklMjBiZWF1dHklMjBzYWxvbiUyMHNwYSUyMGludGVyaW9yfGVufDF8fHx8MTc4MDQ3NTIxOHww&ixlib=rb-4.1.0&q=80&w=1080",
    title: "Studio Ambiente",
  },
  {
    url: "https://images.unsplash.com/photo-1758188753373-5b01a0fc6d9d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwzfHxsdXh1cnklMjBiZWF1dHklMjBzYWxvbiUyMHNwYSUyMGludGVyaW9yfGVufDF8fHx8MTc4MDQ3NTIxOHww&ixlib=rb-4.1.0&q=80&w=1080",
    title: "Premium Produkte",
  },
  {
    url: "https://images.unsplash.com/photo-1773924093206-9a433a14bb44?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHw4fHxsdXh1cnklMjBiZWF1dHklMjBzYWxvbiUyMHNwYSUyMGludGVyaW9yfGVufDF8fHx8MTc4MDQ3NTIxOHww&ixlib=rb-4.1.0&q=80&w=1080",
    title: "Entspannungsbereich",
  },
];
</script>
<template>
  <section id="gallery" class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <div class="inline-block">
          <span class="text-gold-500 font-semibold text-sm uppercase tracking-wider"
            >Galerie</span
          >
          <div class="h-1 w-16 bg-gold-400 mt-2 rounded-full mx-auto"></div>
        </div>

        <h2 class="text-4xl md:text-5xl font-bold text-sand-900 mt-4 mb-6">
          Einblicke in unser <span class="text-gold-500">Studio</span>
        </h2>

        <p class="text-lg text-sand-600 max-w-2xl mx-auto">
          Erleben Sie die Atmosphäre unseres exklusiven Beauty-Studios und lassen Sie sich
          inspirieren.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="(image, index) in images"
          :key="index"
          class="group relative overflow-hidden rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300"
        >
          <div class="aspect-square overflow-hidden">
            <img
              :src="image.url"
              :alt="image.title"
              class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
            />
          </div>
          <div
            class="absolute inset-0 bg-gradient-to-t from-sand-900/80 via-sand-900/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"
          >
            <div class="absolute bottom-0 left-0 right-0 p-6">
              <h3 class="text-xl font-semibold text-white">{{ image.title }}</h3>
            </div>
          </div>
        </div>
        ))}
      </div>
    </div>
  </section>
</template>
