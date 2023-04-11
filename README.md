# ExcusesGeneratorBot


### This is an attempt to make a simple telegram bot with FastAPI for serverless hosting without any bot frameworks. The idea is inspired by [Excuses.ai](excuses.ai) website.

## About

You can use this bot to generate excuses. It uses a reverse engineered api from [Excuses.ai](excuses.ai) to generate the results.

## Why FastAPI?

Because, FastAPI is the fastest micro framework for python. Faster than Flask, and Asynchronous.

## Deployment

### For Development & Testing

- Fork & Clone this repo
```
git clone https://github.com/anzilr/ExcusesGeneratorBot.git
```

* CD to the project directory
```
cd ExcusesGeneratorBot
```

+ Install dependencies
```
pip install -r requirements.txt
```

- Edit the `BOT_TOKEN` value in `config.py` 
```
BOT_TOKEN = os.environ.get("BOT_TOKEN", "<YOUR BOT TOKEN FROM BOTFATHER>")
```
Don't forget to clear the token when you are committing the file to git.

- Start the server
```
uvicorn main:app --reload
```
This will restart the server automatically when you make changes to the code.

### Deploy to Deta Space

You can deploy this bot to deta, and it's free for lifetime.
- Go to [Deta.space](deta.space) and sign up. Don't forget to check the developer mode on.

- Set up the space CLI (follow [this](https://deta.space/docs/en/basics/cli) documentation).

- Fork & Clone this repo
```
git clone https://github.com/anzilr/ExcusesGeneratorBot.git
```

* CD to the project directory
```
cd ExcusesGeneratorBot
```

* Create a new micro
```
space new
```
Follow the instructions

- To push your code to space, run the following command
```
space push
```

- After the process finished, it will give you a link for the app. Copy that.

- To set up the webhook, replace `<BOT_TOKEN>` and `<APP_LINK>` with your bot token and the link you copied from the previous step.
```
https://api.telegram.org/bot<BOT_TOKEN>/setWebhook?url=<APP_LINK>
```

- After editing the above link, copy and paste it to a browser and hit enter. You should get a response like below
```
{"ok":true,"result":true,"description":"Webhook was set"}
```
- Now, go to deta.space. You can see the app pinned on there. Click on the 3 dots and select `Settings` -> `Configuration`. Enter your bot token then save.

- Now send `/start` in your bot, It will respond.

- If you make any changes in the code, just run `space push` command. It will update the bot and restart.

