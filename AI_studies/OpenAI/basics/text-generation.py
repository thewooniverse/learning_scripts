# import modules
from dotenv import load_dotenv
import os
from openai import OpenAI
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4, width=80, depth=2)

# env variables, constants and API keys
load_dotenv()
openai_api_key=os.getenv('OPENAI_API_KEY', 'YourAPIKey_BACKUP')
serpapi_api_key=os.getenv("SERPAPI_API_KEY", "YourAPIKey_Backup")
# print(serpapi_api_key) # check
# print(openai_api_key)

client = OpenAI()


"""
/// QUICKSTART ///
"""

# response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
#   ])
# print(response)
"""
ChatCompletion(id='chatcmpl-8dI6qmgl3tR0iBo5cn9xyiCDsNqgD', 
choices=[Choice(finish_reason='stop', 
index=0, message=ChatCompletionMessage(content='The 2020 World Series was played at Globe Life Field in Arlington, Texas.', role='assistant', function_call=None, tool_calls=None), logprobs=None)], 
created=1704375096, model='gpt-3.5-turbo-0613', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=17, prompt_tokens=53, total_tokens=70))

Next up - study chat completion object / quickstart guide below:
 |      Returns:
 |          A dictionary representation of the model.
"""
# print(response.choices[0].message)
"""
ChatCompletionMessage(content='The World Series in 2020 was played in Arlington, Texas at the Globe Life Field.',
role='assistant', function_call=None, tool_calls=None)
"""
# help(response)
# print(response.dict()['choices'][0]['message']['content'])
"""
The World Series in 2020 was played at Globe Life Field in Arlington, Texas.
"""


# help(response)
"""
https://platform.openai.com/docs/guides/text-generation/
-> Basic documentation on chat completion
https://platform.openai.com/docs/api-reference/chat
-> goes into detail on chat completion, chat completion objects, and chat completion chunk objects.
"""



























"""
//////////// Text Generation Capabilities walkthrough ////////////

https://platform.openai.com/docs/guides/text-generation/chat-completions-api

Chat completion example:
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
        "role": "assistant"
      },
      "logprobs": null
    }
  ],
  "created": 1677664795,
  "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
  "model": "gpt-3.5-turbo-0613",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 17,
    "prompt_tokens": 57,
    "total_tokens": 74
  }
}
"""

r2 = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are an expert chef that can help me decide what to cook at home based on the ingredients I have"},
    {"role": "user", "content": "My name El Jeffe, please call me this"},
    {"role": "assistant", "content": "I will remember your name as El Jeffe"},
    {"role": "user", "content": "Whats my name"}
  ]
)
print(r2)
# print(r2.dict()['choices'][0]['message']['content']) << method is deprecated
dump = r2.model_dump()
print(dump)
print(type(dump)) # class 'dict'
"""
ChatCompletion(id='chatcmpl-8flUGu4wmDVLXJLiz9loIKrtMkg34', 
choices=[Choice(finish_reason='stop', 
index=0, 
message=ChatCompletionMessage(content='Your name is El Jeffe.', role='assistant', function_call=None, tool_calls=None), logprobs=None)], 
created=1704964680, 
model='gpt-4-0613', 
object='chat.completion', 
system_fingerprint=None, 
usage=CompletionUsage(completion_tokens=7, 
prompt_tokens=62, 
total_tokens=69))
---
Your name is El Jeffe.
"""



"""
JSON mode:
"""

# response = client.chat.completions.create(
#   model="gpt-3.5-turbo-1106",
#   response_format={ "type": "json_object" },
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
#     {"role": "user", "content": "Who won the last world cup, and who was their coach?"}
#   ]
# )
# print(response.choices[0].message.content)
"""
{
  "winner": "France",
  "coach": "Didier Deschamps"
}
"""




"""
// Frequency and Presence Penalties testing //

"""
# r3 = client.chat.completions.create(
#   model="gpt-4",
#   frequency_penalty = 2, # positive value decreases the likelihood of repeating itself.
#   presence_penalty =  2, # positive value increases the likelihood of new topics by penalizing older topics
#   messages=[
#     {"role": "system", "content": "You are a creative poet who rambles on about things"},
#     {"role": "user", "content": "write me a 10 line poem about computers, AI and whatever else."}
#   ]
# )
# print(r3.choices[0].message.content)











"""
// API reference playground //
"""
# userid
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  user="150235",
  n=3,
  messages=[
    {"role": "system", "content": "You are a creative poet"},
    {"role": "user", "content": "Please write me a haiku about Artificial Intellgience"}
  ])
pp.pprint(completion.model_dump())














"""
//////////// Chat completion objects ////////////
"""
{
  "id": "chatcmpl-123", # A unique identifier for the chat completion.
  "object": "chat.completion", # The object type, which is always chat.completion.
  "created": 1677652288, # The Unix timestamp (in seconds) of when the chat completion was created.
  "model": "gpt-3.5-turbo-0613", # The model used for the chat completion.

  "system_fingerprint": "fp_44709d6fcb", # This fingerprint represents the backend configuration that the model runs with.
  # Can be used in conjunction with the seed request parameter to understand when backend changes have been made that might impact determinism.

  "choices": [{ # A list of chat completion choices. Can be more than one if n is greater than 1.
    "index": 0, # The index of the choice in the list of choices.

    "message": { # A chat completion message generated by the model.
      "role": "assistant", # The role of the author of this message.
      "content": "\n\nHello there, how may I assist you today?", # The contents of the message.
      # The tool calls generated by the model, such as function calls.

    },

    "logprobs": 0, # null, # Log probability information for the choice. 
    "finish_reason": "stop" 
    # The reason the model stopped generating tokens. 
    # This will be:
    # stop if the model hit a natural stop point or a provided stop sequence,
    # length if the maximum number of tokens specified in the request was reached, 
    # content_filter if content was omitted due to a flag from our content filters, 
    # tool_calls if the model called a tool, or 
    # function_call (deprecated) if the model called a function. << function call is deprecated
  }],

  "usage": {# Usage statistics for the completion request.
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
    } 
}




