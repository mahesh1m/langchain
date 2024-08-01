from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.agents import AgentType
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model="gpt-4o")
agent=create_csv_agent(llm=model,
path="C:\\Users\\user\\Desktop\\Langchain Quest Program\\4_agents_tools\\sample.csv",
agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
allow_dangerous_code=True,
verbose=True)
result=agent.run(" find average of Column C in the dataset?")