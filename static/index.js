import { SetInitialAuthBoxDisplay } from "../auth-display.js"

SetInitialAuthBoxDisplay();

const userBox = document.getElementById("user-box");
userBox.addEventListener("click", () => {
    let dropDown = document.getElementById("dropdown");
    if (dropDown.style.display == "flex") {
        dropDown.style.display = "none";
    } else {
        dropDown.style.display = "flex";
    }
});

window.onclick = function(event) {
    const userBox = document.getElementById("user-box");
    const clickOnUserBox = userBox.contains(event.target);
    if (!clickOnUserBox) {
        let dropDown = document.getElementById("dropdown");
        dropDown.style.display = "none";
    }
  }

const logoutBtn = document.getElementById("logout");
logoutBtn.addEventListener("click", () => {
    localStorage.removeItem("access_token");
    window.location.href = "/";
});

// "favourite" feature
let favourite_checkboxes = document.getElementsByClassName("favourite");

for (const element of favourite_checkboxes) {
    element.addEventListener("change", () => {
        const XHR = new XMLHttpRequest();

        if (element.checked) {
            XHR.open("PUT", "http://localhost/api/v1/me/favourites/" + element.value);
        } else {
            XHR.open("DELETE", "http://localhost/api/v1/me/favourites/" + element.value);
        }

        XHR.send();
    });
}
