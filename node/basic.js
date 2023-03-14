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
