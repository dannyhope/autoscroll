browser.action.onClicked.addListener((tab) => {
	if (!tab.id) return;
	browser.scripting
		.executeScript({
			target: { tabId: tab.id },
			files: ["bookmarklet.js"],
		})
		.catch(() => {
			// Restricted pages cannot be scripted.
		});
});
