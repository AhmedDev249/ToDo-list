 # Simple To-Do List Application

 This is a basic web-based To-Do List application built with Flask, allowing users to create, view, edit, and delete tasks.

 ## Features

 *   **View Tasks**: See a list of all your current tasks on the homepage.
 *   **Add New Tasks**: Easily add new tasks via a dedicated "Add Task" page.
 *   **Edit Tasks**: Modify the title of existing tasks.
 *   **Delete Tasks**: Remove tasks you no longer need.
 *   **Simple User Interface**: A clean and straightforward interface for managing your tasks.
 *   **API Endpoint**: Includes a basic API endpoint for adding tasks (though the web UI uses a separate form submission).

 ## Technologies Used

 *   **Backend**: Python (Flask)
 *   **Database**: SQLite (default for SQLAlchemy, managed by Flask-SQLAlchemy)
 *   **Frontend**: HTML, CSS
 *   **Other Libraries**:
     *   `Flask-CORS`: For handling Cross-Origin Resource Sharing (if you plan to use a separate frontend).
     *   `Flask-JWT-Extended`: For JSON Web Token-based authentication (currently used for the `/add_task` API endpoint, but not integrated into the web UI).

 ## Setup and Installation

 Follow these steps to get the application up and running on your local machine.

 ### 1. Clone the Repository

 First, clone the project repository to your local machine:

 ```bash
 git clone <repository_url> # Replace with your actual repository URL
 cd "ToDo list" # Navigate into the project directory
 ```

 ### 2. Create a Virtual Environment

 It's highly recommended to use a virtual environment to manage project dependencies.

 ```bash
 python -m venv venv
 ```

 ### 3. Activate the Virtual Environment

 *   **On Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
 *   **On macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

 ### 4. Install Dependencies

 Install the required Python packages using pip. You'll need a `requirements.txt` file. If you don't have one, you can create it by running:

 ```bash
 pip freeze > requirements.txt
 ```

 Then, install the dependencies:

 ```bash
 pip install -r requirements.txt
 ```

 If you don't have a `requirements.txt` yet, you'll need to install the core libraries manually:

 ```bash
 pip install Flask Flask-SQLAlchemy Flask-CORS Flask-JWT-Extended
 ```

 ### 5. Run the Application

 With the virtual environment activated, run the Flask application:

 ```bash
 python app.py
 ```

 The application will typically run on `http://127.0.0.1:5000/`.

 ## Usage

 Once the application is running:

 *   **Homepage**: Open your web browser and go to `http://127.0.0.1:5000/` to view your tasks.
 *   **Add Task**: Click the "Add New Task" button or navigate directly to `http://127.0.0.1:5000/add`.
 *   **Edit Task**: On the homepage, click the "Edit" button next to the task you wish to modify.
 *   **Delete Task**: On the homepage, click the "Delete" button next to the task you wish to remove.

 ## Project Structure

 ```
 ToDo list/
 ├── app.py                  # Main Flask application entry point
 ├── config.py               # Application configuration
 ├── extensions.py           # Flask extensions (DB, JWT) initialization
 ├── models.py               # Database models (Tasks)
 ├── routes/
 │   ├── __init__.py
 │   ├── auth.py             # Authentication routes (if implemented)
 │   └── view.py             # Web UI routes (home, add, edit, delete)
 └── templates/
     ├── add_task.html       # Form for adding new tasks
     ├── edit_task.html      # Form for editing existing tasks
     └── index.html          # Homepage displaying all tasks
 ```

 ## API Endpoints (for reference)

 While the web UI handles task management, there's also a basic API endpoint:

 *   **`POST /add_task`**:
     *   **Requires**: JWT authentication (e.g., `Authorization: Bearer <token>`)
     *   **Request Body**: JSON object with a `title` key (e.g., `{"title": "My new task"}`)
     *   **Functionality**: Adds a new task to the database.

 ## Future Enhancements

 *   **Task Completion Status**: Add a checkbox to mark tasks as completed.
 *   **User Authentication**: Implement full user login/registration so each user has their own task list.
 *   **Improved UI/UX**: Enhance the styling and user experience.
 *   **Filtering/Sorting**: Add options to filter tasks (e.g., by completed status) or sort them.
 *   **Error Handling**: More robust error handling and user feedback.

 ---

 Feel free to contribute or suggest improvements!