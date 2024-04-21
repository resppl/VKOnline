# AUTHOR'S GITHUB: github.com/resppl
# SCRIPT ON GITHUB: github.com/resppl/TelegramRemotePC

import vk_api
import time

def set_online(token):
    try:
        vk_session = vk_api.VkApi(token=token)
        vk_session.method("account.setOnline")
        print("The online status has been set successfully.")
    except Exception as e:
        print(f"Error when setting up the online status: {e}")

if __name__ == "__main__":
    print("The script has been successfully launched. To complete the process, disable it completely.")

    token = "ENTER_YOUR_VK_API_TOKEN"

    while True:
        set_online(token)
        time.sleep(300)