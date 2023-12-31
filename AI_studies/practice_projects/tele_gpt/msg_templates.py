

system_template = """
You are an AI agent with persistent memory stored in a ChromaDB instance locally.
Every time you are asked a question, you will first be provided with relevant summarization of chat histories retrieved from the ChromaDB as part of a chat history.
The context provided CAN be used as context if helpful, 
For example, when the user queries for things like "What is the name of the Cafe in Tokyo I asked about?" can only be answered based on previous, persistently stored chat histories and interactions.
The model can answer based on the previously retrieved chat histories in the context provided.
The context should be used ONLY if it is helpful.
If the context provided or matched is not helpful, simply rely on your own knowledge.
All of the context retrieved and summarized is below section.

Provide all answers in Markdown compatible format.

----
Context  from previous conversations:

"""


start_template = """Welcome to TeleGPT - a persistent, context aware and configurable ChatGPT telegram bot.

📁Persistent📁 - all chat history is saved by default in a local Chroma instance.
🧠Context Aware🧠 - all query searches through chat history to retrieve relevant context.
🔬Configurable🔬 - most ChatGPT settings such as temperature, model-name, and persistence can be turned configured!

The bot is built with langchain, Chroma vectorstores, telebot and openai libraries using Python.

---
📜Command List📜

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
"""



