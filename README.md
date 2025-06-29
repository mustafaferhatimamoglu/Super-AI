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

### Installing `pyautogui`

The examples rely on [`pyautogui`](https://pypi.org/project/pyautogui/). If the
system Python installation is managed and `pip install` fails, create a virtual
environment first:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pyautogui
```

Alternatively, pass `--break-system-packages` to `pip` if you understand the
risks.

## Keyboard and Mouse Automation

The `keyboard_mouse_automation.py` script shows a minimal example of
automatically controlling the mouse and keyboard using `pyautogui`.
After installing the dependency, run the script to see the automation in
action:

```bash
pip install pyautogui
python keyboard_mouse_automation.py
```

To quickly check for syntax errors in both automation scripts you can compile
them using Python's built-in bytecode compiler:

```bash
python -m py_compile super_ai_agent.py keyboard_mouse_automation.py
```

## Running the automatic prompt submitter

The `super_ai_agent.py` script looks for text files inside the `prompts/`
folder and submits each file's contents to the Sora interface. After a file is
processed it is moved to `prompts/processed/` so it won't be submitted again.

```bash
# ensure pyautogui is available
pip install pyautogui

# create the processed folder if it does not exist
mkdir -p prompts/processed

# run once and exit after all prompts are sent
python super_ai_agent.py

# watch for new prompts continuously
python super_ai_agent.py --loop
```

Pass `--help` for a full list of command line options.
