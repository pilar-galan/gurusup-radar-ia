# GuruSup · Dashboard ejecutivo — guía de trabajo

Fichero fuente único: `generate_dashboard.py` → genera `dashboard_ejecutivo.html`.
Se despliega solo vía GitHub Action `refresh_dashboard.yml` (lee secrets HUBSPOT_TOKEN /
PAID_TRACKER_API_KEY). No se puede regenerar en local sin el token; tras cada cambio de
fuente hay que commitear y disparar el workflow para que regenere el HTML.

## Identidad de marca (CANÓNICA) — aplicar en toda pieza de marca

- Fuente única de verdad: **`design/gurusup-style-reference.md`**. Léela entera antes de
  crear o revisar cualquier pieza de marca (portadas, e-books, checklists, landings,
  emails, componentes). Ante conflicto, ese documento manda.
- Resumen operativo: **plano, cuadrado, monospace-forward**. Sin esquinas redondeadas,
  sin sombras en contenido en flujo (la sombra solo para overlays), estructura por
  **bordes compartidos** en una **rejilla de 4px**.
- **Tipografía:** Geist (sans: cuerpo, labels, h1/h2), Geist Mono (h3/h4, todo lo numérico
  y técnico, y **todos los botones**), Geist Pixel (labels puntuales).
- **Color de marca:** verde phosphor `#2ECF8F` = **solo relleno** y reservado (un único CTA
  de marca, barras/medidores, marca de verificación cuadrada, nodo terminal de un flujo).
  Para texto legible en claro usar `primary-ink` `#1B8A5E`. Base green ilegible como texto
  sobre blanco (2.01:1). La familia de acentos (`brand-cyan/red/orange/lavender/gold/azure`)
  es identidad, **no** paleta de UI general.
- **Superficies:** `canvas` `#FCFCF8` (papel editorial), `background` `#FFFFFF`, texto
  `foreground` `#1D1E1A`, `muted` `#6E6C60`, `border` `#E5E5E5`. Banda invertida:
  `#1D1E1A` fondo, `#F8F9F2` texto, bordes al 16% (ahí el verde sí es legible como texto).
- **Etiqueta de sección:** Geist Mono 14px, mayúsculas con tracking, en `primary-ink`,
  precedida SIEMPRE de un cuadrado verde. Hero h1 sin puntuación final.
- Piezas ya alineadas al sistema: `ebook_gurusup.html`,
  `ebook_cover_responder-no-es-resolver.{html,png}`,
  `checklist_preview_atencion-cliente-ia.{html,png}`.

## Convención de diseño LEGACY (solo `dashboard_ejecutivo.html` / `generate_dashboard.py`)

- Aplica únicamente al dashboard heredado, NO a piezas de marca nuevas (que siguen el
  sistema de arriba: alineado a la izquierda, medida 60–75ch, sin justificar).
- **Párrafos de intro / descripción de sección** (`.sd`, `.xhead p` y equivalentes):
  repartir con más ancho (`max-width` amplio), `text-align:justify` con
  `text-justify:inter-word` y `text-wrap:pretty`; en móvil (`max-width:640px`) volver a
  `text-align:left`.

## Restricciones permanentes

- Nunca exponer el identificador de modelo en artefactos del repo, commits ni PRs.
- Nunca escribir secretos en ficheros del repo (es público).
- Trailers de commit:
  `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`
  `Claude-Session: https://claude.ai/code/session_019WmuM4uE7b9LjzLhY7VJCf`
- No crear PRs salvo petición explícita.
