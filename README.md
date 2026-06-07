# 🤖 LangGraph Agents

A growing collection of AI agents built with [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain), ranging from simple tool-calling agents to complex multi-agent workflows.

---

## 📁 Project Structure

```
agents/
├── Agents.py          # Simple ReAct agent with weather tool (Ollama / llama3.1)
├── .env               # Environment variables (never commit this)
├── requirements.txt   # Python dependencies
└── README.md
```

> More agents and examples will be added here over time.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/agents.git
cd agents
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
# Add any API keys here as needed
# OPENAI_API_KEY=your_key_here
# ANTHROPIC_API_KEY=your_key_here
```

### 5. Run an agent

```bash
python Agents.py
```

---

## 🧠 Agents

### `Agents.py` — Simple ReAct Agent

A basic agent powered by [Ollama](https://ollama.com/) (`llama3.1:8b`) that uses a custom tool to answer questions.

**Model:** `llama3.1:8b` via `ChatOllama`  
**Framework:** LangGraph `create_react_agent`  
**Tools:** `get_weather(city)` — returns the current weather for a given city

**Example:**
```
User: What is the weather in India?
Agent: The weather in India is sunny.
```

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `langchain` | Core agent and tool abstractions |
| `langgraph` | Agent orchestration and graph execution |
| `langchain-ollama` | Local LLM integration via Ollama |
| `python-dotenv` | Environment variable management |

---

## 📦 Requirements

```txt
langchain
langgraph
langchain-ollama
python-dotenv
```

Install with:

```bash
pip install langchain langgraph langchain-ollama python-dotenv
```

You also need [Ollama](https://ollama.com/) installed and the model pulled:

```bash
ollama pull llama3.1:8b
```

---

## 🗺️ Roadmap

- [x] Simple ReAct agent with custom tools
- [ ] Multi-tool agent
- [ ] Stateful conversational agent with memory
- [ ] Multi-agent collaboration
- [ ] Agent with RAG (Retrieval-Augmented Generation)
- [ ] Human-in-the-loop agent

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

[MIT](LICENSE)
