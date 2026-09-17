# Raster provenance — assets/img

Every file here also carries its provenance embedded as PNG tEXt / JPEG comment (`impeccable embed-prompt --scan assets/img` reports 0 missing).

| File(s) | Origin |
|---|---|
| `ill-box, ill-emptybox, ill-globe, ill-cactus, ill-mic, ill-bubbles, ill-notebook, ill-sun, ill-plane` | Generated 2026-09-16 on Higgsfield, model `nano_banana_pro`; prompt: flat mid-century paper-cut vector illustration, limited palette (#F4C542 / #D9A22E / #A8B79A / #D4784A / #2B2A28), no gradients/outlines/shadows/text, isolated on white. White keyed to alpha with Pillow edge floodfill. Originals in `assets/gen/` (git-ignored). |
| `logo-mark*.png` | Jennifer's original `eotb-logo-smaller.png` refined on Higgsfield (`nano_banana_pro`, image reference + "refine, keep composition and hand-lettered personality, flat single mustard, no gradients"), recolored #E9B22E / #2B2A28, white keyed to alpha. |
| `logo-bold.png`, `favicon.png`, `apple-touch-icon.png`, `icon-512.png` | Same brief on Higgsfield `gpt_image_2_5` (bold variant); checkerboard keyed to alpha; icons composed with Pillow. |
| `jennifer-tada.png` | Jennifer's own studio photo `IMG_1840.jpg`; white keyed to alpha with Pillow. Not AI-generated. |
| `og.jpg` | Composed with Pillow from the sun field, the bold logo, and `Jenna-111`. |
| `eotb-logo-smaller.png` | Her original logo (2016), kept for reference. |
| everything else (`Jenna-*.jpg`, `IMG_*.jpg`, course covers, `Reviews*.png`, screenshots, `podcast-.png`, `nightconnections-2.jpg`, …) | Jennifer's own uploads from `englishoutsidethebox.com/wp-content/uploads/`, downloaded 2026-09-16 and resized. Not AI-generated. |
| `../blog/*` | Her blog post images, same source, hash-prefixed to avoid collisions. |
