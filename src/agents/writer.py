from src.core.llm import generate
from src.core.schemas import AgentState
SYSTEM = '''You are a professional business report writer.
Write clear, executive-level reports in markdown format.'''
def run(state: AgentState) -> AgentState:
    prompt = f'''
Write a complete business intelligence report:

File: {state.filename}
Data Info: {state.summary.rows} rows, {state.summary.columns} columns

Analysis:
{state.analysis}

Recommendations:
{state.advice}

Write this report:
# Business Intelligence Report: {state.filename}

## Executive Summary
(3-4 sentences: what the data shows and the most important finding)

## Data Overview
(what data was analyzed)

## Key Findings
(5-7 bullet points with specific numbers)

## Detailed Analysis
### Performance Overview
### Trends & Patterns
### Areas of Concern

## Strategic Recommendations
### Immediate Actions (This Week)
### Medium-Term Strategy (Next Month)

## KPIs to Track
(table with KPI, Current, Target, Timeline)

## Conclusion
(2-3 sentences)
'''
    state.final_report = generate(prompt, system=SYSTEM)
    return state
