import { expect, test } from "@playwright/test";

test("mantem item apos recarregar pagina", async ({
  page,
}) => {
  const nome = `Notebook-${Date.now()}`;

  await page.goto("/");

  await page.getByLabel("Nome").fill(nome);

  await page
    .getByLabel("Descrição")
    .fill("14 polegadas");

  await page
    .getByRole("button", {
      name: "Adicionar",
    })
    .click();

  await expect(
    page.getByRole("heading", {
      name: nome,
    }),
  ).toBeVisible();

  await page.reload();

  await expect(
    page.getByRole("heading", {
      name: nome,
    }),
  ).toBeVisible();
});