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
import Contact from "@/components/website/Contact.vue";
import ScrollToTop from "@/components/common/ScrollToTop.vue";
import CallFab from "@/components/common/CallFab.vue";
</script>

<template>
  <div id="app" class="flex flex-col min-h-screen">
    <!-- Navigation -->
    <Navbar />
    <!-- <Navbar /> -->
    
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
    <!-- <Testimonials /> -->

    <!-- Contact Section -->
    <Contact />
    <!-- <Contact /> -->
  </div>
  <Footer />
  <CallFab />
  <ScrollToTop />
</template>
