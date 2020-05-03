"""Add indexes needed for revsolver

Revision ID: a7442899ef28
Revises: ecb0ca258835
Create Date: 2020-04-21 19:19:43.848258+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7442899ef28'
down_revision = 'ecb0ca258835'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('depends_on_entity_id_idx', 'depends_on', ['entity_id'], unique=False)
    op.create_index('python_package_version_environment_idx', 'python_package_version', ['os_name', 'os_version', 'python_version'], unique=False)
    op.create_index('python_package_version_entity_package_name_idx', 'python_package_version_entity', ['package_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('python_package_version_entity_package_name_idx', table_name='python_package_version_entity')
    op.drop_index('python_package_version_environment_idx', table_name='python_package_version')
    op.drop_index('depends_on_entity_id_idx', table_name='depends_on')
    # ### end Alembic commands ###