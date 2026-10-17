from app.database.base import Base
from app.database.session import engine
from app.models.item import Item

print("Criando tabelas...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
