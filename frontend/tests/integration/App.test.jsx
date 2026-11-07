import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";

import App from "../../src/App";

describe("App", () => {
  beforeEach(() => {
    global.fetch = vi.fn();
  });

  it("carrega itens da API", async () => {
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => [
        {
          id: 1,
          name: "Notebook",
          description: "14 polegadas",
        },
      ],
    });

    render(<App />);

    expect(
      screen.getByText("Carregando...")
    ).toBeInTheDocument();

    await waitFor(() => {
      expect(
        screen.getByText("Notebook")
      ).toBeInTheDocument();
    });
  });

  it("cadastra um item e exibe na lista", async () => {
    fetch
      .mockResolvedValueOnce({
        ok: true,
        json: async () => [],
      })
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          id: 1,
          name: "Notebook",
          description: "14 polegadas",
        }),
      });

    const user = userEvent.setup();

    render(<App />);

    await user.type(
      screen.getByLabelText("Nome"),
      "Notebook"
    );

    await user.type(
      screen.getByLabelText("Descrição"),
      "14 polegadas"
    );

    await user.click(
      screen.getByRole("button", {
        name: "Adicionar",
      })
    );

    await waitFor(() => {
      expect(
        screen.getByText("Notebook")
      ).toBeInTheDocument();
    });
  });

  it("mostra mensagem de erro", async () => {
    fetch.mockRejectedValueOnce(
      new Error("Erro ao carregar itens")
    );

    render(<App />);

    await waitFor(() => {
      expect(
        screen.getByText("Erro ao carregar itens")
      ).toBeInTheDocument();
    });
  });
});