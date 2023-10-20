## PP1: Learning GPT
Learning GPT is a continuous project that will assist me with various learning features that leverage LLMs. Eventually, it may inform a full fledged product with a subscription model off of it as well (that can arbitrage some tokens).

FEATURES;
Given a full directory of texts and PDFs... it can:
- Create an overview and summary of the contents of the directory
- Give its real world / common use cases along with examples

- Develop a learning path from basics to mastery
- Develop a milestone based project to practice and build mastery
- Develop quizzes to test your knowledge
-- Spaced recognition and testing
-- Tracking your progress and mastery towards mastery
- Telegram integration to ping notifications on a timely basis to test.

- Support for updating libraries as they get updated;
-- This is not a ugent feature, as libraries don't get updated THAT often or have that big of changes in a short timespan.
-- And therefore, this can be done manually to until this is developed.
-- The approach to doing this eventually will be using submodules in Git and updating it and updating the embeddigns as well.

### Development Roadmap:
- Summarize the directory and the important lessons covered and key concepts
- Turn them into multiple choice questions
- Integrate into Telegram and test the user on it
- Track progress and incorrect questions (similar to Eidetic does)

Every time quiz() is called, it should populate with everything that the user needs to be reminded of.
Every time they get it wrong;
Topic mastery;


### Architecture and technologies:
- Lanchain
- OpenAI API

|--/main.py/ --> main script
|--/documentations/ --> houses the documentations as well as the learning directories for corresponding documentations.

When users deposit a directory within documentation, for example there is /thefuzz/ library in the /learnGPT/documentations/ folder. When the script is run to target this documentation for learning, it will create a /learn-thefuzz/ directory within the documentations library that houses various things such as...
- chroma_db --> persistent vectorstores for given library
- conversation_log.md --> houses all conversations
- overview.md --> overview + exampels and basic usage
- learning_paths.md --> learning_paths.md

For each topic / milestone there shoudl be a sub directory:
-- notes.md
-- test_questions.md
-- practice_project.md

- learning_progress.pickle --> eventually, will track the progress of my learning, spaced repetition, scores and track what it is that I need to review until mastery.



##### TODOs:
1. Initializing /documents/learn-module/ with the relevant folders
2. Creating and storing the relevant vectorstores within a given directory
2.a. This also includes being able to chop large libraries and execute against them part by part to embed them and add them to the vectorstore individually.

3. Loading the correct vectostore-collection when there is a user query
4. Returning / printing the user query and then storing the conversation history in a persistent db so that it can be used as context in the future.




