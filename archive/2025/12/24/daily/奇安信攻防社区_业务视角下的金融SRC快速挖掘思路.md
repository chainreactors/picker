---
title: 业务视角下的金融SRC快速挖掘思路
url: https://forum.butian.net/share/4671
source: 奇安信攻防社区
date: 2025-12-24
fetch_date: 2025-12-25T03:24:21.469266
---

# 业务视角下的金融SRC快速挖掘思路

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

### 业务视角下的金融SRC快速挖掘思路

* [渗透测试](https://forum.butian.net/topic/47)

挖掘金融类漏洞的核心不仅仅是技术点本身，更需要深入理解业务链路、资金流转规则、风控策略与账户体系，从而在“设计缺陷”中找到突破点。本文总结梳理常见的金融逻辑漏洞类型及关键节点的可利用点，帮助安全人员深入理解这些场景，快速定位高价值逻辑漏洞大大提升漏洞挖掘效率和准确度，减少资损信息泄露等高危问题的发生。

金融SRC各场景漏洞挖掘技巧
--------------
### 注册开户场景
首先我们来了解一下开户场景的大概流程
![image-20251120165143882](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251120165143882.png)
#### 绕过信息校验开户
正常开户申请一般需要手机号+邮箱验证作为必填项，但往往只是在前端进行校验，符合正则格式则通过校验（手机号、邮箱、身份证号）
![image-20251120163408862](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251120163408862.png)
由于传过来的字段存在可选填项（如推荐码等），后端往往不会硬性要求全部字段都取，后端只会拿传过来的部分，这时候去掉手机相关字段仍可以正常开户
![image-20251120163517392](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251120163517392.png)
#### KYC信息复用伪造
攻击者可利用已认证的同一套资料（如身份证正反面、人脸信息）去注册第二个账户
![image-20251203160050564](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251203160050564.png)
正常上传证件信息，会对图片进行统一化格式处理，然后sdk加签存到数据库中，然后调用ocr对图片进行信息提取再去比对校验
如下图为上传证件信息的api接口，会返回一个加密的filekey文件名
![image-20251203155952891](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251203155952891.png)
很多时候后端为了节省资源开销，会优先调用缓存数据库结果，判断是否已经上传过，这时候就会导致一个证件信息可以开多个账户
#### 申请状态查询越权
我们渗透时候可以找到“申请/状态查询”相关接口或页面，修改post参数重放请求（id、orderNo、ticketId、userId等），观察响应是否返回不同用户的数据或敏感字段，然后利用自动化脚本/爆破可预测 ID
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-157040b3e2ee044484789a3bc4d84bb8a83db7fb.png)
如下面这个例子存在 request\\_id
![image-20251204110252131](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251204110252131.png)
可通过遍历`request\_id`获取其他用户手机号、身份证和银行卡信息
![image-20251204110932960](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251204110932960.png)
### 支付场景
#### 高并发下单/提现
后端没有加分布式锁，会导致重复下单 / 重复提现，攻击者可使用burp一秒内提交多次订单，连续发起多笔提现
![image-20251201114520985](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251201114520985.png)
成功创建多笔提现订单
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-c589cc3980fa50175b25bd9655be0a72f56201b5.png)
#### 负值反冲
在支付或退款接口中，如果传入的金额参数为负数，且后端没有严格校验金额必须为正，可能导致用户账户余额不减反增
金融类转账严格要求不能为负数，当修改金额为负数时就会导致负值反冲
![image-20251120110520581](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251120110520581.png)
#### int64 导致金额溢出
金融系统常见操作：
- 金额 × 精度（比如 ×10000 或 ×100000）
- 金额求和（累计 risk amount）
- transfer/settlement 金额偏大（企业/跨境/贷款/还款）
如果攻击者传入一个极大的数值，可能导致系统计算时溢出，变成一个负数或一个很小的数
```php
repayAmount := precision.ConvertAmountByBase(
bo.RepayAmount.String(),
eaBo.MoneyMultiBase,
)
userName, email := f.getUserInfo(ctx, userInfo)
now := time.Now()
provisionExpireTime := f.getProvisionExpireTime(ctx, bo.ChannelId, bo.UserId, bo.PlatformUserId, now)
paymentExpireTime := f.getPaymentExpireTime(ctx, bo.ChannelId, now)
```
常见于后端使用 int64 处理金额，int64 的范围有限（只有 9.22e18），金额乘倍率（比如 ×100000）后很容易超过这个范围，一旦超过CPU 会直接把高位截掉，并且go不会自动检查溢出，传参过大会导致 price / amount 可被改为负数、0.01 等
![image-20251118153559079](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251118153559079.png)
![image-20251118153520380](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251118153520380.png)
#### 篡改参数免手续费进行转账
在涉及外币或虚拟币的交易中，攻击者尝试修改接口中传输参数，使最终结算金额显著降低
![image-20251120110702048](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251120110702048.png)
计算最终金额的时候，会有很多参数参与运算，如渠道、汇率等，这时候可以尝试纂改相关参数免除手续费
![image-20251128150611909](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251128150611909.png)
转账时如果传入xx\\_id值为0的情况下，使后端 ampaign\\_result.code == 0 , 导致可以实现无手续费进行转账
```php
if remittanceTicketReq.GetFeeWaivedAmount() != 0 {
if remittanceTicketReq.GetCampaignId() == "" {
logger.Error(ctx, format: "invalid\_fee\_xxx\_id")
return common.ErrWalletInvalidRequestParam
}
}
```
![image-20251201115257442](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251201115257442.png)
### 优惠券场景
#### 优惠券码爆破
优惠券码未采用加密，并且没配置网关限流策略，导致可以高并发遍历
![image-20251201111453629](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251201111453629.png)
通过对voucher\\_code进行遍历，根据回显字段长度不同判断优惠券是否存在，如下图存在为820、819，不存在为798
![image-20251201111530424](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251201111530424.png)
#### 优惠券无锁限制重复领取
优惠券核销时，系统未严格校验该券的唯一使用记录或总使用次数
加锁安全的情况
```php
func applyCouponWithLock(amount float64) float64 {
coupon.mu.Lock() // 加锁
defer coupon.mu.Unlock() // 解锁
discounted := amount - coupon.Discount
if discounted < 0 {
discounted = 0
}
coupon.UsageCount++
return discounted
}
```
后端未加锁，导致可以重复领取
```php
func applyCoupon(amount float64) float64 {
discounted := amount - coupon.Discount
if discounted < 0 {
discounted = 0
}
atomic.AddInt64(&coupon.UsageCount, 1)
return discounted
}
```
#### 优惠券叠加使用
系统允许用户在单笔订单中，同时使用多张原本设计为互斥或限用一张的优惠券
![image-20251204105300720](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251204105300720.png)
正常单张使用
![image-20251201113637619](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251201113637619.png)
多张优惠券叠加使用
![image-20251201113756324](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251201113756324.png)
### 信息查询场景
#### 越权查询他人敏感信息
金融类对越权漏洞是十分严格的，像一般的越权查看个人信息、订单，是渗透测试的必测项目
![image-20251119165630215](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251119165630215.png)
例如用户 A 在查询自己的信息时，通过修改请求参数为用户 B 的订单 ID，成功查询到用户 B 的账单信息
![image-20251204104318708](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251204104318708.png)
![image-20251204104229848](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251204104229848.png)
稍微复杂一些的隐藏参数情况
![image-20251203163346295](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251203163346295.png)
函数实现是优先从post传参userid去查询的，然后再去解token提取uid进行查询
但是正常调用的时候，post传入的是{}，因此走到第二优先级的解token提取uid进行查询，那我们该如何去挖掘这类的漏洞呢，我们可以通过搜集history返回包中的参数组成字典去fuzz，如下图返回包中有 `userphone、uid、role`等字段
![image-20251203162838679](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251203162838679.png)
通过fuzz发现uid可作为查询参数，越权查询他人的信息
![image-20251203163817197](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251203163817197.png)
![image-20251203163851509](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20251203163851509.png)
#### Toc&amp;ToB网关配置错误接口混用
在 gRPC + Gateway 架构里，越权问题通常发生在普通用户能调用原本只允许管理员的 RPC 方法。
- 生成的 HTTP 路由没有绑定权限检查，任何人都能访问
- Gateway 没加角色校验，或者拦截器配置错误，token 可以被忽略或者被默认当作 admin
假设admin管理端域名为a.com，toc用户端域名为b.com，通过burp history导出一份a.com
![image-20241202145003839](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241202145004176.png)
右键选中 save item，导出对应的xml文件
![image-20241202145302261](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241202145302261.png)
导出文件格式还需要做进一步的处理：
1. \*\*Base64 解码\*\*：
- 将 XML 中的 `<request>` 元素的内容进行 Base64 解码，解码得到完整的 HTTP 请求内容。
2. \*\*解析请求\*\*：
- 根据 HTTP 请求格式，第一行包含了请求方法和路径，例如：POST /api/login HTTP/1.1，提取 `/api/login`
3. \*\*提取 POST 数据\*\*：
- 通过检查是否遇到 HTTP 请求头结束标志 `\r\n\r\n`，来提取请求体
4. \*\*写入 CSV 文件\*\*：
- 将提取到的请求方法、API 路径和 POST 数据写入到 CSV 文件中
导出文件命名为 `burp\_history.xml`，导出文件为 `burp\_history.csv`
脚本文件
```php
import os
import xml.etree.ElementTree as ET
import csv
import base64
input\_file = "burp\_history.xml"
output\_file = "burp\_history.csv"
if os.path.exists(output\_file):
try:
os.rename(output\_file, output\_file)
except PermissionError:
print(f"文件 {output\_file} 正在被占用，请关闭相关程序后重试。")
exit(1)
tree = ET.parse(input\_file)
root = tree.getroot()
try:
with open(output\_file, mode="w", newline="", encoding="utf-8") as csvfile:
csv\_writer = csv....