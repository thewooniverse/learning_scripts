# import modules
from dotenv import load_dotenv
import os
import json
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



#
# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": unit})
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})



def run_conversation():
    # Step 1: send the conversation and available functions to the model
    ## prepare the conversation and tools
    messages = [{"role": "user", "content": "What's the weather like in San Francisco, Tokyo, and Paris?"}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]

    ## send it to the model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    # print(response)
    response_message = response.choices[0].message # gets the mssage from response message 1
    tool_calls = response_message.tool_calls # gets the tool calls from response message 1


    # Step 2: check if the model wanted to call a function
    if tool_calls:

        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_current_weather": get_current_weather,
        }  # only one function in this example, but you can have multiple
        messages.append(response_message)  # extend conversation with assistant's reply

        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls: # each tool_call is a ChatCompletionMessageToolCall ojbect
            function_name = tool_call.function.name # get the name of the function that is to be called from the tool_call
            function_to_call = available_functions[function_name] # get the function from the available_functions using the function name extracted
            function_args = json.loads(tool_call.function.arguments) #json.loads >> converts (deserializes) json string into its corresponding python object.
            
            function_response = function_to_call( # call the function
                location=function_args.get("location"), # set the parameters based on the function args extracted above
                unit=function_args.get("unit"), # set the parameters based on the function args extracted above
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id, # e.g. call_bXvObnJukp5zHSuTzYjpXKEO from tool_call object
                    "role": "tool", # tool
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response
        

        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        pp.pprint(messages)
        # pp.pprint(second_response.choices[0].message.content)
        print(second_response)
        return second_response
run_conversation()



# response object 1 breakdown:
"""
ChatCompletion(id='chatcmpl-8gpEwUU2ZBRl99IfkYmofg2LdBzRk', 
               choices=[Choice(
                   finish_reason='tool_calls', 
                   index=0, 
                   logprobs=None, 
                   message=ChatCompletionMessage(
                       content=None, 
                       role='assistant', 
                       function_call=None, 
                       tool_calls=[ChatCompletionMessageToolCall(id='call_bXvObnJukp5zHSuTzYjpXKEO', 
                                                                 function=Function(arguments='{"location": "San Francisco", "unit": "celsius"}', 
                                                                                   name='get_current_weather'), type='function'), 
                                   ChatCompletionMessageToolCall(id='call_Ey7HmsVq5w4wsJvGX6HOQZHi', 
                                                                 function=Function(arguments='{"location": "Tokyo", "unit": "celsius"}', 
                                                                                   name='get_current_weather'), 
                                                                                   type='function'), 
                                   ChatCompletionMessageToolCall(id='call_hNsVGF1XIYAhcJ0gIdwuuVUp', 
                                                                 function=Function(arguments='{"location": "Paris", "unit": "celsius"}', 
                                                                                   name='get_current_weather'), 
                                                                                   type='function')]))], 
               created=1705217434, 
               model='gpt-3.5-turbo-1106', 
               object='chat.completion', 
               system_fingerprint='fp_cbe4fa03fe', 
               usage=CompletionUsage(completion_tokens=77, prompt_tokens=88, total_tokens=165))
"""



"""
response object 2:

ChatCompletion(id='chatcmpl-8gppIsRCNZTCKWuoQKwD2AlFkI5qu', 
               choices=[
                   Choice(finish_reason='stop', 
                          index=0, 
                          logprobs=None, 
                          message=ChatCompletionMessage(content="Currently, the weather in San Francisco is 72°C, in Tokyo it's 10°C, and in Paris it's 22°C.", 
                                                        role='assistant', 
                                                        function_call=None, 
                                                        tool_calls=None))], 
               created=1705219688, 
               model='gpt-3.5-turbo-1106', 
               object='chat.completion', 
               system_fingerprint='fp_cbe4fa03fe', 
               usage=CompletionUsage(completion_tokens=29, prompt_tokens=169, total_tokens=198))
"""






"""
This is messages that is sent

[   {   'content': "What's the weather like in San Francisco, Tokyo, and "
                   'Paris?',
        'role': 'user'},


    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_u7Jnk3DK5IDfB6mJCDEuNfie', function=Function(arguments='{"location": "San Francisco, CA", "unit": "celsius"}', name='get_current_weather'), type='function'), ChatCompletionMessageToolCall(id='call_4S1YuILrfJZsm27FQzWD3Ihb', function=Function(arguments='{"location": "Tokyo, Japan", "unit": "celsius"}', name='get_current_weather'), type='function'), ChatCompletionMessageToolCall(id='call_OGDyNefb0zoJi2TLSJjPBm7g', function=Function(arguments='{"location": "Paris, France", "unit": "celsius"}', name='get_current_weather'), type='function')]),
    {   'content': '{"location": "San Francisco", "temperature": "72", "unit": '
                   '"celsius"}',
        'name': 'get_current_weather',
        'role': 'tool',
        'tool_call_id': 'call_u7Jnk3DK5IDfB6mJCDEuNfie'},
    {   'content': '{"location": "Tokyo", "temperature": "10", "unit": '
                   '"celsius"}',
        'name': 'get_current_weather',
        'role': 'tool',
        'tool_call_id': 'call_4S1YuILrfJZsm27FQzWD3Ihb'},
    {   'content': '{"location": "Paris", "temperature": "22", "unit": '
                   '"celsius"}',
        'name': 'get_current_weather',
        'role': 'tool',
        'tool_call_id': 'call_OGDyNefb0zoJi2TLSJjPBm7g'}]
ChatCompletion(id='chatcmpl-8gqKMzCnjIrQJGTXaSQ1AXU1PKv4P', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="The current weather in San Francisco is 72°C, in Tokyo it's 10°C, and in Paris it's 22°C.", role='assistant', function_call=None, tool_calls=None))], created=1705221614, model='gpt-3.5-turbo-1106', object='chat.completion', system_fingerprint='fp_cbe4fa03fe', usage=CompletionUsage(completion_tokens=28, prompt_tokens=175, total_tokens=203))
(.venv) ➜  basics git:(main) ✗ python3 functions.py
[   {   'content': "What's the weather like in San Francisco, Tokyo, and "
                   'Paris?',
        'role': 'user'},
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_OUJOwWQjts5CRAmEbmQYbZqz', function=Function(arguments='{"location": "San Francisco", "unit": "celsius"}', name='get_current_weather'), type='function'), ChatCompletionMessageToolCall(id='call_NNvFPZyjfFVsTedEJUMP1rJc', function=Function(arguments='{"location": "Tokyo", "unit": "celsius"}', name='get_current_weather'), type='function'), ChatCompletionMessageToolCall(id='call_7aQMLLOTqt4dyLW4aXud66UF', function=Function(arguments='{"location": "Paris", "unit": "celsius"}', name='get_current_weather'), type='function')]),
    {   'content': '{"location": "San Francisco", "temperature": "72", "unit": '
                   '"celsius"}',
        'name': 'get_current_weather',
        'role': 'tool',
        'tool_call_id': 'call_OUJOwWQjts5CRAmEbmQYbZqz'},
    {   'content': '{"location": "Tokyo", "temperature": "10", "unit": '
                   '"celsius"}',
        'name': 'get_current_weather',
        'role': 'tool',
        'tool_call_id': 'call_NNvFPZyjfFVsTedEJUMP1rJc'},
    {   'content': '{"location": "Paris", "temperature": "22", "unit": '
                   '"celsius"}',
        'name': 'get_current_weather',
        'role': 'tool',
        'tool_call_id': 'call_7aQMLLOTqt4dyLW4aXud66UF'}]


Second response (response to sending the whole messages / conversation history with function call responses above):

ChatCompletion(id='chatcmpl-8gqQ9yKiylCMKVVG5EAewSPPnf6yQ', 
               choices=[Choice(finish_reason='stop', 
                               index=0, 
                               logprobs=None, 
                               message=ChatCompletionMessage(content="Currently, in San Francisco, the weather is 72°C. In Tokyo, the temperature is 10°C, and in Paris, it's 22°C.", 
                                                             role='assistant', 
                                                             function_call=None, 
                                                             tool_calls=None))], 
               created=1705221973, 
               model='gpt-3.5-turbo-1106', 
               object='chat.completion', 
               system_fingerprint='fp_fe56e538d5', 
               usage=CompletionUsage(completion_tokens=33, prompt_tokens=169, total_tokens=202))

"""
