from playwright.async_api import async_playwright
import asyncio
async def main():
 async with async_playwright() as p:
   browser = await p.chromium.launch(headless=False)
   page = await browser.new_page()
   await page.goto('https://amazon.com')
   await page.wait_for_timeout(1000)
   await browser.close()
