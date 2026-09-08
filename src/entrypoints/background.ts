export default defineBackground(() => {
  browser.action.onClicked.addListener(async (tab) => {
    if (!tab.id) return;

    try {
      await browser.scripting.executeScript({
        target: { tabId: tab.id },
        files: ['scripts/scroller.js'],
      });
    } catch (error) {
      // Restricted pages (chrome://, about:, Web Store, and similar) cannot be scripted.
      // Fail silently as per spec.
    }
  });
});
