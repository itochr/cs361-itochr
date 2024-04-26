import typer
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()

@app.command(short_help = 'view existing appointments')
def read(appt: str, category: str):
   typer.echo(f"reading {appt}, {category}")


if __name__ == "__main__":
    app()
