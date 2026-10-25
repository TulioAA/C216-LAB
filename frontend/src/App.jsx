import { useState } from "react";

import { ItemForm } from "./components/ItemForm";
import { ItemList } from "./components/ItemList";

export default function App() {
  const [items, setItems] = useState([]);

  function addItem({ name, description }) {
    setItems((current) => [
      ...current,
      {
        id: crypto.randomUUID(),
        name,
        description,
      },
    ]);
  }

  return (
    <main className="mx-auto max-w-xl p-6">
      <h1 className="mb-6 text-3xl font-bold">
        Gerenciador de Itens
      </h1>

      <ItemForm onAdd={addItem} />

      <section className="mt-6">
        <h2 className="mb-3 text-xl font-semibold">
          Itens cadastrados
        </h2>

        <ItemList items={items} />
      </section>
    </main>
  );
}