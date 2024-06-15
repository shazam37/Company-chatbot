# importing libraries

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor
from langchain.agents import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
import os

# Calling OpenAPI API
# os.environ['OPENAI_API_KEY'] = ""  # use your own API key here
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# providing companies info as a context (example)
company_info = {
    "name": "TeamEpic",
    "location": "India",
    "industry": "Technology",
    "mission": "Shaping the future of technology by nurturing and developing the next generation of AI talent.",
    "founder": "John Doe",
    "founded": "2020",
    "employees": "150",
    "products": ["AI Talent Development", "Generative AI Solutions"],
    "website": "https://www.teamepic.ai"
}

class CompanyInfoAgent:
    def __init__(self):
        pass

    def execute_query(self, query):

        ''' Executes the query and context together with langchain agent'''

        @tool
        def handle_query():

            '''extracts the content from dictionary'''

            context = " ".join([f"{k}: {v}" for k, v in company_info.items()])
            return context
        
        tools = [handle_query]

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are very powerful assistant, good at helping solving queries for the company. Please answer everything in a detailed and well mannered way to the users query. Ask the user whether they want to upload a file. If so, they can do it from the below upload section.",
                ),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )

        llm_with_tools = llm.bind_tools(tools)

        agent = (
            {
                "input": lambda x: x["input"],
                "agent_scratchpad": lambda x: format_to_openai_tool_messages(
                x["intermediate_steps"]
                ),
            }
            | prompt
            | llm_with_tools
            | OpenAIToolsAgentOutputParser()
        )

        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
        answer = list(agent_executor.stream({"input": {query}}))

        if answer and 'output' in answer[-1]:
            return answer[-1]['output']
        else:
            return "No response from the model."


# dealing with pdf and docx extensions
class FileUploadAgent:
    def __init__(self):
        pass
    
    # handles the file upload based on the file type
    def handle_upload(self, file_path):
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == '.pdf':
            return self.extract_text_from_pdf(file_path)
        elif file_extension == '.docx':
            return self.extract_text_from_docx(file_path)
        else:
            return "Unsupported file format. Please upload a PDF or DOCX file."

# connects the info_agent and the file_upload_agent 
class Chatbot:
    def __init__(self):
        self.company_info_agent = CompanyInfoAgent()
        self.file_upload_agent = FileUploadAgent()
        self.current_task = None

    def handle_input(self, user_input):
        # Simple heuristic to determine if the query is about company info or file upload
        if "upload" in user_input.lower():
            self.current_task = 'upload'
            return "Please upload a file (PDF or DOCX) using the form below."
        elif self.current_task == 'upload':
            return self.handle_file_upload(user_input)
        else:
            self.current_task = 'info'
            return self.company_info_agent.execute_query(user_input)

    def handle_file_upload(self, file_path):
        response = self.file_upload_agent.handle_upload(file_path)
        self.current_task = None  # Reset the task
        return response    