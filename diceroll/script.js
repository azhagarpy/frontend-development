const button =document.querySelector(".rollbtn");
const img= document.getElementById("img");
function alagar(){
    alert(1);
}
function roll() {
    let randomnum=Math.floor(Math.random()*6)+1;
    /*document.querySelector("#img1").setAttribute("src",
					"dice" + randomnum + ".png");
                    */
    if (randomnum == 1) {
        document.querySelector("#img1").setAttribute("src","dice1.png");
    }
    if (randomnum == 2) {
        document.querySelector("#img1").setAttribute("src","dice2.png");
    }
    if (randomnum == 3) {
        document.querySelector("#img1").setAttribute("src","dice3.png");
    }
    if (randomnum == 4) {
        document.querySelector("#img1").setAttribute("src","dice4.png");
    }
    if (randomnum == 5) {
        document.querySelector("#img1").setAttribute("src","dice5.png");
    }
    if (randomnum == 6) {
        document.querySelector("#img1").setAttribute("src","dice6.png");
    }
}
