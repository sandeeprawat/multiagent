# Getting Started with AI Research Multi-Agent System

This guide will help you get started with the AI Research Multi-Agent System.

## Quick Start

### 1. Prerequisites

Make sure you have:
- Python 3.9 or higher
- pip package manager
- API keys for Azure OpenAI, xAI, Anthropic, and Bing Search

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/sandeeprawat/multiagent.git
cd multiagent

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and fill in your API keys:

```bash
# Azure OpenAI (GPT-5.2)
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_GPT_DEPLOYMENT=gpt-52
AZURE_OPENAI_API_VERSION=2024-02-01

# xAI (Grok 4)
XAI_API_KEY=your_xai_api_key_here
XAI_GROK_MODEL=grok-4

# Anthropic (Claude)
ANTHROPIC_API_KEY=your_anthropic_api_key_here
ANTHROPIC_CLAUDE_MODEL=claude-3-opus-20240229

# Bing Search API
BING_SEARCH_API_KEY=your_bing_search_api_key_here
BING_SEARCH_ENDPOINT=https://api.bing.microsoft.com/v7.0/search
```

### 4. Run the Example

#### Option A: Using Jupyter Notebook (Recommended)

```bash
jupyter notebook ai_research_multiagent.ipynb
```

Then run all cells in the notebook.

#### Option B: Using Python Script

```bash
python example_research.py
```

## Understanding the System

### Agent Roles

1. **GPT Researcher (GPT-5.2)**
   - Primary research agent
   - Searches web using Bing
   - Provides initial comprehensive research

2. **Grok Researcher (Grok 4)**
   - Secondary research agent
   - Offers alternative perspectives
   - Challenges or validates primary research

3. **Claude Mediator**
   - Acts as arbiter and critic
   - Cross-questions both researchers
   - Synthesizes final answer

### Workflow

```
1. User submits research question
   ↓
2. GPT Researcher conducts initial research
   ↓
3. Grok Researcher provides complementary research
   ↓
4. Claude Mediator cross-questions both
   ↓
5. Agents collaborate to refine answer
   ↓
6. Claude synthesizes final comprehensive answer
```

## Customization

### Adjust Agent Temperature

In your configuration, modify the `temperature` parameter:

```python
gpt52_config = {
    "config_list": [...],
    "temperature": 0.7,  # Lower = more focused, Higher = more creative
}
```

### Change Max Rounds

Increase or decrease conversation rounds:

```python
results = conduct_research(
    topic=topic,
    agents=agents,
    manager_config=gpt52_config,
    max_rounds=20  # Default is 12
)
```

### Modify System Messages

Edit the system messages in `src/agents.py` to change agent behavior.

## Common Use Cases

### Academic Research

```python
topic = "What are the implications of CRISPR gene editing in 2024?"
results = conduct_research(topic, agents, gpt52_config)
```

### Technology Analysis

```python
topic = "Compare the latest AI model architectures and their performance"
results = conduct_research(topic, agents, gpt52_config)
```

### Market Research

```python
topic = "What are the current trends in renewable energy investments?"
results = conduct_research(topic, agents, gpt52_config)
```

## Tips for Better Results

1. **Be Specific**: Ask focused questions for better results
2. **Increase Rounds**: Complex topics may need more conversation rounds
3. **Review Logs**: Check conversation history to understand agent reasoning
4. **Iterate**: Refine your questions based on initial results

## Troubleshooting

### "API Key Error"
- Check that all API keys are set in `.env`
- Verify the `.env` file is in the project root

### "No search results"
- Verify Bing Search API key is valid
- Check your internet connection

### "Timeout errors"
- Increase timeout in agent configs
- Check API service status

## Next Steps

1. Experiment with different research topics
2. Customize agent system messages
3. Add more agents for specialized tasks
4. Integrate with your own data sources

## Resources

- [Full Documentation](README.md)
- [Microsoft AutoGen Docs](https://microsoft.github.io/autogen/)
- [Azure AI Services](https://learn.microsoft.com/azure/ai-services/)
- [Example Notebook](ai_research_multiagent.ipynb)
