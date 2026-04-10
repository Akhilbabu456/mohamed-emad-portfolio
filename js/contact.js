$(function() {
    // Get the form.
    var form = $('#ajax_form');

    // Get the messages div.
    var formMessages = $('#form-messages');

    // Set up an event listener for the contact form.
	$(form).submit(function(event) {
		// Stop the browser from submitting the form.
		event.preventDefault();

        // Check for uncompleted fields
        var name = $('#name').val().trim();
        var email = $('#email').val().trim();
        var message = $('#message').val().trim();

        if (name === '') {
            $(formMessages).removeClass('alert-success').addClass('alert-danger');
            $(formMessages).text('Please enter your name.');
            return;
        }
        if (email === '') {
            $(formMessages).removeClass('alert-success').addClass('alert-danger');
            $(formMessages).text('Please enter your email.');
            return;
        }
        if (message === '') {
            $(formMessages).removeClass('alert-success').addClass('alert-danger');
            $(formMessages).text('Please enter your message.');
            return;
        }

		// Serialize the form data.
		var formData = $(form).serialize();
		
        // Submit the form using AJAX.
		$.ajax({
			type: 'POST',
			url: $(form).attr('action'),
			data: formData,
            dataType: 'json'
		})
		.done(function(response) {
			// Make sure that the formMessages div has the 'success' class.
			$(formMessages).removeClass('alert-danger').addClass('alert-success');

			// Set the success message text.
			$(formMessages).text('Thank You! Your message has been sent successfully.');

			// Clear the form.
			$('#name').val('');
			$('#email').val('');
			$('#message').val('');
		})
		.fail(function(data) {
			// Make sure that the formMessages div has the 'danger' class.
			$(formMessages).removeClass('alert-success').addClass('alert-danger');

			// Display failure message
            $(formMessages).text('Oops! The email wasn\'t sent. Please try again.');
		});
		
	});
	
});