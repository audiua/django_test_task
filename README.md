This is a test project.

#Install

### .env settings example
```commandline
DEBUG=true
SECRET_KEY=0r^4chmbzsum32i(g-v$pc=7x942-22pde2^+))bv&pyo
STATIC_ROOT=/static
DATABASE=postgres
DB_NAME=postgres
DB_USER=postgres
DB_PASS=postgres
DB_SERVICE=postgres
DB_PORT=5432
```

### run docker-compose
+ in project root directory run command 
```commandline
docker-compose up
```
If you will see errors with permissions denied, run the command in the project root directory
```commandline
sudo chown -R $USER:$USER .
```
and run command again
```commandline
docker-compose up
```
You should see the running containers

###  manage a database (dev only)
+ for manage a postresql is running a container with a pgadmin4
+ run in a browser 0.0.0.0:5050
+ add a server with following settings:
```json
    {
        "general": {
            "name": "local"
        },
        "connection": {
            "Hostname/address": "postgres",
            "Port": 5432,
            "Maintenance database": "postgres",
            "Username": "postgres",
            "Password": "postgres"
        }
    }
```
+ save the server

Refresh servers, and you will see the local server  
with the postgres database

### persist data
data is persisted in the docker volumes.  
see https://docs.docker.com/compose/compose-file/#volume-configuration-reference.  
To list all volumes run the command
```commandline
docker volumes ls
```

####for deleting the volume run the command
see https://docs.docker.com/engine/reference/commandline/volume_rm/  
```commandline
docker volume rm volme_name
```
####delete test volumes
```commandline
docker volume rm kiwi_postgres kiwi_redis kiwi_pgadmin
```

### run migrations
For running django migrations you should run the command
```commandline
docker-compose run --rm kiwi_web python3 manage.py migrate
```

### collect satticfiles
```commandline
docker-compose run --rm kiwi_web python3 manage.py collectstaticfiles
```

#develop

### run tests
for running tests you should run the command
```commandline
docker-compose run --rm kiwi_web python3 manage.py test
```


#prodaction
###deploy