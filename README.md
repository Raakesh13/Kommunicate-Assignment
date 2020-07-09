# Kommunicate-Assignment
Make sure python3 is installed and added to PATH on your computer.
If not installed, download and install from https://www.python.org/downloads/. Make sure to check the **Add python 3._ to Path** if installing on windows.

Install pipenv(to usevirtual environment and install python packages). Use command **pip3 install pipenv** in terminal or command prompt to install pipenv.

Clone the project and open the directory in your command prompt or terminal and check the pipfile and pipfile.lock are present(**ls** or **dir**). Run the command: **pipenv install**. This will install the required python package for the project.

Run command **pipenv shell** to activate the virtual environment.

Run command **python app.py** or **python3 app.py**(if python 2 is also install on the computer) to start the server.

Use **postman** application to access the rest-API. Access the below URL with POST request and provide the movie-list in body as shown in the screenshot.

> localhost:5000/movies

>![postman_screenshot](https://github.com/Raakesh13/Kommunicate-Assignment/blob/master/Screenshot%20from%202020-07-10%2002-43-43.png?raw=true)

Response will be in JSON format as shown in the sceenshot:
>![postman_screenshot](https://github.com/Raakesh13/Kommunicate-Assignment/blob/master/Screenshot%20from%202020-07-10%2002-45-49.png?raw=true)
