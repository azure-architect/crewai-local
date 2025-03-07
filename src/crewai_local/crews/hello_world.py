from typing import Dict, Any

from crewai import Agent, Task, Crew
from crewai_local.core.base_crew import BaseCrew

class HelloWorldCrew(BaseCrew):
    """A simple hello world crew for testing."""
    
    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run a simple hello world crew.
        
        Args:
            inputs: Input parameters (name is optional)
            
        Returns:
            Dict containing greeting message
        """
        name = inputs.get("name", "World")
        
        # Create a simple agent
        greeter = Agent(
            role="Greeter",
            goal="Provide a friendly greeting",
            backstory="I am a friendly greeter who welcomes people",
        )
        
        # Create a simple task
        greeting_task = Task(
            description=f"Create a friendly greeting for {name}",
            expected_output="A warm and friendly greeting message",
            agent=greeter
        )
        
        # Create the crew
        crew = Crew(
            agents=[greeter],
            tasks=[greeting_task],
            verbose=True
        )
        
        # Run the crew
        result = crew.kickoff()
        
        return {
            "greeting": result,
            "recipient": name
        }
