#  Contract Generator

This is a powerful contract generation tool that uses AI to automatically create legal contracts based on input details. This application allows users to generate service agreements between two parties with various sections such as introduction, responsibilities, compensation, confidentiality, etc.

## Features

- **AI-Powered Contract Generation**: Generate a full contract with AI that customizes each section based on input data.
- **Concise Responses**: The AI ensures that each contract section is clear, concise, and in paragraph form without unnecessary subsections.
- **Sidebar Input**: The user inputs the required details via the sidebar, including party names, contract start date, and specific section details.
- **Seamless UI**: Simple, clean interface with a well-structured design, including clear separation between contract sections.
- **Customizable**: Easily modify the sections of the contract and customize details as per requirement.

## Technologies Used

- **Streamlit**: Used for the web interface.
- **Groq API (via LangChain)**: Powers the AI that generates contract sections.
- **OpenAI**: The AI model used for generating the contract responses.
- **Python**: Backend programming language used to tie everything together.

## Requirements

- Python 3.x
- `streamlit`
- `dotenv`
- `langchain_groq`
- `openai` (for interacting with GPT models)
- A Groq API key

![image](https://github.com/user-attachments/assets/31cec0b1-4470-4be0-af8d-4374b52cc19d)

