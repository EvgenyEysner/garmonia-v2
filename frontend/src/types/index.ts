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
