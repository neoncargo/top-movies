function sendData(form) {
  const XHR = new XMLHttpRequest();
  const FD = new FormData(form);

  XHR.addEventListener("load", (event) => {
    response = JSON.parse(event.target.responseText);
    localStorage.setItem("access_token", response.access_token);
  });

  XHR.open("POST", "http://localhost/api/v1/login/token");
  XHR.send(FD);
}

function check() {
  let XHR = new XMLHttpRequest();
  XHR.open("GET", "http://localhost/api/v1/login/secure");
  XHR.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('access_token'));
  XHR.send();
}

const form = document.getElementById("form");
const checkButton = document.getElementById("check");

window.addEventListener("load", () => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();

    sendData(form);
  });

  checkButton.addEventListener("click", (event) => {
    check();
  });
});
