import SafariServices

final class SafariExtensionHandler: SFSafariExtensionHandler {
    override func messageReceived(withName messageName: String, from page: SFSafariPage, userInfo: [String: Any]?) {
        guard messageName == "autoscroll.toggle" else { return }
        page.dispatchMessageToScript(withName: "autoscroll.toggle", userInfo: nil)
    }

    override func validateToolbarItem(in window: SFSafariWindow, validationHandler: @escaping (Bool, String?) -> Void) {
        validationHandler(true, nil)
    }
}
