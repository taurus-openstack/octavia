# Copyright (c) 2018 China Telecom Corporation
# All Rights Reserved.
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

"""amphora add flavor id

Revision ID: 4f65b4f91c39
Revises: 80dba23a159f
Create Date: 2018-07-16 09:59:07.169894

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4f65b4f91c39'
down_revision = '80dba23a159f'


def upgrade():
    op.add_column(
        'amphora',
        sa.Column('compute_flavor', sa.String(255), nullable=True)
    )
