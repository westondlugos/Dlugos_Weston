function emailValidation(){
    var x = document.forms.input.email.value;
    var atPos =  x.indexOf("@");
    var dotPos = x.lastIndexOf(".");
    if( atPos < 1 ||  dotPos < atPos + 2 || dotPos + 2 > x.length)
        alert("Email isn't valid");
    else
        alert("Email valid");
}
function passwordValidation(){
        var y = document.forms.input.password.value;

        if( y.length < 6)
            alert("password isn't more than 6 letters");
        else
            alert("password valid");
}