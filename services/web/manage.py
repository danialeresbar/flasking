from flask.cli import FlaskGroup

from project import app, database, User

cli = FlaskGroup(app)


@cli.command('create_database')
def create_database():
    database.drop_all()
    database.create_all()
    database.session.commit()


@cli.command('seed_database')
def seed_database():
    database.session.add(User(email="admin@admin.org"))
    database.session.commit()


if __name__ == "__main__":
    cli()
