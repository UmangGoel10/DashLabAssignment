import os
import json
from marshal import dumps
import time


from groq import Groq

client = Groq(
    api_key="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",
)

file1 = open("input.txt", "r")
file2 = open("output.json", "w")
string = " "
while True:
    string = file1.readline()
    timesent = int(time.time())

    if string is "":
        break
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": string,

            }
        ],
        model="llama3-8b-8192",
    )
    output = chat_completion.choices[0].message.content
    timerec = int(time.time())

    basic_structure = [{
        'prompt': string,
        'Message': output,
        'Timesent': timesent,
        'Timerec': timerec,
        'source': "llama3-8b-8192",
    }]

    json.dump(basic_structure, file2,indent=4)

file1.close()
file2.close()
