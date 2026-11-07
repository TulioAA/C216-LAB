import { useEffect, useState } from "react";

import { ItemForm } from "./components/ItemForm";
import { ItemList } from "./components/ItemList";
import {
  createItem,
  listItems,
} from "./services/items";

export default function App() {
  const [items, setItems] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  useEffect(() => {
    async function loadItems() {
      try {
        const data = await listItems();

        setItems(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    loadItems();
  }, []);

  async function addItem(values) {
    try {
      setError("");

      const newItem = await createItem(values);

      setItems((current) => [
        ...current,
        newItem,
      ]);
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <main className="mx-auto max-w-xl p-6">
      <h1 className="mb-6 text-3xl font-bold">
        Gerenciador de Itens
      </h1>

      {error && (
        <div className="mb-4 rounded border border-red-300 bg-red-50 p-3 text-red-700">
          {error}
        </div>
      )}

      <ItemForm onAdd={addItem} />

      <section className="mt-6">
        <h2 className="mb-3 text-xl font-semibold">
          Itens cadastrados
        </h2>

        {loading ? (
          <p>Carregando...</p>
        ) : (
          <ItemList items={items} />
        )}
      </section>
    </main>
  );
}