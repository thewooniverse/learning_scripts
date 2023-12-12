# Persistent Agent
Persistent Agent is simply a GPT-4 wrapper that has persistent memory storage.

Procedure:
-> Agent is asked a new query
-> Chroma Database (containing embedded chatlogs) is searched using a retrieval / search algorithm to get relevant documents - using MMR
-> The retrieved documents are then summarized as context in the form of a template as a SystemMessage part of the chat history.
-> The new query is appended to the chat history as a HumanMessage schema to the chat history
-> The completed chat history is then passed onto the chat model for a response
-> Response is returned / printed; and the chat interaction (new HumanMessage + AIMesage) is embedded and saved into the Chorma database.



Testing:
-> Asking questions like "Which hotel did I ask the review for in Tokyo?"; this information will not be available to GPT, but only available as context in the chat history / ChromaDB.


