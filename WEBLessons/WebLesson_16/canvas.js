
function mouse()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    window.addEventListener("mousemove",icon,false);
    
}

function icon(e){
    canvas.clearRect(0,0,600,600);
    var pic  = new Image();
    pic.src = "https://openclipart.org/download/222076/Mouse-Cursor-Arow-Fixed.svg";
    var xPos = e.clientX;
    var yPos = e.clientY;
     canvas.drawImage(pic,xPos,yPos,200,200)
}

window.addEventListener("load",mouse,false);

