# # # # # from flask import Flask, request
# # # # # from twilio.twiml.messaging_response import MessagingResponse
# # # # # import anthropic
# # # # # import json
# # # # # import os
# # # # # from dotenv import load_dotenv

# # # # # load_dotenv()

# # # # # app = Flask(__name__)
# # # # # client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# # # # # # Load your PDF map
# # # # # with open("pdf_map.json", "r") as f:
# # # # #     PDF_MAP = json.load(f)

# # # # # def find_pdf_with_claude(user_message):
# # # # #     available_pdfs = list(PDF_MAP.keys())
    
# # # # #     response = client.messages.create(
# # # # #         model="claude-sonnet-4-20250514",
# # # # #         max_tokens=200,
# # # # #         system="""You are a college PDF finder assistant.
# # # # # A student will ask for a PDF. Match their request to the correct file from the list.
# # # # # Files are named as: branch/section/subject.pdf
# # # # # Example: cse/a5/cn.pdf

# # # # # Reply ONLY with the exact file path. Nothing else.
# # # # # If no match found, reply exactly: NOT_FOUND""",
# # # # #         messages=[{
# # # # #             "role": "user",
# # # # #             "content": f"Available PDFs:\n{chr(10).join(available_pdfs)}\n\nStudent request: {user_message}"
# # # # #         }]
# # # # #     )
    
# # # # #     return response.content[0].text.strip()

# # # # # @app.route("/webhook", methods=["POST"])
# # # # # def webhook():
# # # # #     incoming_msg = request.form.get("Body", "").strip()
# # # # #     resp = MessagingResponse()
# # # # #     msg = resp.message()

# # # # #     print(f"Received: {incoming_msg}")

# # # # #     pdf_key = find_pdf_with_claude(incoming_msg)
# # # # #     print(f"Claude matched: {pdf_key}")

# # # # #     if pdf_key == "NOT_FOUND" or pdf_key not in PDF_MAP:
# # # # #         msg.body(
# # # # #             "Sorry, I couldn't find that PDF 😕\n\n"
# # # # #             "Try asking like:\n"
# # # # #             "• CSE A5 CN pdf\n"
# # # # #             "• Send me OS notes A1\n"
# # # # #             "• I want DBMS A5"
# # # # #         )
# # # # #     else:
# # # # #         pdf_url = PDF_MAP[pdf_key]
# # # # #         msg.body(f"Here is your PDF 📄: {pdf_key}")
# # # # #         msg.media(pdf_url)

# # # # #     return str(resp)

# # # # # @app.route("/", methods=["GET"])
# # # # # def home():
# # # # #     return "WhatsApp PDF Bot is running! ✅"

# # # # # if __name__ == "__main__":
# # # # #     app.run(debug=True, port=5000)


# # # # from flask import Flask, request
# # # # from twilio.twiml.messaging_response import MessagingResponse
# # # # import json
# # # # from difflib import get_close_matches

# # # # app = Flask(__name__)

# # # # # Load PDF map
# # # # with open("pdf_map.json", "r") as f:
# # # #     PDF_MAP = json.load(f)

# # # # def find_pdf(user_message):
# # # #     msg = user_message.lower()

# # # #     # simple keyword search
# # # #     for key in PDF_MAP.keys():
# # # #         normalized = key.replace("/", " ").replace(".pdf", "").lower()
# # # #         if all(word in normalized for word in msg.split() if len(word) > 1):
# # # #             return key

# # # #     # fallback fuzzy match
# # # #     matches = get_close_matches(
# # # #         msg,
# # # #         [k.replace("/", " ").replace(".pdf", "") for k in PDF_MAP.keys()],
# # # #         n=1,
# # # #         cutoff=0.3
# # # #     )

# # # #     if matches:
# # # #         for key in PDF_MAP.keys():
# # # #             if matches[0] in key.replace("/", " ").replace(".pdf", ""):
# # # #                 return key

# # # #     return "NOT_FOUND"

# # # # @app.route("/webhook", methods=["POST"])
# # # # def webhook():
# # # #     incoming_msg = request.form.get("Body", "").strip()
# # # #     print("Received:", incoming_msg)

# # # #     resp = MessagingResponse()
# # # #     msg = resp.message()

# # # #     pdf_key = find_pdf(incoming_msg)
# # # #     print("Matched:", pdf_key)

# # # #     if pdf_key == "NOT_FOUND":
# # # #         msg.body("Sorry bro 😕 PDF not found.\nI think you are Messaging Something else")
# # # #     else:
# # # #         msg.body(f"Here is your PDF 📄: {pdf_key}")
# # # #         msg.media(PDF_MAP[pdf_key])

# # # #     return str(resp)

# # # # if __name__ == "__main__":
# # # #     app.run(debug=True, port=5000)


# # # from flask import Flask, request
# # # import requests

# # # app = Flask(__name__)

# # # ACCESS_TOKEN = "EAAgxFfvcTZBIBRCIfmqjB08JXLqr9tBzJEsAMMdGpZB6H0C2YHtcEavuZC90ZAUUhOZADwxCyyRIVIaQPh3eDkZBTJlYZASX7L7oScr41CRw9rGI0CKEEMuZA68UH6vNRNXZBFmBBWNWQ4FC44I86ZAMR3BSMTYhjzSuv9vxwj9ZBQlpTK61LlTZBDbJjrjSu3cbQ3bktqNeGHBnbgQq10QR0Dcy1ZBvu6a3QReHbbmpwsXjsnNUD6Qbd5QIAKrCFcZCXLnXNYe5I1ZC85YMsZA9snU4jMVHxw3x"
# # # PHONE_NUMBER_ID = "1095814390277545"
# # # VERIFY_TOKEN = "hello123"

# # # @app.route('/webhook', methods=['GET', 'POST'])
# # # def webhook():
# # #     if request.method == 'GET':
# # #         mode = request.args.get("hub.mode")
# # #         token = request.args.get("hub.verify_token")
# # #         challenge = request.args.get("hub.challenge")

# # #         print("MODE:", mode)
# # #         print("TOKEN:", token)
# # #         print("CHALLENGE:", challenge)

# # #         if mode == "subscribe" and token == VERIFY_TOKEN:
# # #             return str(challenge), 200
# # #         else:
# # #             return "Verification failed", 403

# # #     if request.method == 'POST':
# # #         data = request.json

# # #         try:
# # #             message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
# # #             sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

# # #             reply = f"You said: {message}"

# # #             url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

# # #             headers = {
# # #                 "Authorization": f"Bearer {ACCESS_TOKEN}",
# # #                 "Content-Type": "application/json"
# # #             }

# # #             payload = {
# # #                 "messaging_product": "whatsapp",
# # #                 "to": sender,
# # #                 "type": "text",
# # #                 "text": {"body": reply}
# # #             }

# # #             requests.post(url, headers=headers, json=payload)

# # #         except Exception as e:
# # #             print(e)

# # #         return "ok", 200

# # # if __name__ == '__main__':
# # #     app.run(port=5000)


# # # from flask import Flask, request
# # # import requests
# # # import json

# # # app = Flask(__name__)

# # # # 🔐 Replace with your NEW token (regenerate if exposed)
# # # ACCESS_TOKEN = "EAAgxFfvcTZBIBRCIfmqjB08JXLqr9tBzJEsAMMdGpZB6H0C2YHtcEavuZC90ZAUUhOZADwxCyyRIVIaQPh3eDkZBTJlYZASX7L7oScr41CRw9rGI0CKEEMuZA68UH6vNRNXZBFmBBWNWQ4FC44I86ZAMR3BSMTYhjzSuv9vxwj9ZBQlpTK61LlTZBDbJjrjSu3cbQ3bktqNeGHBnbgQq10QR0Dcy1ZBvu6a3QReHbbmpwsXjsnNUD6Qbd5QIAKrCFcZCXLnXNYe5I1ZC85YMsZA9snU4jMVHxw3x"
# # # PHONE_NUMBER_ID = "1095814390277545"
# # # VERIFY_TOKEN = "hello123"

# # # # 📄 Load PDF map
# # # with open("pdf_map.json", "r") as f:
# # #     PDF_MAP = json.load(f)

# # # # 🔍 Simple PDF search
# # # def find_pdf(user_message):
# # #     msg = user_message.lower()

# # #     for key in PDF_MAP.keys():
# # #         if msg in key.lower():
# # #             return key

# # #     return "NOT_FOUND"


# # # @app.route('/webhook', methods=['GET', 'POST'])
# # # def webhook():

# # #     # 🔹 Verification (GET request from Meta)
# # #     if request.method == 'GET':
# # #         mode = request.args.get("hub.mode")
# # #         token = request.args.get("hub.verify_token")
# # #         challenge = request.args.get("hub.challenge")

# # #         if mode == "subscribe" and token == VERIFY_TOKEN:
# # #             return str(challenge), 200
# # #         else:
# # #             return "Verification failed", 403

# # #     # 🔹 Incoming message (POST)
# # #     if request.method == 'POST':
# # #         data = request.json

# # #         try:
# # #             message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
# # #             sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

# # #             print("User:", message)

# # #             pdf_key = find_pdf(message)

# # #             if pdf_key == "NOT_FOUND":
# # #                 reply = "Sorry 😕 PDF not found.\nTry like:\nCSE A5 CN"
# # #             else:
# # #                 pdf_url = PDF_MAP[pdf_key]
# # #                 reply = f"Here is your PDF 📄:\n{pdf_url}"

# # #             # 📤 Send reply
# # #             url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

# # #             headers = {
# # #                 "Authorization": f"Bearer {ACCESS_TOKEN}",
# # #                 "Content-Type": "application/json"
# # #             }

# # #             payload = {
# # #                 "messaging_product": "whatsapp",
# # #                 "to": sender,
# # #                 "type": "text",
# # #                 "text": {"body": reply}
# # #             }

# # #             requests.post(url, headers=headers, json=payload)

# # #         except Exception as e:
# # #             print("Error:", e)

# # #         return "ok", 200


# # # if __name__ == '__main__':
# # #     app.run(port=5000)



# # from flask import Flask, request, send_from_directory
# # import requests
# # import os

# # app = Flask(__name__)

# # ACCESS_TOKEN = "EAAgxFfvcTZBIBRCIfmqjB08JXLqr9tBzJEsAMMdGpZB6H0C2YHtcEavuZC90ZAUUhOZADwxCyyRIVIaQPh3eDkZBTJlYZASX7L7oScr41CRw9rGI0CKEEMuZA68UH6vNRNXZBFmBBWNWQ4FC44I86ZAMR3BSMTYhjzSuv9vxwj9ZBQlpTK61LlTZBDbJjrjSu3cbQ3bktqNeGHBnbgQq10QR0Dcy1ZBvu6a3QReHbbmpwsXjsnNUD6Qbd5QIAKrCFcZCXLnXNYe5I1ZC85YMsZA9snU4jMVHxw3x"
# # PHONE_NUMBER_ID = "1095814390277545"
# # VERIFY_TOKEN = "hello123"

# # PDF_FOLDER = "pdfs"
# # NGROK_URL = "https://sharply-lepidopterous-penny.ngrok-free.dev"

# # # 🔍 Find matching PDF
# # def find_pdf(user_message):
# #     msg = user_message.lower()

# #     for file in os.listdir(PDF_FOLDER):
# #         if msg in file.lower():
# #             return file

# #     return None


# # # 📂 Serve PDFs
# # @app.route('/pdfs/<filename>')
# # def serve_pdf(filename):
# #     return send_from_directory(PDF_FOLDER, filename)


# # @app.route('/webhook', methods=['GET', 'POST'])
# # def webhook():

# #     # 🔹 Verification
# #     if request.method == 'GET':
# #         mode = request.args.get("hub.mode")
# #         token = request.args.get("hub.verify_token")
# #         challenge = request.args.get("hub.challenge")

# #         if mode == "subscribe" and token == VERIFY_TOKEN:
# #             return str(challenge), 200
# #         else:
# #             return "Verification failed", 403

# #     # 🔹 Message handling
# #     if request.method == 'POST':
# #         data = request.json

# #         try:
# #             message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
# #             sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

# #             print("User:", message)

# #             pdf_file = find_pdf(message)

# #             url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

# #             headers = {
# #                 "Authorization": f"Bearer {ACCESS_TOKEN}",
# #                 "Content-Type": "application/json"
# #             }

# #             if pdf_file:
# #                 pdf_url = f"{NGROK_URL}/pdfs/{pdf_file}"

# #                 payload = {
# #                     "messaging_product": "whatsapp",
# #                     "to": sender,
# #                     "type": "document",
# #                     "document": {
# #                         "link": pdf_url,
# #                         "filename": pdf_file
# #                     }
# #                 }
# #             else:
# #                 payload = {
# #                     "messaging_product": "whatsapp",
# #                     "to": sender,
# #                     "type": "text",
# #                     "text": {
# #                         "body": "❌ PDF not found.\nTry typing part of file name (example: module)"
# #                     }
# #                 }

# #             requests.post(url, headers=headers, json=payload)

# #         except Exception as e:
# #             print("Error:", e)

# #         return "ok", 200


# # if __name__ == '__main__':
# #     app.run(port=5000)




# # from flask import Flask, request, send_from_directory
# # import requests
# # import os

# # app = Flask(__name__)

# # # 🔐 Replace with your NEW token
# # ACCESS_TOKEN = "EAAgxFfvcTZBIBRCIfmqjB08JXLqr9tBzJEsAMMdGpZB6H0C2YHtcEavuZC90ZAUUhOZADwxCyyRIVIaQPh3eDkZBTJlYZASX7L7oScr41CRw9rGI0CKEEMuZA68UH6vNRNXZBFmBBWNWQ4FC44I86ZAMR3BSMTYhjzSuv9vxwj9ZBQlpTK61LlTZBDbJjrjSu3cbQ3bktqNeGHBnbgQq10QR0Dcy1ZBvu6a3QReHbbmpwsXjsnNUD6Qbd5QIAKrCFcZCXLnXNYe5I1ZC85YMsZA9snU4jMVHxw3x"
# # PHONE_NUMBER_ID = "1095814390277545"
# # VERIFY_TOKEN = "hello123"

# # PDF_FOLDER = "pdfs"
# # NGROK_URL = "https://sharply-lepidopterous-penny.ngrok-free.dev"


# # # 🔍 SMART PDF FINDER (handles cse cn unit1)
# # def find_pdfs(user_message):
# #     msg = user_message.lower()

# #     subjects = ["cn", "nmps", "se"]

# #     subject = None
# #     unit = None

# #     # detect subject (even inside sentence)
# #     for s in subjects:
# #         if s in msg:
# #             subject = s

# #     # detect unit (flexible)
# #     for i in range(1, 6):
# #         if f"unit{i}" in msg or f"unit {i}" in msg:
# #             unit = f"unit{i}"

# #     results = []

# #     if subject:
# #         subject_path = os.path.join(PDF_FOLDER, "cse", subject)

# #         if os.path.exists(subject_path):
# #             for file in os.listdir(subject_path):
# #                 file_clean = file.lower().replace(" ", "")

# #                 if unit:
# #                     if unit in file_clean:
# #                         results.append(("cse", subject, file))
# #                 else:
# #                     results.append(("cse", subject, file))

# #     return results

# # # 📂 SERVE PDF FILES
# # @app.route('/pdfs/<path:filename>')
# # def serve_pdf(filename):
# #     return send_from_directory(PDF_FOLDER, filename)


# # @app.route('/webhook', methods=['GET', 'POST'])
# # def webhook():

# #     # 🔹 VERIFICATION
# #     if request.method == 'GET':
# #         mode = request.args.get("hub.mode")
# #         token = request.args.get("hub.verify_token")
# #         challenge = request.args.get("hub.challenge")

# #         if mode == "subscribe" and token == VERIFY_TOKEN:
# #             return str(challenge), 200
# #         else:
# #             return "Verification failed", 403

# #     # 🔹 HANDLE MESSAGE
# #     if request.method == 'POST':
# #         data = request.json

# #         try:
# #             message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
# #             sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

# #             print("User:", message)

# #             results = find_pdfs(message)

# #             url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

# #             headers = {
# #                 "Authorization": f"Bearer {ACCESS_TOKEN}",
# #                 "Content-Type": "application/json"
# #             }

# #             if results:
# #                 for branch, subject, file in results:
# #                     pdf_url = f"{NGROK_URL}/pdfs/{branch}/{subject}/{file}"

# #                     payload = {
# #                         "messaging_product": "whatsapp",
# #                         "to": sender,
# #                         "type": "document",
# #                         "document": {
# #                             "link": pdf_url,
# #                             "filename": file
# #                         }
# #                     }

# #                     requests.post(url, headers=headers, json=payload)

# #             else:
# #                 payload = {
# #                     "messaging_product": "whatsapp",
# #                     "to": sender,
# #                     "type": "text",
# #                     "text": {
# #                         "body": "❌ No PDFs found.\nTry: cn or cn unit1"
# #                     }
# #                 }

# #                 requests.post(url, headers=headers, json=payload)

# #         except Exception as e:
# #             print("Error:", e)

# #         return "ok", 200


# # if __name__ == '__main__':
# #     app.run(port=5000)





# from flask import Flask, request, send_from_directory
# import requests
# import os

# app = Flask(__name__)

# ACCESS_TOKEN = "EAAgxFfvcTZBIBRCIfmqjB08JXLqr9tBzJEsAMMdGpZB6H0C2YHtcEavuZC90ZAUUhOZADwxCyyRIVIaQPh3eDkZBTJlYZASX7L7oScr41CRw9rGI0CKEEMuZA68UH6vNRNXZBFmBBWNWQ4FC44I86ZAMR3BSMTYhjzSuv9vxwj9ZBQlpTK61LlTZBDbJjrjSu3cbQ3bktqNeGHBnbgQq10QR0Dcy1ZBvu6a3QReHbbmpwsXjsnNUD6Qbd5QIAKrCFcZCXLnXNYe5I1ZC85YMsZA9snU4jMVHxw3x"
# PHONE_NUMBER_ID = "1095814390277545"
# VERIFY_TOKEN = "hello123"

# PDF_FOLDER = "pdfs"
# NGROK_URL = "https://sharply-lepidopterous-penny.ngrok-free.dev"


# # 🔍 AI-like PDF finder
# def find_pdfs(user_message):
#     msg = user_message.lower()

#     subjects = ["cn", "nmps", "se"]

#     subject = None
#     unit = None

#     for s in subjects:
#         if s in msg:
#             subject = s

#     for i in range(1, 6):
#         if f"unit{i}" in msg or f"unit {i}" in msg:
#             unit = f"unit{i}"

#     results = []

#     if subject:
#         subject_path = os.path.join(PDF_FOLDER, "cse", subject)

#         if os.path.exists(subject_path):
#             for file in os.listdir(subject_path):
#                 file_clean = file.lower().replace(" ", "")

#                 if unit:
#                     if unit in file_clean:
#                         results.append(("cse", subject, file))
#                 else:
#                     results.append(("cse", subject, file))

#     return results


# # 📂 Serve PDFs
# @app.route('/pdfs/<path:filename>')
# def serve_pdf(filename):
#     return send_from_directory(PDF_FOLDER, filename)


# @app.route('/webhook', methods=['GET', 'POST'])
# def webhook():

#     # 🔹 Verification
#     if request.method == 'GET':
#         mode = request.args.get("hub.mode")
#         token = request.args.get("hub.verify_token")
#         challenge = request.args.get("hub.challenge")

#         if mode == "subscribe" and token == VERIFY_TOKEN:
#             return str(challenge), 200
#         else:
#             return "Verification failed", 403

#     # 🔹 Message handling
#     if request.method == 'POST':
#         data = request.json

#         try:
#             message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
#             sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

#             msg = message.lower()

#             # 💬 Friendly responses
#             if any(word in msg for word in ["thank", "thanks", "thank you"]):
#                 reply = "😊 You're welcome! If you need PDFs, just ask!"

#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 }

#                 requests.post(url, headers=headers, json=payload)
#                 return "ok", 200


#             if any(word in msg for word in ["bye", "goodbye"]):
#                 reply = "👋 Bye! Come back anytime for PDFs."

#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 }

#                 requests.post(url, headers=headers, json=payload)
#                 return "ok", 200


#             # 🔥 MENU SYSTEM
#             if msg in ["hi", "hello"]:
#                 reply = """👋 Welcome to CSE Bot

# 📚 Available Subjects:
# 1. CN
# 2. NMPS
# 3. SE

# 👉 Try:
# - cn
# - cn unit1
# - send nmps unit2

# Type 'help' for more info"""
                
#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 }

#                 requests.post(url, headers=headers, json=payload)
#                 return "ok", 200

#             # 🔹 HELP COMMAND
#             if "help" in msg:
#                 reply = """ℹ️ How to use:

# Send messages like:
# 👉 cn
# 👉 cn unit1
# 👉 send nmps unit2
# 👉 se notes

# Bot will send PDFs automatically 📄"""
                
#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 }

#                 requests.post(url, headers=headers, json=payload)
#                 return "ok", 200

#             # 🔹 SUBJECT LIST
#             if "subjects" in msg:
#                 reply = """📚 Subjects Available:

# - CN
# - NMPS
# - SE"""
                
#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 }

#                 requests.post(url, headers=headers, json=payload)
#                 return "ok", 200

#             # 🔹 PDF SEARCH
#             results = find_pdfs(message)

#             if results:
#                 for branch, subject, file in results:
#                     pdf_url = f"{NGROK_URL}/pdfs/{branch}/{subject}/{file}"

#                     payload = {
#                         "messaging_product": "whatsapp",
#                         "to": sender,
#                         "type": "document",
#                         "document": {
#                             "link": pdf_url,
#                             "filename": file
#                         }
#                     }

#                     requests.post(url, headers=headers, json=payload)

#             else:
#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {
#                         "body": "❌ No PDFs found.\nTry: cn or cn unit1"
#                     }
#                 }

#                 requests.post(url, headers=headers, json=payload)

#         except Exception as e:
#             print("Error:", e)

#         return "ok", 200


# if __name__ == '__main__':
#     app.run(port=5000)








# from flask import Flask, request, send_from_directory
# import requests
# import os

# app = Flask(__name__)

# # 🔐 Replace with your NEW token
# ACCESS_TOKEN = "EAAgxFfvcTZBIBRGyZAVFYUp4xuUh1URR3vI5Fwv7ECeZB7I5njJTRhfT9qkxAWexFrLulsNTAUDqocI9dZA8uTDZByT2c0eyboAFuGkbrrzckGZAgyYAjks27tL1ZBpOrdT2HjYS2ZAapWpsGeHQdTJo7UI03fMnTdd8JNMFtGZAFJxsLetWp63MmJjPx8oZCN7vs7SRKfbc0QRopd9d6ZAUL9gkV5pbgZBZBo5S0g08OR8j6y6w7fCZALqenRZArKYZBqsZBdJp1JtIeEZBU51jKOkSZADmastXjmA"
# PHONE_NUMBER_ID = "1095814390277545"
# VERIFY_TOKEN = "hello123"

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# PDF_FOLDER = os.path.join(BASE_DIR, "pdfs")
# # NGROK_URL = "https://sharply-lepidopterous-penny.ngrok-free.dev"
# NGROK_URL = "https://whatsapp-bot-1-63hu.onrender.com"


# # 🔍 Smart PDF finder
# def find_pdfs(user_message):
#     msg = user_message.lower()

#     subjects = ["cn", "nmps", "se"]

#     subject = None
#     unit = None

#     words = msg.split()

#     for s in subjects:
#         if s in words:
#             subject = s

#     for i in range(1, 6):
#         if f"unit{i}" in msg or f"unit {i}" in msg:
#             unit = f"unit{i}"

#     results = []

#     if subject:
#         subject_path = os.path.join(PDF_FOLDER, "cse", subject)

#         if os.path.exists(subject_path):
#             for file in os.listdir(subject_path):
#                 file_clean = file.lower().replace(" ", "")

#                 if unit:
#                     if unit in file_clean:
#                         results.append(("cse", subject, file))
#                 else:
#                     results.append(("cse", subject, file))

#     return results


# # 📂 Serve PDFs
# @app.route('/pdfs/<path:filename>')
# def serve_pdf(filename):
#     full_path = os.path.join(PDF_FOLDER, filename)
#     return send_from_directory(os.path.dirname(full_path), os.path.basename(full_path))


# @app.route('/webhook', methods=['GET', 'POST'])
# def webhook():

#     # 🔹 Verification
#     if request.method == 'GET':
#         mode = request.args.get("hub.mode")
#         token = request.args.get("hub.verify_token")
#         challenge = request.args.get("hub.challenge")

#         if mode == "subscribe" and token == VERIFY_TOKEN:
#             return str(challenge), 200
#         else:
#             return "Verification failed", 403

#     # 🔹 Message handling
#     if request.method == 'POST':
#         data = request.json

#         try:
#             message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
#             sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

#             msg = message.lower()

#             # ✅ DEFINE FIRST (IMPORTANT FIX)
#             url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

#             headers = {
#                 "Authorization": f"Bearer {ACCESS_TOKEN}",
#                 "Content-Type": "application/json"
#             }

#             # 💬 Friendly responses
#             if any(word in msg for word in ["thank", "thanks", "thank you"]):
#                 reply = "😊 You're welcome! If you need PDFs, just ask!"

#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 }

#                 requests.post(url, headers=headers, json=payload)
#                 return "ok", 200

#             if any(word in msg for word in ["bye", "goodbye"]):
#                 reply = "👋 Bye! Come back anytime for PDFs."

#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 }

#                 requests.post(url, headers=headers, json=payload)
#                 return "ok", 200

#             # 🔥 MENU
#             if msg in ["hi", "hello"]:
#                 reply = """👋 Welcome to CSE Bot

# 📚 Available Subjects:
# 1. CN
# 2. NMPS
# 3. SE

# 👉 Try:
# - cn
# - cn unit1
# - send nmps unit2

# Type 'help' for more info"""

#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 }

#                 requests.post(url, headers=headers, json=payload)
#                 return "ok", 200

#             # 🔹 HELP
#             if "help" in msg:
#                 reply = """ℹ️ How to use:

# 👉 cn
# 👉 cn unit1
# 👉 send nmps unit2
# 👉 se notes"""

#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 }

#                 requests.post(url, headers=headers, json=payload)
#                 return "ok", 200

#             # 🔹 SUBJECTS
#             if "subjects" in msg:
#                 reply = """📚 Subjects:

# - CN
# - NMPS
# - SE"""

#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 }

#                 requests.post(url, headers=headers, json=payload)
#                 return "ok", 200

#             # 🔹 PDF SEARCH
#             results = find_pdfs(message)

#             if results:
#                 for branch, subject, file in results:
#                     pdf_url = f"{NGROK_URL}/pdfs/{branch}/{subject}/{file}"

#                     payload = {
#                         "messaging_product": "whatsapp",
#                         "to": sender,
#                         "type": "document",
#                         "document": {
#                             "link": pdf_url,
#                             "filename": file
#                         }
#                     }

#                     requests.post(url, headers=headers, json=payload)

#             else:
#                 payload = {
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {
#                         "body": "❌ No PDFs found.\nTry: cn or cn unit1"
#                     }
#                 }

#                 requests.post(url, headers=headers, json=payload)

#         except Exception as e:
#             print("Error:", e)

#         return "ok", 200


# if __name__ == '__main__':
#     app.run(port=5000)



# from flask import Flask, request, send_from_directory
# import requests
# import os

# app = Flask(__name__)

# ACCESS_TOKEN = "EAAgxFfvcTZBIBRGyZAVFYUp4xuUh1URR3vI5Fwv7ECeZB7I5njJTRhfT9qkxAWexFrLulsNTAUDqocI9dZA8uTDZByT2c0eyboAFuGkbrrzckGZAgyYAjks27tL1ZBpOrdT2HjYS2ZAapWpsGeHQdTJo7UI03fMnTdd8JNMFtGZAFJxsLetWp63MmJjPx8oZCN7vs7SRKfbc0QRopd9d6ZAUL9gkV5pbgZBZBo5S0g08OR8j6y6w7fCZALqenRZArKYZBqsZBdJp1JtIeEZBU51jKOkSZADmastXjmA"
# PHONE_NUMBER_ID = "1095814390277545"
# VERIFY_TOKEN = "hello123"

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# PDF_FOLDER = os.path.join(BASE_DIR, "pdfs")

# NGROK_URL = "https://whatsapp-bot-1-63hu.onrender.com"


# # 🔍 Smart PDF finder
# def find_pdfs(user_message):
#     msg = user_message.lower()
#     subjects = ["cn", "nmps", "se"]

#     subject = None
#     unit = None

#     words = msg.split()

#     for s in subjects:
#         if s in words:
#             subject = s

#     for i in range(1, 6):
#         if f"unit{i}" in msg or f"unit {i}" in msg:
#             unit = f"unit{i}"

#     results = []

#     if subject:
#         subject_path = os.path.join(PDF_FOLDER, "cse", subject)

#         print("Checking path:", subject_path)  # debug

#         if os.path.exists(subject_path):
#             for file in os.listdir(subject_path):
#                 file_clean = file.lower().replace(" ", "")

#                 if unit:
#                     if unit in file_clean:
#                         results.append(("cse", subject, file))
#                 else:
#                     results.append(("cse", subject, file))

#     return results


# # 📂 FIXED PDF SERVE
# @app.route('/pdfs/<path:filename>')
# def serve_pdf(filename):
#     file_path = os.path.join(PDF_FOLDER, filename)

#     print("Serving file:", file_path)  # debug

#     if os.path.exists(file_path):
#         return send_from_directory(
#             os.path.dirname(file_path),
#             os.path.basename(file_path),
#             as_attachment=True
#         )
#     else:
#         return "File not found", 404


# @app.route('/webhook', methods=['GET', 'POST'])
# def webhook():

#     if request.method == 'GET':
#         mode = request.args.get("hub.mode")
#         token = request.args.get("hub.verify_token")
#         challenge = request.args.get("hub.challenge")

#         if mode == "subscribe" and token == VERIFY_TOKEN:
#             return str(challenge), 200
#         else:
#             return "Verification failed", 403

#     if request.method == 'POST':
#         data = request.json

#         try:
#             message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
#             sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

#             msg = message.lower()

#             url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

#             headers = {
#                 "Authorization": f"Bearer {ACCESS_TOKEN}",
#                 "Content-Type": "application/json"
#             }

#             # 💬 Friendly responses
#             if any(word in msg for word in ["thank", "thanks", "thank you"]):
#                 reply = "😊 You're welcome! If you need PDFs, just ask!"
#                 requests.post(url, headers=headers, json={
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 })
#                 return "ok", 200

#             if msg in ["hi", "hello"]:
#                 reply = """👋 Welcome to CSE Bot

# 📚 Subjects:
# - CN
# - NMPS
# - SE

# Try:
# cn
# cn unit1"""
#                 requests.post(url, headers=headers, json={
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": reply}
#                 })
#                 return "ok", 200

#             # 🔹 PDF SEARCH
#             results = find_pdfs(message)

#             if results:
#                 for branch, subject, file in results:
#                     pdf_url = f"{NGROK_URL}/pdfs/{branch}/{subject}/{file}"

#                     print("Sending:", pdf_url)

#                     requests.post(url, headers=headers, json={
#                         "messaging_product": "whatsapp",
#                         "to": sender,
#                         "type": "document",
#                         "document": {
#                             "link": pdf_url,
#                             "filename": file
#                         }
#                     })

#             else:
#                 requests.post(url, headers=headers, json={
#                     "messaging_product": "whatsapp",
#                     "to": sender,
#                     "type": "text",
#                     "text": {"body": "❌ No PDFs found"}
#                 })

#         except Exception as e:
#             print("Error:", e)

#         return "ok", 200


# if __name__ == '__main__':
#     app.run(port=5000)
from flask import Flask, request, send_file
import requests
from urllib.parse import quote
import os

app = Flask(__name__)

# 🔐 Use ENV in Render (fallback for local testing)
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN") or "EAAgxFfvcTZBIBRGZAr0wWTIDPfx4aicjFpOJFZBroYZCxN0UxZA9p0JjnBxCRSJ22l4G7WyfGAt36jAvUFw6y98cspY5ZB2ivtB14vgMdZBWetMSTq9DPZCfW3mFFVF3niCjTmAJc2sIF1fOio6EJ05Hz4YGrjIjJXJxxeciCq6DLyZAu3StlKam6pYEs98d2CWpdN4KM1HcZCAX0IIz5RPWZCnahAZBBU1ZCTqf0BfBPj2wQ21DymOnZBRlHzKIaWrvtZCiMgAFADygMgQmlT4nmEa4BXbraPO"
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID") or "1095814390277545"
VERIFY_TOKEN = "hello123"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_FOLDER = os.path.join(BASE_DIR, "pdfs")

# 🌐 Your Render URL
BASE_URL = "https://whatsapp-bot-ymr2.onrender.com"


# 🔥 SMART + FUTURE-PROOF PDF FINDER
def find_pdfs(user_message):
    msg = user_message.lower()
    words = msg.split()

    base_path = os.path.join(PDF_FOLDER, "CSE")

    subject = None
    unit = None

    # 🔹 Auto-detect subject (no hardcoding)
    if os.path.exists(base_path):
        for folder in os.listdir(base_path):
            if folder.lower() in words:
                subject = folder  # keeps original case (CN, NMPS, etc.)

    # 🔹 Detect unit
    for i in range(1, 6):
        if f"unit{i}" in msg or f"unit {i}" in msg:
            unit = f"unit{i}"

    results = []

    if subject:
        subject_path = os.path.join(base_path, subject)

        if os.path.exists(subject_path):
            for file in os.listdir(subject_path):
                file_clean = file.lower().replace(" ", "")

                if unit:
                    if unit in file_clean:
                        results.append(("CSE", subject, file))
                else:
                    results.append(("CSE", subject, file))

    return results


# 📂 SERVE PDFs (FINAL FIX USING send_file)
@app.route('/pdfs/<path:filename>')
def serve_pdf(filename):
    file_path = os.path.join(PDF_FOLDER, filename)

    print("Serving:", file_path)

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():

    # 🔹 Verification
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge"), 200
        return "Verification failed", 403

    # 🔹 Message handling
    if request.method == 'POST':
        data = request.json

        try:
            message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

            msg = message.lower()

            url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

            headers = {
                "Authorization": f"Bearer {ACCESS_TOKEN}",
                "Content-Type": "application/json"
            }

            # 💬 Friendly replies
            if any(word in msg for word in ["thank", "thanks"]):
                reply = "😊 You're welcome!"
                response = requests.post(url, headers=headers, json={
                    "messaging_product": "whatsapp",
                    "to": sender,
                    "type": "text",
                    "text": {"body": "Test reply"}
                })

                print("STATUS:", response.status_code)
                print("RESPONSE:", response.text)
                return "ok", 200

            if msg in ["hi", "hello"]:
                reply = """👋 Welcome to CSE Bot

📚 Available Subjects:
- CN
- NMPS
- SE

Try:
cn
cn unit1"""
                requests.post(url, headers=headers, json={
                    "messaging_product": "whatsapp",
                    "to": sender,
                    "type": "text",
                    "text": {"body": reply}
                })
                return "ok", 200

            # 🔍 Find PDFs
            results = find_pdfs(message)

            if results:
                for branch, subject, file in results:
                    pdf_url = f"{BASE_URL}/pdfs/{branch}/{subject}/{quote(file)}"

                    print("Sending:", pdf_url)

                    requests.post(url, headers=headers, json={
                        "messaging_product": "whatsapp",
                        "to": sender,
                        "type": "document",
                        "document": {
                            "link": pdf_url,
                            "filename": file
                        }
                    })
            else:
                requests.post(url, headers=headers, json={
                    "messaging_product": "whatsapp",
                    "to": sender,
                    "type": "text",
                    "text": {
                        "body": "❌ No PDFs found.\nTry: cn or cn unit1"
                    }
                })

        except Exception as e:
            print("Error:", e)

        return "ok", 200


if __name__ == '__main__':
    app.run(port=5000)