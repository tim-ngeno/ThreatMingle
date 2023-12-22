$(document).ready(() => {
  $('#assessment-form').submit((e) => {
    // Prevent default form submission
    e.preventDefault();

    // Show loading indicator
    $('#loading-indicator').show();

    // Disable the submit button to prevent multiple submissions
    $('#scan-button').prop('disabled', true);

    window.location.href = redirectUrl;
  });
});
