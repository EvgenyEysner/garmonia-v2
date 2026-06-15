<script setup lang="ts">
import { onMounted, onUnmounted, ref } from "vue";
import { ChevronUp } from "@lucide/vue";

const isVisible = ref(false);

const SCROLL_THRESHOLD = 400;

function updateVisibility() {
  isVisible.value = window.scrollY > SCROLL_THRESHOLD;
}

function scrollToTop() {
  const home = document.querySelector("#home");
  if (home) {
    home.scrollIntoView({ behavior: "smooth" });
    return;
  }
  window.scrollTo({ top: 0, behavior: "smooth" });
}

onMounted(() => {
  updateVisibility();
  window.addEventListener("scroll", updateVisibility, { passive: true });
});

onUnmounted(() => {
  window.removeEventListener("scroll", updateVisibility);
});
</script>

<template>
  <Transition
    enter-active-class="transition duration-300 ease-out"
    enter-from-class="opacity-0 translate-y-4 scale-95"
    enter-to-class="opacity-100 translate-y-0 scale-100"
    leave-active-class="transition duration-200 ease-in"
    leave-from-class="opacity-100 translate-y-0 scale-100"
    leave-to-class="opacity-0 translate-y-4 scale-95"
  >
    <button
      v-show="isVisible"
      type="button"
      class="fixed bottom-6 right-4 sm:right-6 z-50 flex h-12 w-12 sm:h-14 sm:w-14 items-center justify-center rounded-full bg-gold-500 text-white shadow-lg shadow-gold-300/50 ring-2 ring-white/80 hover:bg-gold-600 active:scale-95 transition-colors"
      aria-label="Nach oben scrollen"
      @click="scrollToTop"
    >
      <ChevronUp class="h-6 w-6 sm:h-7 sm:w-7 shrink-0" aria-hidden="true" />
    </button>
  </Transition>
</template>
