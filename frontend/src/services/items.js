const API_URL = "http://localhost:8000/items/";

export async function listItems() {
  const response = await fetch(API_URL);

  if (!response.ok) {
    throw new Error("Erro ao carregar itens");
  }

  return response.json();
}

export async function createItem(item) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(item),
  });

  if (!response.ok) {
    const error = await response.json();

    throw new Error(
      error.detail || "Erro ao criar item",
    );
  }

  return response.json();
}