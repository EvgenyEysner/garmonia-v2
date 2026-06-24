import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";
import HomeView from "@/views/HomeView.vue";

const NAVBAR_OFFSET = 80;

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/datenschutz",
    name: "datenschutz",
    component: () => import("@/views/DatenschutzView.vue"),
    meta: { title: "Datenschutzerklärung" },
  },
  {
    // Noch nicht umgesetzte Rechtsseiten (Impressum, AGB) sowie unbekannte
    // Pfade vorerst auf die Startseite leiten.
    path: "/:pathMatch(.*)*",
    redirect: { name: "home" },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, _from, savedPosition) {
    if (savedPosition) return savedPosition;
    if (to.hash) {
      return { el: to.hash, top: NAVBAR_OFFSET, behavior: "smooth" };
    }
    return { top: 0 };
  },
});

export default router;
