$(function () {
    "use strict";
    $(function () {
        $(".preloader").fadeOut();
    });


});

(function ($) {
    "use strict";
    // catagory-container swiper slider init
    var catagoryContainer = new Swiper('.catagory-container', {
        slidesPerView: 6,
        loop: true,
        navigation: {
            nextEl: '.catagory-slider-next',
            prevEl: '.catagory-slider-prev',
        },
        spaceBetween: 30,
        breakpoints: {
            990: {
                slidesPerView: 4
            },
            768: {
                slidesPerView: 2
            },
            540: {
                slidesPerView: 2
            },
            400: {
                slidesPerView: 2
            }
        }
    });


    // trending-product-container swiper slider init
    var trendingContainer = new Swiper('.trending-product-container', {
        slidesPerView: 4,
        loop: true,
        navigation: {
            nextEl: '.trending-slider-next',
            prevEl: '.trending-slider-prev',
        },
        spaceBetween: 30,
        breakpoints: {
            1200: {
                slidesPerView: 3
            },
            990: {
                slidesPerView: 3
            },
            768: {
                slidesPerView: 2
            },
            540: {
                slidesPerView: 1
            },
            400: {
                slidesPerView: 1
            }
        }
    });

    // trending-product-container swiper slider init
    var recommendContainer = new Swiper('.recommend-product-container', {
        slidesPerView: 4,
        loop: true,
        navigation: {
            nextEl: '.trending-slider-next',
            prevEl: '.trending-slider-prev',
        },
        spaceBetween: 30,
        breakpoints: {
            1200: {
                slidesPerView: 3
            },
            990: {
                slidesPerView: 3
            },
            768: {
                slidesPerView: 2
            },
            540: {
                slidesPerView: 1
            },
            400: {
                slidesPerView: 1
            }
        }
    });

    // brand-feature-product-container swiper slider init
    var recommendContainer = new Swiper('.feature-brand-container', {
        slidesPerView: 5,
        loop: true,
        navigation: {
            nextEl: '.brand-feature-slider-next',
            prevEl: '.brand-feature-slider-prev',
        },
        spaceBetween: 30,
        breakpoints: {
            1200: {
                slidesPerView: 4
            },
            990: {
                slidesPerView: 3
            },
            768: {
                slidesPerView: 2
            },
            540: {
                slidesPerView: 1
            },
            400: {
                slidesPerView: 1
            }
        }
    });

    // trending-product-container swiper slider init
    var testimonialContainer = new Swiper('.testimonial-container', {
        slidesPerView: 1,
        loop: true,
        navigation: {
            nextEl: '.testimonial-slider-next',
            prevEl: '.testimonial-slider-prev',
        },
        spaceBetween: 30,
    });

    // banner-slider-container swiper slider init
    var banneSliderConainer = new Swiper('.banner-slider-container', {
        slidesPerView: 1,
        loop: true,
        spaceBetween: 0,
        speed: 900,
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        }
    });

    // infoBoxContainer swiper slider init
    var infoBoxContainer = new Swiper('.info-box-container', {
        slidesPerView: 3,
        loop: true,
        centeredSlides: true,
        initialSlide: 2,
        spaceBetween: 30,
        autoplay: {
            delay: 3500,
            disableOnInteraction: false,
        },
        breakpoints: {
            990: {
                slidesPerView: 2
            },
            767: {
                slidesPerView: 1
            }
        }
    });


    $('.info-hover-effect-parent').on('mouseover', '.info-hover-effect-child', function () {
        $('.info-hover-effect-child.active').removeClass('active');
        $(this).addClass('active');
    });

    $('.product-slick').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav'
    });

    $('.slider-nav').slick({
        vertical: false,
        slidesToShow: 4,
        slidesToScroll: 1,
        centerMode: true,
        asNavFor: '.product-slick',
        arrows: true,
        dots: false,
        focusOnSelect: true
    });



    $('.add-product img').elevateZoom({
        zoomType: "inner",
        scrollZoom: true
    });

    // $('.cart-btn-toggle').on('click', function(){
    //     $(this).closest('.cart-btn-toggle').find('.cart-btn').hide()
    //     $(this).closest('.cart-btn-toggle').find('.price-btn').show()
    // })
    // $('.cart-btn').on('click', function(){
    //  $(this).parent('.cart-btn-toggle').find('.cart-btn').hide()
    //  $(this).parent('.cart-btn-toggle').find('.price-btn').show()
    // })
    $('.price-increase-decrese-group .quantity-right-plus').on('click', function () {
        var $qty = $(this).closest('.price-increase-decrese-group').find('.input-number');
        var currentVal = parseInt($qty.val(), 10);
        if (!isNaN(currentVal)) {
            $qty.val(currentVal + 1);
        }
    });
    $('.price-increase-decrese-group .quantity-left-minus').on('click', function () {
        var ths = $(this);
        var $qty = $(this).closest('.price-increase-decrese-group').find('.input-number');
        var currentVal = parseInt($qty.val(), 10);
        if (!isNaN(currentVal) && currentVal > 0) {
            $qty.val(currentVal - 1);
        }
        if (currentVal === 1) {
            console.log(ths);
            // ths.parents('.price-increase-decrese-group').css('background-color','red');
            ths.parents('.price-btn').hide();
            ths.parents('.price-btn').siblings('.cart-btn').show();
        }
    });


    var $qty = $(this).closest('.price-increase-decrese-group').find('.input-number');
    var currentVal = $qty.val();
    if (currentVal === 0) {
        // $(this).closest('.cart-btn-toggle').find('.cart-btn').show()
        $(this).closest('.cart-btn-toggle').find('.price-btn').hide()
    }

    $(".wish-link").on("click", function (e) {

        let id = $(this).attr("id");
        var entry = {
            prod_id: id,
            user_id: $(`#hidden_usr${id}`).val(),
        }
        fetch(`/add_to_wishlist`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(entry),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        }).then(function (response) {
            if (response.status !== 200) {
                // find a way to flush error msg
                console.log(response.status);
                return;
            }
            response.json().then(function (data) {
                if (data.status == 408) {
                    // find a way to flush error msg and exit
                    console.log(data.err);
                    return;
                }

                // a variable to keep track of whether we added or removed
                // so that we can update colors accordingly
                let action = 'added_to_wishlist';
    
    
                // cookies from cart update
                if (getCookie('wishlist') != '' && getCookie('wishlist').value != '{}') {
                    // it's not empty so we just append the item and change the total
                    // w_cookie is wishlist cookie
                    let w_cookie = getCookie('wishlist');
    
    
                    // due to the way it was made, check if it's JSON parsable (i.e we made it ourselves)
                    if (w_cookie['parse'] == true) {
                        // c_wishlist is the w_cookie converted to JSON list/dict
                        let c_wishlist = JSON.parse(w_cookie['value']);

                        
                        // if the product is in the wishlist already that's our
                        // queue to remove it from the wishlist
                        if (c_wishlist[entry['prod_id']] != {}) {
                            // remove from wishlist
                            delete c_wishlist[entry['prod_id']];
                            action = 'removed_from_wishlist';
                        } else {
                        // we create wishlist entry 
                        c_wishlist[entry['prod_id']] = entry;
                        }
                        // convert it back to JSON string
                        const serialized = JSON.stringify(c_wishlist);
                        setCookie('wishlist', serialized, 7);
                    } else {
                        // at this point, we know the cart is in a format which is not JSON parsable, so we reset things
                        setCookie('wishlist', "", 1);
                    }
    
                } else {
                    // we set the cookie since it's empty
                    let wishlist = {
                        [entry['prod_id']]: entry,
                    }
                    const serialized = JSON.stringify(wishlist);
                    setCookie('wishlist', serialized, 7);
                }
                // update color
    
                const heart_svg_id = "wishlist-heart" + id;
                if (action == 'added_to_wishlist') {
                    document.getElementById(heart_svg_id).style.fill = 'red';
                } else {
                    document.getElementById(heart_svg_id).style.fill = 'white';
                }
                
            })
    
        });

    });

    // $(".all-catagory-option > a").on("click",function(e){
    //     $('.page-layout').toggleClass('open-side-menu')
    //     $('body').toggleClass('open-side-menu')
    // });
    var contentwidth = jQuery(window).width();
    if ((contentwidth) > '1200') {
        $('.home-layout').addClass('open-side-menu')
    }
    if ((contentwidth) > '1200') {
        $('.sticky-sidebar-home').addClass('open-side-menu')
    }
    if ((contentwidth) < '991') {
        $('.widget .widget-wrapper').addClass('collapse')
    }

    if ((contentwidth) < '991') {
        $('.cart-btn-toggle').removeAttr('onclick');
    }


    $('.cart-product-item>.close-item').on('click', function () {
        $(this).parent('.cart-product-item').remove();
    })

    $('.wishlist-item>.close-item').on('click', function () {
        $(this).parent('.wishlist-item').remove();
    })


    // fixed menu app home page
    $(window).on("scroll", function () {
        var scroll = $(window).scrollTop();

        if (scroll >= 100) {
            $(".header-bottom,.mobile-header,.catagory-sidebar-area").addClass("fixed-totop animated slideInDown");
        } else {
            $(".header-bottom,.mobile-header,.catagory-sidebar-area").removeClass("fixed-totop  animated slideInDown");
        }
    });


    // fixed bottom to top
    $(window).on("scroll", function () {
        var scroll = $(window).scrollTop();

        if (scroll >= 500) {
            $(".to-top").addClass("fixed-totopmbb");
        } else {
            $(".to-top").removeClass("fixed-totopmbb");
        }
    });


    /*  //popup
      $('.popup-close,.popup-overlay').on("click", function(){
          $('#popup').hide();
      });*/
    $(document).ready(function () {
        if (!localStorage.getItem("cookieBannerDisplayed")) {
            $("#popup").delay(2000).fadeIn();
        }
    });

    if ($(window).width() > 990) {
        $(document).ready(function () {
            $('.sidebar')
                .theiaStickySidebar({
                    additionalMarginTop: 110
                });
        });
    }

    $(document).on('click', ".cookie-btn ", function () {
        $('#popup').hide();
        localStorage.setItem("cookieBannerDisplayed", "true");
    });

    $(document).on('click', ".cookie-exit ", function () {
        deleteAllCookies();
        $('#popup').hide();
    });

    function deleteAllCookies() {
        var cookies = document.cookie.split(";");

        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            var eqPos = cookie.indexOf("=");
            var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
            document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
        }
    }

    $(function () {
        setNavigation();
    });

    function setNavigation() {
        var pathArray = window.location.pathname.split('/');
        var lastItem = pathArray.pop();
        $(".menu a").each(function () {
            var href = $(this).attr('href');
            if (lastItem.substring(0, href.length) === href) {
                var myLi = $(this).closest('li');
                myLi.addClass('active');
                myLi.parent().parent().addClass('active');
            }
        });
    }






})(jQuery);



function cartopen() {
    //alert("Hi")
    document.getElementById("sitebar-cart").classList.add('open-cart');
    document.getElementById("sitebar-drawar").classList.add('hide-drawer');

    //reload
    $('#sitebar-cart').load(document.URL + ' #sitebar-cart>*')
    $('#sitebar-cart').load(document.URL + ' #sitebar-cart>*')
}

function cartclose() {
    document.getElementById("sitebar-cart").classList.remove('open-cart');
    document.getElementById("sitebar-drawar").classList.remove('hide-drawer');
}

// open modal
function openModal() {
    document.getElementById("product-details-popup").classList.add('open-side');
}

$(document).on('click', '.modalOpen', function () {
    var el = $(this);
    var id = el.attr("id");

    // $('#hidden_id').text()

    //  $('#hidden_unit').text()
    // $('#hidden_discount').text()
    $('#modal-product-name').text($(`#hidden_name${id}`).val());
    $('#modal-product-category').text($(`#itemCategory${id}`).text());
    $('#modal-product-price').text($(`#hidden_price${id}`).val());
    $('#modal-product-image').append('<img src="images/products/' + $(`#hidden_image${id}`).val() + ' alt="product"></img>');
});

function closeModal() {
    document.getElementById("product-details-popup").classList.remove('open-side');
}

// open signup form
function OpenSignUpForm() {
    document.getElementById("login-area").classList.add('open-form');
}

function CloseSignUpForm() {
    document.getElementById("login-area").classList.remove('open-form');
}



// jQuery(function($){
//     $(document).ajaxSend(function() {
//         $("#overlay").fadeIn(300);　
//     });

//     $('#edit').click(function(){
//         $.ajax({
//             type: 'GET',
//             success: function(){
//                 $("#load-data").load("components/edit-profile.html", function(responseTxt, statusTxt, xhr){
//                     if(statusTxt == "success")
//                       alert("External content loaded successfully!");
//                     if(statusTxt == "error")
//                       alert("Error: " + xhr.status + ": " + xhr.statusText);
//                   });
//             }
//         }).done(function() {
//             setTimeout(function(){
//                 $("#overlay").fadeOut(300);
//             },500);
//         });
//     });	
// });


$(document).ready(function () {

    $("input[type='radio']").click(function () {
        var sim = $("input[type='radio']:checked").val();
        //alert(sim);
        if (sim < 3) { $('.myratings').css('color', 'red'); $(".myratings").text(sim); }
        else { $('.myratings').css('color', 'green'); $(".myratings").text(sim); }
    });
});


/*$(document).on('click','.userSubscription',function(){
    var email = $('.userSubscription').val();
    var registered = 1;
    var values = {
        email: email,
        registered: registered
    };
    fetch(`${window.origin}/subscribe`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(values),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
    .then(function(response) {
        if (response.status !== 200)
        {
            console.log(`Error: $(response.status)`);
        }
        else
        {
            response.json().then(function(data){
                console.log(data)
            })
        }
    })     
});*/

function subscribe_anon() {
    var email = "Samuel";

    var entry = {
        email: email
    };
    fetch(`${window.origin}/subscribe`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
}

$(document).on('click', '.anonymousSubscription', function () {
    var email = $('#anonymousEmail').val();
    var token = $('.newsletter_token').val();
    var where = 'newsletter'
    alert(email)
    $.post("add.php", { email: email, token: token, where: where },
        function (result) {
            if (result == 'success') {
                alert('Thank you. Your newsletter subsription was successful!');
                location.reload(true);
            }
            else if (result == 'exists') {
                alert('You are already subscribed for our newsletter.');
            }
            else {
                alert("Something went wrong. Please try again later.");
            }
        });
});


function subscribe_anon() {
    var email = document.getElementById("anonymousEmail");

    var entry = {
        email: email.value
    };

    fetch(`/subscribe`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(function (response) {
        // First sort situation where response not 200
        if (response.status !== 200) {
            console.log(response.status);
            return;
        }

        response.json().then(function (data) {
            console.log(data)
        })
    });
}

function setCookie(cname, cvalue, exdays) {
    // A method to set cookies
    // needs to be fed:
    // -the cookie name `cname`
    // -the cookie value `cvalue`
    // -the number of days till expiry
    // be careful and give it the right kind of input
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    const expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    // a function to get a specific JS Cookie
    // we give it the name of the cookie and it searches for it
    // if the cookie value is JSONparsable, then we return true for
    // the value of parse otherwise it's false and we always have
    // a dictionary of three values returned: 
    // name of the cookie
    // value of the cookie
    // parse which is true if the value is JSON parsable
    const name = cname + "=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const ca = decodedCookie.split('; ');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        let c_split = c.split('=');
        if (c_split[0] === cname) {

            let parse_value = false;
            try {
                JSON.parse(c_split[1]);
                parse_value = true;
            } catch (e) { }

            return {
                name: c_split[0],
                value: c_split[1],
                parse: parse_value
            };
        }
    }
    return "";
}


function deleteCookie(cname) {
    // a function to delete cookies by changing expiry date
    document.cookie = cname + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}



$(document).on('click', '.cart-btn', function () {
    var id = $(this).attr("id");
    var entry = {
        prod_id: id,
        user_id: $(`#hidden_usr${id}`).val(),
        quantity: $(`#hidden_qty${id}`).val(),
    }
    fetch(`/add_to_cart`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(function (response) {
        if (response.status !== 200) {
            // find a way to flush error msg
            console.log(response.status);
            return;
        }
        response.json().then(function (data) {
            if (data.status == 408) {
                // find a way to flush error msg and exit
                console.log(data.err);
                return;
            }


            //place count here so it's accessible from UI
            let count = 1;

            // cookies from cart update
            if (getCookie('cart') != '') {
                // it's not empty so we just append the item and change the total
                let c_cookie = getCookie('cart');



                if (c_cookie['parse'] == true) {

                    let c_cart = JSON.parse(c_cookie['value']);
                    // update count
                    count = parseInt(c_cart['count']);
                    count += 1;
                    // if the product is in the cart already that's a big error
                    // and the whole cart functionality should be reviewed
                    // since this should not happen
                    if (c_cart['items'][entry['prod_id']] != {}) {
                        console.log("Big error, refer to add-to-cart on functions.js")
                    }
                    c_cart['items'][entry['prod_id']] = entry;
                    c_cart['count'] = count;

                    const serialized = JSON.stringify(c_cart);
                    setCookie('cart', serialized, 7);
                } else {

                    // at this point, we know the cart is in a format which is not JSON parsable, so we reset things
                    setCookie('cart', "", 1);
                }

            } else {
                // we set the cookie since it's empty

                let cart = {
                    'items': { [entry['prod_id']]: entry, },
                    // get count from originally created count const initialized to 1
                    'count': count,
                }
                const serialized = JSON.stringify(cart);
                setCookie('cart', serialized, 7);
            }
            // update count of products

            const cartCountSpan = document.querySelector('.cart-count span');
            cartCountSpan.innerHTML = count + ' Items';
            const cartCountIcons = document.querySelectorAll('.cart-icon .count');
            for (const icon of cartCountIcons) {
                icon.innerHTML = count;
            }

            // at this point, change button to be hidden and only display +/- for quantity
            const inc_dec_btn = document.getElementById("inc_dec" + id);
            if (inc_dec_btn.classList.contains('d-none')) {
                inc_dec_btn.classList.remove('d-none');
            }
            inc_dec_btn.classList.add('d-flex');
            const add_2_cart_btn = document.getElementById("add_to_cart" + id);

            if (add_2_cart_btn.classList.contains('d-flex')) {
                add_2_cart_btn.classList.remove('d-flex');
            }
            add_2_cart_btn.classList.add('d-none');

            //reload
            $('#sitebar-cart').load(document.URL + ' #sitebar-cart>*')
        })

    });
});

$(document).on('click', '.cart_increase', function () {
    id = $(this).attr("id");
    const entry = {
         prod_id: id,
         quantity: $(`#cart_qty${id}`).val(),
         user_id: $(`#hidden_usr${id}`).val(),
         where: 'cart_increase',
        }
    fetch(`/change_qty`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(function (response) {
            if (response == 'max') {
                alert('Quantity Unavailable');
                return
            }
            if (response.status !== 200) {
                // find a way to flush error msg
                console.log(response.status);
                return;
            }
            response.json().then(function (data) {
                if (data.status == 408) {
                    // find a way to flush error msg and exit
                    console.log(data.err);
                    return;
                }
                let c_cookie = getCookie('cart');
                if (c_cookie['parse'] == true) {
                    let c_cart = JSON.parse(c_cookie['value']);
                    // if the product is not in the cart already that's a big error
                    // and the whole cart functionality should be reviewed
                    // since this should not happen
                    if (c_cart['items'][entry['prod_id']] == {}) {
                        console.log("Big error, refer to add-to-cart on functions.js")
                    }
                    c_cart['items'][entry['prod_id']]['quantity'] = data.quantity;   
                    const serialized = JSON.stringify(c_cart);
                    setCookie('cart', serialized, 7);
                } else {
                    // at this point, we know the cart is in a format which is not JSON parsable, so we reset things
                    setCookie('cart', "", 1);
                    return;
                }
                
                document.getElementById(`cart_qty${id}`).value = data.quantity;
                document.getElementById(`productlist_qty${id}`).value = data.quantity;
                //reload
                $('#sitebar-cart').load(document.URL + ' #sitebar-cart>*')
            })
        });
});

$(document).on('click', '.cart_decrease', function () {
    id = $(this).attr("id");
    const entry = {
         prod_id: id,
         quantity: $(`#cart_qty${id}`).val(),
         user_id: $(`#hidden_usr${id}`).val(),
         where: 'cart_decrease',
        }
    fetch(`/change_qty`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(function (response) {
            if (response == 'max') {
                alert('Quantity Unavailable');
                return
            }
            if (response.status !== 200) {
                // find a way to flush error msg
                console.log(response.status);
                return;
            }
            response.json().then(function (data) {
                if (data.status == 408) {
                    // find a way to flush error msg and exit
                    console.log(data.err);
                    return;
                }
                let c_cookie = getCookie('cart');
                if (c_cookie['parse'] == true) {
                    let c_cart = JSON.parse(c_cookie['value']);
                    // if the product is not in the cart already that's a big error
                    // and the whole cart functionality should be reviewed
                    // since this should not happen
                    if (c_cart['items'][entry['prod_id']] == {}) {
                        console.log("Big error, refer to add-to-cart on functions.js")
                    }
                    c_cart['items'][entry['prod_id']]['quantity'] = data.quantity;   
                    const serialized = JSON.stringify(c_cart);
                    setCookie('cart', serialized, 7);
                } else {
                    // at this point, we know the cart is in a format which is not JSON parsable, so we reset things
                    setCookie('cart', "", 1);
                    return;
                }
                
                document.getElementById(`cart_qty${id}`).value = data.quantity;
                document.getElementById(`productlist_qty${id}`).value = data.quantity;
                //reload
                $('#sitebar-cart').load(document.URL + ' #sitebar-cart>*')
            })
        });
});

$(document).on('click', '.checkout_cart_increase', function () {
    var el = $(this);
    var id = el.attr("id");
    if ($(`#hiddenAvailableQty${id}`).val() != null) {
        $(`#checkout_cart_qty${id}`).val($(`#hiddenAvailableQty${id}`).val());
        const item = document.querySelector(`#item${id}`);
        if (item.classList.contains("stock-out")) {
            item.classList.remove("stock-out");
        }
    }
    var qty = $(`#checkout_cart_qty${id}`).val();
    var total = $('#checkout_total').val();
    var where = 'cart_increase';

    $.post("cart.php", { id: id, qty: qty, total: total, where: where },
        function (result) {
            if (result == 'max') {
                alert('Quantity Unavailable');
            }
            else {
                var data = $.parseJSON(result);
                var subtotal = data[0];
                var total = data[1];
                var total_hidden = data[2];
                var item_qty = data[3];
                $(`#checkout_subtotal${id}`).html(subtotal);
                $('#checkout_total_value').html(total);
                $('#checkout_total').val(total_hidden);
                $('#navbar_cart_hidden').val(total_hidden);
                $('#navbar_cart_total').html(total);
                $(`#checkout_unit_qty${id}`).html(item_qty);
                $('#mobile_cart_total').html(total);
            }
        });
});

$(document).on('click', '.checkout_cart_decrease', function () {
    var el = $(this);
    var id = el.attr("id");
    if ($(`#hiddenAvailableQty${id}`).val() != null) {
        $(`#checkout_cart_qty${id}`).val($(`#hiddenAvailableQty${id}`).val());
        const item = document.querySelector(`#item${id}`);
        if (item.classList.contains("stock-out")) {
            item.classList.remove("stock-out");
        }
    }
    var qty = $(`#checkout_cart_qty${id}`).val();
    var total = $('#checkout_total').val();
    var where = 'cart_decrease';
    $.post("cart.php", { id: id, qty: qty, total: total, where: where },
        function (result) {
            var data = $.parseJSON(result);
            var subtotal = data[0];
            var total = data[1];
            var total_hidden = data[2];
            var item_qty = data[3];
            $(`#checkout_subtotal${id}`).html(subtotal);
            $('#checkout_total_value').html(total);
            $('#checkout_total').val(total_hidden);
            $('#navbar_cart_hidden').val(total_hidden);
            $('#navbar_cart_total').html(total);
            $(`#checkout_unit_qty${id}`).html(item_qty);
            $(`#checkout_cart_qty${id}`).val(item_qty);
            $('#mobile_cart_total').html(total);
        });
});

$(document).on('click', '.productlist_increase', function () {
    id = $(this).attr("id");
    const entry = {
         prod_id: id,
         quantity: $(`#cart_qty${id}`).val(),
         user_id: $(`#hidden_usr${id}`).val(),
         where: 'cart_increase',
        }
    fetch(`/change_qty`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(function (response) {
            if (response == 'max') {
                alert('Quantity Unavailable');
                return
            }
            if (response.status !== 200) {
                // find a way to flush error msg
                console.log(response.status);
                return;
            }
            response.json().then(function (data) {
                if (data.status == 408) {
                    // find a way to flush error msg and exit
                    console.log(data.err);
                    return;
                }
                let c_cookie = getCookie('cart');

                if (c_cookie['parse'] == true) {

                    let c_cart = JSON.parse(c_cookie['value']);
                    // if the product is not in the cart already that's a big error
                    // and the whole cart functionality should be reviewed
                    // since this should not happen
                    if (c_cart['items'][entry['prod_id']] == {}) {
                        console.log("Big error, refer to add-to-cart on functions.js")
                    }
                    c_cart['items'][entry['prod_id']]['quantity'] = data.quantity;   


                    const serialized = JSON.stringify(c_cart);
                    setCookie('cart', serialized, 7);
                } else {
                    // at this point, we know the cart is in a format which is not JSON parsable, so we reset things
                    setCookie('cart', "", 1);
                    return;
                }                    
                document.getElementById(`cart_qty${id}`).value = data.quantity;
                document.getElementById(`productlist_qty${id}`).value = data.quantity;
                //reload
                $('#sitebar-cart').load(document.URL + ' #sitebar-cart>*')
            })
        });
});

$(document).on('click', '.productlist_decrease', function () {
    id = $(this).attr("id");
    const entry = {
         prod_id: id,
         quantity: $(`#cart_qty${id}`).val(),
         user_id: $(`#hidden_usr${id}`).val(),
         where: 'cart_decrease',
        }
    fetch(`/change_qty`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(function (response) {
            if (response == 'max') {
                alert('Quantity Unavailable');
                return
            }
            if (response.status !== 200) {
                // find a way to flush error msg
                console.log(response.status);
                return;
            }
            response.json().then(function (data) {
                if (data.status == 408) {
                    // find a way to flush error msg and exit
                    console.log(data.err);
                    return;
                }
                let c_cookie = getCookie('cart');
                if (c_cookie['parse'] == true) {
                    let c_cart = JSON.parse(c_cookie['value']);
                    // if the product is not in the cart already that's a big error
                    // and the whole cart functionality should be reviewed
                    // since this should not happen
                    if (c_cart['items'][entry['prod_id']] == {}) {
                        console.log("Big error, refer to add-to-cart on functions.js")
                    }
                    c_cart['items'][entry['prod_id']]['quantity'] = data.quantity;   
                    const serialized = JSON.stringify(c_cart);
                    setCookie('cart', serialized, 7);
                } else {
                    // at this point, we know the cart is in a format which is not JSON parsable, so we reset things
                    setCookie('cart', "", 1);
                    return;
                }
                
                document.getElementById(`cart_qty${id}`).value = data.quantity;
                document.getElementById(`productlist_qty${id}`).value = data.quantity;
                //reload
                $('#sitebar-cart').load(document.URL + ' #sitebar-cart>*')
            })
        });
});

$(document).on('click', '.featured_increase', function () {
    var el = $(this);
    var id = el.attr("id");
    var qty = $(`#featured_qty${id}`).val();
    var total = $('#navbar_cart_hidden').val();
    var where = 'cart_increase'
    $.post("cart.php", { id: id, total: total, qty: qty, where: where },
        function (result) {
            if (result == 'max') {
                alert('Quantity Unavailable');
            }
            else {
                var data = $.parseJSON(result);
                var subtotal = data[0];
                var total = data[1];
                var total_hidden = data[2];
                var item_qty = data[3];
                $(`#cart_subtotal${id}`).html(subtotal);
                $('#total_value').html(total);
                $('#cart_total').val(total_hidden);
                $(`#recommended_qty${id}`).val(item_qty);
                $('#navbar_cart_hidden').val(total_hidden);
                $(`#cart_qty${id}`).val(item_qty);
                $('#navbar_cart_total').html(total);
                $(`#cart_unit_qty${id}`).html(item_qty);
                $('#mobile_cart_total').html(total);
            }
        });
});

$(document).on('click', '.featured_decrease', function () {
    var el = $(this);
    var id = el.attr("id");
    var qty = $(`#featured_qty${id}`).val();
    var total = $('#navbar_cart_hidden').val();
    var where = 'cart_decrease'
    $.post("cart.php", { id: id, total: total, qty: qty, where: where },
        function (result) {
            var data = $.parseJSON(result);
            var subtotal = data[0];
            var total = data[1];
            var total_hidden = data[2];
            var item_qty = data[3];
            $(`#cart_subtotal${id}`).html(subtotal);
            $('#total_value').html(total);
            $('#cart_total').val(total_hidden);
            $(`#recommended_qty${id}`).val(item_qty);
            $('#navbar_cart_hidden').val(total_hidden);
            $('#navbar_cart_total').html(total);
            $(`#cart_qty${id}`).val(item_qty);
            $(`#cart_unit_qty${id}`).html(item_qty);
            $('#mobile_cart_total').html(total);
        });
});

$(document).on('click', '.recommended_increase', function () {
    var el = $(this);
    var id = el.attr("id");
    var qty = $(`#recommended_qty${id}`).val();
    var total = $('#navbar_cart_hidden').val();
    var where = 'cart_increase'
    $.post("cart.php", { id: id, total: total, qty: qty, where: where },
        function (result) {
            if (result == 'max') {
                alert('Quantity Unavailable');
            }
            else {
                var data = $.parseJSON(result);
                var subtotal = data[0];
                var total = data[1];
                var total_hidden = data[2];
                var item_qty = data[3];
                $(`#cart_subtotal${id}`).html(subtotal);
                $('#total_value').html(total);
                $('#cart_total').val(total_hidden);
                $(`#featured_qty${id}`).val(item_qty);
                $('#navbar_cart_hidden').val(total_hidden);
                $('#navbar_cart_total').html(total);
                $(`#cart_qty${id}`).val(item_qty);
                $(`#cart_unit_qty${id}`).html(item_qty);
                $('#mobile_cart_total').html(total);
            }
        });
});

$(document).on('click', '.recommended_decrease', function () {
    var el = $(this);
    var id = el.attr("id");
    var qty = $(`#recommended_qty${id}`).val();
    var total = $('#navbar_cart_hidden').val();
    var where = 'cart_decrease'
    $.post("cart.php", { id: id, total: total, qty: qty, where: where },
        function (result) {
            var data = $.parseJSON(result);
            var subtotal = data[0];
            var total = data[1];
            var total_hidden = data[2];
            var item_qty = data[3];
            $(`#cart_subtotal${id}`).html(subtotal);
            $('#total_value').html(total);
            $('#cart_total').val(total_hidden);
            $(`#featured_qty${id}`).val(item_qty);
            $('#navbar_cart_hidden').val(total_hidden);
            $('#navbar_cart_total').html(total);
            $(`#cart_qty${id}`).val(item_qty);
            $(`#cart_unit_qty${id}`).html(item_qty);
            $('#mobile_cart_total').html(total);
        });
});

$(document).on('click', '#user_contact', function () {
    var email = $('#hidden_email').val();
    var subject = $('#subject').val();
    var message = $('#message').val();
    var token = $('.contact_page_token').val();
    var where = 'site_contact'
    $.post("add.php", { email: email, token: token, subject: subject, message: message, where: where },
        function (result) {
            if (result == 'success') {
                alert('Your message was successfully sent! We shall get back to you in the shortest instance possible.');
                location.reload(true);
            }
            else if (result == 'error') {
                alert("Something went wrong. Please try again later.");
            }
            else {
                alert("Something went wrong. Please try again later.");
            }
        });
});

$(document).on('click', '#anonymous_contact', function () {
    var name = $('#full_name').val();
    var email = $('#email_address').val();
    var number = $('#mobile_number').val();
    var subject = $('#subject').val();
    var message = $('#message').val();
    var token = $('.contact_page_token').val();
    var where = 'site_contact';
    $.post("add.php", { name: name, email: email, token: token, number: number, subject: subject, message: message, where: where },
        function (result) {
            if (result == 'success') {
                alert('Your message was successfully sent! We shall get back to you in the shortest instance possible.');
                location.reload(true);
            }
            else if (result == 'error') {
                alert("Something went wrong. Please try again later.");
            }
            else {
                alert("Something went wrong. Please try again later.");
            }
        });
});

$(document).on('click', '#user_comment', function () {
    var email = $('#hidden_email').val();
    var id = $('#blog_id').val();
    var comment = $('#comment').val();
    var token = $('.comment_token').val();
    var where = 'site_comment';
    $.post("add.php", { id: id, email: email, token: token, comment: comment, where: where },
        function (result) {
            if (result == 'success') {
                alert('Your comment was successfully posted! ');
                location.reload(true);
            }
            else if (result == 'error') {
                alert("Something went wrong. Please try again later.");
                location.reload(true);
            }
            else {
                alert("Something went wrong. Please try again later.");
                location.reload(true);
            }
        });
});

$(document).on('click', '#anonymous_comment', function () {
    var name = $('#name').val();
    var email = $('#email').val();
    var id = $('#blog_id').val();
    var comment = $('#comment').val();
    var token = $('.comment_token').val();
    var where = 'site_comment';
    $.post("add.php", { id: id, name: name, email: email, token: token, comment: comment, where: where },
        function (result) {
            if (result == 'success') {
                alert('Your comment was successfully posted! ');
                location.reload(true);
            }
            else if (result == 'error') {
                alert("Something went wrong. Please try again later.");
                location.reload(true);
            }
            else {
                alert("Something went wrong. Please try again later.");
                location.reload(true);
            }
        });
});

$(document).on('click', '.reply-btn', function () {
    var el = $(this);
    var id = el.attr("id");
    var email = $('#hidden_email').val();
    var extraForm = "";
    extraForm += "<form action='#' class='respons-contact-form'>";
    extraForm += '<div class="form-item col-lg-7 p-0">';
    extraForm += '<input type="text" name="subcomment_name" id="subcomment_name" placeholder="Full Name" required>';
    extraForm += '<i class="fas fa-user"></i>';
    extraForm += '</div>';
    extraForm += '<div class="form-item col-lg-7 p-0">';
    extraForm += '<input type="text" name="subcomment_email" id="subcomment_email" placeholder="Email Address" required>';
    extraForm += '<i class="fas fa-envelope"></i>';
    extraForm += '</div>';
    extraForm += '<div class="form-item col-lg-12 p-0">';
    extraForm += '<textarea name="subcomment" id="subcomment" placeholder="Type your reply" required></textarea>';
    extraForm += '<i class="fab fa-telegram-plane"></i>';
    extraForm += '</div>';
    extraForm += '<div>';
    extraForm += '<input type="hidden" class="subcomment_token" id="token" name="token">';
    extraForm += `<input type="hidden" class="comment_id" id="comment_id" name="comment_id" value="` + id + `">`;
    extraForm += '<button type="submit" class="submit anonymous_subcomment" id="' + id + '" >Reply to Comment</button>';
    extraForm += '</div>';
    extraForm += "</form>";
    extraForm += "<br>";

    var form = "";
    form += "<form action='#' class='respons-contact-form'>";
    form += "<input type='hidden' class='subcomment_token' id='token' name='token'>";
    form += "<input type='hidden' class='comment_id' id='comment_id' name='comment_id' value='" + id + "'>";
    form += "<input type='hidden' name='subcomment_hidden_email' id='subcomment_hidden_email' value='" + email + "'>";
    form += "<div class='form-item col-lg-12 p-0'>";
    form += "<textarea name='subcomment' id='subcomment' placeholder='Type your reply' required></textarea>";
    form += "<i class='fab fa-telegram-plane'></i>";
    form += "</div>";
    form += "<button type='submit' class='submit user_subcomment' id='" + id + "'>Reply to Comment</button>";
    form += "</form>";
    form += "<br>";
    $(`.subcomment-response-user${id}`).html(form);
    $(`.subcomment-response-anonymous${id}`).html(extraForm);
});

$(document).on('click', '.user_subcomment', function () {
    var email = $('#subcomment_hidden_email').val();
    var id = $('#comment_id').val();
    var subcomment = $('#subcomment').val();
    var token = $('.subcomment_token').val();
    var where = 'site_subcomment';
    $.post("add.php", { id: id, email: email, token: token, subcomment: subcomment, where: where },
        function (result) {
            if (result == 'success') {
                alert('Your reply was successfully posted! ');
                location.reload(true);
            }
            else if (result == 'error') {
                alert("Something went wrong. Please try again later.");
                location.reload(true);
            }
            else {
                alert("Something went wrong. Please try again later.");
                location.reload(true);
            }
        });
});

$(document).on('click', '.anonymous_subcomment', function () {
    var name = $('#subcomment_name').val();
    var email = $('#subcomment_email').val();
    var id = $('#comment_id').val();
    var subcomment = $('#subcomment').val();
    var token = $('.subcomment_token').val();
    var where = 'site_subcomment';
    $.post("add.php", { id: id, name: name, email: email, token: token, subcomment: subcomment, where: where },
        function (result) {
            if (result == 'success') {
                alert('Your reply was successfully posted! ');
                location.reload(true);
            }
            else if (result == 'error') {
                alert("Something went wrong. Please try again later.");
                location.reload(true);
            }
            else {
                alert("Something went wrong. Please try again later.");
                location.reload(true);
            }
        });
});

function filter_data() {
    var organization = $('.organization_name').val();
    var loader = '<div class="loader__figure"></div';
    loader += '<p class="loader__label">' + organization + '</p>';
    $('.loader').html(loader);
    var action = 'fetch data';
    var range = $('.js-range-slider').val();
    var arr = range.split(";");
    var minimum_price = arr.splice(0, 1).join("");
    var maximum_price = arr.join(";");
    var category = get_filter('category_selector');
    var where = 'filter';
    $.post("load.php", { action: action, minimum_price: minimum_price, maximum_price: maximum_price, category: category, where: where },
        function (data) {
            $('.product-list').html(data);
        });
}

function get_filter(class_name) {
    var filter = [];
    $('.' + class_name + ':checked').each(function () {
        filter.push($(this).val());
    });
    return filter;
}

$(document).on('change', '.js-range-slider', function () {
    filter_data();
});

$(document).on('click', '.category_selector', function () {
    filter_data();
});

$(document).on('click', '.editProfile', function () {
    var firstname = $('#firstname').val();
    var lastname = $('#lastname').val();
    var email = $('#email').val();
    var mobile = $('#mobile').val();
    var Location = $('#location').val();
    var old_email = $('#old_email').val();
    var token = $('#token').val();
    var where = $('#where').val();
    $.post("save.php", { firstname: firstname, lastname: lastname, email: email, mobile: mobile, location: Location, old_email: old_email, token: token, where: where },
        function (result) {
            if (result == 'success') {
                alert('Your details have been edited successfully');
                location.reload(true);
            }
            else if (result == 'exists') {
                alert('Email address or mobile number entered exists');
            }
            else {
                alert("Something went wrong");
            }
        });
});

function paginate(page) {
    var where = 'pagination';
    $.ajax({
        url: "load.php",
        method: "POST",
        data: { page: page, where: where },
        success: function (data) {
            $('.pagination_data').html(data);
        }
    });
}

$(document).on('click', '.pagination_link', function () {
    var page = $(this).attr("id");
    paginate(page);
});

$('#product_Search').keyup(function () {
    var txt = $('#product_Search').val();
    var selector = document.getElementById('Cat_select');
    var category = selector[selector.selectedIndex].value;
    if (txt != '') {
        $.ajax({
            url: 'search.php',
            type: "post",
            data: { search: txt, category: category },
            dataType: "text",
            success: function (data) {
                $('#show_list').html(data);
            }
        });
    }
    else {
        $('#show_list').html('');
    }
    $(document).on('click', 'a', function () {
        $("#product_Search").val($(this).text());
        $("#show_list").html('');
    });
});

$('#Product_Search').keyup(function () {
    var txt = $('#Product_Search').val();
    var selector = document.getElementById('Cat_Select');
    var category = selector[selector.selectedIndex].value;
    if (txt != '') {
        $.ajax({
            url: 'search.php',
            type: "post",
            data: { search: txt, category: category },
            dataType: "text",
            success: function (data) {
                $('#Show_List').html(data);
            }
        });
    }
    else {
        $('#Show_List').html('');
    }
    $(document).on('click', 'a', function () {
        $("#Product_Search").val($(this).text());
        $("#Show_List").html('');
    });
});

$('.view').on('click', function () {
    // $(this).text("Show Less"); 
    $(this).parents('.order-card').addClass("show")
});
$('.show-less').on('click', function () {
    // $(this).text("Show Less"); 
    $(this).parents('.order-card').removeClass("show")
});

$(document).on('click', '#completeOrder', function () {
    $('#confirmDetails input:required').each(function () {
        if ($(this).val() === '') {
            alert('Kindly fill in all required fields');
        }
    });
    var date = $("#order_date").val();
    var mode = $("input[type='radio'][name='delivery_location']:checked").val();
    var payment = $("input[type='radio'][name='payment']:checked").val();
    var id = $("#customerId").val();
    var where = 'onlineOrder';
    $.post("add.php", { id: id, date: date, mode: mode, payment: payment, where: where },
        function (result) {
            alert('Your order has been successfully made.');
            window.location.href = 'order-success.php';
        });
});

