$(function () {
  "use strict";
  $(function () {
    $(".preloader").fadeOut();
  });

  function setTime() {
    var d = new Date(),
      el = document.getElementById("time");

    el.innerHTML = formatAMPM(d);

    setTimeout(setTime, 1000);
  }

  function formatAMPM(date) {
    var hours = date.getHours(),
      minutes = date.getMinutes(),
      seconds = date.getSeconds(),
      ampm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0' + minutes : minutes;
    var strTime = hours + ':' + minutes + ':' + seconds + ' ' + ampm;
    return strTime;
  }

  function formatDate() {
    const today = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const currentDate = today.toLocaleDateString(undefined, options);

    return currentDate;
  }

  function setDate() {
    var date_div = document.getElementById("nav_date");
    date_div.innerHTML = '<i class="fa fa-calendar"></i>&ensp;' + formatDate().toString();
  }

  setDate();
  setTime();
});


// CRUD generic functions //////////////////////////////////////////////////////////////////////////////////
// Create request
function createRequest(params) {
  var form = document.getElementById(params['formId']);
  const data = new FormData(form)
  fetch(`${window.origin}` + params['serverUrl'], {
    method: "POST",
    credentials: "include",
    body: data,
    cache: "no-cache",
  }).then(function (response) {
    // Close the modal
    $('.close').click();
    form.reset();
    // First sort successful resource creations
    if (response.status == 201) {
      $('#flash_message').append(flashMessage('success', params['object'] + ' added successfully'));
      setTimeout(function() {location.reload(true);}, 2000);
      return;
    }
    // Else handle errors
    else {
      response.text().then(function (data) {
        // If the record already exists
        if (data == 'Resource Exists') {
          $('#flash_message').append(flashMessage('warning', params['object'] + ' already exists'));
        }
        // If an unsupported media type has been uploaded (e.g. an image)
        else if (response.status == 415) {
          $('#flash_message').append(flashMessage('danger', data));
        }
        // If there was an empty field
        else if (response.status == 422) {
          empty_list = JSON.parse(data)
          for (var i = 0; i < empty_list.length; i++) {
            $('#flash_message').append(flashMessage('danger', empty_list[i] + ' value missing'));
          }
        }
        // Any other uncaught error
        else {
          console.log(data)
          $('#flash_message').append(flashMessage('danger', 'Something unexpected happened. Please try again.'));
        }
      })
    }
  });
}
// Update request
function updateRequest(serverUrl, values, reload = false) {
  // The value keys must match the column attributes of the database table being updated
  fetch(`${window.origin}` + serverUrl, {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(values),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  }).then(function (response) {
    // First sort situation where response not 200
    if (response.status !== 200) {
      $('#flash_message').append(flashMessage('warning', 'We were unable to process your request. Please try again later.'));
      console.log(response.status);
      return;
    }
    response.text().then(function (data) {
      if (data != 'OK') {
        if (data == 'Resource Exists') {
          $('#flash_message').append(flashMessage('warning', 'The value of the field updated would result in duplication. Request cancelled.'));
        }
        else {
          console.log(data)
          $('#flash_message').append(flashMessage('danger', 'Something unexpected happened. Please try again.'));
        }
      }
      else if (reload == true) {
        location.reload(true);
      }
    })
  });
}
// Delete request
function deleteRequest(el, object, serverUrl, values) {
  bootbox.confirm('Do you really want to delete the selected ' + object + '?', function (result) {
    if (result) {
      fetch(`${window.origin}` + serverUrl, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(values),
        cache: "no-cache",
        headers: new Headers({
          "content-type": "application/json"
        })
      }).then(function (response) {
        // First sort situation where response not 200
        if (response.status !== 200) {
          $('#flash_message').append(flashMessage('warning', 'We were unable to process your request. Please try again later.'));
          console.log(response.status);
          return;
        }
        response.text().then(function (data) {
          if (data == 'OK') {
            $('#flash_message').append(flashMessage('success', object + ' removed successfully.'));
            setTimeout(function() {location.reload(true);}, 2000);
            /*
            $(el).closest('tr').css('background', 'tomato');
            $(el).closest('tr').fadeOut(800, function () {
              el.remove();
            });*/
            
          }
          else {
            console.log(data)
            $('#flash_message').append(flashMessage('danger', 'Something unexpected happened. Please try again.'));
          }
        })
      });
    }
  });
}

// Flash messaging
var flashMessage = function (code, message) {
  html = '<div class="alert alert-' + code + '">' + message + '<button type="button" class="m1-2 mb-1 close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>';
  return html;
};

///////////////////////////////////////////////////////////////////////////////////////////////
// Customer CRUD /////////////////////////////////////////////////////////////////////////////
$(document).on('click', '#addCustomer', function (e) {
  e.preventDefault();
  var args = {
    formId: 'form_add_customer',
    serverUrl: '/crud/customers-create',
    object: 'Customer'
  };
  createRequest(args);
});

$('#customersEditable').editableTableWidget();
$('#customersEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#customersEditable td.editable').on('change', function (evt, newValue) {
  var rowx = $(this).attr("id");
  var values = {
    id: $(`.id${rowx}`).text(),
    phone_no: $(`.phone_number${rowx}`).text()
  };
  updateRequest('/crud/customers-update', values)
});

$('.deleteCustomer').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'customer', '/crud/customers-delete', values);
});
// Order CRUD /////////////////////////////////////////////////////////////////////////////
$(document).on('click', '#addOrder', function (e) {
  e.preventDefault();
  var args = {
    formId: 'form_add_order',
    serverUrl: '/crud/orders-create',
    object: 'Order'
  };
  createRequest(args);
});

$('#ordersEditable').editableTableWidget();
$('#ordersEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#ordersEditable td.editable').on('change', function (evt, newValue) {
  rowx = $(this).attr("id");
  var values = {
    id: $(`.id${rowx}`).text(),
    order_ref: $(`.order_ref${rowx}`).text(),
    amount: $(`.amount${rowx}`).text(),
    time: $(`.time${rowx}`).text()
  };
  updateRequest('/crud/orders-update', values)
});

$('.deleteOrder').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'order', '/crud/orders-delete', values);
});