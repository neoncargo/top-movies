import { SetInitialAuthBoxDisplay } from "../auth-display.js"

function sendData(form) {
  const XHR = new XMLHttpRequest();
  const FD = new FormData(form);

  XHR.addEventListener("load", (event) => {
    const response = JSON.parse(event.target.responseText);
    if (response.access_token) {
        localStorage.setItem("access_token", response.access_token);
        window.location.href = "/";
    }
  });

  XHR.open("POST", "/api/v1/users/login");
  XHR.send(FD);
}

SetInitialAuthBoxDisplay();

const form = document.getElementById("form");

window.addEventListener("load", () => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();

    sendData(form);
  });
});
