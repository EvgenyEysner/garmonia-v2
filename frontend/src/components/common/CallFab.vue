<script setup lang="ts">
import { Phone } from "@lucide/vue";
import { contact } from "@/content";
</script>

<template>
  <a
    :href="contact.phoneHref"
    class="fixed bottom-[5.5rem] right-4 md:bottom-6 left-4 z-50 md:hidden flex h-14 w-14 items-center justify-center rounded-full bg-gold-500 text-white shadow-lg shadow-gold-300/50 ring-2 ring-white/80 hover:bg-gold-600 active:scale-95 transition-colors"
    aria-label="Jetzt anrufen"
  >
    <Phone class="h-6 w-6 shrink-0" aria-hidden="true" />
  </a>
</template>
