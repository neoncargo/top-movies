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
