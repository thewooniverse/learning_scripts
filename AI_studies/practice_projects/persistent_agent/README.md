# Persistent Agent
Persistent Agent is simply a GPT-4 wrapper that has persistent memory storage and context.

Procedure:
-> Agent is asked a new query
-> Chroma Database (containing embedded chatlogs) is searched using a retrieval / search algorithm to get relevant documents - using MMR
-> The retrieved documents are then summarized as context in the form of a template as a SystemMessage part of the chat history.
-> The new query is appended to the chat history as a HumanMessage schema to the chat history
-> The completed chat history is then passed onto the chat model for a response
-> Response is returned / printed; and the chat interaction (new HumanMessage + AIMesage) is embedded and saved into the Chorma database.


Testing:
-> Asking questions like "Which hotel did I ask the review for in Tokyo?"; this information will not be available to GPT, but only available as context in the chat history / ChromaDB.


# Telebot Agent:
Telebot Agent is a simple GPT-4 wrapper that uses Telegram bot API and OpenAI API / Langchain to answer any questions from the user.
It builds on top of persistent agent, and eventually also will have support as its own project with a VPS / uptime to keep the bot running 24/7.

Basic feature is this:
- User can question / query to the agent via Telegram messages, these conversation history is saved in a persistent chroma db and is used as persistent context.

The tech stack is pretty much the persistent agent as above + telegram / telebot API to support telegram based messaging and organize preferences, API keys per channel during set up.
Then it is also kept online using a VPS.
This is a useful project that will accelerate my learning in general, and straight forward enough.
Maximizing fun building it, use AI as much as possible in the process to unblock - just ask for it to get the building blocks and get on building!
Ask any questions, its very liberating.


