# Super-AI

Python orchestrator for running multiple OpenAI agents. The `superMFI`
function triggers PCB design, circuit simulation, error analysis and diagram
generation steps.

## Setup

Install dependencies and run the orchestrator:

```bash
pip install -r requirements.txt
python orchestrator.py
```

## Testing

To try the orchestrator locally you need an OpenAI API key. After installing the requirements, export your key and run the script:

```bash
export OPENAI_API_KEY=<your-key>
python orchestrator.py
```

The built-in example triggers the `superMFI` workflow and prints each step's output to the console. There are currently no automated tests, but running `pytest` verifies the environment is set up correctly.


## Browser automation example

`selenium_chatgpt.py` demonstrates how to send a prompt to the ChatGPT web
interface using Selenium. Install the extra dependency and run the script with a
message:

```bash
pip install -r requirements.txt
python selenium_chatgpt.py "Hello"
```

The script opens a browser window and waits for you to log in to ChatGPT if
necessary, then prints the assistant's response to the console.
