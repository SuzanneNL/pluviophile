// Source: https://youtu.be/hqGNfYrjFZc
// GLOBAL
var c,ctx,vRain;

// RAIN
class Rain{
    //coordinate + length + speed
    constructor(x,y,l,v){
        this.x=x;
        this.y=y;
        this.vy=v;
        this.l=l;
    }
    show(){ //draw
        ctx.beginPath();
        ctx.strokeStyle="white";
        ctx.moveTo(this.x,this.y); //starts drops
        ctx.lineTo(this.x,this.y+this.l); //ends drops
        ctx.stroke();
    }
    //insert gravity
    fall(){
        this.y+=this.vy;

        // if the drops touch the ground
        // it gets recreated
        if(this.y>c.height){
            this.x=Math.floor(Math.random()*c.width)+5;
            this.y=Math.floor(Math.random()*100)-100; //from 0 to 99 -100, they all have different heights;
            this.l=Math.floor(Math.random()*30)+1; //from 1 to 30
            this.vy=Math.floor(Math.random()*12)+4;
        }
    }
}

// LOOP
function loop(){
    ctx.clearRect(0,0,c.width,c.height);

    for(var i=0;i<vRain.length;i++){
        vRain[i].show();
        vRain[i].fall();
    }
}

// SETUP
function setup(){
    c = document.getElementById("canvas")
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    ctx = c.getContext("2d");

    vRain = []; // List of all the drops
    for(var i=0;i<60;i++){
        vRain[i] = new Rain(
            Math.floor(Math.random()*c.width)+5,
            Math.floor(Math.random()*100)-100,
            Math.floor(Math.random()*30)+1,
            Math.floor(Math.random()*12)+4)
    }


    setInterval(loop,10);
}
