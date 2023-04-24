import openai

OPEN_API_KEY = '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'

openai.api_key = OPEN_API_KEY


def generateText(UserInputQuestion = ""):
    messages = ({"role": "user", "content" : UserInputQuestion})
    rsp = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0, # inovation , [0, 1]
    )
    reply = rsp["choices"][0]["message"]["content"]
    return reply
