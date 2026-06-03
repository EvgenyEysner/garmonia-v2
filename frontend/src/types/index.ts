// API Error Response (Django/DRF)
export interface ApiErrorResponse {
  message: string;
  status: number;
  errors?: Record<string, string[]>;
}

// Navbar Item
export interface NavItem {
  label: string;
  href: string;
}

// Service (Leistungen – Karten mit Bild-Header + Icon)
export interface ServiceCardItem {
  id: string;
  icon: import("vue").Component;
  image: string;
  imageAlt: string;
  title: string;
  description: string;
  treatments: string[];
  color: string;
}

// Footer
export interface SocialLink {
  url: string;
  icon: string;
  name: string;
}

export interface FooterLink {
  label: string;
  href: string;
}

// API: Kategorien & Behandlungen (Preisliste)
export interface CategoryItem {
  id: number;
  name: string;
}

export interface TreatmentItem {
  id: number;
  name: string;
  category: CategoryItem;
  description: string | null;
  price: string | null;
}

export interface PriceCategoryGroup {
  category: string;
  services: { id: number; name: string; price: string }[];
}

export interface TestimonialItem {
  id: number;
  full_name: string;
  text: string;
}

export interface ContactFormPayload {
  name: string;
  email: string;
  phone: string;
  treatment_id: number;
  message?: string;
}

export interface GalleryItem {
  id: number;
  image: string;
  description: string;
}
