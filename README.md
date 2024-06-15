# Company Chatbot

## Introduction
This project is a Flask-based chatbot application that provides detailed company information upon request and can handle file uploads (PDF and DOCX) for processing text content. Its logic is built using the integration of OpenAI API and Langchain. You can give the context of the company using a dictionary in the **agents.py** file so that the chatbot responds based on the companies info. 

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/chatbot-project.git
   cd chatbot-project

2. Install the required libraries:
   
   ```sh
   pip install -r requirements.txt

3. Set up your OpenAI API key:

   ```sh
   export OPENAI_API_KEY="your_openai_api_key_here"

### Running the Application

1. Start the Flask application:

   ```sh
   python app.py

2. The application will be running on http://127.0.0.1:5000.

### Project Structure

- agents.py: Main application file containing the chatbot logic

- app.py: application file containing the Flask routes.

- requirements.txt: File listing all the dependencies required for the project.

- README.md: This file, providing setup and usage instructions.

- static and templates: for the HTML and CSS files.

- Documentation: containing information about using the app.

- Development Notes: containing information about the development process and the challenges faced.

### The app outlook

- The app before any upload looks like:
  
![image1](https://github.com/shazam37/Company-chatbot/assets/119686545/4d6edb84-8b65-4b3c-9892-65ab0036dcc7)

- The app upon receiving a query gives a response:

![image2](https://github.com/shazam37/Company-chatbot/assets/119686545/800549b3-e59f-4693-a422-9783ad023615)

- The app on file upload gives a prompt for successful file submission: 

![image3](https://github.com/shazam37/Company-chatbot/assets/119686545/d46760a1-5fe8-4683-8956-4544c64fcb0a)


   
