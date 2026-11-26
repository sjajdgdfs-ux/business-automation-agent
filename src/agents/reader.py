from src.core.tools import read_file
from src.core.schemas import DataSummary, AgentState
def run(state: AgentState, content: bytes = None) -> AgentState:
    raw, info = read_file(content=content, filename=state.filename)
    state.raw_data = raw
    if info:
        state.summary = DataSummary(
            rows=info.get('rows', 0),
            columns=info.get('columns', 0),
            column_names=info.get('column_names', []),
            sample=info.get('sample', raw[:500]),
            data_type=info.get('data_type', 'text')
        )
    else:
        state.summary = DataSummary(rows=0, columns=0, column_names=[], sample=raw[:500], data_type='text')
    return state
