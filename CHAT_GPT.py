from termcolor import colored
import time
import openai

api_key = input(colored("Welcome and thank you for trying out this tool. Check out other utilities at t.me/VikingTerminal.\n\nEnter your OpenAI API key: ", "green"))
username = input("Enter your username: ")

openai.api_key = api_key

def send_message(message):
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=conversation
    )

    return response['choices'][0]['message']['content']

welcome = colored("Welcome to the chat with ChatGPT!! This tool is part of the Viking project. Join\n t.me/VikingTerminal", "green")
instructions = colored("Enter your messages. Type 'exit' to quit.", "yellow")
print(f"{welcome}\n{instructions}")

while True:
    user_input = input(colored(f"{username}: ", "blue"))
    if user_input.lower() == 'exit':
        break

    response = send_message(user_input)

    for char in response:
        print(colored(char, "cyan"), end="", flush=True)
        time.sleep(0.03)
    print()