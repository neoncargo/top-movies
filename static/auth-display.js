export function SetInitialAuthBoxDisplay(show_only = "all") {
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
        if (!authBtns) {
            console.error("No auth-btns-box element");
            return;
        }

        authBtns.style.display = "block";
    }
}
