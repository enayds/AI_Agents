# importing necessary libraries
import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.llms import ollama
search_tool = DuckDuckGoSearchRun()

# definning the llm
# llm = ollama(model = 'mistral')
llm = ollama.Ollama(model='mistral')  # Note the uppercase 'O'


# creating the different agents
researcher = Agent(
    role = "Topic Researcher",
  goal = "Gather information and teaching methods for the chosen topic.",
  backstory = """
  You are well-equipped to explore various knowledge sources, from online data to expert articles, to understand the nuances of a given topic.
  Your goal is to collect relevant information and brainstorm effective teaching methods for beginners, ensuring a clear and engaging learning experience.
  """,
    verbose=True,  # enable more detailed or extensive output
    allow_delegation=True,  # enable collaboration between agent
    llm = llm
)

writer = Agent(
    role = "Text Explainer",
  goal = "Craft a clear and concise explanation of the topic based on research findings and teaching ideas.",
  backstory = """
  Your expertise lies in transforming complex information into easily understandable narratives.
  You leverage the research insights and teaching methods provided to create an engaging and informative text tailored for a novice audience. You strive to present the topic in a logical and accessible manner.
  """,
  verbose = True,
  allow_delegation = True,
  llm = llm
)

examiner = Agent(
    role = "Understanding Evaluator",
  goal = "Assess the learner's grasp of the topic by generating relevant questions and providing accurate answers with explanations.",
  backstory = """
  You excel at evaluating understanding through crafting insightful questions.
  By analyzing the explanatory text, you formulate multiple-choice or open-ended questions that gauge the learner's knowledge absorption.
  Moreover, You provide accurate answers along with clear explanations to reinforce learning and clarify any remaining doubts.
  """,
  verbose = True,
  allow_delegation = True,
  llm = llm
)

# Create tasks for your agents
task_researcher = Task(
    description="""Develop ideas for teaching someone new to the subject.
    Explore various knowledge sources, from online data to expert articles, to understand the nuances of the chosen topic.
    Brainstorm effective teaching methods for beginners, ensuring a clear and engaging learning experience.
    Your final answer MUST be a comprehensive set of teaching ideas and methods.""",
    agent=researcher
)

task_writer = Task(
    description="""Use the Researcher’s ideas to write a piece of text to explain the topic.
    Craft a clear and concise explanation of the topic based on the research findings and teaching ideas provided by the Researcher.
    Tailor the text for a novice audience, presenting the topic in a logical and accessible manner.
    Your final answer MUST be a well-written and informative text explaining the chosen topic.""",
    agent=writer
)

task_examiner = Task(
    description="""Craft 2-3 test questions to evaluate understanding of the created text, along with the correct answers.
    Analyze the explanatory text provided by the Writer to formulate 2-3 insightful test questions.
    Provide accurate answers along with clear explanations to reinforce learning and clarify any remaining doubts.
    Your final answer MUST be a set of test questions, along with the correct answers and explanations.""",
    agent=examiner
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer, examiner],
  tasks=[task_researcher, task_writer, task_examiner],
  verbose=1,
  process = Process.sequential
)

result = crew.kickoff()

print("######################################")
print(result)
