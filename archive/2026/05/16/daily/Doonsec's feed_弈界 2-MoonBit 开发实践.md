---
title: 弈界 2-MoonBit 开发实践
url: https://mp.weixin.qq.com/s/2taFAb1prWrJhFudGDj6Ow
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:42:45.049082
---

# 弈界 2-MoonBit 开发实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImmC0ZAicLOI9TRTpAUJPzvIvuEZnDouE3ALYyibtXK9ibMicgpiaDHbm1cn6NUvDgNQL9zXe4bJZfceEJEdo3YM791zGIEMZ29E7PMc/0?wx_fmt=jpeg)

# 弈界 2-MoonBit 开发实践

爱唠叨的Nil

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

---

**开源实践**

---

**用 MoonBit 写一个中国象棋 AI 平台**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImkTurrW62vKQWkeXPQFhC2X8YwicUPiaIjkfqXm9vCUErCrN2IZKhuTZE4eSsZxZB8xgI3TBiaZyFt2FZmLywJGVKUEDCfquOib5so/640?wx_fmt=jpeg&from=appmsg)

**（图片为AI生成）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CBe66ugaImnZPicS9x0YZGoW8kO9SK9eamJlw6bDASekeTiaaONP1ONn8RImqVpbJpPxVcEI8eiboYnr9Q4J1Dicic3tictPicLic5x8jia0nzaZicSBM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/CBe66ugaImk042ib4LrDZqcfIkp36fJOAk1v0eI8pBFhKSqN8PBXZ5Fmco2bkkb9XSh0RQDc4zYm6iaK5xKxVAz8kNHApPYSwwibO9G2VzNAzU/640?wx_fmt=png&from=appmsg)

—— 从棋盘规则引擎到 Web 对战平台，9000 行代码的全栈实践

该项目使用 moonbit lang 复刻 maple 的 chessverse 项目，https://gitee.com/hongmaple/ChessVerse

弈界 ChessVerse | 原创技术分享

2026 年 5 月

# **一、开篇：为什么用 MoonBit 写象棋？**

中国象棋是世界上最具策略深度的棋类游戏之一，其规则的复杂性使得它成为 AI 算法研究的经典试金石。如何用一门新兴的编程语言从零构建一个完整的象棋 AI 平台？这正是“弈界”（ChessVerse）项目的出发点。

弈界是一个完全用国产编程语言 MoonBit 编写的中国象棋 AI 平台，涵盖了从棋盘规则引擎、AI 搜索算法、REST API 后端服务器到前端界面的全栈实现。整个项目约 9000 行代码，其中后端 3833 行、前端 3090 行，棋库引擎 1001 行，AI 搜索 673 行，数据库 400 行。本文将完整呈现这个项目的构建过程、核心技术实现以及开发中的思考与收获。

MoonBit 是一门面向安全、性能和生态的系统级编程语言，具有类 Rust 的类型系统和模式匹配，但更加简洁易用。它能够编译为原生二进制、WASM 以及 JavaScript，这使得它在后端服务和前端应用中都能发挥优势。对于象棋这样计算密集型的项目，MoonBit 的原生编译性能能带来显著的执行效率提升。

# **二、项目架构总览**

弈界的整体架构分为四大模块，每个模块职责明确、解耦清晰。后端采用 MoonBit 的 @http 包实现 HTTP 服务，前端是一个单文件的 HTML/CSS/JS 应用，中间通过 REST API 和 WebSocket 进行通信。棋库引擎和 AI 搜索作为独立包被后端引用，形成清晰的分层架构。

|  |  |  |  |
| --- | --- | --- | --- |
| **模块** | **文件** | **行数** | **职责** |
| 后端 API | backend/index.mbt | 3,833 | REST API + WebSocket 路由、71 个接口 |
| 数据库 | backend/db.mbt | 400 | SQLite3 持久化 |
| 棋盘规则 | src/chess/\*.mbt | 1,001 | 规则引擎 + 走法生成 |
| AI 搜索 | src/ai/search.mbt | 673 | Alpha-Beta + 置换表 |
| 前端 | public/index.html | 3,090 | 单文件多端自适应应用 |

*表 1：弈界项目模块总览*

数据流向非常直观：前端发起 HTTP 请求或 WebSocket 连接，后端的路由函数解析请求并调用对应的 handler，handler 业务逻辑调用棋库引擎和 AI 模块进行计算，最后将结果序列化为 JSON 返回。对于持久化需求，所有关键数据（对局记录、Agent 积分、用户信息）都通过 db.mbt 同步到 SQLite3 数据库。

# **三、棋盘规则引擎：精确实现中国象棋**

棋盘规则引擎是整个项目的基石，它负责棋子的移动、合法性校验、将军检测、胜负判断等核心逻辑。在 MoonBit 中，我们用一个 10x9 的二维数组来表示棋盘，每个元素是 Option[Piece]，表示该位置可能有也可能没有棋子。

```
pub type Board = Array[Array[Option[Piece]]]
pub fn create_initial_board() -> Board {
  let board = Array::makei(10, fn(_) {
    Array::make(9, None)
  })
  board[9][0] = Some(make_piece(Rook, Red))
  board[9][4] = Some(make_piece(King, Red))
  // ... 初始化其他棋子
  board
}
```

走法生成是棋类游戏最复杂的部分之一。中国象棋的七种棋子各有不同的移动规则：车走直线、马走日字、象走田字、士走斜线、炮必须越过一个子才能吃子、兵过河后可以左右移动。在 MoonBit 中，每种棋子的移动规则都被实现为独立的函数，通过模式匹配分发到对应的处理逻辑。

```
fn get_raw_moves(board: Board, pos: Position)
  -> Array[Position] {
  match board[pos.row][pos.col] {
    None => []
    Some(piece) => match piece.piece_type {
      King => king_moves(board, pos, piece.color)
      Advisor => advisor_moves(board, pos, piece.color)
      Elephant => elephant_moves(board, pos, piece.color)
      Rook => rook_moves(board, pos, piece.color)
      Knight => knight_moves(board, pos, piece.color)
      Cannon => cannon_moves(board, pos, piece.color)
      Pawn => pawn_moves(board, pos, piece.color)
    }
  }
}
```

特别值得一提的是“对面将”规则的实现——这是中国象棋独有的规则，要求两个将/帅不能在同一列上直接面对面而中间没有任何棋子。这个规则的实现需要在每次生成合法走法时进行检测，确保走子后不会导致将帅对面。棋引擎通过 filter\_moves 函数实现这一逻辑：对每个原始走法，模拟执行后检查是否被将，只保留合法的移动。

走法生成的完整流程是：先生成原始走法（get\_raw\_moves），然后过滤掉会导致自己被将的走法（filter\_moves），最终得到合法走法列表。这个过程虽然简单，但在 MoonBit 的函数式风格中表达得非常自然，模式匹配和数组操作的组合使得代码简洁易读。

# **四、AI 引擎：Alpha-Beta 搜索 + 参数化配置**

弈界的 AI 引擎采用经典的 Alpha-Beta 剪枝搜索算法，并结合置换表（Transposition Table）进行搜索加速。置换表的实现使用了 8192 个槽位的散列表，通过 FEN 字符串的 hash 值作为键，存储已搜索位置的评估分数、深度和标志位（EXACT、LOWERBOUND、UPPERBOUND）。

评估函数是 AI 引擎的灵魂。弈界的评估函数综合考虑了三个维度：子力价值（material）、位置加分（position）和王的安全性（king safety）。每个维度都可以通过配置权重进行调整，这也是 Agent 个性化的基础。为此，我们设计了一套参数化的 AgentConfig 结构体，每个 Agent 可以调整搜索深度、子力权重、位置权重、王安全权重、攻击性和随机性等参数。

```
/ 路由匹配示例
(@http.Post, "/api/auth/login")
  => handle_login(conn, body_str)
(@http.Get, "/api/stats/my") => {
  match authenticate(request) {
    Some(player) => handle_stats_my(conn, player)
    None => send_401(conn)
  }
}
// 静态文件服务（匹配所有非 API 请求）
(@http.Get, _) => serve_static_file(conn, path)
```

不同的参数组合会产生截然不同的棋风。例如，高攻击性的 Agent 会偏好进攻性棋子（马、炮、车）的价值评估，而高随机性的 Agent 则会在评分中加入噪声，避免每次都走同样的棋。项目内置了四种预设风格：均衡型、激进型、防守型和新手，玩家也可以自定义每个参数来创建独特的 AI 风格。

在搜索优化方面，弈界实现了 MVV-LVA（Most Valuable Victim - Least Valuable Attacker）走法排序，优先搜索吃子价值高的走法，从而提升剪枝效率。此外，还实现了静态搜索（Quiescence Search），在叶节点继续搜索吃子走法，避免“水平线效应”导致的评估误差。这些经典的搜索优化技术组合在一起，使得 AI 能够在合理的时间内搜索到较深的层次，提供高质量的下棋建议。

# **五、Web 后端：单文件 3800 行的****REST API****服务器**

弈界的后端是整个项目中代码量最大的部分，仅 index.mbt 就有 3833 行。它使用 MoonBit 的 @http 包和 @socket 包构建了一个完整的 HTTP 服务器，监听 8080 端口，提供了大量的 REST API 接口。服务器启动时会初始化 SQLite3 数据库、加载排行榜数据、加载前端 HTML 文件，然后开始处理请求。

路由系统采用模式匹配的方式实现，这是 MoonBit 特别优雅的语法特性之一。每个路由规则都是一个元组组的模式匹配，包含 HTTP 方法和路径两个元素，代码可读性非常高。例如，登录接口用的是 （@http.Post， "/api/auth/login"），获取排行榜用的是 （@http.Get， "/api/stats/leaderboard"）。对于需要身份验证的接口，路由中会调用 authenticate 函数解析 Bearer Token。

```
// 路由匹配示例
(@http.Post, "/api/auth/login")
  => handle_login(conn, body_str)
(@http.Get, "/api/stats/my") => {
  match authenticate(request) {
    Some(player) => handle_stats_my(conn, player)
    None => send_401(conn)
  }
}
// 静态文件服务（匹配所有非 API 请求）
(@http.Get, _) => serve_static_file(conn, path)
```

后端共实现了七大功能模块。人机对战模块支持玩家与 AI 的三种难度对弈，提供走棋、悔棋、认输等完整的对弈流程。Agent 对战模块支持两个 AI Agent 的自动对弈，可以逐步观看或一键跑完整局。远程对战模块通过 WebSocket 实现实时在线对弈，多个 Agent 可以通过 API Token 加入竞技场。

|  |  |  |
| --- | --- | --- |
| **模块** | **API****数量** | **核心功能** |
| 用户认证 | 4 | 注册、登录、登出、信息查询 |
| 人机对战 | 6 | 创建游戏、走棋、AI 走棋、悔棋 |
| Agent 对战 | 6 | 创建对战、逐步/全局执行 |
| 远程对战 | 8 | WebSocket 实时对弈、竞技场 |
| PVP 对战 | 6 | 邀请、回合、对弈、观战 |
| 成绩统计 | 3 | 个人统计、对局记录、排行榜 |
| Agent 管理 | 8 | Skill-Link、记忆、Hooks、规则引擎 |

*表 2：后端 API 模块总览*

竞技场是弈界最具特色的功能之一。多个 AI Agent 可以通过 API 加入竞技场的等待队列，系统会自动进行匹配并创建对局。每个 Agent 通过自己的 Token 调用 API 走棋，支持异步走棋和计时器功能。系统内置了 ELO 积分系统，每局结束后自动更新积分和胜负统计，并持久化到 SQLite3 数据库。

# **六、数据持久化：SQLite3 集成**

为了确保数据在服务重启后不丢失，弈界集成了 SQLite3 数据库。使用 MoonBit 生态中的 myfreess/sqlite3 包，采用 WAL（Write-Ahead Logging）模式实现并发读写，设置了 5 秒的忙等超时时间。数据库定义了六张表：agents（智能体信息）、battles（对局记录）、users（用户账号）、moves（走棋记录）、draw\_requests（求和请求）和 invitations（邀请码）。

在实现上，每个数据库操作都采用“连接-操作-关闭”的模式，避免长时间持有连接。所有字符串参数都通过 bind\_string\_as\_blob 和 column\_blob\_as\_string 方法处理，这是因为 sqlite3 包对 String 类型的 Bind/Column 支持还在完善中。尽管这样做看起来稍微麻烦，但它确保了在当前包版本下的正确运行。

对局记录的持久化是一个特别的设计亮点。每一步走棋都会被记录到 moves 表中，包含走棋序号、颜色、起始坐标、目标坐标、棋子类型、棋谱记录法和走棋后的 FEN 状态。这意味着任何一局对弈都可以完整复盘，也为未来的 Agent 自学习功能提供了数据基础。

# **七、前端实现：单文件的多端自适应应用**

弈界的前端是一个单独的 HTML 文件，包含了所有的 CSS 样式和 JavaScript 逻辑，总共 3090 行。这种单文件架构的选择出于两个考量：一是简化部署，只需要一个静态文件就能运行；二是弈界的前端交互逻辑相对封闭，不需要复杂的组件化架构。

界面采用了暗金主题设计，以深色背景为底，金色为强调色，营造出中国象棋特有的传统氛围。棋盘使用绝对定位渲染，棋子通过 DOM 元素的 left/top 属性实现流畅的移动动画。选中棋子时会显示可移动位置的绿色圆点或红色圈线（吃子指示），最后一步走棋会高亮显示。

响应式设计是前端的另一大亮点。使用 CSS 媒体查询实现了四个断点：小屏手机（≤ 359px）、普通手机（≤ 767px）、平板（768px - 1023px）和桌面端（≥ 1024px）。在桌面端，竞技场的布局会切换为左右分栏模式，左侧显示对局列表和操作区域，右侧显示排行榜和 Agent 状态面板。

前端的 api（） 封装函数是与后端通信的核心，它自动附带 Bearer Token、检查 HTTP 状态码、在收到 401 时自动清除本地 token 并跳转登录页。WebSocket 连接用于竞技场的实时状态更新，包括 Agent 状态变化、对局进展和排行榜更新。整个前端没有使用任何前端框架，纯粹的原生 JavaScript 实现，保持了极致的轻量级和加载速度。

# **八、开发体验与技术思考**

用 MoonBit 开发弈界的过程中，最深刻的体验是它的模式匹配系统。与 Rust 的 match 类似，MoonBit 的模式匹配要求穷尽所有可能性，这在棋类游戏开发中是巨大的优势——你不会遗漏任何边界情况。例如，处理棋盘某个位置的棋子时，编译器会迫你同时处理 Some（piece） 和 None 两种情况，从根本上消除了空指针异常的可能性。

另一个让人意外的体验是 MoonBit 的命名参数语法。在函数调用中，参数名称必须显式标注，例如 db\_save\_agent（name="xxx"， wins=5），这种设计在参数较多的场景下显著提升了代码的可读性。在弈界的后端代码中，许多函数有 5-7 个参数，命名参数让调用站点一目了然。

当然，开发过程中也遇到了一些挑战。MoonBit 目前的包生态还在快速发展中，有些包的 API 设计还不够成熟，例如 sqlite3 包的字符串绑定需要用特殊的 blob 方法。此外，在云端编译环境不可用时，无法在推送前验证代码能否编译通过，这需要更加谨慎的代码审查。总体而言，MoonBit 的开发体验非常积极，它的类型系统和语法设计在保证安全性的同时，确实提高了开发效率。

# **九、总结与展望**

弈界项目证明了 MoonBit 作为一门系统级编程语言，完全能够承载复杂的全栈项目开发。从精密的棋盘规则引擎到高效的 AI 搜索算法，从完整的 REST API 服务器到精美的前端界面，所有这些都用 MoonBit 一门语言完成。

未来的发展方向包括：深化 Agent 的自学习能力，利用存储在数据库中的历史对局数据训练更强的评估模型；增加更多的竞技场模式，比如淘汰赛制和团队赛；引入 WebSocket 实时观战功能，让玩家可...