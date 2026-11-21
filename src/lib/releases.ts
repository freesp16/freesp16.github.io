// GitHub releases of the app, read once per build. Without network, without releases or when the API refuses, the
// site still builds: every download link then falls back to the releases page.
import { project } from '../project';

export interface Asset {
	name: string;
	url: string;
	size: number;
}

export interface Release {
	tag: string;
	name: string;
	url: string;
	date: string;
	prerelease: boolean;
	body: string;
	assets: Asset[];
}

let cached: Promise<Release[]> | undefined;

export function getReleases(): Promise<Release[]> {
	cached ??= load();
	return cached;
}

async function load(): Promise<Release[]> {
	const headers: Record<string, string> = { Accept: 'application/vnd.github+json' };
	if (process.env.GITHUB_TOKEN) headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
	try {
		const res = await fetch(`https://api.github.com/repos/${project.appRepo}/releases?per_page=30`, { headers });
		if (!res.ok) {
			console.warn(`[releases] GitHub API answered ${res.status}; download links fall back to the releases page`);
			return [];
		}
		const list = (await res.json()) as any[];
		return list
			.filter((r) => !r.draft)
			.map((r) => ({
				tag: r.tag_name,
				name: r.name || r.tag_name,
				url: r.html_url,
				date: r.published_at,
				prerelease: r.prerelease,
				body: r.body ?? '',
				assets: (r.assets ?? []).map((a: any) => ({ name: a.name, url: a.browser_download_url, size: a.size })),
			}));
	} catch (e) {
		console.warn(`[releases] could not reach GitHub (${(e as Error).message}); download links fall back to the releases page`);
		return [];
	}
}

/** The newest stable release, or the newest pre-release when there is no stable one yet. */
export async function getLatest(): Promise<Release | undefined> {
	const all = await getReleases();
	return all.find((r) => !r.prerelease) ?? all[0];
}

export function findAsset(release: Release | undefined, pattern: RegExp): Asset | undefined {
	return release?.assets.find((a) => pattern.test(a.name));
}

export function formatSize(bytes: number): string {
	if (bytes >= 1 << 20) return `${(bytes / (1 << 20)).toFixed(1)} MB`;
	return `${Math.max(1, Math.round(bytes / 1024))} KB`;
}

export function formatDate(iso: string): string {
	return new Date(iso).toLocaleDateString('en-GB', { year: 'numeric', month: 'long', day: 'numeric' });
}
