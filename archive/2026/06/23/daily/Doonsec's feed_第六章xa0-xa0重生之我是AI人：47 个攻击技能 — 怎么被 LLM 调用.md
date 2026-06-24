---
title: 第六章xa0-xa0重生之我是AI人：47 个攻击技能 — 怎么被 LLM 调用
url: https://mp.weixin.qq.com/s/xQ34eDJAFEYn_rlaZIlIpw
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T05:59:39.712016
---

# 第六章xa0-xa0重生之我是AI人：47 个攻击技能 — 怎么被 LLM 调用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0LGiaGIrzXunj7jCenyU8hGGicmicCK24fAOBTIxrZnUS1CJe5WInx0ic0icibrtWc4RNrZU0AUTUNGGYJJ32ocNpn8V9s749DzfhCg0YoQR3Rziao/0?wx_fmt=jpeg)

# 第六章 - 重生之我是AI人：47 个攻击技能 — 怎么被 LLM 调用

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于威胁情报Z分析
，作者Gachong

![](http://wx.qlogo.cn/mmhead/j8cooK2zCqoqY1ibzIuH0db0U6NFgdx4PahHyU6OOprunMrA5RzXbibpMcUA18kVOibjEK1IK7HQ28/0)

**威胁情报Z分析**
.

国际网络安全威胁情报，地缘政治事件分析。

1. 关于内置的skills

在 Hati 里，一个"技能"就是一个Markdown 文件，写着"如果遇到 X 情况，按 Y 步骤测"。

对比传统概念：

● Ansible playbook：YAML 写的运维剧本

● Burp extension：Java/Python 写的插件

● Hati skill：Markdown 写的渗透测试剧本

为啥选 Markdown？

● 人类能读、LLM 能读、版本控制友好

● 改一个技能不需要重新编译代码

● 加新技能零代码(下一节细讲)

2. SKILL.md 长什么样

位置：skills/hack-skills/skills/sqli-sql-injection/SKILL.md

完整内容(简化版)：

```
---name： sqli-sql-injectiondescription： SQL injection detection and exploitationseverity： hightags： [sqli， database， web]---
## detection1. 找带参数的 URL(id=1， page=2， search=...)2. 加单引号 ' 看是否报错3. 加 ' OR '1'='1 看是否绕过4. 加 UNION SELECT 1，2，3 看是否回显
## exploitation- 联合查询： ' UNION SELECT username，password FROM users--- 布尔盲注： ' AND SUBSTRING(@@version，1，1)='5'--- 时间盲注： '; IF(1=1， SLEEP(5)， 0)--
## success_indicators- 响应里出现： SQL syntax， MySQL， syntax error- 页面长度变化超过 20%- UNION 回显数字
## pocsGET /artists.php？artist=1' OR '1'='1 HTTP/1.1GET /products？id=1 UNION SELECT 1，2，3--
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXunABGMibjbIN3iaJfibqdz1iazWWiaeqiaeW5E8UiaaxtZzhspDrHKE4FIKicQvuicicDccEceC9B1d22xtibq4gZ657RxNKiap8rFd0eCymIk/640?wx_fmt=png&from=appmsg)

几个有意思的字段：

● success\_indicators：多模式确认的特征字符串(避免误报)

● pocs：通用模板，具体目标要 LLM 适配

● severity：告诉 LLM 漏洞严重程度

● tags：用来自动匹配(下节讲)

3. 全部 47 个技能一览

我把所有技能按漏洞类型整理：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXunD7gdRtiaenYjJ79fzCgEaZjGGHUEFkIVCPHlja11XyP0f8F3Chsby4SCrDO1sickHF2eEhib0nxrNQnFC92gibl5LrXagpYwDYYE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXunibS7FooMQdiaKjDTEFic54TFKJSaUcR6VkUtesbpRKhHnhhMUSR8ePKPc5YOdicy6BicxtbfrfSeHQF094eO2vYVdLgWpAbFl6C2E/640?wx_fmt=png&from=appmsg)

4. 怎么加载：SkillLoader

文件：agents/skill\_loader.py：21-100

加载逻辑很短：

```
class SkillLoader：    def __init__(self， skills_path=None)：        if skills_path is None：            skills_path = "skills/hack-skills/skills"        self.skills_path = Path(skills_path)        self._skills_cache = {}        self._load_all_skills()
    def _load_all_skills(self)：        for skill_dir in self.skills_path.iterdir()：            if skill_dir.is_dir()：                skill_name = skill_dir.name                skill_data = self._load_skill(skill_dir)                if skill_data：                    self._skills_cache[skill_name] = skill_data        print(f"[SkillLoader] 已加载 {len(self._skills_cache)} 个攻击技能")
    def _load_skill(self， skill_dir)：        skill_file = skill_dir / "SKILL.md"        if not skill_file.exists()：            return None
        content = skill_file.read_text(encoding='utf-8')        metadata = self._parse_frontmatter(content)  # YAML 解析        sections = self._extract_sections(content)  # ## 标题切分
        return {            "name"： metadata.get("name"， skill_dir.name)，            "description"： metadata.get("description"， "")，            "content"： content，            "sections"： sections，            "dir"： skill_dir.name，        }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXumUiaVXm3SXicUf0LWSM0l3b9V60bBmLiaWk6B4iaOQTmapMZTO4cGKQaRibsSNMRRvGjPguA1iccTJArm6TmCJ3zz2OLialibolyZz5X8/640?wx_fmt=png&from=appmsg)

注意细节：

● 用 Python pathlib，跨平台

● 解析 YAML frontmatter(用 --- 包围的元数据)

● 切分 ## 章节(给 LLM 喂特定章节不用全文)

5. 怎么自动匹配：match\_skills

文件：agents/skill\_loader.py：143-220

这是 LLM 不参与的一步 — 纯关键词打分。为啥不用 LLM 匹配？

● 快：不烧 token，不调外部 API

● 便宜：0 成本

● 稳定：LLM 匹配有随机性，关键词不会

```
def match_skills(self， target_info)：    """    target_info = {        "url"： "http：//testphp.vulnweb.com"，        "tech"： ["php"， "mysql"]，        "open_ports"： [80， 3306]，        "keywords"： ["search"， "login"]    }    """    matched = []    for name， skill in self._skills_cache.items()：        score = 0        reasons = []
        # 看到数据库端口 → SQL 相关加分        if 3306 in target_info["open_ports"] and "sql" in name.lower()：            score += 2            reasons.append("数据库端口开放")
        # 看到 PHP → 文件操作类加分        if "php" in target_info["tech"] and "rce" in name.lower()：            score += 2            reasons.append("PHP 目标")
        # 看到 login 关键词 → 认证类加分        if any(k in target_info["url"] for k in ["login"， "auth"， "admin"])：            if "auth" in name.lower() or "bypass" in name.lower()：                score += 2                reasons.append("认证相关 URL")
        if score > 0：            matched.append({"name"： name， "score"： score， "reasons"： reasons， ...})
    return sorted(matched， key=lambda x： -x["score"])
```

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXukuDuwaT1WYXicYxa86l6xic9GH4bbYokKqb7l8akfgcbfjjBrq5eLfIicJ6G812ZgQT6LlgoAJzfhIBucjFEj5g5Kic0wATPyzgXU/640?wx_fmt=png&from=appmsg)

打分逻辑：

● 数据库端口(3306/1433/5432)→ SQL 类 +2

● PHP 目标 → RCE/LFI 类 +2

● URL 含 login → 认证类 +2

● 描述里出现 target 的 keyword → +1

返回的是 top N，按 score 倒序，LLM 拿到后再二次决策。

6. LLM 怎么"用"技能：模板适配

这是最巧的一步。技能是模板，目标是动态的。Hati 不会傻到把技能原文直接发出去 — 它让 LLM 改写。

文件：agents/orchestrator.py 中 \_llm\_adapt\_skill\_to\_target

简化版逻辑：

```
def _llm_adapt_skill_to_target(self， skill_content， target_info)：    prompt = f"""    技能模板：    {skill_content}
    目标：    - URL： {target_info['url']}    - 技术栈： {target_info['tech']}
    请把技能里的通用模板改写成针对这个目标的具体 HTTP 请求。    输出 JSON： {{"url"： "..."， "method"： "..."， "headers"： ...， "body"： "..."}}    """    response = self.llm.chat(prompt)    return parse_poc_from_llm(response)
```

实际效果：

```
技能原文：  "在 id 参数后加 ' OR '1'='1，看是否返回所有数据"
LLM 适配后：{  "url"： "http：//testphp.vulnweb.com/artists.php？artist=1' OR '1'='1"，  "method"： "GET"，  "headers"： {"User-Agent"： "..."}，  "body"： null}
```

这一步是 Hati 跟普通工具的本质区别 — 它真的能适配目标，而不是死板发模板。

7. 多模式确认

发包之后，Hati 不信 LLM 的"我觉得成功了"。它用特征字符串二次确认。

```
def multi_pattern_confirm(self， response， skill)：    indicators = skill["sections"].get("success_indicators"， [])    for pattern in indicators：        if re.search(pattern， response.text， re.IGNORECASE)：            return True    return False
```

为啥要二次确认？

● LLM 自己可能说"我觉得成功了"但其实没 — 幻觉

● 一次发包可能命中也可能是巧合

● 多模式确认大幅降低误报

实际数据：加二次确认后，误报率从 25% 降到 < 3%。

8. 怎么加新技能(零代码)

这是 Hati 最"工程友好"的地方。

步骤：

1. 在 skills/hack-skills/skills/ 下新建目录

```
mkdir skills/hack-skills/skills/my-new-vuln
```

2.写一个 SKILL.md

```
---name： my-new-vulndescription： Something new---
## detection...
## success_indicators...
```

3.重启 Hati(或重新调 get\_skill\_loader())

完事。 没有改任何 Python 代码。

加新技能的成本：

✅ 不需要懂 Python

✅ 不需要重启核心服务(可热加载，见 get\_skill\_loader 单例)

✅ 自动被 LLM 发现和匹配

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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