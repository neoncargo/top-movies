import { SetInitialAuthBoxDisplay } from "../auth-display.js"

function sendData() {
  const XHR = new XMLHttpRequest();

  XHR.addEventListener("load", (event) => {
    const response = JSON.parse(event.target.responseText);
    if (response.access_token) {
        localStorage.setItem("access_token", response.access_token);
        window.location.href = "/";
    }
  });

  const to_send = JSON.stringify({username: username.value, password: password.value});

  XHR.open("POST", "/api/v1/users");
  XHR.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  XHR.send(to_send);
}

SetInitialAuthBoxDisplay();

const form = document.getElementById("form");

const username = document.getElementById("input_username");

const password = document.getElementById("input_password");
const password_repeat = document.getElementById("input_password_repeat");


const submitButton = document.getElementById("register");

window.addEventListener("load", () => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();

    if (password.value !== password_repeat.value) {
        alert("Passwords don't match");
        return;
    }

    sendData();
  });

//   submitButton.addEventListener("mousedown", (event) => {
//     event.preventDefault();
//   });
});
