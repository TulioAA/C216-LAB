import { test, expect } from "@playwright/test";

test("cadastrar maquina", async ({ page }) => {
  await page.goto("http://localhost:5173/");

  await page.fill('input[placeholder="Nome"]', "Trator Playwright");

  await page.fill(
    'input[placeholder="Marca"]',
    "John Deere"
  );

  await page.fill(
    'input[placeholder="Modelo"]',
    "6110J"
  );

  await page.fill(
    'input[placeholder="Ano"]',
    "2024"
  );

  await page.fill(
    'input[placeholder="Horas Trabalhadas"]',
    "100"
  );

  await page.fill(
    'input[placeholder="Próxima Manutenção"]',
    "500"
  );

  await page.click(
    'button[type="submit"]'
  );

  await expect(
    page.getByText(
      "Trator Playwright"
    )
  ).toBeVisible();
});