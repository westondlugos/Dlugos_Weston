function drag() {
    puck = document.getElementById("puck");
    leftbox = document.getElementById("leftBox");

    puck.addEventListener("dragstart", startDrag, false);
    puck.addEventListener("dragend", endDrag,false);

    leftbox.addEventListener("dragenter", dragEnter,false);
    leftbox.addEventListener("dragover", dragOver,false);
    leftbox.addEventListener("drop", drop,false);

}

function dragEnter(e){
    e.preventDefault();
    leftbox.style.background = "purple";

}
function startDrag(e){
    var pic = '<img id = "puck" src = "http://lgcdn.hockeymonkey.com/80A850/hockey/media/catalog/product/cache/3/small_image/600x/9df78eab33525d08d6e5fb8d27136e95/o/f/oficehocpuc.jpg">';
    e.dataTransfer.setData('Picture', pic);


}



function dragOver(e){
    e.preventDefault();
    leftbox.style.background = "purple";
}

function drop(e){
    e.preventDefault();
    leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e) {
    e.target.style.visibility = "hidden";
}

window.addEventListener("load", drag,false);