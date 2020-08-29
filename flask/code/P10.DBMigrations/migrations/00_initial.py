"""
Initial migration
"""
name = "00_initial"
dependencies = []


def upgrade(db):
    db.create_collection('games')
    db.command('createUser', 'flask2', pwd="pwd", roles=[{'role': 'readWrite', 'db': 'traveler'}])

def downgrade(db):
    pass
