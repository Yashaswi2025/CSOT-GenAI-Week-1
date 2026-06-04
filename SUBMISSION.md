# Terminal Chatbot using OpenRouter API

## Overview

This project implements a terminal-based chatbot in Python using the OpenAI SDK and the OpenRouter API. The chatbot maintains conversation history, enabling coherent multi-turn interactions by resending previous messages with every API call.

---

## Importing Required Libraries

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
```

### Purpose

* `os` is used to access environment variables.
* `OpenAI` provides access to OpenRouter through an OpenAI-compatible interface.
* `load_dotenv()` loads environment variables from a `.env` file.

---

## Loading Environment Variables

```python
load_dotenv()
```

This function loads variables from the `.env` file into the program's environment.

Example `.env` file:

```text
OPENROUTER_API_KEY=your_api_key_here
```

---

## Creating the Client

```python
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)
```

### Purpose

This initializes the API client using:

* OpenRouter's API endpoint
* The API key stored in the environment variable

Using environment variables prevents exposing sensitive credentials in source code.

---

## Main Chatbot Function

```python
def run_chatbot():
```

This function contains the complete chatbot logic.

---

## Initial Conversation State

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]
```

The chatbot begins with a system message that defines the assistant's behavior.

### Roles

| Role      | Purpose                 |
| --------- | ----------------------- |
| system    | Sets assistant behavior |
| user      | User input              |
| assistant | Model response          |

---

## Starting the Session

```python
print("Chat started. Type 'exit' to quit.\n")
```

Displays instructions for the user.

---

## Continuous Chat Loop

```python
while True:
```

Runs indefinitely until the user exits.

---

## Taking User Input

```python
user_input = input()
```

Reads input from the terminal.

---

## Exit Command

```python
if (user_input == "quit" or user_input == "exit"):
    print("Thank you! Have a nice day.")
    break
```

Typing `quit` or `exit` terminates the chatbot.

---

## Reset Command

```python
if (user_input == "\\reset"):
    messages = []
    continue
```

Clears conversation history and starts a fresh conversation.

---

## Adding User Message

```python
messages.append({"role": "user", "content": user_input})
```

Stores the user's message in the conversation history.

---

## Limiting Conversation Size

```python
if (len(messages) > 100):
    messages = messages[-100:]
```

Keeps only the most recent 100 messages to reduce token usage and API costs.

---

## Sending Request to the Model

```python
response = client.responses.create(
    model="openrouter/free",
    input=messages,
    store=False
)
```

### Parameters

* `model` specifies which model to use.
* `input` contains the complete conversation history.
* `store=False` prevents storing conversation data.

The full history is sent each time so the model can maintain context.

---

## Token Usage Command

```python
if (user_input == "\\tokens"):
    print(response.usage)
```

Displays token usage information for the most recent API request.

---

## Extracting the Response

```python
reply = response.output_text
```

Retrieves the assistant's generated text from the API response.

---

## Updating Conversation History

```python
messages.append({"role": "assistant", "content": reply})
```

Stores the assistant's response so future messages can reference it.

---

## Displaying the Response

```python
print(reply)
```

Outputs the assistant's response to the terminal.

---

## Program Entry Point

```python
if __name__ == "__main__":
    run_chatbot()
```

Ensures the chatbot starts only when the script is run directly.

---

## Features Implemented

* Multi-turn conversational memory
* OpenRouter API integration
* Environment variable based API key management
* Exit command (`exit`, `quit`)
* Reset command (`\reset`)
* Token usage reporting (`\tokens`)
* Conversation history tracking
* Context preservation across API calls

---

## Future Improvements

1. Preserve the system prompt after using `\reset`.
2. Save conversations to a file.
3. Add streaming responses.
4. Improve error handling.
5. Allow model selection from the terminal.
6. Add colored terminal output for better user experience.

---

## Conclusion

The chatbot successfully demonstrates how large language models can maintain conversational context through message history. By repeatedly sending previous messages along with new user input, the assistant can generate coherent and context-aware responses over multiple turns.
