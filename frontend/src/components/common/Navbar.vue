<script setup lang="ts">
import { ref } from "vue";
import { CalendarClock, Menu, X } from "@lucide/vue";
import { navItems } from "@/content";

const isMobileMenuOpen = ref(false);

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};

const scrollToSection = (href: string) => {
  const element = document.querySelector(href);
  if (element) {
    element.scrollIntoView({ behavior: "smooth" });
    isMobileMenuOpen.value = false;
  }
};
</script>

<template>
  <nav
    class="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-sm border-b border-sand-200"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-20">
        <!-- Logo -->
        <div class="flex items-center">
          <a
            href="#home"
            @click.prevent="scrollToSection('#home')"
            class="flex items-center space-x-2"
          >
            Schönheitsecke Oldenburg
          </a>
        </div>

        <!-- Desktop: Navigation + Termin -->
        <div class="hidden md:flex items-center gap-8">
          <ul class="flex space-x-8">
            <li v-for="item in navItems" :key="item.href">
              <a
                :href="item.href"
                @click.prevent="scrollToSection(item.href)"
                class="text-sand-700 hover:text-gold-500 transition-colors duration-200 cursor-pointer"
              >
                {{ item.label }}
              </a>
            </li>
          </ul>
          <a
            href="#contact"
            class="nav-cta inline-flex items-center gap-2 bg-gold-500 text-white px-5 py-2.5 rounded-lg hover:bg-gold-600 transition-colors font-semibold shrink-0"
            @click.prevent="scrollToSection('#contact')"
          >
            <CalendarClock class="w-4 h-4 shrink-0" aria-hidden="true" />
            <span>Termin buchen</span>
          </a>
        </div>

        <!-- Mobile: Menü-Button -->
        <button
          type="button"
          @click="toggleMobileMenu"
          class="md:hidden p-2 rounded-lg text-sand-700 hover:bg-sand-100 transition-colors"
          :aria-expanded="isMobileMenuOpen"
          :aria-label="isMobileMenuOpen ? 'Menü schließen' : 'Menü öffnen'"
        >
          <Menu v-if="!isMobileMenuOpen" class="w-6 h-6" aria-hidden="true" />
          <X v-else class="w-6 h-6" aria-hidden="true" />
        </button>
      </div>
    </div>

    <!-- Mobile Navigation -->
    <div
      v-if="isMobileMenuOpen"
      class="nav-mobile-panel md:hidden bg-white border-t border-sand-200 animate-fade-in"
    >
      <ul class="py-2">
        <li v-for="item in navItems" :key="item.href">
          <a
            :href="item.href"
            @click.prevent="scrollToSection(item.href)"
            class="block px-4 py-3 text-sand-700 hover:bg-sand-50 hover:text-gold-400 transition-colors cursor-pointer"
          >
            {{ item.label }}
          </a>
        </li>
        <li class="px-4 py-3">
          <a
            href="#contact"
            class="nav-cta flex items-center justify-center gap-2 bg-gold-500 text-white px-4 py-3 rounded-lg hover:bg-gold-600 transition-colors w-full font-semibold"
            @click.prevent="scrollToSection('#contact')"
          >
            <CalendarClock class="w-4 h-4 shrink-0" aria-hidden="true" />
            <span class="leading-none">Termin buchen</span>
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>
