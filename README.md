# Web Scraping With Playwright

[<img src="https://img.shields.io/static/v1?label=&message=Playwright&color=brightgreen" />](https://github.com/topics/playwright) [<img src="https://img.shields.io/static/v1?label=&message=Web%20Scraping&color=important" />](https://github.com/topics/web-scraping)

- [Support for proxies in Playwright](#support-for-proxies-in-playwright)
- [Basic scraping with Playwright](#basic-scraping-with-playwright)
- [Web Scraping](#web-scraping)

This article discusses everything you need to know about news scraping, including the benefits and use cases of news scraping as well as how you can use Python to create an article scraper.

For a detailed explanation, see our [blog post](https://oxy.yt/erHw).


## Support for proxies in Playwright

#### Without Proxy.js

```javascript

// Node.js

const { chromium } = require('playwright'); "
const browser = await chromium.launch();
```



```python

# Python

from playwright.async_api import async_playwright
import asyncio
with async_playwright() as p:
    browser = await p.chromium.launch()
```

#### With Proxy

```javascript
// Node.js
const launchOptions = {
    proxy: {
        server: 123.123.123.123:80'
    },
    headless: false
}
const browser = await chromium.launch(launchOptions);
```



```python
# Python
proxy_to_use = {
    'server': '123.123.123.123:80'
}
browser = await p.chromium.launch(proxy=proxy_to_use, headless=False)
```

## Basic scraping with Playwright

### Node.Js

```shell
npm init -y
npm install playwright
```

```javascript
const playwright = require('playwright');
(async () => {
    const browser = await playwright.chromium.launch({
        headless: false // Show the browser. 
    });

    const page = await browser.newPage();
    await page.goto('https://books.toscrape.com/');
    await page.waitForTimeout(1000); // wait for 1 seconds
    await browser.close();
})();
```

### Python

```shell
pip install playwright
```



```python
from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as pw: 
        browser = await pw.chromium.launch(
            headless=False  # Show the browser
        )
        page = await browser.new_page()
        await page.goto('https://books.toscrape.com/')
        # Data Extraction Code Here
        await page.wait_for_timeout(1000)  # Wait for 1 second
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
```

## Web Scraping



![](https://oxylabs.io/blog/images/2021/10/Books_to_scrape_image.png)

#### Node.JS

```javascript
const playwright = require('playwright');

(async () => {
    const browser = await playwright.chromium.launch();
    const page = await browser.newPage();
    await page.goto('https://books.toscrape.com/');
    const books = await page.$$eval('.product_pod', all_items => {
        const data = [];
        all_items.forEach(book => {
            const name = book.querySelector('h3').innerText;
            const price = book.querySelector('.price_color').innerText;
            const stock = book.querySelector('.availability').innerText;
            data.push({ name, price, stock});
        });
        return data;
    });
    console.log(books);
    await browser.close();
})();
```

#### Python

```python
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
```

If you wish to find out more about Web Scraping With Playwright, see our [blog post](https://oxy.yt/erHw).
