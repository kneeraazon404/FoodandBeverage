var date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

setTimeout(function () {
  $("#message").fadeOut("slow");
}, 300);
