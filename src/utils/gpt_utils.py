import openai
import os

# Set up your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]


def gpt_api(query, model_type="text-davinci-002"):
    # Generate the text using the OpenAI API
    response = openai.Completion.create(
        engine=model_type,
        prompt=query,
        temperature=0.7,
        max_tokens=1024
    )

    return response.choices[0].text


if __name__ == '__main__':
    print(gpt_api("你是谁"))
