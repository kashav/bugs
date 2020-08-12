window.onload = async function() {
  var target = document.querySelector("div");

  var observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      document.querySelector("pre").textContent += mutation.addedNodes[0].textContent + "\n";
    });
  });

  observer.observe(target, { attributes: true, childList: true, characterData: true });

  setInterval(m, 2000);
}

function m() {
  document.querySelector("div").innerText = Math.random();
}
