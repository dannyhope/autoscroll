(function () {
  let timer = null;
  window.addEventListener("message", function (event) {
    if (event.source !== window || !event.data || event.data.type !== "autoscroll.toggle") return;
    if (timer !== null) {
      clearInterval(timer);
      timer = null;
      return;
    }
    timer = setInterval(function () {
      window.scrollTo(0, window.pageYOffset + 1000);
    }, 100);
  });
  window.addEventListener("wheel", function (event) {
    if (event.deltaY < 0 && timer !== null) {
      clearInterval(timer);
      timer = null;
    }
  }, { passive: true });
})();
