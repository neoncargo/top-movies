function sendData() {
  const XHR = new XMLHttpRequest();

  XHR.addEventListener("load", (event) => {
    response = JSON.parse(event.target.responseText);
    localStorage.setItem("access_token", response.access_token);
  });

  to_send = JSON.stringify({username: username.value, password: password.value});

  XHR.open("POST", "http://localhost/api/v1/users");
  XHR.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  XHR.send(to_send);
}

const form = document.getElementById("form");

const username = document.getElementById("username");

const password = document.getElementById("password");
const password_repeat = document.getElementById("password_repeat");


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

  submitButton.addEventListener("mousedown", (event) => {
    event.preventDefault();
  });
});
