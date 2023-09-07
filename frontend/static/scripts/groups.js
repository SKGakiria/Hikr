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
        <div class="py-3 border-t border-gray3 bg-white cursor-pointer flex flex-col"><a
                class="flex hover:no-underline" href="/groups/${group.id}/">
                <div class="mr-4 relative sm:block">
                  <img alt="${group.name}" loading="lazy" width="178" height="100" class="object-cover object-center rounded-md max-h-[178px]" style="color: transparent;" src="${group.image}" target=""/>
                </div>
                <div class="flex flex-col overflow-hidden w-full">
                    <div class="flex pb-4 justify-between">
                        <div>
                            <h3 class="pb-0.25 text-xl font-semibold w-full whitespace-normal overflow-ellipsis line-clamp-3 hdv6t0">${group.name}</h3>
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
    </div>`;
    $('#groupListContainer').append(groupTile);
  }
}

async function memberCount (groupId) {
  const groupMembersUrl = '/api/groups/' + groupId + '/members/';
  try {
    const response = await $.get(groupMembersUrl);
    if (Array.isArray(response)) {
      return response.length;
    } else {
      return 0;
    }
  } catch (error) {
    console.error('Error:', error);
    return 0;
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
