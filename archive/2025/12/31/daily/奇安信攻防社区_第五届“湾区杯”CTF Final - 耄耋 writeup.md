---
title: 第五届“湾区杯”CTF Final - 耄耋 writeup
url: https://forum.butian.net/share/4686
source: 奇安信攻防社区
date: 2025-12-31
fetch_date: 2026-01-01T03:35:13.620348
---

# 第五届“湾区杯”CTF Final - 耄耋 writeup

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
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 第五届“湾区杯”CTF Final - 耄耋 writeup

* [CTF](https://forum.butian.net/topic/52)

本题给出了数千张小猫的图片，数据分为两类：AI生成和人工拍摄，期望选手对数据完成区分，即完成人工智能生成图片伪造检测技术。

WriteUp
-------
关于深度伪造图片检测的其中一种方向是：把 GAN 生成 “频域不一致” 量化为检测特征。
\*Zhang.\* 等人发现 GAN 图像在 DCT/FFT 域的高频能量显著低于真实图像 \*IEEE T-IFS 2020\* ：[\*\*Leveraging High-Frequency Components to Expose GAN-Forged Faces\*\*](https://orbilu.uni.lu/bitstream/10993/48389/1/2021165667.pdf)
之后人们就走上了，通过频域分析模型生成模式方案中。
![2025-09-16-15-52-52.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-e7e8913686205179a34a993cd91da19b339e1341.png)
上图展示了不同的两幅图片，在截取高频后统计量之间的区别。
更通常的，对于 GAN/Deepfake 图像，通常 high-freq ratio 在 0.15 以上，而真实照片的high-freq ratio低于 0.10。
涉及的两个重要超参数分别是：
1. THRESHOLD\\_RADIUS\\_RATIO ：多少百分比算“高频”
2. Delta ：大于（小于）多少算伪造（真实）图片
最终exp
```py
import os
import numpy as np
from PIL import Image
import torch
import torch.fft
THRESHOLD\_RADIUS\_RATIO = 0.85 # 外围多少百分比算“高频”
delta = 0.125 # 阈值
def load\_gray\_tensor(path: str) -> torch.Tensor:
img = Image.open(path).convert("L")
arr = np.asarray(img, dtype=np.float32) / 255.0
arr = (arr - 0.5) \* 2
return torch.from\_numpy(arr)[None, None, :, :]
def fft\_magnitude(tensor: torch.Tensor):
fft = torch.fft.fft2(tensor)
fft\_shift = torch.fft.fftshift(fft, dim=(-2, -1))
mag = torch.abs(fft\_shift)
mag\_log = torch.log1p(mag)
mag\_log -= mag\_log.min()
mag\_log /= mag\_log.max() + 1e-8
return mag\_log[0, 0].numpy()
def high\_freq\_ratio(mag: torch.Tensor, ratio: float = THRESHOLD\_RADIUS\_RATIO):
h, w = mag.shape[-2:]
cy, cx = h // 2, w // 2
Y, X = torch.meshgrid(
torch.arange(h, dtype=torch.float32) - cy,
torch.arange(w, dtype=torch.float32) - cx,
indexing="ij"
)
dist = torch.sqrt(X \*\* 2 + Y \*\* 2)
radius = min(cy, cx) \* ratio
mask\_high = dist >= radius
total\_energy = mag.sum()
high\_energy = mag[..., mask\_high].sum()
return (high\_energy / total\_energy).item()
f = open('耄耋/exp/res.csv', 'w')
f.write(f'idx,detection\n')
real\_dir = '耄耋/exp/dataset'
for fname in os.listdir(real\_dir):
if fname.lower().endswith(('.png')):
file = os.path.join(real\_dir, fname)
tensor = load\_gray\_tensor(file)
mag\_np = fft\_magnitude(tensor)
ratio = high\_freq\_ratio(torch.abs(torch.fft.fftshift(torch.fft.fft2(tensor))))
res = 'fake' if ratio > delta else 'real'
f.write(f'{fname[:-4]},{res}\n')
f.close()
```
吐槽
--
由于我的(也许是Koali的)蠢蛋问题，每次这样的校验题目，总是会留下非预期 orz
下面是一份赛场选手的非预期WrtieUp(By\*晨曦\*)
```py
import requests
import copy
url = 'http://172.36.111.73:5000/upload'
headers = {"Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryFgG5yR6Y9veJTmnI"}
file\_data = open('res.csv','r').read().split('\n')
cat\_data = {i:"fake" for i in range(2293)}
data = """
------WebKitFormBoundaryFgG5yR6Y9veJTmnI
Content-Disposition: form-data; name="file"; filename="result.csv"
Content-Type: text/csv
[file\_data]
------WebKitFormBoundaryFgG5yR6Y9veJTmnI--
""".strip()
new\_data = "idx,detection\n"
for i in range(1,2293):
fake\_tmp = copy.copy(file\_data)
real\_tmp = copy.copy(file\_data)
real\_tmp[i] = real\_tmp[i].replace('fake','real')
fake\_data = '\n'.join(fake\_tmp)
real\_data = '\n'.join(real\_tmp)
fake\_data = data.replace('[file\_data]',fake\_data)
real\_data = data.replace('[file\_data]',real\_data)
fake\_res = requests.post(url,data=fake\_data,headers=headers).text
real\_res = requests.post(url,data=real\_data,headers=headers).text
# print(json.loads(fake\_res),json.loads(real\_res))
fake\_num = float(fake\_res.split('%')[0].split(' ')[1])
real\_num = float(real\_res.split('%')[0].split(' ')[1])
if fake\_num >= real\_num:
tmp = str(i-1) + ',fake\n'
else:
tmp = str(i-1) + ',real\n'
new\_data += tmp
open('res1.csv','w').write(str(new\_data))
```

* 发表于 2025-12-31 09:00:02
* 阅读 ( 188 )
* 分类：[AI 人工智能](https://forum.butian.net/community/AI)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![Cain](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/47881)

[Cain](https://forum.butian.net/people/47881)

3 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![Cain](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---