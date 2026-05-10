---
title: 【Atract:安全运营平台】 01：登录模块安全自查清单：你中了几个？
url: https://mp.weixin.qq.com/s/JuYxvrxRlZgOoSVlb83nzQ
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:33:26.045204
---

# 【Atract:安全运营平台】 01：登录模块安全自查清单：你中了几个？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kQTEwQUIic2djt0RgOcgXpJOR69BQx8f2npqf23haFXF3UFSb09XFsrQCFHCRD0ibIc96M1lFicKNco0cIFLWibMlMM3BibiafLevKaAETeKZeFQU/0?wx_fmt=jpeg)

# 【Atract:安全运营平台】 01：登录模块安全自查清单：你中了几个？

原创

cjstang
cjstang

新安集

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**友情提醒**

**本文阅读时间推荐：5 min**

![图片](https://mmbiz.qpic.cn/mmbiz_png/YUyZ7AOL3onRYF83yUDYSe4PcKQr8aLwK5X5M3xjVfcAicDhshtFSa17W6HVLaLXvhQ9ExaAiaqdyDqLHYrx7N6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

如想讨论

以下内容

▼

欢迎关注公众号联系我哟

▼

**\*CISP-TRS（威胁响应专家  - 备考中）\***

**\*OSCP+备考经验（已通过认证）\***

**CISSP备考经验（已通过认证）**

**CCSK（云安全）（已通过认证）**

**ISO/IEC 27001 Foundation（已通过认证）**

序

写在前面

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWg53p5nsEnjKGS4ZibH00kIAHnOxhaUdBBhvJVO3Qt3t7Sq8DqVC5ib4pgxSMiaAdictmsDpVicC0U18VA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

| 一个安全运营平台，如果连登录都不可信，后面的一切都是假的。

如前面文章所说，历史小半年，从零开发了一套**内部安全运营平台**，边写边踩坑，边踩边思考：**每一行代码，在攻击者眼里意味着什么？**

在开源出来之前，我想记录一下每个功能的设计，索性记录成一个系列以供大家交流，这个系列不讲大道理，我会**直接贴代码 + 讲安全设计**，希望能向各位专职开发或者做安全开发的前辈取取经。

![](https://mmbiz.qpic.cn/mmbiz_png/kQTEwQUIic2dl1IUIv4ubS8vcq9VOkCWMp2FTswLjLR5WDd9UlcC8FcLicMw27OqnjNyaagGMmGWGMibd6nNnlAPicicrXNAy8EeNQRqqibSnLxlA/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fkFT2nlsyDbboLesmpvuGKMP0qVNJqgEJUMLbsQ6ZfLC8WS6dlp6RBkJ5ksqNo5pLJBwChxLXw8ib3g3HZICSte2NxJ885maQc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

**{一、一个登录模块，需要防什么？}**

很多人觉得登录就是：输入账号密码 → 验证 → 跳转。

但在安全场景下，你需要面对：

| 攻击方式 | 真实威胁 |
| --- | --- |
| 暴力破解 | 脚本无限尝试弱口令 |
| 撞库 | 用泄露的密码库批量测试 |
| Session劫持 | 窃取登录态 |
| 验证码绕过 | 自动化工具无视验证码 |
| 账号锁定后绕过 | 业务逻辑缺陷 |

所以，**一个"安全"的登录模块，本质是第一道防火墙**。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fkFT2nlsyDbboLesmpvuGKMP0qVNJqgEJUMLbsQ6ZfLC8WS6dlp6RBkJ5ksqNo5pLJBwChxLXw8ib3g3HZICSte2NxJ885maQc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

**{二、代码实现：我是这样写登录}**

| 以下是我平台 `soc01/views/login.py` 的核心代码（已简化展示，保留安全关键点）

### 2.1 验证码：拒绝自动化攻击

```
python
from soc01.utils.captcha import Captcha
captcha_code = request.POST.get('captcha_code', '').strip()session_captcha = request.session.get('captcha_code', '')
if not captcha_code:    error = '请输入验证码！'elif not Captcha().verify(captcha_code, session_captcha):    error = '验证码错误，请重新输入！'
```

**安全设计点**：

* 验证码与 Session 绑定，不靠前端校验
* 验证后立即清除 Session 中的验证码，防止重放
* 登录失败时**强制刷新验证码**，不给脚本机会

> 💡 一个小细节：`captcha_timestamp = int(datetime.now().timestamp())` 传给前端，强制浏览器重新请求验证码，避免旧验证码被复用。

---

### 2.2 密码：永远不存明文

```
python
from django.contrib.auth.hashers import check_password
if check_password(password, user_obj.password):    login_success = True
```

**安全设计点**：

* 存储用 `make_password` 哈希加盐（**PBKDF2**）
* 比对用 `check_password`，不自己写算法
* **日志里绝不打印密码原文**（哪怕调试）

> 很多泄露事故，源头是 debug 日志里打印了 `password=123456`。

---

### 2.3 Session：控制凭证生命周期

```
python
request.session['user_info'] = {    'id': user_obj.id,    'account': user_obj.account,    'uname': user_obj.uname,    'roles': roles_info,}request.session.set_expiry(7200)  # 2小时过期
```

**安全设计点**：

* 明确 Session 过期时间（2小时）
* 登出时 `session.clear()`，彻底销毁
* Session 中只存**必要信息**，不存密码等敏感字段

> 登录成功后立即 `pop('captcha_code')`，避免验证码残留被滥用。

---

### 2.4 登录拦截装饰器：统一鉴权

```
python
def login_required(view_func):    def wrapper(request, *args, **kwargs):        if not request.session.get('user_info'):            messages.warning(request, '请先登录后再操作！')            return redirect('/login/')        return view_func(request, *args, **kwargs)    return wrapper
```

**使用方式**：

```
python
@login_requireddef dashboard(request):    ...
```

**安全设计点**：

* 全局复用，避免遗漏
* 未登录直接重定向，不暴露任何业务数据
* 可扩展：后续可加 IP、User-Agent 二次校验

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fkFT2nlsyDbboLesmpvuGKMP0qVNJqgEJUMLbsQ6ZfLC8WS6dlp6RBkJ5ksqNo5pLJBwChxLXw8ib3g3HZICSte2NxJ885maQc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

**{三、多角色支持：权限前置设计}**

在登录阶段就注入角色信息：

```
python
roles_info = []for role in user_obj.roles.all():    roles_info.append({        'role_id': role.id,        'role_identifier': role.identifier,  # admin / operator / auditor        'role_name': role.name    })request.session['user_info']['roles'] = roles_info
```

**安全设计点**：

* ```
  登录时加载 ≠ 只依赖登录时加载：Session 存权限用于前端性能优化，真正的权限校验在装饰器中实时查库，性能和安全性兼得
  ```
* 支持多角色并存（比如：知识库管理员 + 大黑阔（漏洞提交人）等）
* 为后续 `@require_permission` 装饰器打下基础，前端用 Session 控制菜单显隐，后端用数据库实时判断，两层分离，互不信任

> 记住一句话：**前端权限是用户体验，后端权限是安全红线。**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fkFT2nlsyDbboLesmpvuGKMP0qVNJqgEJUMLbsQ6ZfLC8WS6dlp6RBkJ5ksqNo5pLJBwChxLXw8ib3g3HZICSte2NxJ885maQc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

**{四、登出：不是“关掉浏览器”那么简单}**

```
python
def logout(request):    request.session.clear()    messages.success(request, '已成功退出登录！')    return redirect('/login/')
```

**常见错误**：

* 只删前端 Cookie，后端 Session 仍有效 → Session 可被重放
* 没有清空服务端 Session → 占用存储 + 安全隐患

**正确做法**：

* 服务端 `clear()` 或 `flush()`
* 客户端清除 Cookie（Django 默认行为）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fkFT2nlsyDbboLesmpvuGKMP0qVNJqgEJUMLbsQ6ZfLC8WS6dlp6RBkJ5ksqNo5pLJBwChxLXw8ib3g3HZICSte2NxJ885maQc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

**{五、安全开发三板斧（本期敲重点）}**

| 斧头 | 对应设计 |
| --- | --- |
| **永远不相信用户输入** | 验证码、参数 strip、空值校验 |
| **永远保护凭证生命周期** | Session 过期、登出销毁、验证码一次性 |
| **永远为审计留痕** | 记录登录时间、角色、IP（可扩展） |

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fkFT2nlsyDbboLesmpvuGKMP0qVNJqgEJUMLbsQ6ZfLC8WS6dlp6RBkJ5ksqNo5pLJBwChxLXw8ib3g3HZICSte2NxJ885maQc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

**{六、下期预告}**

> **《安全运营平台 02：权限模型实战 —— 最小权限原则落地》**

我会分享：

* RBAC 表结构设计
* `@require_permission` 装饰器实现
* 菜单动态渲染
* 一个真实案例：越权漏洞是如何被权限模型拦截的

---

## 写在最后

这个系列所有代码都来自我**正在开发的安全运营平台**，不是 demo，不是 toy。

如果你也在做：

* 安全平台开发
* 内部运营系统
* 或单纯想学**带安全思维的 Django 开发**

欢迎关注、留言、讨论。

> **安全开发，不是"能跑就行"，而是"能防御才行"。**

---

**上一篇文章：**

**[十年甲方安全之路：从表格记录漏洞到一个人使用AI开发上线的安全运营平台（SOC）](https://mp.weixin.qq.com/s?__biz=MzIzNDE0Mzk0NA==&mid=2649595762&idx=1&sn=db685bdd9cce6c5e04c1f3063a86ddab&scene=21#wechat_redirect)**

## 历史精彩文章：

[甲方攻防大戏：功劳归我，活？归供应商，钱？还想续约不？](https://mp.weixin.qq.com/s?__biz=MzIzNDE0Mzk0NA==&mid=2649595620&idx=1&sn=d7e6884cd40cef80e39c20933020c525&scene=21#wechat_redirect)

[Hi，97小伙，请远离黑灰产，珍惜创业机会！别实名制扫描我了~！](https://mp.weixin.qq.com/s?__biz=MzIzNDE0Mzk0NA==&mid=2649594827&idx=1&sn=7bab9d2ea16f39829877bdf84303acba&scene=21#wechat_redirect)

[从被动写 2 小时情况说明到主动防患：一个甲方安全人牵头 fastjson 升级的全纪实](https://mp.weixin.qq.com/s?__biz=MzIzNDE0Mzk0NA==&mid=2649595649&idx=1&sn=03563af8a8f769b5fa2d7a98eb1882a4&scene=21#wechat_r...