#    Copyright 2017 Walmart Stores Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""add flavor and flavor_profile table

Revision ID: b9c703669314
Revises: 4f65b4f91c39
Create Date: 2018-01-02 16:05:29.745457

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b9c703669314'
down_revision = '4f65b4f91c39'


def upgrade():

    op.create_table(
        'flavor_profile',
        sa.Column('id', sa.String(36), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('provider_name', sa.String(255), nullable=False),
        sa.Column('flavor_data', sa.String(4096), nullable=False),
        sa.PrimaryKeyConstraint('id'))

    op.create_table(
        'flavor',
        sa.Column('id', sa.String(36), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.String(255), nullable=True),
        sa.Column('enabled', sa.Boolean(), nullable=False),
        sa.Column('flavor_profile_id', sa.String(36), nullable=False),
        sa.ForeignKeyConstraint(['flavor_profile_id'],
                                ['flavor_profile.id'],
                                name='fk_flavor_flavor_profile_id'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name',
                            name='uq_flavor_name'),)
