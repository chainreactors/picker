---
title: 用隐式马尔科夫模型检测XSS攻击Payload
url: https://mp.weixin.qq.com/s/iRnIgLCMV3BjM1JKMVXIFA
source: Doonsec's feed
date: 2026-07-31
fetch_date: 2026-08-01T05:08:43.581808
---

# 用隐式马尔科夫模型检测XSS攻击Payload

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldws1Wy1licQzfdp5Wl33xXk6wEqwhSv5w2ukJG4Y1ich2rRmSK4iap1aeG1B0wUIkWovmI0a9PhLGbMg/0?wx_fmt=jpeg)

# 用隐式马尔科夫模型检测XSS攻击Payload

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于蚁景网络安全
，作者秋名山上的小柠

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM7Yk0SeU4ibQcLl1mDLlqhbAOdK1Ik3EO85soOvkh9e8wQ/0)

**蚁景网络安全**
.

致力于为你带来更实用的网络安全技术内容！

## 0.前言

学习一下如何使用机器学习的方式去识别xss payload

## 1.xss介绍

其实xss说白了就是，通过向网页中注入恶意的脚本代码，一般来说都是 JavaScript，让代码在其他用户的浏览器中执行，从而达到窃取信息、冒充身份、传播木马等目的

换句话说，网站本来应该只展示安全的内容的，但是攻击者把一些恶意的脚本给塞入了网站中，让浏览器错误地把其当成正常内容执行了

大概有以下这几种分类：

**反射型**：payload 在请求里，也就是URL或者表单，服务器拼回页面即触发，通常需要诱导点击

**存储型**：payload 被存入库，比如说什么网站的评论、昵称、公告之类的，所有访问者都会触发

**DOM 型**：前端脚本把不可信数据塞进危险 DOM Sink`innerHTML` 之类的，不依赖服务器拼接

**盲 XSS**：这个顾名思义是看不到弹窗，但 payload 会在后台或者运营端页面执行

**自我 XSS**：诱导用户在控制台粘贴代码

**变异 XSS**：浏览器或框架在解析或者重排 DOM 时修补标签，绕过原本的过滤器

## 2.隐式马尔科夫

马尔科夫模型就是基于本次观测的状态来预测上一次的状态 而不依赖前面的所有内容

假设现在有三个时间点：1，2，3

在2这个时间点是a，到了3这个时间点就变成了A，而马尔科夫模型在这里就仅根据a来预测，而不是根据a前面的内容

主要解决连续问题，比如说：

* 文本类中上一个字或者词中下一个字词的出现概率
* 一个连续的字词构成的句子判断句子的情感等

使用的时候需要在虚拟环境中下载一个第三方库

```
ounter(linepip install hmmlearn -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 3.使用隐式马尔科夫识别XSS

注意：这里只截取重要部分代码，并没有展示完全

xss语法特征

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(line<src><script><alert>http://<img>onerror
```

导入一个文本的数据，都是各种各样的xss变体,github或者是kaggle上都能找到相关的xss数据集

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldws1Wy1licQzfdp5Wl33xXk6lmSGibwD9UfE4OU5iaYibic1ZibYYEp9JmOLlGxFage7AXhswj4q8NI4l3w/640?wx_fmt=png&from=appmsg)

然后进行一个数据向量的处理

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldws1Wy1licQzfdp5Wl33xXk67gu5COFqHUeeV6Lle783gLe776iaY3zKPdX4jFFvicHhyLESSDSeNXIQ/640?wx_fmt=png&from=appmsg)

这是个正则表达式，匹配双引号里面的字符串，比如说xss里面会有这种<>括起来的符号

还有把http开头的，闭合的标签，反斜杆，或者是只有一个>，还有=符号，毕竟xss里面有什么onerror=xxx之类

还有函数调用，老生常谈的alert

然后使用nltk，一个自然语言的工具，用来做分词处理

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldws1Wy1licQzfdp5Wl33xXk6Bk0luO3Tpp1PlwW6e6tU3ntSwoGLMGtw6UeqQcPu3MHQbp23GxDVIQ/640?wx_fmt=png&from=appmsg)

那什么是分词处理？把一段连续的文本拆分成一个个有意义的“词语”或“最小语言单位”的过程

在英语中，单词之间有空格，计算机很容易识别：

> “I love natural language processing.”

可以直接得到：["I", "love", "natural", "language", "processing"]

但在中文中，句子是连续的，没有空格：

> “我爱自然语言处理。”

对计算机来说，这是一个连续的字符串，它不知道“我爱”、“自然语言处理”这些边界。 所以就需要**中文分词算法**来判断哪些字该组合在一起

接下来就是转换列表，去重，添加等常规操作

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldws1Wy1licQzfdp5Wl33xXk6Bk0luO3Tpp1PlwW6e6tU3ntSwoGLMGtw6UeqQcPu3MHQbp23GxDVIQ/640?wx_fmt=png&from=appmsg)

这样就大致完成了数据向量的处理

模型的结构

```
ounter(lineounter(lineounter(lineimport model_paramfrom hmmlearn import hmmremodel = hmm.GaussianHMM(n_components=model_param.N, covariance_type="full", n_iter=model_param.n_iter)
```

model\_param.N是模型的状态，就是样本到底有几个类型，比如3个不同类型的骰子之类的

covariance\_type="full" 这个表示所有的样本都是有数据的，都是不为0的

```
ounter(lineounter(lineounter(lineounter(line#状态个数N=5#迭代次数n_iter=100
```

这里就把状态数和迭代数设置为5和100，这里100次看个人电脑配置吧，我100次都跑得挺慢的

模型的训练

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineimport model_structimport joblibimport vec_dataindex_wordbag=1 #词袋索引wordbag={} #词袋wordbag = vec_data.load_wordbag("E:\\my_hmm\\data\\xss-200000.txt",2000)X,X_lens = vec_data.vec("E:\\my_hmm\\data\\xss-200000.txt",wordbag)remodel = model_struct.remodel.fit(X,X_lens)joblib.dump(remodel, "xss-train.pkl")
```

把用到的数据都加入到词袋中去，第一次词袋是空的，第一次就是去填满这个内容，也就是词的特征，第二次是做匹配，也就是根据上面的特征去做匹配才能返回X这个结果

有了X和X\_lens之后就可以做训练，然后把xss-train.pkl这个模型保存到本地

模型测试

可以设置一个判断的阈值，或者理解为一个评分

都是负数，评分越靠近0就说明越不像xss，评分越远离0就说明很像xss

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldws1Wy1licQzfdp5Wl33xXk6Cwkyuz9PoRuLNZQ7dQq0RZVeBHJKeickKOrFDSnm8oMQsvzbyhESrkQ/640?wx_fmt=png&from=appmsg)

比如说我们在test数据中放入这么几条数据

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line/0_1/?%22onmouseover='prompt(42873)'bad=%22%3E/0_1/api.php?op=map&maptype=1&city=test%3Cscript%3Ealert%28/42873/%29%3C/script%3E/0_1/api.php?op=map&maptype=1&defaultcity=%e5%22;alert%28/42873/%29;///0_1/api.php?op=map&maptype=1&defaultcity=%E5%8C%97%E4%BA%AC&api_key=%22%3E%3C/script%3E%3Cscript%3Ealert%28/42873/%29;%3C/script%3E/0_1/api.php?op=map&maptype=1&defaultcity=%E5%8C%97%E4%BA%AC&field=%29%3C/script%3E%3Cscript%3Ealert%2842873%29%3C/script%3E///0_1/api.php?op=video_api&pc_hash=1&uid=1&snid=%3C/script%3E%3Cscript%3Ealert(/42873/)%3C/script%3E//&do_complete=1%20/0_1/api.php?op=video_api&uid=1&snid=1&pc_hash=%3C/script%3E%3Cscript%3Ealert(/360/)%3C/script%3E//&do_complete=1/0_1/?callback=%3Cscript%3Eprompt(42873)%3C/script%3E
```

让训练好的模型去检测这些是不是xss攻击

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldws1Wy1licQzfdp5Wl33xXk6hrbRxgopGsrIgsbMekgtGefsJXg99BvXHWP5BljYSQsV4dZicrdlh6Q/640?wx_fmt=png&from=appmsg)

可以看到评分越小，说明它越像xss攻击

接下来，可以把训练好的模型做成一个可视化界面

可以使用django或者flask框架，这里就使用flask框架

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line...#最大似然概率阈值T=-13def process_text(input_text):    # 这里可以添加处理逻辑    remodel = joblib.load("E:\\my_hmm\\model\\xss-train.pkl")    f = open("test.txt", "w")    f.write(input_text)    f.close()    pro,line = test(remodel,"test.txt")    print(pro)    if pro == -1000:        return "请输入长度为10以上的payload"    elif pro > T:        return "没有检测到xss代码"    else:        return f"检测的结果是: {line},评分为：{pro}"
@app.route('/', methods=['GET', 'POST'])def index():    result = ""    if request.method == 'POST':        input_text = request.form['input_text']        result = process_text(input_text)    return render_template('index.html', result=result)
if __name__ == '__main__':    app.run(debug=True)
```

先把训练好的模型加载进来，然后把input\_txt保存成一个本地文件test.txt，然后使用写好的判断分数函数去做一个分数判断

因为最简单的xss攻击payload也会超过10个长度，所以可以先把长度小于10的排除了

如果分数大于-13，就说明模型认为不是xss攻击

实际效果就如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldws1Wy1licQzfdp5Wl33xXk6Ia4ptP0avaDa3JhMYNBPWAiaYRtx1q3UtylTCkHXqO2uxORCfMJSNibw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldws1Wy1licQzfdp5Wl33xXk61rJr9Gd5zM3t8z9Fzz4ib0s6P7IBzic7iau8ulsUMVyTnNqKdHbDY4xnQ/640?wx_fmt=png&from=appmsg)

使用样本里面没有的xss payload 模型也能检测出来

但是并非百分之百正确，却可以解决一些看起来像的问题

有一点要注意，虽然 HMM 可以捕捉 XSS Payload 的语法序列特征，但对于经过多层编码、混淆的攻击样本效果有限

此外，模型需要大量带标签的数据进行训练，否则容易过拟合

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

学习网安实战技术，戳“阅读原文”

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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