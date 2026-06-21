---
title: 第17章 Computer Use + GUI Agent —— AI 操控电脑
url: https://mp.weixin.qq.com/s/fodOisjnrOATpsWav-PAaQ
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:48:23.471533
---

# 第17章 Computer Use + GUI Agent —— AI 操控电脑

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/T0ibbhsCmribRHMT3iaFLshiaVQZPUw1ryn6GfcAHY6QiabLycYoXjtLjNsicu1n1QYEiaFR5Ik0PZSJY4DmWBhcp3OuVhB88iblFialchK1gib0PicBCA/0?wx_fmt=jpeg)

# 第17章 Computer Use + GUI Agent —— AI 操控电脑

原创

网络安全民工
网络安全民工

网络安全民工

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 17.1 为什么需要 Computer Use？

传统 Agent 的局限：Agent 只能调 API → 但世界上绝大多数软件没有 API！

企业内部的遗留系统

桌面软件（Photoshop、Excel）

图形化界面的 SaaS 工具

Computer Use 的突破：

Agent 不再需要对方提供 API

它直接「看屏幕 → 分析画面 → 控制鼠标键盘」

就像人类一样和任何软件交互

类比：

传统 Agent = 只能打电话的人（必须对方有号码）

Computer Use = 能走进办公室的人（可以和任何人面对面交流）

# 17.2 Screenshot-Action Loop —— 核心循环

这是所有 Computer Use 系统的底层逻辑：

📊 架构示意

```
  ┌──────────────────────────────────────────────────┐  │                                                    │  │  1. 📸 Screenshot: 截取当前屏幕画面                 │  │         │                                          │  │         ▼                                          │  │  2. 👁️ Analyze: LLM 视觉分析画面                    │  │     - 识别窗口、按钮、文本框                        │  │     - 读取屏幕上的文字内容                          │  │     - 理解当前界面的状态                            │  │         │                                          │  │         ▼                                          │  │  3. 🤔 Decide: 决定下一步操作                       │  │     - 应该点击哪里？                                │  │     - 应该输入什么？                                │  │     - 是否需要滚动？                                │  │         │                                          │  │         ▼                                          │  │  4. 🖱️ Execute: 执行操作                            │  │     - mouse_move(x, y)                             │  │     - left_click()                                 │  │     - type("文本")                                 │  │     - scroll(direction)                            │  │     - key_press("Enter")                           │  │         │                                          │  │         ▼                                          │  │     回到步骤 1（直到任务完成）                       │  │                                                    │  └──────────────────────────────────────────────────┘
```

关键挑战：像素坐标的精确计算

问题：LLM 需要输出 「点击 (450, 200)」这样的坐标

但 LLM 是文本模型，不理解像素

Anthropic 的解决方案（训练阶段）：

专门训练 Claude 精确计数像素的能力

"Training Claude to count pixels accurately was critical.

Without this skill, the model finds it difficult to give mouse commands."

实操中的坐标系统：

截图尺寸通常是 1280x800 或 1920x1080

LLM 返回的坐标需要缩放到实际屏幕分辨率

返回格式：(x\_pct, y\_pct) 百分比比绝对像素更稳健

# 17.3 Anthropic Computer Use vs OpenAI CUA

📊 架构示意

```
┌──────────────┬─────────────────────────┬─────────────────────────┐│     维度      │  Anthropic Computer Use  │   OpenAI CUA            │├──────────────┼─────────────────────────┼─────────────────────────┤│ 发布时间      │ 2024.10 (API)            │ 2025.01 (Operator)       ││             │ 2025.10 (正式发布)        │                         ││ 操作范围      │ 整个操作系统              │ 浏览器内（虚拟浏览器）    ││ 模型          │ Claude 3.5+ Sonnet      │ GPT-4o (CUA 微调版)     ││ 环境          │ 用户真实桌面/Docker      │ 安全的虚拟浏览器环境      ││ 安全性        │ 依赖使用者自行沙箱         │ 平台内置安全隔离         ││ 动作类型      │ 鼠标+键盘+截图            │ 浏览器操作（点击/输入/滚动）││ 成本          │ 截图Token昂贵            │ 浏览器操作Token消耗较低   ││ Benchmark    │ OSWorld 14.9%            │ 未公布独立评分           │└──────────────┴─────────────────────────┴─────────────────────────┘
```

Anthropic 的设计哲学：「给 Claude 真实的电脑，让它按人类的方式工作」

OpenAI 的设计哲学：「给 GPT-4o 一个安全沙箱，专注于 Web 任务」

选型建议：

需要控制桌面软件 → Anthropic Computer Use

只需要浏览器操作 → OpenAI CUA

想要完全控制 → Anthropic + Docker 沙箱

# 17.4 性能数据与局限

OSWorld Benchmark 成绩：

📊 架构示意

```
  ┌──────────────────┬───────────┐  │      系统         │   得分     │  ├──────────────────┼───────────┤  │ 人类              │   75.0%   │  │ Claude 3.5 Sonnet │   14.9%   │  │ GPT-4V            │    7.8%   │  └──────────────────┴───────────┘
```

→ Claude 翻倍了前最好成绩，但离人类还很远

延迟：

每个动作 3-4 秒（截取→分析→执行）

10步任务 = 30-40秒

对比 Selenium 的 0.1秒/步，差距巨大

成本：

每张 1080p 截图消耗约 1500 tokens

每分钟成本约 $0.10-0.30

对比 API 调用的 $0.001/分钟，贵 100 倍

当前定位（2025-2026）：

→ 不是 Selenium 的替代品

→ 适合「API 无法覆盖的长尾场景」

→ 适合「快速原型验证」

→ 生产级自动化仍需传统方案

# 17.5 安全沙箱 —— 必须学！

给 AI 鼠标键盘的权限 = 极高的安全风险：

✗ 读取屏幕上的密码

✗ 复制敏感数据

✗ 误操作删除文件

✗ Prompt Injection 利用 AI 执行危险命令

安全措施（必须！）：

Docker 容器隔离

```
docker run -d \--security-opt=no-new-privileges \--cap-drop=ALL \--network=none \--read-only \computer-use-sandbox
```

操作系统级隔离

非管理员用户

只读挂载关键目录

网络访问白名单

操作确认（Human-in-the-Loop）

危险操作需用户确认

大额交易/删除文件 → 二次确认

审计日志

记录每一次鼠标点击和键盘输入

可追溯所有操作

Anthropic 官方建议：

"Always sandbox in Docker containers with limited permissions.

Never run with admin privileges."

# 17.5.1 坐标系统工程 —— 为什么 LLM 总是点不准？

▍ 坐标转换：从 LLM 输出到屏幕像素

LLM 输出的坐标通常是「归一化坐标」或「基于截图分辨率的坐标」。

但实际屏幕分辨率可能不同 → 需要坐标缩放。

问题链：

截图 1280x800 → LLM 分析 → 输出「点击 (640, 400)」→ 但实际屏幕是 2560x1600→ 如果直接发 (640, 400)，点到错误位置！

标准做法：

a) 发给 LLM 的截图使用固定分辨率（如 1280x800）

b) LLM 输出坐标基于 1280x800

c) 执行前做坐标缩放：x\_real = x\_llm × (screen\_width / screenshot\_width)

d) 使用百分比坐标更稳健：(x\_pct, y\_pct) 而非绝对像素

▍ 为什么 LLM 的坐标会有 ±5px 的误差？

这是 Computer Use 的一个核心难点：「让文本模型理解空间坐标」。

Anthropic 专门训练了 Claude 的「像素计数能力」，但仍然存在天然误差：

小按钮（20x20px）→ 5px 误差可能点到按钮外

密集列表 → 可能点到相邻项

动态 UI（动画中的元素）→ 坐标过了检测时已经变了

工程应对：

a) 坐标容错 —— 点击后截图验证，不符预期则微调坐标重试

b) 区域点击代替点点击 —— 「点击按钮中心区域」而非精确坐标

c) 元素描述作为主导航 —— 「点击 'Login' 按钮」→ 先用 OCR 定位

▍ 截图分辨率的经济学

分辨率越高 → LLM 的坐标越精准 → 但 Token 成本越高

分辨率越低 → 成本低 → 但可能 LLM 看错按钮

最佳实践（Anthropic 推荐）:

日常操作：1024x768 → 约 800 tokens/图

需要细节：1280x800 → 约 1200 tokens/图

文本密集（代码、表格）：1920x1080 → 约 2000 tokens/图

动态分辨率策略：

第一轮 → 低分辨率 1024x768（快速判断页面状态）

发现无法识别 → 升级到 1280x800

仍然需要细节 → 局部截图 500x500（放大特定区域）

# 17.5.2 沙箱深度 —— 不是「run docker」就完了

▍ 多层安全隔离（从外到内 4 层）

第1层：容器隔离 —— Docker/VM 层

禁用网络（--network=none）、只读根文件系统（--read-only）、

限制 CPU/Memory、丢弃所有 Linux Capabilities

第2层：用户隔离 —— 容器内部跑非 root 用户

USER agent（非 root），家目录只读

授予的目录要白名单管理，不是黑名单

第3层：动作白名单 —— 不是所有键盘组合都允许

禁止: Ctrl+Alt+Del、Win+R、rm -rf、格式化命令

允许: 文本输入、鼠标移动、窗口切换

第4层：结果审查 —— Agent 操作完的截图交给另一个 LLM 审核

检查：是否打开了敏感页面？是否输入了敏感内容？

这是最后一道防线

▍ 成本优化 —— Computer Use 的「省钱三板斧」

缓存重复截图 —— 同一个页面多次截取 → 对比 hash，相同则复用 LLM 分析结果

最小化截图区域 —— 不全屏截图，只截需要操作的应用窗口

混合自动化 —— 能用 API 的操作用 API（便宜 100 倍），

只在 API 无法覆盖时启动 Computer Use

面试可以提：「我们不是用 Computer Use 替代 Selenium，而是用 Computer Use

覆盖 Selenium 覆盖不到的 5% 的长尾操作场景。」

# 17.6 模拟 Computer Use Agent

下面实现一个 ComputerUseAgent 模拟器，模拟 Claude 的「截图→分析→动作」

核心循环。真实的 Computer Use 每次迭代需要传入 desktop screenshot 的 base64

给 Claude Vision，这里用描述文字替代。关键保留了三阶段：环境感知、动作决策、

执行反馈，以及坐标计算的容错逻辑。

📝 对应的代码实现

add\_elementfind\_element\_atdescribeanalyze\_screendecide\_actionexecute\_actionrun\_taskdemo\_computer\_useVirtualScreenComputerUseAgent

```
import timeimport jsonfrom typing import Optionalclass VirtualScreen:    """模拟计算机屏幕 —— 用作 Computer Use 的目标环境。"""    def __init__(self, width: int = 1280, height: int = 800):        self.width = width        self.height = height        self.elements = {}  # 屏幕上的 UI 元素 {name: (x, y, w, h)}    def add_element(self, name: str, x: int, y: int,                    w: int, h: int, text: str = ""):        """添加一个 UI 元素（按钮/输入框/文本）。"""        self.elements[name] = {            "x": x, "y": y, "w": w, "h": h, "text": text,        }    def find_element_at(self, click_x: int, click_y: int) -> Optional[str]:        """根据坐标查找被点击的元素。"""        for name, elem in self.elements.items():            if (elem["x"] <= click_x <= elem["x"] + elem["w"] and                    elem["y"] <= click_y <= elem["y"] + elem["h"]):                return name        return None    def describe(self) -> str:        """生成屏幕描述（模拟 LLM 视觉分析的结果）。"""        lines = [f"屏幕分辨率: {self.width}x{self.height}"]        for name, elem in self.elements.items():            lines.append(                f"  [{name}] 位置({elem['x']},{elem['y']}) "                f"大小({elem['w']}x{elem['h']}) 文本:「{elem['text']}」"            )        return "\n".join(lines)class ComputerUseAgent:    """Computer Use Agent —— 模拟完整的 Screenshot-Action Loop。    核心循环：      while not done:          screenshot → analyze → decide → execute → observe    """    def __i...