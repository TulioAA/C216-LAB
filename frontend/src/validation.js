export function validateItem({ name, description }) {
  const errors = {};

  if (!name.trim()) {
    errors.name = "Nome obrigatório";
  }

  return {
    errors,
    values: {
      name: name.trim(),
      description: description.trim(),
    },
  };
}