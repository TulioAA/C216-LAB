import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";

import { ItemForm } from "../../src/components/ItemForm";

describe("ItemForm", () => {
  it("chama onAdd ao enviar formulário válido", async () => {
    const onAdd = vi.fn();

    render(<ItemForm onAdd={onAdd} />);

    const user = userEvent.setup();

    await user.type(
      screen.getByLabelText("Nome"),
      "Notebook",
    );

    await user.click(
      screen.getByRole("button", {
        name: "Adicionar",
      }),
    );

    expect(onAdd).toHaveBeenCalled();
  });
});