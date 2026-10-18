import os
from google import genai

client = genai.Client(api_key = 'AQ.Ab8RN6Kn37T2GxmgMnzrXGm-cWDZo53McDaIcZMdxZkOpqAQqw')
with open("CHATGPT_DEVSOC.txt","r") as file:
    for line in file:
        prompt = line.strip()
        print(f"Q. {prompt}")
        response = client.models.generate_content(
            model = "gemini-3.5-flash-lite",
            contents = prompt,
            config = {'system_instruction':"Do not use any markdown formatting like bold asterisks, italics. You can use anything which will be shown in command terminal"}
        )
        answer = response.text
        print(f"A. {answer}\n")
