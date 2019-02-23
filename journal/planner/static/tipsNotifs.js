function setTime() {

var currentTime = new Date();

var h = currentTime.getHours();
var m = currentTime.getMinutes();
var s = currentTime.getSeconds();

	document.getElementById("time").innerText = h + ":" + m + ":" + s;
	document.getElementById("time").textContent = h + ":" + m + ":" + s;
	setTimeout(setTime, 1000);
}


setTime();