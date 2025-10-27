---
title: 【技术干货】UI 和 API 自动化测试神器 - Playwright
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247497154&idx=1&sn=463e5c74dbd7cc4a0d31c3b27a0133a6&chksm=c007585ef770d148cfcc7f0bfbd919c61cea7e84133ccbc4fc1eeb635e8068515a703e5c022c&scene=58&subscene=0#rd
source: 星阑科技
date: 2023-02-22
fetch_date: 2025-10-04T07:43:58.105939
---

# 【技术干货】UI 和 API 自动化测试神器 - Playwright

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wfFYMXc5G1MkB33kPG39RNicXRzeiamibm5EsW2nxQudoJUicslqSSKM2zzVWt9icERKrvtjPJFqunhpyks94fYnRAg/0?wx_fmt=jpeg)

# 【技术干货】UI 和 API 自动化测试神器 - Playwright

星阑科技

以下文章来源于星阑实验室
，作者PortalLab

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7I2gqBRVgAVpkPNqBsibrgE0DM5mTmZIRYzgFUNPjF59g/0)

**星阑实验室**
.

聚焦API安全最新资讯，分享API安全研究成果

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOeiaFHTFtiatmEIxZQcXOHfyr6GOBM88IeMm28ybjSAHEJKicuQxPxN5L5NFZ5mza2NOnuokf9ant2fUQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NSkNgX8voWSJmuSUlcQtsLKWSxBUmsxRCOqbNibhhXFuhtfXiak5ibYGMcEGD9yzzIy4qVq1Q5a63IQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NSkNgX8voWSJmuSUlcQtsLgZE9TXJrsxHuabVS0UbocSyplzJJ0pxtQQZpAzIBdZwlByjZ3qUUAQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "好看的图.png")

**Tim**

**@PortalLab实验室**

**简介**

Playwright 是微软开源的端到端（end-to-end）测试框架，可用于现代 Web 应用。Playwright 提供如下特性：

**1. 任意浏览器、任意平台、一种 API**

* **跨浏览器：**Playwright 支持所有现代渲染引擎，包括 Chromium、WebKit 和 Firefox。
* **跨平台：**在 Windows、Linux 和 macOS 上，进行本地或 CI 测试（无头或有头）。
* **跨语言：**可在 TypeScript、JavaScript、Python、.NET、Java 中使用 Playwright API。
* **测试移动 Web：**Android Google Chrome 和移动 Safari 的本地移动仿真。桌面和云上运行的渲染引擎相同。

**2. 弹性、没有古怪的测试**

* **自动等待：**Playwright 在执行操作前，将等待到元素可被操作。它还有一组丰富的检查事件。两者结合可消除对人为超时的需求 — 这是导致古怪测试的主要原因。
* **Web 优先断言：**Playwright 断言是专门为动态 Web 创建的。检查将自动重试，直到满足必要的条件。
* **追踪：**配置测试重试策略，捕获执行踪迹，录像，截屏，以防止遗忘。

**3. 无需折中、无限制：浏览器在不同进程中运行属于不同源的 Web 内容。Playwright 与现代浏览器架构保持一致，在进程外运行测试。这使得 Playwright 摆脱典型的进程内测试运行器限制。**

* **复合一切：**横跨多个选项卡、多个源和多个用户的测试场景。为不同用户创建具有不同上下文的场景，并且在服务器上运行它们，这些都在一个测试中进行。
* **可信事件：**悬停元素，与动态控件交互，生成可信事件。Playwright 使用真正的浏览器输入管道，与真正的用户没有区别。
* **测试 Frame、穿透 Shadow DOM：**Playwright 选择器穿透 Shadow DOM，允许无缝进入 Frame。

**4. 完全隔离、快速执行：**

* **浏览器上下文：**Playwright 为每个测试创建一个浏览器上下文。浏览器上下文等同于全新的浏览器配置文件。它提供零开销的完全测试隔离。创建新浏览器上下文仅需几毫秒。
* **登录一次：**保存上下文的身份认证状态，并且在所有测试中重用。避免在每个测试中重复登录，还提供独立测试的完全隔离。

**5. 强大的工具：**

* **代码生成：**通过录制操作生成测试。将它们保存成任何语言。
* **Playwright 检查器：**检查页面，生成选择器，逐步完成测试执行，查看单击点，探索执行日志。
* **追踪查看器：**捕获所有信息以调查测试失败。Playwright 追踪包含测试执行录屏、实时 DOM 快照、操作资源管理器、测试源等。

**本文测试环境**

* **操作系统：**macOS 12.6
* **Python：**3.10.6（下文以 Python 为例，进行讲述）
* **Playwright：**1.30.0

**安装**

**创建测试环境**

```
mkdir playwright-democd playwright-demo/python3 -m venv venv# 安装 Pytest 插件venv/bin/pip3 install pytest-playwright# 安装需要的浏览器venv/bin/playwright install
```

**添加样例测试**

在当前工作目录或子目录内部，创建 test\_my\_application.py 文件，其内容如下：

```
import refrom playwright.sync_api import Page, expect

def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):    page.goto("https://playwright.dev/")
    # Expect a title "to contain" a substring.    expect(page).to_have_title(re.compile("Playwright"))
    # create a locator    get_started = page.locator("text=Get Started")
    # Expect an attribute "to be strictly equal" to the value.    expect(get_started).to_have_attribute("href", "/docs/intro")
    # Click the get started link.    get_started.click()
    # Expects the URL to contain intro.    expect(page).to_have_url(re.compile(".*intro"))
```

**运行样例测试**

在默认情况下，测试运行在 Chromium 上，可通过 CLI 选项进行配置，测试以 Headless 模式运行。测试结果和测试日志被展示在终端中。

```
venv/bin/pytest
```

**编写测试**

Playwright 断言（assertion）是专门为动态网页创建的。检查将自动重试，直到满足必要的条件。Playwright 自带 auto-wait，这意味着它在执行操作前，等待到元素变为可操作的（actionable）。Playwright 提供 expect 函数来编写断言。

下面是展示如何编写使用断言、定位器（locator）和选择器（selector）的测试的示例。

```
import refrom playwright.sync_api import Page, expect

def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):    page.goto("https://playwright.dev/")
    # Expect a title "to contain" a substring.    expect(page).to_have_title(re.compile("Playwright"))
    # create a locator    get_started = page.locator("text=Get Started")
    # Expect an attribute "to be strictly equal" to the value.    expect(get_started).to_have_attribute("href", "/docs/intro")
    # Click the get started link.    get_started.click()
    # Expects the URL to contain intro.    expect(page).to_have_url(re.compile(".*intro"))
```

**断言**

Playwright 提供 expect （https://playwright.dev/python/docs/test-assertions）函数，它将一直等待，直到满足预期条件。

```
import refrom playwright.sync_api import expect
expect(page).to_have_title(re.compile("Playwright"))
```

**定位器**

定位器（Locator）是 Playwright 的自动等待和重试能力的核心部分。定位器是一种随时在网页上查找元素的方法，用于在元素上执行诸如 .click、.fill 之类的操作。可以使用 page.locator(selector, \*\*kwargs) 方法创建自定义定位器。

```
from playwright.sync_api import expect
get_started = page.locator("text=Get Started")
expect(get_started).to_have_attribute("href", "/docs/installation")get_started.click()
```

选择器（Selector）是用于创建定位器的字符串。Playwright 支持许多不同的选择器，比如 Text、CSS、XPath 等。阅读 in-depth guide 文档，了解更多关于可用的选择器以及如何进行选择的信息。

```
from playwright.sync_api import expect
expect(page.locator("text=Installation")).to_be_visible()
```

**测试隔离**

Playwright Pytest 插件基于 test fixture（比如 built in page fixture）的概念，它将被传给你的测试。由于浏览器上下文，在测试之间，页面（Page）彼此隔离，这相当于开启新的浏览器行为，每个测试获得新环境，即使在一个浏览器中运行多个测试时，也是如此。

```
from playwright.sync_api import Page
def test_basic_test(page: Page):  # ...
```

**使用测试钩子**

可以使用各种各样的 fixture 在测试之前或之后执行代码，以及在它们之间共享对象。函数（function）作用域的 fixture 具有 beforeEach/afterEach 一样的自动使用行为。模块（module）作用域的 fixture 具有 beforeAll/afterAll 一样的自动使用行为，它在所有测试之前和所有测试之后运行。

```
import pytestfrom playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)def before_each_after_each(page: Page):    print("beforeEach")    # Go to the starting url before each test.    page.goto("https://playwright.dev/")    yield    print("afterEach")
def test_main_navigation(page: Page):    # Assertions use the expect API.    expect(page).to_have_url("https://playwright.dev/")
```

**运行测试**

可以运行单个测试、一组测试或全部测试。测试可以运行在一种或多种浏览器上。默认情况下，以 Headless 方式运行测试，这意味着在运行测试时，不会打开浏览器窗口，可以在终端中看到结果。通过使用 --headed 标记，可以以 headed 模式运行测试。

* 在 Chromium 上运行测试

```
pytest
```

* 运行单个测试文件

```
pytest test_login.py
```

* 运行一组测试文件

```
pytest tests/todo-page/ tests/landing-page/
```

* 使用函数名运行测试

```
pytest -k "test_add_a_todo_item"
```

* 以有头（headed）模式运行测试

```
pytest --headed test_login.py
```

* 在指定的浏览器上运行测试

```
pytest test_login.py --browser webkit
```

* 在多种浏览器上运行测试

```
pytest test_login.py --browser webkit --browser firefox
```

* 并行运行测试

```
pytest --numprocesses auto
```

【假定已安装 pytest-xdist，查看 here （https://playwright.dev/python/docs/test-runners#parallelism-running-multiple-tests-at-once）获取更多信息。】

**运行测试**

因为 Playwright 运行在 Python 中，所以可以使用 Debugger 调试它。Playwright 自带 Playwright Inspector，它允许你逐步通过 Playwright API 调用，查看它们的调试日志，以及探索选择器（selectors）。

```
PWDEBUG=1 pytest -s
```

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1Nic4mklfEV7amaicaWIywyjBndrIAQZI9KvtM8Dv98WOkqHvXJqncyMZI6Hz19cDTFFkY0LbNSVN1A/640?wx_fmt=png)

查看调试指南（debugging guide）了解关于 Playwright Inspector 以及使用浏览器开发者工具（Browser Developer tools）进行调试的更多信息。

**测试生成器**

Playwright 具有开箱即用的生成测试的能力，这是快速开始测试的好方法。它会打开两个窗口，一个是浏览器窗口，通过它你可以与希望测试的网站进行交互，另一个是 Playwright Inspector 窗口，通过它你可以录制测试、拷贝测试、清除测试以及改变测试的语言。

你将学习：

* How to generate tests with Codegen

**运行 Codegen**

```
playwright codegen playwright.dev
```

运行 codegen，然后在浏览器中执行操作。Playwright 将为用户的交互生成代码。Codegen 尝试生成弹性的基于文本的选择器。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1Nic4mklfEV7amaicaWIywyjBvA6rGGOCy5vV31wNQx3DJeiciclDnKl1Axye2lxOTujicahNfLmNuLsPQ/640?wx_fmt=png)

当你完成与页面的交互时，按下 record 按钮停止录制，使用 copy 按钮把生成的代码拷贝到编辑器。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1Nic4mklfEV7amaicaWIywyjBqeq8f7VfjI1Xc1zLO6sTQz2RIzB595FK9fSyF16Ju3gE35slBodoOw/640?wx_fmt=png)

使用 clear 按钮清除代码，重新开始录制。完成时，关闭 Playwright Inspector 窗口，或停止终端命令。

如欲了解有关生成测试的更多信息，请查看 Codegen 的详细指南。

**追踪查看器（Trace Viewer）**

Playwright 追踪查看器是一个 GUI 工具，它使你可以探查测试中记录的 Playwright 追踪，可以在测试的每个操作中来回移动，可视化地查看每个操作期间正在发生什么。

你将学习：

* 如何记录追踪
* 如何打开 HTML 报告
* 如何打开追踪查看器

**记录追踪**

像下面一样使用 browser\_context.tracing API 记录追踪：

```
browser = chromium.launch()context = browser.new_context()
# Start tracing before creating / navigating a page.context.tracing.start(screenshots=True, snapshot...