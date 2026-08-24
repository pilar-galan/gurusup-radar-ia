# GuruSup · Dashboard ejecutivo — guía de trabajo

Fichero fuente único: `generate_dashboard.py` → genera `dashboard_ejecutivo.html`.
Se despliega solo vía GitHub Action `refresh_dashboard.yml` (lee secrets HUBSPOT_TOKEN /
PAID_TRACKER_API_KEY). No se puede regenerar en local sin el token; tras cada cambio de
fuente hay que commitear y disparar el workflow para que regenere el HTML.

## Sistema de diseño GuruSup (aplicar SIEMPRE, también en materiales nuevos)

Desde 2026-08 el dashboard usa el sistema de diseño oficial de GuruSup (referencia
`gurusup-style-reference`, tema oscuro): flat, cuadrado, monospace-forward, sin
sombras de elevación salvo en overlays flotantes (popover, toast, gate de contraseña).
Los dos bloques `:root` de `generate_dashboard.py` (uno para `EXEC_CSS`, otro para
`TEMPLATE`) son la fuente de verdad de los tokens; cualquier color nuevo se añade ahí,
nunca como hex suelto en una regla.

- **Color** — fondo `#1D1E1A`, tarjeta `#24261F`, borde `#34362C`, texto `#F8F9F2`,
  texto atenuado `#BEBBB2`. Marca primaria (verde fósforo) `#2ECF8F` para fills,
  rings y section labels; su paso oscuro `#1B8A5E` para bordes/underlines. Éxito
  `#34D399`, error `#FF9F8F`, ámbar `#E2B85B`. Paleta categórica cerrada de 8 colores
  (`chart-1`…`chart-8`: sky/amber/cyan/orange/mint/rose/lime/coral) para distinguir
  canales, fuentes o categorías — nunca inventar un hex nuevo para eso, reasignar uno
  existente. Texto sobre un fill verde/ámbar siempre usa tinta oscura `#1D1E1A`,
  nunca blanco (el verde de marca falla el contraste con blanco).
- **Tipografía** — Geist Sans (`var(--font-sans)`) para texto general, cargada vía
  jsDelivr (`@fontsource-variable/geist`). Geist Mono (`var(--font-mono)`) para todo
  dato numérico (`.tnum`, valores de KPI) y para botones/pestañas, cargada vía
  `@fontsource-variable/geist-mono`.
- **Forma** — cero radio de esquina en todo el documento (`border-radius:0`); solo
  los círculos reales (puntos de estado, thumb de un slider) usan `50%`. La
  estructura entre bloques del mismo rango viene de un borde compartido, nunca de
  gradiente + sombra.
- Estas reglas aplican a cualquier material nuevo de GuruSup (dashboards, informes,
  landings, emails de Discord/reporting): reutilizar los tokens de arriba en vez de
  colores o formas ad hoc.

## Convenciones de diseño (aplicar SIEMPRE, también en peticiones nuevas)

- **Párrafos de introducción / descripción de sección** (`.sd`, `.xhead p` y equivalentes):
  no deben quedar apelotonados a la izquierda. Repartir el texto usando más ancho
  (`max-width` amplio, ~92ch en secciones, ~1040px en el hero), `text-align:justify`
  con `text-justify:inter-word` y `text-wrap:pretty`, para que queden equilibrados,
  justificados y visualmente repartidos. En móvil (`max-width:640px`) volver a
  `text-align:left` para evitar ríos de espacio.
- Mantener este estilo de párrafo equilibrado/justificado en cualquier bloque de texto
  introductorio o explicativo que se añada en el futuro.

## Restricciones permanentes

- Nunca exponer el identificador de modelo en artefactos del repo, commits ni PRs.
- Nunca escribir secretos en ficheros del repo (es público).
- Trailers de commit:
  `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`
  `Claude-Session: https://claude.ai/code/session_019WmuM4uE7b9LjzLhY7VJCf`
- No crear PRs salvo petición explícita.
