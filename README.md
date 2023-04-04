
# social_network_project

The basic CRUD operations for social network app which are implemented with django rest framework. The other part of this project automated bot which reads the config file and demonstrates the api functionality




## Features

- user signup 
- user login 
- post creation 
- post like 
- post unlike 
- analytics about how many likes was made. Example url /api/analitics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics aggregated by day. 
- user activity an endpoint which will show when user was login last time and when he mades a last request to the service.







## Run Locally

Clone the project

```bash
  git clone https://github.com/olehbilobok/social_network_project.git
```
Go to the project directory

```bash
  cd social_network_project
```
Perfom next commands
```bash
  python3 venv venv
```
```bash
  source venv/bin/activate
```
```bash
  pip install requirements.txt
```
```bash
  source set_env_variables.sh
```
```bash
  source set_env_variables.sh
```
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```
```bash
  python manage.py runserver
```



## Environment Variables

To run this project, you will need to add the following environment variables to your set_env_variables.sh file

`SECRET_KEY`

`DB_NAME`


## Postman Collection

[API collection](https://api.postman.com/collections/15325181-c47958dc-e8dc-4660-a629-bc2f95709df5?access_key=PMAT-01GX5R45N2GKA1KMP5T24TA396)

## Postman Variables

`host` = http//:127:0.0.1:8000/api

