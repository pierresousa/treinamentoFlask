function mudarDisplay(elemento1){
    var display1 = document.getElementById(elemento1).style.display;
    if(display1 == "none"){
        document.getElementById(elemento1).style.display = 'block';
    }else{
        document.getElementById(elemento1).style.display = 'none';
    }  
}
