import path from "path";
import { fileURLToPath } from "url";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwindcss from "@tailwindcss/vite";
import type {} from "vite-ssg";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  ssgOptions: {
    formatting: "minify",
    includedRoutes() {
      return ["/", "/datenschutz"];
    },
    // Kritisches CSS-Inlining (beasties) ist hier bewusst deaktiviert: Das
    // gebuendelte CSS ist klein (~9 KB gzip), waehrend das vorgerenderte HTML
    // gross ist. Inlining wuerde das HTML auf dem kritischen Pfad vergroessern
    // und damit FCP/LCP auf langsamem Mobilfunk eher verschlechtern.
    beastiesOptions: false,
    // vite-ssg/unhead setzt im gerenderten HTML lang="en"; auf "de" korrigieren.
    onPageRendered(_route, html) {
      return html.replace(/<html lang="en">/i, '<html lang="de">');
    },
  },
  build: {
    // Langzeit-Caching: Framework-Code von App-Code trennen, damit
    // App-Updates nicht den Vendor-Chunk invalidieren.
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (!id.includes("node_modules")) return;
          if (/[\\/]node_modules[\\/](@vue|vue|vue-router|pinia)[\\/]/.test(id)) {
            return "vue-vendor";
          }
          if (id.includes("@lucide")) return "icons";
          if (id.includes("axios")) return "axios";
        },
      },
    },
  },
});
