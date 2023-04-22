function SetInitialAuthBoxDisplay() {
    const jwt = localStorage.getItem("access_token");

    const userLogged = (jwt && (jwt !== "undefined"));
    if (userLogged) {
        const decodedJwt = JSON.parse(atob(jwt.split(".")[1]));
        const username = decodedJwt.sub;
        document.getElementById("username").textContent = username;

        let userBox = document.getElementById("user-box");
        userBox.style.display = "grid";
    } else {
        let authBtns = document.getElementById("auth-btns-box");
        authBtns.style.display = "block";
    }
}

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
