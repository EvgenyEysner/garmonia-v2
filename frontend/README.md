# Garmonia Frontend

Single-page marketing website for Kosmetikstudio Garmonia / Schoenheitsecke Oldenburg, built with Vue 3 and Vite. The site is statically pre-rendered (SSG) for fast loading and good SEO, and it consumes content from the [backend API](../backend/README.md).

---

## Table of contents

- [Technology stack](#technology-stack)
- [Project structure](#project-structure)
- [Local development](#local-development)
- [Available scripts](#available-scripts)
- [Environment variables](#environment-variables)
- [Static site generation](#static-site-generation)
- [Routing](#routing)
- [API client](#api-client)
- [Analytics and cookie consent](#analytics-and-cookie-consent)
- [Styling](#styling)
- [Production build and Docker](#production-build-and-docker)

---

## Technology stack

- Vue 3 (`<script setup>` SFCs) with TypeScript
- Vite 7 as the build tool
- vite-ssg for static site generation (pre-rendering)
- Tailwind CSS 4
- Pinia for state management
- Vue Router 5
- Axios for HTTP requests
- Leaflet for the interactive location map
- Lucide icons
- ESLint and Prettier for linting and formatting

---

## Project structure

```
frontend/
├── public/                  Static assets served as-is
│   ├── robots.txt
│   ├── sitemap.xml
│   └── images/              Logo, Open Graph images, favicon
├── src/
│   ├── api/client.ts        Axios instance and typed API methods
│   ├── assets/              Images and fonts bundled by Vite
│   ├── components/
│   │   ├── common/          Navbar, Footer, CookieBanner, FABs, ScrollToTop
│   │   └── website/         Page sections (Hero, About, Services, Gallery, ...)
│   ├── composables/
│   │   └── useCookieConsent.ts   Consent state management (GDPR/TTDSG)
│   ├── services/
│   │   └── analytics.ts     Google Analytics 4 with Consent Mode
│   ├── views/
│   │   ├── HomeView.vue      Landing page
│   │   └── DatenschutzView.vue   Privacy policy page
│   ├── router/              Route definitions and router setup
│   ├── content.ts           Static site content (navigation, brands, contact)
│   ├── types/index.ts       Shared TypeScript types
│   ├── utils.ts             Helper functions
│   ├── App.vue
│   ├── main.ts              ViteSSG entry point
│   └── style.css            Tailwind entry and global styles
├── docs/SSG-SETUP.md        Notes on the SSG setup
├── Dockerfile               Multi-stage build -> static files served by Nginx
├── nginx.conf               Nginx config used inside the frontend image
├── index.html               HTML shell with meta tags, Open Graph, JSON-LD
├── vite.config.ts
└── package.json
```

---

## Local development

Prerequisites: Node.js 24 and npm.

```bash
cd frontend
npm install
npm run dev
```

The dev server runs at `http://localhost:5173`. It calls the backend at the URL defined by `VITE_API_BASE_URL`, so make sure the backend is running and reachable (default `http://localhost:8000`).

---

## Available scripts

| Script             | Description                                              |
| ------------------ | -------------------------------------------------------- |
| `npm run dev`      | Start the Vite development server                        |
| `npm run build`    | Type-check (`vue-tsc`) and build the SSG site            |
| `npm run preview`  | Preview the production build locally                     |
| `npm run lint`     | Run ESLint                                               |
| `npm run lint:fix` | Run ESLint with auto-fix                                 |
| `npm run format`   | Format source files with Prettier                       |

---

## Environment variables

Vite environment variables are read from `frontend/.env` and are inlined at build time. They must be prefixed with `VITE_`.

| Variable                | Description                                            | Example                  |
| ----------------------- | ------------------------------------------------------ | ------------------------ |
| `VITE_API_BASE_URL`     | Base URL of the backend (without the `/api` suffix)    | `http://localhost:8000`  |
| `VITE_STUDIO_LOCATION`  | `latitude,longitude` for the Leaflet map               | `53.1428031,8.2226412`   |
| `VITE_GA4_ID`           | Google Analytics 4 measurement ID                      | `G-XXXXXXXXXX`           |

The API client appends `/api` to `VITE_API_BASE_URL` automatically.

For production builds these values are passed as Docker build arguments (see [Production build and Docker](#production-build-and-docker)).

---

## Static site generation

The site is pre-rendered with vite-ssg. The entry point in `src/main.ts` exports `createApp` via `ViteSSG` instead of mounting directly, which lets the build crawl routes and emit static HTML.

Routes to pre-render are configured in `vite.config.ts`:

```ts
ssgOptions: {
  formatting: "minify",
  includedRoutes() {
    return ["/", "/datenschutz"];
  },
}
```

The build (`npm run build`) produces a `dist/` directory containing `index.html`, `datenschutz.html` and hashed asset bundles. Code that depends on browser-only APIs (for example Leaflet) is imported dynamically and guarded so it does not run during server-side pre-rendering.

See [`docs/SSG-SETUP.md`](docs/SSG-SETUP.md) for details and for how to add a new pre-rendered route.

---

## Routing

Routes are defined in `src/router/routes.ts`:

| Path           | Name          | View                  | Notes                          |
| -------------- | ------------- | --------------------- | ------------------------------ |
| `/`            | `home`        | `HomeView.vue`        | Landing page with all sections |
| `/datenschutz` | `datenschutz` | `DatenschutzView.vue` | Privacy policy                 |
| `/:pathMatch(.*)*` | -         | redirect to `home`    | Unknown paths redirect home    |

The document title is set per route via `router.afterEach` in `main.ts`, falling back to a default title.

---

## API client

`src/api/client.ts` exports a configured Axios instance and a typed `websiteApi` object. Key points:

- Base URL is `${VITE_API_BASE_URL}/api` with a 10-second timeout.
- A request interceptor attaches the Django CSRF token from cookies when present.
- A response interceptor normalizes errors into a consistent `ApiErrorResponse` shape.
- A `unwrapList` helper transparently handles both plain-array and paginated (`{ results: [] }`) responses.

Available methods: `sendContactForm`, `getTreatments`, `getGalleryImages`, `getTestimonials`, `getMonthlyOffer`.

---

## Analytics and cookie consent

The site implements GDPR/TTDSG-compliant consent before loading any non-essential scripts.

- `src/composables/useCookieConsent.ts` manages consent state. Necessary cookies are always active; optional categories (`analytics`, `externalMedia`) require explicit opt-in. The decision is stored in `localStorage` under `garmonia_cookie_consent` with a version field so the banner can be re-shown when the policy changes.
- `src/services/analytics.ts` integrates Google Analytics 4 using Consent Mode. Analytics only loads when `VITE_GA4_ID` is set, the build is a production build, and the visitor has granted the analytics category. Single-page navigations are tracked via the router.
- `src/components/common/CookieBanner.vue` renders the banner and settings dialog. The footer exposes a button to reopen the settings at any time.

---

## Styling

Styling uses Tailwind CSS 4 via the `@tailwindcss/vite` plugin. The global entry is `src/style.css`. The salon's color palette (gold/sand tones) is shared conceptually with the Django admin theme so the public site and the admin look consistent.

---

## Production build and Docker

The `Dockerfile` is a multi-stage build: it builds the static site with Node and serves the result with Nginx.

Build arguments (with defaults) control the inlined environment values:

- `VITE_API_BASE_URL` (default `https://schoenheitsecke-oldenburg.de`)
- `VITE_STUDIO_LOCATION`
- `VITE_GA4_ID`

The runtime stage serves `dist/` with the `nginx.conf` in this directory, which handles SSG routing (for example mapping `/datenschutz` to `datenschutz.html`), long-lived caching for hashed assets, gzip, and a sensible SPA fallback.

In the full stack the frontend container only exposes port `80` internally; the top-level Nginx reverse proxy terminates TLS and forwards requests to it. See the [root README](../README.md) for the complete Docker Compose setup and deployment workflow.
