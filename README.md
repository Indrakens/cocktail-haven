# COCKTAIL | HEAVEN
Website designed to provide users learn and try cocktail recipes. Users can register to the site and once logged in they have access to all the site features. Registered users can create their own cocktail recipes and share their cocktail recipes with other users. Also can update or delete their own cocktail recipe. Users can like/ unlike cocktail recipes and also be involved in conversations related to chosen cocktail recipes by commenting on them. 
#
![Screenshot 2024-02-28 131824](https://github.com/Indrakens/cocktail-heaven/assets/127971416/3a057369-5999-4d0e-aa3a-dabe95d9ed5d)

#### The website was deployed via Heroku - the live site can be found here - [COCKTAIL | HEAVEN](https://cocktailheaven-c43cabf55fb3.herokuapp.com/) 

## TABLE OF CONTENT
* [UX](https://github.com/Indrakens/cocktail-heaven#ux)
* [UX DESIGN](https://github.com/Indrakens/cocktail-heaven#ux-design)
  * [Color Scheme](https://github.com/Indrakens/cocktail-heaven#color-scheme)
  * [Fonts](https://github.com/Indrakens/cocktail-heaven#fonts)
  * [Images](https://github.com/Indrakens/cocktail-heaven#images)
  * [Icons](https://github.com/Indrakens/cocktail-heaven#icons)
* [DATABASE MODEL](https://github.com/Indrakens/cocktail-heaven#database-model)  
* [Wireframe](https://github.com/Indrakens/cocktail-heaven#wireframe)
* [AGILE](https://github.com/Indrakens/cocktail-heaven#agile)  
* [EPICS](https://github.com/Indrakens/cocktail-heaven#epics)
* [USER STORIES](https://github.com/Indrakens/cocktail-heaven#user-stories)
* [SCOPE](https://github.com/Indrakens/cocktail-heaven#scope)
  * [FUTURE TO IMPLEMENT](https://github.com/Indrakens/cocktail-heaven/tree/main#future-to-implement)
* [FEATURES](https://github.com/Indrakens/cocktail-heaven#features)
  * [WEB](https://github.com/Indrakens/cocktail-heaven#web)
  * [PHONE](https://github.com/Indrakens/cocktail-heaven#phone)
* [ALERT AND SUCCESS MESSAGES ](https://github.com/Indrakens/cocktail-heaven#alert-and-success-messages)
* [TESTING](https://github.com/Indrakens/cocktail-heaven#testing)
* [TEHNOLOGY USED](https://github.com/Indrakens/cocktail-heaven#tehnology-used)
* [DEPLOYMENT](https://github.com/Indrakens/cocktail-heaven#deployment)
* [FORKING AND CLONING](https://github.com/Indrakens/cocktail-heaven#forking-and-cloning)
* [CREDITS](https://github.com/Indrakens/cocktail-heaven#credits)
* [CONTENT AND RESOURCES](https://github.com/Indrakens/cocktail-heaven#content-and-resources)
* [BUGS](https://github.com/Indrakens/cocktail-heaven/tree/main#bugs)
  * [UNFIXED BUG](https://github.com/Indrakens/cocktail-heaven#unfixed-bug)
* [ACKNOWLEDGMENT](https://github.com/Indrakens/cocktail-heaven#acknowledgment)    
# UX
## UX DESIGN 
### Color Scheme
|     |        |
|----|------|
| Color Palette [COOLORS](https://coolors.co/) | ![color palette](https://github.com/Indrakens/heaven1/assets/127971416/3fc6e434-d333-4f46-b278-37251a853f40)|
### Fonts
* The website uses ['UBUNTU'](https://fonts.google.com/?query=ubuntu) and ['LATO'](https://fonts.google.com/?query=lato) fonts from [Google Fonts](https://fonts.google.com/?query=lato) .
### Images
|          |          |
|-------|-------|
| Logo image was searched and saved in file [LOGO IMAGE](https://www.google.com/search?q=cocktail+logo&tbm=isch&ved=2ahUKEwi67K6yjNGCAxWtXUEAHcJxArgQ2-cCegQIABAA&oq=cocktail+logo&gs_lcp=CgNpbWcQARgAMgQIIxAnMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgoIABCABBCKBRBDOgYIABAHEB5Q-xBYjB5gtjFoAHAAeACAAZIBiAHzBJIBAzcuMpgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=IopaZbrTOa27hbIPwuOJwAs&bih=923&biw=1903&hl=en#imgrc=VZcki_BNEoSS1M)| ![logo](https://github.com/Indrakens/cocktail-heaven/assets/127971416/22299728-e65c-4e7e-a2f7-fc6bab350f60)|
| Header image was searched and saved in file [HEADER IMAGE]( https://www.google.com/search?q=cocktails+green&tbm=isch&ved=2ahUKEwik5765iNGCAxXMTkEAHWwLDkcQ2-cCegQIABAA&oq=cocktails&gs_lcp=CgNpbWcQARgBMgQIIxAnMgQIIxAnMgoIABCABBCKBRBDMgoIABCABBCKBRBDMgoIABCABBCKBRBDMgoIABCABBCKBRBDMgoIABCABBCKBRBDMgUIABCABDIKCAAQgAQQigUQQzIKCAAQgAQQigUQQ1AAWABg5A9oAHAAeACAATmIATmSAQExmAEAqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=AIZaZaTnCMydhbIP7Ja4uAQ&bih=923&biw=1920#imgrc=LVQx2cFOvohiSM )| ![Green-Cocktail](https://github.com/Indrakens/heaven1/assets/127971416/baab3fcc-c011-4001-aec9-c647fa826f0a)|
| Placeholder image was searched and saved in file - [PLACEHOLDER IMAGE](https://www.google.com/search?q=cocktails+green+vector+logo&tbm=isch&ved=2ahUKEwjy4LadidGCAxWmXEEAHasFB_MQ2-cCegQIABAA&oq=cocktails+green+vector+logo&gs_lcp=CgNpbWcQAzoECCMQJ1ChDlj9I2C5KGgAcAB4AIABjwKIAbwGkgEFNC4wLjKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=0YZaZbK0LKa5hbIPq4ucmA8&bih=923&biw=1920#imgrc=30DceCdjDVQoDM)| ![lime-cocktail](https://github.com/Indrakens/cocktail-heaven/assets/127971416/021a185a-1582-4acb-bba4-1f0ee7d3dc8c)|
### Icons
  * The website uses [Font Awesome]( https://fontawesome.com/ ) icons for comment icon, heart icon, social media icons.
# DATABASE MODEL
|         |      |
|-------|-------|
| Recipe and Comment Database Model| ![IMG_1422](https://github.com/Indrakens/heaven1/assets/127971416/9766fef9-43a6-4ece-bd1c-558092b6703c)|  
# WIREFRAME
## Home 
|                   |                |
|----------|---------|
| Unregistered User Home Page| ![New Wireframe 1](https://github.com/Indrakens/heaven1/assets/127971416/cfa036c6-79e8-4a12-81a7-86ce93f4265e)|
| Login User Home Page - The user can see the update and delete buttons below their added cocktail recipe| ![login (1)](https://github.com/Indrakens/heaven1/assets/127971416/5acb2e13-5d02-4633-b2c7-cdb3a448c5d4)|
## Register / LogIn
|              |              |
|---------|---------|
| Register Account  | ![register](https://github.com/Indrakens/heaven1/assets/127971416/cb5183ce-5d40-4c42-b077-42a455b696d2)|
| LogIn    | ![login](https://github.com/Indrakens/heaven1/assets/127971416/460373ff-b6a4-447b-9003-a223e4a9c470)|
## Recipe Page
|        |       |
|-------|----------|
| Cocktail Recipe Detail Page | ![recipe detail](https://github.com/Indrakens/heaven1/assets/127971416/b095094a-d8ab-4bda-b089-2520d054aad6)|
## Add Cocktail
|         |         |
|------|--------|
| Add Cocktail  | ![add1234 (1)](https://github.com/Indrakens/heaven1/assets/127971416/96264b14-fd33-4fa5-a968-648e7271df53)|
## Update / Delete
|        |         |
|--------|---------|
| Update Cocktail | ![update cocktail](https://github.com/Indrakens/heaven1/assets/127971416/944ec674-5b7a-45b6-a24e-922ff8ce4851)|
| Delete Cocktail | ![delete](https://github.com/Indrakens/heaven1/assets/127971416/3bd0ca0b-16b6-421d-9d9a-79589695f366)| 
# AGILE
The Agile methodology was used to plan the project. Each user story was linked to an Epic. Issues were used to create Epics and User Stories with a custom template. Once work on the website story was complete, the user story was moved into the "Done" column.
## EPICS
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
The goal of the project is to create a cocktail recipe website. To provide users to find an ideal cocktail recipe for them and inspire them to create their own recipes and share them with other users. Allow logged-in users to have full CRUD functionality. Logged-in users can like, and comment on a cocktail recipe, and share their mixology skills with other users. As the front-end users, the site Admin has full CRUD functionality in the Django Admin panel.
* User - can view site content, register an account, log-in and log-out
* Cocktail Recipes - log-in user can create, edit, delete it's own recipe
* Other Cocktail Recipes - log-in user can read, like/unlike, and comment recipe
## FUTURE TO IMPLEMENT
* Improvement could be made to create a page where users could delete their accounts. At the moment only Admin in the admin panel can delete the users.
# FEATURES
## WEB
### Home Page 
|           |              |
|------|-------|
| Welcoming Header | ![IMG_1260](https://github.com/Indrakens/heaven1/assets/127971416/4cf59f1e-c5bb-4392-9385-a47129a483c5)|
| Displays cocktail images, cocktail description, created-on and number of likes. Users can Login or Register by clickin on links to get recipe | ![IMG_1264](https://github.com/Indrakens/heaven1/assets/127971416/4539a57b-630d-4813-af3d-0d3e749ea3ab)|
| LogIn User - Welcoming Header | ![IMG_1265](https://github.com/Indrakens/heaven1/assets/127971416/a9da2687-c69f-4096-819b-32ba3ef0a6cb)|
| LogIn User - displays cocktail image, cocktail description, link to get cocktail recipe, created-on, number of likes | ![IMG_1397](https://github.com/Indrakens/heaven1/assets/127971416/2bfe83f6-f949-49ad-85ac-bd8879391176)|
### Update / Delete Buttons
* Update and delete buttons ar visible only for your own added cocktail recipe 

|        |        |
|-------|-------|
| Appears below cocktail image, deskription and link - get the (cocktail name)| ![IMG_1413](https://github.com/Indrakens/heaven1/assets/127971416/ffcc2254-65ce-45d0-ba5c-755c16c3b4f2)|
### Navigation Bar
* The navigation bar appears top of the page

|      |       |
|-------|---------|
| Nav Bar | ![E8B31B85-81D6-4CCE-98DE-B86A24EC4CA0](https://github.com/Indrakens/heaven1/assets/127971416/65825968-6698-4405-8471-fbb521fde479)|
| LogIn User - Nav Bar | ![46D0A134-400E-4D13-ADB3-32CCF9CB34EB](https://github.com/Indrakens/heaven1/assets/127971416/c4ad9e19-632f-48db-aaff-3350859b9b69)|
| Logo redirects User to Home page | ![l1](https://github.com/Indrakens/heaven1/assets/127971416/512f33b9-e044-4068-9c06-8b24116e2d8c)|
### Register 
* Users can register an account by entering
* Username, Email (optional), Password
* Users who have already registered can click on  
* Log In link, redirects to Log In page

|        |        |
|------|-------|
| Register an Account | ![IMG_1284](https://github.com/Indrakens/heaven1/assets/127971416/c2fc4d04-8878-46f3-a08a-4cf72c925980)|
### Log In
* Users who haven't already registered can click on Register link 
* Register link, redirects to Register page 

|      |       |
|------|------|
| Log In | ![IMG_1285](https://github.com/Indrakens/heaven1/assets/127971416/f862698d-58be-4973-952a-9db18dcb7dd7)|
### Log Out
* To log-out click on Log Out button
* Exit log-out page click on Exit link, redirects to homepage

|      |      |
|------|------|
| Log Out | ![IMG_1286](https://github.com/Indrakens/heaven1/assets/127971416/c20f8bdc-4e27-475b-8f96-0cb7f1d1dc40)|
### Cocktail Recipe Detail
* Recipe detail page have access only logged in users
* Users can clikc on Get The cocktail link to view recipe details, redirects to cocktail recipe detail page
* Users can click on heart icon to like recipe, view recipe details, see number of likes and number of comments

|         |        |
|------|------|
| Cocktail recipe detail page | ![IMG_1287](https://github.com/Indrakens/heaven1/assets/127971416/1ebbb788-d845-4cf4-8137-63e2d7245d89)|
### Comment Recipe
* Comment recipe have acces only logged in users
* Users can write comments in cocktail recipe detail page 
* After submission a success message displays 
* The comment does not appear until the admin approves the comment for publication

|       |        |
|------|------|
| Approved comments appears left side | ![IMG_1288](https://github.com/Indrakens/heaven1/assets/127971416/dd8fa8c9-b890-41aa-b25c-7e55d6e6a4b3)|
### Add Cocktail 
* Users can click on Add Cocktail in top of the page
* Provides a form to submit fields to complete to add cocktail recipes to the public and for CRUD functionality
* The placeholder image is available if the user has not supplied a cocktail image

|     |       |
|-----|------|
| Add Cocktail | ![IMG_1401](https://github.com/Indrakens/heaven1/assets/127971416/06029f9b-eedc-4a99-8e82-7ac23db1a5c9)|
### Update Cocktail Recipe
* Update cocktail recipe is available for logged in users
* Clicking on Update button user is able to update cocktail recipe

|      |      |
|-----|------|
| Update Cocktail | ![IMG_1402](https://github.com/Indrakens/heaven1/assets/127971416/4019952e-a795-4659-bc3d-ed6e5ab2f347)|
### Delete Cocktail Recipe
* Delete cocktail recipe is available to logged in users
* Clicking on Delete button belove cocktail image, user is redirected to Delete Cocktail page
* To delete recipe click on delete button
* To exit click on Exit link, redirects to home page

|       |      |
|-----|-----|
| Delete Cocktail | ![IMG_1292](https://github.com/Indrakens/heaven1/assets/127971416/189ab783-41ea-4123-885d-5b934202a495)|
### Error Handlers
|       |       |
|------|-------|
| The 404 code means that a server could not find a client-requested webpage. | ![IMG_1365](https://github.com/Indrakens/heaven1/assets/127971416/91f2f123-0b03-4451-98f3-4310ecdbbd9e)|
| The HTTP status code 500 is a generic error response. It means that the server encountered an unexpected condition that prevented it from fulfilling the request.| ![IMG_1363](https://github.com/Indrakens/heaven1/assets/127971416/6570abca-ea4e-4e90-8a7a-0361151d2b47)|
| The 403 Forbidden error indicates that the server understands the request but can't provide additional access. This means that the web page you're trying to open in your browser is a resource that you're not allowed to access.| ![IMG_1368](https://github.com/Indrakens/heaven1/assets/127971416/0443a695-5fcd-416b-8aa3-9e4fe847dbbd)|
### Footer
* Footer is displayed in the bottom of the page
* Includes social media links: Facebook, Instagram, Twiter 

|      |       |
|------|------|
| Footer | ![footer](https://github.com/Indrakens/heaven1/assets/127971416/b31ce067-fc17-43aa-9211-fe9f83d93086)|
## PHONE
### HOME
|       |        |
|------|--------|
| Welcoming Header | ![IMG_1300](https://github.com/Indrakens/heaven1/assets/127971416/3686c975-5b19-41fb-a23d-c479394d41ea)|
| Displays cocktail images, cocktail description, created-on and number of likes. Users can Login or Register by clickin on links to get recipe | ![IMG_1305](https://github.com/Indrakens/heaven1/assets/127971416/6c745aad-3fe8-4fee-a57d-22b6a16df04c)|
| LogIn User - Welcoming Header | ![IMG_1301](https://github.com/Indrakens/heaven1/assets/127971416/4419af72-9040-49cd-afb1-068ebb470a2c)|
| LogIn User - displays cocktail image, cocktail description, link to get cocktail recipe, created-on, number of likes | ![IMG_1414](https://github.com/Indrakens/heaven1/assets/127971416/5e42f641-8a6d-4c05-b709-9b8492cf8b5b)| 
### Navigation Bar 
|      |       |
|------|-------|
| Nav | ![IMG_1302](https://github.com/Indrakens/heaven1/assets/127971416/99f66968-02a0-4aa0-b638-be1c79c3fd3d)|
| Nav Menu | ![IMG_1303](https://github.com/Indrakens/heaven1/assets/127971416/4d83fb42-6327-4753-80b6-4297d82587a0)|
| Nav Menu - LogIn User | ![IMG_1304](https://github.com/Indrakens/heaven1/assets/127971416/139c3e13-4a5c-4919-a4a3-ed0abc427661)|
### Register
|     |     |
|---|---|
| Register an Account | ![IMG_1307](https://github.com/Indrakens/heaven1/assets/127971416/f3c3346a-374c-4d36-9843-022194f3258a)|
### LogIn
|      |       |
|-----|------|
| Log In | ![IMG_1308](https://github.com/Indrakens/heaven1/assets/127971416/4ff983d3-334b-4583-a2f0-96199ad2fd67)|
### LogOut
|      |       |
|-----|-----|
| Log Out | ![IMG_1309](https://github.com/Indrakens/heaven1/assets/127971416/a2d182a9-1d6c-4f53-88a9-fca210ada7f6)|
### Cocktail Recipe Detail
|     |       |
|------|------|
| Recipe Detail Page | ![IMG_1310](https://github.com/Indrakens/heaven1/assets/127971416/cbc69d4d-83a0-4cae-bebf-7d3790ff38ec)|
### Comment Recipe
|      |      |
|------|-------|
| Comments and comment body displays under cocktail recipe details in recipe detail page | ![IMG_1311](https://github.com/Indrakens/heaven1/assets/127971416/b35bb7c6-3eea-4e1c-b787-6cc9aca4fe46)|
### Add Cocktail 
|      |       |
|------|-------|
| Add Cocktail | ![IMG_1404](https://github.com/Indrakens/heaven1/assets/127971416/88314cde-f2f0-48e0-83b7-005f8d55d7b4)|
| Continues under Ingredients | ![IMG_1313](https://github.com/Indrakens/heaven1/assets/127971416/ab5ed744-fbc2-4591-958d-baad0203bce4)|
### Update Cocktail Recipe
|      |       |
|------|------|
| Update Cocktail | ![IMG_1407](https://github.com/Indrakens/heaven1/assets/127971416/41ecc8da-5d14-46a3-adf1-b99223e9f1dc)|
| Continues under Ingredients | ![IMG_1316](https://github.com/Indrakens/heaven1/assets/127971416/f0c52025-0061-4684-b206-e33495b67901)|
### Delete Cocktail Recipe
|       |     |
|-------|-------|
| Delete Cocktail | ![IMG_1317](https://github.com/Indrakens/heaven1/assets/127971416/31c5d7e9-0f91-4a9a-8783-f2d9a5e8e990)|
### Forbidden Access
|    |      |
|------|-------|
| Forbidden Access | ![IMG_1369](https://github.com/Indrakens/heaven1/assets/127971416/2bdd0f0c-ccae-4a91-96ba-3aa2178a0f9f)|
### Error Handlers
|       |        |
|------|------|
| 404 | ![IMG_1366](https://github.com/Indrakens/heaven1/assets/127971416/e26eaf6c-0841-42b9-8c71-35e11ea81fb4)|
| 500 | ![IMG_1364](https://github.com/Indrakens/heaven1/assets/127971416/10f66ac8-5f69-41fd-afc6-dce491c5e793)|
### Footer
|      |     |
|-----|-----|
| Footer | ![f](https://github.com/Indrakens/heaven1/assets/127971416/4cd4ad4d-790f-4444-a622-22a5a372a474)|
# ALERT AND SUCCESS MESSAGES 
|            |         |
|-------|-------|
| Registered - displays top of the page | ![IMG_1322](https://github.com/Indrakens/heaven1/assets/127971416/413dd739-ba46-495a-b2e8-82d937621d74)|
| Register - paswor too similar to the user name and too short | ![IMG_1328](https://github.com/Indrakens/heaven1/assets/127971416/e717f3c2-95dd-4a00-8ddb-1f5deac6f3a0)|
|Register - must type same pasword again | ![IMG_1329](https://github.com/Indrakens/heaven1/assets/127971416/c14c4cda-3754-466a-a917-3dea3ed2e70b)| 
| Register - already existing username | ![IMG_1330](https://github.com/Indrakens/heaven1/assets/127971416/c79114d8-9839-4e42-b392-8750fea60614)|
| LogIn - displays top of the page | ![IMG_1327](https://github.com/Indrakens/heaven1/assets/127971416/6c224ec5-21af-412c-baa2-952d80c9d809)|
| Log In - username or pasword are not correct | ![IMG_1318](https://github.com/Indrakens/heaven1/assets/127971416/e9c80d68-95af-4d30-8012-4d5c422b99e0)|
| Log Out - displays top of the page | ![IMG_1324](https://github.com/Indrakens/heaven1/assets/127971416/4958ac9e-f903-45d6-8c42-b4831d808180)|
| Add Cocktail - displays top of the page |![IMG_1331](https://github.com/Indrakens/heaven1/assets/127971416/4fed4a31-6646-4cd0-b2c1-538cff8f935b)|
| Update Cocktail - displays top of the page | ![IMG_1332](https://github.com/Indrakens/heaven1/assets/127971416/799e4f3e-00a0-41ef-9709-40464395647b)|
|  Comment approval message - displays bottom of tha page | ![IMG_1333](https://github.com/Indrakens/heaven1/assets/127971416/1e102359-aadd-4959-b691-f0f0c02e0fab)|
# TESTING
Full testing can be seen [TESTING.md](https://github.com/Indrakens/cocktail-heaven/blob/main/TESTING.md) file.
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
# CREDITS
* Cocktail Images - was downloaded from [good houskeeping](https://www.goodhousekeeping.com/) website
* Cocktail Recipes - was taken from [good houskeepeing](https://www.goodhousekeeping.com/) website
# CONTENT AND RESOURCES
### Django Documentation
* Read through the django documentation multiple times
* Used extensively during development of this project
### W3 Schools
* Used for reference throughout for css examples
### Code Institute
* The Code Institute reference material was used as a general reference for things that I had previously done during the course
* Course content for portfolio project 4 helped able to complete this project 
# BUGS
* I wasn't able to check python testing in terminal, didn't show any testing.py files. I had to add code in settings.py.

|        |        |
|--------|--------|
| import sys | ![IMG_1348](https://github.com/Indrakens/heaven1/assets/127971416/7313ab3e-62b1-4cf8-a156-0383ac61b806)|
| add if statement to DATABASES | ![IMG_1351](https://github.com/Indrakens/heaven1/assets/127971416/6034d4be-6d57-4a31-9087-17f29ae54f09)|
* I was making changes in recipe models for serving and time. I changed CharField to IntegerField for serving and time. After those changes I wasn't able to migrate and website wasn't working. To fix it I reset Database and create new superuser. Steps to reset Database:

|           |            |
|-------|-------|
| 1. | Delete the db.sqlite3 file. If this file contains important data, you might want to settle a backup for those|
| 2. | In ElephantSQL, in the Details dashboard, click on the ‘Reset’ button|
| 3. |  Delete all the migrations files inside the migration folder of all the Django applications (EXCEPT for **init.py** file, this is important)|
| 4. |  Make migrations again|
| 5. | Create a new superuser|
#### Website stopped working and had an error - NoReversMatch at /.
Reverse for 'recipe' with arguments '(",)' not found. I had to add extra code in my models.py file under display total number of likes
|        |         |
|--------|--------|
| Added code |![IMG_1393](https://github.com/Indrakens/heaven1/assets/127971416/1d98fe92-e1b7-4628-8cb8-78a7e56b4825)| 
#### The website had an error while trying to add and update the cocktail recipe. In models.py file imported RegexValidator and for name in Recipe model added validator to prevent the 500 error. For slug in Recipe model removed unique=True and added blank=True to prevent an error.
|        |         |
|------|-------|
| Changed code in Recipe model for name and slug | <img width="447" alt="Screenshot 2024-02-27 224213" src="https://github.com/Indrakens/cocktail-heaven/assets/127971416/56be8cd8-bdb5-4f24-924a-6ce8dff76c49">|
## UNFIXED BUG
* The alert messige after deleting cocktail recipe does not appear so I had to remove it. Was working before and not anymore. Wasnt able to fix it.

|     |     |
|------|------|
| Code before | ![IMG_1420](https://github.com/Indrakens/heaven1/assets/127971416/d57668b1-af78-4227-9950-7e72622adbed)|
| Code after removing success message | ![IMG_1421](https://github.com/Indrakens/heaven1/assets/127971416/b670b248-6326-4e7f-8333-8260b99ee222)|
# ACKNOWLEDGMENT
* Graeme Taylor - my mentor who provided me with great feedback and guidance at the inception of this projec
* Alan Bushell - our teacher, always a great mentor during stand-up. And who helped insure me to get true this project
* To all the tutors in Code Institute