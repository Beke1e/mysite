Local Deployment Instructions for Flask App
-------------------------------------------

1. Open a command prompt in the project directory (f:/project/mysite).

2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the Flask app with Waitress:
   python -m waitress --listen=0.0.0.0:8080 app:app

6. Open your browser and navigate to http://localhost:8080 to see the app running.

Notes:
- To stop the server, press Ctrl+C in the command prompt.
- Ensure Python is installed and added to your system PATH.
