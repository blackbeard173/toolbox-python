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
    if(selected_option == '1'):
        # system('clear')
        # subprocess.run(["/path/to/your/shell/script", "arguments"], shell=True)
        # subprocess.run(["./test.sh"])
        typer.echo(f"run ./search.sh [search term]")
    elif(selected_option == '2'):
        typer.echo(f"run ./cht.sh [search term]")
    elif(selected_option == '3'):
        typer.echo(
            f"run python keylogger.py; check logs.json for keystrokes saved")
    elif (selected_option == '4'):
        kali_tools()

    elif(selected_option == '2'):
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
    elif(selected_option == '5'):
        certification_list()


def qol():
    typer.echo(f"1: htop")
    typer.echo(f"2: neofetch")
    typer.echo(f"3: starship")
    typer.echo(f"4: bat")


def menu():
    typer.echo(f"1> Googler")
    typer.echo(f"2> CheatSheet")
    typer.echo(f"3> Keylogger")
    typer.echo(f"4> Kali Top 10 Tools")
    typer.echo(f"5> QoL Tools")
    typer.echo(f"6> Certifications")


def kali_tools():
    with open('kali-tools-top10.txt', 'r') as f:
        print(f.read())


def certification_list():
    with open('certification_list.txt', 'r') as f:
        print(f.read())


if __name__ == "__main__":
    app()
