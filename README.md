1. Create a Twilio account (requires you to verify phone number).
2. Go to Twilio Console
3. Take Account SID, Auth Token and Phone number from there and put them in the env file
4. Run `pip install -r requirements.txt` in the root directory of the repository.
5. Run `ngrok http 5020` in the terminal. It will start an ngrok server and give you a link. Copy that link.
6. Go to Messaging > Settings > WhatsApp Sandbox Settings and paste the link in "WHEN A MESSAGE COMES IN" field there. Make sure its set to HTTP Post. Dont touch anything else.

Steps till here were from https://www.youtube.com/watch?v=MLDexb0siww

Next steps are from https://medium.com/@today.rafi/whatsapp-cloud-api-how-to-send-whatsapp-messages-from-python-9baa03c93b5d

Then you can just run the app and enjoy :)
