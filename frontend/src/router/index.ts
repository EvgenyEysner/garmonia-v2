import type { RouterScrollBehavior } from "vue-router";
import { routes } from "./routes";

export const NAVBAR_OFFSET = 80;

export const scrollBehavior: RouterScrollBehavior = (to, _from, savedPosition) => {
  if (savedPosition) return savedPosition;
  if (to.hash) {
    return { el: to.hash, top: NAVBAR_OFFSET, behavior: "smooth" };
  }
  return { top: 0 };
};

export { routes };
