import openai

api_key = "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"

openai.api_key = api_key

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Merhaba, nasılsınız?"}
]

while True:
    # Kullanıcıdan giriş alır.
    user_input = input("Soru veya mesajınızı girin (Çıkmak için 'exit' yazabilirsiniz): ")

    if user_input.lower() == 'exit':
        break

    # Kullanıcının mesajını mesajlar listesine ekler.
    messages.append({"role": "user", "content": user_input})

    # Mesajları API'ye gönderir ve modelden yanıt alır.
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Modelin yanıtını alır.
    bot_reply = response.choices[-1].message["content"]
    
    # Modelin yanıtını ekrana yazdırır.
    print("GPT-3.5 Pro: ", bot_reply)

    # Modelin yanıtını mesajlar listesine ekler.
    messages.append({"role": "assistant", "content": bot_reply})
