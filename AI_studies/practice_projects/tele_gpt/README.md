# Overview
TeleGPT is a simple ChatGPT integrated Telegram Bot with persistent memory and context awareness.
TeleGPT can be configured to each user's OpenAI API Key and use different chat agents as required (GPT 3.5 and 4.0 supported).
TeleGPT is built on two large libraries: Langchain and Telebot with Chroma based persistent storage RAG for persistent context awareness.

To use Telebot, you may simply start a chat with @telegptwastaken_bot on Telegram or invite it to your group; after providing your API Key you should have access.


## Features and Commands
/chat "query" - returns context aware responses to the query from the chat agent
/clear - clears the context / chat history completely
/chat_history "query" - returns the documents and queries and response from the persistent chat history that best match the query
/api_key "api_key" - enters the API key for the given chat group
/settings - opens the settings and configuration for the given chat environment
/add_system_message - adds system message / instructions to the bot


In order to have multiple persistent / categorized chat histories with the bot, you may start several different groups with the agent inside it.
For example, you may have one with:
- Translate TeleGPT
- Cooking TeleGPT



### Dev todos
1. Complete simple message sending / response telegram bots -> completed 
2. Integrate simple version of querying chat agent via Telegram bot /chat "query" feature -> completed
3. Formatting of the query responses - Markdown -> completed
-- completed above --
4. Settings, configurations and API keys // buttons
5. API key provisions and entering
6. Saving chat history to chat stores
7. RAG based on chat history
8. Clearing chat history




