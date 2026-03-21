---
title: 一款开源AI MCP框架原理分析
url: https://mp.weixin.qq.com/s/1-Bcq3N5wPUgTqvZIb1IOg
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:00:21.069277
---

# 一款开源AI MCP框架原理分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icCLY10D8tvLPu6nO6oEF7Jk5p5SqO3RfQJgibibDzYg6v8KSPuYApXwDiaHcDIkibUfBxK7PodqFUydhP6hGGAJKibmgNVK8ZP1gGicHWBWbgpwk0/0?wx_fmt=jpeg)

# 一款开源AI MCP框架原理分析

小叶Sec

![]()

在小说阅读器中沉浸阅读

以下文章来源于好靶场
，作者小王

![](http://wx.qlogo.cn/mmhead/XYrRG5UShDc8MiasaqKIRuv8ygOQeco20z91bZzqSptr4yT8nEmmLBzdFCY6BRHg3fKmcfiafia6cg/0)

**好靶场**
.

学安全要练习，练习就选好靶场。我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。

58.5

💡 好靶场

团队宗旨：我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。所以我们团队名称就叫“好靶场”。

我们承诺每天至少更新1-2个新靶场。我们追求的是稳定日常更新而不仅仅是数量。

* • 全球第一家以SRC报告为蓝图制作靶场的网络安全靶场平台。
* • 全球第一家引入AI靶场助教的网络安全靶场平台。
* • 14个不同方向靶场供你选择。
* • 代码审计+漏洞修复靶场全新上架。

* • 无门槛费，每次开启不扣除积分，不扣除金币，超级会员每天不限次数开启靶场。
* • 靶场独立，每个靶场环境完全隔离。

# 好靶场目前进度

774

靶场数量

209个

漏洞报告数量

#

* # 0x00 前言

  首发先知社区。
* 本文主要是针对一款开源AI MCP框架的原理进行分析，看看其中的实现逻辑。

  最近看到OpenClaw特别火，所以抽出一些时间用来研究相关的东西，也不用特别神化这个东西，就是一个调度器，用Claude调度反而更快。

  简单的看一下，AI，Skills，以及MCP的关系。
* ![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJ0I7vVibtZShDh0cMiafuFVTQo4hX6picpGVjdg2W9icibV4IAASCHpg4x4DoibQlyA5QBE7GlCb7O4Ulenul3vrcibmH6VhK3dJLiawY/640?wx_fmt=png&from=appmsg)

* ## Skills

  AI使用的SOP文档，第一步干嘛，第二步干嘛...

  ## MCP

  AI可以使用的工具，比如你的任务拆解出来，需要计算1+1的结果，AI自己就处理了，但是如果是一个更难的问题，虽然他也能做，但是会很慢，以及会出错，所以他需要一个专业的工具，给他确切的结果。

  eg：

  你让他解码一个Base64，他拿到这个任务，拆解为：

  所以如何把之前人调度的脚本，现在通过一种标准的方式，让AI可以进行调度，就是一个需要解决的问题。

  # 0x01 MCP框架拆解

  项目地址：https://github.com/haobachang-1/HBC\_SEC\_MCP

  > HBC\_SEC\_MCP 是一个安全工具网关，将传统命令行安全工具包装为现代化的 MCP 服务。它实现了 MCP JSON-RPC 2.0 协议，让 AI 客户端能够以标准化的方式发现并调用安全测试能力。

  ## 核心技术栈

  ## 配置说明

  编辑 `app/config.py` 修改服务配置：

  ## 依赖要求

  看了代码之后，发现这个工具最根本的理念是，让安全人员或者工具编写人员，不再关注MCP的格式和调用方法，只通过一个Model就可以编写工具供AI进行调用。

  ## 调用逻辑图

+ • Python 3.8+
+ • Flask >= 3.0.0
+ • requests >= 2.31.0
+ • mcp >= 1.0.0

+ • `API_PORT` - 服务监听端口（默认：5000）
+ • `DEBUG_MODE` - 调试模式开关
+ • `TOOL_SQLMAP_SCAN` - SQLMap 工具名称常量

+ • **Flask** - Web 服务框架，提供 HTTP API
+ • **MCP Protocol** - Model Context Protocol 协议实现
+ • **SQLMap** - 集成 SQL 注入检测工具
+ • **Python 3** - 主要开发语言

+ • 你给我的是不是Base64。
+ • 如果是，我需要解开他。
+ • 有Base64解码工具，我直接调用。
+ • 如果没有，我就只能自己通过Base64的原理计算了。

* ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvK3d3FFSn6Bgg4Y5GWpvib9tDgrWLCeN74JhVPM8kspIOOD6BCAQPqpObscKN5IM0v8z6p24piactacGsI6b2I86gorG7Hick6mCE/640?wx_fmt=png&from=appmsg)

  ##

  ## 目录结构

  ```
  HBC_SEC_MCP/
  ├── server.py              # Flask 服务主入口
  ├── requirements.txt       # 项目依赖
  ├── .gitignore            # Git 忽略规则
  ├── README.md            # 项目说明文档
  ├── app/
  │   ├── __init__.py
  │   ├── config.py          # 配置常量
  │   ├── mcp_protocol.py    # MCP 协议实现
  │   ├── tool_dispatcher.py # 工具调度器
  │   ├── command_executor.py # 命令执行封装
  │   ├── logging_setup.py   # 日志配置
  │   └── tools/
  │       ├── __init__.py
  │       ├── base_tool.py       # 工具基类
  │       ├── sqlmap_tool.py     # SQLMap 集成
  │       ├── command_exec_tool.py # 命令执行工具
  │       └── _tool_template.py  # 新工具开发模板
  └── log/                   # 运行日志目录
  ```

  ## Server.py 调用逻辑

  可以看到这里通过`/mcp/capabilities`获取所有的能力，并且通过动态列表拉取的方式，通过Tools获取到了工具列表。
* ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLkicppWMDOGwdRP0AxYHMx9nwldtH52jbyYg5PGjibHLEsBiciaJ1DN8CFDb8u1NorpYJq4jaReP5kQ3nBjDZ9Qf7nnAkABT5Zxn8/640?wx_fmt=png&from=appmsg)

* 这里我们跟进一下工具获取的方法，可以看到有一个基础工具，可以通过指定的路径来读取到所有的文件，并且动态的进行注册
* ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvIF3p1f0AQicr0ibUeZV8SksVkgsE4ibUeniaarJSrZ5dicRWiasoJqibZtDseNOtESaKf4ajme1J9Ff3lqYpdkjNEO3CibRejpW0aLnoM/640?wx_fmt=png&from=appmsg)

* ## Tools动态注册

  在Tools文件夹里找到了一个基础的工具类，这个工具类包含了工具名字和描述，这里的描述是为了给AI进行提示和说明的，你说的越清楚，AI约了解这个工具，当然你也可以通过Skills进行约束。

  ```
  from typing import Any, Dict, Optional, Tuple

  from .base_tool import BaseTool

  class XxxTool(BaseTool):
      """Template tool: copy this file and rename class/module for a new tool."""

      # Tool unique name used by MCP tools/call and HTTP dispatcher.
      name = "xxx_tool"

      # Tool description shown in tools/list.
      description = "Run xxx tool."

      # MCP input schema for this tool.
      input_schema = {
          "type": "object",
          "properties": {
              "target": {"type": "string"},
              "additional_args": {"type": "string"},
          },
          "required": ["target"],
      }

      @staticmethod
      def _parse_params(params: Dict[str, Any]) -> Tuple[Optional[Dict[str, str]], Optional[str]]:
          target = str(params.get("target", "")).strip()
          if not target:
              return None, "target is required"

          normalized = {
              "target": target,
              "additional_args": str(params.get("additional_args", "")).strip(),
          }
          return normalized, None

      @staticmethod
      def _build_command(target: str, additional_args: str = "") -> str:
          command = f"echo running xxx for {target}"
          if additional_args:
              command += f" {additional_args}"
          return command

      def run(self, params: Dict[str, Any]) -> Dict[str, Any]:
          normalized, error = self._parse_params(params)
          if error:
              return {"error": error, "success": False}

          command = self._build_command(
              target=normalized["target"],
              additional_args=normalized["additional_args"],
          )

          # Replace this mock response with real execution logic.
          return {
              "success": True,
              "message": "Template tool executed",
              "command": command,
          }
  ```

  然后就是run方法，在run方法里提供了一个可以自己进行控制的内容，所有的工具调度都可以自行在这里实现。查看了一下MCP自带的工具，使用的是`execute_command`方法
* ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvJ1Vg6ytbrfnGJmI06mbpT5hlMZoLuIPnhNjQ3GmLJGKzuHoBwzNAib3zBlGuIEl7c1URlboBZvwITEv0poHNcSCRHtDuha8ZOk/640?wx_fmt=png&from=appmsg)

* 继续向下追溯，可以看到最终在这里执行了系统命令，然后按照如下格式进行返回，

  ```
  return {
    "stdout": self.stdout_data,
   "stderr": self.stderr_data,
   "return_code": self.return_code,
   "success": success,
   "timed_out": self.timed_out,
   "partial_results": partial_results,
  }
  ```

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvIVAUay0dricYDCpfD96GQnPyzSicVJxHmtbmRVgzxyjSfcbw9FyZsUERYI9bwuOjaqIibMC41wEiaI87nSYqp3BjyLbicHJyBibG3ib4/640?wx_fmt=png&from=appmsg)

* 其他的就是一些自动扫描一类的东西，可以自由编写自己的工具进行封装。在mcp\_protocol.py里，还发现除了支持http的调用以外，还支持标准的MCP协议进行连接。

  ```
  import json
  from typing import Any, Dict

  from .config import MCP_PROTOCOL_VERSION

  def mcp_success_response(req_id: Any, result: Dict[str, Any]) -> Dict[str, Any]:
      return {"jsonrpc": "2.0", "id": req_id, "result": result}

  def mcp_error_response(req_id: Any, code: int, message: str) -> Dict[str, Any]:
      return {"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}}

  def handle_mcp_method(req_id: Any, method: str, params: Dict[str, Any], execute_named_tool, tools_catalog):
      if method == "initialize":
          return mcp_success_response(
              req_id,
              {
                  "protocolVersion": MCP_PROTOCOL_VERSION,
                  "capabilities": {"tools": {"listChanged": False}},
                  "serverInfo": {"name": "kali-mcp-http", "version": "1.0.0"},
              },
          ), 200

      if method == "notifications/initialized":
          return None, 204

      if method == "ping":
          return mcp_success_response(req_id, {}), 200

      if method == "tools/list":
          return mcp_success_response(req_id, {"tools": tools_catalog()}), 200

      if method == "tools/call":
          tool_name = params.get("name", "")
          arguments = params.get("arguments", {}) or {}
          if not tool_name:
              return mcp_error_response(req_id, -32602, "Missing tool name"), 400

          tool_result = execute_named_tool(tool_name, arguments)
          is_error = bool(tool_result.get("error"))
          text_result = json.dumps(tool_result, ensure_ascii=False)
          return (
              mcp_success_response(
                  req_id,
                  {
                      ...