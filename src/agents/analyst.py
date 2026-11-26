from src.core.llm import generate
from src.core.schemas import AgentState
SYSTEM = '''You are a senior business data analyst.
Analyze data thoroughly and extract meaningful business insights.
Always be specific with numbers and percentages.'''
def run(state: AgentState) -> AgentState:
    prompt = f'''
Analyze this business data and provide detailed insights:

File: {state.filename}
Rows: {state.summary.rows}
Columns: {state.summary.columns}
Column Names: {', '.join(state.summary.column_names)}

Data Sample:
{state.summary.sample}

Provide:
1. Data Overview (what kind of data is this?)
2. Key Patterns & Trends (with specific numbers)
3. Top Performers / Best Results
4. Problem Areas / Concerns
5. Anomalies or Outliers
'''
    state.analysis = generate(prompt, system=SYSTEM)
    return state
