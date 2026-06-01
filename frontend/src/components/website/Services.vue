<script setup lang="ts">
import { onMounted, onUnmounted, ref } from "vue";
import ServiceCard from "@/components/website/ServiceCard.vue";
import type { ServiceItem } from "@/types";

import service1 from "@/assets/images/service-1.webp";
import service2 from "@/assets/images/service-2.webp";
import service3 from "@/assets/images/service-3.webp";
import service4 from "@/assets/images/service-4.webp";
import service5 from "@/assets/images/service-5.webp";

const services: ServiceItem[] = [
  {
    id: "cosmetic",
    title: "Kosmetische Behandlungen",
    description:
      "Gesichtsbehandlungen gehören zu den gefragtesten Verfahren, da sie helfen können, Falten zu reduzieren und den Hautton zu verbessern.",
    imageSrc: service1,
    imageAlt: "Kosmetische Gesichtsbehandlung im Studio",
  },
  {
    id: "permanent-makeup",
    title: "Permanent Make Up",
    description:
      "Permanent Make-up ist ein revolutionäres kosmetisches Verfahren, das Ihre natürliche Schönheit mit dauerhaften Ergebnissen verbessern kann.",
    imageSrc: service2,
    imageAlt: "Permanent Make Up Behandlung",
  },
  {
    id: "hair-removal",
    title: "Körperenthaarung",
    description:
      "Die Körperenthaarung kann schnell und effizient mit minimalen Beschwerden durchgeführt werden. Dabei stehen verschiedene Methoden zur Verfügung.",
    imageSrc: service3,
    imageAlt: "Professionelle Körperenthaarung",
  },
  {
    id: "foot-care",
    title: "Fußpflege",
    description:
      "Pediküre ist eine großartige Möglichkeit, Ihre Füße zu verwöhnen, damit sie gesund aussehen und sich so anfühlen. Mit regelmäßiger Pediküre halten Sie Ihre Füße in Topform!",
    imageSrc: service4,
    imageAlt: "Professionelle Fußpflege und Pediküre",
  },
  {
    id: "nail-design",
    title: "Nageldesign",
    description:
      "Sie wünschen längere Nägel, ist die Modellage die beste Lösung. Die vorhandene Länge ist dabei unentscheidend. Eine Verlängerung ist bei jedem möglich.",
    imageSrc: service5,
    imageAlt: "Kreatives Nageldesign und Modellage",
  },
];

const trackRef = ref<HTMLElement | null>(null);
const activeIndex = ref(0);

function updateScrollState() {
  const track = trackRef.value;
  if (!track) return;

  const slides = track.querySelectorAll<HTMLElement>("[data-slide]");
  if (!slides.length) return;

  const trackRect = track.getBoundingClientRect();
  const trackCenter = trackRect.left + trackRect.width / 2;

  let closest = 0;
  let minDistance = Infinity;

  slides.forEach((slide, index) => {
    const slideRect = slide.getBoundingClientRect();
    const slideCenter = slideRect.left + slideRect.width / 2;
    const distance = Math.abs(slideCenter - trackCenter);
    if (distance < minDistance) {
      minDistance = distance;
      closest = index;
    }
  });

  activeIndex.value = closest;
}

function scrollToIndex(index: number) {
  const track = trackRef.value;
  if (!track) return;

  const slides = track.querySelectorAll<HTMLElement>("[data-slide]");
  const target = slides[index];
  if (!target) return;

  const offset = target.offsetLeft - track.clientWidth / 2 + target.offsetWidth / 2;

  track.scrollTo({
    left: Math.max(0, offset),
    behavior: "smooth",
  });
}

function goPrev() {
  const nextIndex = activeIndex.value <= 0 ? services.length - 1 : activeIndex.value - 1;
  scrollToIndex(nextIndex);
}

function goNext() {
  const nextIndex = activeIndex.value >= services.length - 1 ? 0 : activeIndex.value + 1;
  scrollToIndex(nextIndex);
}

let resizeObserver: ResizeObserver | undefined;

onMounted(() => {
  const track = trackRef.value;
  if (!track) return;

  track.addEventListener("scroll", updateScrollState, { passive: true });
  resizeObserver = new ResizeObserver(updateScrollState);
  resizeObserver.observe(track);
  updateScrollState();
});

onUnmounted(() => {
  const track = trackRef.value;
  if (track) {
    track.removeEventListener("scroll", updateScrollState);
  }
  resizeObserver?.disconnect();
});
</script>

<template>
  <section
    id="services"
    class="section section-alt scroll-mt-nav overflow-hidden"
    aria-labelledby="services-heading"
  >
    <div class="container-custom">
      <header class="text-center mb-10 md:mb-14">
        <h2
          id="services-heading"
          class="inline-flex items-center justify-center gap-3 text-3xl md:text-4xl font-bold text-gold-600 font-heading"
        >
          Unsere Leistungen
          <span class="text-gold-400" aria-hidden="true">
            <svg
              class="w-7 h-7 md:w-8 md:h-8"
              viewBox="0 0 24 24"
              fill="currentColor"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M17 8C8 10 5.9 16.17 3.82 21.34L5.71 22l1.23-2.27c.48.17.98.27 1.51.27 3.31 0 6-2.69 6-6 0-.53-.1-1.03-.27-1.51L13 19.29l.66-1.89C18.83 15.1 22 8 22 8s-3-1-5-0zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"
              />
            </svg>
          </span>
        </h2>
        <div class="mt-4 mx-auto w-24 h-1 rounded-full bg-gold-400" />
      </header>

      <!-- Slider -->
      <div class="relative pt-16 pb-4">
        <div
          ref="trackRef"
          class="services-slider flex gap-4 sm:gap-6 overflow-x-auto scroll-smooth snap-x snap-mandatory pb-2 -mx-4 px-4 sm:mx-0 sm:px-0"
          role="region"
          aria-roledescription="Karussell"
          aria-label="Unsere Leistungen"
        >
          <div
            v-for="(service, index) in services"
            :key="service.id"
            data-slide
            class="services-slide snap-center shrink-0"
            :aria-label="`${index + 1} von ${services.length}: ${service.title}`"
          >
            <ServiceCard
              :title="service.title"
              :description="service.description"
              :image-src="service.imageSrc"
              :image-alt="service.imageAlt"
            />
          </div>
        </div>
      </div>

      <!-- Navigation (wie altes Design: rosa + dunkel) -->
      <div class="flex items-center justify-center gap-5 mt-6">
        <button
          type="button"
          class="services-nav-btn services-nav-btn--prev"
          aria-label="Vorherige Leistung"
          @click="goPrev"
        >
          <svg
            class="w-5 h-5"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            aria-hidden="true"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2.5"
              d="M15 19l-7-7 7-7"
            />
          </svg>
        </button>
        <button
          type="button"
          class="services-nav-btn services-nav-btn--next"
          aria-label="Nächste Leistung"
          @click="goNext"
        >
          <svg
            class="w-5 h-5"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            aria-hidden="true"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2.5"
              d="M9 5l7 7-7 7"
            />
          </svg>
        </button>
      </div>
    </div>
  </section>
</template>
