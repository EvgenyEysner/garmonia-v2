<script setup lang="ts">
import Navbar from "./components/common/Navbar.vue";
import Hero from "@/components/website/Hero.vue";
import Footer from "@/components/common/Footer.vue";
import About from "@/components/website/About.vue";
import Services from "@/components/website/Services.vue";
import Favorite from "@/components/website/Favorite.vue";
</script>

<template>
  <div id="app" class="flex flex-col min-h-screen">
    <!-- Navigation -->
    <Navbar />
    <!-- Hero Section -->
    <Hero />
    <!-- <Hero /> -->

    <!-- About Section -->
    <About />
    <!-- <About /> -->
    <!-- Services Section -->
    <Services />
    <!-- <Services /> -->
    <!-- Favorite Section -->
    <Favorite />
    <!-- <Favorite /> -->
    <!-- Gallery Section -->
    <section id="gallery" class="section scroll-mt-nav">
      <div class="container-custom">
        <h2 class="text-center mb-12">Galerie</h2>
        <p class="text-center text-sand-600">Galerie-Komponente folgt...</p>
      </div>
    </section>

    <!-- Pricing Section -->
    <section id="pricing" class="section section-alt scroll-mt-nav">
      <div class="container-custom">
        <h2 class="text-center mb-12">Preise</h2>
        <p class="text-center text-sand-600">Preis-Tabelle folgt...</p>
      </div>
    </section>

    <!-- Team Section -->
    <section id="team" class="section scroll-mt-nav">
      <div class="container-custom">
        <h2 class="text-center mb-12">Unser Team</h2>
        <p class="text-center text-sand-600">Team-Komponente folgt...</p>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section section-alt scroll-mt-nav">
      <div class="container-custom">
        <h2 class="text-center mb-12">Kontakt</h2>
        <p class="text-center text-sand-600">Kontaktformular folgt morgen!</p>
      </div>
    </section>
  </div>
  <Footer />
</template>
