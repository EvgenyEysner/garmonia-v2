<script setup lang="ts">
import { ref } from "vue";
import type { NavItem } from "@/types";

/**
 * Mobile Menu State
 */
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
  <nav class="fixed top-0 left-0 right-0 z-50 bg-white shadow-soft">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-20">
        <!-- Logo -->
        <div class="flex-shrink-0">
          <a
            href="#home"
            @click.prevent="scrollToSection('#home')"
            class="text-2xl font-bold text-gold-400 hover:text-gold-500 transition-colors"
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
              class="text-sand-700 hover:text-gold-400 font-medium transition-colors cursor-pointer"
            >
              {{ item.label }}
            </a>
          </li>
        </ul>

        <!-- Mobile Menu Button -->
        <button
          @click="toggleMobileMenu"
          class="md:hidden p-2 rounded-lg text-sand-700 hover:bg-sand-100 transition-colors"
          aria-label="Toggle Menu"
        >
          <svg
            v-if="!isMobileMenuOpen"
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
          <svg
            v-else
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
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
      </ul>
    </div>
  </nav>
</template>
