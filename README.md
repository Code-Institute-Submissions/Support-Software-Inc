# Support Software Inc

![PyPI - Django Version](https://img.shields.io/badge/Django-3.0.1-green)
![Build Status](https://travis-ci.org/Lowe54/Support-Software-Inc.svg?branch=master)

## Introduction

Welcome to the next generation in service desk software,

## Table of Contents

- [Support Software Inc](#support-software-inc)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [UX/UI Design](#uxui-design)
    - [Wireframes](#wireframes)
  - [User stories](#user-stories)
  - [Database Design](#database-design)
    - [Versions](#versions)
    - [Database Models](#database-models)
      - [User](#user)
      - [Organisation](#organisation)
      - [Tickets](#tickets)
      - [Comments](#comments)
      - [Purchase](#purchase)
      - [Ticket Files](#ticket-files)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
  - [Technology, Frameworks and Tools Used](#technology-frameworks-and-tools-used)
    - [Languages](#languages)
    - [Frameworks and Libaries](#frameworks-and-libaries)
    - [Tools](#tools)
  - [Github Branches](#github-branches)
    - [Master](#master)
    - [~~3.1-testing~~](#s31-testings)
    - [~~Organisation-module~~](#sorganisation-modules)
    - [Feature/Emails](#featureemails)
    - [Feature/user-import](#featureuser-import)
  - [Deployment](#deployment)
    - [IMPORTANT NOTICE](#important-notice)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Setting up Amazon Web Services (AWS)](#setting-up-amazon-web-services-aws)
  - [Testing](#testing)
    - [Credits](#credits)

## UX/UI Design

### Wireframes

The initial designs for this software can be found in the [Wireframes Folder](/wireframes), the desktop version of these were based off a full HD monitor with a resolution of 1920 x 1080px while the mobile designs were based off an iPhone X (375px x 812px Portrait) / (812px x 375px Landscape)

## User stories

| User story # | What am I looking for?                                                                                                             |
|--------------|------------------------------------------------------------------------------------------------------------------------------------|
| 1            | I am an end user who wants to be able to see all updates to a request                                                              |
| 2            | I am an employee who wants to be able to respond to requests without constantly being redirected to a seperate page                |
| 3            | I am an employee who wants to be able to search for a particular request, without having to go through each and every one          |
| 4            | I am an end user who wants to see all of my open requests, without having to select multiple filters                               |
| 5            | I am an end user who wants to be able to fix errors in my name or email, without having to contact the support company             |
| 6            | I am an end user who wants to be able to see all requests that need my reply, without having to filter all my requests             |
| 7            | I am an employee who wants to be able to associate multiple users to an organisation, without having to select each user each time |

## Database Design

### Versions

Version 1
![User Model v1](/wireframes/database_design_v1.png)

Version 2
![User Model v2](/wireframes/db_design_v2.png)

Version 3
![User Model v3](/wireframes/db_design_v3.png)

Version 4
![User Model v4](/wireframes/db_design_v4.png)

Version 5
![User Model v5](/wireframes/db_design_v5.png)

### Database Models

#### User

The user model extends the default Django User model with a profile picture, user role, their organisation,  if they are an organisation admin and if they can view all their organisations requests.

#### Organisation

The organisation model simply contains the organisations UUID (Universally Unique Identifier), along with the organisation name.

#### Tickets

The tickets table contains all the information relevent to a support request, including who raised the request, the date/time it was raised on, status, priority, any associated users (Who would recieve emails when the request was updated), along with closure details (If the request is closed).

#### Comments

The Comments table links users to various comments, as well as the type of comment (Public or Internal), the date and time the comment was posted, and the ticket the comment was posted on.

#### Purchase

#### Ticket Files

While this remains a feature to be implemented (See Upcoming features), it would link an uploaded file to a request, as well as the type and size of the uploaded file

## Features

### Existing Features

- Full login system
  - Users can register and login, as well as manage their account.
- Instant Commenting
  - User's aren't redirected to a seperate page to comment, it is all contained within the ticket page
- Organisation List
  - Admin's can manage organisations, associate and disassociate users all from one screen
- Result filtering
  - Users can filter their results by keyword, status, and priority

### Features Left to Implement

The following are lists of features that remain to be implemented, along with a brief description of what they entail.

- Emails
  - Email functionality including, but not limited to:
    - Sending registration emails
    - Ticket update emails
    - Broadcast emails sent by site admin(s)

- User Management
  - While this is currently possible from the admin site for individual users, this includes the following:
    - The ability for organisation admins to manage their organisation users
    - Import and Export of Users (Import functionality limited to administrators only)

## Technology, Frameworks and Tools Used

### Languages

- [HTML](https://www.w3.org/standards/webdesign/htmlcss)
- [CSS](https://www.w3.org/standards/webdesign/htmlcss#whatcss)
- [Python](https://www.python.org/)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### Frameworks and Libaries

- [JQuery](https://jquery.com)
  - The project uses **JQuery** to simplify DOM manipulation.
- [Django](https://www.djangoproject.com/)
  - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [FontAwesome](https://fontawesome.com/)
  - The project uses the free version of **FontAwesome** in order to add extra icons to the site
- [Popper JS](https://popper.js.org/)
  - Popper JS is used to position tooltips
- [Bootstrap](https://getbootstrap.com/)
  - Bootstrap is used for general grid layout + layout utilities
- [SASS](http://sass-lang.com/)
  - **SASS** was used to add extra functionality to CSS, it allows for nested statements to be used, which in turn made the files easier to read.

### Tools

- [DB Diagram](https://dbdiagram.io/home)
  - DB Diagram is a free tool that was used to design the database

## Github Branches

### Master

This branch contains the live version of the site.

### ~~3.1-testing~~

This Branch was created to test a minor Django version upgrade, it has been merged into the master branch

### ~~Organisation-module~~

This branch was created to test splitting the 'Organisation' Table into it's own module, which means that it would be seperate and able to have its own set of URL's, instead of sharing the Authentication ones. This branch has been merged into the master branch

### Feature/Emails

This branch contains future email functionality.

### Feature/user-import

This branch contains functionality that would allow an admin to import a csv file of users into the system.

## Deployment

### IMPORTANT NOTICE

These deployment steps are intented for a windows operating system, if your OS is different, please lookup the instructions for your OS

### Local Deployment

### Heroku Deployment

[AppOverview]: documentationImages/heroku/app_overview.png
[AppCreate]: documentationImages/heroku/app_create.png
[AppAutoDeploy]: documentationImages/heroku/app_automatic_deploy.png
[AppManualDeploy]: documentationImages/heroku/app-manual-deployment.png
[AppSettingsLink]: documentationImages/heroku/app_Settings_link.png
[AppConfigVars]: documentationImages/heroku/app_config_var_button.png

1) If you already have an heroku account, please go to step 4 after signing in
2) Go to [https://signup.heroku.com/](https://signup.heroku.com/)
3) Fill out the registration form
4) Once on the app overview (See below), click on 'New -> Create new app'
![AppOverview]

5) Enter an app-name and choose the region, then click on 'Create App'

![AppCreate]
<!-- markdownlint-disable MD029 -->
6) Now choose the deployment method, there are 3 options
<!-- markdownlint-enable-->
  a) Heroku CLI (Command Line Interface)

  b) GitHub Deployment

  c) Container Registry (Docker)

For option 'a', follow the instructions given, for 'b', you will be asked to
link to a github account and for 'c', again follow the instructions given.

For this project, I went with the github deployment for simplicity, as it only
meant one push per deployment.

Once linked, You can enable automatic deploys based off a branch
![AppAutoDeploy]
Or perform a manual deployment
![AppManualDeploy]

In order for the app to run however, certain environment variables need to be set.

From the application overview page, click on 'Settings'

![AppSettingsLink]

Then click on 'Reveal Config Vars'

![AppConfigVars]

You need to add the following variables
<!--markdownlint-disable MD013 MD034 -->
| Config var name       | Purpose                                                                                    | Available Options  | Notes                                                                            |
|-----------------------|--------------------------------------------------------------------------------------------|--------------------|----------------------------------------------------------------------------------|
| AWS                   | If set to 1, will use AWS to serve styling and javascript                                  | 1 = Yes, 0 = No    |                                                                                  |
| AWS_ACCESS_KEY_ID     | Amazon Web Services Access Key                                                             | Supplied by AWS    | See AWS Deployment                                                               |
| AWS_SECRET_ACCESS_KEY | Amazon Web Services Secret Access Key                                                      | Supplied by AWS    | See AWS Deployment                                                               |
| DATABASE_URL          | Postgres DB URL, Auto populated once postgres is added to the Heroku App (See steps below) | Auto-Populated     | You can populate with your own database URL if it's hosted seperately.           |
| DEV                   | Development mode                                                                           | 1 = Yes, 0 = No    | DO NOT ENABLE IN PRODUCTION                                                      |
| SECRET_KEY            | Django Secret Key                                                                          |                    | https://miniwebtool.com/django-secret-key-generator/ recommended to generate one |
| STRIPE_SECRET         | Stripe's Secret Key                                                                        | Supplied by Stripe | See Stripe Deployment                                                            |

<!-- markdown-enable-->
### Setting up Amazon Web Services (AWS)

## Testing

For all testing ran on this site, please refer to [TESTING.md](TESTING.md)

### Credits

[Jesse Couch](https://codepen.io/designcouch/pen/Atyop) for the burger bar animation.

[WebFikirleri](https://codepen.io/WebFikirleri/pen/MLXYKm) for the floating action button
