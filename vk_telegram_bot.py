import telebot
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

BOT_TOKEN = '' # Token of your bot
LISTENER_ID = '' #ID of user/chat or @channel_name in Telegram

bot = telebot.TeleBot(BOT_TOKEN) # for working with your bot in Telegramm


def main():
    
    login, password = 'name@best_mail.com', 'your_password' # Your login and password (Vk)
    vk_session = vk_api.VkApi(login, password)
    
    try:
        vk_session.auth() #Authorization
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    longpoll = VkLongPoll(vk_session) # LongPoll in Vk
    text_message = 'Новое сообщение:' #Translation: "New message"

    for event in longpoll.listen(): #for any event in LongPoll
    
        if event.type == VkEventType.MESSAGE_NEW: #we need only messages from Vk
            
            if event.from_user:
                text_message = text_message + str(event.user_id) + '\n'
            elif event.from_chat:
                text_message = text_message + ' в беседе' + str(event.chat_id) + '\n' #Translation: "in chat"
            elif event.from_group:
                text_message = text_message + ' группы' + str(event.group_id) + '\n' #Translation: "of group"

            text_message = text_message + 'Текст: ' + event.text #Translation: "Text"


            bot.send_message(LISTENER_ID,text_message) #Sending message in Telegramm

if __name__ == '__main__':
    main()
