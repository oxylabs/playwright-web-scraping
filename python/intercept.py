from playwright.async_api import async_playwright
import asyncio
import requests

async def handle_route(route) -> None:
    response = await route.fetch()
    body = await response.text()
    body = body.replace("<title>", "<title>Modified Response")
    await route.fulfill(
        response=response,
        body=body,
        headers={**response.headers, "content-type": "text/html"},
    )
 
async def main():
   async with async_playwright() as pw:
       browser = await pw.chromium.launch(
          proxy={
              'server': "http://pr.oxylabs.io:7777",
              "username": "USERNAME",
              "password": "PASSWORD"
              },
          headless=False
      )
 
       page = await browser.new_page()
       # abort image loading
       await page.route("**/*.{png,jpg,jpeg,svg}", lambda route: route.abort())
       await page.route("**/*", handle_route)
       await page.goto('https://www.oxylabs.io')
       await page.wait_for_timeout(5000)
       await browser.close()
 
if __name__ == '__main__':
   asyncio.run(main())