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
| cocktails2023/ urls.py | <img width="520" alt="Screenshot 2024-02-28 133337" src="https://github.com/Indrakens/cocktail-heaven/assets/127971416/c2b03165-f049-4a16-b224-1ded504612d6">|
| cocktails2023 / views.py        | <img width="516" alt="Screenshot 2024-02-28 133603" src="https://github.com/Indrakens/cocktail-heaven/assets/127971416/6e2c6e00-3d7c-46e1-a24f-7fbc444c8f65">|
| admin.py                        | <img width="534" alt="Screenshot 2024-02-28 133849" src="https://github.com/Indrakens/cocktail-heaven/assets/127971416/aff61a43-8b47-4447-9aca-16d02b718538">|
| models.py                      | <img width="536" alt="Screenshot 2024-02-27 225612" src="https://github.com/Indrakens/cocktail-heaven/assets/127971416/367f8bc7-251a-44d8-ae37-76d710c23af3">|
| forms.py                       | <img width="523" alt="Screenshot 2024-02-28 134104" src="https://github.com/Indrakens/cocktail-heaven/assets/127971416/e2c144d6-d604-45de-b9f2-d0eb27d029bb">|
| urls.py                        | <img width="540" alt="Screenshot 2024-02-28 134644" src="https://github.com/Indrakens/cocktail-heaven/assets/127971416/70fcc00d-98b8-4ce1-91b1-5bd4ab3032f6">|
| views.py                       | <img width="535" alt="Screenshot 2024-02-28 135129" src="https://github.com/Indrakens/cocktail-heaven/assets/127971416/07425a1d-d836-4346-9b24-273f32595730">|
| test_forms.py                  | <img width="549" alt="Screenshot 2024-02-28 135418" src="https://github.com/Indrakens/cocktail-heaven/assets/127971416/23a472a9-ecfa-4c42-86d7-ef83e6c0f785">|
| test_urls.py                   | <img width="537" alt="Screenshot 2024-02-28 135600" src="https://github.com/Indrakens/cocktail-heaven/assets/127971416/21c13eee-74ec-410a-a7de-a098aecf63f1">|
| test_views.py                  | <img width="541" alt="Screenshot 2024-02-28 135841" src="https://github.com/Indrakens/cocktail-heaven/assets/127971416/2b81993c-e695-43e9-8873-35296675010a">|
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
|        |         |
|---------|--------|
| Lighthouse Testing |![IMG_1357](https://github.com/Indrakens/heaven1/assets/127971416/caa671d2-49f1-4414-a15f-6687778bd019)|
# CROSS-BROWSER COMPATIBILITY
|  TEST      |  RESULTS       |
|--------|---------|
| Google Chrome| PASS |
| Microsoft Edge  | PASS |
| Firefox        | PASS |
| Safari| PASS |
#