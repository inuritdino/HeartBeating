// document.getElementById('human-heart1').style.border = "1px";


function run(){
    var id = setInterval(frame, 5);
    var elem = document.getElementById("animate");
    function frame() {
	elem.style.transform = "scale(1.1)";
    }
}
