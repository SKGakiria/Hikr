$(document).ready(function () {
  const eventsUrl = '/api/events/';
  
  $('#search-form').submit(function (event) {
    event.preventDefault();
    const searchQuery = $('#search-input').val();
    $('#eventsListContainer').empty();
    fetchEventsData(eventsUrl, searchQuery);
  });
  
  $('#search-submit').on('keypress', function (e) {
    if (e.which === 13) { // 13 is the Enter key code
      const searchQuery = $('#search-input').val();
      $('#eventsListContainer').empty();
      fetchEventsData(eventsUrl, searchQuery);
    }
  });

  fetchEventsData(eventsUrl);
  
  async function fetchEventsData (eventsUrl, searchQuery = '') {
    const url = new URL(window.location.origin + eventsUrl);
    if (searchQuery) {
      url.searchParams.append('search', searchQuery);
    }
    const data = await $.get(url);
    for (let i = 0; i < 8 && i < data.results.length; i++) {
      const event = data.results[i];
      const eventOwner = await getFullUserName(event.owner);
      const eventParticipantsCount = await getParticipantsCount(event.id);
      const formattedDateTime = formatDateAndTime(event.date, event.time);
      const eventTile = `
          <div>
          <div data-recommendationid=""
              data-recommendationsource="ml-popular-events-nearby"
              data-eventref="${event.id}"
              class="p-0 bg-clip-padding bg-cover bg-transparent relative h-full flex bg-white z-0 break-words transition-shadow duration-300 w-full flex-row justify-start py-4 border-t border-gray3 md:pt-4 md:pb-5">
              <a class="w-full inline cursor-pointer relative hover:no-underline"
                  href="/events/${event.id}">
                  <div class="flex w-full flex-col">
                      <div
                          class="flex flex-row-reverse md:flex-row flex-1 overflow-hidden">
                          <div class="bg-transparent ml-3 md:mr-3 md:ml-0 d15a685b">
                              <div class="relative overflow-hidden bg-transparent w-full"
                                  style="height:125px"><img
                                      alt="${event.name}" loading="lazy"
                                      fetchpriority="high" width="222" height="125"
                                      decoding="async" data-nimg="1"
                                      class="rounded-t-lg rounded-lg w-full absolute top-0 left-0 object-contain object-center"
                                      style="color:transparent"
                                      src="${event.image}"/>
                              </div>
                          </div>
                          <div class="overflow-hidden w-full">
                              <div
                                  class="flex justify-between md:items-center flex-col-reverse md:flex-row">
                                  <div
                                      class="flex flex-col uppercase text-sm leading-5 tracking-tight text-darkGold font-medium pb-1 pt-1 line-clamp-1 lg:line-clamp-2">
                                      <h3><time title="${formattedDateTime}">${formattedDateTime} </time></h3>
                                  </div>
                              </div>
                              <h2
                                  class="text-gray7 font-medium text-base pt-0 pb-1 line-clamp-3">
                                  ${event.name}
                              </h2>
                              <div class="w-full  text-sm  mx-auto mb-2 md:mb-4">
                                  <p class="md:line-clamp-1 text-gray6">
                                  <i class="fa-regular fa-user" style="color: #c0bfbc;"></i>&nbsp;&nbsp;${eventOwner}
                                  </p>
                                  <br>
                                  <p class="md:line-clamp-1"><i class="fa-solid fa-location-dot" style="color: #c0bfbc;"></i>&nbsp;&nbsp;${event.location}</p>
                              </div>
                              <div class="h-0 sm:h-8 sm:block xmedia">
                              <div class="text-gray6 text-sm"><div aria-label="${eventParticipantsCount} Going" class="text-gray6 text-sm">${eventParticipantsCount} Going</div></div>
                              </div>
                          </div>
                      </div>
                      <div class="h-8 mt-1.5 sm:h-0 sm:mt-0 block sm:hidden xmedia">
                      </div>
                  </div>
              </a>
          </div>
      </div>
          `;
      $('#eventsListContainer').append(eventTile);
    }
  }
  
  async function getParticipantsCount (eventId) {
    const eventParticipantsUrl = '/api/events/' + eventId + '/participants/';
    try {
      const response = await $.get(eventParticipantsUrl);
  
      // Check if the response contains data and is an array
      if (Array.isArray(response)) {
        return response.length;
      } else {
        // Handle the case where there is no content (HTTP 204) or unexpected data
        return 0;
      }
    } catch (error) {
      console.error('Error:', error);
      return 0;
    }
  }
  
  async function getFullUserName (userUrl) {
    try {
      const userData = await $.get(userUrl);
      return userData.first_name + ' ' + userData.last_name;
    } catch (error) {
      console.error('Error:', error);
    }
  }
  
  function formatDateAndTime (apiDate, apiTime) {
    // Create a JavaScript Date object from the provided date and time
    const dateTime = new Date(`${apiDate}T${apiTime}`);
  
    // Create an array of month names
    const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  
    // Get the day of the week, month, day, hour, and minute
    const dayOfWeek = dateTime.toLocaleString('en-US', { weekday: 'short' });
    const month = monthNames[dateTime.getMonth()];
    const day = dateTime.getDate();
    const hour = dateTime.getHours();
    const minute = dateTime.getMinutes();
  
    // Format the time as AM/PM
    const ampm = hour >= 12 ? 'PM' : 'AM';
    const formattedHour = hour % 12 || 12; // Convert 0 to 12 for 12-hour format
  
    const timeZoneAbbreviation = 'EAT';
  
    // Create the formatted string
    const formattedDateAndTime = `${dayOfWeek}, ${month} ${day} · ${formattedHour}:${minute.toString().padStart(2, '0')} ${ampm} ${timeZoneAbbreviation}`;
  
    return formattedDateAndTime;
  }
});
