(function ($) {
	"use strict";

	// Form
	var contactForm = function () {
		if ($('#contactForm').length > 0) {
			$("#contactForm").validate({
				submitHandler: function (form) {
					var form = document.getElementById('contactForm');
					const data = new FormData(form)
					fetch(`${window.origin}` + '/crud/session-registration-create', {
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
							$('#flash_message').append(flashMessage('success', 'Session Registration Successful'));
							$(location).prop('href', `${window.origin}` + '/session-registration-success/' + data.get("session_uuid"));
							return;
						}
						// Else handle errors
						else {
							response.text().then(function (data) {
								// Registration exists
								if (data == 'Resource Exists') {
									$('#flash_message').append(flashMessage('warning', 'You are already registered for this session.'));
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
				} // end submitHandler

			});
		}
	};
	contactForm();

})(jQuery);
