export function SetInitialAuthBoxDisplay(show_only = "all") {
    let jwt = localStorage.getItem("access_token");

    let decodedJwt = {};
    if (jwt) {
        decodedJwt = JSON.parse(atob(jwt.split(".")[1]));
        if (decodedJwt.exp * 1000 <= Date.now()) {
            localStorage.removeItem("access_token");
            jwt = null;
        }
    }

    if (jwt) {
        const username = decodedJwt.sub;
        document.getElementById("username").textContent = username;
        let userBox = document.getElementById("user-box");
        userBox.style.display = "grid";
    } else {
        let authBtns = document.getElementById("auth-btns-box");
        authBtns.style.display = "block";
    }
}
