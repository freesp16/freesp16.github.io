// Exports every brand/*.svg to PNG at 1024 and 512 px (transparent background except the tiles).
import sharp from 'sharp';
import { readdirSync } from 'node:fs';
for (const f of readdirSync('.').filter((f) => f.endsWith('.svg'))) {
	for (const size of [1024, 512]) {
		await sharp(f, { density: (72 * size) / 256 }).resize(size, size).png({ compressionLevel: 9 }).toFile(`png/${f.replace('.svg', '')}-${size}.png`);
	}
}
console.log('done');
