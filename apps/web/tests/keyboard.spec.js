import { expect, test } from "@playwright/test";

test("selecting a suggestion updates text and clears suggestions before history learning finishes", async ({
  page,
}) => {
  let releaseHistory;
  let resolveHistoryStarted;
  let historyPayload;
  const historyMayFinish = new Promise((resolve) => {
    releaseHistory = resolve;
  });
  const historyStarted = new Promise((resolve) => {
    resolveHistoryStarted = resolve;
  });

  await page.route("http://127.0.0.1:8000/predict/**", async (route) => {
    await route.fulfill({
      json: {
        suggestions: [
          { word: "jẹun", score: 0.98 },
          { word: "lọ", score: 0.72 },
        ],
      },
    });
  });

  await page.route("http://127.0.0.1:8000/history/", async (route) => {
    historyPayload = route.request().postDataJSON();
    resolveHistoryStarted();
    await historyMayFinish;
    await route.fulfill({ json: { ok: true } });
  });

  await page.goto("/");

  const input = page.getByLabel("Yorùbá predictive keyboard input");
  await input.fill("ọmọ náà fẹ́ ");

  const suggestion = page.getByRole("option", { name: /jẹun/ });
  await expect(suggestion).toBeVisible();

  await suggestion.click();
  await historyStarted;

  await expect(input).toHaveValue("ọmọ náà fẹ́ jẹun ");
  await expect(suggestion).toBeHidden();
  expect(historyPayload).toEqual({
    previous: "fẹ́",
    selected: "jẹun",
  });

  releaseHistory();
});
