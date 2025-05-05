player_name = prompt("enter your social security number");

alert("hello " + player_name);
player_guess = prompt("guess a number between 1 & 3");
computer_guess = randomIntFormInterval(1, 3);
alert(computer_guess);
if (player_guess == computer_guess) {
  document.getElementbyId("user_feedback").innerHTML = " correct you win!";
} else {
  document.getElementById("user_feedback").innerHTML =
    "wrong, get off my website you bum it was /n" + computer_guess;
}
function randomIntFormInterval(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
