"""
Update Index
"""
name = "02_upgrade_users_unique_email"
dependencies = ["01_upgrade_users"]


def upgrade(db):
    db.users.create_index([('email', 1)], unique=True)

def downgrade(db):
    pass
