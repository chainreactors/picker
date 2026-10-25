---
title: ycb-web1手搓，剩下的没来得及只能放ai的了
url: https://mp.weixin.qq.com/s/qHCO4Dz77aSRz48fdUdjjA
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:07:43.743393
---

# ycb-web1手搓，剩下的没来得及只能放ai的了

# ycb-web1手搓，剩下的没来得及只能放ai的了

原创

識.
識.

0xNyx

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

拿到第一个web，是文本转换器。标题上写的是

Markdown to PDF converter

这个时候我们简单回顾一下相关的漏洞知识点

Markdown to PDF 转换器在 CTF 中是一个经典的攻击面，其核心风险在于**不可信的 Markdown 输入在服务端被渲染为 HTML，再交由浏览器引擎（如 Headless Chrome、wkhtmltopdf、WeasyPrint）或模板引擎处理。**

**这里毫无疑问，我们关注的重点一定是服务端的渲染引擎，和浏览器的处理引擎。**

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2e8b3KUYFdc8EhHWxz9AqdwIkHeibxhXLrrlsOYib6BVLBv7nLdiaCabvzSUibAwDTRRhY2KbKhkibulm3jodwNJCJ52j3c2Veib8CYo/640?wx_fmt=png&from=appmsg)

简单输入一些内容观察一波，收集信息

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2fGGiaqoo4RtGcOsgpoXVAUtj9aoFgu2OVpIm7SuyT0KMAGXDhu2icF2sQ7iajlVH9YtWCR6SPrFGibibYmaROMtBZXj3iaCBMk0cWmE/640?wx_fmt=png&from=appmsg)

抓包回显正常，没有看出问题

dirsearch扫一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2cbuKDG0c85iaE5DCaiaSIUtAol7qNA0yfjF9Ok0ldJkKqTBNZWMMfBqh5HDrAOWM7nPHsq24z5zQGKn1nn91l2icIAWhcJjVOIMg/640?wx_fmt=png&from=appmsg)

对 145 条常见路径做字典爆破，全部返回 404，确认应用仅存在 GET /与POST /render 两个入口，无 /admin、无源码泄露。

这就很麻烦了

（1）渲染结构：Markdown 围栏代码块的语法为 ```<info-string>，渲染器会将其输出为：

<divclass="cherry-code-block"data-lang="<info-string>">

<pre><code>...</code></pre>

</div>

（2）问题所在：data-lang 的属性值由字符串直接拼接生成，没有做 HTML 属性转义（未编码 " < > &）。

（3）利用思路：在 info-string 中使用 " 闭合属性值、使用 > 提前结束 div 标签，即可把任意 HTML 注入为真实 DOM 节点。（4）为什么需要 <x a=" 兜底：渲染器会在 data-lang 之后继续追加自身属性（class=... 以及收尾的 " 和 >），若不兜住，这些残留字符会落在注入的 iframe 之后破坏解析。因此在注入片段末尾再开一个接盘标签 <x a="，把后续属性全部吞进该属性中：

<divdata-lang=""><iframesrc="file:///flag"...><iframe><xa="class="cherry-codeblock"...>注入的真实元素.后续属性被吞入 a，不再破坏解析

步骤三：构造 payload

beforetext```"><iframesrc="file:///flag" style="width:100%;height:800px"></iframe><x a="code

```after text关键细节（实测差异）：代码块前后必须存在普通文本。若 Markdown 内容只有该代码块，整个 codeBlock 容器会被整体转义成源码文本，注入的 iframe 只是文本、不会成为真实元素；加入 before/after 普通文本后才正常渲染为元素。

步骤四：为什么 iframe 能读取 /flag

浏览器端 http(s) 页面加载 file:// iframe 会被同源策略拦截，但本题是服务端无头Firefox在渲染：渲染进程本身具备容器内文件系统读权限，且该配置允许 file:// 子框架加载；iframe将/flag作为纯文本页面渲染，page.pdf() 生成的 PDF 文本层即包含 flag 内容，只需做PDF 文本抽取即可获得。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2ez8Q9RianfGVmIdwWw9KOicEbUEk2ksYN9vzuvnqp4m5Jgy25icAjJLjb3hCpPDb9jesM55cmskvEko40TS9Te9B3NP2DNOORGSI/640?wx_fmt=png&from=appmsg)

(没搓完，主办方关了靶机)

#### 题目二名称：DataPulse（WEB / 500 分/ 困难/ 赛时41 解）

**【漏洞类型】**Webhook SSRF（字符串黑名单+ 协议白名单缺失）→ Redis 未授权→ Django Pickle 会话反序列化→ RCE → SUID 读flag

**【根因】**① retry-webhook 接受用户可控URL 且把目标响应整包回显，环回过滤只做字符串匹配；② 未限制gopher 协议；③ Redis 仅bind 127.0.0.1 且无认证，而SESSION正是存在这个Redis 里；④ SESSION\_SERIALIZER 为PickleSerializer，会话内容被服务端完全信任

**【利用要点】**http://127.1:8000/ 绕环回黑名单 → gopher://127.1:6379/\_<RESP> 打Redis → 覆写 :1:django.contrib.sessions.cache<sid> → 手工构造 posix.system的pickle → SUID /readflag

##### 步骤一：信息收集与接口枚举

（1）指纹：响应头Server: gunicorn，页脚DataPulse Analytics Platform v2.4.1，栈为Django + Celery + Redis 7.0.15。GET /api/v1/status/ 返回components 里的web/ task\_queue / cache 三块健康状态，其中cache 这条直接暴露了平台依赖缓存组件。

（2）注册与登录都是JSON 接口（页面没有传统form action）：POST /register/ 与POST/login/ 返回dp\_session（32 位hex）与api\_token，说明认证走的是「会话Cookie +API Token」双轨。

（3）从 Dashboard 前端JS 抽出全部业务接口：POST /tasks/create/、GET /tasks/list/、POST /tasks/<task\_id>/retry-webhook/、GET /tasks/<task\_id>/webhook-logs/。前三个决定了后续整条链。

（4）关键约束：retry-webhook 允许传{"url": "..."} 临时指定回调地址，但若建任务时webhook\_url 为空，接口一律返回{"error":"No webhook URL configured"}。所以「建任务时必须先给一个合法webhook」是后面所有SSRF 的前提。

##### 步骤二：把SSRF 从「能发请求」抬到「能读响应」

（1）retry-webhook 不只发请求，它把目标响应整包回显在 log.response\_body 里：{"message":"Webhook notification sent","log":{"status\_code":200,"response\_body":"<目标响应正文>"}}。这条回显就是本次的「数据出站通道」。

（2）环回黑名单绕过：直接打 127.0.0.1 / localhost / 0.0.0.0 / [::1] 全部返回{"error":"Invalid webhook URL"}，过滤是字符串黑名单，因此IPv4 的其它合法写法全部漏过——http://127.1:8000/api/v1/status/ 直接读回本机 JSON；2130706433、0x7f000001 同样可用。

（3）协议白名单缺失：gopher://127.1:6379/*PING%0D%0A 返回+PONG。gopher 的* 之后是原始TCP 载荷，%0D%0A 即CRLF，于是SSRF 升级成「任意本机TCP 明文协议客户端+ 响应回显」。

（4）踩坑：黑名单同样作用于gopher。第一版脚本用127.0.0.1 打6379，response\_body拿到空串，看起来像「6379 没开」，实际是URL 被拦。全链所有内部访问统一写127.1 之后才稳定。

##### 步骤三：打穿Redis（未授权），确认会话是Pickle

（1）指纹：gopher://127.1:6379/\_INFO%0D%0A 回 redis\_version:7.0.15、redis\_mode:standalone、process\_id:16、executable:/app/redis-server，全程无AUTH，命令直通；一次gopher 请求可带多条命令（同一连接顺序执行）。

（2）分库勘察：DB0 是 Celery 的 broker/result（celery-task-meta-*、\_kombu.binding.* ），无用； DB1 是 Django 会话库，键形如 :1:django.contrib.sessions.cache<32hex>，另有 fake\_admin\_session\_1/2 两个明显诱饵；DB2 为空。（3）Redis 没有HEXDUMP，用Lua 做十六进制编码读出会话值：

```
EVAL "local s=redis.call('GET',KEYS[1]); local h=''; for i=1,#s do
       h=h..string.format('%02x',string.byte(s,i)) end; return h" 1 <key>
--返回8004 95 ... 8c02 6e74 948c 0673 7973 7465 6d94 9394 ...
```

80 04 = Pickle protocol 4 魔数。由此得到三条结论：会话存 Redis、序列化器是PickleSerializer（不是默认JSONSerializer）、会话内容被服务端完全信任（登录态与角色都从里面取）。Redis 未授权⇒谁能写Redis，谁就能控制Django 反序列化的对象。

（4）非破坏性对照（这一步必须做，否则后面分不清「格式不对」还是「洞不通」）：把某个闲置会话改写成普通dict 的pickle（{"user\_id":1,"role":"analyst"}）写回，再带该Cookie 访问/dashboard/ 返回200；而不带Cookie 只有登录页。说明写入路径、键名、pickle 格式全部正确，且会话数据确实被业务直接使用。

##### 步骤四：Pickle 反序列化→ RCE

（1）第一个坑：GLOBAL 不能用 pickle.dumps(os.system)。在 Windows 上生成时os.system 的**module** 是nt，pickle 里写的是nt.system；目标Linux unpickle 需要import nt，直接ModuleNotFoundError，异常被Django 吞掉，表现成「投毒没生效」。改为手工拼Linux 的posix.system 字节，纯ASCII、无平台依赖：

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2dHu2kbyT0zqj9mcNHgviakJ5dQqtJWyyaOvppgZrxA6qA3nDHwKSm39g6Wp0Xy54jzsSKZFzclQN9Qh5zE5WodFiaSFtFd1lRJI/640?wx_fmt=png&from=appmsg)

（2）第二个坑：会话值是二进制，必须走RESP Bulk String（行内协议会被换行截断）。一次gopher 里发两条命令（同一TCP 连接）：

```
SELECT1
SET :1:django.contrib.sessions.cache<sid> <pickle_bytes>
RESP 编码：
*2\r\n$6\r\nSELECT\r\n$1\r\n1\r\n
*3\r\n$3\r\nSET\r\n$<len(key)>\r\n<key>\r\n$<len(val)>\r\n<val>\r\n
整段quote(payload, safe="") 后放进gopher://127.1:6379/_<encoded>，返回+OK / +OK
```

（3）触发：带被投毒的dp\_session 访问任何会加载会话的页面（如/dashboard/），返回HTTP 500 是预期现象——os.system 返回 int，Django 之后拿它当 dict 用才炸，而**reduce** 在unpickle 阶段已经执行完了。

（4）命令输出回取：容器里redis-cli 未必有，python3 一定有（Django 本体）。载荷里直接socket 连127.0.0.1:6379，把 /readflag 与id、ls -l 的输出base64 后SET进dp:flag；再用另一个「干净会话」发gopher SELECT 1 / GET dp:flag 取回。被投毒的会话不能复用，否则每次请求都会重复触发反序列化。

##### 步骤五：完整利用链与PoC

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2ePyBtPh2MbgVDTuCjB2LxSYykZOwBLibLAgzCtRbibaLGXpQDxooE2HMIicmM4Hic9BqA6wpvnryZZTbE6EYKVSib8gaT8NhkgE3AY/640?wx_fmt=png&from=appmsg)

#### 题目三名称：FluxPipe（WEB / 492 分/ 困难/ 赛时45 解）

**【漏洞类型】**信息泄露→ SQL 注入（Ecto 裸拼）→ 明文凭据→ 协议逆向（CRC 侧信道oracle）→ 代码执行（Elixir Code.eval\_string）

**【根因】**① /api/v1/health 无鉴权泄露内部拓扑（FPX 4001、EPMD 4369、distribution: enabled）；② /api/v1/pipelines/search 的status 参数直接字符串拼接进SQL；③ 应用以postgres 超级用户连库，可pg\_read\_binary\_file 读任意文件；④ FPX 会话密钥= sha256(erlang\_cookie)[:16]，而 cookie 明写在 /proc/<pid>/cmdline 的 -setcookie；⑤ FPX 的CRC 校验把「期望值」回显；⑥ cmd=4 直通Code.eval\_string 且进程root

**【利用要点】**报错回显拿列结构 → UNION 拖 users.api\_key（admin 明文）→/api/v1/auth 换 token → FPX 握手拿 nonce\_hint → 经 SQLi 读/proc/<beam>/cmdline 取-setcookie → FPX 帧（CRC oracle + XOR-Rotate）→ cmd=4→ /readflag

**【Flag】**DASCTF{47090164257494393148160049029890}

##### 步骤一：信息收集与路由枚举

（1）指纹：响应头 server: Cowboy，页脚 FluxPipe v0.9.3-beta • Powered by Elixir/BEAM • API docs at /api/v1/health。栈为 Elixir OTP 27 + Plug/Cowboy +Ecto + PostgreSQL 15.19。

（2）/api/v1/health 无鉴权，直接抖出内部拓扑：node fluxpipe@127.0.0.1、epmd\_port 4369、services.fpx\_protocol listening:4001、postgresql connected、distribution enabled、beam\_version 27。三个信息点定路线：有自定义二进制协议FPX（4001）、后端是PostgreSQL（SQLi 收益高）、BEAM 开了分布式且只需cookie 即可RCE。

（3）端口探测：目标只开了 Web 端口，4000/4001/4369/5432 全部 closed ⇒ FPX 与EPMD 只能在容器内部访问，必须先打 Web 面进去，再借应用自身去够它们（实际上/api/v1/fpx/\* 就是桥）。

（4）用 205 条字典过滤固定 21 字节的 {"error":"Not found"}，只剩三条活路：/api/v1/health 、 /api/v1/pipelines 、 /graphql ；再往下推一层命中/api/v1/pipelines/search（带status / q 参数）。/graphql 只回schema 骨架，是纯干扰项。

（5）/api/v1/pipelines 本体是固定5 条管道，加任何?status=/?id=/?q= 都不影响返回（列表写死），真正的查询在/search。教训：枚举要到「资源+ 动词」这一层，别停在资源层就下结论。

##### 步骤二：SQL 注入（status 参数）

（1）注入点确认：status=x' 直接把原句吐回来——Query error: ERROR 42601(syntax\_error) unterminated quoted string ... query: SELECT id, name, description, status FROM pipelines WHERE 1=1 AND stat...