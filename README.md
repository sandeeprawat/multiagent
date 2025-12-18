# AI Research Multi-Agent System

A Jupyter notebook-based AI research system using Microsoft Agent Framework (Autogen) with multi-agent design patterns. This project implements a collaborative research workflow using Azure AI Foundry models with Bing search grounding.

## Overview

This project demonstrates a sophisticated multi-agent system for conducting AI-powered research:

- **GPT-5.2 Search Agent**: Primary research agent powered by Azure OpenAI, grounded with Bing search
- **Grok 4 Search Agent**: Secondary research agent powered by xAI, grounded with Bing search  
- **Flexible Arbiter/Mediator**: Configurable arbiter model (Claude, GPT, or Grok) that cross-questions search agents and validates results

## Features

- 🔍 **Web-Grounded Research**: Agents use Bing Search API to access real-time information
- 🤖 **Multi-Agent Collaboration**: Multiple AI models work together to provide comprehensive answers
- ⚖️ **Validation & Mediation**: Configurable arbiter (Claude/GPT/Grok) ensures quality and accuracy
- 🔧 **Flexible Configuration**: Switch arbiter model with a simple environment variable change
- 📊 **Structured Workflow**: Organized conversation flow with clear roles and responsibilities
- 💾 **Export Capabilities**: Save research results for later analysis

## Architecture

```
┌─────────────────┐
│  User Query     │
└────────┬────────┘
         │
    ┌────▼────────────────────────────────┐
    │   Group Chat Manager (GPT-5.2)      │
    └────┬────────────────────────────────┘
         │
    ┌────▼──────────────────────────────────────┐
    │                                            │
┌───▼────────────┐  ┌─────────────┐  ┌─────────▼────────┐
│ GPT Researcher │  │    Grok     │  │ Claude Mediator  │
│   (GPT-5.2)    │  │ Researcher  │  │   (Arbiter)      │
│                │  │  (Grok 4)   │  │                  │
│ + Bing Search  │  │ + Bing      │  │ Cross-questions  │
│                │  │   Search    │  │ & Validates      │
└────────────────┘  └─────────────┘  └──────────────────┘
```

## Prerequisites

- Python 3.9 or higher
- Jupyter Notebook
- API Keys for:
  - Azure OpenAI (GPT-5.2)
  - xAI (Grok 4)
  - Anthropic (Claude)
  - Bing Search API

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sandeeprawat/multiagent.git
   cd multiagent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook ai_research_multiagent.ipynb
   ```

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

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

# Arbiter Model Selection (claude, gpt, or grok)
ARBITER_MODEL=claude

# Bing Search API
BING_SEARCH_API_KEY=your_bing_search_api_key_here
BING_SEARCH_ENDPOINT=https://api.bing.microsoft.com/v7.0/search
```

## Usage

### Basic Research

```python
# Define your research topic
topic = "What are the latest advancements in quantum computing in 2024?"

# Conduct research
results = conduct_research(topic, max_rounds=15)

# View results
print(results["summary"])
```

### Custom Agent Configuration

```python
# Create a custom research agent
custom_agent = create_custom_researcher(
    name="Custom_Researcher",
    system_message="Your custom instructions here",
    config=gpt52_config
)
```

### Export Results

```python
# Save research to file
save_research_results(results, "my_research.json")
```

## How It Works

1. **User Initiates**: Research question is submitted to the system
2. **GPT Researcher**: Searches Bing and provides initial research findings
3. **Grok Researcher**: Adds complementary research and alternative perspectives
4. **Claude Mediator**: 
   - Cross-questions both researchers
   - Identifies gaps or inconsistencies
   - Validates findings
   - Synthesizes final comprehensive answer
5. **Results**: Complete conversation history and summary are returned

## Agent Roles

### GPT-5.2 Search Agent
- Primary researcher
- Conducts thorough web searches
- Analyzes and synthesizes information
- Provides evidence-based insights

### Grok 4 Search Agent
- Secondary researcher
- Offers alternative perspectives
- Looks for counterarguments
- Validates or challenges other findings

### Claude Mediator
- Acts as arbiter and critic (configurable to use Claude, GPT, or Grok)
- Cross-questions research agents
- Identifies inconsistencies
- Synthesizes final answer
- Ensures comprehensive coverage

## Spec-Kit Integration

This project is built following the [Spec-Kit](https://github.com/github/spec-kit) starter project guidelines for AI applications:

- Clear documentation structure
- Environment-based configuration
- Modular design patterns
- Example usage included
- Best practices for AI agent development

## Project Structure

```
multiagent/
├── ai_research_multiagent.ipynb  # Main Jupyter notebook
├── requirements.txt               # Python dependencies
├── pyproject.toml                # Project configuration
├── .env.example                  # Example environment variables
├── README.md                     # This file
└── .gitignore                    # Git ignore rules
```

## Best Practices

1. **API Key Security**: Never commit API keys to version control
2. **Rate Limiting**: Be mindful of API rate limits
3. **Cost Management**: Monitor API usage to control costs
4. **Error Handling**: The notebook includes basic error handling for search failures
5. **Iterative Refinement**: Use multiple rounds to get comprehensive results

## Troubleshooting

### Common Issues

**API Key Errors**
- Verify all API keys are correctly set in `.env`
- Check that the `.env` file is in the project root

**Search Not Working**
- Confirm Bing Search API key is valid
- Check endpoint URL is correct

**Timeout Errors**
- Increase timeout values in agent configurations
- Check internet connectivity

**Rate Limit Errors**
- Add delays between requests
- Use lower max_rounds values

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Resources

- [Microsoft AutoGen Documentation](https://microsoft.github.io/autogen/)
- [Azure AI Foundry](https://learn.microsoft.com/azure/ai-services/)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [xAI Documentation](https://docs.x.ai/)
- [Bing Search API](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api)
- [Spec-Kit Starter](https://github.com/github/spec-kit)

## Support

For issues and questions:
- Open an issue in the GitHub repository
- Check existing issues for solutions
- Review the troubleshooting section above

---

**Note**: This is a research and development project. Ensure you have appropriate API access and understand the costs associated with using these AI services.