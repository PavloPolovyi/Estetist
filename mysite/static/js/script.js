let buttons = document.getElementsByClassName('navBtn')
let links = Array.from(buttons)

for (l of links) {
    l.addEventListener('click', function () {
        let current = document.querySelector('.active');
        current ? current.classList.remove('active') : {};
        this.classList.add('active');
    })
}

let prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    let currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("navbar").style.top = "0";
    } else {
        document.getElementById("navbar").style.top = "-110px";
    }
    prevScrollpos = currentScrollPos;
}