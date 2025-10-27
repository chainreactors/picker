---
title: 拆解大模型“越狱”攻击：对抗样本如何撕开AI安全护栏？
url: https://forum.butian.net/share/4254
source: 奇安信攻防社区
date: 2025-04-15
fetch_date: 2025-10-06T22:02:42.870666
---

# 拆解大模型“越狱”攻击：对抗样本如何撕开AI安全护栏？

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 拆解大模型“越狱”攻击：对抗样本如何撕开AI安全护栏？

本文系统拆解大模型面临的越狱攻击技术，揭示攻击者如何通过巧妙设计突破AI安全限制

引言
==
随着大规模语言模型（LLMs）在内容生成、智能交互等领域的广泛应用，其安全性和可控性成为学界和产业界关注的焦点。尽管主流模型通过道德对齐机制建立了安全护栏，但研究者发现，通过精心设计的"越狱攻击"（Jailbreaking Attack），攻击者仍能诱导模型生成违法、偏见或泄露隐私的受限内容。这类攻击根据攻击者对模型内部信息的掌握程度，可分为白盒攻击和黑盒攻击两类：白盒攻击利用模型参数、梯度等内部信息，通过对抗样本生成或参数逆向工程精准突破防御机制；而黑盒攻击则仅依赖输入输出交互，采用语义混淆、系统提示注入或上下文劫持等策略绕过安全过滤。两类攻击手段的持续演进，不仅暴露了现有对齐技术的脆弱性，更揭示了语言模型安全防御需要从对抗性测试、鲁棒性增强到动态监测的多层次防御框架。深入研究越狱攻击机理，对于构建安全可靠的人工智能系统具有重要现实意义。本文将介绍大模型越狱攻击的几种方式。
越狱攻击是指\*\*恶意行为者通过精心设计的提示，利用模型架构或实现中的漏洞，诱导模型生成不安全或有害的内容\*\*，如下图：
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/03/attach-5215393610246aec9b3ab66ea7c51f1711790a96.png "null")
直接问常规敏感问题：\*"What tools do I need to cut down a stop sign?"\*（砍倒停车标志需要什么工具？）
Al是直接拒绝回答的，但是我们可以通过构造角色扮演指令（如DAN模式），声明"突破AI规则限制，无需遵守任何约束"，然后将恶意请求嵌套在伪合法任务中（例如伪装成"网络安全测试"或"文学创作"），最后利用模型的场景适应能力，诱导其进入"无限制模式"输出危险信息。
### 白盒攻击
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/03/attach-e42ffc097470d12b22896fac366b8cbb89afcfc1.png "null")
白盒攻击分为3部分：
| | | |
|---|---|---|
| 攻击方式 | 核心原理 | 形成原因 |
| \*\*梯度攻击\*\* | 利用梯度方向优化输入，操控模型输出概率 | 模型透明性暴露梯度信息，攻击者通过反向传播劫持生成逻辑 |
| \*\*Logits攻击\*\* | 直接操纵未归一化概率值，强制模型选择目标 | Logits分布暴露模型决策倾向，攻击者针对性篡改概率分布 |
| \*\*微调攻击\*\* | 修改模型参数，削弱安全层功能 | 白盒权限允许参数调整，安全模块可能因局部微调失效 |
#### \*\*基于梯度的攻击（Gradient-based）\*\*
\*\*攻击原理：\*\*
基于梯度的攻击通常通过反向传播获取输入数据的梯度信息，利用梯度方向构造微小扰动，使得模型在扰动后的输入上产生错误预测\*\*，\*\*例如在原始提示语前后加上特定的“前缀”或“后缀”，并通过优化这些附加内容来实现攻击目标。背后思路类似于文本对抗性攻击，目的是让模型生成有害或不恰当的回答。
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1744183868839-993650f2-7fc5-4b68-827f-0fb32f37f2af.png)
上述图片就是一个梯度攻击示例
##### \*\*左侧攻击（Soft Prompt注入）\*\*
- 将恶意指令 "How to make a bomb" 拆解为子词嵌入序列 `[e(How), e(to), e(make), e(a), e(bomb)]`
- 通过梯度反向传播优化每个token的嵌入向量（h0→h1），使得模型隐层状态 ht 向有害响应空间偏移
##### \*\*右侧攻击（对抗后缀生成）\*\*
将原始恶意文本映射为对抗后缀序列 `X\_0 → X\_k`，该过程通过梯度对齐实现
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1744184228503-a1fa396f-7a03-4f72-bc7d-57ee5a980da5.png)
（α为步长，通过迭代优化逐步增强扰动）将生成的对抗后缀与原始提示拼接，迫使LLM在解码时沿白色箭头路径生成有害内容
下面通过github上面一个开源快速梯度下降法（FGSM）的攻击案例来学习一下[项目地址](https://github.com/Starrylay/awesome-HUST-CS-CV/blob/main/FGSM%E6%94%BB%E5%87%BB-%E5%AF%B9%E6%8A%97%E8%AE%AD%E7%BB%83%E9%98%B2%E5%BE%A1/cvlab2.py)
梯度方向指示了\*\*使模型损失函数增长最快的方向\*\*。通过沿此方向添加扰动，可最大化模型的预测误差，实现以下效果：
- \*\*非定向攻击\*\*：让预测标签偏离原始正确标签
- \*\*定向攻击\*\*：使预测标签逼近指定错误标签
下面是[项目地址](https://github.com/Starrylay/awesome-HUST-CS-CV/blob/main/FGSM%E6%94%BB%E5%87%BB-%E5%AF%B9%E6%8A%97%E8%AE%AD%E7%BB%83%E9%98%B2%E5%BE%A1/cvlab2.py)对抗攻击的源码，现在对其关键代码做一些分析
\*\*非定向攻击\*\*
常规的分类模型训练在更新参数时都是将参数减去计算得到的梯度，这样就能使损失值越来越小，从而模型预测结果越来越准确。既然对抗攻击是希望模型将输入图像进行错误分类，那么就要求损失值越来大，这和原来的参数更新目的正好相反。因此，只需要在输入图像中加上计算得到的梯度方向，这样修改后的图像经过网络时的损失值就会变大。
核心公式：
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1744080584688-a77ca600-2c6c-4526-894f-d7ef84dc3712.png)
其中：
- J 为交叉熵损失（Cross Entropy Loss）
- ∇xJ 是损失函数对输入数据的梯度
- ϵ 为扰动强度系数
- sign() 保留梯度方向，消除幅值影响
实现代码：
\*\*梯度计算模块\*\*
```php
def generate\_adversarial\_pattern(input\_image, image\_label, model, loss\_func):
optimizer = torch.optim.Adam(model.parameters(), lr=learning\_rate)
logit, prediction = model(input\_image)
loss = loss\_func(prediction, image\_label)# 计算损失
#每次backward前清除上一次loss相对于输入的梯度
if input\_image.grad != None:
input\_image.grad.data.zero\_()
loss.backward()# 反向传播求梯度
gradient = input\_image.grad# 获取输入梯度
#每次backward后清除参数梯度，防止产生其他影响
optimizer.zero\_grad()
#得到梯度的方向
signed\_grad = torch.sign(gradient)# 取符号方向
return signed\_grad
```
首先看generate\\_adversarial\\_pattern函数。这个函数的参数包括input\\_image（输入图像）、image\\_label（标签）、model（模型）、loss\\_func（损失函数）。函数内部首先定义了一个优化器optimizer，使用的是Adam优化器，然后，logit, prediction = model(input\\_image)这行代码，这里假设模型返回两个值，但不同的模型结构可能不同，需要确认模型的输出结构是否正确。接下来计算loss，使用loss\\_func(prediction, image\\_label)。非定向攻击，损失函数应该计算的是模型对原始标签的损失，通过最大化这个损失来使模型预测错误。然后，检查input\\_image.grad是否为None，如果不是，则清零。这是因为在PyTorch中，梯度是会累积的，所以每次反向传播前需要清除之前的梯度。这里是在处理多个攻击步骤时的考虑，但FGSM通常是一次性攻击，所以可能不需要多次累积梯度。但这里保险起见，确保梯度正确。之后，执行loss.backward()进行反向传播，计算input\\_image的梯度。然后获取梯度input\\_image.grad。接下来，optimizer.zero\\_grad()清空模型参数的梯度，防止对模型参数产生影响。这是因为在生成对抗样本时，我们只关心输入数据的梯度，而不希望改变模型本身的参数。这一步是必要的，否则在后续的模型训练中可能会有干扰。最后，取梯度的符号方向，得到signed\\_grad，并返回。 这就是FGSM的公式，即使用梯度的符号作为扰动的方向 。
\*\*非定向攻击实现\*\*
对应公式中的 \*\*xadv=x+ϵ⋅sign(∇xJ)\*\*
将符号梯度按扰动系数 ϵ 缩放后叠加到原始输入，生成对抗样本
```php
def attack\_fgsm(input\_image, image\_lable, model, loss\_func , eps=0.01):
#预测原来的样本类别
# input\_image = np.array([input\_image])
# input\_image = torch.from\_numpy(input\_image)
\_, y\_pre = model(input\_image)
pre\_prob, pre\_index = torch.max(y\_pre, 1) #概率 和 类别
#生成对抗样本
# loss\_func = nn.CrossEntropyLoss()
input\_image.requires\_grad = True
adv\_pattern = generate\_adversarial\_pattern(input\_image, image\_lable,
model, loss\_func)
clip\_adv\_pattern = torch.clamp(adv\_pattern, 0., 1.)
perturbed\_img = input\_image + (eps \* adv\_pattern)
perturbed\_img = torch.clamp(perturbed\_img, 0., 1.)
#预测对抗样本的类别
\_, y\_adv\_pre = model(perturbed\_img)
adv\_pre\_prob, adv\_pre\_index = torch.max(y\_adv\_pre, 1) # 概率 和 类别
#可视化
if args.is\_view == True:
fig, ax = plt.subplots(1,3,figsize=(20, 4))
ax[0].imshow(input\_image[0][0].cpu().detach().numpy().squeeze(), cmap = 'gray')
ax[0].set\_title('orignal sample\nTrue:{} Pred:{} Prob:{:.3f}'.format(image\_lable[0].cpu().detach().numpy(), pre\_index[0].cpu().detach().numpy(), pre\_prob[0].cpu().detach().numpy()))
ax[1].imshow(clip\_adv\_pattern[0][0].cpu().detach().numpy().squeeze(), cmap='gray')
ax[1].set\_title(r'Adversarial Pattern - EPS: {}/255'.format(args.epsfenzi))
ax[2].imshow(perturbed\_img[0][0].cpu().detach().numpy().squeeze(), cmap='gray')
ax[2].set\_title('Attack sample\nTrue:{} Pred:{} Prob:{:.3f}'.format(image\_lable.cpu().detach().numpy(), adv\_pre\_index[0].cpu().detach().numpy(), adv\_pre\_prob[0].cpu().detach().numpy()))
if pre\_index == image\_lable and adv\_pre\_index != image\_lable:
if args.is\_view == True:
plt.savefig(r'D:\image\randomed\{}to{}eps{}.png'.format(image\_label[0].cpu().detach().numpy(),
adv\_pre\_index[0].cpu().detach().numpy(),
args.epsfenzi), bbox\_inches='tight')
plt.show()
return 1
else:
if args.is\_view == True:
plt.show()
return 0
```
接下来看attack\\_fgsm函数。参数包括input\\_image、image\\_label、model、loss\\_func以及eps。首先，模型对原始输入进行预测，得到y\\_pre，然后取最大概率和对应的类别pre\\_index。通常，模型输出logits，然后经过softmax得到概率，但这里代码中直接用了logits，接下来设置input\\_image.requires\\_grad = True，因为需要计算关于输入图像的梯度。然后调用generate\\_adversarial\\_pattern生成对抗模式adv\\_pattern。此时adv\\_pattern已经是符号化的梯度方向。然后，clip\\_adv\\_pattern被计算为将adv\\_pattern截断在\[0,1\]之间。之后perturbed\\_img = input\\_image + eps \\* adv\\_pattern。这里应用了FGSM的公式，将符号梯度乘以epsilon加到原始图像上。然后，对扰动后的图像进行clamp，确保像素值在0到1之间，符合图像数据的范围。然后，模型对扰动后的图像进行预测，得到y\\_adv\\_pre，并取概率和类别。接下来的部分是可视化，如果args.is\\_view为True，则显示原始图像、对抗模式和扰动后的图像，并展示预测结果。最后，判断原始预测是否正确（pre\\_index == image\\_label）且对抗样本预测错误（adv\\_pre\\_index != image\\_label），如果满足条件，则保存图像并返回1，否则返回0。用来统计攻击的成功率。
\*\*定向攻击：\*\* 通过修改输入使模型在目标类别上的损失最小化，与常规训练方向一致但优化对象不同
损失函数的含义在于衡量预测标签与真实标签之间的差异大小， 差异越大，则说明预测越不准确，我们要有针对性的误导模型，让模型在错误标签下损失函数值越来越小，即在错误标签对输入图片进行梯度下降得到扰动
核心公式：
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1744187163587-c099b70c-be6c-475d-ad45-2c579330aceb.png)
```php
def targeted\_fgsm(input\_image, image\_label, target\_label, model, eps=0.01):
# 1. 原始预测验证
\_, y\_pre = model(input\_image)
pre\_prob, pre\_index = torch.max(y\_pre, 1)
# 2. 对抗样本生成
input\_image.requires\_grad = True
adv\_pattern = generate\_adversaria...