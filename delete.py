import typer
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()

app.command(short_help = 'Delete an existing appointment')
def delete(position: int):
    typer.echo(f"deleting {position}")

if __name__ == "__main__":
    app()