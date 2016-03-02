#Catalog
This project is part of Udacity course. You can create catalog locally by using this project.

## Requirements
You need Python version 2.7.6 or up, pip, Google account and Facebook account. Other requirements will be included in next section.

## Installation

1. Download the repository.
2. Install necessary packages by running command "pip install -r requirements.txt".
3. Create Google project in next steps to make use of Google's OAuth API.
- Create new project on https://console.developers.google.com/.
- In API Manager section, on Credentials tab select OAuth consent screen, type product name and then save.
- Now you can create OAuth client ID credentials.
  - Choose Web Application as Application type.
  - Your app name.
  - In Authorized Javascript origins add "http://127.0.0.1:5000".
  - In Authorized redirect URIs add "http://127.0.0.1:5000/auth/oauth2callback".
- You should have now client id and secret. Type id and secret to client_secrets.json file in specified locations.
- Also find login.html file which is located in templates directory. Type client id to specified location on 36th line.
4. Now set up Facebook app in steps below.
- Add a new web app on https://developers.facebook.com/ and create app ID.
- As Site URL type http://localhost:5000/.
- Go to Settings->Advanced, find Valid OAuth redirect URIs and add "http://localhost:5000/" there.
- Go to Dashboard and get App ID and App Secret. Type them now to fb_client_secrets.json file in specified locations.
- Also write App ID to earlier mentioned login.html file on line 86 in specified location.
5. Run project by executing command "python project.py" in working directory and access "http://127.0.01:5000" or "http://localhost:5000/" in browser.
