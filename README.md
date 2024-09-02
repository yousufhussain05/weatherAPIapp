# Weather App

This is a simple Weather App that uses the OpenWeatherMap API to display the current weather of a specified city. The application is built with Python and uses the tkinter library to create a GUI.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Setup

### Clone the Repository

```bash
git clone (https://github.com/yousufhussain05/weatherAPIapp.git)
```
cd weatherAPIapp
Create a Virtual Environment
It's recommended to create a virtual environment to manage dependencies separately.

On macOS/Linux:
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
On Windows:
bash
Copy code
python -m venv .venv
.\.venv\Scripts\activate
Install Dependencies
bash
Copy code
pip install -r requirements.txt
If requirements.txt does not exist, manually install the dependencies:

bash
Copy code
pip install requests
Handling Common Errors
Error: ModuleNotFoundError: No module named 'requests'
This error indicates that the requests library is not installed in the current environment. To resolve this, ensure that your virtual environment is activated and then install requests:

bash
Copy code
pip install requests
Error: ModuleNotFoundError: No module named '_tkinter'
This error occurs if the tkinter module is not installed or properly configured.

On macOS:

If you're using Homebrew:

bash
Copy code
brew install python-tk
If the issue persists, you may need to reinstall Python with tkinter support:

bash
Copy code
brew install python
After installing, recreate your virtual environment and activate it:

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
Then, install the necessary dependencies again.

On Windows:

tkinter should be included with the standard Python installation. If you encounter this error on Windows, ensure that you have the correct version of Python installed and that your virtual environment is using this version.

Running the Application
Once all dependencies are installed and your virtual environment is active, you can run the application:

bash
Copy code
python main.py
Deactivating the Virtual Environment
When you are done, you can deactivate the virtual environment with:

bash
Copy code
deactivate
