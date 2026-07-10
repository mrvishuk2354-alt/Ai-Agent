# AI Agent 🤖

एक powerful और flexible AI Agent जो विभिन्न tasks को automatically handle कर सकता है।

## Features ✨

- **Multi-tool Support**: विभिन्न tools का उपयोग करके complex tasks को solve करें
- **Conversational AI**: Natural language processing के साथ intelligent conversations
- **Task Planning**: स्वचालित रूप से tasks को plan और execute करें
- **Error Handling**: Robust error handling और recovery mechanisms
- **Logging**: Detailed logs के लिए comprehensive logging system

## Architecture 🏗️

```
├── src/
│   ├── agent/           # Core agent logic
│   ├── tools/           # Tool implementations
│   ├── llm/             # LLM integrations
│   ├── utils/           # Utility functions
│   └── config/          # Configuration files
├── tests/               # Unit tests
├── examples/            # Usage examples
└── requirements.txt     # Python dependencies
```

## Installation 📦

```bash
# Clone the repository
git clone https://github.com/mrvishuk2354-alt/Ai-Agent.git
cd Ai-Agent

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

## Quick Start 🚀

```python
from src.agent import AIAgent

# Initialize agent
agent = AIAgent(model="gpt-4", debug=True)

# Run a task
result = agent.run("आपका task यहाँ लिखें")
print(result)
```

## Documentation 📚

- [Agent Guide](./docs/agent_guide.md)
- [Tool Development](./docs/tools_development.md)
- [API Reference](./docs/api_reference.md)

## Configuration ⚙️

Environment variables की जानकारी `.env.example` में दी गई है।

## License 📄

MIT License

## Author 👨‍💻

[Your Name]
