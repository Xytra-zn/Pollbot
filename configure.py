import os

def configure_bot_token():
    token = os.getenv("TOKEN")
    if token:
        with open("bot.py", "r") as file:
            content = file.read()

        updated_content = content.replace("YOUR_TOKEN", token)

        with open("bot.py", "w") as file:
            file.write(updated_content)
    else:
        print("Error: Bot token not provided.")

if __name__ == "__main__":
    configure_bot_token()
  
