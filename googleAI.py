import google.generativeai as genai

GOOGLE_GEMINI_API_KEY = "AIzaSyAJawNkDUAT24ic1rY4ZEBdz0HwmFc2C5Y"

genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

client_message = input(str("Digite uma mensagem: "))

response = model.generate_content(client_message)

print(response.text)