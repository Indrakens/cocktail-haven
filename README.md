# COCKTAIL | HEAVEN
Website designed to provide users learn and try cocktail recipes. Users can register to the site and once logged in they have access to all the site features. Registered users can create their own cocktail recipes and share their cocktail recipes with other users. Also can update or delete their own cocktail recipe. Users can like/ unlike cocktail recipes and also be involved in conversations related to chosen cocktail recipes by commenting on them. 
[responsiv website image]
#
The website was deployed via Heroku - the live site can be found here - [COCKTAIL | HEAVEN](https://cocktailheaven-c43cabf55fb3.herokuapp.com/)
#
# UX DESIGN
## Color Scheme
[add coclor cheme image]
## Typography
* Fonts
  * The website uses 'Ubuntu',sans-serif font from [Google Fonts]( https://fonts.google.com/?query=ubuntu ) and 'Lato',sans-serif font from [Google Fonts](https://fonts.google.com/?query=lato) .
* Images 
  * Cocktail images were searched and saved in file from [Google]( https://www.google.com/ ).
* Icons
  * The website uses [Font Awesome]( https://fontawesome.com/ ) icons for comment icon, heart icon, social media icons.
# UX
## Wireframe
[add wireframe images] 
# EPICS
* Site Admin [#21](https://github.com/users/Indrakens/projects/22?pane=issue&itemId=44337471)
* Unregistered User [#22](https://github.com/users/Indrakens/projects/22?pane=issue&itemId=44337652)
* Login User [#23](https://github.com/users/Indrakens/projects/22?pane=issue&itemId=44337783)
* Login/ Logout [#24](https://github.com/users/Indrakens/projects/22?pane=issue&itemId=44337948)
* Register [#25](https://github.com/users/Indrakens/projects/22?pane=issue&itemId=44338067)
## User Stories
The full list of User Stories is available on the project [kanban board](https://github.com/users/Indrakens/projects/22/views/1) . From the Epics 14 User Stories were developed.
* US Manage Recipes 
  * As aAdmin I can CRUD cocktail recipes so that I can manage my site content [#26](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44339341)
* Publish or Draft Cocktail Recipes 
  * As a Admin I can create recipe and draft it so that I can complete the cocktail recipe later [#27](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44339576)
* View Number of Comments 
  * As a Admin I can view the number of comments for a recipe so that I can know which are the most commented cocktail recipe [#28](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44339689)
* Manage Comments 
  * As a Admin I can approve or delete comment of each cocktail recipe so that I can filter out inappropriate content [#29](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44339868)
* View Site 
  * As a User I can view a home page so that I know what is the site purpose [#30](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44340072)
* Unregistered User 
  * As a User I can see cocktail images, likes, read cocktail description so that Icould register to site to view cocktail recipes details [#31](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44340298)
* Register an Account 
  * As a User I can register an account so that I can view recipe detail, like, comment the cocktail recipe [#32](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44340505)
* Login/ Logout 
  * As a User I can login so that I can have access to full site [#33](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44340823)
* View Cocktail Recipe 
  * As a User I can click on get the cocktail so that I can view cocktail recipe detail [#34](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44340975)
* View Likes 
  * As a User I can view list of cocktails with number of likes so that I can see what cocktail is most liked [#35](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44341438)
* Like/ Unlike Cocktail Recipe 
  * As a User I can like/unlike cocktail recipe so that I can interact with the site content [#36](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44341656)
* Read Comments 
  * As a User I can view comments so that I can read the conversation [#37](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44341985)
* Comment Cocktail Recipe
  * As a User I can comment a cocktail recipe so thet I can interact with the others users in recipe detail page [#38](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44342238)  
* CRUD 
  * As a User I can CRUD so that I can manage my cocktail recipes [#39](https://github.com/users/Indrakens/projects/22/views/1?pane=issue&itemId=44342407)
# SCOPE
The goal of the project is to create a cocktail recipe website. To provide users to find an ideal cocktail recipe for them and inspire them to create their own cocktail recipe and share it with other users. Allow logged-in users to have full CRUD functionality for their own  cocktail recipes and share their cocktail recipes with other users. Allow logged-in users to comment on a cocktail recipe to share their mixology skills with other users. The logged-in users have the opportunity to start practicing these cocktail recipes and share their experience making them with others. As the front-end users, the site Admin has full CRUD functionality in Django Admin panel. 
* User - can view site content, register an account, log-in and log-out
* Cocktail Recipes - log-in user can create, edit, delete it's own recipe
* Other Cocktail Recipes - log-in user can read, like/unlike, and comment recipe
# FEATURES
### Home Page 
* A welcoming homepage where users can register, and see cocktail recipe images with descriptions, created-on, number of likes, and login button (add image and mobile image)
* Logged in user Home page (add image, mobile image)
### Navigation Bar
* The navigation bar appears top of the page
(add image, mobile image)
* The website Logo links users to Home page (add image and mobile image)
* Logged in user Nav bar (add image, mobile image)
### Footer
* Footer with links to direct user to Facebook, Instagram, Twiter (add image and mobile image)
### Register 
* Users can register an account by entering Username, Email (optional), Password
* Users who have already registered can click on Log In link, redirects to Log In page (add image and mobile image, message image)
### Log In
* Users can login by entering Username and Password
* Users who haven't already registered can click on Register link, redirects to Register page (add image and mobile image, message image)
### Log Out
* Users can Log Out by clicking on Logout link top of the page
* Users can click on Log Out button, to log-out from site, or Exit link whitch redirects to home page(add image, mobile image)
### Cocktail Recipe Detail
* Recipe detail page have access only logged in users
* Users can clikc on Get The cocktail link to view recipe details, redirects to cocktail recipe detail
* Users can click on heart icon to like recipe
### Comment Recipe
* Comment recipe have acces only logged in users
* Users can write comments in comment form on cocktail recipe detail page
* After submission a success message displays
* The comment does not appear until the admin approves the comment for publication (add image, mobile image, message image)
### Add Cocktail Form
* Users can click on Add Cocktail in top of the page
* Provides a form to submit fields to complete to add cocktail recipes to the public and for CRUD functionality
* The placeholder image is available if the user has not supplied a cocktail image(add images, mobile image)
### Update Cocktail Recipe
* Update cocktail recipe is available for logged in users
* Clicking on Edit button belove cocktail image, user is able to update cocktail recipe
### Delete Cocktail Recipe
* Delete cocktail recipe is available to logged in users
* Clicking on Delete button belove cocktail image, user is redirected to Delete Cocktail page
### 403 Error
* Users not able to update other user cocktail recipes, redirects to 403 page
* Users not able to delete other user cocktail recipes, redirects to 403 page (add images)
### 404 Error
* Page not found (add images)
### 500 Error
* Internal server error (add images)
# TESTING
Full testing can be seen [TESTING.md]() file.
#
# TEHNOLOGY USED
#### [HTML](https://en.wikipedia.org/wiki/HTML) - Used to build the front-end website
#### [CSS](https://en.wikipedia.org/wiki/CSS) - Used to style the HTML
#### [JavaScript](https://www.javascript.com/) - Used to add timeout function for messages
#### [Python](https://www.python.org/) - Used as the back-end programming language
#### [Django](https://www.djangoproject.com/) - Used as the Python framework for the website. 
#### [Bootstrap](https://getbootstrap.com/) - Used as the front-end framework for responsiveness and pre-built components
#### [Git](https://git-scm.com/) - Used for version control
#### [GitHub](https://github.com/) - Used for online code storage
#### [GitPod](https://www.gitpod.io/) - Used as a cloud-based IDE for development
#### [ElephantSQL](https://customer.elephantsql.com/login) - Used as the Postgres database 
#### [Heroku](https://id.heroku.com/) - Used for cloud based platform for deployment
#### [Cloudinary](https://cloudinary.com/) - Used for host static files 
#### [Gunicorn](https://gunicorn.org/) - Used as a website server provider
#### [Psycopg2](https://pypi.org/project/psycopg2/) - Used as a postgres database adapter
#
# DEPLOYMENT
* Sign-up / Log-in to [Heroku](https://id.heroku.com/login)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name (app name must be unique) and select a suitable region, then select create app
* Heroku will create the app and bring you to the deploy tab
* From the submenu at the top, navigate to the resources tab 
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Click on the setting tab
* Open the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration
* In the Django app repository create a new file called env.py
* Within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku
* The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* Insert the line if os.path.isfile("env.py"): import env
* Remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* Replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* In the env.py file add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* This key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it
* In the settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors
* Heroku will now build the app for you
* Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site
# FORKING AND CLONING
### Forking the repository
By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
* Logging into GitHub or create an account
* Locate the repository [https://github.com/Indrakens/cocktail-heaven](https://github.com/Indrakens/cocktail-heaven)
* At the top of the repository, on the right side of the page, select "Fork" from the buttons available
* A copy of the repository should now be created in your own repository
### Create a clone of repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally
* Navigate to [https://github.com/Indrakens/cocktail-heaven](https://github.com/Indrakens/cocktail-heaven)
* Click on the arrow on the green code button at the top of the list of files
* Select the clone by https option and copy the URL it provides to the clipboard
* Navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to
* Type 'git clone' and paste the https link you copied from github
* Press enter and git will clone the repository to your local machine 
# CONTENT AND RESOURCES
### Django Documentation
* Read through the django documentation multiple times
* Used extensively during development of this project
### W3 Schools
* Used for reference throughout for css examples
### Code Institute
* The Code Institute reference material was used as a general reference for things that I had previously done during the course
* Course content for portfolio project 4 helped able to complete this project
# ACKNOWLEDGMENT
* Graeme Taylor - my mentor who provided me with great feedback and guidance at the inception of this projec
* Alan Bushell - our teacher, always a great mentor during stand-up. And who helped insure me to get true this project
* To all the tutors in Code Institute