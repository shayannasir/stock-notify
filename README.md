# Stock Notify

A small serverless python script that crawls a website (keychron.in) looking for a particular product (k2 v2) with some specific variation (Block switches and white backlight). Once this is found, it scrapes the details of the products (availability and price) and sends it via a telegram bot to a specific user.


### Dependencies

- python3
- beautifulsoup4
- html5lib
- request
- telegram_send


### Setup

##### Telegram Setup

1. In Telegram goto the bot named **BotFather**
2. Type `/start`
3. Type `/newbot`
4. Choose a name for your bot
5. Note the token received from the BotFather

##### Project Setup

1. Install all the before-mentioned dependencies
2. Run `telegram-send --configure` to configure telegram-send
3. When requested, provide the token received from BotFather while creating the bot


_Note: Do remember to update the website url and the product tracking logic as per your needs._
