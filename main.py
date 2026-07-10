"""
Main script to demonstrate and run the AI Agent
"""

from src.agent import AIAgent
import json


def print_header(text):
    """Print formatted header"""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")


def run_example(agent, task):
    """Run a single example and print results"""
    print(f"📝 Task: {task}")
    print("-" * 60)
    
    result = agent.run(task)
    
    print(f"✅ Response:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print()


def main():
    """Main execution function"""
    
    print_header("🤖 AI AGENT - DEMO")
    
    # Initialize agent
    print("🚀 Initializing AI Agent...")
    agent = AIAgent(model="gpt-4", debug=True)
    print(f"✓ {agent}\n")
    
    # Example 1: Show available tools
    print_header("Example 1: Available Tools")
    run_example(agent, "कौन से tools उपलब्ध हैं?")
    
    # Example 2: Simple calculation
    print_header("Example 2: Simple Calculation")
    run_example(agent, "Calculate: 2 + 2 * 5")
    
    # Example 3: Another calculation
    print_header("Example 3: Another Calculation")
    run_example(agent, "मुझे 100 को 5 से divide करना है")
    
    # Example 4: Text analysis
    print_header("Example 4: Text Analysis")
    text = "Artificial Intelligence is revolutionizing the world. Machine learning and deep learning are key technologies. AI is the future of technology."
    run_example(agent, f"Analyze this text: {text}")
    
    # Example 5: Complex expression
    print_header("Example 5: Complex Math Expression")
    run_example(agent, "Calculate (10 + 20) * 3 - 5")
    
    # Example 6: Another text analysis in Hindi
    print_header("Example 6: Hindi Text Analysis")
    hindi_text = "यह एक बहुत ही अद्भुत दिन है। कृत्रिम बुद्धिमत्ता भविष्य का आधार है।"
    run_example(agent, f"Analyze: {hindi_text}")
    
    # Show statistics
    print_header("📊 Agent Statistics")
    stats = agent.get_stats()
    print(json.dumps(stats, indent=2, ensure_ascii=False))
    
    # Show conversation history
    print_header("💬 Conversation History")
    history = agent.get_history()
    for i, msg in enumerate(history, 1):
        role = "👤 User" if msg["role"] == "user" else "🤖 Agent"
        print(f"{i}. {role}: {msg['content'][:60]}...")
    
    print_header("✨ Demo Complete!")


if __name__ == "__main__":
    main()
