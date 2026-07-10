"""
Text Analysis Tool - Analyze and process text
"""

from src.tools.base_tool import BaseTool
from typing import Dict, Any
import re
from collections import Counter


class TextAnalysisTool(BaseTool):
    """Tool to analyze text content"""
    
    def __init__(self):
        super().__init__(
            name="text_analysis",
            description="Analyze text - word count, character count, sentiment, keywords, etc."
        )
    
    def execute(self, text: str, analysis_type: str = "full") -> Dict[str, Any]:
        """
        Execute text analysis
        
        Args:
            text: Text to analyze
            analysis_type: Type of analysis - 'full', 'stats', 'keywords'
        
        Returns:
            Dict with analysis results
        """
        try:
            if not text or not isinstance(text, str):
                return {
                    "status": "error",
                    "error": "Invalid text input"
                }
            
            results = {"status": "success", "analysis_type": analysis_type}
            
            # Basic statistics
            words = text.split()
            sentences = re.split(r'[.!?]+', text)
            characters = len(text)
            
            if analysis_type in ["full", "stats"]:
                results["statistics"] = {
                    "word_count": len(words),
                    "character_count": characters,
                    "sentence_count": len([s for s in sentences if s.strip()]),
                    "average_word_length": characters / len(words) if words else 0
                }
            
            if analysis_type in ["full", "keywords"]:
                # Extract keywords (common words)
                stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'is', 'was'}
                keywords = [w.lower() for w in words if w.lower() not in stop_words and len(w) > 3]
                word_freq = Counter(keywords)
                
                results["keywords"] = dict(word_freq.most_common(10))
            
            self.logger.info(f"Text analysis completed: {len(words)} words")
            
            return results
        
        except Exception as e:
            self.logger.error(f"Analysis error: {str(e)}")
            return {
                "status": "error",
                "error": str(e)
            }
