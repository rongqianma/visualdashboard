# Visualization keywords in Humanities Journal Articles

Temporarily hosted on - https://visualdashboard-40qr.onrender.com/


### Components

- Github repository that is set to public
- Free Render account - (Render)[https://dashboard.render.com/]

## How to connect Github repository to Render

- Make sure you have all the files, and the directory structure of this repo
- Open the Render dashboard, and create a New Web Service
- Select Build & Deploy from a Git repository
- Either connect to your Github account and select the repo, or link it to a public repository like this one
- Give your web service a unique name
- Change the start command to - "gunicorn --chdir src app:server"
- Choose create web service, and your dash app is now hosted on a Free Tier Render Service

## How to make changes to the dashboard?

- Edit the files in the repository as needed.
- Once the edits are made, navigate to your webservice on the Render dashboard
- Select the option to "Manually deploy the latest commit"
