from playwright.async_api import async_playwright
import asyncio
import requests
 
 
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
       await page.goto('https://www.oxylabs.io')
       await page.wait_for_timeout(5000)
 
       all_images = await page.query_selector_all('img')
       images = []
       for i, img in enumerate(all_images):
           image_url = await img..get_attribute("src")
           content = requests.get(image_url).content
           with open("image_{}.svg".format(i), "wb") as f:
               f.write(content)
           images.append(image_url)
       print(images)
       await browser.close()
 
if __name__ == '__main__':
   asyncio.run(main())