# Portadas de blog · Agentes de IA

Tres propuestas de imagen de previsualización (1200×630 lógicos, exportadas a 2400×1260 @2x)
con la paleta de marca: `#021f12` (verde oscuro), `#2ECF8F` (menta) y blanco.

| Fichero | Concepto |
|---|---|
| `portada-agentes-ia-red.png` | Fondo oscuro + red de agente (objetivo, contexto, memoria, herramientas, acción) |
| `portada-agentes-ia-flujo.png` | Fondo oscuro + flujo en 3 pasos (Entiende → Decide → Actúa) |
| `portada-agentes-ia-mint.png` | Fondo menta + ciclo del agente (Lee → Piensa → Actúa → Aprende) |

## Regenerar

Las fuentes están en `src/` (HTML + CSS + tipografía Manrope subset latin embebida).
Con Chromium disponible:

```bash
cd blog-covers/src
./render.sh red.html   ../portada-agentes-ia-red.png
./render.sh flujo.html ../portada-agentes-ia-flujo.png
./render.sh mint.html  ../portada-agentes-ia-mint.png
```

`render.sh` renderiza a 2x, recorta el lienzo exacto (fondo centinela magenta en `body`)
y guarda el PNG final. Editar textos/colores directamente en los HTML.
