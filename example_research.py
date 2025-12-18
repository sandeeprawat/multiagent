"""
Example script demonstrating how to use the AI Research Multi-Agent System.

This script shows how to:
1. Load environment variables
2. Configure the agents
3. Conduct research on a topic
4. Save results
"""

import os
from dotenv import load_dotenv
from src.agents import create_research_agents, conduct_research
from src.tools import save_research_results

# Load environment variables
load_dotenv()


def main():
    """Main function to run the research example."""
    
    # Configure GPT-5.2 (Azure OpenAI)
    gpt52_config = {
        "config_list": [
            {
                "model": os.getenv("AZURE_OPENAI_GPT_DEPLOYMENT", "gpt-52"),
                "api_type": "azure",
                "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
                "base_url": os.getenv("AZURE_OPENAI_ENDPOINT"),
                "api_version": os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
            }
        ],
        "temperature": 0.7,
        "timeout": 120,
    }

    # Configure Grok 4 (xAI)
    grok4_config = {
        "config_list": [
            {
                "model": os.getenv("XAI_GROK_MODEL", "grok-4"),
                "api_key": os.getenv("XAI_API_KEY"),
                "base_url": "https://api.x.ai/v1",
            }
        ],
        "temperature": 0.7,
        "timeout": 120,
    }

    # Configure Claude (Anthropic)
    claude_config = {
        "config_list": [
            {
                "model": os.getenv("ANTHROPIC_CLAUDE_MODEL", "claude-3-opus-20240229"),
                "api_key": os.getenv("ANTHROPIC_API_KEY"),
                "api_type": "anthropic",
            }
        ],
        "temperature": 0.5,
        "timeout": 120,
    }

    # Create agents
    print("Creating research agents...")
    arbiter_model = os.getenv("ARBITER_MODEL", "claude").lower()
    print(f"Using {arbiter_model.upper()} as arbiter/mediator model")
    agents = create_research_agents(gpt52_config, grok4_config, claude_config, arbiter_model)
    print("Agents created successfully!")

    # Define research topic
    topic = "What are the latest advancements in quantum computing in 2024?"
    print(f"\nResearch Topic: {topic}")
    print("=" * 80)

    # Conduct research
    print("\nStarting research...")
    results = conduct_research(
        topic=topic,
        agents=agents,
        manager_config=gpt52_config,
        max_rounds=15
    )

    # Display results
    print("\n" + "=" * 80)
    print("RESEARCH COMPLETE")
    print("=" * 80)
    
    print("\nConversation History:")
    for i, message in enumerate(results["chat_history"], 1):
        speaker = message.get("name", "Unknown")
        content = message.get("content", "")
        print(f"\n[{i}] {speaker}:")
        print("-" * 80)
        print(content)

    print("\n" + "=" * 80)
    print("Summary:")
    print("=" * 80)
    print(results.get("summary", "No summary available"))

    # Save results
    output_file = save_research_results(results)
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()
