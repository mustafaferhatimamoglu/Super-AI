# Super-AI

Python orchestrator for running multiple OpenAI agents. The `superMFI`
function triggers PCB design, circuit simulation, error analysis and diagram
generation steps.

## Setup

Install dependencies and run the orchestrator:

```bash
pip install openai
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
