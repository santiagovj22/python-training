"""
Add user's table
"""
name = "01_upgrade_users"
dependencies = ["00_initial"]


def upgrade(db):
    db.create_collection('users')

def downgrade(db):
    pass
