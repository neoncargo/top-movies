function sendData(form) {
  const XHR = new XMLHttpRequest();
  const FD = new FormData(form);

  XHR.addEventListener("load", (event) => {
    response = JSON.parse(event.target.responseText);
    localStorage.setItem("access_token", response.access_token);
  });

  XHR.open("POST", "http://localhost/api/v1/users/");
  XHR.send(FD);
}

const form = document.getElementById("form");
const submitButton = document.getElementById("register");

window.addEventListener("load", () => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();

    sendData(form);
  });

  submitButton.addEventListener("mousedown", (event) => {
    event.preventDefault();
  });
});
