# Copyright 2018 Huawei
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
#

"""Extend pool for support backend re-encryption

Revision ID: a1f689aecc1d
Revises: 1afc932f1ca2
Create Date: 2018-10-23 20:47:52.405865

"""


from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a1f689aecc1d'
down_revision = '1afc932f1ca2'


def upgrade():
    op.add_column('pool', sa.Column('tls_certificate_id', sa.String(255),
                                    nullable=True))
