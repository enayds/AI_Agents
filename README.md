# Agent Framework Test Case

This Python code demonstrates the implementation of an agent workflow for generating questions and answers on a specific topic using the CrewAI agent framework in Python. The framework leverages the Ollama model, specifically the 'mistral' model, with a maximum of 7 billion parameters.

## Getting Started

To run this code, ensure that you have the necessary libraries installed. You can install them using the following command:

```bash
pip install crewai langchain_community
```

Make sure to replace the `ollama.Ollama(model='mistral')` line with the appropriate Ollama model from the model catalog if you wish to use a different model.

## Agents

### 1. Researcher

- **Role**: Topic Researcher
- **Goal**: Gather information and teaching methods for the chosen topic.
- **Backstory**: Equipped to explore various knowledge sources, from online data to expert articles, to understand the nuances of a given topic. The goal is to collect relevant information and brainstorm effective teaching methods for beginners, ensuring a clear and engaging learning experience.

### 2. Writer

- **Role**: Text Explainer
- **Goal**: Craft a clear and concise explanation of the topic based on research findings and teaching ideas.
- **Backstory**: Expertise lies in transforming complex information into easily understandable narratives. Leverages research insights and teaching methods to create an engaging and informative text tailored for a novice audience. Strives to present the topic in a logical and accessible manner.

### 3. Examiner

- **Role**: Understanding Evaluator
- **Goal**: Assess the learner's grasp of the topic by generating relevant questions and providing accurate answers with explanations.
- **Backstory**: Excels at evaluating understanding through crafting insightful questions. Analyzes the explanatory text to formulate multiple-choice or open-ended questions that gauge the learner's knowledge absorption. Provides accurate answers along with clear explanations to reinforce learning and clarify any remaining doubts.

## Tasks

### 1. Task Researcher

- **Description**: Develop ideas for teaching someone new to the subject. Explore various knowledge sources to understand the nuances of the chosen topic. Brainstorm effective teaching methods for beginners, ensuring a clear and engaging learning experience. The final answer must be a comprehensive set of teaching ideas and methods.

### 2. Task Writer

- **Description**: Use the Researcher’s ideas to write a piece of text to explain the topic. Craft a clear and concise explanation of the topic based on the research findings and teaching ideas provided by the Researcher. Tailor the text for a novice audience, presenting the topic in a logical and accessible manner. The final answer must be a well-written and informative text explaining the chosen topic.

### 3. Task Examiner

- **Description**: Craft 2-3 test questions to evaluate understanding of the created text, along with the correct answers. Analyze the explanatory text provided by the Writer to formulate insightful test questions. Provide accurate answers along with clear explanations to reinforce learning and clarify any remaining doubts. The final answer must be a set of test questions, along with the correct answers and explanations.

## Crew

- **Agents**: Researcher, Writer, Examiner
- **Tasks**: Task Researcher, Task Writer, Task Examiner
- **Process**: Sequential

## Usage

To execute the agent workflow, run the script and observe the output. The result will provide insights into the collaborative process of the agents and the successful execution of the assigned tasks.

```python
python ai_agents.py
```

The script will print the result of the agent workflow.

**Note**: Ensure that you have the necessary permissions to access the chosen Ollama model and any other dependencies.
