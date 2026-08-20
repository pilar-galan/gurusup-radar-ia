# Portadas de blog · Agentes de IA (sin texto)

Piezas visuales abstractas para acompañar el artículo, sin ningún texto: el titular va
en el propio blog. 1200×630 lógicos, exportadas a 2400×1260 (@2x). Paleta: `#021f12`,
`#2ECF8F` y blanco solo como brillo puntual.

| Fichero | Concepto | Uso |
|---|---|---|
| `agentes-ia-constelacion.png` | Núcleo con satélites sobre malla de nodos | Opción principal |
| `agentes-ia-flujo.png` | Flujos que entran y salen del núcleo | Más gráfica y simétrica |
| `agentes-ia-malla.png` | Malla de puntos con densidad radial | La más discreta |
| `agentes-ia-menta.png` | Fondo menta con red en verde oscuro | Para contraste en feed |

## Regenerar

`src/gen.py` construye el SVG de cada pieza (geometría paramétrica: densidad de malla,
radios, opacidades, reparto angular por ángulo dorado). `src/render.sh` lo rasteriza con
Chromium a 2x y recorta el lienzo exacto usando un fondo centinela magenta en `body`.

```bash
cd blog-covers/src
python3 gen.py                      # escribe v1..v4.html
./render.sh v1.html ../agentes-ia-constelacion.png
./render.sh v2.html ../agentes-ia-flujo.png
./render.sh v3.html ../agentes-ia-malla.png
./render.sh v4.html ../agentes-ia-menta.png
```

Requiere Chromium (ruta al binario en `render.sh`) y Pillow para el recorte.
Si hace falta otro formato (cuadrado 1:1, vertical, banner), cambiar `W`/`H` en `gen.py`.
