<script setup lang="ts">
import { RouterView } from "vue-router";
import Navbar from "@/components/common/Navbar.vue";
import Footer from "@/components/common/Footer.vue";
import ScrollToTop from "@/components/common/ScrollToTop.vue";
import CallFab from "@/components/common/CallFab.vue";
import CookieBanner from "@/components/common/CookieBanner.vue";
</script>

<template>
  <div id="app" class="flex flex-col min-h-screen">
    <Navbar />
    <RouterView />
  </div>
  <Footer />
  <CallFab />
  <ScrollToTop />
  <CookieBanner />
</template>
