import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

def run_chatbot():
    """
    A terminal chatbot that holds a coherent multi-turn conversation.

    Your implementation should:
    - Start with a system message that sets the assistant's behaviour.
    - Maintain a `messages` list with alternating user/assistant turns.
    - Append the assistant's reply to `messages` after each call.
    - Resend the full history on every API call.
    - Allow the user to type 'exit' or 'quit' to end the session.

    Stretch:
    - Add a '/reset' command that clears history so you can feel context loss live.
    - Add a '/tokens' command that prints response.usage after the last call.
    """
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("Chat started. Type 'exit' to quit.\n")

    while True:
        # TODO: take user input
        user_input = input()
        if (user_input == "quit" or user_input == "exit"):
            print("Thank you! Have a nice day.")
            break         
        if (user_input == "\\reset"):             
            messages = []
            continue
        # TODO: append the user turn to messages
        messages.append({"role": "user", "content": user_input})
        if (len(messages) > 100):
            messsages = messages[-100:]
        # TODO: call the API with the full messages list
        response = client.responses.create(
            model="openrouter/free",
            input=messages,
            store=False
        )
        if (user_input == "\\tokens"):             
            print(response.usage)
        # TODO: extract the assistant's reply
        reply = response.output_text
        # TODO: append the assistant turn to messages
        messages.append({"role": "assistant", "content": reply})
        # TODO: print the reply
        print(reply)

if __name__ == "__main__":
    run_chatbot()
