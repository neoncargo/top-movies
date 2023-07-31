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

// load movies and add to html
let jwt = localStorage.getItem("access_token");
if (jwt) {
    const container = document.querySelector(".index-content");

    let response = await fetch(
        "/api/v1/me/favorites",
        {
            headers: {
                "Authorization": 'Bearer ' + jwt
            }
        }
    );
    response = await response.json();

    for (const movie of response) {
        container.innerHTML += `
            <div class="movie-card">
                <a href="/movies/${movie.id}"><span></span></a>
                <div class="inner-movie">
                <input class="favorite" type="checkbox" name="favorite" value="${movie.id}">
                <div class="img-section"><img src="${movie.image_url}" alt=""></div>
                <p>${movie.title}</p>
                </div>
            </div>
        `;
    }
}
