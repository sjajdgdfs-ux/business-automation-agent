import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from src.core.schemas import AgentState
from src.agents import reader, analyst, advisor, writer
console = Console()
def run(filename: str, content: bytes) -> AgentState:
    state = AgentState(filename=filename)
    total_start = time.time()
    console.print(Panel('📂 [bold cyan]Reader Agent[/bold cyan] — Reading file...'))
    t = time.time()
    state = reader.run(state, content=content)
    console.print(f'[green]✅ File read[/green] ({time.time()-t:.1f}s) — {state.summary.rows} rows, {state.summary.columns} columns')
    console.print(Panel('📊 [bold cyan]Analyst Agent[/bold cyan] — Analyzing data...'))
    t = time.time()
    state = analyst.run(state)
    console.print(f'[green]✅ Analysis done[/green] ({time.time()-t:.1f}s)')
    console.print(Panel('💡 [bold cyan]Advisor Agent[/bold cyan] — Generating recommendations...'))
    t = time.time()
    state = advisor.run(state)
    console.print(f'[green]✅ Recommendations ready[/green] ({time.time()-t:.1f}s)')
    console.print(Panel('✍️  [bold cyan]Writer Agent[/bold cyan] — Writing report...'))
    t = time.time()
    state = writer.run(state)
    console.print(f'[green]✅ Report ready[/green] ({time.time()-t:.1f}s)')
    table = Table(title='Pipeline Summary')
    table.add_column('Agent', style='cyan')
    table.add_column('Status', style='green')
    table.add_row('📂 Reader',  '✅ Done')
    table.add_row('📊 Analyst', '✅ Done')
    table.add_row('💡 Advisor', '✅ Done')
    table.add_row('✍️  Writer',  '✅ Done')
    table.add_row('⏱️  Total',   f'{time.time()-total_start:.1f}s')
    console.print(table)
    state.status = 'completed'
    return state
