import typer

app = typer.Typer()


@app.command()
def say_hi(name):
    print("Hello ", name)


@app.command()
def say_bye(name):
    print("Bye ", name)


if __name__ == '__main__':
    app()
