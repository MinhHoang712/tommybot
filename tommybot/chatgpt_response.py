import openai

OPEN_API_KEY = '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'
MAX_TOKENS = 2048
openai.api_key = OPEN_API_KEY

messages = [
    {
        "role" : "system",
        "content" : ""
    }
]


def generateText(UserInputQuestion = ""):
    messages.append({"role": "user", "content" : UserInputQuestion})
    rsp = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0, # inovation , [0, 1]
        max_tokens=MAX_TOKENS # default = model compability
    )
    reply = rsp["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply
