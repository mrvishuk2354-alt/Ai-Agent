"""AI Agent Package"""

from src.agent import AIAgent
from src.tools.registry import ToolRegistry
from src.tools.base_tool import BaseTool
from src.tools.calculator import CalculatorTool
from src.tools.text_analysis import TextAnalysisTool

__version__ = "0.1.0"
__author__ = "Your Name"

__all__ = [
    "AIAgent",
    "ToolRegistry",
    "BaseTool",
    "CalculatorTool",
    "TextAnalysisTool"
]
