# freesp16 website

The project site of [freesp16](https://github.com/freesp16/freesp16), published at <https://freesp16.github.io>.
Built with [Astro](https://astro.build) and [Starlight](https://starlight.astro.build).

```sh
npm install
npm run dev       # http://localhost:4321
npm run build     # static site in dist/
```

## Where things are

| Path | What |
| --- | --- |
| `src/content/docs/` | The pages (Markdown/MDX): home, features, download, install, FAQ, changelog, contribute, support |
| `src/project.ts` | Project name, repo, release asset names: change them here only |
| `src/lib/releases.ts` | Reads the app's GitHub releases at build time (download buttons, changelog) |
| `src/components/` | Download cards, screenshots, gallery, changelog, footer notice |
| `src/assets/screens/` | App screenshots (1600 × 960, rendered by the app itself) |
| `src/styles/theme.css` | Colours (the app's design tokens) and small layout tweaks |

Without network or without a published release the site still builds; download buttons then link to the releases page.

## Releases

The download buttons pick from the latest release: `freesp16` (the armel executable) for the hardware, and the asset
whose name matches `linux…x86_64` / `amd64` (or an `.AppImage`) for the Linux desktop. The boot menu's `autoexec.bin`
comes from the latest release of [freesp16/bootmenu](https://github.com/freesp16/bootmenu). The site rebuilds on every push, once a day, and
when the app's release workflow sends a `release-published` event:

```sh
gh api repos/freesp16/freesp16.github.io/dispatches -f event_type=release-published
```

(In a workflow, that needs a token with access to this repository, for example a fine-grained PAT stored as a secret.)

## Screenshots

Rendered headlessly from the app's Linux build with a scripted input (`<PREFIX>_INPUT_SCRIPT`, `screenshot` steps)
at `scale=2`; see the app's `scripts/host-smoke.sh` for the setup.
