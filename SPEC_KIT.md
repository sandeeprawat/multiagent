# Spec-Kit Starter Project

This project follows the [Spec-Kit](https://github.com/github/spec-kit) starter project guidelines for AI applications.

## What is Spec-Kit?

Spec-Kit is a GitHub initiative to provide standardized starter templates for AI projects. It ensures:

- **Clear Documentation**: README, getting started guides, and examples
- **Environment-based Configuration**: Secure API key management
- **Modular Design**: Reusable components and clear separation of concerns
- **Best Practices**: Following industry standards for AI development

## How This Project Follows Spec-Kit

### 1. Project Structure

```
multiagent/
├── ai_research_multiagent.ipynb  # Main Jupyter notebook interface
├── src/                          # Modular Python package
│   ├── __init__.py
│   ├── agents.py                 # Agent creation and management
│   └── tools.py                  # Utility functions and tools
├── example_research.py           # Example usage script
├── requirements.txt              # Dependencies
├── pyproject.toml               # Project metadata and config
├── .env.example                 # Example environment variables
├── README.md                    # Main documentation
├── GETTING_STARTED.md          # Quick start guide
└── SPEC_KIT.md                 # This file
```

### 2. Documentation

- **README.md**: Comprehensive overview, features, and usage
- **GETTING_STARTED.md**: Step-by-step setup and examples
- **Code Comments**: Docstrings and inline documentation
- **Example Notebook**: Interactive tutorial with explanations

### 3. Configuration Management

- Environment variables via `.env` file
- Example configuration in `.env.example`
- No hardcoded API keys or secrets
- Clear separation of config from code

### 4. Modular Design

- **agents.py**: Agent creation logic
- **tools.py**: Reusable utilities
- **Notebook**: User-friendly interface
- **Example script**: Programmatic usage

### 5. Dependencies

- Clearly defined in `requirements.txt`
- Version constraints for reproducibility
- Optional dev dependencies in `pyproject.toml`

### 6. Best Practices

#### Security
- API keys in environment variables
- `.env` excluded from git via `.gitignore`
- No credentials in code or notebooks

#### Code Quality
- Type hints in function signatures
- Docstrings for all public functions
- Clear variable and function names
- Logical file organization

#### User Experience
- Multiple entry points (notebook, script)
- Clear error messages
- Example usage included
- Troubleshooting guide

#### Reproducibility
- Pinned dependency versions
- Environment configuration examples
- Clear setup instructions

## AI Application Patterns

This project demonstrates several AI application patterns:

### Multi-Agent Collaboration

```python
# Multiple AI models work together
agents = {
    "gpt_researcher": GPT-5.2 Agent,
    "grok_researcher": Grok 4 Agent,
    "claude_mediator": Claude Agent,
}
```

### Tool Integration

```python
# Agents can use external tools
@tool
def bing_search(query: str) -> str:
    # Search the web for information
    ...
```

### Conversation Management

```python
# Structured conversation flow
group_chat = GroupChat(
    agents=[...],
    max_round=12,
    speaker_selection_method="auto",
)
```

## Extending This Project

### Add New Agents

```python
# In src/agents.py
new_agent = ConversableAgent(
    name="New_Agent",
    system_message="Agent instructions",
    llm_config=config,
)
```

### Add New Tools

```python
# In src/tools.py
def new_tool(param: str) -> str:
    """Tool description."""
    # Implementation
    return result
```

### Customize Workflow

```python
# In notebook or script
custom_workflow = GroupChat(
    agents=custom_agents,
    max_round=custom_rounds,
    speaker_selection_method="round_robin",
)
```

## Spec-Kit Checklist

This project implements:

- [x] Clear README with overview and usage
- [x] Getting started guide
- [x] Example code and notebooks
- [x] Environment-based configuration
- [x] Modular code structure
- [x] Type hints and documentation
- [x] Dependency management
- [x] Security best practices
- [x] .gitignore for sensitive files
- [x] Troubleshooting guide
- [x] Multiple usage patterns (notebook + script)
- [x] Error handling
- [x] Extensibility examples

## Contributing

When contributing to this project, please maintain the Spec-Kit standards:

1. **Documentation**: Update relevant docs when adding features
2. **Examples**: Include usage examples for new features
3. **Configuration**: Use environment variables for config
4. **Modularity**: Keep code organized and reusable
5. **Type Hints**: Add type annotations
6. **Docstrings**: Document all public functions

## Resources

- [Spec-Kit Repository](https://github.com/github/spec-kit)
- [Microsoft AutoGen](https://microsoft.github.io/autogen/)
- [Azure AI Best Practices](https://learn.microsoft.com/azure/ai-services/)
- [Python Packaging Guide](https://packaging.python.org/)

---

This project is designed to be a starting point for AI research applications. Feel free to extend and customize it for your specific needs while maintaining the Spec-Kit structure and best practices.
