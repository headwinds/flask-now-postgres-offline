# Forge a modular Python API with blueprints, csrf protection, and recaptcha

so you want to build a simple Flask based python API with [Flaskex](https://github.com/anfederico/Flaskex) and deploy it with [now](https://zeit.co/now)?

Built on top of the Flaskex starter, I added the following:
* registration with recaptcha 
* verify registration account via email 
* more modular blueprint routes so that you can serve json or html templates
* a route which performs a database join
* routes that perform all the REST verbs: GET, POST, PUT, DELETE, PATCH 
* redesigned the landing page flow and added a few new pages
* offline dev: so that you can code without wifi 
* offline sync: the end user could do work in a native app and sync later

# Getting Started 

After you have setup your [recaptcha](https://pusher.com/tutorials/google-recaptcha-flask) keys, you can either begin with either the remote or local deployment.

#### Local deployment

Then let's dig into the code base and run it locally. 

1. create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) called env

```
python -m venv tutorial-env 
```

2. install the requirements.

```
$ source env/bin/activate 
$ python install -r requirements.txt
```

3. rename .env-sample to .env and edit the local database connection uri to match your local setup

```
DATABASE_URI = "postgresql+psycopg2://testuser:testpassword@localhost:5432/postgres"
```

If this fails, you will probably need to [create a test user](https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e) on your postgres DB. 

4. run the app 

```
$ python app.py 
```

Open your browswer to http://localhost:5000

#### Remote deployment

Let's deploy it right away in 3 steps.

1. setup your remote postgreSQL database.

I went with [ElephantSQL](https://www.elephantsql.com/) which has a nice free tier for hobbyists. Once you create your database, find that database from the **list all instances** drop down at the top. On the details screen, you should be able to find your url. 


2. Add your zeit [secrets](https://zeit.co/docs/v2/deployments/environment-variables-and-secrets) 

```
now secret add flashex-db-uri 'postgresql+psycopg2://username:password@dbhost:dbport/dbname' 
now secret add flaskex-secret-key 'flaskex' 
```

3. deploy 

```
now
```

Open your browswer then copy and paste the url it provided to your clipboard. 

# Credit 

This codebase is mainly based on the original [Flaskex sample](https://github.com/anfederico/Flaskex) with inspiration taken from the [now flaskex example](https://zeit.co/examples/flaskex-postgresql) which for me went too far. I decided I didn't want a separate flask app running for each route and thought it easier for someone learning python to concentrate on the single app approach. 

I also wanted to this example to work completely offline so that I could tinker with it during my subway commute. 

# Other nice flask starter projects

* [flask-restplus-server-example](https://github.com/frol/flask-restplus-server-example)
* [flask_weather](https://github.com/M0nica/flask_weather)
