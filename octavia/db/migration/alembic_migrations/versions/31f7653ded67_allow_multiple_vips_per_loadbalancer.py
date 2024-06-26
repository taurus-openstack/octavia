#    Copyright 2019 Verizon Media
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

"""allow multiple vips per loadbalancer

Revision ID: 31f7653ded67
Revises: 6ac558d7fc21
Create Date: 2019-05-04 19:44:22.825499

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '31f7653ded67'
down_revision = '6ac558d7fc21'


def upgrade():
    op.create_table(
        'additional_vip',
        sa.Column('load_balancer_id', sa.String(36), nullable=False,
                  index=True),
        sa.Column('ip_address', sa.String(64), nullable=True),
        sa.Column('port_id', sa.String(36), nullable=True),
        sa.Column('subnet_id', sa.String(36), nullable=True),
        sa.Column('network_id', sa.String(36), nullable=True),
        sa.ForeignKeyConstraint(['load_balancer_id'], ['load_balancer.id'],
                                name='fk_add_vip_load_balancer_id'),
        sa.PrimaryKeyConstraint('load_balancer_id', 'subnet_id',
                                name='pk_add_vip_load_balancer_subnet'),
    )
