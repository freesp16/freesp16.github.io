// Everything the site says about the project in one place: rename or move the project here only.
export const project = {
	name: 'freesp16',
	tagline: 'A free, open-source sampler and groovebox app for the Pioneer DJ TORAIZ SP-16.',
	org: 'freesp16',
	appRepo: 'freesp16/freesp16',
	// The boot menu (its own project): the stick's autoexec.bin, which lists and starts freesp16 and other apps.
	bootmenuRepo: 'freesp16/bootmenu',
	discord: 'https://discord.gg/DedpwtE6EK',
	siteUrl: 'https://freesp16.github.io',
	license: 'GPL-3.0-or-later (JUCE: AGPLv3)',
	// Release asset names: the hardware build is the plain armel executable `freesp16` (the boot menu lists it under
	// that file name); the boot menu release ships autoexec.bin; the Linux build is matched by pattern.
	hardwareAsset: /^freesp16$/i,
	bootmenuAsset: /^autoexec\.bin$/i,
	linuxAsset: /linux.*(x86_64|amd64)|amd64.*linux|\.AppImage$/i,
	checksumAsset: /\.sha256$|sha256sums/i,
} as const;

export const repoUrl = `https://github.com/${project.appRepo}`;
export const releasesUrl = `${repoUrl}/releases`;
export const latestReleaseUrl = `${releasesUrl}/latest`;
export const issuesUrl = `${repoUrl}/issues`;
export const newIssueUrl = `${repoUrl}/issues/new`;

export const bootmenuUrl = `https://github.com/${project.bootmenuRepo}`;
export const bootmenuLatestUrl = `${bootmenuUrl}/releases/latest`;
