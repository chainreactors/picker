---
title: 全栈安全工程师实录：自产→自测→自修→自验，高危漏洞闭环全流程
url: https://mp.weixin.qq.com/s/haW9Lh9mMHRD-y9n_rAiUg
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:22:55.109944
---

# 全栈安全工程师实录：自产→自测→自修→自验，高危漏洞闭环全流程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kQTEwQUIic2co5urIFVicJrwoibPOfqChgxa6hN5EEibz1f34ft3cvHMH0VmSP6icJ8COCX9evzDKgoWZicdArWMuaDcNFLWQhDiao2yvMcBDXHEBk/0?wx_fmt=jpeg)

# 全栈安全工程师实录：自产→自测→自修→自验，高危漏洞闭环全流程

原创

cjstang
cjstang

新安集

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

友情提醒

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

| 邪恶闭环：自己写的漏洞、自己测试发现、自己修复加固、自己复测验证

在很多人的认知里，安全漏洞要么是测试团队测出、要么是渗透人员挖到。但对于单兵全栈开发、自研项目的从业者来说，还有一种最真实、最接地气的安全场景：**自己写的漏洞、自己测试发现、自己修复加固、自己复测验证**。

近期在自研安全运营平台上线前，正好借着AI+skill，完整的**自产→自测→自修→自验**高危漏洞闭环实战。全程单人搞定，从代码编写引入漏洞，到内网QA环境挖掘风险，再到代码修复、最终复测通关，全程无第三方参与。

这次踩坑也让我深刻意识到：**IDE自动化扫描永远替代不了人工业务安全测试**。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fNBg6Y1URDjiaQ51YwlxydbDItqTvlYV6Ribq5VfuO7rXYzIZehhDLucmIDN1379aY88RTsRSzVUSNyiaoesHd2E3qGjDxkWtHVg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

****{01 背景：单兵手搓项目，工具扫描无告警}****

##

项目上线前，我先通过PyCharm自带的安全检测工具完成全代码扫描，未发现任何高危漏洞。常规的SQL注入、XSS、代码缺陷均无问题，本以为代码安全达标，可以直接进入部署环节。

但经验告诉我：黑盒**工具能扫出语法漏洞，却不一定能扫出业务逻辑漏洞**。正好近期在用一些红队的skill，所以想着DAST+SAST（黑盒+白盒）形式。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fNBg6Y1URDjiaQ51YwlxydbDItqTvlYV6Ribq5VfuO7rXYzIZehhDLucmIDN1379aY88RTsRSzVUSNyiaoesHd2E3qGjDxkWtHVg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

****{02  漏洞自测：内网QA环境人工复现，实锤风险}****

白+黑  融合场景：claude code +代码审计的skill/黑盒漏洞扫描skill

![](https://mmbiz.qpic.cn/mmbiz_png/kQTEwQUIic2f8vvpWfhvdbxKpltYYtZbqarD5kiagO432GhzaaKicHeFo91KH1ZhdH7pGb1LxARkofGuxqu3IvrvzXA72494D7uGdZTTe2wfNU/640?wx_fmt=png&from=appmsg)

白盒一会就出了报告：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2cLNkoT9fqEfbUDTeKWnba1esXuq5YfPOL13LpM0Y35qNuVdriaaV3a2nI6Vszb1uyYOVibicUsq0JHp1YULDKGeQXtP9jCUVZIZ8/640?wx_fmt=png&from=appmsg)

为验证漏洞真实性，我在内网QA测试环境搭建真实业务场景，模拟黑白盒测试流程，准备两类测试账号：

* 管理员账号：拥有密码重置权限

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2dhP0rKkAFcJFDYFW9Ou560WnQNC9788aAWRUasDNP7jdUnAmm1e1eRVdR0aiaEqaic05CPAuIIPbPccib17SkPDfRocnRtk1EZDE/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2cUS9JF7ibAJiaralTprN8D3F3gn7ZqrlPGramDHgkicFbPUFUxzAPj0IictkAylqOklfotLjU78GfQO5U0NCFT41qPGbRMYKxSV0g/640?wx_fmt=png&from=appmsg)
* 普通用户账号：仅基础登录权限，无任何用户管理权限

![](https://mmbiz.qpic.cn/mmbiz_png/kQTEwQUIic2d48u7NI4PxbKsxjVzp6OgicouWts45hRLC1dydg6Sgy7et4RGFrDcfVvc2SC6G32h6BibT28s940wGd383CpxC01dBER9bSYrPc/640?wx_fmt=png&from=appmsg)

全程无任何权限拦截，越权攻击链路完全通畅，漏洞彻底实锤。也印证了：**AI不同时期写的代码质量也是参差不齐**。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fNBg6Y1URDjiaQ51YwlxydbDItqTvlYV6Ribq5VfuO7rXYzIZehhDLucmIDN1379aY88RTsRSzVUSNyiaoesHd2E3qGjDxkWtHVg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

****{03 漏洞自产：一行代码缺失，埋下安全隐患}****

简单分析了一下代码，本次漏洞完全源于开发阶段的疏忽，属于典型的“自己写出来的安全漏洞”。在开发密码重置接口时，仅配置了登录状态校验，**遗漏了核心的功能权限校验装饰器**。

漏洞原始代码如下：

```
@login_requireddef user_reset_pwd(request, nid): ”””重置用户密码””” # 先获取用户信息用于日志 user_obj = models.User.objects.filter(id=nid).first() if not user_obj: return JsonResponse({'code': 404, 'msg': '用户不存在'})  username = user_obj.account random_pwd = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) encrypted_pwd = make_password(random_pwd) models.User.objects.filter(id=nid).update(password=encrypted_pwd) # 记录操作日志：重置密码 user_info_session = request.session.get('user_info') current_user = models.User.objects.filter(id=user_info_session.get('id')).first() if user_info_session else None  LogManager.record_operation_log( request=request, user=current_user, operation_type=7, # 修改密码 operation_desc=f”重置用户【{username}】的密码”, operation_module=”用户管理”, result_status=1 )  return JsonResponse({'code': 200, 'msg': '重置成功', 'password': random_pwd})
```

**漏洞核心问题**：接口仅校验用户是否登录，未校验当前用户是否拥有「重置密码」的操作权限。

这意味着：**平台内任意一个普通登录用户，都可以通过修改请求参数，重置包括超级管理员在内的所有账号密码**，实现全站账号接管，风险等级为高危。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fNBg6Y1URDjiaQ51YwlxydbDItqTvlYV6Ribq5VfuO7rXYzIZehhDLucmIDN1379aY88RTsRSzVUSNyiaoesHd2E3qGjDxkWtHVg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

****{04 漏洞自修：补齐权限校验，从根源修复风险}****

定位漏洞根源后，我立即对接口进行安全修复，核心优化为**双层鉴权闭环**，在原有登录校验基础上，增加专属功能权限校验装饰器，匹配后台预设的权限码。

看了菜单权限是有对这一块的考虑，但代码层中确实丢失了权限的判断

![](https://mmbiz.qpic.cn/mmbiz_png/kQTEwQUIic2cwOGtFTBGicOgD5tJV6ObFibP2CPbtFzJugnw60pXGicTVzpqO6NqFLvuCeT8YfRg5alrLfbfr9soiactlOtHIG5fxt08xicd4ouaU/640?wx_fmt=png&from=appmsg)

修复后完整代码如下：

```
from .login import login_required, require_permission @login_required@require_permission('user:reset_pwd')# 专属权限，仅授权角色可访问 def user_reset_pwd(request, nid): ”””重置用户密码”””
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fNBg6Y1URDjiaQ51YwlxydbDItqTvlYV6Ribq5VfuO7rXYzIZehhDLucmIDN1379aY88RTsRSzVUSNyiaoesHd2E3qGjDxkWtHVg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

****{05 漏洞自验：多场景复测，完成安全闭环}****

修复完成后，QA环境开展多场景回归复测，彻底验证漏洞修复效果，确保业务可用、风险清零。

**测试用例：无权限普通用户调用接口**

使用普通用户Session发起请求，系统直接拦截，返回权限不足提示，越权攻击链路彻底阻断，漏洞修复生效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2eeGianZSF91CX6gNSHvVTovsnwckA02XMYXONQOgndyBA6wcOtriafEpicHSUnfX1icvUA4YwXfLfrSRAevM67hCAO9azrMibFIicck/640?wx_fmt=png&from=appmsg)

测试通过，本次高危漏洞从诞生到彻底消亡，完成**自产→自测→自修→自验**全流程闭环。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fNBg6Y1URDjiaQ51YwlxydbDItqTvlYV6Ribq5VfuO7rXYzIZehhDLucmIDN1379aY88RTsRSzVUSNyiaoesHd2E3qGjDxkWtHVg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEFP21VntQ2vUQCHc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

****{06 实战总结：单兵开发必备的安全思维}****

本次单人漏洞闭环实战，给独立开发、全栈从业者、后端研发提了几个核心避坑要点：

**1. 永远不要只依赖自动化工具兜底安全**

前期的IDE，只能说一言难尽，黑盒+白盒，工具+人工，才是永远的神！

**2. 高危接口强制双层鉴权，缺一不可**

密码重置、用户管理、权限分配、数据删除等核心接口，必须同时配置「登录状态校验+功能权限校验」，杜绝水平、垂直越权漏洞。

**3. 单兵项目必须建立完整安全闭环**

无专职测试、安全团队的个人项目，开发者要身兼多职，自己把控代码质量、自己测试安全、自己修复漏洞、自己验证效果，形成完整安全链路。

**4. 上线前必做权限专项审计**

梳理所有后台路由接口，逐一核对权限装饰器、权限码配置，重点排查用户管理、系统配置等高风险模块，提前规避隐形漏洞。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fNBg6Y1URDjiaQ51YwlxydbDItqTvlYV6Ribq5VfuO7rXYzIZehhDLucmIDN1379aY88RTsRSzVUSNyiaoesHd2E3qGjDxkWtHVg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kQTEwQUIic2fBhovWS2txuTPlNHib789RzWn8RbF7c75ibc14JWMAfw8hpZ3OJibFKNxibficqBqSPzdeDWFTzPeJ1xkG4TxpEF...