// Get the modal
var modal = document.getElementById('myModal');
var modal2 = document.getElementById('myModal2');
var addDay = document.getElementById("addDay");
// Get the button that opens the modal
var plancard = document.getElementById("plan-card");
var btn = document.getElementById("btn");
var btnDay = document.getElementById("btn-home-add-day")

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
var span2 = document.getElementsByClassName("close2")[0];
var span3 = document.getElementsByClassName("close3")[0];

// When the user clicks the button, open the modal 
plancard.onclick = function() {
  modal.style.display = "block";
}

btn.onclick = function() {
  modal.style.display = "none";
  modal2.style.display = "block";
}

btnDay.onclick = function() {
	addDay.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

span2.onclick = function() {
  modal2.style.display = "none";
}

span3.onclick = function() {
	addDay.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  else if (event.target == modal2) {
  	modal2.style.display = "none";
  }
  else if (event.target == addDay) {
  	addDay.style.display = "none";
  }
}