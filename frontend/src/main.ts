import { ViteSSG } from "vite-ssg";
import "./style.css";
import App from "./App.vue";
import { routes, scrollBehavior } from "./router";
import { setupAnalyticsRouter } from "@/services/analytics";

const DEFAULT_TITLE =
  "Kosmetikstudio Garmonia: Natürliche Schönheit, die lange hält!";

export const createApp = ViteSSG(
  App,
  { routes, scrollBehavior },
  ({ router, isClient }) => {
    router.afterEach((to) => {
      if (typeof document === "undefined") return;
      const routeTitle = typeof to.meta.title === "string" ? to.meta.title : null;
      document.title = routeTitle ?? DEFAULT_TITLE;
    });

    if (isClient) {
      setupAnalyticsRouter(router);
    }
  }
);
