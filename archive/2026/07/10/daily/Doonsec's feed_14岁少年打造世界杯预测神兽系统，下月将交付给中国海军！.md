---
title: 14岁少年打造世界杯预测神兽系统，下月将交付给中国海军！
url: https://mp.weixin.qq.com/s/-bog3pXHEmIjBhVlX2AYKw
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:00:25.111078
---

# 14岁少年打造世界杯预测神兽系统，下月将交付给中国海军！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpLJuTuIpgoD6MibpCwgB5BS8lFQZNf270Em9jJnLV3le1hDyeOokia0nb79SGCwFQVpkKCGkAqtRtXGbSXSyzsM7QmVbiaw5Kpibo/0?wx_fmt=jpeg)

# 14岁少年打造世界杯预测神兽系统，下月将交付给中国海军！

原创

佚名
佚名

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# ![二等奖](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQohHk0gjYeliciaVhibUXxGF8heY7vwtNagRaibMlktkQPbL8RFqZPDbLg0zqKOW2q0t4E0xmzdZLa2UBxqlZlVHLiauJEibicS6WIE9c/640?wx_fmt=webp&from=appmsg) 二等奖

在刚结束的哇为晟腾 Agent Hackathon 里，神兽世界杯预测系统拿到了二等奖和最佳人气奖，台前获奖的获奖选手是两位天才少年。原本这只是一个比赛结果，谈不上多么特别。真正让人感觉不对劲的，是答辩现场的一幕：评委追问到细节时，台前选手明显答不上来，随后其父亲曲植上台，直接接过话筒开始补充说明。也正是从这一刻起，问题不再只是这个项目拿了什么奖，而是这个项目到底是谁在做，到底做成了什么样。

完整视频和加速版见文末。

![神兽世界杯](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQqgZ0eYaLX8xTYxKSMj1cqTfCpQWYyJfjiazxEq4w3ADOfSUqo0wdGHUxzpeFIMLn7pXSuoIfNSYuyvFafciahr74LcSC3xbxmMQ/640?wx_fmt=webp&from=appmsg)

神兽世界杯

顺着这个问题往下翻，仓库和后面的官方群的聊天记录，几乎把答案自己交了出来。

## 一、从来没见过如此神的仓库

这个仓库给人的第一感觉，不是复杂，而是失控。代码、日志、任务单、设计稿、自述文案、运行残留、半成品脚本混在一起，看起来不像一个整理过的工程仓库，更像把开发机桌面整个打包上传了。工程不成熟很常见，但把工作台垃圾、未来设想和对外宣传揉成一坨再交出去，这就不是迭代快，而是连最基本的工程边界都没立住。

![主页](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQo59FTnDLzaxHFBlR2zu9FltqWyWI2JCAJRDiaKcwXBHHZBibibLsBstEiatcwmVs5EyUEVJ2UUcDTWqyLdRzW8yPU1LsrECLBusA0/640?wx_fmt=webp&from=appmsg)

主页

更难看的是，它不是单纯地乱，而是边乱边互相打脸。先看最基本的系统说明。`SYSTEM_INTRO.md:15-17` 里先说：

```
1. **不靠喂饭** — 我没有接入任何付费API，比分、赔率、情报都是白虎自己从网上扒的。爸爸相信"能搜到的就不要买"。
2. **不做单线程** — 我的预测不是一条Elo打天下。22个维度同时打架，蝴蝶效应动态补丁看心情激活。
3. **不准静止** — 每次启动我都要看自己变了什么。准确率掉了我会着急，会主动找原因。我有"好奇心引擎"，每天检查自己缺什么知识，然后想办法补上。
```

同一份说明在 `SYSTEM_INTRO.md:34` 和 `SYSTEM_INTRO.md:49-52` 又写成：

```
| **22维融合** | 球星因子、默契连线、DNA惯性、疲劳累积、替补深度、东道主环境、出线压力…… |
```

```
- **架构**: Flask + MySQL + Redis + 多Scale
- **服务器**: 阿里云 ECS (2核2G)，本地开发引擎 (localhost:19527)
- **数据源**: 全推接口 (3秒级市场数据), 公开网页抓取
- **核心模型**: Elo + 22维融合 + 5类蝴蝶效应 + 5层次情感分析
```

而 `README.md:19` 和 `README.md:94` 又是另一套口径：

```
> **五大神兽 · 23维融合 · 蝴蝶效应 · 自学习闭环**
```

```
- **DimensionBridge**：23维统一数据接口，每条修正带 value/confidence/source/raw
```

最后 `xuanwu/firo_tf_odds.py:31-35` 里又直接留下了第三方凭证入口：

```
FIROAPI_BASE = "https://www.firoapi.com"
FIROAPI_KEY = os.getenv("FIROAPI_KEY", "JqnnM33bLMGuCxEzafRpIguHQZaOtglY")
FIROAPI_PRIV_KEY_B64 = os.getenv(
    "FIROAPI_PRIV_KEY_B64",
    "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCMuS3ENY2KKHOgU"
```

一处写 22 维，一处写 23 维；一边说没有接入任何付费 API，一边又把第三方 API Key 和私钥直接写进仓库。连系统到底几维、数据到底怎么买、有没有外部付费源都说不清，后面那套大词堆起来的系统哲学，先天就已经打了折。

再看它最爱宣传的自学习闭环。`README.md:141` 写的是：

```
8步闭环，全程无人值守。AtomCode可执行文件路径通过 `config/charter.yaml` 中的 `agent_exe_path` 配置，默认搜索 `D:\qxh\atomcode-v4.25.0-windows-x64.exe`，也支持环境变量 `ATOMCODE_EXE_PATH` 注入。
```

而 `baihu/curiosity.py:30-35` 则是：

```
# ═══════════════════════════════════════════════════════════
# 自修改总开关 — 止血阶段物理关停
# 关停理由：准确率 55↔66 震荡未稳、无回归测试、无回滚机制。
#           在地基稳定前，神兽不具备修改自身代码的资格。
# 开启条件：settled 锁落地 + 回归测试绿 + 准确率方差 < 2pp（见 _止血_AFTER.json）
# ═══════════════════════════════════════════════════════════
SELF_MODIFY_ENABLED = False
```

这就很诚实了。文案在讲闭环、无人值守、自动修复，代码却直截了当地写着先别动，地基不稳，功能关停。**这不是能力已经跑起来，只是暂时收着不用；这是关键能力根本不敢开。**

最后再看它对外讲的跨平台和零依赖。`README.md:31` 先写：

```
神兽世界杯的预测引擎（约 7 万行 Python 代码）为**纯 CPU 计算**，不依赖任何 GPU/NPU 加速框架。数值计算主要使用 Python 标准库 `math`，无 CUDA/PyTorch/TensorFlow 依赖。**任何配备 Python 3.8+ 的 ARM/x86 Linux/Windows 环境均可直接运行，包括华为昇腾、鲲鹏等国产芯片。**
```

但 `README.md:243-244` 的安装说明只有：

```
- Python 3.8+
- 依赖：`pip install flask flask-cors tinydb`
```

而 `requirements.txt:1-8` 实际上是：

```
# 神兽世界杯 v1.0 - 混沌与真实预测系统
# Python 3.8+ | 零外部ML依赖，纯数学计算

# 核心（必须）
numpy>=1.21.0

# 工具
psutil>=5.9.0
```

更别提 `watchdog.py:67-68` 和 `watchdog.py:88-101` 还直接写死了 Windows 命令和路径：

```
        subprocess.run(f'taskkill /f /im "{name_pattern}"', shell=True,
                       capture_output=True, timeout=10)
```

```
            subprocess.run('taskkill /f /fi "WINDOWTITLE eq server*"', shell=True,
                           capture_output=True, timeout=10)
        except:
            pass
        # Also kill any python running server.py
        try:
            subprocess.run('wmic process where "name=\'python.exe\' and commandline like \'%%server.py%%\'" delete',
                           shell=True, capture_output=True, timeout=10)
        except:
            pass
        time.sleep(2)
        # Start server
        os.chdir('D:/神兽世界杯')
        subprocess.Popen(['python', 'server.py'], shell=True)
```

一边说 ARM、x86、Linux、Windows 都能直接跑，一边守护逻辑硬编码 `taskkill`、`wmic`、`D:/神兽世界杯` 这种纯 Windows 路径和命令；一边在 README 里写手工安装 `flask`、`flask-cors`、`tinydb`，一边 `requirements.txt` 里只有 `numpy` 和 `psutil`。这已经不是宣传写得夸张一点，而是系统状态、依赖清单、运行前提和部署环境压根没对齐。说得更直白一点，这不像一个跨平台工程，更像一套只在作者那台 Windows 机器上勉强跑过、然后硬往外讲成通用架构的东西。

![多平台](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQoZh4YTfUzEyKUKXkpZJROCya6ZLTkbjk08LgqwU5JbeC8Cqib1Ej3fiaTIicYT113mjibWemThq0RDqwh18Kliaohr42lpIInUjx1A/640?wx_fmt=webp&from=appmsg)

多平台

所以第一眼的不对劲，不只是仓库乱，而是**乱得没有边界，吹得没有刹车，文案、代码和运行现实还经常彼此冲突**。一个项目如果连自己现在是什么状态都说不清，那它最该做的不是继续抬系统级叙事，而是先把最基本的工程诚实补上。

## 二、一轮代码审计，一键getshell

如果前面那些还能解释成比赛项目赶时间、工程卫生一般，那么再往下看，问题就已经不是乱，而是危险。由于技术有限（实际上是懒得运行这坨代码），下面只列代码层面能够直接确定的部分漏洞。

### 高危问题一：`/api/tools/call` 这条链，本质上是浏览器可利用的 localhost 命令执行面

第一条在 `server.py:633-635,8232-8246,8256`。服务全局开了 `CORS(app)`，暴露了一个未认证的 `/api/tools/call`，接口允许 `bash`，而所谓的安全检查却只盯着文件路径，对 `bash` 完全无效。

```
app = Flask(__name__)

CORS(app)  # 允许跨域请求，供前端驾驶舱使用
```

```
    valid_actions = {"bash", "read_file", "write_file", "edit_file", "list_directory", "grep", "glob"}

    if action notin valid_actions:

        return jsonify({"code": -1, "msg": f"不支持的工具: {action}，支持: {', '.join(sorted(valid_actions))}"}), 400

    # 安全检查：禁止读写系统敏感路径

    sensitive = ["/etc/", "/.ssh/", "\\etc\\", "\\.ssh\\"]

    if action == "read_file"or action == "write_file"or action == "edit_file":

        fp = params.get("file_path", params.get("path", ""))
```

```
    result = _mcp_bridge_call(action, params, timeout)
```

这段代码真正的问题，不在于它监听的是 localhost，而恰恰在于很多人会误以为监听 localhost 就天然安全。全局 CORS 一开，恶意网页完全可以借浏览器跨域访问本地服务；接口又明确允许 `bash`，那这条链本质上就是浏览器可利用的 localhost 命令执行面。

### 高危问题二：`/execute` 提供了第二条独立的本地命令执行链

第二条在 `mcp_bridge/atomcode_api.py:15-18,277-287,460-469,478-480`，更直接。

```
接口：
  POST /execute   {"action": "...", "params": {...}}
                  -> {"code": 0, "data": {...}}
                  -> {"code": 1, "error": "..."}
```

```
def tool_bash(params: dict) -> dict:
    command = params["command"]
    timeout = int(params.get("timeout", DEFAULT_BASH_TIMEOUT))
    timeout = min(max(timeout, 1), MAX_BASH_TIMEOUT)
    cwd = params.get("cwd") or None
    # 与 PS Worker 一致：cmd.exe /c
    try:
        proc = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
```

```
@app.route("/execute", methods=["POST"])
def execute():
    try:
        payload = request.get_json(force=True, silent=False)
    except Exception as e:
        return jsonify({"code": 1, "error": f"invalid JSON body: {e}"}), 400
    if not isinstance(payload, dict):
        return jsonify({"code": 1, "error": "body must be a JSON object"}), 400
    action = payload.get("action")
    params = payload.get("params", {})
```

```
        data = _run_action(action, params)
        dur = int((time.time() - t0) * 1000)
```

这已经不是留下了一个小口子，而是压根没把边界立起来。一个项目同时存在两条独立的本地命令执行链，本身就足够说明问题了。

### 高危问题三：硬编码 API Key、内嵌私钥，仓库里直接留凭证

继续翻，在 `xuanwu/firo_tf_odds.py:31-35` 和 `xuanwu/calibrate_pinnacle.py:42-65` 还能看到明文 API Key 和内嵌私钥。

```
FIROAPI_BASE = "https://www.firoapi.com"
FIROAPI_KEY = os.getenv("FIROAPI_KEY", "JqnnM33bLMGuCxEzafRpIguHQZaOtglY")
FIROAPI_PRIV_KEY_B64 = os.getenv(
    "FIROAPI_PRIV_KEY_B64",
    "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCMuS3ENY2KKHOgU"
```

```
FIROAPI_KEY = os.getenv("FIROAPI_KEY", "JqnnM33bLMGuCxEzafRpIguHQZaOtglY")
FIROAPI_PRIV_KEY_B64 = os.getenv("FIROAPI_PRIV_KEY_B64", "")
FIROAPI_BASE = "https://www.firoapi.com"
```

```
    if not priv_b64:
        # 使用内嵌私钥（仅开发/演示；生产应走环境变量）
        priv_b64 = (
            "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCMuS3ENY2KKHOgU"
            "/uWp/kNvOGqh7RZoFsRfXC8B9UVm/il9d/nSKuQ2kCqa4n1HSd4bFFO2...