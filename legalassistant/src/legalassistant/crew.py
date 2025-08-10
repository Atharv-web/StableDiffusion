from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pathlib import Path
from legalassistant.tools import DocxAnnotatorTool
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource

# Resolve knowledge file path relative to the project structure


crew_knowledge = JSONKnowledgeSource(
    file_path=["checklist.json"],
)

@CrewBase
class Legalassistant():
    """Legalassistant crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def docAnalyst(self) -> Agent:
        return Agent(
            config=self.agents_config['docAnalyst'], # type: ignore[index]
            verbose=True
        )

    @agent
    def verifyingAnalyst(self) -> Agent:
        return Agent(
            config=self.agents_config['verifyingAnalyst'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def docWriter(self) -> Agent:
        return Agent(
            config=self.agents_config['docWriter'] ,
            verbose=True,
            tools=[DocxAnnotatorTool()]
        )


    @task
    def doc_analyzing_task(self) -> Task:
        return Task(
            config=self.tasks_config['doc_analyzing_task'], # type: ignore[index]
        )

    @task
    def verifying_task(self) -> Task:
        return Task(
            config=self.tasks_config['verifying_task'], # type: ignore[index]
        )
    
    @task
    def writing_task(self) -> Task:
        return Task(
            config= self.tasks_config['writing_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Legalassistant crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            knowledge_sources=[crew_knowledge],
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
