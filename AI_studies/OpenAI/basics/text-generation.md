

Chat completion has replaced completion API endpoint.
Chat completion API allows for more conversation, context (system message, AI message equivalent in langchain) to be provided, whereas simple completion API takes a single text (known as prompt) as input.




## Example code / calling OpenAI API
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

## Message types:
### Conversation History
Including conversation history is important when user instructions refer to prior messages. In the example above, the user’s final question of "Where was it played?" only makes sense in the context of the prior messages about the World Series of 2020. Because the models have no memory of past requests, all relevant information must be supplied as part of the conversation history in each request. If a conversation cannot fit within the model’s token limit, it will need to be shortened in some way.

### System Messages
The system message helps set the behavior of the assistant. For example, you can modify the personality of the assistant or provide specific instructions about how it should behave throughout the conversation. However note that the system message is optional and the model’s behavior without a system message is likely to be similar to using a generic message such as "You are a helpful assistant."

### User Messages
The user messages provide requests or comments for the assistant to respond to. Assistant messages store previous assistant responses, but can also be written by you to give examples of desired behavior.



## Example return object
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

response['choices'][0]['message']['content'] # ---> extracts the reply

### Finish reasons
Every response will include a finish_reason. The possible values for finish_reason are:
- stop: API returned complete message, or a message terminated by one of the stop sequences provided via the stop parameter
- length: Incomplete model output due to max_tokens parameter or token limit
- function_call: The model decided to call a function
- content_filter: Omitted content due to a flag from our content filters
- null: API response still in progress or incomplete
- Depending on input parameters, the model response may include different information.




## JSON mode;
A common way to use Chat Completions is to instruct the model to always return a JSON object that makes sense for your use case, by specifying this in the system message. While this does work in some cases, occasionally the models may generate output that does not parse to valid JSON objects.

To prevent these errors and improve model performance, when calling gpt-4-1106-preview or gpt-3.5-turbo-1106, you can set response_format to { "type": "json_object" } to enable JSON mode. When JSON mode is enabled, the model is constrained to only generate strings that parse into valid JSON object.

Important notes:

- When using JSON mode, always instruct the model to produce JSON via some message in the conversation, for example via your system message. If you don't include an explicit instruction to generate JSON, the model may generate an unending stream of whitespace and the request may run continually until it reaches the token limit. To help ensure you don't forget, the API will throw an error if the string "JSON" does not appear somewhere in the context.
- The JSON in the message the model returns may be partial (i.e. cut off) if finish_reason is length, which indicates the generation exceeded max_tokens or the conversation exceeded the token limit. To guard against this, check finish_reason before parsing the response.
- JSON mode will not guarantee the output matches any specific schema, only that it is valid and parses without errors.




## tokens - counting and managing tokens:
Language models read and write text in chunks called tokens. In English, a token can be as short as one character or as long as one word (e.g., a or apple), and in some languages tokens can be even shorter than one character or even longer than one word.

For example, the string "ChatGPT is great!" is encoded into six tokens: ["Chat", "G", "PT", " is", " great", "!"].

The total number of tokens in an API call affects:

How much your API call costs, as you pay per token
How long your API call takes, as writing more tokens takes more time
Whether your API call works at all, as total tokens must be below the model’s maximum limit (4097 tokens for gpt-3.5-turbo)
Both input and output tokens count toward these quantities. For example, if your API call used 10 tokens in the message input and you received 20 tokens in the message output, you would be billed for 30 tokens. Note however that for some models the price per token is different for tokens in the input vs. the output (see the pricing page for more information).

To see how many tokens are used by an API call, check the usage field in the API response (e.g., response['usage']['total_tokens']).

Chat models like gpt-3.5-turbo and gpt-4 use tokens in the same way as the models available in the completions API, but because of their message-based formatting, it's more difficult to count how many tokens will be used by a conversation.

### counting tokens without a API call
To see how many tokens are in a text string without making an API call, use OpenAI’s tiktoken Python library. Example code can be found in the OpenAI Cookbook’s guide on how to count tokens with tiktoken.

Each message passed to the API consumes the number of tokens in the content, role, and other fields, plus a few extra for behind-the-scenes formatting. This may change slightly in the future.

If a conversation has too many tokens to fit within a model’s maximum limit (e.g., more than 4097 tokens for gpt-3.5-turbo), you will have to truncate, omit, or otherwise shrink your text until it fits. Beware that if a message is removed from the messages input, the model will lose all knowledge of it.

Note that very long conversations are more likely to receive incomplete replies. For example, a gpt-3.5-turbo conversation that is 4090 tokens long will have its reply cut off after just 6 tokens.






## Reproducible outputs
Chat Completions are non-deterministic by default (which means model outputs may differ from request to request). That being said, we offer some control towards deterministic outputs by giving you access to the seed parameter and the system_fingerprint response field.

To receive (mostly) deterministic outputs across API calls, you can:
- Set the seed parameter to any integer of your choice and use the same value across requests you'd like deterministic outputs for.
- Ensure all other parameters (like prompt or temperature) are the exact same across requests.
- Sometimes, determinism may be impacted due to necessary changes OpenAI makes to model configurations on our end. To help you keep track of these changes, we expose the system_fingerprint field. If this value is different, you may see different outputs due to changes we've made on our systems.

https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter


## Frequency and presence penalties
The frequency and presence penalties found in the Chat Completions API and Legacy Completions API can be used to reduce the likelihood of sampling repetitive sequences of tokens.

Reasonable values for the penalty coefficients are around 0.1 to 1 if the aim is to just reduce repetitive samples somewhat. If the aim is to strongly suppress repetition, then one can increase the coefficients up to 2, but this can noticeably degrade the quality of samples. Negative values can be used to increase the likelihood of repetition.

frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.



### explainer into frequency and presence penalties

Imagine you're telling a story with your friends, and you all take turns adding one sentence at a time. You wouldn't want the story to repeat the same things over and over, and you also wouldn't want everyone to keep mentioning something that's only supposed to be a small part of the story. To keep the story interesting, you'd want new ideas and events to come up.

In the world of language models, like the one you're using to chat with me now, "frequency penalty" and "presence penalty" are tools used to make the model's responses more varied and interesting, kind of like how you'd want your friends' additions to the story to be:

Frequency Penalty: This is like telling your friends, "Try not to repeat things too much." If you set a frequency penalty, the language model tries not to repeat the same words and phrases within a response. The higher the penalty, the less likely the model is to repeat itself.

Presence Penalty: This is like saying, "Don't keep bringing up the same topic." The presence penalty makes the model less likely to keep mentioning the same thing over and over throughout the conversation. So if you've already talked about dragons in your story, a higher presence penalty would make the model try to move on to other subjects rather than bringing up dragons again.

Both of these penalties help the language model make the conversation or the text it's generating more diverse and prevent it from getting stuck on a loop, repeating the same words or topics too much. It keeps the "story" it's telling you fresh and more engaging.



## logit bias parameter
Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

### ELI5 w ChatGPT
Imagine you have a bag full of letter tiles, like the ones you use in the game Scrabble. You're going to pull out tiles to make a word, and normally every tile has the same chance of being picked. But let's say you really love the letter "Z" and you want it to show up more often when you're making words. What you could do is add more "Z" tiles to the bag to increase the chances of picking a "Z".

In the world of language models, "logit bias" is like adding or removing letter tiles to change how likely they are to be picked when the model is generating text.

When we talk about "logits", think of them as the model's "thinking" about how likely each letter (or word) should be used next in a sentence. Before the model decides what to pull out of the bag (before it "samples" the next word), it looks at the logits to see which letters or words are more likely.

The "logit bias" allows you to tweak these logits. If you set a positive bias for a token (a word or piece of a word), it's like adding more of that tile to the bag, making the model more likely to use it in the text. If you set a negative bias, it's like taking tiles out of the bag, making it less likely to be used.

If you give a small bias (like between -1 and 1), you're making a slight adjustment. It's a bit like adding just a few more tiles or taking a few away.
If you give a huge bias (like -100 or 100), you're making a big change. A big positive number is like filling the bag with only "Z" tiles, so you're almost sure to pick "Z". A big negative number is like removing all the "Z" tiles from the bag, so you'll never pick a "Z".
So, "logit bias" lets you influence the model's choice of words, making some more common and others less, or even completely banning them or ensuring they're chosen.






