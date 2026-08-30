let timeLeft = 15;

const timer = document.getElementById("timer");

const quizForm = document.getElementById("quiz-form");


const countdown = setInterval(function () {

    timeLeft--;

    timer.innerHTML = "⏱️ " + timeLeft;


    if (timeLeft <= 0) {

        clearInterval(countdown);

        quizForm.submit();

    }

}, 1000);