"""empty message

Revision ID: fcd652eab590
Revises: 
Create Date: 2019-10-17 02:32:46.580398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcd652eab590'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teams',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.Column('prize_pool', sa.Numeric(), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('won_team_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['won_team_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('playoff_matches',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Enum('standby', 'live', 'over', name='playoffmatchstatus'), nullable=True),
    sa.Column('type', sa.Enum('quarter_final', 'semi_final', 'final', name='playoffmatchtype'), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('team1_id', sa.Integer(), nullable=False),
    sa.Column('team1_score', sa.Integer(), nullable=True),
    sa.Column('team2_id', sa.Integer(), nullable=False),
    sa.Column('team2_score', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['team1_id'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['team2_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group_matches',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Enum('standby', 'live', 'over', name='groupmatchstatus'), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('team1_id', sa.Integer(), nullable=False),
    sa.Column('team1_score', sa.Integer(), nullable=True),
    sa.Column('team2_id', sa.Integer(), nullable=False),
    sa.Column('team2_score', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['team1_id'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['team2_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group_teams',
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('group_id', 'team_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group_teams')
    op.drop_table('group_matches')
    op.drop_table('playoff_matches')
    op.drop_table('groups')
    op.drop_table('events')
    op.drop_table('teams')
    # ### end Alembic commands ###
