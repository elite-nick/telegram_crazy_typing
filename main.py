import os
from pyrogram import Client, filters, enums

# эти данные нужно получить на my.telegram.org
api_id = "API_ID"
api_hash = "API_HASH"

# в chat_id можно написать ID чата или логин пользователя (логин указывается без @ и в двойных кавычках!)
chat_id = "username"

typing_type = enums.ChatAction.TYPING
typing_type_text = "X печатает..."
script_ver = "v0.1"

app = Client("session_file", api_id, api_hash)

print("\nВыберите тип спама: \n\n"
         "1. X печатает..."
         "\n2. X отправляет фото..."
         "\n3. X записывает видео..."
         "\n4. X отправляет видео..."
         "\n5. X записывает аудиосообщение..."
         "\n6. X отправляет аудиосообщение..."
         "\n7. X записывает видеосообщение..."
         "\n8. X отправляет видеосообщение..."
         "\n9. X отправляет документ..."
         "\n10. X играет..."
         "\n11. X выбирает стикер..." 
      )
select_spam = input()
if select_spam == "2":
        typing_type = enums.ChatAction.UPLOAD_PHOTO
        typing_type_text = "X отправляет фото..."
        
elif select_spam == "3":
        typing_type = enums.ChatAction.RECORD_VIDEO
        typing_type_text = "X записывает видео..."
        
elif select_spam == "4":
        typing_type = enums.ChatAction.UPLOAD_VIDEO
        typing_type_text = "X отправляет видео..."
        
elif select_spam == "5":
        typing_type = enums.ChatAction.RECORD_AUDIO
        typing_type_text = "X записывает аудиосообщение..."
        
elif select_spam == "6":
        typing_type = enums.ChatAction.UPLOAD_AUDIO
        typing_type_text = "X отправляет аудиосообщение..."
        
elif select_spam == "7":
        typing_type = enums.ChatAction.RECORD_VIDEO_NOTE
        typing_type_text = "X записывает видеосообщение..."
        
elif select_spam == "8":
        typing_type = enums.ChatAction.UPLOAD_VIDEO_NOTE
        typing_type_text = "X отправляет видеосообщение..."
        
elif select_spam == "9":
        typing_type = enums.ChatAction.UPLOAD_DOCUMENT
        typing_type_text = "X отправляет документ..."
        
elif select_spam == "10":
        typing_type = enums.ChatAction.PLAYING
        typing_type_text = "X играет..."
         
elif select_spam == "11":
        typing_type = enums.ChatAction.CHOOSE_STICKER
        typing_type_text = "X выбирает стикер..."
              
else:
        typing_type = enums.ChatAction.TYPING
        typing_type_text = "X печатает..."
              
@app.on_message(None)
def hello(client, message):
    app.send_chat_action(chat_id, typing_type)

os.system('cls')
print("Telegram Crazy Typing " + script_ver)
print("\nСтатус спама: Работает!")
print("Спам работает на ChatID: " + str(chat_id))
print("Тип спама: " + typing_type_text)
print("\n(Для прекращения спама закройте скрипт)")
app.run()