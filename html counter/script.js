let num=0;
const timer=document.getElementById("display");
document.getElementById("display").innerHTML =num;
/*function inc(){
    let num=num+1;
    document.getElementById("display").innerHTML =num;
}*/
document.getElementById("inc").onclick = function(){
    num =num+1;
    timer.innerHTML =num;
}
document.getElementById("dec").onclick = () => {
    num=num-1;
    timer.innerHTML=num;
    if (num<0) {
        num=0;
        timer.innerHTML=num;
    }
}
document.getElementById("reset").onclick = () => {
    num=0;
    timer.innerHTML=num;
}

