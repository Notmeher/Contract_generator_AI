import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from prompts import generate_prompt  # Import the function from prompts.py

# Load environment variables
load_dotenv()

class CallAIAgent:
    def __init__(self):
        # Set the Groq API key (or any other API key as needed)
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        
        # Initialize ChatGroq client with the specified model and API key
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=self.groq_api_key,
            model_name="llama-3.3-70b-versatile"
        )

    def generate_full_contract(self, party1, party2, start_date, sections_data):
        """
        Generates a full contract using Groq's model (llama-3.3-70b-versatile).
        """
        try:
            full_contract = f"Agreement between {party1} and {party2}\n\nEffective Date: {start_date}\n\n"
            for section, details in sections_data.items():
                # Use the generate_prompt function from prompts.py to create the prompt
                prompt = generate_prompt(section, party1, party2, details)
                
                # Prepare the input for the prompt template
                input_vars = {
                    "section": section,
                    "party1": party1,
                    "party2": party2,
                    "details": details
                }
                
                # Use PromptTemplate to create the correct prompt
                prompt_template = PromptTemplate.from_template(prompt)
                
                # Generate the section content using the Groq model
                try:
                    response = prompt_template | self.llm
                    section_content = response.invoke(input_vars).content
                    full_contract += f"\n### {section} ###\n{section_content}\n"
                    full_contract += "\n" + "-"*50 + "\n"  # Line to separate sections
                except Exception as e:
                    return f"Error generating {section}: {e}"
            
            return full_contract
        except Exception as e:
            return f"Error: {e}"
