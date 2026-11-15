"""initial"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "a0575ed64f79"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        "maquinas",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nome_maquina", sa.String(), nullable=False),
        sa.Column("marca", sa.String(), nullable=False),
        sa.Column("modelo", sa.String(), nullable=False),
        sa.Column("ano", sa.Integer()),
        sa.Column("horas_trabalhadas", sa.Integer()),
        sa.Column("horas_proxima_manutencao", sa.Integer()),
    )

    op.create_table(
        "manutencoes",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "maquina_id",
            sa.Integer(),
            sa.ForeignKey("maquinas.id"),
            nullable=False,
        ),
        sa.Column(
            "tipo_manutencao",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "descricao",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "data_manutencao",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "custo",
            sa.Integer(),
            nullable=False,
        ),
    )


def downgrade() -> None:

    op.drop_table("manutencoes")
    op.drop_table("maquinas")