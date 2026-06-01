<script setup lang="ts">
import type { FooterLink, SocialLink } from "@/types";

const currentYear = new Date().getFullYear();
const socialLinks: SocialLink[] = [
  { name: "Instagram", url: "https://www.instagram.com/olga.eisner/", icon: "" },
  { name: "Facebook", url: "https://www.facebook.com/evgeny.eisner/", icon: "" },
];

const footerLinks: FooterLink[] = [
  { label: "Impressum", href: "/impressum" },
  { label: "Datenschutz", href: "/datenschutz" },
  { label: "AGB", href: "/agb" },
];
</script>
<template>
  <footer class="bg-sand-800 text-sand-100">
    <div class="max-w-7xl mx-auto px-4 py-12">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Kontakt Info -->
        <div>
          <h3 class="text-xl font-bold text-gold-400 mb-4">Schönheitsecke Oldenburg</h3>
          <div class="space-y-2 text-sand-300">
            <p>Bahnhofsplatz 2a</p>
            <p>26122 Oldenburg</p>
            <p class="mt-4">
              <a href="tel:+491797716648" class="hover:text-gold-400 transition-colors">
                +49 123 456 7890
              </a>
            </p>
            <p>
              ✉️
              <a
                href="mailto:garmonia.eisner@gmail.com"
                class="hover:text-gold-400 transition-colors"
              >
                garmonia.eisner@gmail.com
              </a>
            </p>
          </div>
        </div>

        <div>
          <h3 class="text-xl font-bold text-gold-400 mb-4">Folgen Sie uns</h3>
          <ul class="space-y-2">
            <li v-for="link in socialLinks" :key="link.name">
              <a
                :href="link.url"
                target="_blank"
                rel="noopener noreferrer"
                class="text-sand-300 hover:text-gold-400 transition-colors"
              >
                {{ link.name }}
              </a>
            </li>
          </ul>
        </div>

        <div>
          <h3 class="text-xl font-bold text-gold-400 mb-4">Rechtliches</h3>
          <ul class="space-y-2">
            <li v-for="link in footerLinks" :key="link.href">
              <a :href="link.href" class="text-sand-300 hover:text-gold-400 transition-colors">
                {{ link.label }}
              </a>
            </li>
          </ul>
        </div>
      </div>

      <p class="mt-10 pt-6 border-t border-sand-700 text-center text-sand-400 text-sm">
        © {{ currentYear }} Schönheitsecke Oldenburg
      </p>
    </div>
  </footer>
</template>
