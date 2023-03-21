# Step 0: Protect OpenAI API Key

Follow instructions in this [link](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5)

# Step 1: Preparing index.json

- Run `python build_index.py`
- Notes:
    - `data` folder contains all data files
    - better to set `working_directory`


# Step 2: Chatbot

- Run `python chatbot_GUI.py`
- Notes:
    - set `path_to_index_json` in `chat.py`
    - set `bot_name`