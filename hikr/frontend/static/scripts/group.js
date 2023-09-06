$(document).ready(function () {
  // Join a group
  $('#join-group-button').on('click', function (event) {
    event.preventDefault();
    console.log('join group button clicked');
    if (sessionStorage.getItem('authToken') !== null) {
      const groupId = $(this).attr('data-group-id');
      console.log(groupId);
      $.ajax({
        url: '/api/groups/' + groupId + '/members/',
        contentType: 'application/json',
        type: 'POST',
        headers: {
          Authorization: 'Token ' + sessionStorage.getItem('authToken'),
          'X-CSRFToken': getCookie('csrftoken')
        },
        success: function (response) {
          showToasts(['Joined group successfully!'], 'succ-toast');
          window.location.href = '/groups/' + groupId + '/';
        },
        error: function (error) {
          showToasts(['Error joining group. Please try again.'], 'err-toast');
          console.error(error);
        }
      });
    } else {
      showToasts(['Please login to join a group.'], 'err-toast');
      window.location.href = '/login/';
    }
  });

  // Leave a group
  $('#leave-group-button').on('click', function (event) {
    event.preventDefault();
    console.log('leave group button clicked');
    if (sessionStorage.getItem('authToken') !== null) {
      const groupId = $(this).attr('data-group-id');
      console.log(groupId);
      console.log(sessionStorage.getItem('authToken'), '  button clicked');
      $.ajax({
        url: '/api/groups/' + groupId + '/members/',
        contentType: 'application/json',
        type: 'DELETE',
        headers: {
          Authorization: 'Token ' + sessionStorage.getItem('authToken'),
          'X-CSRFToken': getCookie('csrftoken')
        },
        success: function (response) {
          showToasts(['Left group successfully.'], 'succ-toast');
          window.location.href = '/groups/' + groupId + '/';
        },
        error: function (error) {
          showToasts(['Error leaving group. Please try again.'], 'err-toast');
          console.error(error);
        }
      });
    } else {
      console.log('Error leaving group. Please try again.');
      showToasts(['Please login to leave a group.'], 'err-toast');
      window.location.href = '/login/';
    }
  });
});

function getCookie (name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Function to show multiple messages
function showToasts (messages, toastType) {
  // const toast = document.getElementById(toastType);
  // toast.innerHTML = '';
  // messages.forEach(function (message) {
  //   const messagePara = document.createElement('p');
  //   messagePara.innerText = message;
  //   toast.appendChild(messagePara);
  // });
  // toast.style.display = 'block';
  // setTimeout(function () {
  //   toast.style.opacity = '0';
  //   setTimeout(function () {
  //     toast.style.display = 'none';
  //   }, 500);
  // }, 5000);
  console.log(messages);
}
