$(function () {
  if (document.getElementById('newCustomer')) {
    $('#newCustomer').blur();
  }
});

var barcode = '';
var interval;
document.addEventListener('keydown', function (evt) {
  if (interval) {
    clearInterval(interval);
  }
  if (evt.code == 'Enter') {
    if (barcode) {
      handleBarcode(barcode);
    }
    barcode = '';
    return;
  }
  if (evt.key != 'Shift') {
    barcode += evt.key;
  }
  interval = setInterval(() => barcode = '', 20);
});

function handleBarcode(scanned_barcode) {
  let str;
  barcode_parts = extract_barcode_parts(scanned_barcode);
  //generate checksum
  cartArray(barcode_parts['product_id'], barcode_parts['quantity'], mode = 'auto');
}

function generate_barcode(product_id, quantity) {
  let barcode = "21";
  let padded_product_id = pad_with_zeros(product_id, 5);
  let padded_quantity = pad_with_zeros(quantity, 5);

  barcode += padded_product_id + padded_quantity;
  let checksum = calculate_checksum(barcode);

  return barcode + checksum;
}

function extract_barcode_parts(barcode) {
  let product_id = barcode.substring(2, 7);
  let quantity = barcode.substring(7, 12);
  return {
    product_id: parseInt(product_id),
    quantity: parseInt(quantity) / 1000
  };
}

function validate_checksum(barcode) {
  let calculated_checksum = calculate_checksum(barcode.substring(0, 12));
  let barcode_checksum = barcode[12];

  return calculated_checksum === barcode_checksum;
}

function calculate_checksum(barcode) {
  let checksum = 0;
  for (let i = 0; i < 12; i++) {
    let digit = parseInt(barcode[i]);
    if (i % 2 === 0) {
      checksum += digit * 3;
    } else {
      checksum += digit;
    }
  }

  checksum = 10 - (checksum % 10);

  if (checksum === 10) {
    return "0";
  } else {
    return checksum.toString();
  }
}

function pad_with_zeros(number, length) {
  let str = number.toString();
  while (str.length < length) {
    str = "0" + str;
  }
  return str;
}

function activate_credit_order_button() {
  /**
   * This function makes the credit order button clickable based
   * on requirements
   */
  var button = document.getElementById("creditOrderButton");
  // ensure that the customer has been selected
  if ($('input[name=selectedCustomer]:checked').length > 0) {
    // ensure that the type of order has been selected
    if ($('input[name=order_type]:checked').length > 0) {
      if (cartItems.length > 0) {
        //there are items in the cart
        if (credit_customer == true) {
          // that is a credit customer
          button.style.pointerEvents = "auto";
        }
        else {
          // that is not a credit customer
          button.style.pointerEvents = "none";
        }
      }
      else {
        // there ae not items in the cart
        button.style.pointerEvents = "none";
      }
    }
  }
}

var complete_order_now = false;
function complete_now_unchecker() {
  complete_order_now = false;
}
$("#completeOrderNowBtn").on("click", function () {
  complete_order_now = true;
})

function payment_fields_validation() {
  // initialize the complete order now button
  var completeOrderAndPrint = ''
  if ($('#completeOrder').length > 0) {
    completeOrderAndPrint = document.getElementById('completeOrder');
  }
  else if ($('#delivery_transaction_btn').length > 0) {
    completeOrderAndPrint = document.getElementById('delivery_transaction_btn');
  }
  // if the payment mode that has been selected is cash ...
  if (document.getElementById('cash').checked == true) {
    // ensure that the amount paid has been entered
    if ($("#amount_paid").val() !== '') {
      // enable the complete order button
      completeOrderAndPrint.disabled = false;
    }
    else {
      // disable the complete order button
      completeOrderAndPrint.disabled = true;
    }
  }
  // if the transaction is mpesa or hybrid
  else if (document.getElementById('hybrid').checked == true || document.getElementById('mpesa').checked == true) {
    // if the transaction is hybrid
    if (document.getElementById('hybrid').checked == true) {
      // if mpesa payment has been attributed to the order and the cash paid in the transaction is keyed in ...
      if (Object.keys(TransactionAttributeDict).length > 0 && $("#amount_paid").val() !== '') {
        // enable the complete order button
        completeOrderAndPrint.disabled = false;
      }
      // if amount paid in cash is keyed in and verify later option is selected
      else if (verify_later == true && $("#amount_paid").val() !== '') {
        // enable the complete order button
        completeOrderAndPrint.disabled = false;
      }
      // if amount paid in cash is removed
      else {
        // disable the complete order button
        completeOrderAndPrint.disabled = true;
      }
    }
    // if transaction is made in mpesa
    else if (document.getElementById('mpesa').checked == true) {
      // if mpesa payment has been attributed to the order
      if (Object.keys(TransactionAttributeDict).length > 0) {
        // enable the complete order button
        completeOrderAndPrint.disabled = false;
      }
      // if the verify later option is selected
      else if (verify_later == true) {
        // enable the complete order button
        completeOrderAndPrint.disabled = false;
      }
    }
  }
  // if the payment mode that has been selected is customer account ...
  else if (document.getElementById('customer_account').checked == true) {
    // if the use customer account balance option is selected
    if (use_customer_account_balance == true) {
      // enable the complete order button
      completeOrderAndPrint.disabled = false;
    }
  }
}

function enable_complete_order() {
  /**
  * This function disables the complete order button if some of the fields
  * are not entered.
  */
  // initialize buttons for complete not and complete on credit
  var completeOrderAndPrint = document.getElementById('completeOrder');
  var completeCreditOrder = document.getElementById('completeCreditDeliveryOrder');
  // ensure that a customer has been selected
  if ($('input[name=selectedCustomer]:checked').length > 0) {
    // ensure that the type of order has been selected
    if ($('input[name=order_type]:checked').length > 0) {
      // ensure that items have been added to cart
      if (cartItems.length > 0) {
        // check if order is finished on non-credit terms
        if (complete_order_now == true) {
          // if this is a walk in customer
          if ($('input[name="order_type"]:checked').val() == 'walk in') {
            // If payment mode has been selected
            if ($('input[name=payment-mode]:checked').length > 0) {
              // call function to validate payment fields
              payment_fields_validation();
            }
          }
          // if this is a delivery customer
          else {
            // If payment mode is selected
            if ($('input[name=payment-mode]:checked').length > 0 && $('input[name="payment_on_delivery"]:checked').val() !== 'on') {
              // if delivery staff and location are keyed in
              if (($("#deliverer").val() != null) && ($("#delivery-location").val() !== '')) {
                // call function to validate payment fields
                payment_fields_validation()
              }
              // if delivery location is removed
              else {
                // disable the complete order button
                completeOrderAndPrint.disabled = true;
              }
            }
            // If payment on delivery is selected
            else if ($('input[name="payment_on_delivery"]:checked').val() == 'on') {
              // if delivery staff and location are keyed in
              if (($("#deliverer").val() != null) && ($("#delivery-location").val() !== '')) {
                // enable the complete order button
                completeOrderAndPrint.disabled = false;
              }
              // if delivery location is removed
              else {
                // disable the complete order button
                completeOrderAndPrint.disabled = true;
              }
            }
            // If payment on delivery is unchecked
            else {
              // disable the complete order button
              completeOrderAndPrint.disabled = true;
            }
          }
        }
        // otherwise order is being finished on credit terms
        else {
          // Delivery staff and location have been fielded
          if (($("#credit-deliverer").val() != null) && ($("#credit-delivery-location").val() !== '')) {
            // enable the complete order button
            completeCreditOrder.disabled = false;
          }
          // if the delivery location is removed
          else {
            // disable the complete order button
            completeCreditOrder.disabled = true;
          }
        }
      }
      // if the cart is emptied
      else {
        // disable buttons to complete order
        completeOrderAndPrint.disabled = true;
        completeCreditOrder.disabled = true;
      }
    }
  }
}


/*$("input[id='amount_paid']").keyup(function () {
  if (($('input:radio[name="payment-mode"]').is(':checked'))) {
    completeOrderAndPrint.disabled = false;
  }
});*/
/**
 * The variable below is a bool that will be used as one of the 
 * conditions for enabling the order complete on credit button
 */
var credit_customer = false;
function enable_disable_credit_button(selection) {
  /**
   * This function enables of disables the order
   * 'complete on credit button' based on conditions
   * 1) If the customer is selected for credit completion
   * 2) If the customers has a debt of less than Ksh. 2000
   */
  var id = $(selection).val();
  if ($(`#credit_customer${id}`).val() == 1 && $(`#customer_debt${id}`).val() < 2000) {
    // Show the complete on credit button
    $(`.placeOrderCredit`).show();
    //set the credit customer bool to true
    credit_customer = true;
  }
  else {
    // hide the complete on credit button
    $(`.placeOrderCredit`).hide();
    //set the credit customer bool to false
    credit_customer = false;
  }
  /**
   * Activate the credit order button if the button is 
   * enabled and all fields have been filled in through 
   * this function
   */
  activate_credit_order_button();
}

$('input:radio[name="selectedCustomer"]').change(function () {
  /**
   * This function disables the customer name chackbox if 
   * a registered customer is selected
   */
  $("#newCustomer").attr('disabled', 'disabled');
  $("#newCustomer").val('');
  /** 
   * call the function to enables or disable the
   * complete on credit button based on conditions
   */
  enable_disable_credit_button(this);
});

$('input:radio[id="selectedUnregisteredCustomer"]').change(function () {
  /**
     * We enable the complete order button if an unregisterest customer is selected
     * and also enable the customer name field for someone to optionally enter the
     * customer name. By default the customer name is set as walk in.
     */
  $("#newCustomer").removeAttr("disabled");
  $("#newCustomer").val('Walk_In');
  $("#completeOrderNowBtn").disabled = false;
  $("#completeOrderLaterBtn").disabled = false;
  // The Summary of customer details is autofilled
  var name = $("#newCustomer").val();
  customerDetails = "";
  customerDetails += "<h5>Confirm Customer Details</h5>&emsp;&emsp;-";
  customerDetails += "&emsp;&emsp;Name: ";
  customerDetails += name;
  customerDetails += "<br>&emsp;&emsp;&emsp;&emsp;&ensp;Location: ";
  customerDetails += 'N/A';
  customerDetails += "<br>&emsp;&emsp;&emsp;&emsp;&ensp;Contact: ";
  customerDetails += 'N/A';
  if ($('#customerDetails').html('')) {
    $("#customerDetails").append(customerDetails);
  }
  // Set delivery location as N/A in the order delivery section
  $("#delivery-location").val("N/A");
  $("#credit-delivery-location").val("N/A");
  newCustomer = $(`#newCustomer`).val();
});

var newCustomer = '';
$("#newCustomer").on("keyup", function () {
  /**
   * The Summary of customer details is autofilled if the customer naem field
   * is filled
   */
  var name = $("#newCustomer").val();
  customerDetails = "";
  customerDetails += "<h5>Confirm Customer Details</h5>&emsp;&emsp;-";
  customerDetails += "&emsp;&emsp;Name: ";
  customerDetails += name;
  customerDetails += "<br>&emsp;&emsp;&emsp;&emsp;&ensp;Location: ";
  customerDetails += 'N/A';
  customerDetails += "<br>&emsp;&emsp;&emsp;&emsp;&ensp;Contact: ";
  customerDetails += 'N/A';
  if ($('#customerDetails').html('')) {
    $("#customerDetails").append(customerDetails);
  }
  newCustomer = $(`#newCustomer`).val();
  $(`#orderCustomerName`).val(name);
})

/**
 * initialize customer account balance.
 * This balance will be used when the customer
 * account balance will be selected as the payment
 * method
 */
var customer_account_balance = null

// Creating an array that will be used to store the customer values
var customerArr = new Array();
function selectCustomer(selection) {
  var id = selection.value;
  var name = '';
  var location = '';
  var number = '';
  while (customerArr.length > 0) {
    customerArr.pop();
  }
  customerArr.push(id);
  if (id == 'N/A') {
    name = $(`#newCustomer${id}`).val();
    location = 'N/A';
    number = 'N/A';
    deliverer = 'N/A';
    newCustomer = $(`#newCustomer`).val();
    customer_account_balance = 0;
  }
  else {
    newCustomer = 'N/A';
    name = $(`#customerName${id}`).text();
    location = $(`#customerLocation${id}`).text();
    number = $(`#customerNumber${id}`).text();
    customer_account_balance = parseInt($(`#customerAccountBalance${id}`).text())
  }
  customerArr.push(location);
  $("#completeOrderNowBtn").disabled = false;
  $("#completeOrderLaterBtn").disabled = false;
  $("#delivery-location").val(location);
  $("#credit-delivery-location").val(location);
  customerDetails = "";
  customerDetails += "<h5>Confirm Customer Details</h5>&emsp;&emsp;-";
  customerDetails += "&emsp;&emsp;Name: ";
  customerDetails += name;
  customerDetails += "<br>&emsp;&emsp;&emsp;&emsp;&ensp;Location: ";
  customerDetails += location;
  customerDetails += "<br>&emsp;&emsp;&emsp;&emsp;&ensp;Contact: ";
  customerDetails += number;
  if ($('#customerDetails').html('')) {
    $("#customerDetails").append(customerDetails);
    $(`#orderCustomerName`).val(name);
    // Set delivery location in the order delivery section
    $(`#delivery-location`).val(location);
    $("#credit-delivery-location").val(location);
  }
}


// Adding to cart
// The array below will be used to store cart details as products are added
var cartItems = new Array();
function cartArray(Id, qty, mode = 'manual') {
  var id = Id;
  /**
   * All the values partaining to the product added to the cart 
   * are fetched (from the products table in that page) and stored 
   * in variables ready for use.
  */
  var productId = '';
  var productName = '';
  var productPrice = '';
  var available = '';
  var discount = '';
  if (mode == 'manual') {
    productId = $(`#id${id}`).text();
    productName = $(`#name${id}`).text();
    productPrice = parseFloat($(`#sp${id}`).text());
    available = parseFloat($(`#qty${id}`).text());
    discount = parseFloat($(`#Discount${id}`).text());
    /**
     * When the product is added, the cart button should be disabled
     * to prevent double entrying
    */
    var button = document.getElementById(`add_product${id}`);
    button.disabled = true;
  }
  else if (mode == 'auto') {
    productId = $(`#scanned_id${id}`).val();
    productName = $(`#scanned_name${id}`).val();
    productPrice = parseFloat($(`#scanned_sp${id}`).val());
    available = parseFloat($(`#scanned_qty${id}`).val());
    discount = parseFloat($(`#scanned_Discount${id}`).val());
  }
  var quantity = parseFloat(qty).toFixed(2);
  // check if the quantity entered is in stock
  if (quantity > available) {
    alert('Quantity Not Available');
    return;
  }
  /**
   * If item already in cart and is scanned again, just 
   * increase the qty by the amount decoded from the barcode
   */
  for (var i = 0; i < cartItems.length; i++) {
    if (cartItems[i][0] == productId) {
      upQuantity(productId, quantity);
      return;
    }
  }
  // The added item's details are then pushed to the cart items array
  cartItems.push([productId, productName, productPrice, quantity, discount, available]);
  //enable the complete order button if this is the last item to be added
  enable_complete_order();
  // activate the order credit complete button
  activate_credit_order_button();
  // populateCart function which is responsible for showing the cart items in the UI is called
  populateCart();
};

function populateCart() {
  /**
   * ProductDetails variable is for storing the HTMl of the cart table 
   * rows which will be appended to the existing cart table
  */
  productDetails = "";
  var initial = parseInt($('#cartTotal').html());
  /** 
   * Loop through the cart items array to construct each
   * row with the product details
  */
  for (var i = 0; i < cartItems.length; i++) {
    var id = cartItems[i][0];
    var price = cartItems[i][2];
    var name = cartItems[i][1];
    var qty = cartItems[i][3];
    var discount = cartItems[i][4];
    var cost = price - discount;
    var subTotal = cost * qty;
    var Total = +initial + +subTotal;
    $('#cartTotal').html(Total);
    productDetails += `<tr style="text-align: center;">
             <td class="uneditable">${id}</td>
              <td class="uneditable">${name}</td>
               <td class="uneditable" id="price${id}">${price}</td>
                <td class="editable" id="quantity${id}">${parseFloat(qty).toFixed(2)}</td>
                <td class="editable" id="discount${id}">${discount}</td>
                 <td> <button class="btn">
                 <i id="upQuantity${id}" onclick="upQuantity(${id},${1})" class='fa fa-plus'></i>
                 </button>
                 <button class="btn">
                 <i id="downQuantity${id}" onclick="downQuantity(${id},${price},${qty})" class='fa fa-minus'></i>
                 </button>
                 <button id="deleteCart${id}" onclick="deleteCart(${id},this,${price},${qty});" type='button' class='btn btn-danger btn-sm deleteFromCart' >
                 <i class='fa fa-times-circle'></i>&ensp;Remove</button>
                 </td>
                <td class="editable" id="subTotal${id}">${parseFloat(subTotal).toFixed(2)}</td>
                   </tr>`;
    // Append the cart details row to the cart table
    $('#cartData').html(productDetails);
    // Should be able to detect changes made directly in the cart table value
    $('#cartEditable').editableTableWidget();
    $('#cartEditable td.uneditable').on('change', function (evt, newValue) {
      return false;
    });
    $('#cartEditable td').on('change', function (evt, newValue) {
      /**
       * Loop through the table and check if a value in any row has been changed
       * This is because this cart table is a dynamic table with no fixed ID
       * attributes therefore identifying the changed row can only be done through
       * the loop, before updating the corresponding cart product in the cart array
       */
      for (var i = 0; i < cartItems.length; i++) {
        var availableQty = cartItems[i][5];
        // A case where the quantity value is changed
        if (parseFloat($(`#quantity${cartItems[i][0]}`).html()) == newValue) {
          /**
           * The new quantity cannot be:
           * 1) Greater that the available quantity
           * 2) Less than 1
           */
          if (parseFloat(newValue) <= availableQty && parseFloat(newValue) > 0) {
            var id = cartItems[i][0];
            var price = parseFloat($(`#price${id}`).html());
            var discount = parseFloat($(`#discount${id}`).html());
            // Calculate the Unit cost of the item given the discount
            var cost = price - discount;
            // Calculate the subtotal using the obtained unit cost and quantity
            newSub = newValue * cost;
            // Update the quantity value in the cart array
            cartItems[i][3] = newValue;
            // update the subtotal in the UI (to 2 decimal places)
            $(`#subTotal${id}`).html(parseFloat(newSub).toFixed(2));
          }
          /**
           * Throw warning errors if value of quantity is less than 
           * one or greater than the quantity available
           */
          else if (parseFloat(newValue) <= availableQty && parseFloat(newValue) == 0) {
            alert('Quantity cannot be 0');
            return false;
          }
          else {
            alert('Quantity Not Available');
            return false;
          }
        }
        // Case where the discount value is changed
        if (parseFloat($(`#discount${cartItems[i][0]}`).html()) == newValue) {
          /**
           * Ensure the discount is not greater than the unit price
           * NB: The discount of products is done per unit price
           */
          if (newValue <= parseFloat($(`#price${cartItems[i][0]}`).html())) {
            // Get new cost after the discount
            var cost = parseFloat($(`#price${cartItems[i][0]}`).html()) - parseFloat(newValue);
            // Get the new subtotal based on the new cost and quantity of the item in the cart
            newSub2 = parseFloat($(`#quantity${cartItems[i][0]}`).html()) * parseFloat(cost);
            // Update the cat items array with the new discount
            cartItems[i][4] = newValue;
            // Update the subtotal section of the UI with the new subtotal to 2 decimal places
            $(`#subTotal${cartItems[i][0]}`).html(parseFloat(newSub2).toFixed(2));
            // If discount is greater that the unit plrice throw a warning error
          } else {
            alert('Discount cannot be greater than unit price.');
            return false;
          }
        }
        /**
         * If the subtotal is changed, we will do a reverse 
         * (Quantity equivalent to that subtotal will be calculated)
         */
        if (parseFloat($(`#subTotal${cartItems[i][0]}`).html()) == newValue) {
          var id = cartItems[i][0];
          var price = parseFloat($(`#price${id}`).html());
          var discount = parseFloat($(`#discount${id}`).html());
          var cost = price - discount;
          var availableQty = cartItems[i][5];
          // Calculate the corresponding quantity based on the subtotal key in
          var qty = parseFloat(newValue) / parseFloat(cost);
          // Ensure that the quantity is available and is not less than 1
          if (parseFloat(qty) <= availableQty && parseFloat(qty) > 0) {
            $(`#quantity${id}`).html(parseFloat(qty).toFixed(2));
            cartItems[i][3] = qty;
          }
          // Otherwise throw the corresponding error warnings
          else if (parseFloat(qty) <= availableQty && parseFloat(newValue) == 0) {
            alert('Quantity cannot be 0');
            return false;
          }
          else {
            alert('Quantity Not Available');
            return false;
          }
        }
      }
      /**
       * After all the modifications, the total of the cart
       * is calculated using the function below
       */
      calculateTotal();
    });
  }
}

function calculateTotal() {
  /**
   * This function takes the cart items array and calculates 
   * the total using the subtotals stored in the array.
   * The total is then updated on the UI of the cart table
   */
  var total = 0;
  for (var i = 0; i < cartItems.length; i++) {
    total += parseFloat($(`#subTotal${cartItems[i][0]}`).html());
  }
  $(`#cartTotal`).html(Math.round(total).toFixed(2));
}

function upQuantity(product_id, qty) {
  /**
   * This function increases the cart quantity by 
   * one each time the the '+' icon is clicked.
   * The id is passed in since it will be the identifier
   * of the cart item to be updated.
   * The loop below will be used to check for the specific
   * cart row
   */
  for (var i = 0; i < cartItems.length; i++) {
    // Check that the increament won't surpass the available quantity
    if (cartItems[i][0] == product_id) {
      currentQ = cartItems[i][3];
      newQ = parseFloat(currentQ) + qty;
      if (newQ <= cartItems[i][5]) {
        cartItems[i][3] = newQ;
      } else {
        alert('Quantity Not Available');
      }

    }
  }
  // Update the cart UI and calculate the total after the updates are made
  populateCart();
  calculateTotal();
}
function downQuantity(a, b, c) {
  /**
  * This function decreases the cart quantity by 
  * one each time the the '-' icon is clicked.
  * The id is passed in since it will be the identifier
  * of the cart item to be updated.
  * The loop below will be used to check for the specific
  * cart row
  */
  for (var i = 0; i < cartItems.length; i++) {
    // Check that the decreament wont go below 1
    if (cartItems[i][0] == a) {
      currentQ = cartItems[i][3];
      if (currentQ > 1) {
        newQ = parseFloat(currentQ) - 1;
        cartItems[i][3] = newQ;
      } else {
        alert('Quantity cannot be below 1');
      }
    }
  }
  // Update the cart UI and calculate the total after the updates are made
  populateCart();
  calculateTotal();
}

function deleteCart(id, item, price, qty) {
  /**
   * This function updates the cart when an item is removed from the cart.
   * id: The id of the cart item
   * item: The identifier of the element to be removed from the UI
   * price: The proce of the item beling removed
   */
  var el = item;
  var Total = '';
  // The user should first confirm if the item should be removed
  bootbox.confirm('Do you really want to remove the seleted item from the cart?', function (result) {
    if (result) {
      $(el).closest('tr').css('background', 'tomato');
      $(el).closest('tr').fadeOut(800, function () {
        $(this).remove();
      });
      /**
       * Upto here we have just removed the row from the UI.
       *  We now need to remove it from the array
       */
      for (var i = 0; i < cartItems.length; i++) {
        if (cartItems[i][0] == id) {
          var discount = cartItems[i][4];
          var quantity = cartItems[i][3];
          var subTotal = (price - discount) * quantity;
          var initial = $('#cartTotal').html();
          // Calculate the new total after removing the item from the cart
          Total = +initial - +subTotal;
          if (document.getElementById(`add_product${id}`)) {
            var button = document.getElementById(`add_product${id}`);
            /**
             * Now that the item has been removed from the cart, 
             * you should enable its 'Add to cart button again
             */
            button.disabled = false;
          }
          // Get the index of the product to be removed in the cart array
          var check = getIndexOfProduct(cartItems, id);
          // Removed the product from the cart array
          cartItems.splice(check, 1);
        }
      }
      // remove the complete order button if all items are removed from cart
      enable_complete_order();
      // deactivate the order credit complete button
      activate_credit_order_button();
      // Update the total section of the cart table UI after the operation is complete
      $(`#cartTotal`).html(Math.round(Total).toFixed(2));
    }
  });
}


function getIndexOfProduct(arr, k) {
  // This function gets the index of a product in the array given the product id
  for (var i = 0; i < arr.length; i++) {
    if (k == arr[i][0]) {
      return i;
    }
  }
}

$(document).on('click', '.placeOrder', function () {
  /**
   * This function autofills the date in date field if it is not filled 
   * and place order button is clicked.
   * It also displays the cart total in the place order modal
   */
  $(`#order_total_value`).html(Math.round(parseInt($('#cartTotal').html())).toFixed(2));
  setDeliveryDate();
});

function setDeliveryDate() {
  if ($(`#deliveryDate`).val() == '') {
    let today = new Date().toISOString().slice(0, 10);
    $(`#deliveryDate`).val(today);
  }
}

$(`#amount_paid`).keyup(function () {
  /**
   * This function calculates the balance when the paid amount is keyed in
   * in situations where payment is made in cash
   * Helps in quick customer service
   */
  if (isNaN(Math.round(parseInt($(`#amount_paid`).val())))) {
    $(`#paidBalance`).html('Balance: Ksh. 0.00')
  }
  else {
    $(`#paidBalance`).html('Balance: Ksh. ' + (Math.round(parseInt($(`#amount_paid`).val()) - parseInt($('#order_total_value').html()))).toFixed(2));
  }
});

function show_extra_fields() {
  /**
   * This function shows the amount paid field based on the mode of payment
   * selected by the user. This is because it is only relevant for the cash
   * payment option.
   */
  // The cash checkbox element is fetched
  var cash_checkbox = document.getElementById('cash');
  // The hybrid checkbox element is fetched
  var hybrid_checkbox = document.getElementById('hybrid');
  // The customer account checkbox element is fetched
  var customer_account_checkbox = document.getElementById('customer_account');
  // the mpesa checkbox element id fetched
  var mpesa_checkbox = document.getElementById('mpesa');
  // The div containing the amount paid field witb the balance value is fetched
  var cash_field = document.getElementById('cash_paid_val');
  // The div containing verify transation button is fetched
  var cashless_field = document.getElementById('verify_transaction');
  // The div containing stk push button is fetched
  var stk_push_button = document.getElementById('initiate_stk_push_prompt');
  // The div containing customer account section is fetched
  var customer_account_field = document.getElementById('customer_account_section');
  // If cash radio is selected
  if (cash_checkbox.checked == true) {
    // show cash field
    cash_field.style.display = 'block';
    // hide cashless field
    cashless_field.style.display = 'none';
    // hide stk push button
    stk_push_button.style.display = 'none';
    // hide customer account section
    customer_account_field.style.display = 'none';
  }
  else if (hybrid_checkbox.checked == true) {
    // show cash field
    cash_field.style.display = 'block';
    // show cashless field
    cashless_field.style.display = 'block';
    // show stk push button
    stk_push_button.style.display = 'block';
    // hide customer account section
    customer_account_field.style.display = 'none';
  }
  else if (mpesa_checkbox.checked == true) {
    // hide cash field
    cash_field.style.display = 'none';
    // show cashless field
    cashless_field.style.display = 'block';
    // show stk push button
    stk_push_button.style.display = 'block';
    // hide customer account section
    customer_account_field.style.display = 'none';
  }
  else if (customer_account_checkbox.checked == true) {
    // show customer account section
    customer_account_field.style.display = 'block';
    // hide cash field
    cash_field.style.display = 'none';
    // hide stk push button
    stk_push_button.style.display = 'none';
    // hide cashless field
    cashless_field.style.display = 'none';
    /**
     * enable customer balance completion button based on 
     * whether the customer account balance is greater or
     * equal to the order cost. That is done using the 
     * enable_customer_account_payment() function
     */
    enable_customer_account_payment(parseInt(Math.round($(`#cartTotal`).html()).toFixed(2)));
  }
}

function show_order_details_extra_details() {
  customer_account_balance = parseInt($('#customer_account_balance').text());
  // The customer account checkbox element is fetched
  var customer_account_checkbox = document.getElementById('customer_account');
  // The div containing verify transation button is fetched
  var cashless_field = document.getElementById('verify_transaction');
  // The div containing stk push button is fetched
  var stk_push_button = document.getElementById('initiate_stk_push_prompt');
  // The div containing customer account section is fetched
  var customer_account_field = document.getElementById('customer_account_section');
  if (customer_account_checkbox.checked == true) {
    // show customer account section
    customer_account_field.style.display = 'block';
    // hide cashless field
    cashless_field.style.display = 'none';
    // hide stk push button
    stk_push_button.style.display = 'none';
    /**
     * enable customer balance completion button based on 
     * whether the customer account balance is greater or
     * equal to the order cost. That is done using the 
     * enable_customer_account_payment(amount) function
     */
    enable_customer_account_payment(parseInt(Math.round($(`#order_total_value`).html()).toFixed(2)));
  }
  else {
    // show cashless field
    cashless_field.style.display = 'block';
    // show stk push button
    stk_push_button.style.display = 'block';
    // hide customer account section
    customer_account_field.style.display = 'none';
  }
}


function enable_customer_account_payment(amount) {
  /**
   * This function is used in checking the validity
   * of using the customer account balance, doing the computation
   * for the new customer balance and displayng error messages where
   * necessary
   */
  // get the button for completing orders with the customer account balance
  var customer_account_btn = document.getElementById('customer_account_completion_btn');
  // get the element that displays the customer account details
  var customer_account_details = document.getElementById('customer_account_txn_details');
  // get the customer account option checkbox
  var customer_account_checkbox = document.getElementById('customer_account');
  if (isNaN(customer_account_balance)) {
    // an unregistered customer has been selected
    customer_account_btn.disabled = true;
    customer_account_details.style.display = 'none';
    if (customer_account_checkbox.checked == true) {
      $('#customer_account_completion_error').append(flashMessage('danger', 'Kindly <b>select a registered customer</b> to proceed.'));
    }
  }
  else if (customer_account_balance === null) {
    // no customer has been selected
    customer_account_btn.disabled = true;
    customer_account_details.style.display = 'none';
    $('#customer_account_completion_error').append(flashMessage('warning', 'Kindly <b>select a customer</b> to proceed.'));
  }
  else if (customer_account_balance < amount) {
    // The customer account balance is less than the order cost
    customer_account_btn.disabled = true;
    customer_account_details.style.display = 'block';
    $(`#current_customer_account_balance`).html(customer_account_balance);
    $(`#new_customer_account_balance`).html("0");
    if (customer_account_checkbox.checked == true) {
      $('#customer_account_completion_error').append(flashMessage('danger', '<b>Account balance not enough</b> to complete this order.'));
    }
  }
  else if (parseInt(Math.round($(`#cartTotal`).html()).toFixed(2)) == 0) {
    // The order cost is 0
    customer_account_btn.disabled = true;
    customer_account_details.style.display = 'block';
    $(`#current_customer_account_balance`).html("0");
    $(`#new_customer_account_balance`).html("0");
    if (customer_account_checkbox.checked == true) {
      $('#customer_account_completion_error').append(flashMessage('danger', '<b>The order cost is Ksh. 0.</b> Kindly add an item to the cart.'));
    }
  }
  else {
    // the account balance is enough to complete the transaction
    customer_account_btn.disabled = false;
    customer_account_details.style.display = 'block';
    var new_customer_balance = customer_account_balance - amount;
    $(`#current_customer_account_balance`).html(customer_account_balance);
    $(`#new_customer_account_balance`).html(new_customer_balance);
  }
}

let use_customer_account_balance = false;

function complete_with_customer_account_balance() {
  bootbox.confirm("Are you sure you want to complete using the customer account balance?", function (result) {
    if (result) {
      use_customer_account_balance = true;
      enable_complete_order();
      if (document.getElementById('add_transaction_btn')) {
        document.getElementById('add_transaction_btn').disabled = false;
      }
    }
  })
}

function disable_add_transaction_btn() {
  if (document.getElementById('add_transaction_btn')) {
    document.getElementById('add_transaction_btn').disabled = true;
  }
}

function show_delivery_section() {
  /**
   * This function unhides the delivery section in the case where 'walk_in delivery'
   * or 'phone call' order type is selected when creating an order
   */
  var credit_modal = document.querySelector('.placeOrderCredit');
  var delivery_section = document.getElementById('delivery-details');
  var walk_in = document.getElementById('walk_in');
  // If walk_in radio is selected
  if (walk_in.checked == true) {
    // hide delivery_section
    delivery_section.style.display = 'none';
    credit_modal.setAttribute("id", "completeOrderCreditBtn");
    credit_modal.removeAttribute("data-target");
  }
  else {
    // show delivery section
    delivery_section.style.display = 'block';
    credit_modal.setAttribute("data-target", "#completeOrderCredit");
    credit_modal.removeAttribute("id");
  }
}

let verify_later = false;

$(document).on('click', '#completeOrder', function (e) {
  /**
   * Function called when the complete order button
   * (after every detail has been added) is clicked
   */
  e.preventDefault();
  e.stopPropagation();
  /**
   * Create a dictionary that will carry all the details of the order
   * at once (order, order_details, transaction details, delivey details)
   * for sending to the server as a JSON for processing
   */
  var order_request = {};
  // get the total cost of the order
  var order_cost = parseInt(Math.round($(`#cartTotal`).html()).toFixed(2));
  // calculate the tax based on the order cosy
  var tax_payable = 0.16 * order_cost;
  // set initial total discount to 0
  var total_discount = 0;
  // Create a 2D array that will carry arrays of order details
  var order_details = [];
  for (var i = 0; i < cartItems.length; i++) {
    /**
     * This for loop calculates the total discount of the order based on the
     * individual discounts of each order item. This is done by incrementing
     * the total discount in each iteration
     * It also pushes order details from the cart array to the order details
     * array which will be part of the order JSON sent to the server
     */
    total_discount += parseInt(cartItems[i][4]);
    order_details.push({
      'product_id': cartItems[i][0],
      'quantity': cartItems[i][3],
      'discount': cartItems[i][4],
      'order_detail_status': 'unchanged'
    })
  }
  // By default set order status to fulfilled
  var order_status = 'fulfilled';
  if (document.getElementById('walk_in').checked == false) {
    /**
     * If the order is for delivery, set the order 
     * status to processing. 
     * It will be set to fulfilled once it is delivered
     */
    order_status = 'processing'
  }
  // Add order details to the order request dictionary
  order_request['order'] = {
    'customer_id': customerArr[0],
    'order_cost': order_cost,
    'tax_payable': Math.round(tax_payable).toFixed(2),
    'order_type': $('input[name="order_type"]:checked').val(),
    'total_discount': total_discount,
    'order_status': order_status,
    'order_date': $(`#deliveryDate`).val()
  };
  // Add the order_details array to the order_request dictionary
  order_request['order_details'] = order_details;
  if ($('input[name="payment_on_delivery"]:checked').val() == 'on') {
    complete_order_payment_on_delivery(order_request, order_cost);
  }
  else if (verify_later == true) {
    complete_order_verify_payment_later(order_request, order_cost);
  }
  else {
    complete_order(order_request, order_cost);
  }
});

function complete_order(order_request, order_cost) {
  /**
   * This function fully completes the order with all details in places
   * including a verified transaction
   */
  if ($('input[name="payment-mode"]:checked').val() == 'cash') {
    /**
     * If the payment was cash, and the amount paid field appeared, 
     * whatever is entered in the field will be set as the amount paid.
     * The transaction status will be 'successful' since it will have been 
     * completed.
     */
    // Transaction details are added to the order_request dictionary
    order_request['transaction_details'] = {
      'payment_method': 'cash',
      'amount_paid': order_cost,
      'transaction_code': 'N/A',
      'mobile_number': 'N/A',
      'payment_balance': 0,
      'payment_terms': 'before_delivery',
      'transaction_status': 'successful'
    };
  }
  else if ($('input[name="payment-mode"]:checked').val() == 'customer_account') {
    /**
     * If the payment was through the customer account balance, 
     * the order cost will be set as the amount paid.
     * The transaction status will be 'successful' since it will have been 
     * completed.
     */
    // Transaction details are added to the order_request dictionary
    order_request['transaction_details'] = {
      'payment_method': 'customer_account',
      'amount_paid': order_cost,
      'transaction_code': 'N/A',
      'mobile_number': 'N/A',
      'payment_balance': 0,
      'payment_terms': 'before_delivery',
      'transaction_status': 'successful'
    };
  }
  else if ($('input[name="payment-mode"]:checked').val() == 'hybrid') {
    /**
     * In a case where the transaction is hybrid, a JSON containing both modes
     * of payment and their corresponding details is created
     */
    // Payment balance will be calculate by differencing amount paid and order cost
    payment_balance = order_cost - parseInt($(`#amount_paid`).val());

    // Transaction details are added to the order_request dictionary
    order_request['transaction_details'] = {
      'hybrid': true,
      'cash_payment_details': {
        'payment_method': 'cash',
        'amount_paid': parseInt($(`#amount_paid`).val()),
        'transaction_code': 'N/A',
        'mobile_number': 'N/A',
        'payment_terms': 'before_delivery',
        'payment_balance': 0,
        'transaction_status': 'successful'
      },
      'mpesa_payment_details': {
        'payment_method': 'mpesa',
        'amount_paid': 0,
        'transaction_code': 'N/A',
        'mobile_number': 'N/A',
        'payment_terms': 'before_delivery',
        'payment_balance': payment_balance,
        'transaction_status': 'waiting',
        'mpesa_transaction_id': TransactionAttributeDict['transaction_id']
      }
    };
  }
  else {
    /**
     * A case where the transaction was made in mpesa, the details are fetched
     * set in a JSON for transmission to the server
     */

    // Transaction details are added to the order_request dictionary
    order_request['transaction_details'] = {
      'payment_method': 'mpesa',
      'amount_paid': 0,
      'transaction_code': 'N/A',
      'mobile_number': 'N/A',
      'payment_balance': order_cost,
      'payment_terms': 'before_delivery',
      'transaction_status': 'waiting',
      'mpesa_transaction_id': TransactionAttributeDict['transaction_id']
    };
  }
  // If a delivery order type is selected, include delivery details
  if (document.getElementById('walk_in').checked == false) {
    order_request['delivery_details'] = {
      'delivery_staff_id': $(`#deliverer`).val(),
      'delivery_stage': 'dispatch',
      'delivery_fee': 0,
      'delivery_location': $(`#delivery-location`).val(),
      'delivery_date': $(`#deliveryDate`).val(),
      'delivery_speed': 0
    };
  }
  process_order(order_request);
}

function complete_order_payment_on_delivery(order_request, order_cost) {
  /**
   * This function completes the order but with pending payment that will
   * be verified by the delivery for completion
   */
  // Transaction details are added to the order_request dictionary
  order_request['transaction_details'] = {
    'payment_method': 'none_yet',
    'amount_paid': 0,
    'transaction_code': 'N/A',
    'mobile_number': 'N/A',
    'payment_balance': order_cost,
    'payment_terms': 'on_delivery',
    'transaction_status': 'waiting'
  };
  // include delivery details
  order_request['delivery_details'] = {
    'delivery_staff_id': $(`#deliverer`).val(),
    'delivery_stage': 'dispatch',
    'delivery_fee': 0,
    'delivery_location': $(`#delivery-location`).val(),
    'delivery_date': $(`#deliveryDate`).val(),
    'delivery_speed': 0
  };
  process_order(order_request);
}

function complete_order_verify_payment_later(order_request, order_cost) {
  /**
   * This function is completes the order but with pending transaction
   * verification for any given reason. Transaction will be verified at
   * a later time
   */
  // Transaction details are added to the order_request dictionary
  if ($('input[name="payment-mode"]:checked').val() == 'mpesa') {
    // If it is purely mpesa
    order_request['transaction_details'] = {
      'payment_method': 'mpesa',
      'amount_paid': 0,
      'transaction_code': 'N/A',
      'mobile_number': 'N/A',
      'payment_balance': order_cost,
      'payment_terms': 'before_delivery',
      'transaction_status': 'waiting'
    };
  }
  else {
    // If it is a hybrid transaction
    // Payment balance will be calculate by differencing amount paid and order cost
    payment_balance = order_cost - parseInt($(`#amount_paid`).val());

    // Transaction details are added to the order_request dictionary
    order_request['transaction_details'] = {
      'hybrid': true,
      'cash_payment_details': {
        'payment_method': 'cash',
        'amount_paid': parseInt($(`#amount_paid`).val()),
        'transaction_code': 'N/A',
        'mobile_number': 'N/A',
        'payment_balance': 0,
        'payment_terms': 'before_delivery',
        'transaction_status': 'successful'
      },
      'mpesa_payment_details': {
        'payment_method': 'mpesa',
        'amount_paid': 0,
        'transaction_code': 'N/A',
        'mobile_number': 'N/A',
        'payment_balance': payment_balance,
        'payment_terms': 'before_delivery',
        'transaction_status': 'waiting'
      }
    };
  }

  // If a delivery order type is selected, include delivery details
  if (document.getElementById('walk_in').checked == false) {
    order_request['delivery_details'] = {
      'delivery_staff_id': $(`#deliverer`).val(),
      'delivery_stage': 'dispatch',
      'delivery_fee': 0,
      'delivery_location': $(`#delivery-location`).val(),
      'delivery_date': $(`#deliveryDate`).val(),
      'delivery_speed': 0
    };
  }
  process_order(order_request);
}

// Completing an Order
$(document).on('click', '#completeOrderCreditBtn', function () {
  /**
   * Create a dictionary that will carry all the details of the order
   * at once (order, order_details, transaction details, delivey details)
   * for sending to the server as a JSON for processing
   */
  var order_request = {};
  // get the total cost of the order
  var order_cost = parseInt(Math.round($(`#cartTotal`).html()).toFixed(2));
  // calculate the tax based on the order cost
  var tax_payable = 0.16 * order_cost;
  // set initial total discount to 0
  var total_discount = 0;
  // Create a 2D array that will carry arrays of order details
  var order_details = [];
  for (var i = 0; i < cartItems.length; i++) {
    /**
     * This for loop calculates the total discount of the order based on the
     * individual discounts of each order item. This is done by incrementing
     * the total discount in each iteration
     * It also pushes order details from the cart array to the order details
     * array which will be part of the order JSON sent to the server
     */
    total_discount += parseInt(cartItems[i][4]);
    order_details.push({
      'product_id': cartItems[i][0],
      'quantity': cartItems[i][3],
      'discount': cartItems[i][4],
      'order_detail_status': 'unchanged'
    })
  }
  // Add order details to the order request dictionary
  order_request['order'] = {
    'customer_id': customerArr[0],
    'order_cost': order_cost,
    'tax_payable': Math.round(tax_payable).toFixed(2),
    'order_type': $('input[name="order_type"]:checked').val(),
    'total_discount': total_discount,
    'order_status': 'fulfilled',
    'order_date': $(`#deliveryDate`).val()
  };
  // Add the order_details array to the order_request dictionary
  order_request['order_details'] = order_details;
  // Transaction details are added to the order_request dictionary
  order_request['transaction_details'] = {
    'payment_method': 'none_yet',
    'amount_paid': 0,
    'transaction_code': 'N/A',
    'mobile_number': '073489458',
    'payment_balance': order_cost,
    'payment_terms': 'credit',
    'transaction_status': 'waiting'
  };
  process_order(order_request);
});

$(document).on('click', '#completeCreditDeliveryOrder', function (e) {
  e.preventDefault();
  e.stopPropagation();
  /**
 * Create a dictionary that will carry all the details of the order
 * at once (order, order_details, transaction details, delivey details)
 * for sending to the server as a JSON for processing
 */
  var order_request = {};
  // get the total cost of the order
  var order_cost = parseInt(Math.round($(`#cartTotal`).html()).toFixed(2));
  // calculate the tax based on the order cost
  var tax_payable = 0.16 * order_cost;
  // set initial total discount to 0
  var total_discount = 0;
  // Create a 2D array that will carry arrays of order details
  var order_details = [];
  for (var i = 0; i < cartItems.length; i++) {
    /**
     * This for loop calculates the total discount of the order based on the
     * individual discounts of each order item. This is done by incrementing
     * the total discount in each iteration
     * It also pushes order details from the cart array to the order details
     * array which will be part of the order JSON sent to the server
     */
    total_discount += parseInt(cartItems[i][4]);
    order_details.push({
      'product_id': cartItems[i][0],
      'quantity': cartItems[i][3],
      'discount': cartItems[i][4],
      'order_detail_status': 'unchanged'
    })
  }
  // Add order details to the order request dictionary
  order_request['order'] = {
    'customer_id': customerArr[0],
    'order_cost': order_cost,
    'tax_payable': Math.round(tax_payable).toFixed(2),
    'order_type': $('input[name="order_type"]:checked').val(),
    'total_discount': total_discount,
    'order_status': 'processing',
    'order_date': $(`#deliveryDate`).val()
  };
  // Add the order_details array to the order_request dictionary
  order_request['order_details'] = order_details;
  // Transaction details are added to the order_request dictionary
  order_request['transaction_details'] = {
    'payment_method': 'none_yet',
    'amount_paid': 0,
    'transaction_code': 'N/A',
    'mobile_number': 'N/A',
    'payment_balance': order_cost,
    'payment_terms': 'credit',
    'transaction_status': 'waiting'
  };
  order_request['delivery_details'] = {
    'delivery_staff_id': $(`#credit-deliverer`).val(),
    'delivery_stage': 'dispatch',
    'delivery_fee': 0,
    'delivery_location': $(`#credit-delivery-location`).val(),
    'delivery_date': $(`#deliveryDate`).val(),
    'delivery_speed': 0
  };
  process_order(order_request);
});

function process_order(order_request) {
  // Order request dictionary is finally sent to the server for processing
  fetch(`${window.origin}/crud/orders-create`, {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(order_request),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  }).then(function (response) {
    // Create order details once order creation is done
    // *************************************
    // we should also change the UI
    // *************************************          
    if (response.status == 201) {
      alert('Order added successfully')
      location.reload(true);
      return;
    }
    // Else handle errors
    response.text().then(function (data) {
      // Any error
      $('#flash_message').append(flashMessage('danger', 'Something unexpected happened. Please try again.'));
    });
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

function sales_status(el, message, serverUrl, values, redirect_url) {
  bootbox.confirm(message, function (result) {
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
            window.location.href = redirect_url;
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
// Return functions for the cashier /////////////////////////////
function cancelOrder(el, id) {
  var values = {
    id: id
  };
  sales_status(el,
    'Do you really want to cancel the selected order?',
    '/crud/cancel-order',
    values,
    '/cashier/sales');
}

function returnOrderItem(el, id) {
  var values = {
    id: id
  };
  sales_status(el,
    'Do you really want to return the selected order item?',
    '/crud/return-order-item',
    values,
    window.location.href);
}

//////////////////////////////////////////////////////////////////
// Return functions for the delivery person //////////////////////
function deliveryCancelOrder(el, id) {
  var values = {
    id: id
  };
  sales_status(el,
    'Do you really want to cancel the selected order?',
    '/crud/cancel-order',
    values,
    '/delivery/my-orders');
}

function deliveryReturnOrderItem(el, id) {
  var values = {
    id: id
  };
  sales_status(el,
    'Do you really want to return the selected order item?',
    '/crud/return-order-item',
    values,
    window.location.href);
}
//////////////////////////////////////////////////////////////////
// Transactions functions ////////////////////////////////////////
function fetch_transactions() {
  /**
   * Does a generalized search of mpesa transactions that have not yet
   * been attributed and are of the amount expected to be paid
   */
  // Show loader while in progress
  show_transaction_loader();
  /**
   * initialize the payment amount variable that will be used to
   * store the amount expected to be paid on mpesa
   */
  var payment_amount = 0;
  if ($('#order_total_value').length > 0) {
    // fetch the order cost in the add orders page
    var order_cost = parseInt($(`#order_total_value`).html());
  }
  else if ($('#order_payment_balance').length > 0) {
    // fetch the payment balance in the order details page
    var order_cost = parseInt($(`#order_payment_balance`).html())
  }
  /**
   * Check if hybrid checkbox exists (if it exists operation is 
   * being done in the add order page or delivery transactions page 
   * else it is in the order details page)
   */
  if (document.getElementById('hybrid')) {
    // If hybrid radio is selected
    if (document.getElementById('hybrid').checked == true) {
      /**
       * If it is a hybrid payment method, the difference between the amount
       * entered as paid in cash and the order cost is set as the amount
       * expected in mpesa.
       */
      payment_amount = order_cost - parseInt($(`#amount_paid`).val());
    }
    else {
      /**
       * Otherwise if the mode of payment is mpesa, the total order
       * cost will be the amount expected to be paid
       */
      payment_amount = order_cost;
    }
  }
  else {
    /**
     * Otherwise if the mode of payment is mpesa, the total order
     * cost will be the amount expected to be paid
     */
    payment_amount = order_cost;
  }

  if (payment_amount < 1) {
    // If nothing is to be paid (order cost is 0), there is nothing to verify
    $('#transaction_flash').append(flashMessage('warning', 'Order cost is Ksh. 0. For a transaction, the order cost must be greater than Ksh. 0.'));
    $(`#transaction_results`).html('<div class="d-flex justify-content-center mt-5 mb-5"><h4>No Result</h4></div>');
  }
  else {
    /**
     * Pass in the expected payment amount that will be sent as a request
     * to the server as a JSON to search from unattributed payments of that
     * amount
     */
    var values = {
      'amount': payment_amount
    }
    fetch(`${window.origin}` + '/crud/check-mpesa/', {
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
        $('#transaction_flash').append(flashMessage('warning', 'We were unable to process your request. Please try again later.'));
        console.log(response.status);
        return;
      }
      response.text().then(function (data) {
        if (data == 'invalid') {
          /**
         * Invalid response means that the transaction has not been found
         * This could be because the customer has not paid or there is a
         * delay on Safaricom's end.
         * In this case output that the results are missing and since is a
         * general search using the payment amount expected, give the user
         * the option to use the adnvanced search where they will use IDs
         * for a unique search
        */
          var transaction_results = '';
          $('#transaction_flash').append(flashMessage('warning', 'Matching transaction not found. Try using the <b>advanced</b> search to fetch the transaction'));
          transaction_results += '<div class="d-flex justify-content-center mt-5 mb-5"><h4>No Result</h4></div>';
          transaction_results += '<br>';
          transaction_results += '<div class="d-flex justify-content-center"><button type="button" class="btn btn-success" onclick="fetch_transactions()"><i class="fa fa-refresh" aria-hidden="true"></i> Refresh</button></div>';
          $(`#transaction_results`).html(transaction_results);
        }
        else {
          /**
           * The response returns found results which are now appended on 
           * the UI for verification in tabular form together with the radio
           * button that is used to select the payment and a refresh button
           * to refresh the transaction fetch
           */
          data = JSON.parse(data)
          $('#transaction_flash').append('');
          var transaction_results = '';
          transaction_results += '<h5 class="ml-5">Matching Transaction Found</h5>';
          transaction_results += '<table cellspacing="0" cellpadding="0" style="text-align: center;">';
          transaction_results += '<thead style="border-bottom:0px;font-size:15px;">';
          transaction_results += '<tr>';
          transaction_results += '<th scope="col" width="5%">Select</th>';
          transaction_results += '<th scope="col" width="15%">Name</th>';
          transaction_results += '<th scope="col" width="35%">Mobile No.</th>';
          transaction_results += '<th scope="col" width="25%">Txn Code</th>';
          transaction_results += '<th scope="col" width="20%">Date/Time</th>';
          transaction_results += '</tr>';
          transaction_results += '</thead>';
          transaction_results += '<tbody style="border-bottom:0px;font-size:12px;">';
          transaction_results += '<tr>';
          transaction_results += '<td><input type="radio" id="selectedTransaction" onclick="selectTransaction(' + data['id'] + ',' + payment_amount + ');" name="selectedTransaction" value="fssdfdf"></td>';
          transaction_results += '<td>' + data['name'] + '</td>';
          transaction_results += '<td>' + data['phone'] + '</td>';
          transaction_results += '<td>' + data['code'] + '</td>';
          transaction_results += '<td>' + data['time'] + '</td>';
          transaction_results += '</tr>';
          transaction_results += '</tbody>';
          transaction_results += '</table>';
          transaction_results += '<br>';
          transaction_results += '<div class="d-flex justify-content-center"><button type="button" class="btn btn-success" onclick="fetch_transactions()"><i class="fa fa-refresh" aria-hidden="true"></i> Refresh</button></div>';
          $(`#transaction_results`).html(transaction_results);
        }
      })
    });
  }
  // Hide the loader and show the results
  show_transaction_results();
}

// Initialize a dictionary that will be used to store the mpesa payment id
var TransactionAttributeDict = {};
function selectTransaction(transaction_id) {
  // Get confirmation from user that they want to attribute that payment to the order
  bootbox.confirm('Are you sure you want to attribute the selected payment to this order?', function (result) {
    if (result) {
      /**
       * Store the mpesa payment id in the dictionary that will be transmitted
       * to the server for attribution to the order.
       * Enable the complete order button now that transaction has been verified
       * Close the modal after confirmation
       */
      TransactionAttributeDict['transaction_id'] = transaction_id;
      // set the verify later boolean to false
      verify_later = false;
      use_customer_account_balance = false;
      if ($('#completeOrder').length > 0) {
        enable_complete_order();
      }
      else if ($('#delivery_transaction_btn').length > 0) {
        payment_fields_validation();
      }
      if (document.getElementById('add_transaction_btn')) {
        document.getElementById('add_transaction_btn').disabled = false;
      }
      let closeCanvas = document.querySelector('[data-bs-dismiss="offcanvas"]');
      closeCanvas.click();
    }
  });
}

function show_transaction_loader() {
  // Shows the loader as transations are being fetched
  var loader = '';
  loader += '<div id="transaction_loader">';
  loader += '<div class="d-flex justify-content-center">';
  loader += '<div class="spinner-border text-success mt-5 mb-5" role="status">';
  loader += '<span class="sr-only">Loading...</span>';
  loader += '</div>';
  loader += '</div>';
  loader += '</div>';
  $(`#transaction_results`).html(loader);
}

function show_transaction_results() {
  // Hides the loader and shows the transaction results fetched from the database
  document.getElementById('transaction_results').style.display = 'block';
  document.getElementById('transaction_loader').style.display = 'none'
}

function fetch_transaction_using_id() {
  /**
   * Uses an identifier (phone number or transaction code) to fetch
   * unattributed mpesa transactions of that amount
   */
  // Show loader while in progress
  show_transaction_loader();
  /**
   * initialize the payment amount variable that will be used to
   * store the amount expected to be paid on mpesa
   */
  var payment_amount = 0;
  /**
    * Create a dictionary where the values of the transaction being searched
    * will be passed for purposes of sending the request to the server as a
    * JSON
    */
  var transaction_values = {};
  if ($(`#transaction_amount`).val() != '') {
    payment_amount = $(`#transaction_amount`).val();
    /**
     * Pass in the values of the transaction the dictionary that will be
     * send to the server as part of the request
     */
    transaction_values['amount'] = payment_amount;
    // If the other paramenters (mobile no. or transaction code) are given together with the amount
    if ($(`#mpesa_txn_id`).val() != '' && $(`#transaction_id_value`).val() != '') {
      transaction_values['detail_type'] = $(`#mpesa_txn_id`).val();
      transaction_values['detail'] = $(`#transaction_id_value`).val();
    }
  }
  else {
    if ($('#order_total_value').length > 0) {
      // fetch the order cost in the add orders page
      var order_cost = parseInt($(`#order_total_value`).html());
    }
    else if ($('#order_payment_balance').length > 0) {
      // fetch the payment balance in the order details page
      var order_cost = parseInt($(`#order_payment_balance`).html())
    }
    if (document.getElementById('hybrid')) {
      // If hybrid radio is selected
      if (document.getElementById('hybrid').checked == true) {
        /**
         * If it is a hybrid payment method, the difference between the amount
         * entered as paid in cash and the order cost is set as the amount
         * expected in mpesa.
         */
        payment_amount = order_cost - parseInt($(`#amount_paid`).val());
      }
      else {
        /**
         * Otherwise if the mode of payment is mpesa, the total order
         * cost will be the amount expected to be paid
         */
        payment_amount = order_cost;
      }
    }
    else {
      /**
       * Otherwise if the mode of payment is mpesa, the total order
       * cost will be the amount expected to be paid
       */
      payment_amount = order_cost;
    }

    /**
     * Pass in the values of the transaction the dictionary that will be
     * send to the server as part of the request
     */
    transaction_values['amount'] = payment_amount;
    transaction_values['detail_type'] = $(`#mpesa_txn_id`).val();
    transaction_values['detail'] = $(`#transaction_id_value`).val();
  }
  fetch(`${window.origin}` + '/crud/check-mpesa/', {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(transaction_values),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  }).then(function (response) {
    // First sort situation where response not 200
    if (response.status !== 200) {
      $('#transaction_flash').append(flashMessage('warning', 'We were unable to process your request. Please try again later.'));
      console.log(response.status);
      return;
    }
    response.text().then(function (data) {
      if (data == 'invalid') {
        /**
         * Invalid response means that the transaction has not been found
         * This could be because the customer has not paid or there is a
         * delay on Safaricom's end.
         * In this case output that the results are missing and since its a
         * unique search, give the user the option to either try again or do
         * the verification later
        */
        var transaction_results = '';
        $('#transaction_flash').append(flashMessage('warning', 'Matching transaction not found. Try again or <b>verify later</b>'));
        transaction_results += '<div class="d-flex justify-content-center mt-5 mb-5"><h4>No Result</h4></div>';
        transaction_results += '<br>';
        transaction_results += '<div class="d-flex justify-content-center"><button type="button" class="btn btn-success" onclick="fetch_transactions()"><i class="fa fa-refresh" aria-hidden="true"></i> Refresh</button></div>';
        $(`#transaction_results`).html(transaction_results);
      }
      else {
        /**
         * The response returns found results which are now appended on 
         * the UI for verification in tabular form together with the radio
         * button that is used to select the payment and a refresh button
         * to refresh the transaction fetch
         */
        data = JSON.parse(data)
        $('#transaction_flash').append('');
        var transaction_results = '';
        transaction_results += '<h5 class="ml-5">Matching Transaction Found</h5>';
        transaction_results += '<table cellspacing="0" cellpadding="0" style="text-align: center;">';
        transaction_results += '<thead style="border-bottom:0px;font-size:15px;">';
        transaction_results += '<tr>';
        transaction_results += '<th scope="col" width="5%">Select</th>';
        transaction_results += '<th scope="col" width="15%">Name</th>';
        transaction_results += '<th scope="col" width="35%">Mobile No.</th>';
        transaction_results += '<th scope="col" width="25%">Txn Code</th>';
        transaction_results += '<th scope="col" width="20%">Date/Time</th>';
        transaction_results += '</tr>';
        transaction_results += '</thead>';
        transaction_results += '<tbody style="border-bottom:0px;font-size:12px;">';
        transaction_results += '<tr>';
        transaction_results += '<td><input type="radio" id="selectedTransaction" onclick="selectTransaction(' + data['id'] + ',' + payment_amount + ');" name="selectedTransaction" value="fssdfdf"></td>';
        transaction_results += '<td>' + data['name'] + '</td>';
        transaction_results += '<td>' + data['phone'] + '</td>';
        transaction_results += '<td>' + data['code'] + '</td>';
        transaction_results += '<td>' + data['time'] + '</td>';
        transaction_results += '</tr>';
        transaction_results += '</tbody>';
        transaction_results += '</table>';
        transaction_results += '<br>';
        transaction_results += '<div class="d-flex justify-content-center"><button type="button" class="btn btn-success" onclick="fetch_transactions()"><i class="fa fa-refresh" aria-hidden="true"></i> Refresh</button></div>';
        $(`#transaction_results`).html(transaction_results);
      }
    })
  });
  // Hide the loader and show the results
  show_transaction_results();
}

function enable_transaction_search_btn() {
  /**
   * Enables the search button when both the ID type and ID value have been
   * keyed in to avoid erroneous requests
   */
  var button = document.getElementById('transaction_search_btn');
  if ($(`#transaction_id_value`).val() != '' && $(`#mpesa_txn_id`).val() != null) {
    // If ID type select option is not null and the ID value is not blank enable search
    button.disabled = false;
  }
  else if ($(`#transaction_amount`).val() != '') {
    button.disabled = false;
  }
  else {
    // Otherwise disable
    button.disabled = true;
  }
}

function verify_transaction_later() {
  verify_later = true;
  /**
   * check if we are on the cashier's add order page 
   * or the deliverer's add transaction page
   */
  if ($('#completeOrder').length > 0) {
    // cashier's add order page
    enable_complete_order();
  }
  else if ($('#delivery_transaction_btn').length > 0) {
    // deliverer's add transaction page
    payment_fields_validation();
  }
  let closeCanvas = document.querySelector('[data-bs-dismiss="offcanvas"]');
  closeCanvas.click();
}


$(document).on('click', '#show_transaction_filters', function (e) {
  // Shows the unique search section and hides the advanced search link
  document.getElementById('identifiers_fetch').style.display = 'block';
  document.getElementById('show_transaction_filters').style.display = 'none';
})

$(document).on('click', '#hide_transaction_filters', function (e) {
  // Hides the unique search section and shows the advanced search link
  document.getElementById('identifiers_fetch').style.display = 'none';
  document.getElementById('show_transaction_filters').style.display = 'block';
})

// VERIFY LATER & DELIVERY PAYMENT ATTRIBUTION ////////////////////////////////////////////////////////////////
function attribute_order_transaction() {
  if ($('input[name="payment-mode"]:checked').val() == 'cash') {
    values = {
      'order_id': $(`#order_id`).text(),
      'amount_paid': $("#amount_paid").val()
    }
    updateRequest('/crud/attribute-cash-transaction', values)
    alert("Payment attributed successfully")
    location.reload(true);
  }
  else if ($('input[name="payment-mode"]:checked').val() == 'mpesa') {
    if (verify_later == true) {
      delivery_verify_payment_later($(`#order_id`).text())
    }
    else {
      values = {
        'order_id': $(`#order_id`).text(),
        'transaction_id': TransactionAttributeDict['transaction_id']
      }
      updateRequest('/crud/attribute-transaction', values)
      alert("Payment attributed successfully")
      location.reload(true);
    }
  }
  else if ($('input[name="payment-mode"]:checked').val() == 'hybrid') {
    if (verify_later == true) {
      delivery_verify_payment_later($(`#order_id`).text(), cash_paid = $("#amount_paid").val())
    }
    else {
      values = {
        'order_id': $(`#order_id`).text(),
        'amount_paid': $("#amount_paid").val(),
        'transaction_id': TransactionAttributeDict['transaction_id']
      }
      updateRequest('/crud/attribute-hybrid-transaction', values)
      alert("Payment attributed successfully")
      location.reload(true);
    }
  }
  else if ($('input[name="payment-mode"]:checked').val() == 'customer_account') {
    values = {
      'order_id': $(`#order_id`).text(),
      'amount_paid': $("#order_payment_balance").text()
    }
    updateRequest('/crud/attribute-customer-account-transaction', values)
    alert("Payment attributed successfully")
    location.reload(true);
  }
}

function delivery_verify_payment_later(order_id, cash_paid = 0) {
  /**
   * This function handles cases where the delivery person chooses the verify
   * later option during the payment verification process
   */
  if (cash_paid == 0) {
    // This is an mpesa only payment
    values = {
      'order_id': order_id
    }
    updateRequest('/crud/verify-later-mpesa-transaction', values)
    alert("Payment verification should be done later")
    location.reload(true);
  }
  else {
    // This is a hybrid payment
    values = {
      'order_id': order_id,
      'amount_paid': cash_paid
    }
    updateRequest('/crud/verify-later-hybrid-transaction', values)
    alert("Cash payment has been attributed successfully. Mpesa payment should be verified later.")
    location.reload(true);
  }
}


$(document).on('click', '.complete_delivery', function (e) {
  e.preventDefault();
  var values = {
    'id': $(this).attr("id"),
    'order_status': 'fulfilled'
  }
  updateRequest('/crud/complete-delivery', values);
  window.location.href = '/delivery/my-orders';
})


$(document).on('click', '.verify_delivery', function (e) {
  e.preventDefault();
  var values = {
    'id': $(this).attr("id"),
  }
  updateRequest('/crud/verify-delivery', values);
  window.location.href = '/cashier/unverified-deliveries';
})

$('.forcePaymentAttribution').click(function (e) {
  e.preventDefault();
  var id = $(this).attr("id")
  var values = {
    'order_id': id,
    'transaction_code': $(`#transaction_code` + id).val(),
    'msisdn': $(`#msisdn` + id).val(),
    'amount': $(`#amount` + id).val(),
    'name': $(`#name` + id).val()
  }
  updateRequest('/crud/force-attribute', values, reload = true);
});
// ORDERS FILTER /////////////////////////////////////////////////////////////
$('#filter_orders').keyup(function () {
  /**
   * Function that listens for input on the customer/date filter field
   * The value keyed in is sent together with the time frame of the search
   * The search criteria is considered. If the search criteria is customer,
   * value for customer is used to search and if the search criteria is date,
   * the date keyed in is used for the search
   */
  var values = {}
  if ($(`#search_criteria`).val() == 'customer') {
    values.customer = $(`#filter_orders`).val();
    values.time_frame = $(`#time_frame`).val();
  }
  else if ($(`#search_criteria`).val() == 'date') {
    values.date = $(`#filter_orders`).val();
  }
  ordersFilter(values);
});

$(`#time_frame`).change(function () {
  values = {}
  if ($(`#filter_orders`).val() != '') {
    values.customer = $(`#filter_orders`).val();
    values.time_frame = $(`#time_frame`).val();
  }
  else {
    values.time_frame = $(`#time_frame`).val();
  }
  ordersFilter(values);
});

$(`#search_criteria`).change(function () {
  $(`#filter_orders`).val('');
  if ($(`#search_criteria`).val() == 'customer') {
    $('#filter_orders').attr('placeholder', 'Customer Name...');
    $(`#time_frame_selector`).show();
  }
  else if ($(`#search_criteria`).val() == 'date') {
    $('#filter_orders').attr('placeholder', 'Date... (yyyy-mm-dd)');
    $(`#time_frame_selector`).hide();
  }
});

function ordersFilter(values) {
  /**
   * Function that sends an order filter request to the server for processing
   */
  $('#dynamic-section').html('<div style="margin-left:470px; margin-top:180px; margin-bottom:180px;width: 3rem; height: 3rem;" class="spinner-border spinner-border-lg text-success"</div>');
  fetch(`${window.origin}` + '/crud/orders-fetch-ui', {
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
      $('#dynamic-section').html(data);
    })
  });
}

$('#stk_push_no').keyup(function () {
  /**
   * Function that enables/disables the stk push button based in input
   * If there is some input in the msisdn field, the button is enabled
   * otherwise, it is disabled
   */
  var stk_push_btn = document.getElementById('initiateStkPushBtn');
  if ($('#stk_push_no').val() != '') {
    // There is a value in the field therefore, enable the button
    stk_push_btn.disabled = false;
  }
  else {
    // There is no value in the field therefore disable the button
    stk_push_btn.disabled = true;
  }
});

function initiate_stk_push(staff_id) {
  bootbox.confirm('Do you really want to push the stk push to this customer?', function (result) {
    if (result) {
      var order_cost = 0;
      if ($('#order_total_value').length > 0) {
        // fetch the order cost in the add orders page
        order_cost = parseInt($(`#order_total_value`).html());
      }
      else if ($('#order_payment_balance').length > 0) {
        // fetch the payment balance in the order details page
        order_cost = parseInt($(`#order_payment_balance`).html());
      }
      var payment_amount = 0;
      /**
       * Check if hybrid checkbox exists (if it exists operation is 
       * being done in the add order page or delivery transactions 
       * page else it is in the order details page)
       */
      if (document.getElementById('hybrid')) {
        // If hybrid radio is selected
        if (document.getElementById('hybrid').checked == true) {
          /**
           * If it is a hybrid payment method, the difference between the amount
           * entered as paid in cash and the order cost is set as the amount
           * expected in mpesa.
           */
          payment_amount = order_cost - parseInt($(`#amount_paid`).val());
        }
        else {
          /**
           * Otherwise if the mode of payment is mpesa, the total order
           * cost will be the amount expected to be paid
           */
          payment_amount = order_cost;
        }
      }
      else {
        /**
         * Otherwise if the mode of payment is mpesa, the total order
         * cost will be the amount expected to be paid
         */
        payment_amount = order_cost;
      }
      // Reject the request if the amount to be paid is 0
      if (payment_amount == 0) {
        alert("Amount to be paid has to be greater than 0 for request to be sent");
        return;
      }
      // Change the phone number to the expected format
      var msisdn = $(`#stk_push_no`).val()
      if (msisdn.length > 9) {
        /**
         * Truncate to the last 9 digits (It removes the preceding 0 or the zip
         * code)
         * Required msisdn format ((7/1)XXXXXXXX)
         */
        msisdn = msisdn.substr($(`#stk_push_no`).val().length - 9)
      }
      else if (msisdn.length < 9)
      {
        alert("The mobile number you have entered is incorrect");
        return;
      }
      /**
       * Create the JSON to be sent with the request
       * The JSON request requires:
       * msisdn where the request will be sent
       * amount that the customer will be prompted to pay
       * staff_id of the initiator of the stk request
       */
      request_values = {
        'msisdn': '254'+parseInt(msisdn),
        'amount': payment_amount,
        'staff_id': staff_id
      }
      // stk push request dictionary is finally sent to the server for processing
      fetch(`${window.origin}/crud/stk-push`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(request_values),
        cache: "no-cache",
        headers: new Headers({
          "content-type": "application/json"
        })
      }).then(function (response) {
        // If STK push is successful        
        if (response.status == 200) {
          alert('Sim Tool Kit Request Sent Successfully')
          return;
        }
        // Else handle errors
        response.text().then(function (data) {
          // Any error
          $('#flash_message').append(flashMessage('danger', 'Something unexpected happened. Please try again.'));
        });
      });
    }
  });
}


$('#product_sales').keyup(function () {
  /**
   * Function that listens for input on the product filter field
   * The value keyed in is sent together with the time frame of the search
   */
  if ($(`#product_sales`).val() == '') {
    $('#product_sales_table_section').html('');
    return;
  }
  var values = {}
  values.product = $(`#product_sales`).val();
  values.time_frame = $(`#time_frame`).val();
  productSales(values);
});

$(`#time_frame`).change(function () {
  if ($(`#product_sales`).val() == '') {
    $('#product_sales_table_section').html('');
    return;
  }

  values = {}
  values.product = $(`#product_sales`).val();
  values.time_frame = $(`#time_frame`).val();
  productSales(values);
});

function productSales(values) {
  /**
   * Function that sends an order filter request to the server for processing
   */
  $('#product_sales_table_section').html('<div style="margin-left:470px; margin-top:180px; margin-bottom:180px;width: 3rem; height: 3rem;" class="spinner-border spinner-border-lg text-success"</div>');
  fetch(`${window.origin}` + '/crud/product-sales-fetch-ui', {
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
      $('#product_sales_table_section').html(data);
    })
  });
}