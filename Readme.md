## 🌱 LLM based AI-chat testing with Langchain on CLI

:point_right: __Requirements: Python, and any API keys and functions you want; I am currently using openai_api_key, langchain_api_key and huggingface_api_key.__
#### Ollama
Download and install from Ollama's website to use it locally.

_pull a model_
```
ollama pull <model_name>
```
_test a model_
```
ollama run <model_name>
```
#### Set up a virtual environment in the selected project directory
#### *You can use Pipenv; the Pipfile is attached in the repository.
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
---
Default model `gpt-4o-mini` from OpenAI.
```
python chat.py
```
You can select other models: `llama3.1` from Ollama.
```
python chat.py --m llama3.1
```
You can select chat role as well. Default is: `short and concise`
```
python chat.py --r "correct english"
```
Other roles: `correct german` `translate to english` / german / spanish / french / hungarian

End conversation: `add empty row <- push enter`

---
```
#.env

OPENAI_API_KEY
```

---
#### Using scripts

`shell_scripts/runapp.bat` on Windows

`shell_scripts/runapp.sh` on Linux

##### Don't forget to add your path to the script files!

---
:point_right: More in .app_info
