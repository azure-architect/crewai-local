from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseCrew(ABC):
    """Base class for all crew implementations."""
    
    @abstractmethod
    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run the crew with the given inputs.
        
        Args:
            inputs: Input parameters for the crew
            
        Returns:
            Result of the crew execution
        """
        pass
