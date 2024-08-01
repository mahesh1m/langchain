# LangChain Course

Welcome to the LangChain Course! This repo contains all the code examples you'll need to follow along with the LangChain Class. 
By the end of this course, you'll know 
1. how to use LangChain
2. to create your own AI agents
3. automate tasks with AI.

## Course Outline

1. **Setup Environment**
2. **Chat Models**
3. **Prompt Templates**
4. **Chains**
5. **Agents & Tools**

## Getting Started

### Prerequisites

- Python 3.10 or 3.11 or 3.11.9
- Conda Environment
- Visual Studio Code

### Virtual Environment Setup

Step 1. Open conda prompt and type below command. This shall provide you all the coda installed directories

>where conda 

Step 2. Edit environment  variables for your account.
Edit path variable and  add conda directories.

Step 3. open command prompt and check conda --version
>conda --version

Step 5. Open Visual Studio code and open the Langchain quest program demos folder

Step 6 - open terminal (command prompt) in visual studio code

Step 7.create virtual environment named mahesh1

>conda create --name mahesh1 python==3.11.9

Step 8. activate conda environment by giving below command
>conda activate mahesh1

Step 9. Install requisite libraries for the project

>pip install -r requirements.txt

Step 10 open .env and update the variables inside with your own values. Example:

OPENAI_API_KEY='Add your key'
Step 11 - Execute the first program by giving the following code.
python python '.\1 Chat Models\1_chat_model_basic.py'
## Repository Structure

Here's a breakdown of the folders and what you'll find in each:

### 1. Chat Models
Learn how to interact with models like ChatGPT, Claude, and Gemini.

- `1_chat_model_basic.py`
- `2_chat_model_basic_conversation.py`
- `3_chat_model_alternatives.py`
- `4_chat_model_conversation_with_user.py`
- `5_chat_model_save_message_history_firestore.py`


### 2. Prompt Templates
Understand the basics of prompt templates and how to use them effectively.

- `1_prompt_template_basic.py`
- `2_prompt_template_with_chat_model.py`


### 3. Chains
Learn how to create chains using Chat Models and Prompts to automate tasks.

- `1_chains_basics.py`
- `2_chains_under_the_hood.py`
- `3_chains_extended.py`
- `4_chains_parallel.py`
- `5_chains_branching.py`


### 4. Agents & Tools
Learn about agents, how they work, and how to build custom tools to enhance their capabilities.

- `1_agent_and_tools_basics.py`
- `2_agent_react_chat.py`
- '3_csv_agent.py'
Learn about agents, how they work, and how to build custom tools to enhance their capabilities.

## How to Use This Repository

1. **Attend Session:**

2. **Run the Code Examples:** Follow along with the code examples provided in this repository.


## Comprehensive Documentation

Each script in this repository contains detailed comments explaining the purpose and functionality of the code. This will help you understand the flow and logic behind each example.

## FAQ

**Q: What is LangChain?**  
A: LangChain is a framework designed to simplify the process of building applications that utilize language models.

**Q: How do I set up my environment?**  
A: Follow the instructions in the "Getting Started" section and ### Virtual Environment Setup above. Ensure you have Python 3.11.9 installed, setup conda environment, levearge repository, install dependencies, include the kesy in .env file.

**Q: I am getting an error when running the examples. What should I do?**  
A: Ensure all dependencies are installed correctly and your environment variables are set up properly. If the issue persists, seek help from mahesh.mohankumar@sc.com

**Q: Can I contribute to this repository?**  
A: Yes! Contributions are welcome. please keep mahesh.mohankumar@sc.com informed about the same.

**Q: Where can I find more information about LangChain?**  
A: Check out the official LangChain documentation 

