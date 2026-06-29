/**
 * Bild-Optimierung fuer PageSpeed (Mobile).
 *
 * - Verkleinert ueberdimensionierte Quellbilder auf ihre tatsaechliche
 *   Anzeigegroesse und schreibt sie als WebP neu (in-place).
 * - Erzeugt responsive Hero-Varianten in public/images/ fuer srcset + Preload.
 *
 * Idempotent: Bilder, die bereits klein genug sind, werden uebersprungen
 * (sharp upscaled per Default nicht).
 *
 * Ausfuehren:  node scripts/optimize-images.mjs
 */
import { fileURLToPath } from "url";
import path from "path";
import { readFile, writeFile, mkdir } from "fs/promises";
import sharp from "sharp";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "..");

const assets = path.join(root, "src", "assets", "images");
const publicImages = path.join(root, "public", "images");

/** In-place verkleinerte Inhaltsbilder (Quelle = Ziel). */
const inPlace = [
  { file: path.join(assets, "about", "about-2.webp"), width: 512, quality: 72 },
  { file: path.join(assets, "about", "about-3.webp"), width: 512, quality: 72 },
  { file: path.join(assets, "about", "about-4.webp"), width: 640, quality: 72 },
  { file: path.join(assets, "marken", "marke_3.webp"), width: 270, quality: 80 },
];

/** Responsive Hero-Varianten fuer das LCP-Bild. */
const heroSource = path.join(assets, "home-header.webp");
const heroWidths = [640, 960, 1280];
const heroQuality = 74;

function formatKb(bytes) {
  return `${(bytes / 1024).toFixed(1)} KB`;
}

async function resizeInPlace({ file, width, quality }) {
  const input = await readFile(file);
  const meta = await sharp(input).metadata();
  if (meta.width && meta.width <= width) {
    console.log(`skip   ${path.relative(root, file)} (bereits ${meta.width}px)`);
    return;
  }
  const out = await sharp(input)
    .resize({ width, withoutEnlargement: true })
    .webp({ quality })
    .toBuffer();
  await writeFile(file, out);
  console.log(
    `resize ${path.relative(root, file)}  ${meta.width}px -> ${width}px  ` +
      `${formatKb(input.length)} -> ${formatKb(out.length)}`,
  );
}

async function buildHeroVariants() {
  await mkdir(publicImages, { recursive: true });
  const input = await readFile(heroSource);
  for (const width of heroWidths) {
    const out = await sharp(input)
      .resize({ width, withoutEnlargement: true })
      .webp({ quality: heroQuality })
      .toBuffer();
    const target = path.join(publicImages, `hero-${width}.webp`);
    await writeFile(target, out);
    console.log(
      `hero   ${path.relative(root, target)}  ${width}px  ${formatKb(out.length)}`,
    );
  }
}

async function main() {
  for (const item of inPlace) {
    await resizeInPlace(item);
  }
  await buildHeroVariants();
  console.log("Fertig.");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
