"""
Main AI Agent Class
"""

import logging
from typing import Dict, Any, List
from src.tools.registry import ToolRegistry
from datetime import datetime
import json


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


class AIAgent:
    """Main AI Agent class"""
    
    def __init__(self, model: str = "gpt-4", debug: bool = False):
        self.model = model
        self.debug = debug
        self.logger = logging.getLogger("AIAgent")
        self.tool_registry = ToolRegistry()
        self.conversation_history: List[Dict] = []
        self.task_count = 0
        
        self.logger.info(f"AI Agent initialized - Model: {model}, Debug: {debug}")
    
    def run(self, task: str) -> Dict[str, Any]:
        """
        Run a task/query
        
        Args:
            task: Task description or query
        
        Returns:
            Task result
        """
        self.task_count += 1
        timestamp = datetime.now().isoformat()
        
        self.logger.info(f"Task #{self.task_count}: {task}")
        
        # Add to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": task,
            "timestamp": timestamp
        })
        
        try:
            # Parse task for tool usage
            result = self._process_task(task)
            
            # Add response to history
            self.conversation_history.append({
                "role": "agent",
                "content": result,
                "timestamp": datetime.now().isoformat()
            })
            
            return result
        
        except Exception as e:
            self.logger.error(f"Task execution error: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "task": task
            }
    
    def _process_task(self, task: str) -> Dict[str, Any]:
        """Process and execute a task"""
        
        # Check for calculator usage
        if any(word in task.lower() for word in ['calculate', 'math', 'plus', 'minus', 'times', 'divide', '+']):
            return self._handle_calculator_task(task)
        
        # Check for text analysis
        if any(word in task.lower() for word in ['analyze', 'count', 'keyword', 'text', 'word']):
            return self._handle_text_analysis_task(task)
        
        # List available tools
        if any(word in task.lower() for word in ['list', 'tools', 'help', 'available']):
            return self._handle_list_tools()
        
        # Default response
        return {
            "status": "info",
            "message": "Task understood",
            "task": task,
            "available_commands": [
                "Calculate: '2 + 2' या 'multiply 5 by 3'",
                "Analyze text: 'analyze this text: ...'",
                "List tools: 'show me available tools'"
            ]
        }
    
    def _handle_calculator_task(self, task: str) -> Dict[str, Any]:
        """Handle calculator tasks"""
        # Extract expression from task
        expression = self._extract_expression(task)
        
        if expression:
            result = self.tool_registry.use_tool("calculator", expression=expression)
            return {
                "status": "success",
                "tool_used": "calculator",
                "result": result
            }
        
        return {
            "status": "error",
            "error": "Could not extract mathematical expression from task"
        }
    
    def _handle_text_analysis_task(self, task: str) -> Dict[str, Any]:
        """Handle text analysis tasks"""
        # Extract text from task
        text = self._extract_text(task)
        
        if text:
            result = self.tool_registry.use_tool("text_analysis", text=text, analysis_type="full")
            return {
                "status": "success",
                "tool_used": "text_analysis",
                "result": result
            }
        
        return {
            "status": "error",
            "error": "Could not extract text from task"
        }
    
    def _handle_list_tools(self) -> Dict[str, Any]:
        """List all available tools"""
        tools = self.tool_registry.list_tools()
        return {
            "status": "success",
            "message": "Available tools:",
            "tools": tools
        }
    
    def _extract_expression(self, task: str) -> str:
        """Extract mathematical expression from task"""
        import re
        # Look for patterns like "calculate 2+2" or just "2+2"
        match = re.search(r'(\d+[\+\-\*/%()]*\d+[\+\-\*/%().\d]*)', task)
        return match.group(1) if match else None
    
    def _extract_text(self, task: str) -> str:
        """Extract text to analyze from task"""
        # Look for text after "analyze" or "analyze text:"
        import re
        match = re.search(r'(?:analyze|text:?)\s+(.+)', task, re.IGNORECASE)
        return match.group(1).strip() if match else None
    
    def get_history(self) -> List[Dict]:
        """Get conversation history"""
        return self.conversation_history
    
    def get_stats(self) -> Dict[str, Any]:
        """Get agent statistics"""
        return {
            "tasks_completed": self.task_count,
            "tools_available": len(self.tool_registry.tools),
            "conversation_length": len(self.conversation_history),
            "model": self.model,
            "debug_mode": self.debug
        }
    
    def __str__(self):
        return f"AIAgent(model={self.model}, tasks={self.task_count}, tools={len(self.tool_registry.tools)})"
