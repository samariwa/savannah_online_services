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

/* google.charts.load("current", {packages:["corechart"]});
 google.charts.setOnLoadCallback(drawChart);
 function drawChart() {
    var where = 'fastmoving';
  $.post("../charts.php",{where:where},
   function(result){
     var data = $.parseJSON(result);
     var data0 = data[0][0];
     var data1 = data[0][1];
     var data2 = data[1][0];
     var data3 = data[1][1];
     var data4 = data[2][0];
     var data5 = data[2][1];
     var data6 = data[3][0];
     var data7 = data[3][1];
     var data8 = data[4][0];
     var data9 = data[4][1];
     var data10 = data[5][0];
     var data11 = data[5][1];
     var data12 = data[6][0];
     var data13 = data[6][1];
   var data = google.visualization.arrayToDataTable([
     [data0, data1],
    [data2, parseInt(data3)],
     [data4, parseInt(data5)],
     [data6, parseInt(data7)],
     [data8, parseInt(data9)],
     [data10, parseInt(data11)],
     [data12, parseInt(data13)],
   ]);
   var options = {
     title: 'Fast moving products',
     legend: 'none',
      is3D:true,
     pieSliceText: 'label',
     slices: {  1: {offset: 0.2},
               4: {offset: 0.1},
               0: {offset: 0.2},
               2: {offset: 0.1},
     },
   };

   var chart = new google.visualization.PieChart(document.getElementById('piechart'));
   chart.draw(data, options);
   });
 }

 google.charts.load("current", {packages:["corechart"]});
 google.charts.setOnLoadCallback(drawChart2);
 function drawChart2() {
    var where = 'fastselling';
  $.post("../charts.php",{where:where},
   function(result){
     var data = $.parseJSON(result);
     var data0 = data[0][0];
     var data1 = data[0][1];
     var data2 = data[1][0];
     var data3 = data[1][1];
     var data4 = data[2][0];
     var data5 = data[2][1];
     var data6 = data[3][0];
     var data7 = data[3][1];
     var data8 = data[4][0];
     var data9 = data[4][1];
     var data10 = data[5][0];
     var data11 = data[5][1];
     var data12 = data[6][0];
     var data13 = data[6][1];
   var data = google.visualization.arrayToDataTable([
     [data0, data1],
    [data2, parseInt(data3)],
     [data4, parseInt(data5)],
     [data6, parseInt(data7)],
     [data8, parseInt(data9)],
     [data10, parseInt(data11)],
     [data12, parseInt(data13)],
   ]);
   var options = {
     title: 'Fast moving products',
     legend: 'none',
      is3D:true,
     pieSliceText: 'label',
     slices: {  1: {offset: 0.2},
               4: {offset: 0.1},
               0: {offset: 0.2},
               2: {offset: 0.1},
     },
   };

   var chart = new google.visualization.PieChart(document.getElementById('piechart2'));
   chart.draw(data, options);
   });
 }

 google.charts.load('current', {'packages':['corechart']});
 google.charts.setOnLoadCallback(drawVisualization);

 function drawVisualization() {
   var where = 'salescomparison';
  $.post("../charts.php",{where:where},
   function(result){
              var data = google.visualization.arrayToDataTable([
     ['Day', 'Royson', 'Ken', 'Reuben', 'Damaris', 'George', 'Average'],
     ['07/08/2020',  165,      938,         522,             998,           450,      614.6],
     ['08/08/2020',  135,      1120,        599,             1268,          288,      682],
     ['09/08/2020',  157,      1167,        587,             807,           397,      623],
     ['10/08/2020',  139,      1110,        615,             968,           215,      609.4],
     ['Yesterday',  136,      691,         629,             1026,          366,      569.6],
     ['Today',  136,      691,         629,             1026,          366,      569.6],
   ]);

   var options = {
     title : 'Weekly Sales Made per Deliverer',
     vAxis: {title: 'Sales'},
     hAxis: {title: 'Day'},
     seriesType: 'bars',
     series: {5: {type: 'line'}}        };

   var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
   chart.draw(data, options);
   });
 }

 google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawComparison1);
function drawComparison1() {
 var where = 'salescomparison1';
  $.post("../charts.php",{where:where},
   function(result){
var data = google.visualization.arrayToDataTable([
   ['Deliverer', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
    'Western', 'Literature', { role: 'annotation' } ],
   ['Today', 10, 24, 20, 32, 18, 5, '']
 ]);

var view = new google.visualization.DataView(data);

 var options = {
   width: 550,
   height: 100,
   legend: { position: 'top', maxLines: 3 },
   bar: { groupWidth: '75%' },
   isStacked: true
 };
 var chart = new google.visualization.BarChart(document.getElementById("salesComparison1"));
 chart.draw(view, options);
 });
}

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawComparison2);
function drawComparison2() {
 var where = 'salescomparison2';
  $.post("../charts.php",{where:where},
   function(result){
var data = google.visualization.arrayToDataTable([
   ['Deliverer', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
    'Western', 'Literature', { role: 'annotation' } ],
   ['Yesterday', 10, 24, 20, 32, 18, 5, '']
 ]);

var view = new google.visualization.DataView(data);

 var options = {
   width: 550,
   height: 100,
   legend: { position: 'top', maxLines: 3 },
   bar: { groupWidth: '75%' },
   isStacked: true
 };
 var chart = new google.visualization.BarChart(document.getElementById("salesComparison2"));
 chart.draw(view, options);
  });
}

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawComparison3);
function drawComparison3() {
 var where = 'salescomparison3';
  $.post("../charts.php",{where:where},
   function(result){
var data = google.visualization.arrayToDataTable([
   ['Deliverer', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
    'Western', 'Literature', { role: 'annotation' } ],
   ['Yesterday', 10, 24, 20, 32, 18, 5, '']
 ]);

var view = new google.visualization.DataView(data);

 var options = {
   width: 550,
   height: 100,
   legend: { position: 'top', maxLines: 3 },
   bar: { groupWidth: '75%' },
   isStacked: true
 };
 var chart = new google.visualization.BarChart(document.getElementById("salesComparison3"));
 chart.draw(view, options);
   });
}

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawComparison4);
function drawComparison4() {
 var where = 'salescomparison4';
  $.post("../charts.php",{where:where},
   function(result){
     var data = $.parseJSON(result);
     // alert(data)
     var names = data[0];
     var figures = data[1];
    // alert(names)
    // alert(figures)
var data = google.visualization.arrayToDataTable([
   names,
   figures
 ]);

var view = new google.visualization.DataView(data);

 var options = {
   width: 550,
   height: 100,
   legend: { position: 'top', maxLines: 3 },
   bar: { groupWidth: '75%' },
   isStacked: true
 };
 var chart = new google.visualization.BarChart(document.getElementById("salesComparison4"));
 chart.draw(view, options);
  });
}

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawComparison5);
function drawComparison5() {
 var where = 'salescomparison5';
  $.post("../charts.php",{where:where},
   function(result){
     var data = $.parseJSON(result);
     var data0 = data[0];
var data = google.visualization.arrayToDataTable([
   ['Deliverer', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
    'Western', 'Literature', { role: 'annotation' } ],
   [data0, 10, 24, 20, 32, 18, 5, '']
 ]);

var view = new google.visualization.DataView(data);

 var options = {
   width: 550,
   height: 100,
   legend: { position: 'top', maxLines: 3 },
   bar: { groupWidth: '75%' },
   isStacked: true
 };
 var chart = new google.visualization.BarChart(document.getElementById("salesComparison5"));
 chart.draw(view, options);
 });
}

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawComparison6);
function drawComparison6() {
 var where = 'salescomparison6';
  $.post("../charts.php",{where:where},
   function(result){
     var data = $.parseJSON(result);
     var data0 = data[0];
var data = google.visualization.arrayToDataTable([
   ['Deliverer', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
    'Western',  { role: 'annotation' } ],
   [data0, 10, 24, 20, 32, 18, '']
 ]);

var view = new google.visualization.DataView(data);
 var options = {
   width: 550,
   height: 100,
   legend: { position: 'top', maxLines: 3 },
   bar: { groupWidth: '75%' },
   isStacked: true
 };
 var chart = new google.visualization.BarChart(document.getElementById("salesComparison6"));
 chart.draw(view, options);
 });
}

 /*  var data = google.visualization.arrayToDataTable([
     [data0, data1],
    [data2, parseInt(data3)],
     [data4, parseInt(data5)],
     [data6, parseInt(data7)],
     [data8, parseInt(data9)],
     [data10, parseInt(data11)],
     [data12, parseInt(data13)],
   ]);*/



$(document).ready(function () {
  $(".paginate").DataTable({
    "ordering": false
  });

});


$(document).ready(function () {
  $("#customerOrderSearch").DataTable({
    "ordering": false,
    "pageLength": 5,
    "lengthChange": false,
    "info": false,
    "oLanguage": {
      "sSearch": "<i class='fa fa-search'></i>&ensp;Customer Search:",
      "sZeroRecords": "Customer Not Found"
    }
  });
});

$(document).ready(function () {
  $("#sellerRequisitionSearch").DataTable({
    "ordering": false,
    "pageLength": 5,
    "lengthChange": false,
    "info": false,
    "oLanguage": {
      "sSearch": "<i class='fa fa-search'></i>&ensp;Seller Search:",
      "sZeroRecords": "Seller Not Found"
    }
  });
});

$(document).ready(function () {
  $("#employeePayslipSearch").DataTable({
    "ordering": false,
    "pageLength": 5,
    "lengthChange": false,
    "info": false,
    "oLanguage": {
      "sSearch": "<i class='fa fa-search'></i>&ensp;Employee Search:",
      "sZeroRecords": "Employee Not Found"
    }
  });
});

$(document).ready(function () {
  $("#productOrderSearch").DataTable({
    "ordering": false,
    "pageLength": 5,
    "lengthChange": false,
    "info": false,
    "oLanguage": {
      "sSearch": "<i class='fa fa-search'></i>&ensp;Product Search:",
      "sZeroRecords": "Product Not Found"
    }
  });
});

$(document).ready(function () {
  $("#productSalesSearch").DataTable({
    "ordering": false,
    "pageLength": 5,
    "lengthChange": false,
    "info": false,
    "oLanguage": {
      "sSearch": "<i class='fa fa-search'></i>&ensp;Product Search:",
      "sZeroRecords": "Product Not Found"
    }
  });

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
          if (data == 'Error: Image Missing') {
            $('#flash_message').append(flashMessage('danger', data));
          }
          else if (data == 'Error: The refund value cannot be greater than the account balance') {
            $('#flash_message').append(flashMessage('danger', data));
          }
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
            $(el).closest('tr').css('background', 'tomato');
            $(el).closest('tr').fadeOut(800, function () {
              el.remove();
            });
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

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Customers CRUD ///////////////////////////////////////////////////////////////

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
$('#customersEditable td').on('change', function (evt, newValue) {
  var rowx = parseInt(evt.target._DT_CellIndex.row) + 1;
  var values = {
    id: $(`#id${rowx}`).text(),
    first_name: $(`#firstname${rowx}`).text(),
    last_name: $(`#lastname${rowx}`).text(),
    phone_no: $(`#number${rowx}`).text(),
    location: $(`#location${rowx}`).text(),
    note: $(`#note${rowx}`).text()
  };
  updateRequest('/crud/customers-update', values)
});

$('.blacklistCustomer').click(function () {
  var el = $(this)
  bootbox.confirm('Do you really want to blacklist the selected customer?', function (result) {
    if (result) {
      var values = {
        id: el.attr("id"),
        customer_status: 'blacklisted'
      }
      updateRequest('/crud/customers-update', values)
      $(el).closest('tr').css('background', 'tomato');
      $(el).closest('tr').fadeOut(800, function () {
        el.remove();
      });
    }
  });
});

$('.restoreBlacklistedCustomer').click(function () {
  var el = $(this)
  bootbox.confirm('Do you really want to restore the selected blacklisted customer?', function (result) {
    if (result) {
      var values = {
        id: el.attr("id"),
        customer_status: 'active'
      }
      updateRequest('/crud/customers-update', values)
      $(el).closest('tr').css('background', 'lime');
      $(el).closest('tr').fadeOut(800, function () {
        el.remove();
      });
    }
  });
});

$(".customer_status_checkbox").change(function () {
  var values = {}
  if (this.checked) {
    values.id = $(this).attr("value");
    values.customer_status = 'active';
  }
  else {
    values.id = $(this).attr("value");
    values.customer_status = 'inactive';
  }
  updateRequest('/crud/customers-update', values)
});

$(".credit_customer_checkbox").change(function () {
  var values = {}
  if (this.checked) {
    values.id = $(this).attr("value");
    values.credit_customer = 1;
  }
  else {
    values.id = $(this).attr("value");
    values.credit_customer = '0';
  }
  updateRequest('/crud/customers-update', values)
});

$(document).on('click', '.addRefund', function (e) {
  e.preventDefault();
  /*
  In this function fetch ID of form with ID attribute of the button.
  Each product has its own restock form which have unique form IDS
  which are uniquely identified by the ID
  */
  var args = {
    formId: 'form_add_refund' + $(this).attr("id"),
    serverUrl: '/crud/refund-customer',
    object: 'Customer Refund'
  };
  createRequest(args);
});

$('.deleteCustomer').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'customer', '/crud/customers-delete', values);
});
// Categories CRUD ///////////////////////////////////////////////////////////////

$(document).on('click', '#addCategory', function (e) {
  e.preventDefault();
  var args = {
    formId: 'form_add_category',
    serverUrl: '/crud/categories-create',
    object: 'Category'
  };
  createRequest(args);
});

$('#categoriesEditable').editableTableWidget();
$('#categoriesEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#categoriesEditable td').on('change', function (evt, newValue) {
  var rowx = parseInt(evt.target._DT_CellIndex.row) + 1;
  var values = {
    id: $(`#id${rowx}`).text(),
    category_name: $(`#category${rowx}`).text()
  };
  updateRequest('/crud/categories-update', values)
});

$(".category_status_checkbox").change(function () {
  var values = {}
  if (this.checked) {
    values.id = $(this).attr("value");
    values.category_status = 'active';
  }
  else {
    values.id = $(this).attr("value");
    values.category_status = 'inactive';
  }
  updateRequest('/crud/categories-update', values)
});

$('.deleteCategory').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'category', '/crud/categories-delete', values);
});
// Stock CRUD ///////////////////////////////////////////////////////////////////
$(document).on('click', '#addProduct', function (e) {
  e.preventDefault();
  var args = {
    formId: 'form_add_product',
    serverUrl: '/crud/products-create',
    object: 'Product'
  };
  createRequest(args);
});

$(document).on('click', '.addPurchase', function (e) {
  e.preventDefault();
  /*
  In this function fetch ID of form with ID attribute of the button.
  Each product has its own restock form which have unique form IDS
  which are uniquely identified by the ID
  */
  var args = {
    formId: 'form_restock_product' + $(this).attr("id"),
    serverUrl: '/crud/products-restock',
    object: 'Product Purchase'
  };
  createRequest(args);
});

$('#stockEditable').editableTableWidget();
$('#stockEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#stockEditable td').on('change', function (evt, newValue) {
  var rowx = parseInt(evt.target._DT_CellIndex.row) + 1;
  var values = {
    id: $(`#id${rowx}`).text(),
    product_name: $(`#name${rowx}`).text(),
    restock_level: $(`#restock_level${rowx}`).text()
  };
  updateRequest('/crud/products-update', values)
});

$(".product_status_checkbox").change(function () {
  var values = {}
  if (this.checked) {
    values.id = $(this).attr("value");
    values.product_status = 'active';
  }
  else {
    values.id = $(this).attr("value");
    values.product_status = 'inactive';
  }
  updateRequest('/crud/products-update', values)
});

$('#addReclassCategory').click(function (e) {
  e.preventDefault();
  var args = {
    formId: 'form_add_reclass_category',
    serverUrl: '/crud/reclass-category-create',
    object: 'Reclass Category'
  };
  createRequest(args);
});

$('.parent_product').keyup(function () {
  if ($('.parent_product').val() != '') {
    var value = {
      'string': $('.parent_product').val()
    }
    var results = ''
    fetch(`${window.origin}` + '/crud/search-reclass-product', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(value),
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
        var search_results = JSON.parse(data);
        for (let product_id in search_results) {
          results += '<a href="#" class="list-group-item list-group-item-action border-1 offset-1 product-item" id="' + product_id + '">' + search_results[product_id] + '</a>';
        }
        $('#parent_product_results').html(results);
      })
    });
  }
  else {
    $('#parent_product_results').html('');
  }
  $(document).on('click', 'a', function () {
    $(".parent_product").val($(this).text());
    $("#parent_product_results").html('');
    document.querySelector('.selected_product_id').setAttribute("value", $(this).attr("id"))
  });
});

$('#addReclassItem').click(function (e) {
  e.preventDefault();
  var args = {
    formId: 'form_add_reclass_item',
    serverUrl: '/crud/reclass-item-create',
    object: 'Reclass Item'
  };
  createRequest(args);
});

$('.child_product').keyup(function () {
  if ($('.child_product').val() != '') {
    var value = {
      'string': $('.child_product').val()
    }
    var results = ''
    fetch(`${window.origin}` + '/crud/search-reclass-product', {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(value),
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
        var search_results = JSON.parse(data);
        for (let product_id in search_results) {
          results += '<a href="#" class="list-group-item list-group-item-action border-1 offset-1 product-item" id="' + product_id + '">' + search_results[product_id] + '</a>';
        }
        $('#child_product_results').html(results);
      })
    });
  }
  else {
    $('#child_product_results').html('');
  }
  $(document).on('click', 'a', function () {
    $(".child_product").val($(this).text());
    $("#child_product_results").html('');
    document.querySelector('.selected_product_id').setAttribute("value", $(this).attr("id"))
  });
});

$('#reclassCategoriesEditable').editableTableWidget();
$('#reclassCategoriesEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#reclassCategoriesEditable td').on('change', function (evt, newValue) {
  var rowx = parseInt(evt.target._DT_CellIndex.row) + 1;
  var values = {
    id: $(`#reclass_category_id${rowx}`).text(),
    reclass_category_name: $(`#reclass_category_name${rowx}`).text()
  };
  updateRequest('/crud/products-reclass-categories-update', values)
});

$('#reclassDetailsEditable').editableTableWidget();
$('#reclassDetailsEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#reclassDetailsEditable td').on('change', function (evt, newValue) {
  var rowx = parseInt(evt.target._DT_CellIndex.row) + 1;
  var values = {
    id: $(`#reclass_item_id${rowx}`).text(),
    adjustment: $(`#reclass_detail_adjustment${rowx}`).text()
  };
  updateRequest('/crud/products-reclass-update', values, reload = true)
});

$('.deleteStock').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'product', '/crud/products-delete', values);
});

$('.deleteReclassCategory').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'product reclass category', '/crud/product-reclass-categories-delete', values);
});

$('.deleteReclassItem').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'product reclass item', '/crud/product-reclass-items-delete', values);
});
// Damaged Stock Update //////////////////////////////////////////////////////////

$('#damagedEditable').editableTableWidget();
$('#damagedEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#damagedEditable td').on('change', function (evt, newValue) {
  var rowx = parseInt(evt.target._DT_CellIndex.row) + 1;
  var values = {
    batch_id: $(`#id${rowx}`).text(),
    new_qty: $(`#new_qty_damaged${rowx}`).text()
  };
  updateRequest('/crud/damaged-products-update', values, reload = true)
});

// Suppliers CRUD ////////////////////////////////////////////////////////////////

$(document).on('click', '#addSupplier', function (e) {
  e.preventDefault();
  var args = {
    formId: 'form_add_supplier',
    serverUrl: '/crud/suppliers-create',
    object: 'Supplier'
  };
  createRequest(args);
});

$('#suppliersEditable').editableTableWidget();
$('#suppliersEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#suppliersEditable td').on('change', function (evt, newValue) {
  var rowx = parseInt(evt.target._DT_CellIndex.row) + 1;
  var values = {
    id: $(`#id${rowx}`).text(),
    supplier_contact: $(`#contact${rowx}`).text()
  };
  updateRequest('/crud/suppliers-update', values)
});

$(".supplier_status_checkbox").change(function () {
  var values = {}
  if (this.checked) {
    values.id = $(this).attr("value");
    values.supplier_status = 'active';
  }
  else {
    values.id = $(this).attr("value");
    values.supplier_status = 'inactive';
  }
  updateRequest('/crud/suppliers-update', values)
});

$('.deleteSupplier').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'supplier', '/crud/suppliers-delete', values);
});
// Product Unit Automation Settings Update ////////////////////////////////////////////////////
$(document).on('click', '.editAutomation', function (e) {
  e.preventDefault();
  var id = $(this).attr("id");
  var values = {
    id: id,
    unit_id: $(`#unit${id}`).val(),
    contains: $(`#contains${id}`).val(),
    sub_unit_id: $(`#subunit${id}`).val(),
    subunit_replenish_qty: $(`#replenish${id}`).val(),
    restock_level: $(`#restock${id}`).val()
  };
  updateRequest('/crud/product-units-automation-update', values)
  $('.close').click();
});

// Product Units CRUD ///////////////////////////////////////////////////////////////////////
$(document).on('click', '#addUnit', function (e) {
  e.preventDefault();
  var args = {
    formId: 'form_add_unit',
    serverUrl: '/crud/product-units-create',
    object: 'Product Unit'
  };
  createRequest(args);
});

$('#productUnitsEditable').editableTableWidget();
$('#productUnitsEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#productUnitsEditable td').on('change', function (evt, newValue) {
  var rowx = parseInt(evt.target._DT_CellIndex.row) + 1;
  var values = {
    id: $(`#id${rowx}`).text(),
    unit_name: $(`#unit${rowx}`).text(),
    measurement_mode: $(`#mode${rowx}`).text()
  };
  updateRequest('/crud/product-units-update', values)
});

$(".product_unit_status_checkbox").change(function () {
  var values = {}
  if (this.checked) {
    values.id = $(this).attr("value");
    values.product_unit_status = 'active';
  }
  else {
    values.id = $(this).attr("value");
    values.product_unit_status = 'inactive';
  }
  updateRequest('/crud/product-units-update', values)
});

$('.deleteUnit').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'product unit', '/crud/product-units-delete', values);
});

// Expenses CRUD /////////////////////////////////////////////////////////////////////

$(document).on('click', '#addExpense', function (e) {
  e.preventDefault();
  var args = {
    formId: 'form_add_expense',
    serverUrl: '/crud/expenses-create',
    object: 'Expense'
  };
  createRequest(args);
});

$('#expensesEditable').editableTableWidget();
$('#expensesEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#expensesEditable td').on('change', function (evt, newValue) {
  var rowx = parseInt(evt.target._DT_CellIndex.row) + 1;
  var values = {
    id: $(`#id${rowx}`).text(),
    expense_description: $(`#expense_description${rowx}`).text(),
    party: $(`#party${rowx}`).text(),
    total_owed_amount: $(`#total_owed_amount${rowx}`).text(),
    expense_date: $(`#expense_date${rowx}`).text()
  };
  if (parseInt($(`#payment${rowx}`).text()) > 0) {
    var expense_details = {
      expense_id: values['id'],
      old_balance: parseInt($(`#due${rowx}`).text()),
      paid_amount: parseInt($(`#payment${rowx}`).text()),
      new_balance: parseInt($(`#due${rowx}`).text()) - parseInt($(`#payment${rowx}`).text())
    }
    values['total_paid_amount'] = parseInt($(`#paid${rowx}`).text()) + parseInt($(`#payment${rowx}`).text());
    updateRequest('/crud/expenses-update', values)
    addPaymentDetail(expense_details);
  }
  else if (parseInt($(`#payment${rowx}`).text()) < 0) {
    return $('#flash_message').append(flashMessage('warning', 'Payment amount cannot be a negative number.'));
  }
  else {
    updateRequest('/crud/expenses-update', values)
  }
});

$('.deleteExpense').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'expense', '/crud/expense-delete', values);
});
// Expense Payment Details CRUD //////////////////////////////////////////////////////
function addPaymentDetail(params) {
  var data = new FormData();
  data.append('expense_id', params['expense_id']);
  data.append('old_balance', params['old_balance']);
  data.append('paid_amount', params['paid_amount']);
  data.append('new_balance', params['new_balance']);
  fetch(`${window.origin}/crud/expense-payment-detail-create`, {
    method: "POST",
    credentials: "include",
    body: data,
    cache: "no-cache",
  }).then(function (response) {
    // First sort successful resource creations
    if (response.status == 201) {
      $('#flash_message').append(flashMessage('success', 'Expense Payment Detail added successfully'));
      return;
    }
    // Else handle errors
    response.text().then(function (data) {
      // Any error
      $('#flash_message').append(flashMessage('danger', 'Something unexpected happened. Please try again.'));
    });
  });
}

$('#expensePaymentDetailsEditable').editableTableWidget();
$('#expensePaymentDetailsEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#expensePaymentDetailsEditable td').on('change', function (evt, newValue) {
  var rowx = parseInt(evt.target._DT_CellIndex.row) + 1;
  if (parseInt($(`#payment${rowx}`).text()) < 0) {
    return $('#flash_message').append(flashMessage('warning', 'Payment amount cannot be a negative number.'));
  }
  else if (parseInt($(`#payment${rowx}`).text()) > 0) {
    var values = {
      id: $(`#id${rowx}`).text(),
      paid_amount: parseInt($(`#payment${rowx}`).text())
    }
    updateRequest('/crud/expense-payment-details-update', values, reload = true)
  }
});

$('.deleteExpensePaymentDetail').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'expense payment detail', '/crud/expense-payment-detail-delete', values);
});
// Expense Categories CRUD ///////////////////////////////////////////////////////////

$(document).on('click', '#addExpenseCategory', function (e) {
  e.preventDefault();
  var args = {
    formId: 'form_add_expense_category',
    serverUrl: '/crud/expense-categories-create',
    object: 'Expense Category'
  };
  createRequest(args);
});

$('#expenseCategoryEditable').editableTableWidget();
$('#expenseCategoryEditable td.uneditable').on('change', function (evt, newValue) {
  return false;
});
$('#expenseCategoryEditable td').on('change', function (evt, newValue) {
  var rowx = parseInt(evt.target._DT_CellIndex.row) + 1;
  var values = {
    id: $(`#id${rowx}`).text(),
    expense_category: $(`#expense_category${rowx}`).text()
  };
  updateRequest('/crud/expense-categories-update', values)
});

$(".expense_category_status_checkbox").change(function () {
  var values = {}
  if (this.checked) {
    values.id = $(this).attr("value");
    values.expense_category_status = 'active';
  }
  else {
    values.id = $(this).attr("value");
    values.expense_category_status = 'inactive';
  }
  updateRequest('/crud/expense-categories-update', values)
});

$('.deleteExpenseCategory').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'expense category', '/crud/expense-category-delete', values);
});
// Staff /////////////////////////////////////////////////////////////////////////////
$(document).on('click', '#addAdmin', function (e) {
  e.preventDefault();
  var args = {
    formId: 'form_add_admin',
    serverUrl: '/crud/admin-create',
    object: 'Admin'
  };
  createRequest(args);
});

$('.apply_admin_action').click(function (e) {
  e.preventDefault();
  var status = $("input[name='actions']:checked").val();
  if (status == 'active' || status == 'suspended') {
    var values = {
      id: $(this).attr("id"),
      user_status: status
    };
    updateRequest('/crud/admin-update', values, reload = true)
  }
  else if (status == 'revoked') {
    var values = {
      id: $(this).attr("id")
    }
    deleteRequest($(this), 'admin', '/crud/admin-delete', values);
  }
});

$('.deleteAdmin').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'staff', '/crud/staff-delete', values);
});
// Backup ////////////////////////////////////////////////////////////////////////////
$('#runInstantBackup').click(async function () {
  try {
    var loader = '';
    loader += '<div class="d-flex justify-content-center">';
    loader += '<div class="spinner-border text-success mt-5 mb-5" role="status">';
    loader += '<span class="sr-only">Loading...</span>';
    loader += '</div>';
    loader += '</div>';
    $(`#backup_loader`).html(loader);
    const response = await fetch(`${window.origin}` + '/crud/run_backup_job');
    if (response.status == 200) {
      $('#flash_message').append(flashMessage('success', 'System Backup Completed Successfully'));
      console.log(response.status);
    } else {
      const data = await response.json();
      console.log(data);
      $('#flash_message').append(flashMessage('danger', 'Something unexpected happened. Please try again.'));
    }
    $(`#backup_loader`).html('');
  } catch (error) {
    console.error('An error occurred:', error);
    $('#flash_message').append(flashMessage('danger', 'Something unexpected happened. Please try again.'));
  }
});

$('.downloadBackup').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  fetch(`${window.origin}` + '/crud/download_backup', {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(values),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  }).then(function (response) {});
});

$('.deleteBackup').click(function () {
  var values = {
    id: $(this).attr("id")
  }
  deleteRequest($(this), 'backup', '/crud/delete_backup', values);
});
//////////////////////////////////////////////////////////////////////////////////////
let switches = document.querySelectorAll('.ios-switch')

for (var i = 0; i < switches.length; i++) {
  switches[i].addEventListener('click',
    function (event) {
      if (this.classList.contains('active')) {
        this.classList.remove('active');
        this.querySelector('input[type=checkbox').checked = false;
        enable_complete_order();
      }
      else {
        this.classList.add('active');
        this.querySelector('input[type=checkbox').checked = true;
        enable_complete_order();
      }
    })
}

$(document).on('click', '#uploadFile', function () {
  var name = $('#name').val();
  var description = $('#description').val();
  var form = $('#upload').serialize();
  var form = $('form')[0];
  // You need to use standard javascript object here
  var upload = new FormData(form);
  var location = $('#location').val();
  var where = 'files';
  $.post("../add.php", { name: name, description: description, location: location, upload: upload, where: where },
    function (result) {
      if (result == 'success') {
        alert('File Uploaded Successfully');
        location.reload(true);
      }
      else if (result == 'exists') {
        alert('File Already Exists');
      }
      else {
        alert("Something went wrong");
      }
    });
});


$(document).on('click', '#addFAQ', function () {
  formAjax('Question');
});

$(document).on('click', '#addBlog', function () {
  var blog_text = tinyMCE.get('blog').getContent();
  var form_data = new FormData($('form')[0]);
  form_data.append('blog_text', blog_text);
  $.ajax({
    url: '../add.php',
    type: 'post',
    data: form_data,
    contentType: false,
    processData: false,
    cache: false,
    success: function (data) {
      if (data == 'exists') {
        alert('Blog Already Exists');
        location.reload(true);
      }
      else {
        alert("Blog Added Successfully");
        location.reload(true);
      }
    }
  });
});



$(document).on('click', '#addNote', function () {
  var title = $('#title').val();
  var message = $('#body').val();
  var radios = document.getElementsByName('access');
  for (var i = 0, length = radios.length; i < length; i++) {
    if (radios[i].checked) {
      var access = radios[i].value;
    }
  }
  var where = 'note';
  $.post("../add.php", { title: title, message: message, access: access, where: where },
    function (result) {
      if (result == 'success') {
        alert('Note Added Successfully');
        location.reload(true);
      }
      else {
        alert("Something went wrong");
      }
    });
});

$(document).on('click', '#addVehicle', function () {
  formAjax('Vehicle');
});


$(document).on('click', '#addSickoffApplication', function () {
  var employee = $('#employee').val();
  var reason = $('#sickoffReason').val();
  var start = $('#sickOffStart').val();
  var number = $('#sickoffNumber').val();
  var where = 'sickoff';
  $.post("../add.php", { employee: employee, reason: reason, start: start, number: number, where: where },
    function (result) {
      if (result == 'success') {
        alert('Sick leave application successful');
        location.reload(true);
      }
      else {
        alert(result)
        alert("Something went wrong");
      }
    });
});

$(document).on('click', '#addLeaveApplication', function () {
  var employee = $('#employee').val();
  var start = $('#leaveStart').val();
  var number = $('#leaveNumber').val();
  var standIn = $('#standIn').val();
  var where = 'leave';
  $.post("../add.php", { employee: employee, standIn: standIn, start: start, number: number, where: where },
    function (result) {
      if (result == 'success') {
        alert('Leave application successful');
        location.reload(true);
      }
      else if (result == 'exceeded') {
        alert('Days applied exceeded days remaining. Application failed.');
      }
      else if (result == 'failed') {
        alert('Kindly select another stand in employee. Application failed.');
      }
      else {
        alert("Something went wrong");
      }
    });
});



$(document).on('click', '#addDeliverer', function () {
  formAjax('Deliverer');
});

$(document).on('click', '#addCook', function () {
  formAjax('Cook');
});

$(document).on('click', '#addCleaner', function () {
  formAjax('Cleaner');
});

$(document).on('click', '#addOfficeStaff', function () {
  formAjax('Office Staff');
});

function deleteAjax(id, el, module, where) {
  bootbox.confirm('Do you really want to delete the selected ' + module + '?', function (result) {
    if (result) {
      $.post("../delete.php", { id: id, where: where },
        function (result) {
          if (result == 1) {
            $(el).closest('tr').css('background', 'tomato');
            $(el).closest('tr').fadeOut(800, function () {
              el.remove();
            });
          }
        });
    }
  });
}

$('.deleteBlacklist').click(function () {
  deleteAjax($(this).attr("id"), $(this), 'blacklisted customer', 'blacklist');
});



$('.deleteVehicle').click(function () {
  deleteAjax($(this).attr("id"), $(this), 'vehicle', 'vehicle');
});

$('.deleteDeliverer').click(function () {
  deleteAjax($(this).attr("id"), $(this), 'deliverer', 'deliverer');
});

$('.deleteCook').click(function () {
  deleteAjax($(this).attr("id"), $(this), 'cook', 'cook');
});

$('.deleteOffice').click(function () {
  deleteAjax($(this).attr("id"), $(this), 'office staff', 'office');
});

$('.deletePublicNote').click(function () {
  deleteAjax($(this).attr("id"), $(this), 'note', 'publicNote');
});

$('.deletePrivateNote').click(function () {
  deleteAjax($(this).attr("id"), $(this), 'note', 'privateNote');
});

$('.deleteFAQ').click(function () {
  deleteAjax($(this).attr("id"), $(this), 'FAQ', 'faq');
});

$('.deleteBlog').click(function () {
  deleteAjax($(this).attr("id"), $(this), 'Blog', 'blog');
});

$(document).on('click', '.editPublicNote', function () {
  var where = 'publicNote';
  var el = $(this);
  var id = el.attr("id");
  var title = $(`#title${id}`).val();
  var body = $(`#body${id}`).val();
  $.post("../save.php", { id: id, title: title, body: body, where: where },
    function (result) {
      location.reload(true);
    });
});

$(document).on('click', '.editPrivateNote', function () {
  var where = 'privateNote';
  var el = $(this);
  var id = el.attr("id");
  var title = $(`#title${id}`).val();
  var body = $(`#body${id}`).val();
  $.post("../save.php", { id: id, title: title, body: body, where: where },
    function (result) {
      location.reload(true);
    });
});

$(document).on('click', '.editFAQ', function () {
  var where = 'faq';
  var el = $(this);
  var id = el.attr("id");
  var question = $(`#question${id}`).val();
  var answer = $(`#answer${id}`).val();
  $.post("../save.php", { id: id, question: question, answer: answer, where: where },
    function (result) {
      location.reload(true);
    });
});

$(document).on('click', '.editBlog', function () {
  var where = 'blog';
  var el = $(this);
  var id = el.attr("id");
  var title = $(`#title${id}`).val();
  var blog = tinyMCE.get('blog' + id).getContent();
  $.post("../save.php", { id: id, title: title, blog: blog, where: where },
    function (result) {
      location.reload(true);
    });
});

$(document).on('click', '.addService', function () {
  var where = 'service';
  var el = $(this);
  var id = el.attr("id");
  var now = $(`#now${id}`).val();
  var note = $(`#note${id}`).val();
  var next = $(`#next${id}`).val();
  $.post("../save.php", { id: id, now: now, note: note, next: next, where: where },
    function (result) {
      location.reload(true);
    });
});

$(document).on('click', '.addInspection', function () {
  var where = 'inspection';
  var el = $(this);
  var id = el.attr("id");
  var now = $(`#Now${id}`).val();
  var note = $(`#Note${id}`).val();
  var next = $(`#Next${id}`).val();
  $.post("../save.php", { id: id, now: now, note: note, next: next, where: where },
    function (result) {
      location.reload(true);
    });
});

$(document).on('click', '.saveDriver', function () {
  var where = 'driver';
  var el = $(this);
  var id = el.attr("id");
  var driver = $(`#driver${id}`).val();
  $.post("../save.php", { id: id, driver: driver, where: where },
    function (result) {
      alert("Vehicle driver Successfully changed");
    });
});

$("#receiptCustomer").on("keyup", function () {
  var txt = $('#receiptCustomer').val();
  if (txt != '') {
    $.ajax({
      url: '../search.php',
      type: "post",
      data: { receiptSearch: txt },
      dataType: "text",
      success: function (data) {

        $('#customerReceiptResult').html(data);
      }
    });
  }
  else {
    $('#customerReceiptResult').html('');
  }
  $(document).on('click', 'a', function () {
    $("#receiptCustomer").val($(this).text());
    var id = $(this).attr("id");
    $('#customerId').val(id);
    $("#customerReceiptResult").html('');
  });
})

$(document).on('click', '.printReceipt', function () {
  var name = $(`#receiptCustomer`).val();
  var date = $(`#receiptDate`).val();
  var time = $(`#receiptTime`).val();
  $.post("receiptPDF.php", { name: name, date: date, time: time },
    function (result) {
      var mywindow = window.open('', 'Sympha Fresh', 'height=400,width=600');
      mywindow.document.write('<html><head><title></title>');
      mywindow.document.write('</head><body>');
      mywindow.document.write(result);
      mywindow.document.write('</body></html>');
      mywindow.document.close();
      mywindow.focus();
      mywindow.print();
      //mywindow.close();
    });
});

$(document).on('click', '.printCustomers', function () {
  $.ajax({
    url: 'customersPrint.php',
    type: 'get',
    dataType: 'html',
    success: function (data) {
      var mywindow = window.open('', 'Sympha Fresh', 'height=400,width=600');
      mywindow.document.write('<html><head><title></title>');
      mywindow.document.write('</head><body>');
      mywindow.document.write(data);
      mywindow.document.write('</body></html>');
      mywindow.document.close();
      mywindow.focus();
      mywindow.print();
      //mywindow.close();

    }
  });
});

$(document).on('click', '.printStock', function () {
  $.ajax({
    url: 'stockPrint.php',
    type: 'get',
    dataType: 'html',
    success: function (data) {
      var mywindow = window.open('', 'Sympha Fresh', 'height=400,width=600');
      mywindow.document.write('<html><head><title></title>');
      mywindow.document.write('</head><body>');
      mywindow.document.write(data);
      mywindow.document.write('</body></html>');
      mywindow.document.close();
      mywindow.focus();
      mywindow.print();
      //mywindow.close();
    }
  });
});

$(document).on('click', '.printSales', function () {
  $.ajax({
    url: 'salesPrint.php',
    type: 'get',
    dataType: 'html',
    success: function (data) {
      var mywindow = window.open('', 'Sympha Fresh', 'height=400,width=600');
      mywindow.document.write('<html><head><title></title>');
      mywindow.document.write('</head><body>');
      mywindow.document.write(data);
      mywindow.document.write('</body></html>');
      mywindow.document.close();
      mywindow.focus();
      mywindow.print();
      //mywindow.close();

    }
  });
});

$(document).on('click', '.printExtraSales', function () {
  $.ajax({
    url: 'extraSalesPrint.php',
    type: 'get',
    dataType: 'html',
    success: function (data) {
      var mywindow = window.open('', 'Sympha Fresh', 'height=400,width=600');
      mywindow.document.write('<html><head><title></title>');
      mywindow.document.write('</head><body>');
      mywindow.document.write(data);
      mywindow.document.write('</body></html>');
      mywindow.document.close();
      mywindow.focus();
      mywindow.print();
      //mywindow.close();

    }
  });
});

$(document).on('click', '.printGatePass', function () {
  var deliverer = $(`#deliverer`).val();
  var time = $(`#gatePassTime`).val();
  $.post("gatePassPDF.php", { deliverer: deliverer, time: time },
    function (result) {
      var mywindow = window.open('', 'Sympha Fresh', 'height=400,width=600');
      mywindow.document.write('<html><head><title></title>');
      mywindow.document.write('</head><body>');
      mywindow.document.write(result);
      mywindow.document.write('</body></html>');
      mywindow.document.close();
      mywindow.focus();
      mywindow.print();
      //mywindow.close();
    });
});

$(document).on('click', '.printDistribution', function () {
  var deliverer = $(`#deliverer`).val();
  var time = $(`#distributionTime`).val();
  $.post("distributionPDF.php", { deliverer: deliverer, time: time },
    function (result) {
      var mywindow = window.open('', 'Sympha Fresh', 'height=400,width=600');
      mywindow.document.write('<html><head><title></title>');
      mywindow.document.write('</head><body>');
      mywindow.document.write(result);
      mywindow.document.write('</body></html>');
      mywindow.document.close();
      mywindow.focus();
      mywindow.print();
      //mywindow.close();
    });
});

$(document).on('click', '.printSalesInvoice', function () {
  var deliverer = $(`#deliverer`).val();
  var date = $(`#invoiceDate`).val();
  $.post("sales_invoice_print.php", { deliverer: deliverer, date: date },
    function (result) {
      var mywindow = window.open('', 'Sympha Fresh', 'height=400,width=600');
      mywindow.document.write('<html><head><title></title>');
      mywindow.document.write('</head><body>');
      mywindow.document.write(result);
      mywindow.document.write('</body></html>');
      mywindow.document.close();
      mywindow.focus();
      mywindow.print();
      //mywindow.close();
    });
});

$(document).on('click', '.printCreditNote', function () {
  var deliverer = $(`#deliverer`).val();
  var date = $(`#creditDate`).val();
  $.post("credit_note_print.php", { deliverer: deliverer, date: date },
    function (result) {
      var mywindow = window.open('', 'Sympha Fresh', 'height=400,width=600');
      mywindow.document.write('<html><head><title></title>');
      mywindow.document.write('</head><body>');
      mywindow.document.write(result);
      mywindow.document.write('</body></html>');
      mywindow.document.close();
      mywindow.focus();
      mywindow.print();
      //mywindow.close();
    });
});

$(document).on('click', '.printPaymentStatus', function () {
  var deliverer = $(`#deliverer`).val();
  var date = $(`#statusDate`).val();
  $.post("payment_status_print.php", { deliverer: deliverer, date: date },
    function (result) {
      var mywindow = window.open('', 'Sympha Fresh', 'height=400,width=600');
      mywindow.document.write('<html><head><title></title>');
      mywindow.document.write('</head><body>');
      mywindow.document.write(result);
      mywindow.document.write('</body></html>');
      mywindow.document.close();
      mywindow.focus();
      mywindow.print();
      //mywindow.close();
    });
});

$(document).ready(function () {
  var tableLeftovers = document.getElementById("leftoversEditable");
  var sumVal = 0;
  for (var i = 1; i < tableLeftovers.rows.length; i++) {
    sumVal += parseInt(tableLeftovers.rows[i].cells[7].innerHTML);
    document.getElementById("totalLeftoverValue").innerHTML = sumVal;
  }
});

function replenishDisable() {
  var input = document.getElementById(`replenish`);
  input.disabled = true;
  input.value = "0";
}

function subunitsDisable() {
  var input1 = document.getElementById(`contains`);
  input1.disabled = true;
  var input2 = document.getElementById(`subunit`);
  input2.disabled = true;
  input1.value = "0";
  input2.value = "1";
}

function processOrder(check, action) {
  var id = check.value;
  var value = '';
  var where = 'process_order';
  if (check.checked) {
    value = '1';
  } else {
    value = '0';
  }
  $.post("../save.php", { id: id, value: value, action: action, where: where },
    function (result) {

    });
}

function displayname(input, _this) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      _this.siblings('label').html(input.files[0]['name'])

    }

    reader.readAsDataURL(input.files[0]);
  }
}




// TESTS /////////////////////////////////////////////////////////////////////////////
category_table =$('#testEditable').DataTable({
  "processing": true,
  "serverSide": true,
  "paging": true,
  "pageLength": 10,
  "scroller": true,
  "scrollCollapse": true,
  "scrollY": false,
  "lengthChange": true,
  "searching": true,
  "ordering": true,
  "info": true,
  "autoWidth": true,
  "responsive": true,
  "ajax": {
    url: `${window.origin}/crud/categories-fetch`,
    type: "POST",
    dataSrc: function (json) {
      // Retrieve the row count from the JSON response
      var rowCount = json.recordsTotal;
      $('#items_count').html(rowCount);
      // Return the data for DataTables to display
      return json.data;
  },
    error: function() {
        $("#testEditable").append('<tbody class="category-grid-error"><tr><th colspan="3">No product category data found</th></tr></tbody>');
    }
  },
  "createdRow": function( row, data, dataIndex ) {
    $(row).attr('id', 'row-' + data.category_id);
  },
  "columns": [
    { "data": "id", "width": "10%"},
    { "data": "category_name", "width": "50%" , "searchable": true},
    { "data": "category_status", "width": "40%", "sortable": false },
    {
        "data": null,
        "width": "40%",
        "sortable": false,
        "render": function (data, type, row, meta) {
            return '<button id="' + row.id + '" data_id="' + row.id + '" class="btn btn-danger btn-sm active deleteCategory" role="button" aria-pressed="true"><i class="fa fa-trash"></i>&ensp;Delete</button>';
        }
    }
  ],
});

category_table.columns().every(function () {
  var table = this;
  $('input', this.header()).on('keyup change', function () {
    if (table.search() !== this.value) {
      table.search(this.value).draw();
    }
  });
});