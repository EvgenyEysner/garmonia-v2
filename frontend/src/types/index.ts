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

// Footer Interfaces
interface SocialLink {
  url: string;
  icon: string;
  name: string;
}

interface FooterLink {
  label: string;
  href: string;
}
