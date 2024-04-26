import typer
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()

app.command(short_help = 'Edit an existing appointment')
def edit(position: int):
    typer.echo(f"editing {position}")

if __name__ == "__main__":
    app()