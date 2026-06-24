import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import router from "./router";
import { setupAnalyticsRouter } from "@/services/analytics";

setupAnalyticsRouter(router);

createApp(App).use(router).mount("#app");
