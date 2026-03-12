# Setup and Usage Instructions

## Prerequisites
- Ensure you have [Python 3.8+](https://www.python.org/downloads/) installed.
- Install [Git](https://git-scm.com/downloads) for version control.
- Optional: [Node.js](https://nodejs.org/) for frontend integration.

## Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-org>/calculator.git
   cd calculator
   ```

2. **Create and Activate a Virtual Environment (Python)**
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Agents and Skills**
   - Review `agents/` and `skills/` directories for current configurations.
   - Update or add new agent and skill files as needed, following the provided templates.

5. **Run the Application**
   ```bash
   python app.py
   ```
   The calculator web app will be available at `http://localhost:8000`.

## Usage
- Access the calculator via the browser.
- Use the interface for basic and advanced calculations.
- Agents will automate calculation tasks and provide suggestions.

## Updating Agents and Skills
- Edit agent definitions in `agents/` to customize automation behaviors.
- Add new skills in `skills/` to extend calculation capabilities.
- Refer to the documentation in each directory for template instructions.

## Testing
- Run unit tests with:
   ```bash
   pytest tests/
   ```