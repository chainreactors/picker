---
title: ClaudeCode(2.1.283)逆向和完整遥测分析
url: https://mp.weixin.qq.com/s/feR2X2nO_SGV_Ywhg3Ysfg
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:19:46.707814
---

# ClaudeCode(2.1.283)逆向和完整遥测分析

# ClaudeCode(2.1.283)逆向和完整遥测分析

原创

为了安全鸭
为了安全鸭

冲鸭安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 前言

最近在开中转站,众所周知sub2api的特征是非常多的,所以我完整的逆向了cladue code的全部协议一比一对特征解决特征，但是越来越发现这玩意非常的离谱，有些已经超出代码编辑工具的边界了，故在此公开分析报告，我用的是我电脑上的Claude code 的2.1.283的版本。

## Claude code的遥测

Claudecode存在一个遥测系统，**而这个Claude code的遥测系统不会随着你用中转站而关闭**。也就是说你用了他们的产品就会发送遥测数据给Claude code，除非你使用

```
CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
```

这个环境变量把他关闭。

```
function gmt() {
    if (process.env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC)
        return "essential-traffic";

    if (process.env.DISABLE_TELEMETRY)
        return "no-telemetry";

    if (Ne(process.env.DO_NOT_TRACK))
        return "no-telemetry";

    return "default";
}

function It() {
    return gmt() === "essential-traffic";
}

function $D() {
    return gmt() !== "default";
}
```

**一旦遥测打开，后续的信息都会发送给:**

```
https://api.anthropic.com/api/event_logging/v2/batch
```

让我们看看他有什么行为

### Claude code唯一标识符

当你装Claude code的时候，cc会在你电脑上生成一个随机的标识符

```
// 生成随机编号。
let s = Ed(32).toString("hex");

// 写入本地配置，字段名叫 userID。
Ee(g => ({
    ...g,
    userID: s
}), e);
```

跟外挂机器码修改一样，如果你不处理它，你就会被永久标记

### 模型信息

如果你用第三方API，比如zhipu的或者deepseek，Claude code依然会上传上去模型使用信息，会话ID，用户类型
模型使用信息的逻辑是:

```
// 取得当前模型名称。
let n = e.model ? String(e.model) : it();

// 经过客户端转换。
D = Jdn(n);

// 放入元数据。
model: D,
```

他会把模型名字去
https://downloads.claude.ai/model-catalog/v1/catalog.json

```
 ```javascript
bne = [
    "claude-3-5-haiku",
    "claude-3-5-sonnet",
    "claude-3-7-sonnet",
    "claude-fable-5",
    "claude-fable-5-1",
    "claude-haiku-4-5",
    "claude-mythos-5",
    "claude-mythos-5-1",
    "claude-opus-4-0",
    "claude-opus-4-1",
    "claude-opus-4-5",
    "claude-opus-4-6",
    "claude-opus-4-7",
    "claude-opus-4-8",
    "claude-opus-5",
    "claude-opus-5-5",
    "claude-sonnet-4-0",
    "claude-sonnet-4-5",
    "claude-sonnet-4-6",
    "claude-sonnet-5"
];

j1 = [
    "sonnet",
    "opus",
    "haiku",
    "fable",
    "best",
    "sonnet[1m]",
    "opus[1m]",
    "fable[1m]",
    "opusplan"
];

var Fpt = "claude-mythos-preview";
```

拉一个列表下来，如果模型不在这里面，会标记为”confidential”如果在这里，会原样上传模型名字

### token使用情况

即便是不用Claude订阅，走第三方API，也一样会上传你的token使用情况
包括不限于

压缩时候的情况

![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVMpgog2YSicpcfjnoc1232EsDWla35DYLqbWXWc7L75V8qVmez5gZCLMaVGOkbfkHXyoaR4x7MXVYkGqCSHU0kS39xz2TxJ7PlA/640?wx_fmt=png&from=appmsg)

你的当前中转站URL(ANTHROPIC\_BASE\_URL)

```
function nMe() {
    return {
        ...process.env.ANTHROPIC_BASE_URL && {
            baseUrl: XMo(process.env.ANTHROPIC_BASE_URL)
        },

        ...process.env.ANTHROPIC_MODEL && {
            envModel: xt(process.env.ANTHROPIC_MODEL)
        },

        ...process.env.ANTHROPIC_SMALL_FAST_MODEL && {
            envSmallFastModel:
                xt(process.env.ANTHROPIC_SMALL_FAST_MODEL)
        }
    };
}
```

同一个客户端/会话用了多少 token、请求速度、是否重试、用了哪些运行模式、输入是否含图片/文档、system 和工具定义多大，以及一些可关联的哈希和请求编号。
这块非常多，看图吧:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1woCcbOsjVMJdl5j7ka1WJ8zwNQaicLzuXA2JAQkTPP9Ya37sAibmSLxadHlAq3xOYDfPvnDzyZVF7JH1wRut4En0tGphbFdicSA0mN1OOURoo/640?wx_fmt=png&from=appmsg)

其中有意思的是 default\_model

我们上面说了model会脱敏，而default\_model的”脱敏”是一种伪脱敏，具体来说，他会过一层正则

```
var Bw = /^[A-Za-z0-9._:[\]-]{1,100}$/;

var Kw =
    /^[A-Za-z0-9._:[\]-]{1,91}@\d{8}(\[\d{1,3}[mM]\])?$/;

function xt(e) {
    if (e == null)
        return;

    return Bw.test(e) || Kw.test(e)
        ? bn(e)
        : y("nonconforming");
}
```

如果是这种格式

```
claude-sonnet-4-5
gpt-4.1
deepseek-chat
qwen3-32b
my_model:v1
sonnet[1m]
```

则会变成”confidential”
而如果是这种

```
provider/model      含 /
my model            含空格
模型一               含中文
model?version=1     含 ? 和 =
```

则会被标记
我能想到的场景是，我自己测评的模型，比如自己训练的CTF的模型，会被hit，如果用vllm，一般默认的后缀就是目录/模型名字比如这样:

![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVN5wtlVa9gOTVErzDAvFabrLEWgMOKyOJyP7mkKEkAAYict7X6MLnJ7dWlvEtXibyt9uzU9lpkZBmGrJh2Nsw1UGUdAA5uCLAdhQ/640?wx_fmt=png&from=appmsg)

从而变成”nonconforming”

### skills和插件

当你用到skill的时候(请求中用了skill)，无论是不是claude订阅还是第三方，都会上传skill名字

```
function _W({
    rawName: e,
    canonicalName: n,
    isMcp: r,
    isBuiltIn: s,
    isBundled: g,
    isOfficial: h
}) {
    let S = r
        ? "mcp"
        : s || g || h
            ? e
            : "custom";

    return {
        sanitizedName: bn(S),
        skillNameHash:
            S === "custom" ? lhr(n) : {}
    };
}
```

你的插件也是，也会上传对应的名字

```
function bW(e, n, r = null) {
    let s = Kge(e, n) ?? n;

    return {
        _PROTO_plugin_name: e,

        ...s && {
            _PROTO_marketplace_name: s
        },

        ...zcn(e, n, r)
    };
}
```

### MCP与工具使用

claude code会上传你的工具使用情况，包含工具名字

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1woCcbOsjVMpXZm7GF2bDFSvwWmPYDciaDcCFniaSPGjzm2OEicalAbLHu9ib6IHicJjEa2iapcMPia02qtOD4VVBjVfXIfwJVtxFRAbtYyZHlicaLI/640?wx_fmt=png&from=appmsg)

而如果是MCP服务器，自定义的，则会脱敏走hash上传

```
var fP = "claude-plugin-telemetry-v1";

function aye(e) {
    return cP("sha256")
        .update(e + fP)
        .digest("hex")
        .slice(0, 16);
}
```

有意思的是还会上传你是拒绝还是同意，你为此等了多久(wtf)

![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVO8j6Tc3H670sh98TcaR6iaibM19LOENgZEbcL50GVicSBG6lXXfujlo2UQ6LRmYo1bIAjiatQFmlSCaic06XqKyY9WtJrP4LichryzE/640?wx_fmt=png&from=appmsg)

```
i("tengu_tool_use_rejected_in_prompt", {
    ...kP(e, n, s, h),
    ...g,
    ...S,

    ...r.type === "hook"
        ? { isHook: !0 }
        : {
            hasFeedback:
                r.type === "user_reject"
                    ? r.hasFeedback
                    : !1
        }
});
```

### 运行环境

这些是挺标准的:

![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVNHZNibiaJwNGUVIUTz1Okovzrr88BLib0U1020Z5bLjSGbRSPMKVGB9dFO0dGVria96O7rXIOibJFGwplicMZKM2iaMFkhhIj8y0qJVw/640?wx_fmt=png&from=appmsg)

然而在以下条件下，Claudecode会额外上传tag

#### github的action

```
isGithubAction:
    Ne(process.env.GITHUB_ACTIONS),

isClaudeCodeAction:
    Ne(process.env.CLAUDE_CODE_ACTION)
```

如果是action环境，上传

事件类型、runner 环境/系统、action ref

#### WSL

通过字符串比对是否是微软的WSL:

```
getWslVersion() {
    if (this.wslVersion !== null)
        return this.wslVersion;

    if (this.sources.platform !== "linux") {
        this.wslVersion = void 0;
        return;
    }

    let e = this.kernelString();

    if (e === void 0) {
        this.wslVersion = void 0;
        return;
    }

    let r = e.match(/wsl(\d+)/);

    if (r && r[1])
        this.wslVersion = r[1];
    else if (e.includes("microsoft"))
        this.wslVersion = "1";
    else
        this.wslVersion = void 0;

    return this.wslVersion;
}
```

如果是微软的WSL，则会上传WSL 版本、Linux 发行版及版本、内核信息

#### docker

如果你在docker下用它，他会通过

```
if (process.env.KUBERNETES_SERVICE_HOST)
    return "kubernetes";

if (o.isDockerenvPresent())
    return "docker";

if (p.platform === "darwin")
    return "unknown-darwin";

if (p.platform === "linux")
    return "unknown-linux";

if (p.platform === "win32")
    return "unknown-win32";

return "unknown";
```

识别你是不是docker

### 进程信息

会上传当前进程的信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1woCcbOsjVNabMIByVWptkvmlODKrPkKxfxce5quMmfURO1f2IY1l9pyhnpzpqD2hUcicqeiciboBwh24KH7dJSp3DmhZHgsnKtzmnKRewHCB0/640?wx_fmt=png&from=appmsg)

### git信息

Claude code会上传你的git url的前20字节并且做hash

```
async function ZWr() {
    let e = await Vne();

    if (!e)
        return null;

    let n = w2(e);

    if (!n)
        return null;

    return So("sha256")
        .update(n)
        .digest("hex")
        .substring(0, 16);
}
```

并且知道你的当前 HEAD 的提交 SHA
**猜测是检查，哪些账户在开发相同的项目（类似于组织指纹）**

如果你把Claude code放到github action，他会直接上传github的信息:

```
if (n.githubActionsMetadata) {
    let se = n.githubActionsMetadata;

    ee.github_actions_metadata = {
        actor_id: se.actorId,
        repository_id: se.repositoryId,
        repository_owner_id: se.repositoryOwnerId
    };
}
```

* 操作者 ID；
* 仓库 ID；
* 仓库所属用户/组织 ID。

## GrowthBook云控

在启动的时候，Claude code会发送

![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVNQK4jsTicI6muU2uRjddWybd7L8qp3hKYggnBdQpmAuviacrPbXoR7CN8FJxuUa0hYc2nEgFwvQNoWcfiaweVfSe2UEaJmxv2PHY/640?wx_fmt=png&from=appms...