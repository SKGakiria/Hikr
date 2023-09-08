## Hikr API

1. **api-root (GET)**
   - URL: `/`
   - Description: This is the root endpoint of the API. It's typically used as an entry point to access other resources or discover available endpoints.

2. **group-list (GET, POST)**
   - URL: `/groups/`
   - Description: This endpoint allows you to list all groups (`GET`) or create a new group (`POST`).

3. **group-detail (GET, PUT, DELETE)**
   - URL: `/groups/<int:pk>/`
   - Description: This endpoint allows you to retrieve (`GET`), update (`PUT`), or delete (`DELETE`) a specific group by its primary key (`pk`).

4. **group-membership-list (GET, POST)**
   - URL: `/groups/<int:pk>/members/`
   - Description: This endpoint allows you to list all group members (`GET`) or create a new membership (`POST`) within a specific group identified by its primary key (`pk`).

5. **group-membership-delete (DELETE)**
   - URL: `/groups/<int:pk>/members/<int:member_pk>/`
   - Description: This endpoint allows you to delete a specific membership within a group. It requires the primary keys of both the group (`pk`) and the member (`member_pk`).

6. **event-list (GET, POST)**
   - URL: `/events/`
   - Description: This endpoint allows you to list all events (`GET`) or create a new event (`POST`).

7. **event-detail (GET, PUT, DELETE)**
   - URL: `/events/<int:pk>/`
   - Description: This endpoint allows you to retrieve (`GET`), update (`PUT`), or delete (`DELETE`) a specific event by its primary key (`pk`).

8. **api-event-participants-list (GET, POST)**
   - URL: `/events/<int:pk>/participants/`
   - Description: This endpoint allows you to list all participants of a specific event (`GET`) or add a new participant (`POST`) to that event, identified by its primary key (`pk`).

9. **event-participants-delete (DELETE)**
   - URL: `/events/<int:pk>/participants/<int:participant_pk>/`
   - Description: This endpoint allows you to remove a participant from a specific event. It requires the primary keys of both the event (`pk`) and the participant (`participant_pk`).

10. **user-list (GET)**
    - URL: `/users/`
    - Description: This endpoint allows you to list all users (`GET`).

11. **user-detail (GET, PUT, DELETE)**
    - URL: `/users/<int:pk>/`
    - Description: This endpoint allows you to retrieve (`GET`), update (`PUT`), or delete (`DELETE`) a specific user by their primary key (`pk`).

12. **user-register (POST)**
    - URL: `/users/register/`
    - Description: This endpoint allows a user to register by creating a new user account (`POST`).

13. **knox_login (POST)**
    - URL: `/users/login/`
    - Description: This endpoint is typically used for user authentication, allowing users to log in (`POST`) to their accounts.

14. **knox_logout (POST)**
    - URL: `/users/logout/`
    - Description: This endpoint is used to log out a user session (`POST`) using the Knox authentication framework.

15. **knox_logoutall (POST)**
    - URL: `/users/logoutall/`
    - Description: This endpoint is used to log out a user from all sessions (`POST`) using the Knox authentication framework.

These endpoints provide CRUD (Create, Read, Update, Delete) operations for managing users, groups, events, and their associated data within your Django REST API. The endpoints related to user authentication and sessions are powered by the Knox authentication framework.