---
title: 从命令注入到凭据泄露，手把手教你复现命令行工具高危漏洞
url: https://mp.weixin.qq.com/s/PX8h51A5vT8nglsayj0_tw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:02:55.989100
---

# 从命令注入到凭据泄露，手把手教你复现命令行工具高危漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/J2hBCjr4LftqFGm9iadGQ2fy7IMDFIIbfiatdJxVI0lCFibvHoQ6O0Wmn2PJaOzxVuPbmJqOiauvMKsPBednmmwzm9SnSDF9fLcnGicUVZuUzxRM/0?wx_fmt=jpeg)

# 从命令注入到凭据泄露，手把手教你复现命令行工具高危漏洞

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 从命令注入到凭据泄露，手把手教你复现命令行工具高危漏洞

在日常的安全测试中，大家往往把目光聚焦在 Web API、微服务或者移动端 App 上。然而，命令行客户端（CLI 工具）作为一个经常拥有本地高权限、直接与系统底层交互的组件，它的安全性往往被开发者所忽略。

很多研发同学想当然地认为：“CLI 是在用户本地运行的，能有什么安全问题？”

今天，我们就通过一次真实的 Go 语言 CLI 客户端安全测试实战，手把手带大家看一看 CLI 工具中常见的 3 个高危安全隐患，并分享如何编写 Go 单元测试与 Python Mock 服务进行白盒与黑盒复现。

---

## 一、本地凭据配置文件权限未收敛 (High)

### 1. 漏洞成因

许多 Go 开发者在写入本地配置文件（如 `~/.config/app.yaml`）时，习惯使用 Go 标准库的 `os.WriteFile(path, data, 0600)`，并认为这样就能保证文件只有当前用户可读写。

但是这里存在一个极其隐蔽的认知误区： 在 Go 语言（以及 Unix/Linux 文件系统行为）中，如果目标文件已经存在，`os.WriteFile` 会直接截断并写入数据，但绝不会去修改文件已有的权限属性。

如果恶意软件或用户自己先前以较宽松的权限（例如 `0644`，所有本地用户可读）创建了该文件，CLI 写入敏感的 Access Token 后，该文件依然会保持宽松权限，直接暴露给系统中的其他本地用户。

### 2. 漏洞代码示意

```
// 存在隐患的代码
func SaveConfig(path string, cfg Config) error {
    data, _ := yaml.Marshal(cfg)
    // 如果 config.yaml 之前存在且权限是 644，写入后它依然是 644
    return os.WriteFile(path, data, 0600)
}
```

### 3. 白盒复现测试代码

我们可以通过编写以下 Go 测试代码来复现这一机制。开发者可以将其直接跑在 Go 环境中：

```
func TestStoreSaveDoesNotRestrictExistingPermissions(t *testing.T) {
 t.Parallel()
// 在临时目录生成测试配置文件
 path := filepath.Join(t.TempDir(), "config_broad.yaml")

// 1. 模拟文件被预先创建，并赋予了宽松的 0644 权限（本地全员可读）
if err := os.WriteFile(path, []byte(""), 0644); err != nil {
  t.Fatalf("precreate failed: %v", err)
 }
if err := os.Chmod(path, 0644); err != nil {
  t.Fatalf("chmod failed: %v", err)
 }

// 2. 调用 CLI 内部的保存逻辑（内部使用 os.WriteFile 并传入 0600）
 store := NewStore(path)
 cfg := Config{ServerBaseURL: "https://example.com", AgentToken: "super_secret_token_123"}
if err := store.Save(cfg); err != nil {
  t.Fatalf("save failed: %v", err)
 }

// 3. 检查写入敏感凭据后的权限
 info, err := os.Stat(path)
if err != nil {
  t.Fatalf("stat failed: %v", err)
 }

if info.Mode().Perm() == 0644 {
  t.Log("漏洞验证成功：写入敏感 Token 后，文件权限依然维持宽松的 0644！")
 } elseif info.Mode().Perm() == 0600 {
  t.Fatal("权限已被强制收敛（正常安全逻辑）")
 }
}
```

运行该单元测试时的终端输出与漏洞确认截图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/J2hBCjr4Lfuohxq9QLhIql5KduN6ia37nLe6SlNAfyyliatMrQlpPEKkxmB5GibRibe9MruOdkyiawR9OPObibLfkGbjVbcoQy1kpjXaLboxrxkOM/640?wx_fmt=png&from=appmsg)

Go 单元测试确认权限未强制收敛

### 4. 修复方案

在写入文件后，必须显式调用 `os.Chmod` 来强制重置文件权限：

```
if err := os.WriteFile(s.path, data, 0600); err != nil {
    return err
}
return os.Chmod(s.path, 0600) // 显式强制将权限收敛至 0600
```

---

## 二、浏览器跳转未校验协议 (Medium/High)

### 1. 漏洞成因

许多 CLI 支持扫码或浏览器 OAuth 登录。CLI 通常会请求云端接口获取一个授权页面 URL，然后调用操作系统的“打开浏览器”接口：

* macOS: `exec.Command("open", rawURL)`
* Linux: `exec.Command("xdg-open", rawURL)`
* Windows: `exec.Command("rundll32", "url.dll,FileProtocolHandler", rawURL)`

安全隐患在于：如果 CLI 接收到服务端的 URL 后，未对其 Scheme (协议头) 进行任何校验，就会产生命令/参数注入。 在 macOS 上，`open` 命令可以直接用来启动应用程序或打开本地敏感文件；在 Windows 上，`FileProtocolHandler` 也是同理。如果返回的 URL 被伪造为 `file:///System/Applications/Calculator.app`，CLI 就会在本地拉起计算器。

### 2. 漏洞代码示意

```
// 存在隐患的代码
func OpenBrowser(rawURL string) error {
    var cmd *exec.Cmd
    switch runtime.GOOS {
    case "darwin":
        cmd = exec.Command("open", rawURL) // 未校验 rawURL 是否为 http/https
    // ... Windows 和 Linux 类似
    }
    return cmd.Start()
}
```

### 3. 真实二进制文件黑盒复现方法

如果 CLI 已经是编译好的黑盒二进制文件，我们不需要且无法修改其代码，但可以通过重定向服务端地址到本地 Mock 服务来完成复现：

1. **编写 Python 恶意 Mock 服务器 (`mock_server.py`)**：

```
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MockAuthServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # 匹配 CLI 请求获取授权链接的 API 路由
        if"/api/v1/auth/login/authorize-url"in self.path:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            # 返回伪造的 file:// 协议，指向 macOS 计算器
            payload = {
                "traceId": "mock-trace-id-123",
                "data": {
                    "authorizeUrl": "file:///System/Applications/Calculator.app"
                }
            }
            self.wfile.write(json.dumps(payload).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    print("恶意 Mock 服务已启动在 http://localhost:18080 ...")
    server = HTTPServer(("localhost", 18080), MockAuthServer)
    server.serve_forever()
```

2. **启动 Mock 服务器并执行 CLI 工具**：

```
# 启动 Mock 服务
python3 mock_server.py

# 运行已编译的 CLI 登录命令，将请求指向我们的本地 Mock 服务
./portal-cli login --base-url http://localhost:18080
```

运行及触发漏洞后的实际截图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J2hBCjr4LfvuZtNxWsfv7IhXo3j6gMVetLgmicBo5XgDFoaibszpIicmFghSu8KoXZzpbibTiaMIJmaSERffVO38A2o5a7bNQwFr1EAafCpqa0r8/640?wx_fmt=png&from=appmsg)

黑盒环境下命令执行触发计算器截图

在命令行敲击回车的一瞬间，二进制客户端向 Mock 服务端成功获取到了伪造协议链接。由于内部未校验 Scheme，macOS 系统在接收到指令后，瞬间弹出了本地的计算器界面。

### 4. 修复方案

在调用系统底层执行跳转前，使用 `net/url` 对协议头进行强校验，只允许 `http` 和 `https` 协议：

```
import "net/url"

func OpenBrowser(rawURL string) error {
    parsed, err := url.Parse(rawURL)
    if err != nil || (parsed.Scheme != "http" && parsed.Scheme != "https") {
        return fmt.Errorf("安全拒绝：非法的跳转协议头 %q", parsed.Scheme)
    }
    // 校验通过后，再调用系统的 exec.Command
```

---

## 三、敏感数据在控制台明文渲染泄露 (Medium/Low)

### 1. 漏洞成因

许多企业在设计安全红线时，要求“严禁在对话或终端历史中明文泄漏身份证号、手机号、家庭住址、银行卡号等敏感个人身份信息（PII）”。 但是在实现 CLI 时，开发人员常常贪图省事，把从后端 API 获取到的 JSON 数据，通过反射或字典遍历，直接生成 Markdown 树状表格输出到控制台。

这直接导致了研发设计与业务安全红线的背离： 在控制台明文打印敏感信息，不仅会导致本地日志泄露，更容易在现代“大模型 + AI Agent”协作编程的背景下，导致大模型直接将这些敏感信息收集并存储在会话历史或审计日志中。

### 2. 修复方案：脱敏拦截层 (Masking Layer)

在 CLI 的输出格式化组件（例如 Markdown 表格渲染器）中，引入脱敏拦截层。通过正则或字段名检测，将特定敏感字段（如 `id_card`、`phone`、`address` 等）进行打码掩码处理：

* 手机号脱敏：`13812345678` -> `138****5678`
* 身份证脱敏：`110101199003072345` -> `1101***********345`

---

## 四、总结

命令行工具（CLI）往往直接暴露在用户的本地系统上，其面临的本地特权攻击面与服务端/客户端信任链破坏的威胁不容小觑。

作为安全测试人员或研发人员，在面对 CLI 工具时，应重点关注：

1. 本地配置与凭据文件的严格读写权限强制控制（通过 `os.Chmod` 闭环）。
2. 所有调用系统原生命令（如 `open`、`rundll32`）的输入参数校验，严防任意协议跳转或命令注入。
3. 终端输出的敏感数据脱敏，遵循“最小化知悉”与数据合规原则。

希望这篇实战测试分享能帮大家在开发和测试命令行工具时少踩一些坑。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hHXiayYmia1LqLl6UmtMH3DtucaIaicr9HY5ffO5ckGVia3LvuCPCDNRNAX9fEmhicdmtRshennOyOqtPic6GTeASRNg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过