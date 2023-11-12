# COCKTAIL | HAVEN
Website designed to provide users learn and try cocktail recipes. Users can create their own cocktail recipes and share their cocktail creation skills with everybody.
[responsiv website image]
# UX
## Wireframe
[add wireframe images]
## Color Scheme
[add coclor cheme image]
## Typography
* Fonts
  * The website uses 'Ubuntu',sans-serif font from [Google Fonts]( https://fonts.google.com/?query=ubuntu ) and 'Lato',sans-serif font from [Google Fonts](https://fonts.google.com/?query=lato) .
* Images 
  * Cocktail images were searched and saved in file from [Google]( https://www.google.com/ ).
* Icons
  * The website uses [Font Awesome]( https://fontawesome.com/ ) icons for comment icon, heart icon, social media icons. 
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
# Features
## Home Page 
* A welcoming homepage where users can register, see cocktail recipe images with description, created-on, number of likes, login button. (add image)
* Logged in user Home page (add image)
## Navigation Bar
* The navigation bar appears top of the page.
(add image)
* The website Logo links users to Home page (add image)
* Logged in user Nav bar (add image)
## Footer
* Footer with links to direct user to Facebook, Instagram, Twiter (add image)
## Register 
* Users can register an account by entering Username, Email (optional), Password
* Users who have already registered can click on Log In link, redirects to Log In page (add image)
## Log In
* Users can login by entering Username and Password
* Users who haven't already registered can click on Register link, redirects to Register page (add image)