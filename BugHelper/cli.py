import click

from search import searchError

@click.command()
@click.option('--search', '-s', is_flag=True, help='Search for an error manually')
@click.option('--lasterror', '-l', is_flag=True, help='Search for last CLI Error')
@click.argument('name', default='world', required=False)
def main(name, search, lasterror):
    """Searches for command line errors and gives you the best answer from github"""
    if (search):
        click.echo(searchError())
    if (lasterror):
        click.echo("NOT YET WORKING")

