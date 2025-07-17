import google.generativeai as genai

# Explicitly set your API key (keep this private!)
api_key = "AIzaSyAumAOfcvXR9eQZiXRdXxDETvCLvAlChTM"

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content("write a paragraph about the weather in Vietnamx")
print("\n<**response from gemini api**>\n")
print(response.text)
