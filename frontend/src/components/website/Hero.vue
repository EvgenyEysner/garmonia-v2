<script setup lang="ts">
import { ArrowRight, Sparkles } from "@lucide/vue";
import { scrollToContact } from "@/utils.ts";

const scrollToServices = () => {
  document.querySelector("#services")?.scrollIntoView({ behavior: "smooth" });
};
</script>

<template>
  <section
    id="home"
    class="relative pt-20 min-h-screen flex items-center overflow-hidden"
  >
    <div
      class="absolute inset-0 bg-gradient-to-br from-gold-100 via-sand-50 to-gold-50"
    />

    <div class="absolute inset-0 opacity-10">
      <div class="absolute top-20 left-10 w-72 h-72 bg-gold-400 rounded-full blur-3xl" />
      <div
        class="absolute bottom-20 right-10 w-96 h-96 bg-gold-300 rounded-full blur-3xl"
      />
    </div>

    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
      <div class="grid md:grid-cols-2 gap-12 items-center">
        <div class="space-y-8">
          <div
            class="inline-flex items-center gap-2 bg-white/80 backdrop-blur-sm px-4 py-2 rounded-full border border-gold-200"
          >
            <Sparkles class="w-4 h-4 text-gold-500 shrink-0" aria-hidden="true" />
            <span class="text-sm text-sand-700">Seit über 15 Jahren in Oldenburg</span>
          </div>

          <div class="space-y-4">
            <h1 class="text-5xl md:text-6xl font-bold text-sand-900 leading-tight">
              Schönheit &amp; <br />
              <span class="text-gold-500">Wohlbefinden</span>
            </h1>
            <p class="text-xl text-sand-600 leading-relaxed">
              Erleben Sie professionelle Kosmetik und Pflege in unserem exklusiven Studio
              im Herzen von Oldenburg.
            </p>
          </div>

          <div class="flex flex-col sm:flex-row gap-4">
            <a
              href="#contact"
              class="inline-flex items-center justify-center gap-2 bg-gold-500 text-white px-8 py-4 rounded-xl hover:bg-gold-600 transition-all duration-200 shadow-lg shadow-gold-200 hover:shadow-xl hover:shadow-gold-300 group"
              @click.prevent="scrollToContact"
            >
              <span class="font-semibold">Jetzt Termin buchen</span>
              <ArrowRight
                class="w-5 h-5 shrink-0 group-hover:translate-x-1 transition-transform"
                aria-hidden="true"
              />
            </a>
            <a
              href="#services"
              class="inline-flex items-center justify-center gap-2 bg-white text-sand-900 px-8 py-4 rounded-xl hover:bg-sand-50 transition-all duration-200 border border-sand-200"
              @click.prevent="scrollToServices"
            >
              <span class="font-semibold">Unsere Leistungen</span>
            </a>
          </div>

          <div class="grid grid-cols-3 gap-8 pt-8 border-t border-sand-200">
            <div>
              <div class="text-3xl font-bold text-gold-500">500+</div>
              <div class="text-sm text-sand-600">Zufriedene Kunden</div>
            </div>
            <div>
              <div class="text-3xl font-bold text-gold-500">15+</div>
              <div class="text-sm text-sand-600">Jahre Erfahrung</div>
            </div>
            <div>
              <div class="text-3xl font-bold text-gold-500">Über 40</div>
              <div class="text-sm text-sand-600">Unterschiedliche Behandlungen</div>
            </div>
          </div>
        </div>

        <div class="relative">
          <div class="relative rounded-3xl overflow-hidden shadow-2xl">
            <img
              src="/images/hero-960.webp"
              srcset="
                /images/hero-640.webp   640w,
                /images/hero-960.webp   960w,
                /images/hero-1280.webp 1280w
              "
              sizes="(min-width: 768px) 50vw, 100vw"
              alt="Kosmetikstudio Schönheitsecke Oldenburg"
              class="w-full h-[600px] object-cover"
              width="1280"
              height="478"
              loading="lazy"
              decoding="async"
            />
            <div
              class="absolute inset-0 bg-gradient-to-t from-sand-900/20 to-transparent"
            />
          </div>

          <!--          <div class="absolute -bottom-6 -right-6 bg-white p-6 rounded-2xl shadow-xl">-->
          <!--            <div class="flex items-center gap-3">-->
          <!--              <div class="flex -space-x-2">-->
          <!--                <div-->
          <!--                  v-for="i in 3"-->
          <!--                  :key="`avatar-${i}`"-->
          <!--                  class="w-10 h-10 rounded-full bg-gradient-to-br from-gold-300 to-gold-500 border-2 border-white"-->
          <!--                />-->
          <!--              </div>-->
          <!--              <div>-->
          <!--                <div class="flex gap-1">-->
          <!--                  <Star-->
          <!--                    v-for="i in 5"-->
          <!--                    :key="`star-${i}`"-->
          <!--                    class="w-4 h-4 fill-gold-500 text-gold-500 shrink-0"-->
          <!--                    aria-hidden="true"-->
          <!--                  />-->
          <!--                </div>-->
          <!--                <p class="text-sm text-sand-600 mt-1">500+ Bewertungen</p>-->
          <!--              </div>-->
          <!--            </div>-->
          <!--          </div>-->
        </div>
      </div>
    </div>
  </section>
</template>
