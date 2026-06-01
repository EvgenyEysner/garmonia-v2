<script setup lang="ts">
import Navbar from "./components/common/Navbar.vue";
import Hero from "@/components/website/Hero.vue";
import Footer from "@/components/common/Footer.vue";
import About from "@/components/website/About.vue";
</script>

<template>
  <div id="app" class="flex flex-col min-h-screen">
    <!-- Navigation -->
    <Navbar />
    <!-- Hero Section -->
    <Hero />
    <!-- <Hero /> -->

    <!-- About Section -->
    <section id="about" class="section scroll-mt-nav">
      <About />
    </section>

    <!-- Services Section -->
    <section id="services" class="section section-alt scroll-mt-nav">
      <div class="container-custom">
        <h2 class="text-center mb-12">Unsere Leistungen</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Service Card Beispiel -->
          <div class="card">
            <div class="card-body">
              <h3 class="text-xl font-bold mb-3">Gesichtsbehandlung</h3>
              <p class="text-sand-600 mb-4">
                Professionelle Gesichtspflege für jeden Hauttyp
              </p>
              <p class="text-gold-500 font-bold">ab 59€</p>
            </div>
          </div>
          <!-- Weitere Services kommen hier -->
        </div>
      </div>
    </section>

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
