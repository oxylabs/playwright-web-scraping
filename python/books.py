from playwright.async_api import async_playwright
import asyncio


async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://books.toscrape.com')

        all_items = await page.query_selector_all('.product_pod')
        books = []
        for item in all_items:
            book = {}
            name_el = await item.query_selector('h3')
            book['name'] = await name_el.inner_text()
            price_el = await item.query_selector('.price_color')
            book['price'] = await price_el.inner_text()
            stock_el = await item.query_selector('.availability')
            book['stock'] = await stock_el.inner_text()
            books.append(book)
        print(books)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())