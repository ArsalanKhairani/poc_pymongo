# poc_pymongo
Repo to debug a issue.

### Create virtual env
To create a virtual env:
- `pip install virtualenv` to install virtual env package
- In a directory run `virtualenv poc-pymongo` to create a virtual env with name poc-pymongo. (My directory is `/home/madmin/venv`)
- In the same directry run `source poc-pymongo/bin/activate` to activate virtual env
- Go to project directory & run `pip install -r requirements` to install project dependencies.

### Run project via Flask HTTP server
In the project directory, run:
```
export FLASK_APP=app.py
flask run
```

It'll launch a web server that'll be listening on port 5000 (default).

Reference: http://flask.pocoo.org/docs/0.12/quickstart/

### Run via Apache2
To run the project using Apache2: 
```
cp apache2-site.conf /etc/apache2/sites-available/
sudo a2ensite apache2-site
sudo service apache2 reload
```

Now visit, `http://127.0.0.1:5000/` on your browser and check `/var/log/apache2/error.log` for errors.

### Note
- If you virtual env path is different (and it'll be), copy the same path to `app.wsgi`.
- Similarly, you'll need to update the project path in `app.wsgi` and `apache2-site.conf`.
- You'll need to enable `mod_wsgi` in Apache2 for the project to work.
