# Taskify - Task Manager

### Video URL :  <(https://vimeo.com/942832320)>

### Description :
The Task Manager is a web application that allows users to manage daily tasks or upcoming events. This web application can be used for personal use or any professionl field. Users can sign up for an account, log in, add tasks with titles, descriptions, and due dates, view their tasks, search for tasks, and delete tasks. The application ensures that users can only access their own tasks after logging in.

### Files :
#### "app.py" :
This file contains the main logic of the Flask web application. It defines routes for different pages, such as the index page, login page, sign up page, adding tasks page, searching tasks page, and more. It interacts with the database to perform CRUD operations on tasks and user accounts.

#### "helpers.py" :
This file contains helper functions used by the Flask application. These functions include "login_required" and "logout_required", which are decorators to ensure that users are logged in or logged out before accessing certain routes.

#### "tasks.db" :
This SQLite database file stores user account information and task data. It has tables for users and tasks, with relationships established between them.

#### "templates" folder :
This folder contains HTML templates used by the Flask application to render pages. Each HTML file corresponds to a different page of the application, such as layout.html, index.html, login.html, signup.html, add.html, search.html, search_results.html, error_message.html, and success_message.html.

#### "static" folder :
This folder contains three folder - css, js, and img. The 'css' folder contains all the css files for styling the web application such as main.css, login.css, signup.css, and add.css. The 'js' folder contains all the javascript files for the functionality of the web application such as login.js, add.js, and validations.js. And the 'img' folder contains the image that is used as the background of the web application - 'bg.jpg'.

### Design Choices :
- **User Authentication -** Users are required to sign up and log in to access the task management features. This ensures that each user can only view and manage their own tasks.
- **Task Status -** Tasks are displayed with their due dates, and their status (completed or pending) is indicated based on the due date compared to the current date.
- **Error Handling -** Error messages are displayed to users if they fail to provide required information or if there are issues with their input.
- **Success Messages -** Success messages are shown to users after successfully performing actions such as signing up, logging in, or adding tasks.

### Languages :
The Task Manager is a web application built using several programming languages and technologies.
- **Python -** This language serves as the backbone of the backend logic, leveraging the Flask framework for web development.
- **SQL -** This language is utilized for managing the database, with SQLite serving as the database management system for storing user account information and task data.
- **HTML -** This language is employed for creating the structure and layout of web pages.
- **CSS -** This language is used for styling and enhancing the visual presentation of the application.
- **JavaScript -** This language is employed for client-side interactivity and dynamic behavior, enhancing the user experience with features such as form validation and asynchronous requests.

Together, these languages and technologies enable users to sign up, log in, add, view, search, and delete tasks, ensuring that each user can only access and manage their own tasks after logging in.

### Prerequisites :
What things you need to install the software and how to install them.
- Python3
- pip3
- sqlite3
- cs50
- Flask-Session
- requests
- git

### Installation Instructions :

