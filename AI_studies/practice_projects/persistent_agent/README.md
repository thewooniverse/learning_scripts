# Persistent Agent
Persistent Agent is simply a GPT-4 wrapper that has persistent memory storage.

Procedure:
-> Saves all new chat interactions (new query + resposne) in the ChromaDB
-> When a new query is made, the Chroma database is searched using a retrieval / search algorithm - likely it will be MMR
-> The retrieved documents will be summarized to a few key points of the conversation history, and passed as chat history
-> Step 1 is executed again to store the chat interaction in the ChromaDB



Testing:
-> Asking questions like "Which hotel did I ask the review for in Tokyo?"

