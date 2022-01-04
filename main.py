from os import read, system
from rich.console import Console
import typer
import subprocess

console = Console()

app = typer.Typer()


@app.command()
def toolbox():
    typer.echo(console.print(
        "Welcome to [bold magenta]Toolbox![/bold magenta]", style="red"))
    menu()
    selected_option = typer.prompt("Select a option from menu")
    if (selected_option == '1'):
        # system('clear')
        kali_tools()
        # subprocess.run(["/path/to/your/shell/script", "arguments"], shell=True)
        subprocess.run(["./test.sh"])

    elif(selected_option == '2'):
        # system('clear')
        qol()
        selected_option_qol = typer.prompt("Select a option from menu")
        if(selected_option_qol == '1'):
            subprocess.run(["./install_neofetch.sh"])
            typer.echo(f"Now you can run 'neofetch'")
        if(selected_option_qol == '2'):
            subprocess.run(["./install_starship.sh"])
            typer.echo(f"Now you can run 'neofetch'")


def qol():
    typer.echo(f"1: neofetch")
    typer.echo(f"2: starship")


def menu():
    typer.echo(f"1> Kali Top 10 Tools")
    typer.echo(f"2> Qualtity of Life Tools")


def kali_tools():
    with open('kali-tools.txt', 'r') as f:
        print(f.read())


if __name__ == "__main__":
    app()
