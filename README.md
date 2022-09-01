# Сервис для сокращения ссылок (Django, Docker)


### Endpoints:

  1. GET `/` - get the form to short the link
  2. POST `/` - create a link with the form
  3. GET `url/[short-link]/` - redirect to url you shorted
  4. The lists of shorts and its counter you find here `/admin`


### Start the project:

1. Clone it
```
git clone https://github.com/CodeWormD/yatube_blog.git
```

2. Run docker
```
docker-compose build
docker-compose up
```