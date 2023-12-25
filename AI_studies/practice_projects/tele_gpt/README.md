# Overview
TeleGPT is a simple ChatGPT integrated Telegram Bot with persistent memory, context awareness and configurability.
TeleGPT allows users to interface with ChatGPT using Telegram, maintaining persistent memory and context awareness based on chat history;
TeleGPT can be easily configured for various settings such as temperature, model type, persistence, system messages etc...
TeleGPT is built on two large libraries: Langchain and Telebot with Chroma based persistent storage RAG for persistent context awareness.

## Usage
To use Telebot, you may simply start a chat with @telegptwastaken_bot on Telegram or invite it to your group; after providing your API Key (/set_apikey sk-exampleapikey) you should be able to get started. TeleGPT can be configured to each user's OpenAI API Key and use different chat agents as required (GPT 3.5 and 4.0 supported).

In order to have multiple persistent / categorized chat histories with the bot, you may start several different groups with the agent inside it.
For example, you may have a new group with each topic with the bot:
- Translate
- Cooking
- Travel
And for each group chat, you may configure the model in each group to have different system messages, temperatures and models based on your use case.


## Features and Commands
-- basics --
- /start or /settings - opens the basic set up / settings message and a list of commands and examples
- /chat "query" - returns context aware responses to the query from the chat agent

-- settings --
- /get_config - gets the current configuration (minus the api key)
- /set_apikey "api_key" - sets API key and erases both messages + tries to delete the message after setting the config to use the stored API keys for safety;
- /logging_on /logging_off - turns the chat logging feature (saving chat history persistently), on or off.
- /context_on /context_off - turns off context awareness of the model, model no longer refers to persistent chat history for context.
- /set_model - allows user to use different chat models, accepted are ["gpt-3.5-turbo", "gpt-4-0613", "gpt-4", 'gpt-3.5-turbo-0613']
- /set_temp - allows user to change the temperature (0-1).
- /set_system_message - sets additional System Messages to the agent, for example "You are an expert chef or travel guide" to further personalize the model.
- /clear_history - clears the context / chat history completely



### Dev todos
1. Complete simple message sending / response telegram bots -> completed 
2. Integrate simple version of querying chat agent via Telegram bot /chat "query" feature -> completed
3. Formatting of the query responses - Markdown -> completed
4. Settings and configuration commands:
    - API key provisions and entering <- completed
    - Getting / Setting new additional system messages (max word count)
    - More settings;
6. Saving chat history to chat stores
7. RAG based on chat history
8. Clearing chat history
-- completed above --
10. VPS hosting and testing.


