from dotenv import load_dotenv
import openai, os
load_dotenv()


openai.api_key = os.getenv('OPENAI_KEY')

def ai_response(prompt):
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        temperature = 0.75,
        max_tokens = 300
    )
    refine_response = str(response['choices'][0]['text'])
    return refine_response