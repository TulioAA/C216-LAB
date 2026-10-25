import { describe, expect, it } from "vitest";
import { validateItem } from "../../src/validation";

describe("validateItem", () => {
  it("rejeita nome vazio", () => {
    const { errors } = validateItem({
      name: "",
      description: "",
    });

    expect(errors.name).toBeDefined();
  });

  it("aceita nome válido", () => {
    const { errors } = validateItem({
      name: "Notebook",
      description: "",
    });

    expect(errors.name).toBeUndefined();
  });
});