#!/usr/bin/env python3
"""
Interactive Demo Script - Run and test the AI Agent
"""

import sys
import json
from src.agent import AIAgent


def print_section(title):
    """Print section header"""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def run_demo():
    """Run complete demo"""
    
    print_section("🤖 AI AGENT - COMPLETE DEMO")
    
    # Initialize agent
    print("📦 Initializing AI Agent...")
    agent = AIAgent(model="gpt-4", debug=True)
    print(f"✅ Agent initialized: {agent}\n")
    
    # Demo tasks
    demo_tasks = [
        ("Calculate: 2 + 2", "Simple Addition"),
        ("Calculate 15 * 3 + 5", "Complex Math Expression"),
        ("Divide 100 by 5", "Division Operation"),
        ("मुझे 50 को 10 से multiply करना है", "Hindi - Multiplication"),
        ("Analyze text: Artificial Intelligence is transforming technology", "Text Analysis"),
        ("Show available tools", "List Tools"),
    ]
    
    # Run each demo task
    for i, (task, description) in enumerate(demo_tasks, 1):
        print_section(f"Demo #{i}: {description}")
        print(f"📝 Task: {task}")
        print("-" * 70)
        
        result = agent.run(task)
        
        print(f"✅ Response:")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print()
    
    # Show statistics
    print_section("📊 Agent Statistics")
    stats = agent.get_stats()
    for key, value in stats.items():
        print(f"  • {key}: {value}")
    print()
    
    # Show conversation history
    print_section("💬 Conversation History")
    history = agent.get_history()
    print(f"Total exchanges: {len(history)}\n")
    
    for idx, msg in enumerate(history, 1):
        role_emoji = "👤" if msg["role"] == "user" else "🤖"
        role_text = "User" if msg["role"] == "user" else "Agent"
        content_preview = msg["content"]
        if isinstance(content_preview, dict):
            content_preview = json.dumps(content_preview, ensure_ascii=False)[:60] + "..."
        else:
            content_preview = str(content_preview)[:60] + "..."
        
        print(f"{idx}. {role_emoji} {role_text}:")
        print(f"   {content_preview}")
        print()
    
    print_section("✨ Demo Completed Successfully!")
    print("🎉 AI Agent is working perfectly!")
    print("\n📚 Next steps:")
    print("  1. Try: python demo.py")
    print("  2. Read: README.md")
    print("  3. Explore: src/ directory")
    print("  4. Create custom tools in: src/tools/")
    print()


if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\n❌ Demo interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error during demo: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
