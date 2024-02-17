import typer

app = typer.Typer()

# Define a main command that acts based on arguments
@app.command()
def main(command: str = typer.Argument("hello")):
    """
    Main command that decides which function to call.
    """
    if command == "hello":
        hello()
    elif command == "goodbye":
        goodbye()
    else:
        typer.echo(f"Command {command} not recognized.")

def hello():
    """
    Prints 'Hello World'.
    """
    typer.echo("Hello World")

def goodbye():
    """
    Prints 'Goodbye World'.
    """
    typer.echo("Goodbye World")

if __name__ == "__main__":
    app()
