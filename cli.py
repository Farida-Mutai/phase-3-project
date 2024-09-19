import click
from sqlalchemy.orm import Session
from database import SessionLocal
from helper import create_user, get_user, update_user, delete_user
from main import User

@click.group()
def cli():
    """Expense Tracker CLI"""
    pass

@click.command()
@click.option('--name', prompt='Your name', help='The person logging in.')
def login(name: str):
    with SessionLocal() as session:
        user = session.query(User).filter(User.name == name).first()
        if not user:
            click.echo(f"User {name} not found, creating a new account.")
            user = create_user(session, name=name, email=f'{name.lower()}@example.com')
        click.echo(f"Welcome, {user.name}! Let's check how you spend.")

@click.command()
@click.argument('user_id', type=int)
def view_user(user_id: int):
    with SessionLocal() as session:
        user = get_user(session, user_id)
        if user:
            click.echo(f"User ID: {user.id}, Name: {user.name}, Email: {user.email}")
        else:
            click.echo("User not found.")

@click.command()
@click.argument('user_id', type=int)
@click.option('--name', help='New name for the user.')
@click.option('--email', help='New email for the user.')
def update_user(user_id: int, name: str, email: str):
    with SessionLocal() as session:
        user = update_user(session, user_id, name, email)
        if user:
            click.echo(f"Updated User: ID: {user.id}, Name: {user.name}, Email: {user.email}")
        else:
            click.echo("User not found.")

@click.command()
@click.argument('user_id', type=int)
def delete_user(user_id: int):
    with SessionLocal() as session:
        user = delete_user(session, user_id)
        if user:
            click.echo(f"Deleted User: ID: {user.id}, Name: {user.name}")
        else:
            click.echo("User not found.")

cli.add_command(login)
cli.add_command(view_user)
cli.add_command(update_user)
cli.add_command(delete_user)

if __name__ == '__main__':
    cli()
