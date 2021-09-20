"""This file sets up a command line manager.

Use "python manage.py" for a list of available commands.
Use "python manage.py runserver" to start the development web server on localhost:5000.
Use "python manage.py runserver --help" for additional runserver options.
"""

from flask import Flask
from flask.cli import FlaskGroup

import click

from app import create_app

from app.commands import pcalc


@click.group(cls=FlaskGroup, create_app=create_app)
@click.pass_context
def cli(ctx):
    """Management script for the application."""
    if ctx.parent:
        click.echo(ctx.parent.get_help())


@cli.command(help='Reverse Polish notation Calculator')
def run_calc():
    pcalc.main()


if __name__ == "__main__":
    cli()
