# Configuration Guide

This guide explains all configuration options for the AI Research Multi-Agent System.

## Environment Variables

All sensitive configuration is managed through environment variables in a `.env` file.

### Azure OpenAI (GPT-5.2)

```bash
# The endpoint URL for your Azure OpenAI resource
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

# Your Azure OpenAI API key
AZURE_OPENAI_API_KEY=your_api_key_here

# The deployment name for GPT-5.2
AZURE_OPENAI_GPT_DEPLOYMENT=gpt-52

# API version to use
AZURE_OPENAI_API_VERSION=2024-02-01
```

**How to get these values:**
1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to your Azure OpenAI resource
3. Find the endpoint URL in the "Keys and Endpoint" section
4. Copy one of the API keys
5. Note your deployment name from the "Deployments" section

### xAI (Grok 4)

```bash
# Your xAI API key
XAI_API_KEY=your_xai_api_key_here

# The Grok model to use
XAI_GROK_MODEL=grok-4
```

**How to get these values:**
1. Visit [xAI Console](https://console.x.ai)
2. Create an account or sign in
3. Generate an API key
4. Check available models (currently using grok-4)

### Anthropic (Claude)

```bash
# Your Anthropic API key
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Claude model to use
ANTHROPIC_CLAUDE_MODEL=claude-3-opus-20240229
```

**How to get these values:**
1. Visit [Anthropic Console](https://console.anthropic.com)
2. Create an account or sign in
3. Generate an API key from the API keys section
4. Choose your preferred Claude model version

**Available Claude models:**
- `claude-3-opus-20240229` - Most capable, best for complex tasks
- `claude-3-sonnet-20240229` - Balanced performance and speed
- `claude-3-haiku-20240229` - Fastest, good for simple tasks

### Arbiter Model Selection

```bash
# Choose which model to use as the arbiter/mediator
# Options: claude, gpt, or grok
ARBITER_MODEL=claude
```

**How to choose:**
The arbiter/mediator agent is responsible for cross-questioning search agents, validating results, and synthesizing final answers. You can choose any of the three available models:

- `claude` (default) - Uses Claude for mediation, excellent at critical analysis and synthesis
- `gpt` - Uses GPT-5.2 for mediation, good for balanced and comprehensive validation
- `grok` - uses Grok 4 for mediation, provides alternative perspectives in validation

Simply change the `ARBITER_MODEL` value to switch between models without any code changes.

### Bing Search API

```bash
# Your Bing Search API key
BING_SEARCH_API_KEY=your_bing_search_api_key_here

# Bing Search endpoint (usually doesn't need to change)
BING_SEARCH_ENDPOINT=https://api.bing.microsoft.com/v7.0/search
```

**How to get these values:**
1. Go to [Azure Portal](https://portal.azure.com)
2. Create a "Bing Search v7" resource
3. Get the API key from "Keys and Endpoint"
4. The endpoint is usually the default shown above

## Agent Configuration

### Temperature Settings

Temperature controls randomness in responses (0.0 to 1.0):

```python
# More focused and deterministic (good for factual research)
"temperature": 0.3

# Balanced (default for most use cases)
"temperature": 0.7

# More creative and diverse (good for brainstorming)
"temperature": 0.9
```

**Recommended settings:**
- GPT Researcher: 0.7 (balanced research)
- Grok Researcher: 0.7 (alternative perspectives)
- Claude Mediator: 0.5 (focused validation)

### Timeout Settings

Control how long to wait for API responses (in seconds):

```python
"timeout": 120  # 2 minutes (default)
"timeout": 180  # 3 minutes (for complex queries)
"timeout": 60   # 1 minute (for simple queries)
```

### Max Rounds

Control conversation length:

```python
max_rounds = 8   # Quick research (3-5 minutes)
max_rounds = 12  # Standard research (5-10 minutes)
max_rounds = 20  # Deep research (15-30 minutes)
```

## Advanced Configuration

### Custom System Messages

Modify agent behavior by editing system messages in `src/agents.py`:

```python
# Example: Make GPT researcher more technical
gpt_researcher = ConversableAgent(
    name="GPT_Researcher",
    system_message="""You are a technical research specialist.
    Focus on:
    - Technical accuracy and precision
    - Academic and peer-reviewed sources
    - Detailed explanations of complex concepts
    - Mathematical and scientific rigor
    """,
    llm_config=gpt52_config,
)
```

### Speaker Selection Methods

Control how agents take turns:

```python
# Automatic selection based on context (default)
speaker_selection_method="auto"

# Round-robin (each agent speaks in order)
speaker_selection_method="round_robin"

# Manual selection (for custom logic)
speaker_selection_method="manual"
```

### Bing Search Parameters

Customize search behavior in `src/tools.py`:

```python
def bing_search(query: str, count: int = 5, mkt: str = "en-US") -> str:
    params = {
        "q": query,
        "count": count,      # Number of results (1-50)
        "mkt": mkt,         # Market (en-US, en-GB, etc.)
        "safeSearch": "Moderate",  # Off, Moderate, Strict
        "freshness": "Month",       # Day, Week, Month (optional)
    }
```

## Configuration Profiles

### Profile: Fast Research

For quick, high-level answers:

```python
config = {
    "temperature": 0.5,
    "timeout": 60,
    "max_rounds": 8,
}
```

### Profile: Balanced Research

For most use cases:

```python
config = {
    "temperature": 0.7,
    "timeout": 120,
    "max_rounds": 12,
}
```

### Profile: Deep Research

For comprehensive analysis:

```python
config = {
    "temperature": 0.6,
    "timeout": 180,
    "max_rounds": 20,
}
```

### Profile: Creative Exploration

For brainstorming and ideation:

```python
config = {
    "temperature": 0.9,
    "timeout": 120,
    "max_rounds": 15,
}
```

## Cost Optimization

### Tips to Reduce API Costs

1. **Use appropriate models:**
   - Consider Claude Haiku instead of Opus for simpler tasks
   - Use smaller models when possible

2. **Limit conversation rounds:**
   ```python
   max_rounds = 8  # Instead of 20
   ```

3. **Reduce search count:**
   ```python
   bing_search(query, count=3)  # Instead of 5
   ```

4. **Use caching:**
   - Store and reuse results when possible
   - Implement response caching for repeated queries

5. **Set reasonable timeouts:**
   ```python
   "timeout": 60  # Don't wait too long
   ```

## Security Best Practices

1. **Never commit `.env` file:**
   - Already in `.gitignore`
   - Use `.env.example` as template

2. **Rotate API keys regularly:**
   - Set reminders to update keys
   - Use different keys for dev/prod

3. **Limit API permissions:**
   - Use read-only keys when possible
   - Set up usage limits and alerts

4. **Monitor usage:**
   - Check API dashboards regularly
   - Set up cost alerts

## Troubleshooting Configuration

### Problem: "API key not found"

**Solution:**
```bash
# Check .env file exists
ls -la .env

# Check file is loaded
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv('AZURE_OPENAI_API_KEY'))"
```

### Problem: "Connection timeout"

**Solution:**
```python
# Increase timeout
"timeout": 180  # 3 minutes instead of 2
```

### Problem: "Rate limit exceeded"

**Solution:**
- Add delays between requests
- Reduce max_rounds
- Upgrade API tier if available

### Problem: "Invalid model name"

**Solution:**
- Check model names in API documentation
- Verify deployment names in Azure Portal
- Ensure model versions are current

## Configuration Validation

Use this script to validate your configuration:

```python
import os
from dotenv import load_dotenv

load_dotenv()

required_vars = [
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_OPENAI_API_KEY",
    "XAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "BING_SEARCH_API_KEY",
]

missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    print(f"Missing variables: {', '.join(missing)}")
else:
    print("✓ All required variables are set!")
```

## Environment-Specific Configuration

### Development

```bash
# .env.development
AZURE_OPENAI_GPT_DEPLOYMENT=gpt-4-dev
MAX_ROUNDS=8
TIMEOUT=60
```

### Production

```bash
# .env.production
AZURE_OPENAI_GPT_DEPLOYMENT=gpt-52
MAX_ROUNDS=15
TIMEOUT=180
```

Load specific environment:

```python
from dotenv import load_dotenv
load_dotenv('.env.production')
```

---

For more information, see:
- [Azure OpenAI Configuration](https://learn.microsoft.com/azure/ai-services/openai/)
- [Anthropic API Configuration](https://docs.anthropic.com/)
- [Bing Search API](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api)
