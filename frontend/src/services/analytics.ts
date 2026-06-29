import type { Router } from "vue-router";

declare global {
  interface Window {
    dataLayer?: unknown[];
    gtag?: (...args: unknown[]) => void;
  }
}

const GA4_ID = import.meta.env.VITE_GA4_ID as string | undefined;

let scriptRequested = false;
let configured = false;

function isEnabled(): boolean {
  return Boolean(GA4_ID && import.meta.env.PROD);
}

function ensureGtagStub(): void {
  window.dataLayer = window.dataLayer ?? [];
  if (!window.gtag) {
    // gtag.js erwartet das `arguments`-Objekt im dataLayer. Ein per Spread
    // erzeugtes Array (`(...args) => push(args)`) wird NICHT als Befehl erkannt,
    // wodurch consent/js/config/event ignoriert würden.
    window.gtag = function gtag() {
      // eslint-disable-next-line prefer-rest-params
      window.dataLayer!.push(arguments);
    };
  }
}

function setDefaultConsent(): void {
  ensureGtagStub();
  window.gtag!("consent", "default", {
    analytics_storage: "denied",
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
    wait_for_update: 500,
  });
}

export function updateAnalyticsConsent(granted: boolean): void {
  if (!isEnabled()) return;

  ensureGtagStub();
  window.gtag!("consent", "update", {
    analytics_storage: granted ? "granted" : "denied",
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
  });
}

function configureAnalytics(): void {
  if (!isEnabled() || !GA4_ID || configured) return;

  window.gtag!("js", new Date());
  window.gtag!("config", GA4_ID, { send_page_view: false });
  configured = true;
  trackPageView(window.location.pathname + window.location.search);
}

function loadAnalyticsScript(): void {
  if (!isEnabled() || !GA4_ID || scriptRequested) return;

  scriptRequested = true;
  setDefaultConsent();

  const script = document.createElement("script");
  script.src = `https://www.googletagmanager.com/gtag/js?id=${GA4_ID}`;
  script.async = true;
  script.onload = () => configureAnalytics();
  document.head.appendChild(script);
}

export function enableAnalytics(): void {
  if (!isEnabled()) return;

  loadAnalyticsScript();
  updateAnalyticsConsent(true);

  if (configured) {
    trackPageView(window.location.pathname + window.location.search);
  }
}

export function disableAnalytics(): void {
  updateAnalyticsConsent(false);
}

export function trackPageView(pagePath: string): void {
  if (!isEnabled() || !configured || !GA4_ID) return;

  window.gtag!("event", "page_view", {
    page_path: pagePath,
    page_location: window.location.href,
    page_title: document.title,
  });
}

export function setupAnalyticsRouter(router: Router): void {
  router.afterEach((to) => {
    trackPageView(to.fullPath);
  });
}
