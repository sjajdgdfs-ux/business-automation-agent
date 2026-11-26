import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from src.orchestrator import run
from rich.console import Console
from rich.markdown import Markdown
console = Console()
def main():
    path = input('Enter file path (CSV/Excel/TXT): ').strip()
    if not os.path.exists(path):
        print('File not found')
        return
    with open(path, 'rb') as f:
        content = f.read()
    filename = os.path.basename(path)
    state = run(filename, content)
    console.print(Markdown(state.final_report))
    out = filename + '_report.md'
    with open(out, 'w', encoding='utf-8') as f:
        f.write(state.final_report)
    console.print(f'[green]Report saved to {out}[/green]')
if __name__ == '__main__':
    main()
