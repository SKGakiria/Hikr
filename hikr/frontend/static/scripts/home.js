$(document).ready(function () {
  const eventsUrl = '/api/events/';
  const groupsUrl = '/api/groups/';
  fetchEventsData(eventsUrl);
  fetchGroupsData(groupsUrl);
});

async function fetchEventsData (eventsUrl) {
  const data = await $.get(eventsUrl);
  // Iterate through the first 8 results from the API response
  for (let i = 0; i < 8 && i < data.results.length; i++) {
    const event = data.results[i];
    const eventOwner = await getFullUserName(event.owner);
    const eventParticipantsCount = await getParticipantsCount(event.id);
    const formattedDateTime = formatDateAndTime(event.date, event.time);

    const eventTile = `
                <div data-recommendationid="" data-recommendationsource="" data-eventref="${event.id}" class="p-0 bg-clip-padding bg-cover bg-transparent relative h-full flex bg-white z-0 break-words transition-shadow duration-300 px-4 pt-6 pb-5 smd:px-0 smd:pt-0 smd:flex-row smd:justify-start smd:rounded e3uszjm">
                    <a class="w-full inline cursor-pointer relative hover:no-underline group" href="/events/${event.id}" data-event-label="eventsShelf IRL-Event card variant">
                        <div class="flex w-full h-full flex-row smd:flex-col smd:flex-col-reverse">
                            <div class="space-y-2 grow pr-4 smd:mt-3">
                                <h3 class="text-lg leading-6 font-semibold line-clamp-4 smd:text-xl smd:leading-6 group-hover:underline h1lk27w4">${event.name}</h3>
                                <p class="line-clamp-2 text-sm text-gray6 font-medium">Hosted by: ${eventOwner}</p>
                                <div>
                                    <div class="flex items-center space-x-1.5 text-gray7">
                                        <div style="width:20px;height:20px"><i class="fa-regular fa-calendar" style="color: #c0bfbc;"></i></div>
                                        <div class="flex flex-col uppercase text-sm leading-5 tracking-tight"><time title="">${formattedDateTime}</time></div>
                                    </div>
                                </div>
                                <div class="flex gap-x-4 flex-wrap gl:pt-1">
                                    <div class="flex items-center space-x-1.5 text-gray7">
                                        <div style="width:20px;height:20px"><i class="fa-solid fa-location-dot" style="color: #c0bfbc;"></i></div>
                                        <span>${event.location}</span>
                                    </div>
                                </div>
                                <div class="flex gap-x-4 flex-wrap gl:pt-1">
                                    <div class="flex items-center space-x-1.5 text-gray7">
                                        <div style="width:20px;height:20px"><i class="fa-regular fa-circle-check" style="color: #c0bfbc;"></i></div>
                                        <span>${eventParticipantsCount} going</span>
                                    </div>
                                </div>
                            </div>
                            <div class="bg-transparent ml-3 smd:ml-0 gl:mr-0 d1umy16x">
                                <div class="relative overflow-hidden bg-transparent w-full" style="height:90px"><img alt="${event.name}" loading="lazy" width="90" height="90" decoding="async" data-nimg="1" class="rounded-t-lg rounded-lg w-full h-full absolute top-0 left-0 object-cover object-center group-hover:opacity-80" style="color:transparent" src="${event.image}" />
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
            `;

    $('#eventsContainer').append(eventTile);
  }
}

async function fetchGroupsData (groupsUrl) {
  const data = await $.get(groupsUrl);
  // Iterate through the first 3 results from the API response
  for (let i = 0; i < 3 && i < data.results.length; i++) {
    const group = data.results[i];
    const groupOwner = await getFullUserName(group.owner);
    const firstParagraph = extractFirstParagraph(group.description);
    const groupTile = `
        <div class="flex-1"><a href="groups/${group.id}/" data-event-label="Story 1 variant" target="_blank"
        rel="noopener noreferrer" class="cursor-pointer hover:no-underline group"><img alt="${group.name}" loading="lazy"
          width="375" height="191" decoding="async" data-nimg="1"
          class="w-full rounded-lg mb-6 group-hover:opacity-80" style="color:transparent" src="${group.image}" />
        <h3 class="mb-3 pr-4 text-lg font-semibold">${group.name}</h3>
        <div class="mb-4 line-clamp-2 text-sm text-gray7 font-medium">Created by: ${groupOwner}</div>
        <div class="mb-4 text-gray6">${firstParagraph}</div>
        <div class="text-viridian group-hover:underline">Read more</div>
      </a></div>
        `;
    $('#groupsContainer').append(groupTile);
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

async function getParticipantsCount (eventId) {
  const eventParticipantsUrl = '/api/events/' + eventId + '/participants/';
  try {
    const response = await $.get(eventParticipantsUrl);

    // Check if the response contains data and is an array
    if (Array.isArray(response)) {
      return response.length;
    } else {
      // Handle the case where there is no content (HTTP 204) or unexpected data
      return 1; // The creator of the event is always a participant.
    }
  } catch (error) {
    console.error('Error:', error);
    return 1;
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

// Function to extract the first paragraph from an HTML string
function extractFirstParagraph (htmlString) {
  const closingTagIndex = htmlString.indexOf('</p>');

  if (closingTagIndex !== -1) {
    const firstParagraphText = htmlString.slice(3, closingTagIndex);
    return firstParagraphText;
  } else {
    return htmlString;
  }
}
