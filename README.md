# Visualization Keywords in Humanities Journal Articles

Temporarily hosted on - [https://visualdashboard-40qr.onrender.com/](https://visualdashboard-40qr.onrender.com/)

## About the Application

The application primarily consists of 3 distinct pages:
- Home
- Dashboard
- Acknowledgement

One can make edits to these files by navigating to the `src/pages` directory.

### Dashboard

The dashboard consists of multiple elements:

1. Year Range Slider
2. Journal Drop-down
3. Keyword Drop-Down
4. Card 1-4
5. Graph 1
6. Graph 2
7. Data Table

**What is a callback?**  
Dash apps are made interactive through Dash Callbacks: chainable functions that are automatically called whenever a UI element is changed.

Callbacks have been defined for the following filter elements:

| Filter            | Description                                                                                                 | Interacts with       |
|--------------------|-------------------------------------------------------------------------------------------------------------|----------------------|
| Year Slider        | User can select a year range between 2008 and 2023.                                                        | Cards 1-4, Graph 1, Graph 2, Data Table |
| Journal Dropdown   | User can select one or more journals from the drop-down.                                                   | Cards 1-4, Graph 1, Graph 2, Data Table |
| Keyword Dropdown   | User can select one or more data visualization keywords from the drop down.                                | Graph 1, Graph 2, Data Table       |



# How to Host the Dash Application on Render?

### Components

- Github repository that is set to public
- Free Render account - [https://dashboard.render.com/](https://dashboard.render.com/)

## How to Connect Github Repository to Render

- Make sure you have all the files, and the directory structure of this repo
- Open the Render dashboard, and create a New Web Service
- Select Build & Deploy from a Git repository
- Either connect to your Github account and select the repo, or link it to a public repository like this one
- Give your web service a unique name
- Change the start command to - "gunicorn --chdir src app:server"
- Choose create web service, and your dash app is now hosted on a Free Tier Render Service

## How to Make Changes to the Dashboard?

- Edit the files in the repository as needed
- Once the edits are made, navigate to your webservice on the Render dashboard
- Select the option to "Manually deploy the latest commit"
