const toggleButton = document.getElementsByClassName("toggle-button")[0];
const navbarLinks = document.getElementsByClassName("navbar-links")[0];

toggleButton.addEventListener("click", () => {
  navbarLinks.classList.toggle("active");
});

async function copyBase_URL() {
  var copyText = document.getElementById("base-url");
  var btn = document.getElementById("copy-btn");
  console.log(copyText.innerText);
  await navigator.clipboard.writeText(copyText.innerText);
  btn.classList.remove("btn-outline-warning");
  btn.classList.add("btn-warning");
  btn.innerText = "Copied!";
}
