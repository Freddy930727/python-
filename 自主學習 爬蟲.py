from selenium import webdriver
shrimp = "https://shopee.tw/search?keyword="
item = input("item")
low = "&order=asc" #價格低到高
high = "&order=asc"
end = "&sortBy=price"
pages = int(input("第幾頁")) - 1
page = "&page=" + str(pages)
decision = input("priorty:<lower> or <higher>")
if decision == "lower":
    former = low
elif decision == "higher":
    former = high
url = shrimp + item + former + page + end
print(url)

driver_path = "C:\\webdriver\\chromedriver.exe"
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(driver_path, options=option)
driver.implicitly_wait(10)
driver.get(url)
title_path = "//div[contains(@class,'_1NoI8_ _16BAGk')]"
price_path = "//span[contains(@class, '_341bF0')]"
titles= driver.find_elements_by_xpath(title_path)
prices= driver.find_elements_by_xpath(price_path)

total = len(titles)
print('商品數量：', total)
print('='*90)   

size = 60 if total>=5 else total
index = 0

for title, price in zip(titles, prices):
    print(title.get_attribute('textContent') + "\n"
          + price.text)
    print('-'*90)

    index += 1
    if index == size:
        break

driver.quit()






