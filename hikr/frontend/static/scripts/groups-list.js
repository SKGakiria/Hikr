$(document).ready(function () {
    const groupUrl = '/api/groups/';
    fetchGroupsData(groupUrl);
});

async function fetchGroupsData (groupsUrl) {
    const data = await $.get(groupsUrl);
    for (let i = 0; i < data.results.length; i++) {
        const group = data.results[i];
        const description = extractFirstParagraph(group.description);
        const groupsMembersCount = await memberCount(group.id);
        const groupTile = `
        <div class="w-full">
        <div data-testid="group-card"
            class="py-3 border-t border-gray3 bg-white cursor-pointer flex flex-col"><a
                class="flex hover:no-underline" data-element-name="-groupCard" href="/groups/${group.id}">
                <div class="d1xev8qx mr-4 relative hidden sm:block"><img
                        alt="${group.name}" data-testid="next-image"
                        loading="lazy" width="178" height="100" decoding="async"
                        data-nimg="1"
                        class="object-cover object-center rounded-md max-h-[178px]"
                        style="color: transparent;"
                        src="${group.image}">
                </div>
                <div class="flex flex-col overflow-hidden w-full">
                    <div class="flex pb-4 justify-between">
                        <div>
                            <h3 class="pb-0.25 text-xl font-semibold w-full whitespace-normal overflow-ellipsis line-clamp-3 hdv6t0"
                                data-testid="group-card-title">${group.name}</h3>
                            <h3
                                class="pb-0.5 text-sm font-medium text-darkGold uppercase">
                                ${group.location}</h3>
                        </div>
                    </div>
                    <p class="pma6wzk m-0 pb-1 text-sm text-gray6 overflow-ellipsis line-clamp-2">
                       ${description}</p>
                    <div
                        class="flex pt-6 text-sm text-gray6 w-full items-center justify-between">
                        <div class="flex flex-row">${groupsMembersCount} member${groupsMembersCount !== 1 ? 's' : ''}</div>
                    </div>
                </div>
            </a></div>
    </div>
        `;
        $('#groupContainer').append(groupTile);
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


async function memberCount (groupId) {
    const groupMembersUrl = '/api/groups/' + groupId + '/members/';
    try {
        const response = await $.get(groupMembersUrl);
        if (Array.isArray(response)) {
            return response.length;
        } else {
            return 1;
        }
    }
    catch (error) {
        console.error('Error:', error);
        return 1;
    }

}
  
  function extractFirstParagraph (htmlString) {
    const closingTagIndex = htmlString.indexOf('</p>');
  
    if (closingTagIndex !== -1) {
      const firstParagraphText = htmlString.slice(3, closingTagIndex);
      return firstParagraphText;
    } else {
      return htmlString;
    }
  }