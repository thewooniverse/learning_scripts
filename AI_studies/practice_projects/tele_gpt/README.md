# Overview
TeleGPT is a simple ChatGPT integrated Telegram Bot with persistent memory and context awareness.
TeleGPT can be configured to each user's OpenAI API Key and use different chat agents as required (GPT 3.5 and 4.0 supported).
TeleGPT is built on two large libraries: Langchain and Telebot with Chroma based persistent storage RAG for persistent context awareness.

To use Telebot, you may simply start a chat with @telegptwastaken_bot on Telegram or invite it to your group; after providing your API Key you should be able to use it normally.

In order to have multiple persistent / categorized chat histories with the bot, you may start several different groups with the agent inside it.
For example, you may have a new group with each topic with the bot:
- Translate
- Cooking
- Travel

## Features and Commands
/start or /settings - opens the basic set up / settings message and a list of commands and examples
/chat "query" - returns context aware responses to the query from the chat agent
/get_config - gets the current configuration (minus the api key)
/set_api_key "api_key" - sets API key and erases both messages + deleting the message after setting the config to use the stored API keys;
/persistent_off /persistent_on - turns the persistent settings on or off
/clear_chat_history - clears the context / chat history completely
/set_model - allows user to use different chat models
/set_temp - allows user to change the temperature (0-1).

/chat_history "query" - returns the documents and queries and response from the persistent chat history that best match the query
/set_system_message - sets system message / instructions to the bot





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
9. Buttons testing.



Overall - complete the development features above; and learn to push the bot into a VPS to get it set up and running all the time with bis.





