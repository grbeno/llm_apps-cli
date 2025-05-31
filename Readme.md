## 🌱 LLM based AI-chat/assistants testing with Langchain on CLI

:point_right: __Requirements: Python, and any API keys and functions you want; I am currently using only the openai_api_key.__

#### :small_blue_diamond: Create and activate a virtual environment in the preferred project directory
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
#### :small_blue_diamond: Install dependencies
```
pip install -r requirements.txt
```
#### Install/build langapp
```
pip install .
```
---
#### :small_blue_diamond: How to use
Default model `gpt-4o-mini` from OpenAI.
```
langapp
```
You can select other models, such as `llama3.1` or `deepseek-r1` from Ollama after installing and setting it up.
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

#### :small_blue_diamond: Ollama
Download and install from [Ollama's website](https://ollama.com/download) to use it locally.

_test a model_
```
ollama run <model_name>:<param>b
```
In the case of using an open-source model from Ollama, you need to run the command before the LangChain's `OllamaLLM` instance handles it.

---

#### :small_blue_diamond: Environment variables
```
#.env

OPENAI_API_KEY
```

---
#### :small_blue_diamond: Using scripts

`shell_scripts/runapp.bat` on Windows

`shell_scripts/runapp.sh` on Linux

##### Don't forget to add your project path to the script files!

---
:point_right: More in [.app_info](https://github.com/grbeno/langchain-cmd/blob/main/.app_info)
