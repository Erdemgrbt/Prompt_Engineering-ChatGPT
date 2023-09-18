import openai

class qa:
    def __init__(self):
        self.input = input("Soru veya mesajınızı girin (Çıkmak için 'exit' yazabilirsiniz): ")
        self.api_key = "API-KEY"
        openai.api_key = self.api_key
        
    def ask(self):
        
        self.messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Merhaba, nasılsınız?"}
        ]   

        # Kullanıcının mesajını mesajlar listesine ekler.
        self.messages.append({"role": "user", "content": self.input})

        # Mesajları API'ye gönderir ve modelden yanıt alır.
        self.response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )

        # Modelin yanıtını alır.
        self.bot_reply = self.response.choices[-1].message["content"]

        # Modelin yanıtını mesajlar listesine ekler.
        self.messages.append({"role": "assistant", "content": self.bot_reply}) 
        
        return self.bot_reply
        
while True:
    bot = qa()
    print(bot.ask())