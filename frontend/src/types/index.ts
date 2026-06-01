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

// Service (Leistungen)
export interface ServiceItem {
  id: string;
  title: string;
  description: string;
  imageSrc: string;
  imageAlt: string;
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
