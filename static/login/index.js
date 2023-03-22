function sendData() {
  const XHR = new XMLHttpRequest();

  XHR.addEventListener("load", (event) => {
    response = JSON.parse(event.target.responseText);
    if (response.access_token) {
        localStorage.setItem("access_token", response.access_token);
    }
  });

  to_send = JSON.stringify({username: username.value, password: password.value});

  XHR.open("POST", "http://localhost/api/v1/users/login");
  XHR.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  XHR.send(to_send);
}

function check() {
  let XHR = new XMLHttpRequest();
  XHR.open("GET", "http://localhost/api/v1/login/secure");
  XHR.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('access_token'));
  XHR.send();
}

const form = document.getElementById("form");

const username = document.getElementById("username");
const password = document.getElementById("password");

const submitButton = document.getElementById("login");

window.addEventListener("load", () => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();

    sendData();
  });
});
