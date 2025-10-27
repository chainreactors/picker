---
title: Playwright 入门教程
url: https://www.anquanke.com/post/id/289410
source: 安全客-有思想的安全新媒体
date: 2023-06-30
fetch_date: 2025-10-04T11:45:00.223443
---

# Playwright 入门教程

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Playwright 入门教程

阅读量**289965**

发布时间 : 2023-06-29 15:53:32

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## 1. 环境说明

1. 操作系统：macOS 11.7
2. Python：3.10.6

## 2. 安装

### **2.1. 创建测试环境**

mkdir playwright-demo

cd playwright-demo/

python3 -m venv venv

# 安装 Pytest 插件

venv/bin/pip3 install pytest-playwright

# 安装需要的浏览器

venv/bin/playwright install

### **2.2. 添加样例测试**

在当前工作目录或子目录内部，创建`test_my_application.py`文件，其内容如下：

import re

from playwright.sync\_api import Page, expect

def test\_homepage\_has\_Playwright\_in\_title\_and\_get\_started\_link\_linking\_to\_the\_intro\_page(page: Page):

page.goto(“Fast and reliable end-to-end testing for modern web apps | Playwright”)

# Expect a title “to contain” a substring.

expect(page).to\_have\_title(re.compile(“Playwright”))

# create a locator

get\_started = page.locator(“text=Get started”)

# Expect an attribute “to be strictly equal” to the value.

expect(get\_started).to\_have\_attribute(“href”, “/docs/intro”)

# Click the get started link.

get\_started.click()

# Expects the URL to contain intro.

expect(page).to\_have\_url(re.compile(“.\*intro”))

### **2.3. 运行样例测试**

默认情况下，测试运行在 chromium 上，可通过 CLI 选项进行配置，测试以 Headless 模式运行。测试结果和测试日志被展示在终端中。

venv/bin/pytest

## 3. 编写测试

Playwright 断言（assertion）是专门为动态网页创建的。检查会自动重试，直到满足必要的条件。Playwright 自带 auto-wait，这意味着它在执行操作之前等待元素变为可操作的（actionable）。Playwright 提供 expect 函数来写断言。

下面的样例测试展示了如何写使用断言、定位器（locator）和选择器（selector）的测试。

import re

from playwright.sync\_api import Page, expect

def test\_homepage\_has\_Playwright\_in\_title\_and\_get\_started\_link\_linking\_to\_the\_intro\_page(page: Page):

page.goto(“Fast and reliable end-to-end testing for modern web apps | Playwright”)

# Expect a title “to contain” a substring.

expect(page).to\_have\_title(re.compile(“Playwright”))

# create a locator

get\_started = page.locator(“text=Get started”)

# Expect an attribute “to be strictly equal” to the value.

expect(get\_started).to\_have\_attribute(“href”, “/docs/intro”)

# Click the get started link.

get\_started.click()

# Expects the URL to contain intro.

expect(page).to\_have\_url(re.compile(“.\*intro”))

### 3.1. 断言

Playwright 提供 expect 函数，它会一直等待，直到满足预期条件。

import re

from playwright.sync\_api import expect

expect(page).to\_have\_title(re.compile(“Playwright”))

### 3.2. 定位器

定位器（Locators）是 Playwright 的自动等待和重试能力的核心部分。定位器表示一种随时在网页上查找元素的方法，用于在元素上执行诸如 .click、.fill 之类的操作。可以使用 page.locator(selector, \*\*kwargs) 方法创建自定义的定位器。

from playwright.sync\_api import expect

get\_started = page.locator(“text=Get started”)

expect(get\_started).to\_have\_attribute(“href”, “/docs/installation”)

get\_started.click()

选择器（Selectors）是用于创建定位器的字符串。Playwright 支持许多不同的选择器，比如 Text、CSS、XPath 等。通过 in-depth guide 文档，了解更多关于可用的选择器以及如何进行选择的信息。

from playwright.sync\_api import expect

expect(page.locator(“text=Installation”)).to\_be\_visible()

### 3.3. 测试隔离

Playwright Pytest 插件基于 test fixture（比如 built in page fixture）的概念，它会被传给你的测试。由于浏览器上下文，在测试之间，页面（page）彼此隔离，这相当于开启新的浏览器行为，每个测试获得新环境，即使在一个浏览器中运行多个测试时，也是如此。

from playwright.sync\_api import Page

def test\_basic\_test(page: Page):

# …

### 3.4. 使用测试钩子

你可以使用各种各样的 fixtures 来在你的测试之前或之后执行代码，以及在它们之间共享对象。函数（function）作用域的 fixture 具有 beforeEach/afterEach 一样的自动使用行为。模块（module）作用域的 fixture 具有 beforeAll/afterAll 一样的自动使用行为，它会在所有测试之前和所有测试之后运行。

import pytest

from playwright.sync\_api import Page, expect

@pytest.fixture(scope=”function”, autouse=True)

def before\_each\_after\_each(page: Page):

print(“beforeEach”)

# Go to the starting url before each test.

page.goto(“Fast and reliable end-to-end testing for modern web apps | Playwright”)

yield

print(“afterEach”)

def test\_main\_navigation(page: Page):

# Assertions use the expect API.

expect(page).to\_have\_url(“Fast and reliable end-to-end testing for modern web apps | Playwright”)

## 4. 运行测试

你可以运行单个测试、一组测试或全部测试。测试可以运行在一种或多种浏览器上。默认情况下，测试以 headless 方式运行，这意味着在运行测试时，不会打开浏览器窗口，可以在终端中看到结果。通过使用 –headed 标记，可以以 headed 模式运行测试。

– 在 Chromium 上运行测试

pytest

– 运行单个测试文件

pytest test\_login.py

– 运行一组测试文件

pytest tests/todo-page/ tests/landing-page/

– 使用函数名运行测试

pytest -k “test\_add\_a\_todo\_item”

– 以有头（headed）模式运行测试

pytest –headed test\_login.py

– 在指定的浏览器上运行测试

pytest test\_login.py –browser webkit

– 在多种浏览器上运行测试

pytest test\_login.py –browser webkit –browser firefox

– 并行运行测试

pytest –numprocesses auto

（假定已安装 pytest-xdist，查看 here 获取更多信息。）

### 4.1. 运行测试

因为 Playwright 运行在 Python 中，所以可以使用 debugger 调试它。Playwright 自带 Playwright Inspector，它允许你逐步通过 Playwright API 调用，查看它们的调试日志，以及探索选择器（selectors）。

PWDEBUG=1 pytest -s

![]()

查看我们的调试指南（debugging guide）来了解关于 Playwright Inspector 以及使用浏览器开发者工具（Browser Developer tools）进行调试的更多信息。

## 5. 测试生成器

Playwright 具有开箱即用的生成测试的能力，这是快速开始测试的好方法。它会打开两个窗口，一个是浏览器窗口，通过它你可以与希望测试的网站进行交互，另一个是 Playwright Inspector 窗口，通过它你可以录制测试、拷贝测试、清除测试以及改变测试的语言。

你将学习：

– How to generate tests with Codegen

5.1. 运行代码生成器（Codegen）

playwright codegen Fast and reliable end-to-end testing for modern web apps | Playwright

运行 codegen，然后在浏览器中执行操作。Playwright 会为用户的交互生成代码。Codegen 会尝试生成弹性的基于文本的选择器。

![]()

当你完成与页面的交互时，按下**record**按钮停止录制，使用**copy**按钮把生成的代码拷贝到编辑器。

![]()

使用 clear 按钮清除代码，重新开始录制。完成时，关闭 Playwright Inspector 窗口，或停止终端命令。

要了解有关生成测试的更多信息，请查看 Codegen 的详细指南。

## 6. 追踪查看器（Trace Viewer）

Playwright 追踪查看器是一个 GUI 工具，它使你可以探查你的测试中记录的 Playwright 追踪，你可以在测试的每个操作中来回移动，可视化地查看每个操作期间正在发生什么。

你将学习：

– 如何记录追踪

– 如何打开 HTML 报告

– 如何打开追踪查看器

### 6.1. 记录追踪

像下面一样使用 browser\_context.tracing API 记录追踪：

browser = chromium.launch()

context = browser.new\_context()

# Start tracing before creating / navigating a page.

context.tracing.start(screenshots=True, snapshots=True, sources=True)

page.goto(“Fast and reliable end-to-end testing for modern web apps | Playwright”)

# Stop tracing and export it into a zip archive.

context.tracing.stop(path = “trace.zip”)

这将记录追踪，并把它放到名称为trace.zip的文件中。

### 6.2. 打开追踪

你可以使用 Playwright CLI 打开保存的追踪。

playwright show-trace trace.zip

### 6.3. 查看追踪

通过单击每个操作或使用时间轴悬停来查看测试的追踪，以及查看操作前后的页面状态。在测试的每个步骤期间查看日志、源和网络。追踪查看器创建 DOM 快照，因此你可以与它进行交互，打开开发者工具（devtools）等。

![]()

要了解更多信息，请查看 Trace Viewer 的详细指南。

## 7. Pytest 插件参考

Playwright 提供 Pytest 插件来编写端到端的测试。如果想要使用它，请参考 getting started guide。

### 7.1. 用法

使用 Pytest CLI 运行测试：

pytest –browser webkit –headed

如果你想自动地添加 CLI 参数，请使用 pytest.ini 文件。

7.2. CLI 参数

1. – –headed：以有头模式运行测试（默认：无头）
2. – –browser：用不同的浏览器 chromium、firefox、webkit 运行测试。可以指定多次（默认：所有浏览器）
3. – –browser-channel：使用的 Browser channel
4. – –slow-mo：使用慢动作运行测试
5. – –device：模拟的设备（Device）
6. – –output：用于测试生成的制品（aritifact）的目录（默认：test-results）
7. – –tracing：是否为每次测试记录追踪（trace）。on、off 或 retain-on-failure（默认：off）
8. – –video：是否为每次测试录制视频。on、off 或 retain-on-failure（默认：off）
9. – –screenshot：是否在每次测试后，自动地捕获截屏。on, off, or only-on-failure （默认：off)

### 7.3. Fixture

该插件给 pytest 配置 Playwright 特定的 fixture（fixtures for pytest）。为使用这些 fixture，使用 fixture 名称作为测试函数的参数。

def test\_my\_app\_is\_working(fixture\_name):

# Test using fixture\_name

# …

函数作用域：这些 fixture 在测试函数请求时创建，在测试结束时销毁。

1. – context：用于测试的新浏览器上下文（browser context）
2. – page：用于测试的新浏览器页面（browser page）

会话作用域：这些 fixture 在测试函数请求时创建，在测试结束时销毁。

1. – playwright：Playwright 实例
2. – browser\_type：当前浏览器的 BrowserType 实例
3. – browser：Playwright 启动的 Browser 实例
4. – browser\_name：浏览器名称
5. – browser\_channel：浏览器通道（channel）
6. – is\_chromium、is\_webkit、is\_firefox：各自浏览器类型的布尔值

自定义 fixture 选项：对于 browser 和 context fixture，使用下面的 fixture 定义自定义启动选项。

1. – browser\_type\_launch\_args：重写用于 browser\_type.launch(\*\*kwargs) 的启动参数。它应该返回字典
2. – browser\_context\_args：重写用于 browser.new\_context(\*\*kwargs) 的选项。它应该返回字典

### 7.4. 并行：同时运行多个测试

如果测试运行在有许多 CPU 的机器上，可以通过使用 pytest-xdist 同时运行多个测试，加快测试套件的整体执行时间。

# install dependency

pip install py...