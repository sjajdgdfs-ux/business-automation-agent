from src.core.llm import generate
from src.core.schemas import AgentState
SYSTEM = '''You are a strategic business consultant.
Turn data analysis into clear, actionable recommendations.
Focus on ROI and practical implementation.'''
def run(state: AgentState) -> AgentState:
    prompt = f'''
Based on this data analysis, provide strategic recommendations:

Analysis:
{state.analysis}

Provide:
1. Top 3 Immediate Actions (do this week)
2. Medium-term Strategy (next month)
3. KPIs to Track
4. Expected Outcomes & ROI
5. Risks to Watch
'''
    state.advice = generate(prompt, system=SYSTEM)
    return state
