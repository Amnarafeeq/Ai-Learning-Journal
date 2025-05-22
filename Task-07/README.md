
# 🤖 Python AI Agent System

This project demonstrates how to build a **modular, clean AI Agent system** in Python using modern concepts like:

- ✅ `@dataclass`
- ✅ System & User Prompts
- ✅ Callable Agent Class
- ✅ Classmethods
- ✅ Runner Controller
- ✅ Generics (`TypeVar`)

---

## 📦 Features

- **Agent class** using `@dataclass` for easy data handling.
- Stores a system prompt (instructions) to control agent behavior.
- Callable class instances with `__call__()` method.
- `Runner` class that manages execution without needing instantiation.
- Type flexibility using Python Generics (`TContext`).

---

## 🚀 How to Run

1. Clone this repository:
```bash
git clone https://github.com/your-username/ai-agent-system.git
cd ai-agent-system
```

2. Make sure Python 3.10+ is installed.

3. Run the script:
```bash
python main.py
```

---

## 🧠 Key Concepts Explained

### 1. `@dataclass`
- Automatically generates `__init__`, `__repr__`, and `__eq__`.
- Cleaner and shorter syntax for data-holder classes.

```python
@dataclass
class Agent:
    instructions: str
```

---

### 2a. System Prompt & `__call__()`
- `instructions` is the personality of the agent.
- `__call__()` makes the class callable like a function.

```python
def __call__(self, user_prompt: str):
    return f"{self.instructions} | User: {user_prompt}"
```

---

### 2b. `Runner.run()` with Classmethod
- The prompt changes each time, so it’s passed dynamically.
- `@classmethod` lets you run without instantiating the class.

```python
@classmethod
def run(cls, prompt: str):
    agent = Agent("You're an AI assistant.")
    return agent(prompt)
```

---

### 3. Runner Class
- Acts as a **controller** to:
  - Create the agent
  - Pass the prompt
  - Return the result

---

### 4. Generics (`TContext`)
- Used for type flexibility.
- Allows the Agent to accept any context type (e.g., string, dict).

```python
TContext = TypeVar('TContext')

class Agent(Generic[TContext]):
    def __init__(self, context: TContext):
        self.context = context
```

---

## 📁 Project Structure

```
ai-agent-system/
├── main.py
├── agent.py
├── runner.py
├── README.md
```

---

## 👩‍💻 Author

Made with ❤️ by **Amna**  
[Portfolio Link](https://your-portfolio-link.com)  
GitHub: [@your-username](https://github.com/your-username)

---

## 📜 License

This project is licensed under the MIT License.
