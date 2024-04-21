# ГИТХАБ АВТОРА: github.com/resppl
# СКРИПТ НА ГИТХАБЕ: github.com/resppl/TelegramRemotePC
# САЙТ АВТОРА: resppl.ru

import vk_api
import time

def set_online(token):
    try:
        vk_session = vk_api.VkApi(token=token)
        vk_session.method("account.setOnline")
        print("Статус онлайн установлен успешно.")
    except Exception as e:
        print(f"Ошибка при настройке онлайн-статуса: {e}")

if __name__ == "__main__":
    print("Скрипт успешно запущен. Для завершения процесса отключите его полностью.")

    token = "ENTER_YOUR_VK_API_TOKEN"

    while True:
        set_online(token)
        time.sleep(300)