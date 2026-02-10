# AI Copilot Instructions for LangChain Chat Models Project

## Project Overview
A Python project demonstrating LangChain integration with multiple LLM providers (Hugging Face, OpenAI, Anthropic, Google Gemini). Currently focused on testing text generation pipelines with model inference.

## Architecture & Key Components

### Model Integration Pattern
- **Entry point**: [chatmodels.py](../../chatmodels.py) - demonstrates Hugging Face pipeline integration
- **LLM Providers**: Supports multiple backends via LangChain:
  - `langchain-openai` for OpenAI models
  - `langchain-anthropic` for Claude
  - `langchain-google-genai` for Gemini
  - `langchain-huggingface` for Hugging Face models
- **Current Implementation**: Uses `google/flan-t5-small` model with `transformers.pipeline()`

### Dependency Structure
Dependencies are organized in [requirements.txt](../../requirements.txt) by category:
1. **Core**: `langchain`, `langchain-core` (base framework)
2. **Provider Integrations**: Provider-specific packages + base SDK (e.g., `langchain-openai` + `openai`)
3. **ML Stack**: `transformers`, `huggingface-hub`, `numpy`, `scikit-learn`
4. **Configuration**: `python-dotenv` for environment variable management

## Development Workflow

### Environment Setup
- Uses `.env` file for API keys and configuration (referenced via `python-dotenv`)
- Virtual environment in `venv/` directory
- Run: `pip install -r requirements.txt`

### Current Code Issues to Resolve
- [Line 8](../../chatmodels.py#L8): `llm` variable is undefined (should be created from a specific pipeline/model)
- [Line 10](../../chatmodels.py#L10): Variable name mismatch - `model` created but never used
- Response parsing at [Lines 12-15](../../chatmodels.py#L12-L15) handles both list and string outputs

### Testing Pattern
When modifying model integrations:
1. Verify the correct LLM provider is instantiated
2. Test with small models first (e.g., `flan-t5-small`) before scaling
3. Handle variable output formats from different providers (list vs string)

## Key Conventions

### Multi-LLM Support
When adding new features, ensure compatibility across all supported providers:
- Each provider has its own integration package + base SDK
- Use LangChain's abstraction layer to minimize provider-specific code
- Test with at least one model from each provider category

### Response Handling
Different models return results in different formats:
- Some return lists of dicts with `"generated_text"` or `"text"` keys
- Others return direct strings
- Always implement defensive checks (e.g., `isinstance()`, `.get()` with defaults)

## Common Tasks

**Adding a new LLM provider**: Install `langchain-{provider}` + base SDK, instantiate via LangChain wrapper
**Testing generation**: Keep models small (≤1B params) for development to avoid memory/time issues
**Debugging output**: Add `type()` and repr checks before parsing responses
