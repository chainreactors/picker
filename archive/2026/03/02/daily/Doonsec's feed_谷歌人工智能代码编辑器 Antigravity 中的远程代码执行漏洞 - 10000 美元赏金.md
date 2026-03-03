---
title: 谷歌人工智能代码编辑器 Antigravity 中的远程代码执行漏洞 - 10000 美元赏金
url: https://mp.weixin.qq.com/s/7H5AFeSIpYC2LbJliv6HUg
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:07:38.022448
---

# 谷歌人工智能代码编辑器 Antigravity 中的远程代码执行漏洞 - 10000 美元赏金

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0H6DL7mWZ61S2TGGm6ytQrX5JrZKSxyREGtBxgbGe2d9GOksIgYB3XfCm2EJrn1tqYAibBqEwFdaBm4sjSou65ibUr7qEmxIdvEY/0?wx_fmt=jpeg)

# 谷歌人工智能代码编辑器 Antigravity 中的远程代码执行漏洞 - 10000 美元赏金

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

几周前，谷歌发布了一款名为Antigravity 的全新 IDE 。根据推特上的讨论和各种消息，大家可能已经知道，它的内部运作机制和其他方面都与 Windsurf IDE 完全相同。

每当有新的AI浏览器、集成开发环境或工具上市，就会引发一场寻找第一个有影响力的漏洞的竞赛。这次@s1r1us忙着开发一些很酷的东西，所以轮到我来寻找切入点并着手研究了。

这款谷歌集成开发环境（IDE）自带浏览器。根据我们以往的经验，这是一个极具吸引力的目标。以下简要介绍 Antigravity IDE 的工作流程及其与浏览器的集成方式：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0ERjhLVgNlPFS2u1TC1SdPUGeBEIanYPW1fpxDfZtJb2mdRC5jkVh0YibF6gPQNb2WxpaIPHDobpew8c11XKyLPsXefKhdXC1kc/640?wx_fmt=webp&from=appmsg)

这里使用了一个 VS Code 扩展，它与一个语言服务器交互。这个服务器公开了一系列 API 调用，负责处理任何任务，无论这些任务来自 IDE 还是其他来源。

使用像procexp.exe这样的工具，我们可以全面了解 Antigravity IDE 正在执行的内容。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HANM77dTkPqibpiaTqf6jIEoL3ZCwWMFgNORrSZiaNNqmna5gHPTopqhmYAia6kJticxWdK4VibicnUHraUgjtuvFnkBTeW9SSlHjqT0/640?wx_fmt=other&from=appmsg)

首先是语言服务器：

```
d:\\Antigravity\\resources\\app\\extensions\\antigravity\\bin\\language_server_windows_x64.exe --enable_lsp --extension_server_port 19116 --csrf_token e8d42e20-02b4-4ec8-9156-6ce5d35d0f01 --random_port --cloud_code_endpoint <https://daily-cloudcode-pa.googleapis.com> --app_data_dir antigravity --parent_pipe_path \\\\.\\pipe\\server_8a46fdeaf98e6c96
```

该二进制文件负责运行服务器。端口号在extension\_server\_port参数中指定，每次运行端口号都是随机的。添加 CSRF 令牌标志是为了防范基于 DNS 重绑定的攻击，类似于@s1r1us发现的那些攻击。

语言服务器二进制文件也会调用该node.exe二进制文件。查看命令行，我们可以看到以下内容。

```
C:\Users\STARK-PC\AppData\Local\ms-playwright-go\1.50.1\node.exeC:\Users\STARK-PC\AppData\Local\ms-playwright-go\1.50.1\package\cli.jsrun-driver
```

它使用了 Playwright，用于控制浏览器自动化。IDE 的核心就在language\_server\_windows\_x64.exe这里，它是用 Golang 编写的。

在对 IDE 进行一番摸索并寻找潜在的陷阱之后，我总结出了以下两个切入点，它们应该能让我做出足够有影响力的东西。

Pwn 语言服务器

通过找到泄露 CSRF 令牌的方法，应该可以轻松实现这一点。CSRF 令牌用于防御基于 DNS 重绑定的攻击。添加此保护措施正是为了应对 s1r1us 之前指出的问题。

语言服务器会验证每个传入请求的x-codeium-csrf-token请求头。

第一步是了解 CSRF 令牌是如何生成的。通过检查扩展程序的源代码resources/app/extensions/antigravity/dist/extension.js，我们可以找到相关的代码路径：

```
const n = crypto.randomUUID();
await R.ExtensionServer.initialize(e, n)

[...]
[...]
t.startLanguageServer = asyncfunction(e, t) {
   s = ["--enable_lsp", "--extension_server_port", e.extensionServerPort.toString(), "--csrf_token", e.csrfToken]
```

根据randomUUIDMDN 对该方法的描述，我们可以假设它是安全的，并且是不可预测的，这与Math.random使用的情况不同。

加密：randomUUID() 方法 - Web API | MDN

为了查找 CSRF 令牌可能泄露的地方，我决定对语言服务器二进制文件执行字符串操作，并检查 CSRF 令牌值的使用方式。我搜索了诸如 `<command>` csrf token、csrftoken`<command>` 等模式。

我发现了一些有趣的占位符。查看第[1]行，它使用了一个字符串格式化程序，其值可能是一个 JSON 对象。如第[2]行所示，它访问了该request.csrfToken属性。根据注释，很明显这段脚本被注入到了浏览器中。

```
(program
  (namespace_definition
    name: (namespace_name) @name) @definition.namespace) @codeium.lineage_node
    (asyncfunction() {
      try {
        // Directly set the credentials in the service worker's global scope
        const request = %s; // [1]
        // Use the direct functions (Playwright compatibility)
        if (typeof globalThis.setCredentials === 'function') {
          await globalThis.setCredentials(request.csrfToken, request.serverAddress); // [2]
          // Initialize the RPC client if the function exists
          if (typeof globalThis.initializeRpcClient === 'function') {
            globalThis.initializeRpcClient();
            // TODO(b/450106975): Post launch, figure out why we call initializeRpcClient here and in the background.ts. One of the calls is redundant.
          }
          return { success: true, message: 'WindsurfBrowser API initialized successfully' };
        } else {
          return { success: false, message: 'WindsurfBrowser API not available' };
        }
      } catch (error) {
        console.error('Error setting credentials:', error);
        return { success: false, message: 'Error: ' + error.toString() };
      }
    })()
```

我还可以看到类似这样的调用与 CSRF 令牌有关。

```
google3/third_party/jetski/extension_server_pb/extension_server_go_proto.(*LanguageServerStartedRequest).GetCsrfToken
google3/third_party/jetski/extension_server_pb/extension_server_go_proto.(*LanguageServerStartedRequest).SetCsrfToken
```

然而，为了更好地理解语言服务器，我们需要对这个 Golang 二进制文件进行逆向工程。目前，我们暂且不讨论这个问题。

由于 CSRF 令牌被用于剧本创作中，我决定检查一下浏览器，所以我们直接进入正题。首次打开集成浏览器时，系统会提示您安装扩展程序。

Antigravity 浏览器扩展程序 - Chrome 网上应用商店 https://chromewebstore.google.com/detail/antigravity-browser-exten/eeijfnjmjelapkebgockoeaadonbchdd?pli=1

此扩展程序使 AI 代理能够与浏览器中打开的网站进行交互。安装扩展程序后，您可以进行一些尝试，例如，在聊天窗口中输入“打开 example.com”之类的提示，并将背景颜色更改为蓝色。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0Ejea7raaFunns8Eyg6MJWUbs4DQKb8vCrJxo3snyLsAM6cv3Hoia72InbI6SnYmaUibe6Bor7aBm1esHZcicOibmpibeMPeNbmUJ9g/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0Hibjr1KGVMeQAlOoq7T94Xm4WlHToYMpyYWn2icjh0tqU7L3Tvvz7fice0T2PrReeuW8peRwBYLryhsZK4CicWKiamcJ2mPImUaDFk/640?wx_fmt=webp&from=appmsg)

这看起来很有意思，也引出了一个问题：它是如何控制这一切的？还记得之前我们看到它node.exe被调用来运行cli.js剧作家的脚本吗？我们实际上可以调试一下，更好地了解发生了什么。

为了调试cli.js脚本，我们可以修改代码以启用调试功能，或者尝试放置一个代理，在执行时node.exe附加参数。然而，还有一种更简单的方法，无需任何设置。--inspectcli.js

我们还可以看到，它--remote-debugging-port在启动浏览器进程时使用了该标志。

```
"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9223 --user-data-dir="C:\\Users\\STARK-PC\\.gemini\\antigravity-browser-profile" --disable-fre --no-default-browser-check --no-first-run --auto-accept-browser-signin-for-tests --ash-no-nudges --disable-features=OfferMigrationToDiceUsers,OptGuideOnDeviceModel --flag-switches-begin --flag-switches-end
```

我之前提到的更简便的方法是直接获取要调试的 Node 进程的PID40632 。就我而言，它是，所以我会在终端中执行以下命令。

```
node -e "process._debugProcess(40632)"
```

然后chrome://inspect/用浏览器打开。这样我们就能调试这个cli过程了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FibnQicWPpibsicuN4nrv7GYLDFUIiaSHt3gudD5nbiczgWmuC3BdjwichmTcAoib5ezyAEA2RfibjibrHjNCCMAu89ickggHicIp52J5gWYE/640?wx_fmt=webp&from=appmsg)

在扩展服务工作线程中，我们可以找到一些关于 CSRF 令牌使用的引用chrome-extension://eeijfnjmjelapkebgockoeaadonbchdd/service\_worker\_binary.js。在第[5]行，可以看到它将指定的值设置this.Z到x-codeium-csrf-token键中。追溯这个值，我们会发现该self.setCredentials方法，该函数的第一个参数应该包含 CSRF 令牌的值。

```
self.setCredentials = function(a, b){
    return va(function(c){
        eh = { // [1]
            Z: a,
            V: b
        };

functionoh(){
    if (!eh)
        throw Error("Cannot initialize RPC client: no credentials");
    var a = eh // [2]
      , b = a.Z;

    ya: [new nh(b,a)], // [3]
    ...

functionnh(a, b){
    this.Z = a; // [4]
    ...

nh.prototype.intercept = function(a, b){
    a.metadata["x-codeium-csrf-token"] = this.Z; // [5]
```

现在，搜索setCredentials调用位置却没有任何结果。这很奇怪，因为如果是这样，这个扩展程序究竟是如何获得 CSRF 令牌的呢？答案就在我们之前从语言服务器二进制文件的字符串结果中获取的脚本里。

```
const request = %s; // [1]
        // Use the direct functions (Playwright compatibility)
        if (typeof globalThis.setCredentials === 'function') {
          await globalThis.setCredentials(request.csrfToken, request.serverAddress); // [2]
          // Initialize the RPC client if the function exists
          if (typeof globalThis.initializeRpcClient === 'function') {
            globalThis.initializeRpcClient();
```

这样就一切都清楚了。上述代码被注入到 Antigravity 扩展的上下文中，globalThis.setCredentials与之前的代码相同self.setCredentials，并且第一个参数显然是 CSRF 令牌。

要在浏览器中查看 Playwright 注入的内容脚本，我们需要在开发者工具中启用一个默认未启用的选项。在“源代码”→“搜索”下，启用“搜索匿名脚本和内容脚本” 。我从Masato Kinugawa 的研究中了解到这个技巧。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0GOLfrvnKI2f8ggk5SAJrJ5r2G9OljMPDeialU0sznlxdb3cEtUezlib8hFFZO49cIicicX9SibgB55pErsfib0tiaYBo28up6A2rdeo4/640?wx_fmt=webp&from=appmsg)

现在，如果您搜索evaluate(，应该会看到一些结果；如果不启用该选项，则不会看到任何结果。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HGUnBXBnZfXISYyzymvScNFyUnLHc3A5icOTNoY7vghc8rDo7lvcjiazyVuIYdSPrjkSCZmkSX1tNjBNPiaWP2d1P4BHK8xw3L5k/640?wx_fmt=webp&from=appmsg)

我在这里设置了一个断点，因为此方法负责将注入的内容脚本执行到页面中。这部分代码来自 Playwright 核心包，地址为https://github.com/microsoft/playwright/blob/1eba405f948b93d4d40da0c2b8ace3d9fcd766c9/packages/injected/src/utilityScript.ts#L64

```
var UtilityScript = class {
  constructor(isUnderTest) {
    thi...