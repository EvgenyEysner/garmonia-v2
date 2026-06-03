<script setup lang="ts">
import { ref } from "vue";
import type { NavItem } from "@/types";
import { Menu, Phone, X } from "@lucide/vue";

const isMobileMenuOpen = ref(false);

const navItems: NavItem[] = [
  { label: "Home", href: "#home" },
  { label: "Über uns", href: "#about" },
  { label: "Leistungen", href: "#services" },
  { label: "Galerie", href: "#gallery" },
  { label: "Preise", href: "#pricing" },
  { label: "Team", href: "#team" },
  { label: "Kontakt", href: "#contact" },
];

/**
 * Toggle Mobile Menu
 */
const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};

/**
 * Smooth Scroll to Section
 */
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

        <!-- Desktop Navigation -->
        <ul class="hidden md:flex space-x-8">
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

        <!-- Mobile Menu Button -->
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
            href="tel:+491797716648"
            class="flex items-center justify-center gap-2 bg-gold-500 text-white px-4 py-3 rounded-lg hover:bg-gold-600 transition-colors w-full"
          >
            <Phone class="w-4 h-4 shrink-0" aria-hidden="true" />
            <span class="leading-none">Termin buchen</span>
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>
