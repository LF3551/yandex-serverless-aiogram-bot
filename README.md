# yandex-serverless-aiogram-bot
Simple Telegram bot example on aiogram framework using Yandex Cloud with Webhook


## Steps 
1. First create a bot with telegram "botfather", and copy token to your notes

2. Go to Yandex Cloud Console https://console.cloud.yandex.ru/

3. Create service account in Yandex Cloud with roles `editor` and `serverless.functions.invoker`

4. Create function in Yandex Cloud:
  - choose programming language, in our case it will be Python
  - copy and paste the code from `index.py` to file `index.py` in Cloud Function Editor
  - create file `requirements.txt` in Cloud Function Editor
  - copy and paste data from `requirements.txt` to file `requirements.txt` in Cloud   
    Function Editor
  - select below service account you created earlier
  - add variable `TOKEN` and put your token data
  - click `Create function`

5. You are back to your Cloud Function view:
  - check the box `Public function`
  - copy the link `PUBLIC_FUNCTION_URL` to your public function in notes

6. You need to create Webhook:
   - use template: `https://api.telegram.org/botYOUR_TOKEN/setWebhook?url=PUBLIC_FUNCTION_URL`
   - put this link to your browser and press `enter`
   - you will get this message: `{"ok":true,"result":true,"description":"Webhook was set"}`

7. Send any message to your bot. Everything should work
