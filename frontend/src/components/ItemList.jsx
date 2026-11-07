export function ItemList({ items }) {
  if (items.length === 0) {
    return (
      <p className="text-slate-500">
        Nenhum item cadastrado.
      </p>
    );
  }

  return (
    <ul className="space-y-3">
      {items.map((item) => (
        <li
          key={item.id}
          className="rounded border border-slate-200 p-4"
        >
          <h3 className="font-semibold">
            {item.name}
          </h3>

          {item.description && (
            <p className="mt-1 text-slate-600">
              {item.description}
            </p>
          )}
        </li>
      ))}
    </ul>
  );
}