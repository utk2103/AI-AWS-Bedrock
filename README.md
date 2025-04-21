## 🧠 AWS Bedrock LLM Scripts

This repository contains various scripts demonstrating how to use **Amazon Bedrock** to interact with large language models (LLMs) like **Claude (Anthropic)**, **Titan (Amazon)**, **LLaMA (Meta)**, and **DeepSeek** for different generative AI use cases including:
- Chat-based Q&A
- Summarization
- Web search integration
- Multi-model experimentation
- Latency and performance tracking

---

## 📦 Repository Structure

```bash
aws-bedrock-scripts/
│
├── claude_chat.py              # Claude 3 Sonnet multi-prompt chat with latency logging
├── llama_conversation.py       # Meta LLaMA structured chat prompt
├── deepseek_prompt.py          # DeepSeek R1 chat model integration
├── titan_basic.py              # Basic Titan G1 Text completion example
├── web_search_integration.py   # Web search with Claude assistant and JSON formatting
├── utils/
│   └── timer.py                # Utility for measuring latency
├── README.md                   # This file
```
### 1. Prerequisites
- AWS Account with access to Amazon Bedrock
- IAM role with bedrock:InvokeModel permissions
- Python 3.8+
- AWS CLI configured (aws configure)

Install dependencies:
```pip install -r requirements.txt```

### 2. Useful docs
1. https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html
2. https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api-ex-python.html
