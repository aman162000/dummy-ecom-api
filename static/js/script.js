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

async function getAPIlink() {
  var a = document.getElementById("API-ID");
  a.href = window.location.origin + "#email";
}
async function getABOUTlink() {
  var a = document.getElementById("About-ID");
  a.href = window.location.origin + "#footer";
}

async function copy_Addr() {
  var but = document.getElementsByClassName("btn-address");
  var txt = document.getElementsByClassName("c-address");

  for (let x = 0; x < but.length; x++) {
    but[x].addEventListener(
      "click",
      async function () {
        await navigator.clipboard.writeText(txt[x].innerText);
        but[x].classList.remove("btn-outline-warning");
        but[x].classList.add("btn-warning");
        but[x].innerText = "Copied!";
      },
      false
    );
  }
}
