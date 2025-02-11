# Web Scraping With Playwright

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/product-integrations/refs/heads/master/Affiliate-Universal-1090x275.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

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
  - [Scraping Images](#scraping-images)
    - [Node JS](#node-js-1)
    - [Python](#python-1)
  - [Intercepting HTTP Requests with Playwright](#intercepting-http-requests-with-playwright)
    - [Python](#python-2)
    - [Node JS](#node-js-2)

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

<https://www.amazon.com/b?node=17938598011>

You can see that all the items are under the International Best Seller category, which has div elements with the class name  "a-spacing-base".

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

The Python code will be a bit different. Python has a function eval_on_selector, which is similar to the `$``eval` of Node.js, but it’s not suitable for this scenario. The reason is that the second parameter still needs to be JavaScript. This can be good in a certain scenario, but in this case, it will be much better to write the entire code in Python.

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

The output of both the Node.js and the Python code will be the same.

## Scraping Images

Next, we will learn how to scrape images using Playwright. For this instance, we will be using the Oxylabs official website as an image source. If you visit the website: <https://oxylabs.io> you will notice there are many images, we will extract all these images and save them in our current directory. First, let’s explore how we can accomplish this using Node JS.

### Node JS

The code will be similar to the one that we’ve written earlier. There are multiple ways to extract images using the Javascript playwright wrapper. In this example, we will be using two additional libraries https and fs. These libraries will help us to make Network requests to download the images and store them in the current directory. Take a look at the full source code below:

```javascript
const playwright = require("playwright")
const https = require('https')
const fs = require('fs')

(async() =>{
   const launchOptions = {
       headless: false,
       proxy: {
          server: "http://pr.oxylabs.io:7777",
          username: "USERNAME",
          password: "PASSWORD"
        }
     }
   const browser = await playwright["chromium"].launch(launchOptions)
   const context = await browser.newContext()
   const page = await context.newPage()
   await page.goto('https://oxylabs.io');
   const images = await page.$$eval('img', all_images => {
       const image_links = []
       all_images.forEach((image, index) => {
          const path = `image_${index}.svg`
          const file = fs.createWriteStream(path)
          https.get(image.href, function(response) {
               response.pipe(file);
          })
          image_links.push(image.href) 
       })
       return image_links
   })
   console.log(images)
   await browser.close()
})
```

As you can see. we are initializing a chromium browser instance with the Oxylabs Residential proxy just like the previous example. After navigating to the website, we are using the `$$eval` to extract all the image elements.

After extracting all the images we are using `forEach` loop to iterate over every image element.

```javascript
all_images.forEach((image, index) => {
          const path = `image_${index}.svg`
          const file = fs.createWriteStream(path)
          https.get(image.src, function(response) {
               response.pipe(file);
          })
```

Inside this `forEach` loop, we are constructing the image name using the index and also the path of the image. We are using a relative path so that the images will be stored in the current directory.

We then initiate a `file` object by calling the `createWriteStream` method of the fs library. Finally, we use the https library to send a `GET` request to download the image using the image src URL. We also pipe the response that we receive directly to the file stream which will write it in the current directory. 

Once we execute this code, the script will loop through each of the images available on the oxylabs.io website and download them to our current directory.

### Python

Python’s built-in support for file I/O operations makes this task way easier than Node JS. Similar to the Node JS code, we will first extract the images using the playwright wrapper. Just like our Amazon example, we can use the `query_selector_all` method, to extract all the image elements. After extracting the image elements, we will send a GET request to each image source URL and store the response content in the current directory.

The full source code is given below:

```python
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
```

## Intercepting HTTP Requests with Playwright

Now, we will explore how to intercept HTTP requests with Playwright. It can be used for advanced web scraping, debugging, testing, and performance optimization. For example, using playwright we can Intercept the HTTP Requests to abort loading images, customize headers, modify response output, etc. Let’s take a look at the below examples:

### Python

We will define a new function named `handle_route`, Playwright will invoke this function to intercept the HTTP requests. The function will be simple, we will fetch and update the title of the HTML code and also replace the header to make the `content-type: text/html`.

We will also write another lambda function which will help us to prevent images from loading. So, if we execute the script the website will load without any images, and both title & header modified. The code is given below:

```python
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
```

Notice, we are using the `route()` method to let Playwright know which function to call when intercepting the requests. It takes two parameters, first parameter is a regex to match the URI path. And, the second parameter is the name of the function or lambda. When we are using the `"**/*.{png,jpg,jpeg,svg}"` regex, we are telling Playwright to match all the URLs that end with the given extensions e.g. PNG, JPG, JPEG, and SVG.

### Node JS

The same thing can be achieved using Node JS as well. The code is also quite similar to Python.

```javascript
const playwright = require("playwright")
(async() =>{
   const launchOptions = {
       headless: false,
       proxy: {
          server: "http://pr.oxylabs.io:7777",
          username: "USERNAME",
          password: "PASSWORD"
        }
     }
   const browser = await playwright["chromium"].launch(launchOptions)
   const context = await browser.newContext()
   const page = await context.newPage()
   await page.route(/(png|jpeg|jpg|svg)$/, route => route.abort())
   await page.route('**/*', async route => {
              const response = await route.fetch();
              let body = await response.text();
              body = body.replace('<title>', '<title>Modified Response: ');
              route.fulfill({
                      response,
                      body,
                      headers: {
                              ...response.headers(),
                              'content-type': 'text/html'
                      }
               })
   })
   await page.goto('https://oxylabs.io');
   await browser.close()
})
```

We are using the `page.route` method to intercept the HTTP requests and modify the response’s title and headers. We are also blocking any images from loading. This can be a handy trick to speed up page loading and improve scraping performance.
