import { defineConfig } from 'wxt';

export default defineConfig({
  srcDir: 'src',
  outDir: '.output',
  manifest: ({ browser }) => ({
    name: 'Autoscroll',
    description: 'Scroll to the bottom of the page. Click the toolbar icon; scroll up to stop.',
    version: '0.4.0',
    author: 'Danny Hope',
    homepage_url: 'https://dannyhope.co.uk/autoscroll/',
    permissions: ['activeTab', 'scripting'],
    ...(browser === 'firefox' && {
      browser_specific_settings: {
        gecko: {
          id: 'autoscroll@dannyhope.co.uk',
          strict_min_version: '128.0',
        },
      },
    }),
  }),
  runner: {
    disabled: true,
  },
  manifestVersion: 3,
});
