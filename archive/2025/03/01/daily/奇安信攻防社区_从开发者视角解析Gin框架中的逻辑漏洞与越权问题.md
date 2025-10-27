---
title: 从开发者视角解析Gin框架中的逻辑漏洞与越权问题
url: https://forum.butian.net/share/4164
source: 奇安信攻防社区
date: 2025-03-01
fetch_date: 2025-10-06T21:55:54.401636
---

# 从开发者视角解析Gin框架中的逻辑漏洞与越权问题

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 从开发者视角解析Gin框架中的逻辑漏洞与越权问题

* [漏洞分析](https://forum.butian.net/topic/48)

以go的gin后端框架为例子，详细剖析了各种逻辑越权漏洞的成因已经对应防范手段，也为白帽子提供挖掘思路

并发漏洞
----
### 原理
例如这是一段简单的go商城的示例代码
```go
package handlers
import (
"go2shop/internal/database"
"go2shop/internal/models"
"net/http"
"github.com/gin-gonic/gin"
)
...
func BuyProduct(c \*gin.Context) {
var req struct {
Username string `json:"username" binding:"required"`
ProductID uint `json:"product\_id" binding:"required"`
Quantity int `json:"quantity" binding:"required,gt=0"`
}
if err := c.ShouldBindJSON(&req); err != nil {
c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
return
}
// 查找用户
var user models.User
if err := database.DB.Preload("Inventory").Where("username = ?", req.Username).First(&user).Error; err != nil {
c.JSON(http.StatusBadRequest, gin.H{"error": "User not found"})
return
}
// 查找商品
var product models.Product
if err := database.DB.First(&product, req.ProductID).Error; err != nil {
c.JSON(http.StatusBadRequest, gin.H{"error": "Product not found"})
return
}
// 检查库存和余额
totalPrice := float64(req.Quantity) \* product.Price
if user.Balance < totalPrice {
c.JSON(http.StatusBadRequest, gin.H{"error": "Insufficient balance"})
return
}
if product.Stock < req.Quantity {
c.JSON(http.StatusBadRequest, gin.H{"error": "Insufficient stock"})
return
}
// 更新用户余额和商品库存
user.Balance -= totalPrice
product.Stock -= req.Quantity
// 更新用户的库存
var inventoryItem models.InventoryItem
if err := database.DB.Where("user\_id = ? AND product\_id = ?", user.ID, product.ID).First(&inventoryItem).Error; err == nil {
inventoryItem.Quantity += req.Quantity
database.DB.Save(&inventoryItem)
} else {
newInventoryItem := models.InventoryItem{
UserID: user.ID,
ProductID: product.ID,
Quantity: req.Quantity,
}
database.DB.Create(&newInventoryItem)
}
database.DB.Save(&user)
database.DB.Save(&product)
c.JSON(http.StatusOK, gin.H{"message": "Purchase successful"})
}
...
```
main.go中:
```go
...
r.POST("/buy", handlers.BuyProduct)
```
乍看之下没有任何问题，但其实由于Gin框架是多线程架构，就存在条件竞争的漏洞。也就是说，假设用户同时发送了两个一样的请求到服务器，多线程的Gin框架会同时进行：`if user.Balance < totalPrice {`的条件判断，这个时候就会两个请求都会认为库存足够（10 &gt;= 10）。然后两个请求分别扣减库存，最终商品库存会变为 -10，而实际上应该拒绝第二次购买。
然后两个线程会同时执行数据库的UPDATE的操作，
```go
if err := database.DB.Where("user\_id = ? AND product\_id = ?", user.ID, product.ID).First(&inventoryItem).Error; err == nil {
inventoryItem.Quantity += req.Quantity
database.DB.Save(&inventoryItem)
} else {
newInventoryItem := models.InventoryItem{
UserID: user.ID,
ProductID: product.ID,
Quantity: req.Quantity,
}
database.DB.Create(&newInventoryItem)
}
```
就会导致只付了一碗粉的钱却吃了商家两碗粉。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-ce1e4b40764f4123254227f1089ef35e9667c4f5.png)
这个红色部分就是造成漏洞的过程，可以看到库存被更新了两次
### 如何利用？
我这里使用的是BurpSuite的代理插件 Turbo
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-c843fad77b8c33137840b92ec538aa9b301902f8.png)
使用如下并发脚本:
```py
def queueRequests(target, wordlists):
global BATCH\_SIZE
BATCH\_SIZE = 60
engine = RequestEngine(endpoint='http://172.16.0.96:8888',
concurrentConnections=BATCH\_SIZE,
requestsPerConnection=100,
engine=Engine.THREADED,
pipeline=False,
maxQueueSize=BATCH\_SIZE
)
req = '''POST /buy HTTP/1.1
Host: 172.16.0.96:8888
Connection: keep-alive
Content-Length: 51
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090c11) XWEB/11581 Flue
Content-Type: application/json
Accept: \*/\*
Origin: http://172.16.0.96:8888
Referer: http://172.16.0.96:8888/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
x:%s
{"username":"testuser","product\_id":1,"quantity":1}'''
for i in range(10):
gate\_id = str(i)
for x in range(BATCH\_SIZE):
engine.queue(req, '0.000', gate=gate\_id)
engine.openGate(gate\_id)
time.sleep(0.5)
def handleResponse(req, interesting):
xtime= req.response.split('\r\n\r\n')[1]
req.label = xtime
table.add(req)
def completed(reqsFromTable):
diffs = []
time.sleep(1)
print len(reqsFromTable)
for i in range(len(reqsFromTable)):
if i % BATCH\_SIZE != 0:
continue
entries = []
for x in range(BATCH\_SIZE):
entries.append(float(reqsFromTable[i+x].label))
entries.sort()
diffs.append(entries[-1] - entries[0])
diffs.sort()
print('Best: '+str(min(diffs)))
print('Mean: '+str(mean(diffs)))
print('Stddev: '+str(stddev(diffs)))
print('Median: '+str(diffs[len(diffs)/2]))
print('Range: '+str(max(diffs)-min(diffs)))
handler.setMessage(str(sum(diffs)/len(diffs)))
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-38c63b70837f294063e27aea600628bd8cada0bf.png)
这里就出现了不止一次的成功响应
那作为开发者该如何防止这种情况的发生呢？
### 线程锁
线程锁就是在同时只允许一个线程删改数据，具体实现机制分为读写锁和互斥锁，这两种锁的区别在于:
- 读写锁就是你在一个图书馆，有很多人来借阅书籍。当有人仅仅是阅读书籍（不修改），那么多个读者可以同时进行，不会互相干扰。但如果有人想要修改或整理书籍（写操作），那么在这段时间内，所有的读者和其他写作者都必须等待。
- 互斥锁就是你去上厕所，你拉完擦完屁股出来后后了别人才能拉。
所以说可以看出来了吗？读写锁更加试用于读操作&gt;&gt;写操作，互斥锁更加适用于写操作≈读操作
这里我们应该采用互斥锁来保证安全:
```go
func BuyProduct(c \*gin.Context) {
var req struct {
ProductID uint `json:"product\_id" binding:"required"`
Quantity int `json:"quantity" binding:"required,gt=0"`
}
if err := c.ShouldBindJSON(&req); err != nil {
c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
return
}
// 从 JWT 中获取用户名
username, exists := c.Get("username")
if !exists {
c.JSON(http.StatusUnauthorized, gin.H{"error": "Unauthorized"})
return
}
// 查找用户
userMutex.Lock() // 加锁保护用户资源
var user models.User
if err := database.DB.Preload("Inventory").Where("username = ?", username.(string)).First(&user).Error; err != nil {
userMutex.Unlock()
c.JSON(http.StatusBadRequest, gin.H{"error": "User not found"})
return
}
// 查找商品
productMutex.Lock() // 加锁保护商品资源
var product models.Product
if err := database.DB.First(&product, req.ProductID).Error; err != nil {
productMutex.Unlock()
userMutex.Unlock()
c.JSON(http.StatusBadRequest, gin.H{"error": "Product not found"})
return
}
// 检查库存和余额
totalPrice := float64(req.Quantity) \* product.Price
if user.Balance < totalPrice {
productMutex.Unlock()
userMutex.Unlock()
c.JSON(http.StatusBadRequest, gin.H{"error": "Insufficient balance"})
return
}
if product.Stock < req.Quantity {
productMutex.Unlock()
userMutex.Unlock()
c.JSON(http.StatusBadRequest, gin.H{"error": "Insufficient stock"})
return
}
// 更新用户余额和商品库存
user.Balance -= totalPrice
product.Stock -= req.Quantity
// 更新用户的库存
var inventoryItem models.InventoryItem
if err := database.DB.Where("user\_id = ? AND product\_id = ?", user.ID, product.ID).First(&inventoryItem).Error; err == nil {
inventoryItem.Quantity += req.Quantity
database.DB.Save(&inventoryItem)
} else {
newInventoryItem := models.InventoryItem{
UserID: user.ID,
ProductID: product.ID,
Quantity: req.Quantity,
}
database.DB.Create(&newInventoryItem)
}
// 保存更改
database.DB.Save(&user)
database.DB.Save(&product)
productMutex.Unlock() // 解锁商品资源
userMutex.Unlock() // 解锁用户资源
c.JSON(http.StatusOK, gin.H{"message": "Purchase successful"})
}
```
具体流程图:
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-2e68f8af7c6d83e6a6dd772584f172bd1a69904d.png)
传参式越权漏洞
-------
这个就很好理解了，就是鉴权不充分嘛
例如有的新手开发者（比如我）就会直接从用户传参中获取username从而判断具体是那个用户来操作:
还是回到刚刚`buyProducts`的hanlder的例子:
```go
func BuyProduct(c \*gin.Context) {
var req struct {
Username string `json:"username" binding:"required"`
ProductID ui...