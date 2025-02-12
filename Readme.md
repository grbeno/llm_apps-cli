## 🌱 LLM based AI-chat/assistants testing with Langchain on CLI

:point_right: __Requirements: Python, and any API keys and functions you want; I am currently using only the openai_api_key.__

#### Set up a virtual environment in the selected project directory
*You can use Pipenv; the Pipfile is attached in the repository.
```
python -m venv .venv
```
##### On Windows
```
.venv/Scripts/activate
```
##### On Linux or Mac
```
source venv/bin/activate
```
#### Install dependencies
```
pip install -r requirements.txt
```
#### Install langapp
```
pip install .
```
---
Default model `gpt-4o-mini` from OpenAI.
```
langapp
```
You can select other models: `llama3.1` from Ollama.
```
langapp --m llama3.1
```
You can select chat role as well. Default is: `short and concise`
```
langapp --r "correct english"
```
Other roles: `correct german` `upgrade english`, `remaster the conversation` `translate to english/german/hungarian` or extend with what you need in `prompts.py` and `helpers.py`.

End conversation: `empty prompt / press Enter`

---

#### Ollama
Download and install from [Ollama's website](https://ollama.com/download) to use it locally.

_pull a model_
```
ollama pull <model_name>
```
_test a model_
```
ollama run <model_name>
```

---

#### Environment variables
```
#.env

OPENAI_API_KEY
```

---
#### Using scripts

`shell_scripts/runapp.bat` on Windows

`shell_scripts/runapp.sh` on Linux

##### Don't forget to add your project path to the script files!

---
:point_right: More in [.app_info](https://github.com/grbeno/langchain-cmd/blob/main/.app_info)
