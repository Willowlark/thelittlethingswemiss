---
title: Countdown to Colossalcon East
categories: article
tags: main-blog
excerpt: We all know I mean swim and drink con.
---

<p id="demo" style="margin-left: 40px; text-align: center; font-size: 300%; font-weight:bold;"></p>

<script>
// Set the date we're counting down to
var countDownDate = new Date("Sep 12, 2019 12:00:00").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

// Get todays date and time
var now = new Date().getTime();

// Find the distance between now an the count down date
var distance = countDownDate - now;

// Time calculations for days, hours, minutes and seconds
var days = Math.floor(distance / (1000 * 60 * 60 * 24));
var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
var seconds = Math.floor((distance % (1000 * 60)) / 1000);

// Display the result in the element with id="demo"
document.getElementById("demo").innerHTML =  days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";

// If the count down is finished, write some text 
if (distance < 0) {
clearInterval(x);
document.getElementById("demo").innerHTML = "EXPIRED";
}
}, 1000);
</script>