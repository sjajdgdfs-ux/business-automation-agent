from pydantic import BaseModel
class DataSummary(BaseModel):
    rows: int
    columns: int
    column_names: list[str]
    sample: str
    data_type: str
class AgentState(BaseModel):
    raw_data: str = ''
    filename: str = ''
    summary: DataSummary | None = None
    analysis: str = ''
    advice: str = ''
    final_report: str = ''
    status: str = 'started'
