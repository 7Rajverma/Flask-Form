# Flask-Form
Interactive form using flask framework

# Flask Authentication App

This is a simple Flask-based authentication system that allows users to sign up and log in.

## Features
- User registration with validation
- User login with email and password
- Flash messages for user feedback
- Basic HTML templates for layout and forms

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Set environment variables (optional, for security):
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

2. Start the Flask app:
   ```bash
   python app.py
   ```

3. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure
```
|-- app.py              # Main application file
|-- form.py             # Flask-WTF form validation
|-- templates/          # HTML templates
|   |-- home.html
|   |-- layout.html
|   |-- login.html
|   |-- signup.html
|-- requirements.txt    # List of dependencies
|-- requirements        # Additional dependencies file
```

## Dependencies
- Flask
- Flask-WTF
- WTForms

To install missing dependencies, use:
```bash
pip install flask flask-wtf wtforms
```

## Usage
- Navigate to `/signup` to create an account.
- Navigate to `/login` to log in with your registered credentials.
- Flash messages will inform users of successful actions or errors.

## License
This project is licensed under the MIT License.


