# Brand assets

Four logo proposals, each as an SVG source and PNG exports at 1024 and 512 px:

| Design | Idea |
| --- | --- |
| `1-pads` | The 4 × 4 pad grid with a diagonal of four lit pads in four colours (**the logo in use**) |
| `2-wave` | A sine wave over the pad grid: sound plus pads |
| `3-steps` | 16 sequencer steps as a groove, the played steps lit |
| `4-hit` | One pad being struck, with rings of light |

Variants: `-dark` for dark backgrounds, `-light` for light backgrounds, `-tile` as an app icon on a dark rounded tile.
`logo-proposals.png` shows them side by side. Colours are the app's design tokens (accent `#569DFF`, play `#4ADD8C`,
mod `#FE6270`).

- Re-export the PNGs after editing an SVG: `cd brand && node export.mjs` (uses `sharp` from the site's dependencies).
- `hardware.py` draws `hardware-illustration.png` / `src/assets/hardware.png` (an original illustration with the app's
  real home screen; no vendor artwork). Run it from the repo root.
