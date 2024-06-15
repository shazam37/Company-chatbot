```markdown
# Development Notes for Company Info and File Upload Chatbot

## Project Overview
This document provides insights into the development process, key decisions, and challenges encountered while building the chatbot application.

## Key Components

### CompanyInfoAgent
- Retrieves and processes company information based on user queries.
- Utilizes Langchain's agent-based architecture to handle query and context together.

### FileUploadAgent
- Manages file uploads, supporting PDF and DOCX formats.
- Saves the file for further processing 

### Flask Integration
- Flask is used to create the web server and define API endpoints for interacting with the chatbot.

## Development Process

- **Step 1:** Research and understand Langchain's agent concept and capabilities.
- **Step 2:** Design the chatbot's architecture, focusing on modularity and separation of concerns.
- **Step 3:** Implement `CompanyInfoAgent` and `FileUploadAgent`.
- **Step 4:** Integrate the agents into the Flask application.
- **Step 5:** Test the application with various queries and file uploads to ensure robustness.

## Challenges and Solutions

- **Challenge:** Combining the query and the company context.
  - **Solution:** Utilize langchain built-in tools to integrate them both.

- **Challenge:** Ensuring seamless integration between multiple agents and the Flask application.
  - **Solution:** Carefully design the interaction flow and use appropriate binding methods in Langchain.

## Enhancements that can be made

- Add more sophisticated natural language processing capabilities.
- Improve error handling and user feedback mechanisms.
- Expand support for additional file formats and types.
