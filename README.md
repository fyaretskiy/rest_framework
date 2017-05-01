# rest_framework

1. python manange runserver
2. /api/v1/users (POST, DELETE)
3. /api/v1/posts/{post_id} (GET)

POST to /api/v1/users to receive a token. Place in headers:
Authorization: Token {token}

GET to /api/v1/posts/{post_id} (GET) to retrieve data from https://jsonplaceholder.typicode.com/posts or sql db on second request.
