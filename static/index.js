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

function hook_favorites() {
    // "favorite" feature
    let favorite_checkboxes = document.getElementsByClassName("favorite");

    for (const element of favorite_checkboxes) {
        element.addEventListener("change", () => {
            const XHR = new XMLHttpRequest();

            XHR.addEventListener("load", (event) => {
                if (XHR.status === 401) {
                    localStorage.removeItem("access_token");
                    console.log("got 401. Delete jwt");
                    SetInitialAuthBoxDisplay();
                }
            });

            const jwt = localStorage.getItem("access_token");
            const userLogged = (jwt && (jwt !== "undefined"));

            if (!userLogged) {
                console.log("You need to be logged");
                return;
            }

            if (element.checked) {
                XHR.open("PUT", "/api/v1/me/favorites/" + element.value);
            } else {
                XHR.open("DELETE", "/api/v1/me/favorites/" + element.value);
            }

            XHR.setRequestHeader('Authorization', 'Bearer ' + jwt);

            XHR.send();
        });
    }
}

hook_favorites();

const form = document.getElementById("form");
const searchElem = document.querySelector("#search");
const container = document.querySelector(".index-content");
let oldContent = container.innerHTML;
window.addEventListener("load", () => {
    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        let response = await fetch(
            "/api/v1/search/movies?query=" + searchElem.value,
        );
        response = await response.json();

        container.innerHTML = "";
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
        hook_favorites();
  });
});

// // on empty search
searchElem.addEventListener("input", () => {
    if (searchElem.value == "") {
        container.innerHTML = oldContent;
        hook_favorites();
    }
});
