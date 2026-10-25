import { expect, test } from "@playwright/test";

test("adiciona item na lista", async ({
  page,
}) => {
  await page.goto("/");

  await page.getByLabel("Nome").fill(
    "Notebook",
  );

  await page
    .getByLabel("Descrição")
    .fill("14 polegadas");

  await page
    .getByRole("button", {
      name: "Adicionar",
    })
    .click();

  await expect(
    page.getByText("Notebook"),
  ).toBeVisible();

  await expect(
    page.getByText("14 polegadas"),
  ).toBeVisible();
});