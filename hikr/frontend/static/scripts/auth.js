$(document).ready(function () {
  // User sign up
  $('#signup-form').submit(function (event) {
    event.preventDefault();

    // Create a JavaScript object from the form data
    const formData = {
      email: $('#email').val(),
      username: $('#username').val(),
      password: $('#password').val(),
      first_name: $('#first_name').val(),
      last_name: $('#last_name').val(),
      location: $('#location').val()
    };

    // POST request to signup endpoint
    $.ajax({
      url: '/api/users/register/',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(formData),
      success: function (data) {
        // Signup successful, call the login function
        login(formData.email, formData.password);
      },
      error: function (error) {
        // Extract and display all error messages from the response
        const errorResponse = JSON.parse(error.responseText);
        const errorMessages = Object.values(errorResponse);
        alert(errorMessages)
      }
    });
  });

  // User login
  $('#login-form').submit(function (event) {
    event.preventDefault();
    const email = $('#email').val();
    const password = $('#password').val();
    login(email, password);
  });

  // User logout
  $('#logout-link').on('click', function () {
    if (sessionStorage.getItem('authToken')) {
      sessionStorage.removeItem('authToken');
      alert('User logged out successfully!')
    }
  });
});

// Function for user login
function login (email, password) {
  $.ajax({
    url: '/api/users/login/',
    contentType: 'application/json',
    type: 'POST',
    data: JSON.stringify({
      email,
      password
    }),
    success: function (response) {
      // Store the authentication token securely
      sessionStorage.setItem('authToken', response.token);
      // Check if there is a 'next' parameter in the URL
      const queryParams = new URLSearchParams(window.location.search);
      const nextUrl = queryParams.get('next');

      // Redirect to the 'next' URL if it exists, or to the home page '/'
      if (nextUrl) {
        window.location.href = nextUrl;
      } else {
        window.location.href = '/';
      }
    },
    error: function (error) {
      alert('Invalid email or password. Please try again.');
      console.error(error);
    }
  });
}