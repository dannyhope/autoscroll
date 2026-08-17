chrome.action.onClicked.addListener((tab) => {
	if (!tab.id) return;
	chrome.scripting
		.executeScript({
			target: { tabId: tab.id },
			files: ["bookmarklet.js"],
		})
		.catch(() => {
			// Restricted pages (chrome://, Web Store, and similar) cannot be scripted.
		});
});
