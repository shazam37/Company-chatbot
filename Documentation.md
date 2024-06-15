- **Documentation**

  ```markdown
  # User Guide for Company Info and File Upload Chatbot

  ## Introduction
  This user guide provides instructions on how to interact with the chatbot application, including querying company information and uploading files for text extraction.

  ## Using the Chatbot

  ### Querying Company Information
  1. Send a POST request to the `/query` endpoint with typing your question in the question body.
  2. The chatbot will respond with the relevant information about the company.

  ### Uploading Files
  1. Send a POST request to the `/upload` endpoint with the file you want to upload.
  2. The chatbot will save the text file in the uploads directory.

  ## Example Requests

  ### Query Example
  ```bash
  curl -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" -d '{"input": "What is the mission of TeamEpic?"}'
