let currentText = '';
let count = 0;
let index = 0;
let letter = '';
let direction = true;

var roles = [
  "Computer science & security student.",
  "Always learning, always improving.",
  "Based in Oregon, remotely available anywhere.",
  "Based in Oregon, remotely available anywhere.",
];

function type() {

  setTimeout(type, 60);
	if(count === 0) {
  	direction = true;
  }
	if(letter.length >= roles[index].length) {
    direction = false;
  }
  if(index == roles.length-1) {
    index = 0;
  }
  currentText = roles[index];

  if(direction) {
  	letter = currentText.slice(0,count++);
    document.querySelector('#typing').textContent = letter;
  } else {
  	letter = currentText.slice(0, count--)
    document.querySelector('#typing').textContent = letter;
  }

  if(count === 0) {
    index++;
  }
}