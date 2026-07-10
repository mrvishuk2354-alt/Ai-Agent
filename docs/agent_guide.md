# AI Agent Guide

## Introduction

AI Agent एक powerful framework है जो आपको automated tasks को easily manage करने देता है।

## Basic Usage

### 1. Initialize Agent

```python
from src.agent import AIAgent

# Create agent instance
agent = AIAgent(model="gpt-4", debug=True)
```

### 2. Run Tasks

```python
# Simple calculation
result = agent.run("Calculate 2 + 2")
print(result)

# Text analysis
result = agent.run("Analyze this text: Hello World")
print(result)
```

### 3. Access History

```python
# Get conversation history
history = agent.get_history()
for msg in history:
    print(msg)

# Get statistics
stats = agent.get_stats()
print(stats)
```

## Available Tools

### Calculator Tool

Mathematical calculations करने के लिए:

```python
# Simple operation
result = agent.run("Calculate 10 + 5")

# Complex expression
result = agent.run("Calculate (10 + 20) * 3 - 5")

# Division
result = agent.run("Divide 100 by 5")
```

### Text Analysis Tool

Text को analyze करने के लिए:

```python
# Full analysis
result = agent.run("Analyze: Python is great")

# Word count
result = agent.run("Count words in: The quick brown fox")
```

## Creating Custom Tools

### Step 1: Create Tool Class

```python
from src.tools.base_tool import BaseTool
from typing import Dict, Any

class MyTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="my_tool",
            description="My custom tool description"
        )
    
    def execute(self, **kwargs) -> Dict[str, Any]:
        # Your implementation
        return {"status": "success", "result": "value"}
```

### Step 2: Register Tool

```python
agent = AIAgent()
agent.tool_registry.register("my_tool", MyTool())
```

### Step 3: Use Tool

```python
result = agent.run("Use my_tool to do something")
```

## Configuration

### Environment Variables

`.env` file में set करें:

```env
OPENAI_API_KEY=your_key_here
AGENT_DEBUG=True
AGENT_LOG_LEVEL=INFO
```

## Error Handling

```python
try:
    result = agent.run("Invalid operation")
    if result["status"] == "error":
        print(f"Error: {result['error']}")
except Exception as e:
    print(f"Failed: {str(e)}")
```

## Advanced Features

### Task Logging

सभी tasks automatically log होते हैं:

```python
history = agent.get_history()
for task in history:
    print(f"Task: {task['content']}")
    print(f"Timestamp: {task['timestamp']}")
```

### Statistics

Agent की performance track करें:

```python
stats = agent.get_stats()
print(f"Total tasks: {stats['tasks_completed']}")
print(f"Available tools: {stats['tools_available']}")
```

## Best Practices

1. **Always use try-except blocks**
2. **Check result status before processing**
3. **Log important operations**
4. **Validate input data**
5. **Handle errors gracefully**

## Troubleshooting

### Issue: Tool not found
**Solution:** Ensure tool is registered: `agent.tool_registry.register(name, tool)`

### Issue: Invalid expression
**Solution:** Check expression syntax and characters

### Issue: Memory leak
**Solution:** Periodically clear history: `agent.conversation_history = []`

## FAQ

**Q: कितने tools add कर सकते हैं?**
A: Unlimited - कोई limit नहीं है

**Q: क्या tools async हो सकते हैं?**
A: हाँ, asyncio का उपयोग करें

**Q: History कितना बड़ा हो सकता है?**
A: RAM के साथ limit होती है, जरूरत के अनुसार clear करें
