# blog-site
This is a bare bones, MVP blog site in Django. 
Submitted to fulfill the basic requirements of my long overdue "Capstone" project.
I look forward to soon digging in on a cool personal project when circumstances permit, 
but for now I humbly submit this old project, copied over from a tutorial done back in may, and presented here as a formality to say 
"Here you go. Hope this works."

The purpose here is just to display a working knowledge of a basic Django project.

I've set up a basic site utilizing much of django's coolness. There are muliple apps in the project. 
Each of these consist of some basci

# Check it Out

clone it and hop into the directoryblog:

```
git clone https://github.com/caseydailey/blog-site.git
cd blog-site/blog/mysite
```
make migrations and run the runserver

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

Navigate to http://127.0.0.1:8000/ and click around!
You'll see what I'm talking about when I say barebones, but it's all there.
The project has mulitple apps to handle the main parts of the app seperately and provide some level of "scalability".
Views and URLs are set up to facilitate movemoent throughout and static files are linked in and loaded to allow for easy custome styling using bootstrap.


If you want to acces the CRUD portion of the app, got to http://127.0.0.1:8000/admin
and login as 

```
casey 
```

with the password

```
django123
```

