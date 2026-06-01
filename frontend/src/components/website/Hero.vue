<script setup lang="ts">
import heroBg from "@/assets/images/home-header.webp";

const scrollToContact = () => {
  const contactctSection = document.querySelector("#contact");
  contactctSection?.scrollIntoView({ behavior: "smooth" });
};
</script>
<template>
  <section
    id="home"
    class="relative flex items-center justify-center min-h-screen bg-gradient-gold"
  >
    <!-- Background overlay -->
    <div
      class="absolute inset-0 bg-cover bg-cover"
      :style="{ backgroundImage: `url(${heroBg})` }"
    />
    <!-- Content -->
    <div class="relative z-10 max-w-4xl mx-auto px-4 text-center text-white">
      <h1
        class="text-5xl md:text-6xl lg:text-7xl font-bold mb-6 drop-shadow-lg animate-slide-up"
      >
        Willkommen bei der<br />
        <span class="text-gold-300">Schönheitsecke Oldenburg</span>
      </h1>
      <p class="text-xl md:text-2xl mb-8 opacity-95 drop-shadow-md animate-slide-up">
        Ihr Wohlfühlort für Schönheit & Entspannung
      </p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center animate-slide-up">
        <button @click="scrollToContact" class="btn btn-primary btn-lg shadow-gold">
          Kontakt aufnehmen
        </button>
      </div>
    </div>
  </section>
</template>
