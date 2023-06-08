# Retro

## About Site

Click here to view [Retro](https://forgottenit-retro.herokuapp.com/) (CTRL + Click to open in a new browser tab).

<img src="amiresponsive.png">


# UX - User Experience

## User Stories


### EPIC: User Account
* As a Site User, 


### EPIC: Site Admin
* As a Site Admin

### EPIC: 
* As a Site User

### EPIC: 

### EPIC: 



## Agile Methodology
 
[Kanban Board](https://github.com/users/Forgottenit/projects/4) 

<img src="kanban-board.png">
 

issues  created for User Story 
acceptance criteria and broken down into tasks necessary to satisfy those acceptance criteria. 

MoSCoW Prioritisation 
* Must Have - Guaranteed 
* Should Have - Add significant value but not vital
* Could Have - small impact if not included
* Won't Have - Non-priority 

User Stories were prioritised based on their Moscow levels  tracked with Kanban board 

 Epics, which were not related to the application's features. 
tracked through the Kanban board. 
* EPIC: Initial Setup
* EPIC: Deployment
* EPIC: Styling
* EPIC: Testing
* EPIC: README

## Wireframes
Wireframes were created using [Balsamiq](https://balsamiq.com/)  


<details>
  <summary>Home Page</summary>
  
  <img src="home-page.png" width=800>

</details>

<details>
  <summary></summary>
  
  <img src="" width=800>

</details>

<details>
  <summary></summary>
  
  <img src="" width=800>

</details>

<details>
  <summary></summary>
  
  <img src="" width=800>

</details>

<details>
  <summary></summary>
  
  <img src="" width=800>

</details>

<details>
  <summary></summary>
  
  <img src="" width=800>

</details>

## Database Design
An Entity Relationship Diagram ERD made using [Figma](https://www.figma.com/) 




<img src="erd.png">

## Security Features and Defensive Design
### User Authentication
Django-AllAuth  


### User Authorisation


### Form Validation


### Security-Sensitive Information
env gitignore config vars in heroku debug

## UXD Design
### Colours

[Coolors](https://coolors.co) 

* #FFFFFF White is used for the background colour
* #FEFEFE




<img src="colours.png" width=600>

### Typography
The font used  [Google Fonts](https://fonts.google.com/).
Sans-serif  backup font 

<img src="fonts.png" width=200>

# Features
## Existing Features
### Browser Tabs
favicon 
favicon  generated from  [RealFaviconGenerator](https://realfavicongenerator.net/). 

<img src="" width=800>

### Logo
The logo using [Wix](https://www.wix.com/). 
<img src="logo.png" width=200>

### Navigation Bar



<img src="" width=800>


* Home - Available to all 
* Sign Up - Available not logged in
* Log In - Available not logged in
* Log Out - Available logged in
* 

Small screens

<img src="" width=380>



### Footer
links to Facebook, Twitter, Instagram
Clicking on any of these icons opens a new browser tab so that users navigate back easily.

<img src="" width=500>


### Sign Up Page

<img src="" width=800>



### Log In Page

<img src="" width=800>



### Log Out Page

<img src="" width=800>


### Home Page

<img src="" width=800>



<img src="" width=800>

### 

<img src="" width=800>



<img src="" width=800>



### 



#### Section

<img src="" width=800>



<img src="" width=350>



<img src="" width=350>



<img src="" width=350>



### Warning messages


### 

### Modal



### Error Pages 400 403 404 500
Custom HTML pages for HTTP 400, 403, 404 and 500 errors. 


## Features Left to Implement



# Technologies Used

## Languages
* [HTML]() 
* [CSS]() .
* [Python](https://www.python.org/) 
* [JavaScript]() 

## Frameworks, Libraries and Tools Used within the Application
* [Django](https://www.djangoproject.com/) 
* [Django-AllAuth](https://django-allauth.readthedocs.io/en/latest/overview.html) 
* [Wix](https://www.wix.com/) 
* [RealFaviconGenerator](https://realfavicongenerator.net/) 
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) 
* [Bootstrap](https://getbootstrap.com/)
* [jQuery](https://jquery.com/) 
* [ElephantSQL](https://www.elephantsql.com/) 
* [Cloudinary](https://cloudinary.com/) 
* [Git](https://git-scm.com/) 
* [GitHub](https://github.com/) was used to 
* [Gitpod](https://www.gitpod.io/) was used to 
* [Heroku](https://id.heroku.com/login) was used to 
* [Google Fonts](https://fonts.google.com/) was used
* [Font Awesome](https://fontawesome.com/) was used 


## Other Online Tools used
* [Balsamiq](https://balsamiq.com/) wireframes 
* [Figma](https://www.figma.com/) database image
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) screen sizes/ social login ???.
* [Wave Web Accessibility Evaluation Tools](https://wave.webaim.org/)  test accessiblity.
* [Coolors](https://coolors.co)  colours
* [Remove Background](https://www.remove.bg/) background from the logos.
* [Am I Responsive](https://ui.dev/amiresponsive) was used 
* [Compressor.io](https://compressor.io/) compress the images used in the application and README.
* [Grammarly](https://app.grammarly.com/)  grammatical 

## Validators
* [W3C HTML Validator](https://validator.w3.org/) used to validate HTML codes.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)used to validate CSS codes.
* [JSHint](https://jshint.com/) was used to validate JavaScript codes.
* [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate Python codes.

# Testing


# Deployment
The live deployed application - [Retro](https://forgottenit-retro.herokuapp.com/) (CTRL + Click to open in a new browser tab).

### Initial Setup and Deployment - 

1. **Create a New GitHub Repository**
    - Navigate to the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template).
    - Click on the "Use this template" button.
    - Give your repository a name and click "Create repository from template."
    
2. **Open GitPod Workspace**
    - Navigate to your new GitHub repository.
    - Click on the GitPod button to start a new GitPod workspace. 

3. **Install Django and Supporting Libraries**
    - In your GitPod terminal, type `pip3 install django gunicorn` to install Django and Gunicorn.
    - To help Django work with PostgreSQL (used by Heroku for databases), install `dj-database-url` and `psycopg2` by entering `pip3 install dj_database_url psycopg2` in the terminal.
    - Cloudinary [Cloudinary](https://cloudinary.com/about) is a cloud service that stores a web application's image management. To add it, enter `pip3 install dj3-cloudinary-storage` in the terminal.

4. **Create a requirements.txt File**
    - In your terminal, type `pip3 freeze > requirements.txt` to generate a list of your project's dependencies. This will be used by Heroku to identify what Python packages are required to run your project.

5. **Create a New Django Project**
    - In your terminal, type `django-admin startproject 'project_name' .` Replace "project_name" with your chosen name for the project.
    - The `.` at the end is important as it sets the current directory (the workspace root) as the place to create the new Django project.

6. **Create a New Django App**
    - In your terminal, type `python3 manage.py startapp 'app_name'` to create a new app within your Django project. Replace "app_name" with your chosen name for the app.

7. **Register the New Django App**
    - Open the `settings.py` file located inside your Django project's directory.
    - Scroll down to the `INSTALLED_APPS` section and add your app's name at the bottom. Your `INSTALLED_APPS` should now look something like this:
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        ...
        'app_name',  # Replace "app_name" with the name of your app
    ]
    ```
    - Save the `settings.py` file. Django now knows about your new app and will include it in its operations.

8. **Apply Database Migrations**
    - Django comes with a built-in database abstraction layer that allows you to create your database schema based on your data models. To apply these migrations, in the terminal, type `python3 manage.py migrate`.
    - This command will apply all pending migrations to your database, effectively syncing your database schema with your current Django project's data models.

9. **Start the Django Development Server**
    - Finally, to verify that everything is set up correctly, let's start the Django development server. In the terminal, type `python3 manage.py runserver`.
    - Visit the provided localhost URL in the browser. If everything is set up correctly, you should see the Django welcome screen.
10. **Create a Heroku App**
    - Navigate to the [Heroku](https://dashboard.heroku.com/login) website. 
    - Once logged in, click on the "New" button on the top right corner, and then click "Create new app."
    - Enter a unique name for your app, select your nearest region and then click "Create App."
    - [Retro](https://forgottenit-retro.herokuapp.com/) is available by clicking this link.

11. **Create an ElephantSQL Database**
    - Go to the [ElephantSQL](https://www.elephantsql.com/) website and create an account if you haven't done so.
    - After logging in, click on "Create New Instance" on the dashboard.
    - Enter a name for your instance, select the "Tiny Turtle" free plan, and click "Select Region."
    - Choose the region closest to you and click "Review."
    - Confirm the details and click "Create instance."
    - You'll be directed to your instance's dashboard. Under the "Details" tab, find the "URL" section and click the copy button. You'll need this URL in the next step.

12. **Create an env.py File**
    - In your terminal, type `touch env.py` to create a new file named env.py in your root directory.
    - Open the env.py file and add the following lines of code:
    ```python
    import os
    os.environ["DATABASE_URL"] = "your_database_url"  # replace "your_database_url" with the URL you copied from ElephantSQL
    os.environ["SECRET_KEY"] = "your_secret_key"  # replace "your_secret_key" with your Django project's secret key
    ```
    - Save the file and make sure it's included in your .gitignore file to prevent it from being pushed to your GitHub repository.

13. **Add SQLite Database to .gitignore File**
    - Open your .gitignore file and add the following line of code:
    ```python
    *.sqlite3
    ```
    - This prevents any SQLite database from being pushed to your GitHub repository. Sqlite3 is used in the development stage, ElephantSql will be used for production.

14. **Modify settings.py File**
    - In your settings.py file, import the necessary libraries and environment variables at the top of the file:
    ```python
    import os
    import dj_database_url
    if os.path.isfile('env.py'):
        import env
    ```
    - Replace the Django-provided secret key with your secret key environment variable:
    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ```
    - Comment out the original DATABASES variable and replace it with the following:
    ```python
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    ```
    - These changes set up your Django project to use the ElephantSQL database. This is for production with Heroku deployment, sqlite3 is used in the development stage. 
  
15. **Migrate Database Structure to ElephantSQL Database**
    - To create the necessary tables in your ElephantSQL database, run the following command in your terminal:
    ```python
    python manage.py migrate
    ```
    - You can verify this by going to your ElephantSQL instance's dashboard and checking the "Browser" tab.

16. **Push Changes to GitHub**
    - To save your changes to your GitHub repository, run the following commands in your terminal:
    ```python
    git add .
    git commit -m "your_commit_message"  # replace "your_commit_message" with a short description of your changes
    git push
    ```
    - Now your changes are saved on GitHub.

17. **Set Up Cloudinary**
    - Visit the [Cloudinary](https://cloudinary.com/) website and create an account if you don't have one already.
    - From your Dashboard, you'll see your Cloudinary API environment variable. Click to copy it.
    - Open your env.py file and add the following line of code:
    ```python
    os.environ["CLOUDINARY_URL"] = "your_cloudinary_url"  # replace "your_cloudinary_url" with the URL you copied from Cloudinary
    ```
    - Save the file. This will allow your Django project to connect to your Cloudinary storage.

18. **Set Up Heroku Config Vars**
    - Go to the dashboard of your Heroku app, and navigate to the "Settings" tab.
    - Scroll down to the "Config Vars" section and click on the "Reveal Config Vars" button.
    - Enter the following key-value pairs:
      - Key: `DATABASE_URL`, Value: your ElephantSQL URL
      - Key: `SECRET_KEY`, Value: your Django secret key
      - Key: `PORT`, Value: `8000`
      - Key: `CLOUDINARY_URL`, Value: your Cloudinary URL
      - Key: `DISABLE_COLLECTSTATIC`, Value: `1`  (This is temporary and will be removed when deploying the full project. It is to prevent Heroku from collecting static files, which it does by default)
    - These Config Vars will allow Heroku to properly deploy your Django project.

19. **Update settings.py**
    - Open your settings.py file and add the following lines of code:
    ```python
    INSTALLED_APPS = [
        ...
        ...
        'cloudinary_storage',
        'django.contrib.staticfiles',
        'cloudinary',
        'your_app_name',  # replace "your_app_name" with your Django app's name
    ]
    ```
    - Add the following lines of code to tell Django that you're using Cloudinary to store media and static files for cloud-based image handling.:
    ```python
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ```
    - Also, tell Django where your templates are stored by adding the following lines of code:
    ```python
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [TEMPLATES_DIR],
            'APP_DIRS': True,
            ...
        },
    ]
    ```
    - Lastly, add the following line of code to allow connections from your Heroku app and your local machine:
    ```python
    ALLOWED_HOSTS = ['your_heroku_app_name.herokuapp.com', 'localhost']  # replace "your_heroku_app_name" with your Heroku app's name

    #required CSRF_TRUSTED_ORIGINS for Django 4.2, https:// is required
    CSRF_TRUSTED_ORIGINS = ['https://your_heroku_app_name.herokuapp.com','https://8000-your_local_development_site.com']
    ```

20. **Create Static Files**
    - In your project's root directory, create three new folders: `media`, `static`, and `templates`. This is where you'll store your static files and templates. Template folders will later be added to specific apps as required, along with css etc.

21. **Create a Procfile**
    - In your project's root directory, create a file named `Procfile` (no extension).
    - In the Procfile, add the following line of code:
    ```python
    web: gunicorn 'your_project_name'.wsgi  # replace "your_project_name" with your Django project's name
    ```
    - This file is necessary for running your app on Heroku. Gunicorn is a WSGI (Web Server Gateway Interface) HTTP server for Python web applications.

22. **Push Changes to GitHub**
    - To save your changes to your GitHub repository, run the following commands in your terminal:
    ```python
    git add .
    git commit -m "your_commit_message"  # replace "your_commit_message" with a short description of your changes
    git push
    ```

23. **Connect Heroku to GitHub**
    - Go to your Heroku app's dashboard and navigate to the "Deploy" tab.
    - In the "Deployment method" section, click on the "GitHub" button.
    - Connect your GitHub account if you haven't done so, and in the "Connect to GitHub" section, search for your GitHub repository and click "Connect."

24. **Deploy Your App**
    - Scroll down to the "Manual Deploy" section, select your GitHub branch (`main`), and click "Deploy Branch."
    - Wait for Heroku to finish deploying your app, and then click "View".
    - It is also optional to select Automatic Deploys.

### Local Deployment

If you wish to run this project locally on your machine, please follow the steps outlined below:

1. **Clone the Repository:**

    To make a copy of the project's repository on GitHub on your local machine, you can clone it. Replace `<repository_url>` with the actual URL of the repository and `<project_name>` with the name of the project directory that you cloned:

    ```
    # Clone the repository
    git clone <repository_url>
    # Change directory to the cloned project
    cd <project_name>
    ```

2. **Install Dependencies:**

    The project requires several Python libraries and packages to function correctly. The list of these can be found in the `requirements.txt` file. If you're using a virtual environment, ensure it's activated. Install the dependencies using pip with the following terminal command:

    ```
    pip3 install -r requirements.txt
    ```

3. **Configure Environment Variables:**

    This project uses environment variables to keep sensitive information secure. Create a new file named `env.py` at the root level of the project, and populate it with your data. Replace the placeholders with your actual Cloudinary API key, ElephantSQL database URL, and your chosen secret key:

    ```python
    import os

    os.environ.setdefault("CLOUDINARY_URL", '<enter your Cloudinary API key here>')
    os.environ.setdefault("DATABASE_URL", '<enter your ElephantSQL database URL here>')
    os.environ.setdefault("SECRET_KEY", '<enter your secret key here>')
    os.environ['DEVELOP'] = '1'  # for local environment only
    ```

    Remember to add the `env.py` file to the `.gitignore` file to prevent your sensitive data from being exposed.

4. **Migrate the Database:**

    Ensure you have a running PostgreSQL server that Django can connect to. Apply the migrations to create your database schema:

    ```
    python3 manage.py migrate
    ```
5. **Start the Project Locally:**

    If you're using a virtual environment, remember to activate it whenever you're running the project. With the project cloned, dependencies installed, environment variables set, and the database migrated, you can now start the project locally with the following commands:

    ```
    # Make migration
    python3 manage.py makemigrations
    # Apply the migrations
    python3 manage.py migrate
    # Create a superuser for the Django admin interface
    python3 manage.py createsuperuser
    # Start the Django development server
    python3 manage.py runserver
    ```

6. **Forking the Repository on GitHub:**

    You can fork the repository, which creates a copy of it in your own GitHub account:

    - Open GitHub and navigate to the project repository.
    - Click on the "Fork" button at the top of the page, which creates a new copy of the repository under your GitHub account.

7. **Cloning the Repository on GitHub:**

    To create a local clone of your forked repository, follow the steps below:

    - Navigate to the forked repository in your GitHub account.
    - Click the "Code" button, then under the "HTTPS" tab of the "Clone" section, click the clipboard icon to copy the URL.
    - Open a terminal window, navigate to the directory where you want the clone to reside.
    - Type "git clone", then paste the URL you copied from GitHub.
    - Press "Enter", and a local clone will be created.

# Credits
## Content
* 

## Media
* 

## Code
* Django Documentation 
	* [DJANGO ](https://docs.djangoproject.com/)
* Code Institute
* 
* 
* 
	


# Acknowledgements

* 
* 
* 
* 
