from rich.console import Console
import typer

console = Console()

app=typer.Typer()

@app.command()
def toolbox():
    typer.echo(console.print("Welcome to [bold magenta]Toolbox![/bold magenta]",style="red"))

if __name__=="__main__":
    app()
