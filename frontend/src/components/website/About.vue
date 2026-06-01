<script setup lang="ts"></script>
<template>
  <section
    id="about"
    class="relative flex items-center justify-center min-h-screen bg-gradient-gold"
  >
    <!-- Background overlay -->
    <div class="absolute inset-0 bg-black/30"></div>
    <div
      class="relative z-10 w-full lg:w-5/12 overflow-hidden rounded-2xl shadow-medium transition-all duration-300 ease-in-out"
    >
      <img
        src="@/assets/images/welcom-spa.webp"
        alt="Entspannende Atmosphäre im Kosmetikstudio Garmonia"
        class="block w-full h-auto object-cover"
        loading="lazy"
      />
    </div>
    <!-- Content -->
    <div class="relative z-10 max-w-4xl mx-auto px-4 text-center text-white">
      <h1
        class="text-4xl md:text-5xl lg:text-6xl font-bold mb-6 drop-shadow-lg animate-slide-up"
      >
        Ihr Kosmetikstudio<br />
        <span class="text-gold-300" style="text-transform: uppercase"># 1</span> in
        Oldenburg
      </h1>
      <div class="container-custom">
        <div class="max-w-3xl mx-auto text-left">
          <p class="text-lg text-sand-600 leading-relaxed">
            Das klingt nach einem umfassenden Angebot an Schönheitsbehandlungen!
            Gesichtsbehandlung kann dabei helfen, die Haut zu reinigen, zu pflegen und zu
            regenerieren. Nageldesign bietet eine Vielzahl von Möglichkeiten, um Ihre
            Nägel zu verschönern und zu gestalten. Mit Permanent Make-up können Sie Ihre
            Augenbrauen, Lippen oder Lidstriche langanhaltend betonen. Und eine
            professionelle Fußpflege sorgt dafür, dass Ihre Füße gepflegt und gesund
            bleiben. Gönnen Sie sich eine Auszeit und lassen Sie sich von den Experten im
            Kosmetikstudio verwöhnen!
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
