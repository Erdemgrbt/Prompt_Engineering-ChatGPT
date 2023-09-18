import openai
from quest import *

class QA:
    def __init__(self):
        self.api_key = "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"
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Merhaba, nasılsınız?"}
        ]
        openai.api_key = self.api_key

    def ask(self, user_input):
        # Adds the user's message to the messages list.
        self.messages.append({"role": "user", "content": user_input})

        # It sends messages to the API and receives a response from the model.
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )

        # Gets the model's response.
        bot_reply = response.choices[-1].message["content"]

        # Adds the model's response to the list of messages.
        self.messages.append({"role": "assistant", "content": bot_reply})

        return bot_reply

def main():
    qa_instance = QA()

    while True:
        user_input = get_user_input()
        
        if user_input.lower() == 'exit':
            break

        bot_reply = qa_instance.ask(user_input)
        print("GPT-3.5 Pro: ", bot_reply)
        return False

def get_user_input():
    # Takes user input.
    user_input = incoming_question
    return user_input

if __name__ == "__main__":
    main()
