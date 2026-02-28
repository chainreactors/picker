---
title: 【干货】漏洞挖掘技巧+深层原理分析 前端鉴权绕过（一）
url: https://mp.weixin.qq.com/s/8Dm8npmqBHHgV0Pfwns_RQ
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:56:14.440459
---

# 【干货】漏洞挖掘技巧+深层原理分析 前端鉴权绕过（一）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OUhbKic8oggcfIfFSvibRPYorfAC8mHD03rYuTH75oGO44NdPHcib2Aw8Vkpyq97JAicKibN5WwENW9zibzCLkGV2sJ3r6aTS1MpSyDzp6zaMmfYE/0?wx_fmt=jpeg)

# 【干货】漏洞挖掘技巧+深层原理分析 前端鉴权绕过（一）

小草培养创研中心

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/OUhbKic8oggcTLJyj74Oqo2f3MLFSQVX9m7DsicRPUxmOic89ZgONtpJa7lcFO9jCogGECB65icFvUUicpKyslARXpL3JmVVFXmfLFk2x4IhyKh0/640?wx_fmt=gif&from=appmsg)

**前****言**

在 SRC 相关的漏洞挖掘技巧文章中，前端鉴权绕过是高频出现的内容，本文将从实际案例出发，拆解前端鉴权绕过的实现技巧，深挖其底层代码原理，并总结可落地的挖掘方法与防范原则，为渗透测试和安全开发提供参考

**01**

**经典前端鉴权绕过案例实操**

我们常常在src技巧文章中看到以下的前端鉴权绕过案例

某 Web 系统的密码找回功能采用邮箱验证的方式，其鉴权绕过的实操步骤如下：

1. 在密码修改界面输入目标邮箱，点击获取验证码后，随机输入一串验证码并提交，同时利用抓包工具拦截请求与响应包；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OUhbKic8oggf04xj6fq6FfFOPfGO4e8Q2gvicwLjILS4Nxy4iaAOMU969fcXsclpKChNhVD60m9kPfRFCB214BicGOuLIUXvTLDJrpDxREvjcqY/640?wx_fmt=png&from=appmsg)

2. 拦截到的验证响应包中，存在data:false的核心判断字段，该字段是前端校验验证码是否有效的关键；

![](https://mmbiz.qpic.cn/mmbiz_png/OUhbKic8oggfufkboNNKxqdiarvBV13Y7pUYU7K3sMxIFIWcvjLjWWYVBEh8utGlvsxZvTGiaZYjGpLaykaURb2DU0ZabmgyzEcm3ibRlVhxKibU/640?wx_fmt=png&from=appmsg)

3. 将响应包中的false修改为true后放包，前端会判定验证码验证通过，直接跳转到新密码设置界面；

![](https://mmbiz.qpic.cn/mmbiz_jpg/OUhbKic8ogge9Q5lxzIT4xV5lDibyCCpmo1YIqQ3Ozobj2MpaIrsABObj0iawHG98YqRHuUsN3MHEM5oW60fw4efSumpbwusAibTmib3yVhSu6jM/640?wx_fmt=jpeg)

4. 若密码修改的后端 API 未做任何鉴权校验，此时即可直接完成密码修改，触发密码修改接口未授权访问漏洞。

上一步验证码请求中，前端在客户端内存中已经存储了用户想要修改的邮箱号，因此密码修改接口的传参则按照js运行流程被自动赋值。

**02**

**案例背后的底层原理剖析**

上述案例并非个例，但其背后的代码逻辑和漏洞本质往往被忽略，仅停留在 “技巧操作” 层面，我们从核心本质和代码逻辑两层进行拆解：

*01*

**漏洞核心本质**

此类漏洞的底层是Web 服务器后端 API 的未授权访问漏洞，前端鉴权绕过只是一种 “触发手段”。我们通过修改前端校验依赖的响应包，或直接篡改 JS 中的验证逻辑，绕过前端对多流程 API 调用的前置响应校验，从而直接调用本应通过校验后才能访问的功能接口，本质是利用了前端鉴权的 “表面性” 和后端鉴权的 “疏漏性”。

*02*

**前端代码层的校验逻辑漏洞**

前端鉴权绕过的核心，是突破前端请求 API 后对响应字段的校验逻辑，以下面的前端鉴权代码为例，可清晰看到两个典型的可绕过节点：

//登录认证函数，请求登录API，获取访问令牌Token

async function loginAuth() {

  const loginApi = 'https://api.example.com/auth/login'; //替换为实际登录API地址

  const credentials = {

    username: 'your\_username',

    password: 'your\_password'

  };

  try {

    const response = await fetch(loginApi, {

      method: 'POST',

      headers: { 'Content-Type': 'application/json' },

      body: JSON.stringify(credentials)

    });

    if (!response.ok) throw new Error(`登录失败: ${response.status}`);

    const authData = await response.json();

    //存储Token到本地（实际项目中需考虑安全存储）

    localStorage.setItem('authToken', authData.access\_token);

    return authData.access\_token;

  } catch (error) {

    console.error('认证错误:', error);

    throw error; // 向上传递错误

  }

}

//带鉴权的业务请求函数，请求业务API，处理业务API响应

async function fetchProtectedData() {

  const token = localStorage.getItem('authToken') || await loginAuth(); // 本地Token没有则调用登录API，获取访问令牌Token

  const businessApi = 'https://api.example.com/protected/data'; // 替换为实际业务API地址

  try {

    const response = await fetch(businessApi, {

      method: 'GET',

      headers: {

        'Authorization': `Bearer ${token}`, // Bearer Token鉴权模式

        'Content-Type': 'application/json'

      }

    });

    // 处理Token过期情况（401状态码）

    if (response.status === 401) {

      console.log('Token已过期，尝试刷新...');

      const newToken = await loginAuth(); // 重新登录获取新Token

      return fetchProtectedData(); // 递归重试请求

    }

    if (!response.ok) throw new Error(`业务请求失败: ${response.status}`);

    return await response.json(); // 返回业务数据

  } catch (error) {

    console.error('请求失败:', error);

    throw error;

  }

}

//使用示例

(async () => {

  try {

    // 1. 执行鉴权并获取业务数据

    const result = await fetchProtectedData();

    console.log('业务数据:', result);

  } catch (e) {

    console.error('流程执行失败:', e);

    // 这里处理错误（如显示错误提示）

  }

})();

**以上前端代码在渗透测试中进行审计后，可以绕过的点主要有两个**

**1.**绕过/auth/login的响应判断 if (!response.ok) throw new Error(`登录失败: ${response.status}`);

在 JavaScript 的fetch API 中，response.ok 是一个布尔值：

当 HTTP 状态码在 200-299 之间时，response.ok = true；

当状态码是 401（未授权）、403（禁止访问）、500（服务器错误）等时，response.ok = false。

因此通过burp拦截响应包并修改响应码为200 OK

**2、**绕过localStorage.setItem('authToken', authData.access\_token);给/auth/login的响应字段添加一个access\_token

要直接访问受保护的接口，核心是让业务接口认为你持有有效的 Token。因此通过 Burp 可以篡改登录接口（/auth/login）的响应，返回一个自定义的“假 Token”，让业务接口认可这个 Token。

**具体绕过步骤，如下：**

运行时前端代码首先触发loginAuth()函数，Burp会捕获到POST /auth/login的请求；

在Burp修改响应的状态码为200

再在json中添加字段access\_token

例如最终的绕过payload：

HTTP/1.1 200 OK

Content-Type: application/json

{"access\_token":"fake\_token\_999","expires\_in":3600,"message":"登录成功"}

**这样做可以绕过接口的返回校验逻辑，调用后续https://api.example.com/protected/data接口。**

倘若https://api.example.com/protected/data接口没有使用token做鉴权，则直接测出https://api.example.com/protected/data接口的未授权访问漏洞。

从以上两个案例，我们可以看到前后端分离的开发特征下，前端会承担一部分鉴权工作，后端API的鉴权往往会有疏漏。

**03**

**前后端分离架构下的鉴权核心问题**

在前后端分离架构中，前端负责“看”和“交互”，是与用户直接打交道的部分；后端负责“想”和“算”，是处理业务核心、数据存储和安全保障的引擎。它们通过 API 紧密协作，共同构成完整的应用。

上述案例的出现，与**前后端分离的开发架构特征**密切相关，这一架构下前端和后端的功能划分，直接导致了鉴权环节的天然漏洞隐患：

* 前端的核心作用是**API 请求的调度与展示**，类似于一个 “巨型 API 请求字典”，网站的所有核心数据均来自后端 API，前端的路由守卫、鉴权校验等操作，仅作用于客户端层面，属于 “表面防护”；
* 后端是**数据和权限的核心管控层**，真正的权限校验必须在后端 API 中完成，但实际开发中，很多开发人员会依赖前端的 “前置校验”，省略后端的独立鉴权步骤，导致 API 鉴权疏漏。

本质上，前端鉴权绕过、路由绕过等技巧，都是**辅助测试后端 API 权限问题**的手段：纯 API 权限测试中，接口参数的关联、传递需要大量的推断成本，而前端鉴权绕过可利用前端 JS 代码的自动调用机制，让 API 自动携带所需参数，能快速直接定位到用户交互页面中高价值的接口调用位置，提升漏洞挖掘效率。

**04**

**前端鉴权拦截的高频业务场景**

在渗透测试中，并非所有业务功能都存在前端鉴权绕过的可能，结合 AI 分析与实际挖掘经验，**前端鉴权拦截集中出现在四类高风险业务功能中**，也是漏洞挖掘的重点方向：

*01*

**角色操作类（最核心、最高频）**

这类功能完全依赖前端鉴权逻辑控制访问与操作权限，是鉴权绕过的 “重灾区”，典型场景包括：

* 后台管理系统的菜单 / 按钮权限（如普通用户访问/admin 路径、点击“删除用户”按钮）；
* 多角色系统的功能隔离（如免费用户调用付费会员API、普通用户使用管理员功能）。

**风险点：**前端仅通过本地存储的role: 'admin'、permission: 'delete\_user'等字段判断是否放行 API 请求，或仅校验 Token 是否存在，后端未对角色对应的实际权限做校验。

*02*

**交易 / 支付 / 资产类多流程业务（高风险）**

涉及资金、资产操作的多步流程，前端鉴权漏洞可能导致未授权的资金操作，典型场景包括：

* 支付 / 下单流程（创建订单、确认支付、订单提交）；
* 资产操作（充值、提现、转账、积分兑换、优惠券使用）；
* 订单状态修改（取消订单、确认收货、退款申请）。

**风险点：**前端仅校验 “是否登录”“余额是否足够” 等基础条件，后端未做二次校验；例如前端限制单日提现上限 1000 元，只需篡改鉴权 API 的响应结果，即可绕过该限制。

*03*

**特殊权限资源访问类**

前端通过鉴权控制静态 / 动态资源的访问权限，易因资源地址泄露被绕过，典型场景包括：

* 付费 / 会员资源（视频、音频、电子书、付费文档下载）；
* 后台静态资源（管理系统的 JS、CSS、模板文件）。

**风险点：**前端通过 Token 控制资源 URL 的访问，但资源本身无需额外鉴权，只需获取到资源的真实地址（如/api/v1/vip/video/123.mp4），直接访问即可绕过前端鉴权。

*04*

**身份验证类（基础鉴权环节）**

属于用户身份校验的基础环节，鉴权逻辑简单但漏洞影响大，典型场景包括：

* 登录、注册、找回密码（验证码校验、账号密码正确性校验）。

**风险点：**前端仅校验接口响应的response.ok、data等字段，未做深层校验，篡改响应状态码或核心字段即可绕过登录、验证码验证等逻辑，如本文开头的密码找回案例。

综上，前端鉴权拦截的高频场景有一个共性：**客户端界面存在明显的功能拦截、校验拦截，但后端未对前端的校验结果做二次验证。**针对这类场景，绕过的核心思路是：抓取并推断功能校验对应的 API 请求包，理清或猜测前端对 API 响应的判断逻辑，针对性篡改即可。

**05**

**破解前端鉴权拦截的三种实操方法**

当在渗透测试中发现前端存在鉴权拦截时，可按以下三种方法逐步尝试破解，从简单的响应包篡改，到深度的 JS 代码审计，层层递进：

**方法一：猜解并修改鉴权接口返回值，快速绕过**

这是最直接、最高效的方法，无需分析复杂的 JS 代码，核心是篡改鉴权接口响应体的核心字段，直接绕过前端校验。

* 定位业务功能对应的**核心鉴权接口**（如验证码验证、登录、角色权限校验接口）；
* 利用抓包工具拦截响应包，修改响应体中的核心判断字段，常见包括：业务状态码（status）、角色标识（role）、权限标识（permission）、管理员标识（isAdmin）、校验结果（data）等；
* 若不清楚具体的有效字段值，可准备**状态码 fuzz 字典 （例如：https://github.com/River123-sys/status-code-dict-fuzz）**进行批量测试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OUhbKic8oggffJVASdJxLW4GFJeDnXkOnb8lWmkE2kuG1gywQK15Hk8hBEhsibazdMbKVibwWTBelu0ceZic5DibdRhVF2xVBF0hCEaA316bAEBk/640?wx_fmt=png&from=appmsg)

**示例：**某管理员权限校验接口的响应包为{"status":1,"info":"管理员不存在"}，将status字段从 1 改为 0 后，前端直接判定权限校验通过，跳转到管理员界面。

该战术的优势是操作简单，若运气好测试成功可直接跳转到后续流程并调用高权限 API；若未成功，但判定该鉴权后的功能 API 具有高测试价值，则进入后续的 JS 代码审计环节。

**方法二：定位 JS 鉴权逻辑，构造合规返回值**

当直接修改响应包无效时，需分析前端 JS 代码的鉴权逻辑，针对性构造符合前端校验要求的响应值，步骤如下：

* 利用浏览器开发者工具或 JS 代码审计工具，**全局搜索鉴权接口的名称**，定位到调用该接口的发包函数；
* 分析该函数中**对 API 响应值的处理逻辑**，找到前端校验的核心判断条件（如业务状态码、字段是否存在、字段值范围等）；
* 可将 JS 代码传入 AI 工具，让 AI 辅助分析校验逻辑，**并构造能绕过判断的合规响应值；**
* 利用抓包工具篡改鉴权接口的响应包，返回构造后的合规值，实现绕过。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OUhbKic8oggfQWx56hJsicCrTibSHR0fodL9WsO8uicYUnkPLGLVZu2yUZ0eFlOia1ticx8ZTzCNycycAzanPupfTJrFVue2WLxkpSfAxAic8maFSo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OUhbKic8oggf0qEcm1mwa3zIZxVk6FKoKMa6GwJq3z3xU3dqJEXKH9IDBl6wZicicxLP6B3VPnMW1A7j3ZhshHLGuVKoV4haMys97p9XzSW5ib4/640?wx_fmt=png&from=appmsg)

示例：这段代码中，可以通过构造接口的返回state字段绕过前端鉴权判断

前端仅当鉴权接口响应的A.data.state为undefined或-1000，且state>=0时，才会放行请求。只需构造响应包的state字段为0，即可进入进入返回A.data的正常业务逻辑，绕过拦截。”

**方法三：篡改/重写JS代码，直接跳过校验逻辑*...