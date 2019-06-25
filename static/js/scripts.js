function getOnlineStatus() {
    return navigator.onLine;
  }

function message(status, shake = false, id = "") {
  if (shake) {
    $("#" + id).effect(
      "shake",
      { direction: "right", times: 2, distance: 8 },
      250
    );
  }
  document.getElementById("feedback").innerHTML = status;
  $("#feedback")
    .show()
    .delay(2000)
    .fadeOut();
}

function error(type) {
  $("." + type).css("border-color", "#E14448");
}

const loginWithJson = (e) => {

    const username = $("#login-user").val();
  const password = $("#login-pass").val();

  const jsonData = {username, password};

    $.ajax({
        type: "POST",
        contentType: "application/json; charset=utf-8",
        url: "/api/login",
        data: JSON.stringify(jsonData),
        success: function (data) {
          console.log(data);
        },
        dataType: "json"
      });
}

const loginWithJsonA = function(e) {
    e.preventDefault();

  const url = "/api/login";

  console.log("login to ", url);
  const username = $("#login-user").val();
  const password = $("#login-pass").val();

  const jsonData = {username, password};

  $.post({
    type: "POST",
    url,
    data: JSON.stringify(jsonData),
    //processData: false,
    dataType: 'json',
    contentType:"application/json; charset=utf-8",
    success(response) {
      const json = JSON.parse(response);
      const status = json["status"];
      if (status === "success" && json.source !== "api") {
        location.reload();
      } else if (status === "success" && json.source === "api") {
        console.log("api login success!");
        location.reload();
      } else {
        error("login-input");
      }
    }
  });
};

const login = function(e) {
    e.preventDefault();

  const url = "/api/login";

  console.log("login to ", url);

  const formData = new FormData();

  const username = $("#login-user").val();
  const password = $("#login-pass").val();

  formData.append("username", username);
  formData.append("password", password);

  $.post({
    type: "POST",
    url,
    data: formData,
    processData: false,
    contentType: false,
    success(response) {
      const json = JSON.parse(response);
      const status = json["status"];
      if (status === "success" && json.source !== "api") {
        location.reload();
      } else if (status === "success" && json.source === "api") {
        console.log("api login success!");
        location.reload();
      } else {
        error("login-input");
      }
    }
  });
};

const signup = (e) => {
  e.preventDefault();
  
  const formData = new FormData();

  const username = $("#signup-user").val();
  const password = $("#signup-pass").val();
  const email = $("#signup-mail").val();

  formData.append("username", username);
  formData.append("password", password);
  formData.append("email", email);
  formData.append("offline", getOnlineStatus());
  formData.append("domain", document.domain);

  $.post({
    type: "POST",
    url: "/signup",
    data: formData,
    processData: false,
    contentType: false,
    success(response) {
        console.log("TCL: success -> response", response)
      const json = JSON.parse(response);
      const status = JSON.parse(response)["status"];
      console.log("TCL: success -> status", status)
      
      if (status === "success" && json.source !== "api") {
        location.reload();

        //$.get({url: "/home", type: "GET"})

      } else if (status === "success" && json.source === "api") {
        console.log("api login success!");
        location.reload();
        //$.get({url: "/home", type: "GET"})
      } else {
        error("login-input");
      }
      
    }
  });
};


$(document).ready(function() {
  $(document).on("click", "#login-button", login);
  
  $(document).on("click", "#login-button-json", loginWithJson);
  
  $(document).keypress(function(e) {
    if (e.which === 13) {
      login();
    }
  });

  $(document).on("click", "#signup-button", signup);

  $(document).on("click", "#save", function() {
    $.post({
      type: "POST",
      url: "/settings",
      data: {
        username: $("#settings-user").val(),
        password: $("#settings-pass").val(),
        email: $("#settings-mail").val()
      },
      success(response) {
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
      success(response) {
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
      success(response) {
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
      success(response) {
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
      success(response) {
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
      success(response) {
        message(JSON.parse(response)["status"]);
      }
    });
  });
});

// Open or Close mobile & tablet menu
// https://github.com/jgthms/bulma/issues/856
$("#navbar-burger-id").click(function() {
  if ($("#navbar-burger-id").hasClass("is-active")) {
    $("#navbar-burger-id").removeClass("is-active");
    $("#navbar-menu-id").removeClass("is-active");
  } else {
    $("#navbar-burger-id").addClass("is-active");
    $("#navbar-menu-id").addClass("is-active");
  }
});
