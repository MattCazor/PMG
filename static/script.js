const select = document.getElementById("mode");
const fract = document.querySelectorAll(".fract");
const simple = document.querySelectorAll(".simple");
const rep = document.querySelectorAll(".rep")
const Angle = document.querySelectorAll(".angl")
const spirale = document.querySelectorAll(".spir")
const niveau = document.querySelectorAll(".niveau")

select.addEventListener("change", changement)
function changement() {
    if (select.value == "forme") {
        for (const elem of fract) {
            elem.style.display = "none";
        }
        for (const elem of simple) {
            elem.style.display = "block";
        }
        for (const elem of rep) {
            elem.style.display = "block";
        }
        for (const elem of niveau) {
            elem.style.display = "none";
        }
        for (const elem of spirale) {
            elem.style.display = "none";
        }
        for (const elem of Angle) {
            elem.style.display = "block";
        }
    }
    else if (select.value == "fractale") {
        for (const elem of simple) {
            elem.style.display = "none";
        }
        for (const elem of fract) {
            elem.style.display = "block";
        }
        for (const elem of rep) {
            elem.style.display = "none";
        }
        for (const elem of niveau) {
            elem.style.display = "block";
        }
        for (const elem of spirale) {
            elem.style.display = "none";
        }
        for (const elem of Angle) {
            elem.style.display = "none";
        }
    }
    else if (select.value == "spirale") {
        for (const elem of simple) {
            elem.style.display = "none";
        }
        for (const elem of fract) {
            elem.style.display = "none";
        }
        for (const elem of rep) {
            elem.style.display = "none";
        }
        for (const elem of niveau) {
            elem.style.display = "none";
        }
        for (const elem of spirale) {
            elem.style.display = "block";
        }
        for (const elem of Angle) {
            elem.style.display = "block";
        }
    }
}
changement();