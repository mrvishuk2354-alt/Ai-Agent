"""
Tool Registry - Manage all available tools
"""

from src.tools.base_tool import BaseTool
from src.tools.calculator import CalculatorTool
from src.tools.text_analysis import TextAnalysisTool
from typing import Dict
import logging


class ToolRegistry:
    """Registry for managing all available tools"""
    
    def __init__(self):
        self.tools: Dict[str, BaseTool] = {}
        self.logger = logging.getLogger("ToolRegistry")
        self._register_default_tools()
    
    def _register_default_tools(self):
        """Register default tools"""
        self.register("calculator", CalculatorTool())
        self.register("text_analysis", TextAnalysisTool())
    
    def register(self, name: str, tool: BaseTool):
        """Register a new tool"""
        self.tools[name] = tool
        self.logger.info(f"Tool registered: {name}")
    
    def get_tool(self, name: str) -> BaseTool:
        """Get a tool by name"""
        if name not in self.tools:
            raise ValueError(f"Tool '{name}' not found")
        return self.tools[name]
    
    def use_tool(self, name: str, **kwargs):
        """Execute a tool"""
        try:
            tool = self.get_tool(name)
            return tool(**kwargs)
        except Exception as e:
            self.logger.error(f"Error using tool '{name}': {str(e)}")
            return {"status": "error", "error": str(e)}
    
    def list_tools(self):
        """List all available tools"""
        return {name: str(tool) for name, tool in self.tools.items()}
    
    def __str__(self):
        return f"ToolRegistry with {len(self.tools)} tools"
