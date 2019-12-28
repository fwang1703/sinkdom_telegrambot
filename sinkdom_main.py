import requests

url = "https://api.telegram.org/bot1025672848:AAGlcSLXR1XqbH2vbdFBlMTFWNAtZg0s7vU/"


# getting the chat_id
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id


# gets message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# gets last update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]


# get bot to send message
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response


def send_photo(chat_id, photo_file):
    params = {"chat_id": chat_id, "photo": photo_file}
    response = requests.post(url + "sendPhoto", data=params)
    return response


# main function
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "/sornyhours" or get_message_text(update).lower() == "sorny":
                send_photo(get_chat_id(update), "AgADBQADc6kxG9JPOFQV7ONa0w12P-CrJTMABAEAAwIAA20AA7h5AQABFgQ")
            elif get_message_text(update).lower() == "/maria_no":
                send_message(get_chat_id(update), "Maria stop being so snasty")

            elif get_message_text(update).lower() == "/goodnight":
                send_message(get_chat_id(update), "Goodnight Sinkies. Please go to sleep.")

            elif get_message_text(update).lower() == "/summon_hami":
                send_message(get_chat_id(update), "Hongjoongs feet")

            update_id += 1

main()

