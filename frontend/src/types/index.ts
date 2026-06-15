// API Error Response (Django/DRF)
import type { LucideIcon } from "@lucide/vue";

export interface ApiErrorResponse {
  message: string;
  status: number;
  errors?: Record<string, string[]>;
}

export interface NavItem {
  label: string;
  href: string;
}

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

export interface SocialLink {
  url: string;
  icon: string;
  name: string;
}

export interface FooterLink {
  label: string;
  href: string;
}

export interface CategoryItem {
  id: number;
  name: string;
}

export interface TreatmentItem {
  id: number;
  name: string;
  category: CategoryItem;
  description: string | null;
  price: string;
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

export interface MonthlyOfferItem {
  id: number;
  image: string;
  treatment: TreatmentItem;
  title: string;
  description: string;
  active: boolean;
  price: string;
}

export interface FeaturesItem {
  id: number;
  icon: LucideIcon;
  title: string;
  description: string;
}

export interface BrandItem {
  name: string;
  img: string;
  description: string;
}

export interface ContactItem {
  addressLine1: string;
  addressLine2: string;
  phone: string;
  phoneHref: string;
  email: string;
  emailHref: string;
  hoursWeekdays: string;
  hoursNote: string;
  vatId: string;
}

export interface TopSellerItem {
  name: string;
  category: string;
  price: string;
  duration: string;
  rating: number;
  reviews: number;
  description: string;
  image: string;
}
