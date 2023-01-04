# Discord-OpenAI-Bot
A simple discord chat bot using OpenAi's API.

![OpenAI chat](/mdimg/openAichatEx.png?raw=true "Bot Example")


## Getting the keys

### Discord
Visit https://discord.com/developers/ and create an application for your bot.
From there you can create a bot located in the side menu. You'll need to enable message content intent for your bot to read and respond to messages.
On the same page there will be an option to generate/reset a token which you will need later for the .env file. The token can only be viewed once when created so keep it in a safe space. If you lose the token or need to change it, it can always be regenerated. Paste the key in the DISCORD_TOKEN variable in the .env file


### OpenAI
Visit https://beta.openai.com/account/api-keys. You'll need to log in to your account but as of writing this the API is free to use (Up to $18.00 in credits for 3 months with .02 cents per 1k tokens). You then can generate a new secret key but just like the discord token, it can only be viewed once. Place the key in the OPENAI_API_KEY variable in the .env file.
