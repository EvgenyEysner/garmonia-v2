import type {
  BrandItem,
  ContactItem,
  FeaturesItem,
  FooterLink,
  NavItem,
  ServiceCardItem,
  SocialLink,
  TopSellerItem,
} from "@/types";
import {
  Award,
  Droplet,
  Eye,
  Footprints,
  Hand,
  Heart,
  Sparkles,
  Users,
} from "@lucide/vue";
import marke1 from "@/assets/images/marken/marke_1.webp";
import marke2 from "@/assets/images/marken/marke_2.webp";
import marke3 from "@/assets/images/marken/marke_3.webp";
import marke4 from "@/assets/images/marken/marke_4.webp";
import marke5 from "@/assets/images/marken/marke_5.webp";
import service1 from "@/assets/images/service-1.webp";
import service2 from "@/assets/images/service-2.webp";
import service3 from "@/assets/images/service-3.webp";
import service4 from "@/assets/images/service-4.webp";
import service5 from "@/assets/images/service-5.webp";
import service6 from "@/assets/images/service-6.webp";

export const navItems: NavItem[] = [
  { label: "Home", href: "#home" },
  { label: "Über uns", href: "#about" },
  { label: "Leistungen", href: "#services" },
  { label: "Galerie", href: "#gallery" },
  { label: "Preise", href: "#pricing" },
  { label: "Team", href: "#team" },
  { label: "Kontakt", href: "#contact" },
];

export const contact: ContactItem = {
  addressLine1: "Bahnhofsplatz 2a, 2. OG",
  addressLine2: "26122 Oldenburg",
  phone: "+49 179 7716648",
  phoneHref: "tel:+491797716648",
  email: "garmonia.eisner@gmail.com",
  emailHref: "mailto:garmonia.eisner@gmail.com",
  hoursWeekdays: "Montag - Freitag: 10:00 - 18:00 Uhr",
  hoursNote: "Termine nach Vereinbarung",
  vatId: "DE320418012",
};

export const socialLinks: SocialLink[] = [
  { name: "Instagram", url: "https://www.instagram.com/olga.eisner/", icon: "instagram" },
  { name: "Facebook", url: "https://www.facebook.com/evgeny.eisner/", icon: "facebook" },
];

export const footerLinks: FooterLink[] = [
  { label: "Impressum", href: "/impressum" },
  { label: "Datenschutz", href: "/datenschutz" },
  { label: "AGB", href: "/agb" },
];

export const features: FeaturesItem[] = [
  {
    id: 1,
    icon: Award,
    title: "Staatl. geprüfte Kosmetikerin",
    description: "Professionelle Ausbildung und kontinuierliche Weiterbildung",
  },
  {
    id: 2,
    icon: Heart,
    title: "Individuelle Beratung",
    description: "Persönliche Behandlungskonzepte für Ihre Bedürfnisse",
  },
  {
    id: 3,
    icon: Users,
    title: "Erfahrung seit 2010",
    description: "Über 15 Jahre Expertise in der Schönheitspflege",
  },
  {
    id: 4,
    icon: Sparkles,
    title: "Premium Produkte",
    description: "Hochwertige Markenprodukte für optimale Ergebnisse",
  },
];

export const brands: BrandItem[] = [
  {
    name: "Dermalogica",
    img: marke1,
    description: "Premium Hautpflege",
  },
  {
    name: "Environ",
    img: marke2,
    description: "Vitamin A Skincare",
  },
  {
    name: "Dr. Grandel",
    img: marke3,
    description: "Professionelle Kosmetik",
  },
  {
    name: "Jane Iredale",
    img: marke4,
    description: "Mineral Make-Up",
  },
  {
    name: "Premium Partner",
    img: marke5,
    description: "Hochwertige Pflegeprodukte",
  },
];

export const services: ServiceCardItem[] = [
  {
    id: "cosmetic",
    icon: Sparkles,
    image: service1,
    imageAlt: "Kosmetische Gesichtsbehandlung im Studio",
    title: "Kosmetische Behandlungen",
    description: "Anti-Aging, Hydra Facial, Micro Needling, Peelings und mehr",
    treatments: [
      "Hydra Facial",
      "BioRePeel",
      "Micro Needling",
      "Retinol Peel",
      "Diamant Mikrodermabrasion",
    ],
    color: "from-gold-400 to-gold-600",
  },
  {
    id: "permanent-makeup",
    icon: Eye,
    image: service2,
    imageAlt: "Permanent Make Up Behandlung",
    title: "Permanent Make-Up",
    description: "Augenbrauen, Lippen und Eyeliner - natürlich schön",
    treatments: ["Augenbrauen", "Lippen", "Eyeliner", "Nachbehandlung"],
    color: "from-gold-300 to-gold-500",
  },
  {
    id: "hair-removal",
    icon: Sparkles,
    image: service3,
    imageAlt: "Professionelle Körperenthaarung",
    title: "Körperenthaarung",
    description: "Schonende Haarentfernung für alle Körperbereiche",
    treatments: ["Gesicht", "Beine", "Arme", "Achseln", "Bikinizone"],
    color: "from-gold-500 to-gold-700",
  },
  {
    id: "foot-care",
    icon: Footprints,
    image: service4,
    imageAlt: "Professionelle Fußpflege und Pediküre",
    title: "Fußpflege",
    description: "Medizinische und kosmetische Fußpflege",
    treatments: [
      "Pediküre",
      "Express Pediküre",
      "Hühneraugen-Entfernung",
      "Nagelkorrektur",
    ],
    color: "from-gold-400 to-gold-600",
  },
  {
    id: "nail-design",
    icon: Hand,
    image: service5,
    imageAlt: "Kreatives Nageldesign und Modellage",
    title: "Nageldesign",
    description: "Professionelle Maniküre und Nagelmodellage",
    treatments: [
      "Gel-Modellage",
      "Nagelverlängerung",
      "French Design",
      "Babyboomer",
      "Express-Maniküre",
    ],
    color: "from-gold-500 to-gold-700",
  },
  {
    id: "lashes",
    icon: Droplet,
    image: service6,
    imageAlt: "Wimpernlifting und Augenbrauen-Styling",
    title: "Wimpern & Augen",
    description: "Wimpernlifting, Färben und Augenbrauen-Styling",
    treatments: [
      "Wimpernlifting",
      "Wimpern färben",
      "Augenbrauen färben",
      "Augenbrauen zupfen",
    ],
    color: "from-gold-300 to-gold-500",
  },
];

export const treatments: TopSellerItem[] = [
  {
    name: "Fußpflege",
    category: "Fußpflege",
    price: "Ab 25€",
    duration: "30 - 60 Min",
    rating: 5,
    reviews: 124,
    description:
      "Verwöhnung bis in die Zehenspitzen - erleben Sie eine luxuriöse Fußpflege, die intensive Regeneration mit ästhetischer Perfektion verbindet.",
    image: service4,
  },
  {
    name: "Nagelmodellage",
    category: "Nageldesign",
    price: "Ab 45€",
    duration: "60 - 90  Min",
    rating: 5,
    reviews: 89,
    description:
      "Ob natürlicher Look, klassisches French oder aufwendige Nail-Art – wir verwandeln Ihre Fingernägel in langanhaltende Kunstwerke mit absolutem Wohlfühlfaktor.",
    image: service5,
  },
  {
    name: "Gesichtsbehandlung",
    category: "Kosmetische Behandlungen",
    price: "Ab 55€",
    duration: "45 - 60 Min",
    rating: 5,
    reviews: 156,
    description:
      "Schenken Sie Ihrer Haut ein neues Strahlen: Unsere maßgeschneiderten Gesichtsbehandlungen verbinden Tiefenreinigung, intensive Pflege und pure Entspannung für einen sichtbar frischen, vitalen Teint.",
    image: service1,
  },
  {
    name: "Körperenthaarung mit Wachs",
    category: "Körperenthaarung",
    price: "Ab 20€",
    duration: "15 - 60 Min",
    rating: 5,
    reviews: 201,
    description:
      "Erleben Sie das Gefühl makellos glatter Haut: Unsere professionelle Haarentfernung mit Warmwachs entfernt lästige Härchen besonders gründlich und sorgt für wochenlange, seidige Frische.",
    image: service3,
  },
];
