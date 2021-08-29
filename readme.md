## To migrate tables (script is included)

- docker compose run web python manage.py migrate

## To create superuser

- (winpty) docker exec -it ___id python manage.py createsuperuser
- docker ps -aqf "name=___container_name" (get container id)
