/* Puts in a Node List */
const boxes = document.querySelectorAll(".box");

/*eventlistener for the window when scrolling activates
function checkBoxes*/
window.addEventListener("scroll", checkBoxes);

/* You want to fire it before it shows so the webpage \
is not blank*/
checkBoxes();

function checkBoxes() {
  const triggerBottom = (window.innerHeight / 5) * 4;

  /* box is a node list that we can iterate through*/
  boxes.forEach((box) => {
    /* .getBoundingClientRect returns a DOMreact object*/
    const boxTop = box.getBoundingClientRect().top;

    if (boxTop < triggerBottom) {
      box.classList.add("show");
    } else {
      box.classList.remove("show");
    }
  });
}
