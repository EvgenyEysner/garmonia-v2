import type { RouteRecordRaw } from "vue-router";
import HomeView from "@/views/HomeView.vue";

export const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: { title: "Kosmetikstudio Garmonia: Natürliche Schönheit, die lange hält!" },
  },
  {
    path: "/datenschutz",
    name: "datenschutz",
    component: () => import("@/views/DatenschutzView.vue"),
    meta: { title: "Datenschutzerklärung" },
  },
  {
    // Unbekannte Pfade vorerst auf die Startseite leiten.
    path: "/:pathMatch(.*)*",
    redirect: { name: "home" },
  },
];
