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
        # subprocess.run(["./test.sh"])
    elif(selected_option == '2'):
        # system('clear')
        qol()
        selected_option_qol = typer.prompt("Select a option from menu")
        if(selected_option_qol == '1'):
            subprocess.run(["./install_neofetch.sh"])
            typer.echo(f"Now you can run 'neofetch'")
        elif(selected_option_qol == '2'):
            subprocess.run(["./install_starship.sh"])
            typer.echo(f"Now you can run restart terminal")
        elif(selected_option_qol == '3'):
            subprocess.run(["./install_bat.sh"])
            typer.echo(f"Now you can run 'bat'")
        elif(selected_option_qol == '4'):
            subprocess.run(["./install_htop.sh"])
            typer.echo(f"Now you can run 'htop'")
    elif(selected_option == '3'):
        typer.echo(f"run ./search.sh")
    elif(selected_option == '4'):
        typer.echo(f"run ./cht.sh 'search term'")
    elif(selected_option == '5'):
        certification_list()


def qol():
    typer.echo(f"1: neofetch")
    typer.echo(f"2: starship")
    typer.echo(f"3: bat")
    typer.echo(f"4: htop")


def menu():
    typer.echo(f"1> Kali Top 10 Tools")
    typer.echo(f"2> Qualtity of Life Tools")
    typer.echo(f"3> Googler")
    typer.echo(f"4> CheatSheet")
    typer.echo(f"5> Certifications")


def kali_tools():
    with open('kali-tools-top10.txt', 'r') as f:
        print(f.read())


def certification_list():
    with open('certification_list.txt', 'r') as f:
        print(f.read())


if __name__ == "__main__":
    app()
