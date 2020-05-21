// document.getElementById("changeGreen").onclick = function(){
// 	var output = document.getElementsByClassName("output")
// 	for(var i=0; i < output.length; i++){
// 		output[i].classList.toggle('togglecolor');
// 	}	
// }

// document.getElementById("add_post").onclick = function(){
// 	document.getElementById("add_new_post").classList.toggle('togglecolor')
// }

var tiles = document.querySelectorAll(".img-container");

for(var i = 0; i < tiles.length; i++){
	tiles[i].addEventListener("mouseover", function(){
			this.style.padding = '3px';
})};
for(var i = 0; i < tiles.length; i++){
	tiles[i].addEventListener("mouseout", function(){
			this.style.padding = '0px';	
})};

$(document).ready(function(){
    $(".dropdown-toggle").dropdown();

});  

