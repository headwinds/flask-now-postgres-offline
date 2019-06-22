function message(status, shake=false, id="") {
  if (shake) {
    $("#"+id).effect("shake", {direction: "right", times: 2, distance: 8}, 250);
  } 
  document.getElementById("feedback").innerHTML = status;
  $("#feedback").show().delay(2000).fadeOut();
}

function error(type) {
  $("."+type).css("border-color", "#E14448");
}

const login = function() {
  $.post({
    type: "POST",
    url: "/login",
    data: {"username": $("#login-user").val(), 
           "password": $("#login-pass").val()},
    success(response){
      const status = JSON.parse(response)["status"];
      if (status === "success") { location.reload(); }
      else { error("login-input"); }
    }
  });
};

function getOnlineStatus(){
    return navigator.onLine;
}


$(document).ready(function() {
  
  $(document).on("click", "#login-button", login);
  $(document).keypress(function(e) {if(e.which === 13) {login();}});
  
  $(document).on("click", "#signup-button", function() {
    $.post({
      type: "POST",
      url: "/signup",
      data: {"username": $("#signup-user").val(), 
             "password": $("#signup-pass").val(), 
             "email": $("#signup-mail").val()},
      success(response) {
        var status = JSON.parse(response)["status"];
        if (status === "Signup successful") { location.reload(); }
        else { message(status, true, "signup-box"); }
      }
    });
  });

  $(document).on("click", "#save", function() {
    $.post({
      type: "POST",
      url: "/settings",
      data: {"username": $("#settings-user").val(), 
             "password": $("#settings-pass").val(), 
             "email": $("#settings-mail").val()},
      success(response){
        message(JSON.parse(response)["status"]);
      }
    });
  });

  // TEST THE TRANSACTIONS API

  // GET

  $(document).on("click", "#test-get-transactions", function() {
    $.post({
      type: "GET",
      url: "/transactions/1",
      success(response){
        message(JSON.parse(response)["status"]);
      }
    });
  });

  // POST

  $(document).on("click", "#test-post-transactions", function(transaction) {
    $.post({
      type: "POST",
      url: "/transactions",
      data: transaction,
      success(response){
        message(JSON.parse(response)["status"]);
      }
    });
  });

  // PUT

  $(document).on("click", "#test-post-transactions", function(transaction) {
    $.post({
      type: "PUT",
      url: "/transactions/:id",
      data: transaction,
      success(response){
        message(JSON.parse(response)["status"]);
      }
    });
  });

  // PATCH

  $(document).on("click", "#test-patch-transactions", function(transaction) {
    $.post({
      type: "PATCH",
      url: "/transactions/:id",
      data: transaction,
      success(response){
        message(JSON.parse(response)["status"]);
      }
    });
  });

  // DELETE

  $(document).on("click", "#test-delete-transactions", function(transaction) {
    $.post({
      type: "GET",
      url: "/transactions/:id",
      data: transaction,
      success(response){
        message(JSON.parse(response)["status"]);
      }
    });
  });


});

// Open or Close mobile & tablet menu
// https://github.com/jgthms/bulma/issues/856
$("#navbar-burger-id").click(function () {
  if($("#navbar-burger-id").hasClass("is-active")){
    $("#navbar-burger-id").removeClass("is-active");
    $("#navbar-menu-id").removeClass("is-active");
  }else {
    $("#navbar-burger-id").addClass("is-active");
    $("#navbar-menu-id").addClass("is-active");
  }
});