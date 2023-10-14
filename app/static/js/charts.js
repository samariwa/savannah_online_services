$('.analyticsTab').on('click', function(){
  $('.analyticsTab').removeClass('selected');
  $('.tab-pane fade').removeClass('show active');
  $(this).addClass('selected');
  $('.tab-pane fade').addClass('active');
  eval($(this).attr('id')+"_requests()");
});

// EXPENDITURE ///////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
// Daily Expenditure ////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////

async function daily_expenditure_requests() {
  const expenditure_response = await fetch('/crud/daily-expenditure-analytics-fetch');
  const expenditure_data = await expenditure_response.json();

  daily_expenditure_categories_amount_comparison(expenditure_data['expenditure_categories_amount']);
}

function daily_expenditure_categories_amount_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('daily_expenditure_categories_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Amount Spent',
            data: values,
            borderWidth: 1
          }]
        },
        options: {
            indexAxis: 'y',
            elements: {
                bar: {
                  borderWidth: 1,
                }
              },
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Daily Expenditure Categories/Amount(Ksh.) Comparison'
                }
              }
        }
      });
}

///////////////////////////////////////////////////////////////////////////////////////////
// Weekly Expenditure ////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////

async function weekly_expenditure_requests() {
  const expenditure_response = await fetch('/crud/weekly-expenditure-analytics-fetch');
  const expenditure_data = await expenditure_response.json();

  weekly_expenditure_categories_amount_comparison(expenditure_data['expenditure_categories_amount']);
}

function weekly_expenditure_categories_amount_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('weekly_expenditure_categories_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Amount Spent',
            data: values,
            borderWidth: 1
          }]
        },
        options: {
            indexAxis: 'y',
            elements: {
                bar: {
                  borderWidth: 1,
                }
              },
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Weekly Expenditure Categories/Amount(Ksh.) Comparison'
                }
              }
        }
      });
}

///////////////////////////////////////////////////////////////////////////////////////////
// Bi-weekly Expenditure ////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////

async function biweekly_expenditure_requests() {
  const expenditure_response = await fetch('/crud/biweekly-expenditure-analytics-fetch');
  const expenditure_data = await expenditure_response.json();

  biweekly_expenditure_categories_amount_comparison(expenditure_data['expenditure_categories_amount']);
}

function biweekly_expenditure_categories_amount_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('biweekly_expenditure_categories_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Amount Spent',
            data: values,
            borderWidth: 1
          }]
        },
        options: {
            indexAxis: 'y',
            elements: {
                bar: {
                  borderWidth: 1,
                }
              },
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Bi-weekly Expenditure Categories/Amount(Ksh.) Comparison'
                }
              }
        }
      });
}

///////////////////////////////////////////////////////////////////////////////////////////
// Monthly Expenditure ////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////

async function monthly_expenditure_requests() {
  const expenditure_response = await fetch('/crud/monthly-expenditure-analytics-fetch');
  const expenditure_data = await expenditure_response.json();
  monthly_expenditure_categories_amount_comparison(expenditure_data['expenditure_categories_amount']);
  monthly_expenditure_details_amount_comparison(expenditure_data['expenditure_details_amount']);
}



function monthly_expenditure_categories_amount_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('monthly_expenditure_categories_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Amount Spent',
            data: values,
            borderWidth: 1
          }]
        },
        options: {
            indexAxis: 'y',
            elements: {
                bar: {
                  borderWidth: 1,
                }
              },
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Monthly Expenditure Categories/Amount(Ksh.) Comparison'
                }
              }
        }
      });
}


function monthly_expenditure_details_amount_comparison(data)
{
    var dataset = [];
    for (var key in data['data']){
      for (var value in data['data'][key]){
      dataset.push({
        label: value +' - '+ key,
        stack: key,
        type: "bar",
        data: data['data'][key][value], 
        borderWidth: 1});
    }
  }

    new Chart('monthly_expenditure_details_chart',{
        type: 'bar',
        data: {
          labels: data['periods'],
          datasets: dataset
        },
        options: {
          scales: {
            x: {
              stacked: true,
            },
            y: {
              stacked: true
            }
          },
            elements: {
                bar: {
                  borderWidth: 1,
                }
              },
            responsive: true,
            interaction: {
              intersect: false,
            },
            plugins: {
                legend: {
                  display: false
                },
                title: {
                  display: true,
                  text: 'Monthly Expenditure Categories/Details/Amount(Ksh.) Comparison'
                }
              }
        }
      });
}

///////////////////////////////////////////////////////////////////////////////////////////
// Quaterly Expenditure ////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////

async function quaterly_expenditure_requests() {
  const expenditure_response = await fetch('/crud/quaterly-expenditure-analytics-fetch');
  const expenditure_data = await expenditure_response.json();

  quaterly_expenditure_categories_amount_comparison(expenditure_data['expenditure_categories_amount']);
}

function quaterly_expenditure_categories_amount_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('quaterly_expenditure_categories_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Amount Spent',
            data: values,
            borderWidth: 1
          }]
        },
        options: {
            indexAxis: 'y',
            elements: {
                bar: {
                  borderWidth: 1,
                }
              },
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Quaterly Expenditure Categories/Amount(Ksh.) Comparison'
                }
              }
        }
      });
}

///////////////////////////////////////////////////////////////////////////////////////////
// Trimesterly Expenditure ////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////

async function trimesterly_expenditure_requests() {
  const expenditure_response = await fetch('/crud/trimesterly-expenditure-analytics-fetch');
  const expenditure_data = await expenditure_response.json();

  trimesterly_expenditure_categories_amount_comparison(expenditure_data['expenditure_categories_amount']);
}

function trimesterly_expenditure_categories_amount_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('trimesterly_expenditure_categories_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Amount Spent',
            data: values,
            borderWidth: 1
          }]
        },
        options: {
            indexAxis: 'y',
            elements: {
                bar: {
                  borderWidth: 1,
                }
              },
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Trimesterly Expenditure Categories/Amount(Ksh.) Comparison'
                }
              }
        }
      });
}

///////////////////////////////////////////////////////////////////////////////////////////
// Half Yearly Expenditure ////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////

async function half_yearly_expenditure_requests() {
  const expenditure_response = await fetch('/crud/half-yearly-expenditure-analytics-fetch');
  const expenditure_data = await expenditure_response.json();

  half_yearly_expenditure_categories_amount_comparison(expenditure_data['expenditure_categories_amount']);
}

function half_yearly_expenditure_categories_amount_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('half_yearly_expenditure_categories_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Amount Spent',
            data: values,
            borderWidth: 1
          }]
        },
        options: {
            indexAxis: 'y',
            elements: {
                bar: {
                  borderWidth: 1,
                }
              },
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Half-Yearly Expenditure Categories/Amount(Ksh.) Comparison'
                }
              }
        }
      });
}

///////////////////////////////////////////////////////////////////////////////////////////
// Yearly Expenditure ////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////

async function yearly_expenditure_requests() {
  const expenditure_response = await fetch('/crud/yearly-expenditure-analytics-fetch');
  const expenditure_data = await expenditure_response.json();
  yearly_expenditure_categories_amount_comparison(expenditure_data['expenditure_categories_amount']);
}

function yearly_expenditure_categories_amount_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('yearly_expenditure_categories_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Amount Spent',
            data: values,
            borderWidth: 1
          }]
        },
        options: {
            indexAxis: 'y',
            elements: {
                bar: {
                  borderWidth: 1,
                }
              },
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Yearly Expenditure Categories/Amount(Ksh.) Comparison'
                }
              }
        }
      });
}

// SALES /////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
// Daily Sales /////////////////////////////////////////////////////////////////////////
async function daily_sales_requests() {
  const sales_response = await fetch('/crud/daily-sales-analytics-fetch');
  const sales_data = await sales_response.json();
  daily_sales_values_comparison(sales_data['sales_value']);
}

function daily_sales_values_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('daily_sales_values_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Sales Value',
            data: values,
            borderWidth: 2,
            borderRadius: 5,
            borderSkipped: false,
          }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Daily Sales Value(Ksh.) Comparison'
                }
              }
        }
      });
}
// Weekly Sales /////////////////////////////////////////////////////////////////////////
async function weekly_sales_requests() {
  const sales_response = await fetch('/crud/weekly-sales-analytics-fetch');
  const sales_data = await sales_response.json();
  weekly_sales_values_comparison(sales_data['sales_value']);
}

function weekly_sales_values_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('weekly_sales_values_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Sales Value',
            data: values,
            borderWidth: 2,
            borderRadius: 5,
            borderSkipped: false,
          }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Weekly Sales Value(Ksh.) Comparison'
                }
              }
        }
      });
}
// Bi-weekly Sales ///////////////////////////////////////////////////////////////////////
async function biweekly_sales_requests() {
  const sales_response = await fetch('/crud/biweekly-sales-analytics-fetch');
  const sales_data = await sales_response.json();
  biweekly_sales_values_comparison(sales_data['sales_value']);
}

function biweekly_sales_values_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('biweekly_sales_values_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Sales Value',
            data: values,
            borderWidth: 2,
            borderRadius: 5,
            borderSkipped: false,
          }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Bi-weekly Sales Value(Ksh.) Comparison'
                }
              }
        }
      });
}
// Monthly Sales ////////////////////////////////////////////////////////////////////////
async function monthly_sales_requests() {
  const sales_response = await fetch('/crud/monthly-sales-analytics-fetch');
  const sales_data = await sales_response.json();
  monthly_sales_values_comparison(sales_data['sales_value']);
}

function monthly_sales_values_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('monthly_sales_values_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Sales Value',
            data: values,
            borderWidth: 2,
            borderRadius: 5,
            borderSkipped: false,
          }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Monthly Sales Value(Ksh.) Comparison'
                }
              }
        }
      });
}
// Quaterly Sales ////////////////////////////////////////////////////////////////////////
async function quaterly_sales_requests() {
  const sales_response = await fetch('/crud/quaterly-sales-analytics-fetch');
  const sales_data = await sales_response.json();
  quaterly_sales_values_comparison(sales_data['sales_value']);
}

function quaterly_sales_values_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('quaterly_sales_values_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Sales Value',
            data: values,
            borderWidth: 2,
            borderRadius: 5,
            borderSkipped: false,
          }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Quaterly Sales Value(Ksh.) Comparison'
                }
              }
        }
      });
}
// Trimesterly Sales ////////////////////////////////////////////////////////////////////////
async function trimesterly_sales_requests() {
  const sales_response = await fetch('/crud/trimesterly-sales-analytics-fetch');
  const sales_data = await sales_response.json();
  trimesterly_sales_values_comparison(sales_data['sales_value']);
}

function trimesterly_sales_values_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('trimesterly_sales_values_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Sales Value',
            data: values,
            borderWidth: 2,
            borderRadius: 5,
            borderSkipped: false,
          }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Trimesterly Sales Value(Ksh.) Comparison'
                }
              }
        }
      });
}
// Half-yearly Sales /////////////////////////////////////////////////////////////////////
async function half_yearly_sales_requests() {
  const sales_response = await fetch('/crud/half-yearly-sales-analytics-fetch');
  const sales_data = await sales_response.json();
  half_yearly_sales_values_comparison(sales_data['sales_value']);
}

function half_yearly_sales_values_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('half_yearly_sales_values_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Sales Value',
            data: values,
            borderWidth: 2,
            borderRadius: 5,
            borderSkipped: false,
          }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Half-Yearly Sales Value(Ksh.) Comparison'
                }
              }
        }
      });
}
// Yearly Sales //////////////////////////////////////////////////////////////////////////
async function yearly_sales_requests() {
  const sales_response = await fetch('/crud/yearly-sales-analytics-fetch');
  const sales_data = await sales_response.json();
  yearly_sales_values_comparison(sales_data['sales_value']);
}

function yearly_sales_values_comparison(data)
{
    var labels = [];
    var values = [];
    for (var key in data){
      labels.push(key);
      values.push(data[key] );
    }
    new Chart('yearly_sales_values_chart',{
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Sales Value',
            data: values,
            borderWidth: 2,
            borderRadius: 5,
            borderSkipped: false,
          }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                  position: 'top',
                },
                title: {
                  display: true,
                  text: 'Yearly Sales Value(Ksh.) Comparison'
                }
              }
        }
      });
}

// CUSTOMERS /////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
// Daily Customers /////////////////////////////////////////////////////////////////////////
async function daily_customers_requests() {
  const customers_response = await fetch('/crud/daily-customer-analytics-fetch');
  const customers_data = await customers_response.json();
  daily_customers_values(customers_data['registered_customers_number']);
}

function daily_customers_values(data)
{
  $(`#total_registered_customers_daily`).html(data);
}
// Weekly Customers /////////////////////////////////////////////////////////////////////////
async function weekly_customers_requests() {
  const customers_response = await fetch('/crud/weekly-customer-analytics-fetch');
  const customers_data = await customers_response.json();
  weekly_customers_values(customers_data['registered_customers_number']);
}

function weekly_customers_values(data)
{
  $(`#total_registered_customers_weekly`).html(data);
}
// Bi-weekly Customers ///////////////////////////////////////////////////////////////////////
async function biweekly_customers_requests() {
  const customers_response = await fetch('/crud/biweekly-customer-analytics-fetch');
  const customers_data = await customers_response.json();
  biweekly_customers_values(customers_data['registered_customers_number']);
}

function biweekly_customers_values(data)
{
  $(`#total_registered_customers_biweekly`).html(data);
}
// Monthly Customers ////////////////////////////////////////////////////////////////////////
async function monthly_customers_requests() {
  const customers_response = await fetch('/crud/monthly-customer-analytics-fetch');
  const customers_data = await customers_response.json();
  monthly_customers_values(customers_data['registered_customers_number']);
}

function monthly_customers_values(data)
{
  $(`#total_registered_customers_monthly`).html(data);
}
// Quaterly Customers ////////////////////////////////////////////////////////////////////////
async function quaterly_customers_requests() {
  const customers_response = await fetch('/crud/quaterly-customer-analytics-fetch');
  const customers_data = await customers_response.json();
  quaterly_customers_values(customers_data['registered_customers_number']);
}

function quaterly_customers_values(data)
{
  $(`#total_registered_customers_quaterly`).html(data);
}
// Trimesterly Customers ////////////////////////////////////////////////////////////////////////
async function trimesterly_customers_requests() {
  const customers_response = await fetch('/crud/trimesterly-customer-analytics-fetch');
  const customers_data = await customers_response.json();
  trimesterly_customers_values(customers_data['registered_customers_number']);
}

function trimesterly_customers_values(data)
{
  $(`#total_registered_customers_trimesterly`).html(data);
}
// Half-yearly Customers /////////////////////////////////////////////////////////////////////
async function half_yearly_customers_requests() {
  const customers_response = await fetch('/crud/half-yearly-customer-analytics-fetch');
  const customers_data = await customers_response.json();
  half_yearly_customers_values(customers_data['registered_customers_number']);
}

function half_yearly_customers_values(data)
{
  $(`#total_registered_customers_half_yearly`).html(data);
}
// Yearly Customers //////////////////////////////////////////////////////////////////////////
async function yearly_customers_requests() {
  const customers_response = await fetch('/crud/yearly-customer-analytics-fetch');
  const customers_data = await customers_response.json();
  yearly_customers_values(customers_data['registered_customers_number']);
}

function yearly_customers_values(data)
{
  $(`#total_registered_customers_yearly`).html(data);
}

// STOCK /////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
// Daily Stock /////////////////////////////////////////////////////////////////////////
$('#daily_product_movement_search').keyup(function () {
  /**
   * Function that listens for input on the product movement search field
   * The value keyed 'product' is sent to the server for processing
   */
  if ($(`#daily_product_movement_search`).val() != '') {
    // If the field for product to fetch is not blank
    var product_field = document.getElementById("daily_product_movement_search");
    fetch_product_movement_records(product_field.value, 
                                   product_field.name, 
                                   '#daily_product_movement_table_section');
  }
  else {
    $('#daily_product_movement_table_section').html('');
    return;
  }
});
// Weekly Stock /////////////////////////////////////////////////////////////////////////
$('#weekly_product_movement_search').keyup(function () {
  /**
   * Function that listens for input on the product movement search field
   * The value keyed 'product' is sent to the server for processing
   */
  if ($(`#weekly_product_movement_search`).val() != '') {
    // If the field for product to fetch is not blank
    var product_field = document.getElementById("weekly_product_movement_search");
    fetch_product_movement_records(product_field.value, 
                                   product_field.name, 
                                   '#weekly_product_movement_table_section');
  }
  else {
    $('#weekly_product_movement_table_section').html('');
    return;
  }
});
// Biweekly Stock /////////////////////////////////////////////////////////////////////////
$('#biweekly_product_movement_search').keyup(function () {
  /**
   * Function that listens for input on the product movement search field
   * The value keyed 'product' is sent to the server for processing
   */
  if ($(`#biweekly_product_movement_search`).val() != '') {
    // If the field for product to fetch is not blank
    var product_field = document.getElementById("biweekly_product_movement_search");
    fetch_product_movement_records(product_field.value, 
                                   product_field.name, 
                                   '#biweekly_product_movement_table_section');
  }
  else {
    $('#biweekly_product_movement_table_section').html('');
    return;
  }
});
// Monthly Stock /////////////////////////////////////////////////////////////////////////
$('#monthly_product_movement_search').keyup(function () {
  /**
   * Function that listens for input on the product movement search field
   * The value keyed 'product' is sent to the server for processing
   */
  if ($(`#monthly_product_movement_search`).val() != '') {
    // If the field for product to fetch is not blank
    var product_field = document.getElementById("monthly_product_movement_search");
    fetch_product_movement_records(product_field.value, 
                                   product_field.name, 
                                   '#monthly_product_movement_table_section');
  }
  else {
    $('#monthly_product_movement_table_section').html('');
    return;
  }
});
// Quaterly Stock /////////////////////////////////////////////////////////////////////////
$('#quaterly_product_movement_search').keyup(function () {
  /**
   * Function that listens for input on the product movement search field
   * The value keyed 'product' is sent to the server for processing
   */
  if ($(`#quaterly_product_movement_search`).val() != '') {
    // If the field for product to fetch is not blank
    var product_field = document.getElementById("quaterly_product_movement_search");
    fetch_product_movement_records(product_field.value, 
                                   product_field.name, 
                                   '#quaterly_product_movement_table_section');
  }
  else {
    $('#quaterly_product_movement_table_section').html('');
    return;
  }
});
// Trimesterly Stock /////////////////////////////////////////////////////////////////////////
$('#trimesterly_product_movement_search').keyup(function () {
  /**
   * Function that listens for input on the product movement search field
   * The value keyed 'product' is sent to the server for processing
   */
  if ($(`#trimesterly_product_movement_search`).val() != '') {
    // If the field for product to fetch is not blank
    var product_field = document.getElementById("trimesterly_product_movement_search");
    fetch_product_movement_records(product_field.value, 
                                   product_field.name, 
                                   '#trimesterly_product_movement_table_section');
  }
  else {
    $('#trimesterly_product_movement_table_section').html('');
    return;
  }
});
// Half yearly Stock /////////////////////////////////////////////////////////////////////////
$('#half_yearly_product_movement_search').keyup(function () {
  /**
   * Function that listens for input on the product movement search field
   * The value keyed 'product' is sent to the server for processing
   */
  if ($(`#half_yearly_product_movement_search`).val() != '') {
    // If the field for product to fetch is not blank
    var product_field = document.getElementById("half_yearly_product_movement_search");
    fetch_product_movement_records(product_field.value, 
                                   product_field.name, 
                                   '#half_yearly_product_movement_table_section');
  }
  else {
    $('#half_yearly_product_movement_table_section').html('');
    return;
  }
});
// Yearly Stock /////////////////////////////////////////////////////////////////////////
$('#yearly_product_movement_search').keyup(function () {
  /**
   * Function that listens for input on the product movement search field
   * The value keyed 'product' is sent to the server for processing
   */
  if ($(`#yearly_product_movement_search`).val() != '') {
    // If the field for product to fetch is not blank
    var product_field = document.getElementById("yearly_product_movement_search");
    fetch_product_movement_records(product_field.value, 
                                   product_field.name, 
                                   '#yearly_product_movement_table_section');
  }
  else {
    $('#yearly_product_movement_table_section').html('');
    return;
  }
});

function fetch_product_movement_records(product, period, display_section_id)
{
  /**
     * Function that sends an product movement fetch request to the server 
     * for processing
     * The product and period of to fetch are passed in as arguments
     * The values are used to create a JSON which will used to make the request
     */
  var values = {'product_name' : product,
                   'period': period};
  $('#dynamic-section').html('<div style="margin-left:470px; margin-top:180px; margin-bottom:180px;width: 3rem; height: 3rem;" class="spinner-border spinner-border-lg text-success"</div>');
  fetch(`${window.origin}` + '/crud/product-movement-fetch-ui', {
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
      $(`${display_section_id}`).html(data);
    })
  });
}