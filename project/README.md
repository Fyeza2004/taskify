# Taskify - Task Manager

### **Video URL** :  <(https://vimeo.com/942832320)>

### **Description** :
The Task Manager is a web application that allows users to manage daily tasks or upcoming events. This web application can be used for personal use or any professionl field. Users can sign up for an account, log in, add tasks with titles, descriptions, and due dates, view their tasks, search for tasks, and delete tasks. The application ensures that users can only access their own tasks after logging in.

### **Files** :
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

### **Design Choices** :
- **User Authentication -** Users are required to sign up and log in to access the task management features. This ensures that each user can only view and manage their own tasks.
- **Task Status -** Tasks are displayed with their due dates, and their status (completed or pending) is indicated based on the due date compared to the current date.
- **Error Handling -** Error messages are displayed to users if they fail to provide required information or if there are issues with their input.
- **Success Messages -** Success messages are shown to users after successfully performing actions such as signing up, logging in, or adding tasks.

### **Languages** :
The Task Manager is a web application built using several programming languages and technologies.
- **Python -** This language serves as the backbone of the backend logic, leveraging the Flask framework for web development.
- **SQL -** This language is utilized for managing the database, with SQLite serving as the database management system for storing user account information and task data.
- **HTML -** This language is employed for creating the structure and layout of web pages.
- **CSS -** This language is used for styling and enhancing the visual presentation of the application.
- **JavaScript -** This language is employed for client-side interactivity and dynamic behavior, enhancing the user experience with features such as form validation and asynchronous requests.

Together, these languages and technologies enable users to sign up, log in, add, view, search, and delete tasks, ensuring that each user can only access and manage their own tasks after logging in.

### **Prerequisites** :
What things you need to install the software and how to install them.
- Python3
- pip3
- sqlite3
- cs50
- Flask-Session
- requests
- git

### **Installation Instructions** :
#### Step 1:
First clone this repository using the following command (using your terminal) in the directory of your choice - https://github.com/Fyeza2004/taskify.git

#### Step 2:
Go to the project directory -
cd tastify/

#### Step 3:
The last step is execute the following command in the same location of the app.py file -
flask run

### **User Guide** :
#### Signing Up for an Account:

1. **Navigate to the Sign Up Page:**
   - Open your web browser and go to the Task Manager website.
   - Click on the "Sign Up" link in the navigation bar.

2. **Fill Out the Sign Up Form:**
   - Enter your desired username and password in the provided fields.
   - Click on the "Sign Up" button to create your account.

3. **Confirmation:**
   - After signing up successfully, you will be redirected to the login page.

#### Logging In:

1. **Access the Login Page:**
   - If you're not already on the login page, navigate to it by clicking on the "Login" link in the navigation bar.

2. **Enter Your Credentials:**
   - Provide your username and password in the respective fields.

3. **Login:**
   - Click on the "Login" button to log in to your account.
   - Upon successful login, you will be directed to the Task Manager dashboard.

#### Adding Tasks:

1. **Navigate to the Add Task Page:**
   - From the dashboard, click on the "Add Task" button.

2. **Enter Task Details:**
   - Fill out the title, description, and due date fields for your task.

3. **Save the Task:**
   - Click on the "Save" or "Add Task" button to save your task.
   - Your task will be added to the Task Manager database.

#### Viewing Tasks:

1. **Dashboard:**
   - Upon logging in, you will be directed to the dashboard.
   - Here, you can view a list of all your tasks.

2. **Task Details:**
   - Click on any task to view its details, including title, description, starting date, and due date.

#### Searching for Tasks:

1. **Navigate to the Search Page:**
   - Click on the "Search" link in the navigation bar to access the search page.

2. **Enter Search Query:**
   - In the search bar, enter keywords related to the task you're looking for.

3. **View Search Results:**
   - Task Manager will display a list of tasks that match your search query.

#### Deleting Tasks:

1. **From the Dashboard:**
   - Hover over the task you want to delete.
   - Click on the delete icon or button associated with the task.

2. **Confirmation:**
   - Task Manager will ask for confirmation before deleting the task.
   - Confirm the deletion, and the task will be removed from your list.

### **Get Started Now!**

