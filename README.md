# Build a simple Python 3 API with Flaskex

so you want to build a simple Flask based python API with [Flaskex](https://github.com/anfederico/Flaskex) and deploy it with [now](https://zeit.co/now)?

# Getting Started 


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

Then let's dig into the code base and run it locally. 

1. create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) called env

```
python -m venv tutorial-env 
```

2. install the requirements and the edit the .env with your local and remote settings. I used Elephant SQL free tier. 

```
$ source env/bin/activate 
$ python install -r requirements.txt
```

3. run the app 

```
$ python app.py 
```

Open your browswer to http://localhost:5000

# Credit 

This codebase is mainly based on the original [Flaskex sample](https://github.com/anfederico/Flaskex) with inspiration taken from the [now flaskex example](https://zeit.co/examples/flaskex-postgresql) which for me went too far. I decided I didn't want a separate flask app running for each route and thought it easier for someone learning python to concentrate on the single app approach. 

I also wanted to this example to work completely offline so that I could tinker with it during my subway commute. 

# Other nice flask starter projects

* [recaptcha](https://pusher.com/tutorials/google-recaptcha-flask)
* [flask-restplus-server-example](https://github.com/frol/flask-restplus-server-example)
* [flask_weather](https://github.com/M0nica/flask_weather)
