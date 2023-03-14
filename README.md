# Web Scraping With Playwright

[<img src="https://img.shields.io/static/v1?label=&message=Playwright&color=brightgreen" />](https://github.com/topics/playwright) [<img src="https://img.shields.io/static/v1?label=&message=Web%20Scraping&color=important" />](https://github.com/topics/web-scraping)

- [Web Scraping With Playwright](#web-scraping-with-playwright)
  - [Support for proxies in Playwright](#support-for-proxies-in-playwright)
    - [Node.js](#nodejs)
    - [Python](#python)
    - [Node JS](#node-js)
    - [Python Code](#python-code)
  - [Basic scraping with Playwright](#basic-scraping-with-playwright)
  - [Locating elements](#locating-elements)
  - [Scraping text](#scraping-text)

This article discusses everything you need to know about news scraping, including the benefits and use cases of news scraping as well as how you can use Python to create an article scraper.

For a detailed explanation, see our [blog post](https://oxy.yt/erHw).

## Support for proxies in Playwright

Playwright supports the use of proxies. Before exploring this subject further, here is a quick code snippet showing how to start using a proxy with Chromium:

### Node.js

```javascript
const chromium = require('playwright')
const browser = await chromium.launch()
```

### Python

```python
from playwright.async_api import async_playwright
import asyncio
async def main():
   with async_playwright() as p:
       browser = await p.chromium.launch()
```

This code needs only slight modifications to fully utilize proxies.

In the case of Node.js, the launch function can accept an optional parameter of launch options. This `launchOption` object can, in turn, send several other parameters, e.g.,  headless. The other parameter needed is proxy. This proxy is another object with properties such as server, username, password, etc. The first step is to create an object where these parameters can be specified. And, then pass it to the launch method like the below example:

### Node JS

```javascript
const playwright = require("playwright")
 
(async() =>{
 for (const browserType of ['chromium', 'firefox',  'webkit']){
   const launchOptions = {
       headless: false,
       proxy: {
          server: "http://pr.oxylabs.io:7777",
          username: "USERNAME",
          password: "PASSWORD"
        }
     }
   const browser = await playwright[browserType].launch(launchOptions)
 }
})
```

In the case of Python, it’s slightly different. There’s no need to create an object of LaunchOptions. Instead, all the values can be sent as separate parameters. Here’s how the proxy dictionary will be sent:

### Python Code

```python
from playwright.async_api import async_playwright
import asyncio
async def main():
  with async_playwright() as p:
      browser = await p.chromium.launch(
           proxy={
               'server': "http://pr.oxylabs.io:7777",
               "username": "USERNAME",
               "password": "PASSWORD"
               },
           headless=False
       )
```

When deciding on which proxy to use, it’s best to use residential proxies as they don’t leave a footprint and won’t trigger any security alarms. Oxylabs’ Residential Proxies can help you with an extensive and stable proxy network. You can access proxies in a specific country, state, or even a city. What’s essential, you can integrate them easily with Playwright as well.

## Basic scraping with Playwright

Let’s move to another topic that will cover how to get started with Playwright using Node.js and Python. 

If you’re using Node.js, create a new project and install the Playwright library. This can be done using these two simple commands:

```shell
npm init -y
npm install playwright
```

A basic script that opens a dynamic page is as follows:

```javascript
const playwright = require("playwright")
(async() =>{
for (const browserType of ['chromium', 'firefox',  'webkit']){
   const browser = await playwright[browserType].launch()
   const context = await browser.newContext()
   const page = await context.newPage()
   await page.goto("https://amazon.com")
   await page.wait_for_timeout(1000)
   await browser.close()
   }
})
```
Let’s look at the above code – the first line of the code imports Playwright. Then, multiple browsers are launched. It allows the script to automate Chromium, Firefox, and Webkit. Then, a new browser page is opened. Afterward, the `page.goto()` function navigates to the Amazon web page. After that, there’s a wait of 1 second to show the page to the end user. Finally, the browser is closed.

The same code can be written in Python easily. First, install the Playwright Python library using the pip command and also install the necessary browsers afterward using the install command:

```shell
python -m pip install playwright
playwright install
```

Note that Playwright supports two variations – synchronous and asynchronous. The following example uses the asynchronous API:

```python
from playwright.async_api import async_playwright
import asyncio
async def main():
 async with async_playwright() as p:
   browser = await p.chromium.launch(headless=False)
   page = await browser.new_page()
   await page.goto('https://amazon.com')
   await page.wait_for_timeout(1000)
   await browser.close()
```

This code is similar to the Node.js code. The biggest difference is the use of `asyncio` library. Another difference is that the function names change from camelCase to snake_case.

In Node JS, If you want to create more than one browser context or if you want to have finer control, you can create a context object and create multiple pages in that context. This would open pages in new tabs:

```javascript
const context = await browser.newContext()
const page1 = await context.newPage()
const page2 = await context.newPage()
```

You may also want to handle page context in your code. It’s possible to get the browser context that the page belongs to using the `page.context()` function.

## Locating elements

To extract information from any element or to click any element, the first step is to locate the element. Playwright supports both CSS and XPath selectors.

This can be understood better with a practical example. Open the following amazon link:

https://www.amazon.com/b?node=17938598011

You can see that all the items are under the International Best Seller category, which has div elements with the class name  “a-spacing-base”.

To select all the div elements, you need to run a loop over all these elements. These div elements can be selected using the CSS selector:

```css
.a-spacing-base
```

Similarly, the XPath selector would be as follows:

```text
//*[@class="a-spacing-base"]
```

To use these selectors, the most common functions are as follows:

- `$eval(selector, function)` –  selects the first element, sends the element to the function, and the result of the function is returned;

- `$$eval(selector, function)` –  same as above, except that it selects all elements; 

- `querySelector(selector)` –  returns the first element;

- `querySelectorAll(selector)` – return all the elements.

These methods will work correctly with both CSS and XPath Selectors.

## Scraping text

Continuing with the example of Amazon, after the page has been loaded, you can use a selector to extract all products using the $$eval function.

```javascript
const products = await page.$$eval('.a-spacing-base', all_products => {
   // run a loop here
   })
```

Now all the elements that contain product data can be extracted in a loop:

```javascript
all_products.forEach(product => {
   const title = product.querySelector('span.a-size-base-plus').innerText
})
```

Finally, the innerText attribute can be used to extract the data from each data point. Here’s the complete code in Node.js:

```javascript
const playwright = require("playwright")
(async() =>{
for (const browserType of ['chromium', 'firefox',  'webkit']){
   const launchOptions = {
       headless: false,
       proxy: {
          server: "http://pr.oxylabs.io:7777",
          username: "USERNAME",
          password: "PASSWORD"
        }
     }
   const browser = await playwright[browserType].launch(launchOptions)
   const context = await browser.newContext()
   const page = await context.newPage()
   await page.goto('https://www.amazon.com/b?node=17938598011');
   const products = await page.$$eval('.a-spacing-base', all_products => {
       const data = []
       all_products.forEach(product => {
           const title = product.querySelector('span.a-size-base-plus').innerText
           const price = product.querySelector('span.a-price').innerText
           const rating = product.querySelector('span.a-icon-alt').innerText
           data.push({ title, price, rating})
       });
       return data
   })
   console.log(products)
   await browser.close()
   }
})

```

The Python code will be a bit different. Python has a function eval_on_selector, which is similar to `$eval` of Node.js, but it’s not suitable for this scenario. The reason is that the second parameter still needs to be JavaScript. This can be good in a certain scenario, but in this case, it will be much better to write the entire code in Python.

It would be better to use `query_selector` and `query_selector_all` which will return an element and a list of elements respectively.

```python
from playwright.async_api import async_playwright
import asyncio
 
 
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
       await page.goto('https://www.amazon.com/b?node=17938598011')
       await page.wait_for_timeout(5000)
 
       all_products = await page.query_selector_all('.a-spacing-base')
       data = []
       for product in all_products:
           result = dict()
           title_el = await product.query_selector('span.a-size-base-plus')
           result['title'] = await title_el.inner_text()
           price_el = await product.query_selector('span.a-price')
           result['price'] = await price_el.inner_text()
           rating_el = await product.query_selector('span.a-icon-alt')
           result['rating'] = await rating_el.inner_text()
           data.append(result)
       print(data)
       await browser.close()
 
if __name__ == '__main__':
   asyncio.run(main())
```

The output of both the Node.js and the Python code will be the same. For your convenience, you can click [here](#) to find the complete code used in this article.
