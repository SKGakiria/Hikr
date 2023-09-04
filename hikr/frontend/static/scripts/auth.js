$(document).ready(function () {
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
        showToasts(errorMessages, 'err-toast');
      }
    });
  });

  $('#login-form').submit(function (event) {
    event.preventDefault();
    const email = $('#email').val();
    const password = $('#password').val();
    login(email, password);
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
      showToasts(['User logged in successfully!'], 'succ-toast');
      // Redirect to the home page after login.
      window.location.href = '/';
    },
    error: function (error) {
      showToasts(['Invalid email or password. Please try again.'], 'err-toast');
      console.error(error);
    }
  });
}

// Function to show multiple messages
function showToasts (messages, toastType) {
  const toast = document.getElementById(toastType);
  toast.innerHTML = ''; // Clear existing messages
  messages.forEach(function (message) {
    const messagePara = document.createElement('p');
    messagePara.innerText = message;
    toast.appendChild(messagePara);
  });
  toast.style.display = 'block';
  setTimeout(function () {
    toast.style.opacity = '0';
    setTimeout(function () {
      toast.style.display = 'none';
    }, 500);
  }, 5000); // Show for 5 seconds
}
