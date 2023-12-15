$(document).ready(() => {
  $('#assessment-form').submit((e) => {
    // Prevent default form submission
    e.preventDefault();

    // Show loading indicator
    $('#loading-indicator').show();

    // Disable the submit button to prevent multiple submissions
    $('#scan-button').prop('disabled', true);

    // Perform the submission
    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      success: function (response) {
        // Handle success response
        window.location.href = response.redirect_url;
      },
      error: function (error) {
        // Handle error
        console.error('Error:', error);
      },
      complete: function () {
        // Hide loading indicator and enable submit button
        $('#loading-indicator').hide();
        $('#scan-button').prop('disabled', false);
      }
    });
  });
});
