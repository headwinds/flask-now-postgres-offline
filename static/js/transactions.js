const postTransaction = (e) => {
    e.preventDefault();
  console.log("TCL: postTransaction")
    
  const jsonData = {title: "buy item",
                    type: "transaction",
                    cost: 10,
                    transaction_json: {title: "sword", cost: 10}}

    $.ajax({
        type: "POST",
        contentType: "application/json; charset=utf-8",
        url: "/api/transactions",
        data: JSON.stringify(jsonData),
        success: function (data) {
          if (data.status === 200 && data.message === "success") {
            location.reload();
          }
        },
        dataType: "json"
      });
}

const sayHello = (e) => {
    e.preventDefault();
    console.log("TCL: sayHello")
}


/*

var csrf_token = "{{ csrf_token() }}";

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });


*/