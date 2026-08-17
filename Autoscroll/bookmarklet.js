(function (win) {
	var STEP_PX = 1000;
	var INTERVAL_MS = 100;

	function stop() {
		if (win.__ST) {
			clearInterval(win.__ST);
			win.__ST = null;
		}
		win.removeEventListener("wheel", onWheel, true);
	}

	function onWheel(event) {
		if (event.deltaY < 0) stop();
	}

	if (!win.__ST) {
		win.__ST = setInterval(function () {
			win.scrollTo(0, win.pageYOffset + STEP_PX);
		}, INTERVAL_MS);
		win.addEventListener("wheel", onWheel, true);
	} else {
		stop();
	}
})(this);
