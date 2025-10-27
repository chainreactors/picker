---
title: 我使用ChatGPT审计代码发现了200多个安全漏洞(GPT-4与GPT-3对比报告)
url: https://www.secpulse.com/archives/198731.html
source: 安全脉搏
date: 2023-04-08
fetch_date: 2025-10-04T11:29:14.791957
---

# 我使用ChatGPT审计代码发现了200多个安全漏洞(GPT-4与GPT-3对比报告)

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 我使用ChatGPT审计代码发现了200多个安全漏洞(GPT-4与GPT-3对比报告)

[漏洞](https://www.secpulse.com/archives/category/vul)

[公众号:安全女巫](https://www.secpulse.com/newpage/author?author_id=49672)

2023-04-07

14,542

如果你喜欢我的文章，欢迎关注公众号：安全女巫

转载请注明出处：<https://mp.weixin.qq.com/s/uVFCbaKDYeF9zmVdVXDnUg>

前面使用GPT-4对部分代码进行漏洞审计，后面使用GPT-3对git存储库进行对比。最终结果仅供大家在chatgpt在对各类代码分析能力参考，其中存在误报问题，不排除因本人训练模型存在问题导致，欢迎大家对误报结果进行留言，我会第一时间跟进处理~

大家若想看更全面的内容，请先关注我并发送私信，我会根据大家反馈写一篇GPT-4对某代码更全面的分析报告。

**前言**

GPT-3 在此git 存储库中发现了 213 个安全漏洞。而相比之下，市场上很好的商业工具却只发现了99 个安全漏洞。尽管商业工具以更结构化的格式提供上下文，在手动审查 GPT-3 检测到的 99 / 213 个漏洞的随机样本后，有 4 个是误报。代码审计大家都清楚，存在误报是常规操作。

**其中各类脚本漏洞占比结果如下：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198731-1680853294.png)

**分析漏洞数量总体占比：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198731-1680853295.png)

**简介**

    近年来，ChatGPT 已成为互联网新宠，长期以来一直对现代人工智能的潜在影响持怀疑态度的网络安全行业似乎也注意到了这一点，因为他们担心 ChatGPT 可能会被资源有限、技术知识为零的黑客滥用。

    目前人工智能和机器学习领域取得了巨大的发展，如此便开辟了一个新的可能性领域-基于 AI 的代码分析，如何使用 AI 模型来检测代码中的安全漏洞尤为惹人关注。

    文中使用 OpenAI 的 GPT-4对部分代码进行分析，文末针对GPT-3 如何在包含 129 个易受攻击文件的代码存储库中查找安全漏洞。如果大家感兴趣，我会单独为大家更新哦！

**如何运行**

    GPT-4使用Plus会员版本，跟官网同配置，可处理长代码。（PS:若有朋友需要开通PLus会员，私信留言，将提供保姆级教程和邀请码，能优惠购买哦~）

    GPT-3变体（text-davinci-003）具有4000个标记的上下文窗口，大约为3000个英文单词。这意味着它最多可以处理几百行代码的请求，无法一次性处理整个代码库。

    为了解决这个问题，只能使用GPT-3扫描单文件。这意味着GPT-3难以找到由多个代码文件交互引起的安全漏洞，除非进行足够多的提示词引导。特别是当源代码使用常见的库，如express.js、Flask、Python标准库、C标准库等时。可能GPT-3有相关记录。在本文分析的代码中，GPT-3对导入库有相关记录就能够准确地检测到安全漏洞，而无需检查任何导入库的代码。

    公平地说，我怀疑许多现有的商业漏洞扫描工具在进行静态分析时实际上并不检查导入库的代码，因此这与市场上某些工具的工作方式并没有太大的不同。

    被分析的代码存储库中的每个文件夹都以一种安全漏洞命名，并包含带有示例代码的文件，包含一个或多个漏洞。其中一些文件包含琐碎的代码，但许多是您可能会在生产代码库中遇到同样的代码片段（注意：尽管它们仍然是片段，因此缺乏更大代码库的上下文）。存储库中每个文件夹的 README.md 包含 GPT-3 对该文件夹中所有文件的安全漏洞的分析。

使用的漏洞代码库：

https://github.com/chris-koch-penn/gpt3\_security\_vulnerability\_scanner

开篇我是用GPT-4分析，后面代码将会用GPT-3的进行对比。

**1》代码注入漏洞检测**

**PHP代码片段1(tarlogic-ex2.php)：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198731-1680853296.png)

**检测结果：**

这段代码存在一个漏洞，即通过 PHP 的 unserialize 函数，可以实现远程代码执行。具体原因如下：

1. 在代码中，我们可以看到 entry 类的 \_\_destruct() 方法会调用 $this->awesome->flag()。当 PHP 对象被销毁时，\_\_destruct() 方法会自动执行。
2. 代码末尾使用了 unserialize() 函数，它可以将一个已被序列化的字符串转换回 PHP 值。在这个例子中，用户可以通过命令行参数输入一个序列化的字符串。
3. 通过构造一个序列化的字符串，攻击者可以创建一个 entry 类的实例，同时将其 awesome 属性指向 GiveFlag 类的实例。这样，当 entry 类的实例被销毁时，\_\_destruct() 方法会执行 GiveFlag 类的 flag() 方法，进而执行 GiveFlag 类的 innocent() 方法。GiveFlag 类的 innocent() 方法会打开 "flag.txt" 文件并读取其中的内容。这样一来，攻击者就可以通过输入一个恶意构造的序列化字符串来触发代码执行，获取 "flag.txt" 文件的内容。

为了修复这个漏洞，可以考虑以下几点：

避免使用 unserialize() 函数处理不可信的数据。可以使用其他方法（如 JSON）来传输和解析数据。

对于具有潜在危险的魔术方法，如 \_\_destruct()，要特别小心。确保在使用这些方法时，不会引入安全隐患。

结果还是很详细。

**2》Flask反序列化漏洞**

**Python代码(pickle2.py)：**

GPT-4对长代码分析能力：

```
from __future__ import unicode_literalsfrom flask import Flask, request, make_response, redirect, url_for, sessionfrom flask import render_template, flash, redirect, url_for, requestfrom werkzeug.security import safe_str_cmpfrom base64 import b64decode as b64dfrom base64 import b64encode as b64efrom hashlib import sha256from cStringIO import StringIOimport randomimport string
import osimport sysimport subprocessimport commandsimport pickleimport cPickleimport marshalimport os.pathimport filecmpimport globimport linecacheimport shutilimport dircacheimport ioimport timeitimport popen2import codeimport codeopimport ptyimport posixfile
SECRET_KEY = 'you will never guess'
if not os.path.exists('.secret'):    with open(".secret", "w") as f:        secret = ''.join(random.choice(string.ascii_letters + string.digits)                         for x in range(4))        f.write(secret)with open(".secret", "r") as f:    cookie_secret = f.read().strip()
app = Flask(__name__)app.config.from_object(__name__)
black_type_list = [eval, execfile, compile, open, file, os.system, os.popen, os.popen2, os.popen3, os.popen4, os.fdopen, os.tmpfile, os.fchmod, os.fchown, os.open, os.openpty, os.read, os.pipe, os.chdir, os.fchdir, os.chroot, os.chmod, os.chown, os.link, os.lchown, os.listdir, os.lstat, os.mkfifo, os.mknod, os.access, os.mkdir, os.makedirs, os.readlink, os.remove, os.removedirs, os.rename, os.renames, os.rmdir, os.tempnam, os.tmpnam, os.unlink, os.walk, os.execl, os.execle, os.execlp, os.execv, os.execve, os.dup, os.dup2, os.execvp, os.execvpe, os.fork, os.forkpty, os.kill, os.spawnl, os.spawnle, os.spawnlp, os.spawnlpe,                   os.spawnv, os.spawnve, os.spawnvp, os.spawnvpe, pickle.load, pickle.loads, cPickle.load, cPickle.loads, subprocess.call, subprocess.check_call, subprocess.check_output, subprocess.Popen, commands.getstatusoutput, commands.getoutput, commands.getstatus, glob.glob, linecache.getline, shutil.copyfileobj, shutil.copyfile, shutil.copy, shutil.copy2, shutil.move, shutil.make_archive, dircache.listdir, dircache.opendir, io.open, popen2.popen2, popen2.popen3, popen2.popen4, timeit.timeit, timeit.repeat, sys.call_tracing, code.interact, code.compile_command, codeop.compile_command, pty.spawn, posixfile.open, posixfile.fileopen]

@app.before_requestdef count():    session['cnt'] = 0

@app.route('/')def home():    remembered_str = 'Hello, here\'s what we remember for you. And you can change, delete or extend it.'    new_str = 'Hello fellow zombie, have you found a tasty brain and want to remember where? Go right here and enter it:'    location = getlocation()    if location == False:        return redirect(url_for("clear"))    return render_template('index.html', txt=remembered_str, location=location)

@app.route('/clear')def clear():    flash("Reminder cleared!")    response = redirect(url_for('home'))    response.set_cookie('location', max_age=0)    return response

@app.route('/reminder', methods=['POST', 'GET'])def reminder(): ...