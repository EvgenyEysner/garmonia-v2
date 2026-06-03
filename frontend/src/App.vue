<script setup lang="ts">
import Navbar from "./components/common/Navbar.vue";
import Hero from "@/components/website/Hero.vue";
import Footer from "@/components/common/Footer.vue";
import About from "@/components/website/About.vue";
import Services from "@/components/website/Services.vue";
import Favorite from "@/components/website/Favorite.vue";
import Gallery from "@/components/website/Gallery.vue";
import PriceList from "@/components/website/PriceList.vue";
import Brands from "@/components/website/Brands.vue";
import Testimonials from "@/components/website/Testimonials.vue";
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
    <Gallery />
    <!-- <Gallery /> -->

    <!-- Pricing Section -->
    <PriceList />
    <!-- <PriceList /> -->
    <!-- Brands Section -->
    <Brands />
    <!-- <Brands /> -->

    <!-- Testimonials Section -->
    <Testimonials />

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
