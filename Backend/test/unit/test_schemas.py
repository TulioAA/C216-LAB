from app.schemas.item import ItemCreate, ItemUpdate

def test_item_create_schema():
    item = ItemCreate(name="Teste", description="Desc")
    assert item.name == "Teste"
    assert item.description == "Desc"

def test_item_update_schema():
    item = ItemUpdate(description="Atualizado")
    assert item.description == "Atualizado"
    assert item.name is None
