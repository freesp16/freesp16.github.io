// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// Served from the GitHub organization's Pages repo (freesp16/freesp16.github.io), so there is no base path.
export default defineConfig({
	site: 'https://freesp16.github.io',
	integrations: [
		starlight({
			title: 'freesp16',
			description: 'A free, open-source sampler and groovebox app for the Pioneer DJ TORAIZ SP-16, with a smooth 60 fps screen, and for the Linux desktop.',
			logo: {
				light: './src/assets/logo-light.svg',
				dark: './src/assets/logo-dark.svg',
			},
			favicon: '/favicon.svg',
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/freesp16/freesp16' },
				{ icon: 'discord', label: 'Discord', href: 'https://discord.gg/DedpwtE6EK' },
			],
			editLink: { baseUrl: 'https://github.com/freesp16/freesp16.github.io/edit/main/' },
			customCss: ['./src/styles/theme.css'],
			components: { Footer: './src/components/Footer.astro' },
			lastUpdated: true,
			sidebar: [
				{ label: 'Features', slug: 'features' },
				{ label: 'Download', slug: 'download' },
				{
					label: 'Install',
					items: [
						{ label: 'On the TORAIZ SP-16', slug: 'install/hardware' },
						{ label: 'On the Linux desktop', slug: 'install/linux' },
					],
				},
				{ label: 'FAQ', slug: 'faq' },
				{ label: 'Changelog', slug: 'changelog' },
				{ label: 'Build and contribute', slug: 'contribute' },
				{ label: 'Support', slug: 'support' },
			],
		}),
	],
});
