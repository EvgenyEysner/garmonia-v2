import axios, { type AxiosError, type AxiosInstance } from "axios";
import type {
  ApiErrorResponse,
  ContactFormPayload,
  GalleryItem,
  MonthlyOfferItem,
  TestimonialItem,
  TreatmentItem,
} from "@/types";
import { getCookie } from "@/utils";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

const apiClient: AxiosInstance = axios.create({
  baseURL: `${API_BASE_URL}/api`,
  timeout: 10000,
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true, // Für Django CSRF-Token & Session
});

/**
 * Request-Interceptor
 * add CSRF-Token to the request (for Django)
 */
apiClient.interceptors.request.use(
  (config) => {
    // CSRF-Token aus Cookie holen (Django setzt das)
    const csrfToken = getCookie("csrftoken");
    if (csrfToken) {
      config.headers["X-CSRFToken"] = csrfToken;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response-Interceptor
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error: AxiosError) => {
    const apiError: ApiErrorResponse = {
      message: "Ein Fehler ist aufgetreten",
      status: error.response?.status ?? 500,
    };

    if (error.response) {
      const data = error.response.data as
        | { message?: string; errors?: Record<string, string[]> }
        | undefined;
      apiError.message = data?.message ?? error.message;
      apiError.errors = data?.errors;
    } else if (error.request) {
      apiError.message = "Server ist nicht erreichbar";
    }

    return Promise.reject(apiError);
  }
);

export const websiteApi = {
  sendContactForm: (data: ContactFormPayload) => {
    return apiClient.post("/contact/", data);
  },

  getServices: () => {
    return apiClient.get("/services/");
  },

  getTreatments: () => {
    return apiClient.get<TreatmentItem[]>("/treatment/");
  },

  getGalleryImages: () => {
    return apiClient.get<GalleryItem[]>("/gallery/");
  },

  getTestimonials: () => {
    return apiClient.get<TestimonialItem[]>("/testimonial/");
  },

  getMonthlyOffer: () => {
    return apiClient.get<MonthlyOfferItem[]>("/monthly-offer/");
  },
};
