/***** nav menu */
const toggle = document.getElementById("toggle");
const menu = document.querySelector(".menu");

toggle.addEventListener("click", () => {
  menu.classList.toggle("active");
});

/***** End nav menu */

/****change bg */
const color = document.querySelector(".color");

const body = document.querySelector("body");

color.addEventListener("click", () => {
  body.classList.toggle("bg");
  color.classList.toggle("changecolor");
});

window.onscroll = () => {
  menu.classList.remove("active");
};

/**** Ens change bg */

/**** Details chang Image */

const imagedtails = document.querySelector(".imagedtails");
const allmoredetails = document.querySelector(".allmoredetails");
const imgchange = document.getElementById("imgchange");

function changeImg(eo) {
  imgchange.src = eo;
}

/**** End Details chang Image */


/***** Button to scroll top *********************/
const button = document.getElementById("btn");

window.onscroll = function () {
  if (this.scrollY >= 1000) {
    button.classList.add("activebtn");
  } else {
    button.classList.remove("activebtn");
  }
};

button.onclick = function () {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
};

/**** secound posion to make scroll top */
// const  button = document.getElementById("btn");

// window.onscroll = function () {
//   if (this.scrollY >= 1000) {
//     button.classList.add("activebtn")
//   } else {
//    button.classList.remove("activebtn")
//   }
// }

// button.onclick = function () {
//   window.scrollTo({
//     top:0,
//     behavior: "smooth",
//   });
// }
/********************* End button to scroll top */


/**** Start img load ********* */

const overwindow = document.querySelector(".overwindow");
const timeswindow = document.querySelector(".timeswindow");
function load_window(){
  overwindow.classList.add("activeover")
}

function showload() {
  setTimeout(() => {
    load_window ()
  }, 1000);
}

window.onload = showload;

timeswindow.onclick = function(){
  
  overwindow.classList.remove("activeover")
}

/******* End img load *******/

