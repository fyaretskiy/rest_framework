# rest_framework

1. python manage runserver 
2. /api/v1/users POST to receive a token. 

Place in headers:
Authorization: Token {token}

3. /api/v1/users GET for detail view.
4. /api/v1/users UPDATE {'username': new_username}
5. /api/v1/users DELETE
6. /api/v1/posts/{post_id} 

GET to /api/v1/posts/{post_id} to retrieve data from https://jsonplaceholder.typicode.com/posts or sql db on second request.
