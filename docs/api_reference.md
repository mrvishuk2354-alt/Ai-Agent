# API Reference

## AIAgent Class

### Initialization

```python
AIAgent(model: str = "gpt-4", debug: bool = False)
```

**Parameters:**
- `model` (str): LLM model to use
- `debug` (bool): Enable debug mode

**Example:**
```python
agent = AIAgent(model="gpt-4", debug=True)
```

### Methods

#### `run(task: str) -> Dict[str, Any]`

Run a task or query.

**Parameters:**
- `task` (str): Task description

**Returns:** Result dictionary

**Example:**
```python
result = agent.run("Calculate 10 + 5")
```

#### `get_history() -> List[Dict]`

Get conversation history.

**Returns:** List of message dictionaries

**Example:**
```python
history = agent.get_history()
```

#### `get_stats() -> Dict[str, Any]`

Get agent statistics.

**Returns:** Statistics dictionary

**Example:**
```python
stats = agent.get_stats()
print(stats["tasks_completed"])
```

## ToolRegistry Class

### Methods

#### `register(name: str, tool: BaseTool)`

Register a new tool.

**Example:**
```python
tool = MyTool()
agent.tool_registry.register("my_tool", tool)
```

#### `get_tool(name: str) -> BaseTool`

Get a tool by name.

**Example:**
```python
tool = agent.tool_registry.get_tool("calculator")
```

#### `use_tool(name: str, **kwargs) -> Dict`

Execute a tool.

**Example:**
```python
result = agent.tool_registry.use_tool("calculator", expression="2+2")
```

#### `list_tools() -> Dict`

List all available tools.

**Example:**
```python
tools = agent.tool_registry.list_tools()
```

## BaseTool Class

### Abstract Methods

#### `execute(**kwargs) -> Dict[str, Any]`

Must be implemented by subclasses.

**Returns:** Result dictionary with structure:
```python
{
    "status": "success" | "error",
    "result": any,
    "error": optional_error_message
}
```

## Tool Response Format

### Success Response

```json
{
    "status": "success",
    "tool_used": "tool_name",
    "result": {
        // Tool-specific result data
    }
}
```

### Error Response

```json
{
    "status": "error",
    "error": "Error message",
    "tool_used": "tool_name"
}
```

## Constants

### Tool Names

- `"calculator"` - Mathematical calculations
- `"text_analysis"` - Text analysis

### Status Values

- `"success"` - Operation successful
- `"error"` - Operation failed
- `"info"` - Information message
