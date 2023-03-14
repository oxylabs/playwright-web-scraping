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