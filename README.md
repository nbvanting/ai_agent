## Getting Started

This repository is based on the Boot.dev AI agent course, which can be found at: https://www.boot.dev/courses/build-ai-agent-python


1. **Clone the repository:**
    ```bash
    git clone https://github.com/nbvanting/ai_agent.git
    cd ai_agent
    ```

2. **Set up the project environment using `uv` and the existing `uv.lock` file:**
    ```bash
    uv venv
    uv sync
    ```

    This will create a virtual environment and install all dependencies specified in `uv.lock`.

3. **Add or update dependencies as needed:**
    ```bash
    uv add <dependency1> <dependency2> ...
    ```

    After adding dependencies, `uv.lock` will be updated automatically.

4. **Run the agent:**
    ```bash
    uv run python main.py "<your prompt here>"
    ```
