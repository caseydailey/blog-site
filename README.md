# blog-site
This is a bare bones, MVP, personal site with a blog  made in Django. 
Submitted to fulfill the basic requirements of my long overdue "Capstone" project.
I look forward to soon digging in on a cool personal project when circumstances permit, 
but for now I humbly submit this old project, based on a tutorial done back in may, and presented here to say 

"Here you go. Hope this works?"
 

# Check it Out

clone it and hop into the directory:

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

Now navigate to http://127.0.0.1:8000/ and click around!

You'll see what I'm talking about when I say bare-bones, but it's all there.
The project has mulitple apps to handle the main parts of the app seperately and provide some level of "scalability".
Views and URLs are set up to facilitate movement throughout (learned about generic views--which are fantastic) and static files are linked in and loaded to allow for easy custom styling using bootstrap.  


If you want to create posts in the app, go to http://127.0.0.1:8000/admin
and login as: 

```
casey 
```

with the password:

```
django123
```


Now you can create blog posts with HTML formatting! yay Django!

Thank You!

