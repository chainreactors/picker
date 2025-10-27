---
title: 巧用Chrome-CDP远程调用Debug突破JS逆向
url: https://forum.butian.net/share/4062
source: 奇安信攻防社区
date: 2025-01-23
fetch_date: 2025-10-06T20:07:57.610437
---

# 巧用Chrome-CDP远程调用Debug突破JS逆向

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

### 巧用Chrome-CDP远程调用Debug突破JS逆向

* [渗透测试](https://forum.butian.net/topic/47)

CDP远程调用非常方便，他允许我们直接可以通过代码来操作浏览器完成一系列行为，希望通过我的这篇文章让师傅们对其有一定了解，学习并赋能与我们的渗透测试与安全研究工作之中，提升效率！

巧用Chrome-CDP远程调用Debug突破JS逆向
===========================
前言
--
我在测试一个网站的时候，大多数的网站不会对接口的请求数据做加密处理，但有的时候在测试一些重点行业的网络资产时，常常会碰到一些功能点存在加密，例如登录，个人信息查询，搜索等等。在以往我遇到这些存在接口加密站点的时候，一般就是通过一些调试手段，找到加解密函数，从F12的控制台对变量手动加密，解密，但这一方法的弊病就是我们每次都必须断好点，同时必须提前预知要加解密的内容，还要拼接函数执行，因此如果遇到需要FUZZ或者爆破的接口，只能放弃。再者就是通过开发者工具断点跟栈，一点点找函数调用关系，还原加密算法，但是一旦遇到加密复杂，存在js混淆的网站，这个方法的失败率就会成指数级上升。
于是，为了解决这个需求，在网上冲浪的时候，便发现了\*\*Chrome DevTools Protocol\*\*这个好东西，这是一套开放协议，简称CDP，允许外部程序通过Chrome浏览器提供的接口与其进行交互，CDP提供了丰富的接口，使得我们可以通过WebSocket协议来对接口传输数据，进而操作浏览器的各种功能，例如打开标签页，断点调试，执行js函数等等。这里有兴趣的小伙伴可以看一下官方文档：<https://chromedevtools.github.io/devtools-protocol/>
我在网上搜索资料的时候发现这方面教程极少，应用于安全领域方面的文章也是不超过五篇，在文章最后已经注明了地址，在按照文章学习使用的过程中，也是遇到了挫折重重，但是经过研究分析之后，本篇文章也都会尽可能详细地向大家介绍，CDP远程调用非常方便，他允许我们直接可以通过代码来操作浏览器完成一系列行为，希望通过我的这篇文章让师傅们对其有一定了解，学习并赋能与我们的渗透测试与安全研究工作之中，提升效率！
CDP，启动！
-------
### 开启远程调试
首先我们要开启谷歌浏览器的远程调试，并且设置端口，同时允许所有的源访问调试界面:
进入Chrome的根目录，呼出cmd:
![image-20241219173023743.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-7ffa8e8c04a67c460e6add284da6cc201b8a52ae.png)
执行命令，打开Chrome浏览器，同时设置远程调试端口，允许所有源访问调试详情页面:
\*\*这里要注意，在运行下面命令的时候，我们要先关闭电脑上运行的所有浏览器，不然会由于冲突导致启动失败。\*\*
> chrome --remote-debugging-port=9222 --remote-allow-origins=\\*
### 查看正在进行CDP调试的端点信息
执行命令我们会打开一个全新的Chrome，访问[http://localhost:9222/json](http://localhost:9222/json:):
![image-20241219173604462.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9f5ae3214f1e25281b0daf00eda78f1b815832e0.png)
在上图可以看到，访问之后有一堆json格式的数据，实际这个通俗理解是Chrome为我们以API的方式展示的可供远程调用的端点，我们可以看到我现在有一个标签页，是百度，因此在第二个数据中也看到了它的WebSocke调试地址，webSocketDebuggerUrl，因此假如我们想对其进行远程断点debug，执行js函数，我们就可以对这个地址发命令即可。
这里也标注一下json数据中其他键的含义：
- `id`: 会话 ID，用于在 CDP 中与特定页面进行通信。
- `title`: 页面的标题。
- `url`: 当前页面的 URL。
- `webSocketDebuggerUrl`: WebSocket 地址，用于与 CDP 建立通信。
CDP 命令
------
CDP命令格式，即我们向WebSocket接口发送的数据格式，所有的命令实际上有一个统一的格式规范。
> { 'method': '方法(命令)', 'id': (随便一个数字), 'params': {
>
> 该方法需要用到的参数都写在这里 } }
官方文档介绍了很多命令，这里我们主要用到一个命令:\*\*Debugger.evaluateOnCallFrame\*\*，主要作用就是：在xx处断点，同时在这里执行xx函数。
> { 'method': 'Debugger.evaluateOnCallFrame', 'id': 123, 'params': { 'callFrameId': callFrameId, 'expression': expression, 'objectGroup': 'console', 'includeCommandLineAPI': True, } }
上面那句话可以看到我给了两个变量，而本方法参数callFrameId，实际就表示了在哪里断点，而expression则是我们要执行的js函数。callFrameId的获取我们在下面的实验部分将有所介绍
实验开始
----
### 生成一个示例登录站点
这部分使用GPT来完成，我选用的模型是ChatGPT 4o with canvas，提示词如下：
> 请你帮我写一个登录系统，输入账号密码登录即可。要求使用php语言，无需使用mysql，直接用硬编码判断账号admin和密码admin123即可。登陆成功后可以无需有任何页面，这个系统的关键就是在前端写入账号密码，发送到后端接口校验的时候，要利用js对账号和密码的参数进行加密，请你发挥想象，对AES加密算法进行魔改，把加密算法写道单独的额外的js文件中，尽可能地避免通过前端的js代码审计可以复刻出加密算法，一定要确保js加密的安全性，防止被逆向。
在这篇文章完成的时候利用这个提示词，我测试了多个大模型，发现这个提示词会使AI产生幻觉，包括我再次用ChatGPT 4o跑了一遍，代码就有问题了，要么是前端得加密是先A再B再C，结果后端解密时候顺序乱套了，要么就是前后端的密钥和偏移，以及一些函数都不一样，容易出现一些尴尬的小问题，因此我把这个实验用的示例系统源代码也贴在下面，各位朋友可以复制到本地，方便复现学习。当然代码中也有丰富的注释，大家也可以一目了然加密逻辑，方面理解。
示例系统构成：前端页面i代码ndex.html，二次加密混淆逻辑代码secureEncrypt.js，后端校验代码login.php。
\*\*index.html\*\*
```html
<html lang\="en"\>
<head\>
   <meta charset\="UTF-8"\>
   <meta name\="viewport" content\="width=device-width, initial-scale=1.0"\>
   <title\>史上最安全的登录系统</title\>
   <script src\="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"\></script\>
   <script src\="./js/secureEncrypt.js"\></script\>
   <style\>
       /\\* 页面基础样式 \\*/
       body {
           font-family: Arial, sans-serif;
           background-color: #f4f4f9;
           margin: 0;
           padding: 0;
           display: flex;
           justify-content: center;
           align-items: center;
           height: 100vh;
      }
​
       /\\* 登录容器样式 \\*/
       .login-container {
           background: #fff;
           padding: 2rem;
           border-radius: 8px;
           box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
           max-width: 400px;
           width: 100%;
      }
​
       .login-container h1 {
           margin: 0 0 1.5rem;
           font-size: 1.8rem;
           color: #333;
           text-align: center;
      }
​
       /\\* 表单样式 \\*/
       form {
           display: flex;
           flex-direction: column;
      }
​
       label {
           margin-bottom: 0.5rem;
           font-size: 0.9rem;
           color: #555;
      }
​
       input {
           padding: 0.8rem;
           border: 1px solid #ddd;
           border-radius: 4px;
           margin-bottom: 1rem;
           font-size: 1rem;
           transition: border-color 0.3s ease;
      }
​
       input:focus {
           border-color: #007bff;
           outline: none;
      }
​
       button {
           padding: 0.8rem;
           background-color: #007bff;
           color: #fff;
           border: none;
           border-radius: 4px;
           font-size: 1rem;
           cursor: pointer;
           transition: background-color 0.3s ease;
      }
​
       button:hover {
           background-color: #0056b3;
      }
​
       /\\* 错误和成功信息样式 \\*/
       .message {
           margin-top: 1rem;
           text-align: center;
           font-size: 0.9rem;
      }
​
       .message.error {
           color: #ff0000;
      }
​
       .message.success {
           color: #28a745;
      }
   </style\>
</head\>
<body\>
   <div class\="login-container"\>
       <h1\>史上最安全的登录系统</h1\>
       <form id\="loginForm"\>
           <label for\="account"\>账号:</label\>
           <input type\="text" id\="account" name\="account" placeholder\="请输入你的账号" required\>

           <label for\="password"\>密码:</label\>
           <input type\="password" id\="password" name\="password" placeholder\="请输入你的密码" required\>

           <button type\="submit"\>登录</button\>
           <div id\="message" class\="message"\></div\>
       </form\>
   </div\>
​
   <script\>
       document.getElementById('loginForm').addEventListener('submit', async function (e) {
           e.preventDefault();
​
           const account \= document.getElementById('account').value.trim();
           const password \= document.getElementById('password').value.trim();
           const messageBox \= document.getElementById('message');
​
           if (!account || !password) {
               messageBox.textContent \= "Please fill out all fields.";
               messageBox.className \= "message error";
               return;
          }
​
           messageBox.textContent \= ""; // 清除之前的消息
​
           const key \= "MySuperSecretKey1234567890123456"; // 必须 32 字节
           const iv \= "RandomInitVector"; // 必须 16 字节
​
           try {
               // 加密数据
               const encryptedAccount \= secureEncrypt(account, key, iv);
               const encryptedPassword \= secureEncrypt(password, key, iv);
​
               // 发送加密数据到后端
               const response \= await fetch('login.php', {
                   method: 'POST',
                   headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                   body: new URLSearchParams({
                       account: encryptedAccount,
                       password: encryptedPassword,
                  }),
              });
​
               const result \= await response.json();
               if (response.ok) {
                   messageBox.textContent \= result.message;
             ...