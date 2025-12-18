"""
Agent creation and management for the multi-agent research system.
"""

import os
from typing import Dict, Any, List
from autogen import ConversableAgent, GroupChat, GroupChatManager
from .tools import bing_search


def create_research_agents(
    gpt_config: Dict[str, Any],
    grok_config: Dict[str, Any],
    claude_config: Dict[str, Any]
) -> Dict[str, ConversableAgent]:
    """
    Create all research agents for the multi-agent system.
    
    Args:
        gpt_config: Configuration for GPT-5.2 agent
        grok_config: Configuration for Grok 4 agent
        claude_config: Configuration for Claude mediator
    
    Returns:
        Dictionary of agent name to agent instance
    """
    # GPT-5.2 Search Agent
    gpt_researcher = ConversableAgent(
        name="GPT_Researcher",
        system_message="""You are a primary research agent powered by GPT-5.2.
        Your role is to conduct thorough research on given topics using web search.
        When researching:
        1. Use the bing_search function to find relevant information
        2. Analyze and synthesize information from multiple sources
        3. Provide well-structured, evidence-based insights
        4. Cite your sources clearly
        5. Be open to critique and validation from other agents
        """,
        llm_config=gpt_config,
        human_input_mode="NEVER",
    )

    # Grok 4 Search Agent
    grok_researcher = ConversableAgent(
        name="Grok_Researcher",
        system_message="""You are a secondary research agent powered by Grok 4.
        Your role is to provide alternative perspectives and complementary research.
        When researching:
        1. Use the bing_search function to find relevant information
        2. Focus on different angles than the primary researcher
        3. Look for counterarguments and alternative viewpoints
        4. Validate or challenge findings from other agents
        5. Provide unique insights and analysis
        """,
        llm_config=grok_config,
        human_input_mode="NEVER",
    )

    # Claude Mediator/Arbiter Agent
    claude_mediator = ConversableAgent(
        name="Claude_Mediator",
        system_message="""You are a mediator and arbiter powered by Claude.
        Your role is to:
        1. Cross-question the search agents to probe their findings
        2. Identify inconsistencies or gaps in their research
        3. Validate results by comparing different agents' outputs
        4. Synthesize a final, well-reasoned answer
        5. Ask clarifying questions when needed
        6. Ensure the research is comprehensive and balanced
        
        You should be critical, thorough, and impartial in your mediation.
        """,
        llm_config=claude_config,
        human_input_mode="NEVER",
    )

    # User proxy for initiating research
    user_proxy = ConversableAgent(
        name="User",
        system_message="You are a user who initiates research tasks.",
        llm_config=False,
        human_input_mode="NEVER",
        is_termination_msg=lambda msg: "TERMINATE" in msg.get("content", ""),
    )

    # Register the bing_search function with all agents
    for agent in [gpt_researcher, grok_researcher, claude_mediator]:
        agent.register_for_llm(
            name="bing_search",
            description="Search the web using Bing to find relevant information on a topic."
        )(bing_search)

    user_proxy.register_for_execution(name="bing_search")(bing_search)

    return {
        "gpt_researcher": gpt_researcher,
        "grok_researcher": grok_researcher,
        "claude_mediator": claude_mediator,
        "user_proxy": user_proxy,
    }


def conduct_research(
    topic: str,
    agents: Dict[str, ConversableAgent],
    manager_config: Dict[str, Any],
    max_rounds: int = 12
) -> Dict[str, Any]:
    """
    Conduct multi-agent research on a given topic.
    
    Args:
        topic: Research topic/question
        agents: Dictionary of agent instances
        manager_config: Configuration for the group chat manager
        max_rounds: Maximum number of conversation rounds
    
    Returns:
        Dictionary containing research results and conversation history
    """
    # Create group chat
    group_chat = GroupChat(
        agents=[
            agents["user_proxy"],
            agents["gpt_researcher"],
            agents["grok_researcher"],
            agents["claude_mediator"]
        ],
        messages=[],
        max_round=max_rounds,
        speaker_selection_method="auto",
    )

    # Create group chat manager
    manager = GroupChatManager(
        groupchat=group_chat,
        llm_config=manager_config,
    )

    # Initiate the research
    research_prompt = f"""
    Research Topic: {topic}
    
    Instructions for the team:
    1. GPT_Researcher: Begin by searching for and analyzing information on this topic
    2. Grok_Researcher: Provide complementary research and alternative perspectives
    3. Claude_Mediator: Cross-question both researchers, validate findings, and synthesize final answer
    
    Please collaborate to provide a comprehensive, well-researched answer.
    End with "TERMINATE" when the research is complete.
    """

    # Start the conversation
    chat_result = agents["user_proxy"].initiate_chat(
        manager,
        message=research_prompt,
    )

    return {
        "topic": topic,
        "chat_history": chat_result.chat_history,
        "summary": chat_result.summary,
    }
