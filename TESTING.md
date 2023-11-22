# TABLE OF CONTENT
* [CI PYTHON LINTER](https://github.com/Indrakens/cocktail-heaven/blob/main/TESTING.md#ci-python-linter-pep8ci)
* [UNITTEST](https://github.com/Indrakens/cocktail-heaven/blob/main/TESTING.md#unittest)
* [CSS VALIDATION](https://github.com/Indrakens/cocktail-heaven/blob/main/TESTING.md#css-validation)
* [HTML VALIDATION](https://github.com/Indrakens/cocktail-heaven/blob/main/TESTING.md#html-validation)
* [JAVASCRIPT](https://github.com/Indrakens/cocktail-heaven/blob/main/TESTING.md#javascript)
* [MANUAL TESTING](https://github.com/Indrakens/cocktail-heaven/blob/main/TESTING.md#manual-testing)
* [GOOGLE LIGHTHOUSE TESTING](https://github.com/Indrakens/cocktail-heaven/blob/main/TESTING.md#google-lighthouse-testing)
* [CROSS-BROWSER COMPATIBILITY](https://github.com/Indrakens/cocktail-heaven/blob/main/TESTING.md#cross-browser-compatibility)
#
# CI PYTHON LINTER [pep8ci](https://pep8ci.herokuapp.com/)
|     FILE               |  RESULTS  |
|-------------|:-----:|
| cocktails2023/ urls.py | ![IMG_1230](https://github.com/Indrakens/UCD-resume/assets/127971416/736a64c8-b575-40ad-9dc9-73d83b6d5776)|
| cocktails2023 / views.py        | ![IMG_1231](https://github.com/Indrakens/UCD-resume/assets/127971416/3a358713-fdd4-43d5-9280-d279278bec21)|
| admin.py                        | ![IMG_1233](https://github.com/Indrakens/UCD-resume/assets/127971416/19a03123-b303-44c0-b14f-4868a89e8492)|
| models.py                      | ![IMG_1235](https://github.com/Indrakens/UCD-resume/assets/127971416/78e2310e-9ca7-44ea-a014-6883a48925dd)|
| forms.py                       | ![IMG_1229](https://github.com/Indrakens/UCD-resume/assets/127971416/e826f87a-58b6-415f-a40d-c35db2b7dc4a)|
| urls.py                        | ![IMG_1236](https://github.com/Indrakens/UCD-resume/assets/127971416/2c936669-1cc6-499d-b487-42b308b3d278)|
| views.py                       | ![IMG_1237](https://github.com/Indrakens/UCD-resume/assets/127971416/726d0671-eaad-4394-806a-3edf43a5bff8)|
| test_forms.py                  | ![IMG_1238](https://github.com/Indrakens/UCD-resume/assets/127971416/7ce3a19f-0606-47be-90f3-8056cbb4b995)|
| test_urls.py                   | ![IMG_1239](https://github.com/Indrakens/UCD-resume/assets/127971416/2ff8b943-b383-406b-8a26-6868fac3dc79)|
| test_views.py                  | ![IMG_1241](https://github.com/Indrakens/UCD-resume/assets/127971416/ee82d1ee-546e-4469-bc4f-76ce7b5ebb10)|
# UNITTEST
* Test Database

|                           |   |
|-------------|:-----:|
| Test database for alias 'default' | ![IMG_1242](https://github.com/Indrakens/UCD-resume/assets/127971416/0e579fd9-f08a-49bb-8590-61f2b7e40184)|
#

* Coverage Report

|       |      |
|------|-------|
| Coverage HTML | ![IMG_1355](https://github.com/Indrakens/heaven1/assets/127971416/630b7c11-aaa1-4d48-93d7-8539477c3083)|
# CSS VALIDATION
|       |        |
|-------|--------|
| [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) | ![IMG_1334](https://github.com/Indrakens/heaven1/assets/127971416/fbcf9edb-d5a5-4f89-8bf0-eebae95a3174)|
| Warnings | ![IMG_1337](https://github.com/Indrakens/heaven1/assets/127971416/3c1dfd39-31d1-4273-aaac-8895937ea658)|
# HTML VALIDATION
Due to the Django codes in templates, [W3C Markup Validation Service](https://validator.w3.org/) shows errors, for that reason only included base.html validator result
|        |        |
|------|--------|
| Warning | ![IMG_1342](https://github.com/Indrakens/heaven1/assets/127971416/d120595a-4563-4476-9436-8162f3af7308)|
| Errors | ![IMG_1343](https://github.com/Indrakens/heaven1/assets/127971416/0f9bfa77-0cd1-46b1-ac3d-5b4edd63bf5b)|
| Errors | ![IMG_1344](https://github.com/Indrakens/heaven1/assets/127971416/4965f7ee-2cc1-441b-98fe-832e8d9076c1)|
# JAVASCRIPT
|       |       |
|-----|------|
| [JSHint](https://jshint.com/) - javascript code is only in base.html page, setting timeaut for allert messages | ![IMG_1346](https://github.com/Indrakens/heaven1/assets/127971416/074186b2-b322-448c-9a55-495e336f7bc9)|
# MANUAL TESTING
### Account Registration
|     TEST                    |  RESULTS  |
|-------------|:-----:|
| User can create an account  |    PASS   |
| User can log-in             |    PASS   |
| User can log-out            |    PASS   |
### Navigation Unregistered User
|     TEST                                    |  RESULTS  |
|-------------|:-----:|
| User can navigate to home page              |    PASS   |
| User can navigate to register account page  |    PASS   |
| User can to  log-in page                    |    PASS   |
### Navigation LogIn User
|     TEST                               |  RESULTS  |
|-------------|:-----:|
| User can navigate to home page         |    PASS   |
| User can navigate to add cocktail page |    PASS   |
| User can navigate to log-out page      |    PASS   |
| SuperUser can access to admin panel    |    PASS   |
### LogIn User
|     TEST                                   |  RESULTS  |
|-------------|:-----:|
| User can add cocktail recipe               |    PASS   |
| User is redirected to Add Cocktail page    |    PASS   |
| User can edit cocktail recipe              |    PASS   |
| User is redirected to Update Cocktail page |    PASS   |
| User can delete cocktail recipe            |    PASS   |
| User is redirected to Delete Cocktail page |    PASS   |
| User can view cocktail recipe detail page  |    PASS   |
| User can like cocktail recipe              |    PASS   |
| User can comment cocktail recipe           |    PASS   |
### Admin
|     TEST                                                       |  RESULTS  |
|-------------|:-----:|
| Admin can add cocktail recipe in admin panel                   |    PASS   |
| Admin can change cocktail recipe in admin panel                |    PASS   |
| Admin can delete cocktail recipe in admin panel                |    PASS   |
| Admin can approve or delete user comments in admin panel       |    PASS   |
| Admin can view user details in admin panel                     |    PASS   |
| Admin can delete user with it's created recipes in admin panel |    PASS   |
### Error Handler
| TEST                                                                    | RESULTS |
|--------|---------|
| Forbidden Access - indicates that the server understands the request but can't provide additional access |  PASS  |
| 404 - page not found                                                    |  PASS  |
| 500 - internal server error                                             |  PASS  |
#
# GOOGLE LIGHTHOUSE TESTING

# CROSS-BROWSER COMPATIBILITY
|  TEST      |  RESULTS       |
|--------|---------|
| Google Chrome| PASS |
| Microsoft Edge  | PASS |
| Firefox        | PASS |
| Safari| PASS |
#