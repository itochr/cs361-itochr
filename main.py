import typer
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()

@app.command(short_help = 'Add new appointment')
def add(appt: str, category: str):
   typer.echo(f"adding {appt}, {category}")


if __name__ == "__main__":
    app()
