import { useState } from "react";
import { validateItem } from "../validation";

export function ItemForm({ onAdd }) {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [errors, setErrors] = useState({});

  function handleSubmit(event) {
    event.preventDefault();

    const result = validateItem({
      name,
      description,
    });

    setErrors(result.errors);

    if (Object.keys(result.errors).length > 0) {
      return;
    }

    onAdd(result.values);

    setName("");
    setDescription("");
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="space-y-4 rounded-lg border border-slate-200 bg-white p-4 shadow-sm"
    >
      <div>
        <label
          htmlFor="name"
          className="mb-1 block text-sm font-medium"
        >
          Nome
        </label>

        <input
          id="name"
          value={name}
          onChange={(event) =>
            setName(event.target.value)
          }
          placeholder="Ex.: Notebook"
          className="w-full rounded border border-slate-300 p-2"
        />

        {errors.name && (
          <p className="mt-1 text-sm text-red-600">
            {errors.name}
          </p>
        )}
      </div>

      <div>
        <label
          htmlFor="description"
          className="mb-1 block text-sm font-medium"
        >
          Descrição
        </label>

        <textarea
          id="description"
          value={description}
          onChange={(event) =>
            setDescription(event.target.value)
          }
          placeholder="Opcional"
          rows="4"
          className="w-full rounded border border-slate-300 p-2"
        />
      </div>

      <button
        type="submit"
        className="rounded bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700"
      >
        Adicionar
      </button>
    </form>
  );
}