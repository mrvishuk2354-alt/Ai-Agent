"""
Calculator Tool - Perform mathematical operations
"""

from src.tools.base_tool import BaseTool
from typing import Dict, Any
import re


class CalculatorTool(BaseTool):
    """Tool to perform mathematical calculations"""
    
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Perform mathematical calculations. Supports +, -, *, /, **, %, etc."
        )
    
    def execute(self, expression: str) -> Dict[str, Any]:
        """
        Execute mathematical calculation
        
        Args:
            expression: Mathematical expression as string (e.g., "2 + 2 * 5")
        
        Returns:
            Dict with calculation result
        """
        try:
            # Validate expression - only allow safe characters
            if not re.match(r'^[0-9+\-*/%().\s]+$', expression):
                return {
                    "status": "error",
                    "error": "Invalid characters in expression"
                }
            
            # Perform calculation
            result = eval(expression)
            
            self.logger.info(f"Calculation: {expression} = {result}")
            
            return {
                "status": "success",
                "expression": expression,
                "result": result,
                "type": type(result).__name__
            }
        
        except ZeroDivisionError:
            self.logger.error("Division by zero attempted")
            return {
                "status": "error",
                "error": "Division by zero error"
            }
        
        except SyntaxError as e:
            self.logger.error(f"Syntax error: {str(e)}")
            return {
                "status": "error",
                "error": "Invalid mathematical expression"
            }
        
        except Exception as e:
            self.logger.error(f"Calculation error: {str(e)}")
            return {
                "status": "error",
                "error": str(e)
            }
