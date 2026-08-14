# GuruSup · Dashboard ejecutivo — guía de trabajo

Fichero fuente único: `generate_dashboard.py` → genera `dashboard_ejecutivo.html`.
Se despliega solo vía GitHub Action `refresh_dashboard.yml` (lee secrets HUBSPOT_TOKEN /
PAID_TRACKER_API_KEY). No se puede regenerar en local sin el token; tras cada cambio de
fuente hay que commitear y disparar el workflow para que regenere el HTML.

## Convenciones de diseño (aplicar SIEMPRE, también en peticiones nuevas)

- **Párrafos de introducción / descripción de sección** (`.sd`, `.xhead p` y equivalentes):
  no deben quedar apelotonados a la izquierda. Repartir el texto usando más ancho
  (`max-width` amplio, ~92ch en secciones, ~1040px en el hero), `text-align:justify`
  con `text-justify:inter-word` y `text-wrap:pretty`, para que queden equilibrados,
  justificados y visualmente repartidos. En móvil (`max-width:640px`) volver a
  `text-align:left` para evitar ríos de espacio.
- Mantener este estilo de párrafo equilibrado/justificado en cualquier bloque de texto
  introductorio o explicativo que se añada en el futuro.

## Portadilla común de materiales (aplicar a TODOS los contenidos)

A partir de ahora **todos los materiales** (infografías, guías, checklists, eBooks,
embudos y cualquier pieza nueva) deben abrir con la **misma portadilla / identidad visual**:

- **Cabecera a sangre (full-bleed), 100 % de ancho**, sin márgenes blancos ni aspecto de
  "card". Fondo **azul navy oscuro** (`--hero-bg: #0a162e`).
- **Eyebrow arriba**: en **coral, mayúsculas y tamaño pequeño**, indica el **formato**
  (INFOGRAFÍA / GUÍA / CHECKLIST / EBOOK…) y el ámbito (p. ej. `· AGENTES IA PARA CUSTOMER SERVICE`).
- **Titular en blanco**, destacando la **palabra clave en coral** (`--accent: #fe715d`),
  normalmente en serif itálica `.accent-serif` (Georgia).
- **Iconografía/ilustración a la derecha** que ilustre el contenido de la izquierda
  (p. ej. clipboard con checks para un checklist, círculo de iconos para una infografía).
- **Debajo del titular, 1–2 líneas** (no párrafos) que introduzcan de qué va el contenido inferior.
- Paleta común: navy `#0a162e`, texto blanco, acento coral `#fe715d` / `--accent-ink #d64b36`,
  buenos secundarios verde `#2f9e63` (positivo) y periwinkle `#6a5ce0` (novedad/Brain).
- Los fuentes de estos materiales viven en el scratchpad de sesión
  (`build_info.py` = infografía, `build_checklist.py` = checklist, `build.py` = embudo);
  cada uno renderiza su HTML y su PDF vía Playwright/PyMuPDF.

## Restricciones permanentes

- Nunca exponer el identificador de modelo en artefactos del repo, commits ni PRs.
- Nunca escribir secretos en ficheros del repo (es público).
- Trailers de commit:
  `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`
  `Claude-Session: https://claude.ai/code/session_019WmuM4uE7b9LjzLhY7VJCf`
- No crear PRs salvo petición explícita.
