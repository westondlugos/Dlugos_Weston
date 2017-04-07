function shapes(){
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    canvas.strokeStyle = "red";
    var g = canvas.createLinearGradient(0,0,1000,1000);
    g.addColorStop(.3, "blue");
    g.addColorStop(.5, "green");
    g.addColorStop(.6, "red");




    canvas.beginPath();
    canvas.moveTo(500,100);
    canvas.lineTo(450,300);
    canvas.lineTo(200,175);
    canvas.lineTo(400,380);
    canvas.lineTo(150,425);
    canvas.lineTo(400,470);
    canvas.lineTo(200,650);
    canvas.lineTo(450,550);
    canvas.lineTo(500,800);
    canvas.lineTo(550,550);
    canvas.lineTo(750,650);
    canvas.lineTo(590,470);
    canvas.lineTo(800,425);
    canvas.lineTo(590,380);
    canvas.lineTo(750,175);
    canvas.lineTo(550,300);
    canvas.closePath();
    canvas.fillStyle = g;
    canvas.fill();


    canvas.stroke();






}

window.addEventListener("load",shapes,false);