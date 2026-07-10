"""
Base Tool Class - All tools inherit from this
"""

from abc import ABC, abstractmethod
from typing import Dict, Any
import logging
from datetime import datetime


class BaseTool(ABC):
    """Abstract base class for all tools"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.logger = logging.getLogger(f"Tool:{name}")
        self.execution_count = 0
        self.last_execution = None
    
    @abstractmethod
    def execute(self, **kwargs) -> Dict[str, Any]:
        """Execute the tool - must be implemented by subclasses"""
        pass
    
    def __call__(self, **kwargs) -> Dict[str, Any]:
        """Make tool callable"""
        self.execution_count += 1
        self.last_execution = datetime.now()
        self.logger.info(f"Executing tool: {self.name}")
        return self.execute(**kwargs)
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"
    
    def __repr__(self) -> str:
        return f"<Tool: {self.name}>"
