---
title: [系统安全] 六十二.恶意软件分析 (13)LLM赋能实现基于机器学习的恶意家族分类（初探）
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501299&idx=1&sn=c461a9440fcea0ecee2c1d78cdda5cdd&chksm=cfcf753ef8b8fc289095d45e909b053dcb87dd4794e462fcf1d60ee5c8e7715cc2f2f8c2af13&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2025-02-03
fetch_date: 2025-10-06T20:36:00.761025
---

# [系统安全] 六十二.恶意软件分析 (13)LLM赋能实现基于机器学习的恶意家族分类（初探）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9RqEzqQ5oFBf0rn0Wuzt1lfiaL9xAyw5R8TRmHdRcwz0icicWUShxzic5ghQ/0?wx_fmt=jpeg)

# [系统安全] 六十二.恶意软件分析 (13)LLM赋能实现基于机器学习的恶意家族分类（初探）

原创

Eastmount

娜璋AI安全之家

> 2024年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9RujXz10hUiaqGBEeGK2ibe0KUfwu5rBYEAnluHZ0cAKLqASZvicFRJJ3Mw/640?wx_fmt=png&from=appmsg)

**感谢读者2024年对本公众号的支持。新的一年继续分享干货，共同进步，感恩同行 ^\_^**

该系列文章将系统整理和深入学习系统安全、逆向分析和恶意代码检测，文章会更加聚焦，更加系统，更加深入，也是作者的慢慢成长史。漫漫长征路，偏向虎山行。享受过程，一起奋斗~

**前文探索了利用大模型辅助恶意代码分析，即LLM赋能Lark工具提取XLM代码的抽象语法树。这篇文章将继续尝试探索利用大模型辅助恶意代码分析，尝试进行恶意代码家族分类实验。在恶意代码分析过程中，大家会遇到各种各样的问题，如何结合LLM和GPT完成复杂任务，更好地为安全工程师合作至关重要。基础性探索文章，还请各位大佬多多指教，写得不足之处请海涵。希望您喜欢，且看且珍惜。**

文章目录：

* **一.数据预处理**

+ 1.提取关键特征列
+ 2.恶意家族选择预处理

* **二.数据集划分及统计分析**
* **三.大模型构建机器学习代码**

+ 1.随机森林
+ 2.其它方法

* **四.传统机器学习代码对比**
* **五.评价及总结**

作者的github资源：

* 逆向分析：

+ https://github.com/eastmountyxz/

  SystemSecurity-ReverseAnalysis

* 网络安全：

+ https://github.com/eastmountyxz/

  NetworkSecuritySelf-study

作者作为网络安全的小白，分享一些自学基础教程给大家，主要是关于安全工具和实践操作的在线笔记，希望您们喜欢。同时，更希望您能与我一起操作和进步，后续将深入学习网络安全和系统安全知识并分享相关实验。总之，希望该系列文章对博友有所帮助，写文不易，大神们不喜勿喷，谢谢！如果文章对您有帮助，将是我创作的最大动力，点赞、评论、私聊均可，一起加油喔！

![](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDROZ0FiaQhr7u82U6dJibrM3VO0dUcD3EMLylohBICfH8ibt9D8T7r2jcvDCAFuf4VR5IhcypN5mvCSVg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

> 声明：本人坚决反对利用教学方法进行犯罪的行为，一切犯罪行为必将受到严惩，绿色网络需要我们共同维护，更推荐大家了解它们背后的原理，更好地进行防护。（参考文献见后）

---

# 一.数据预处理

假设存在一个恶意代码家族数据集（如恶意软件、APT攻击、Powershell家族、宏代码家族、Android恶意软件、流量攻击类型家族等），该数据集是将恶意软件脱壳、解混淆处理并提取关键特征所生成的数据集，现需要对其进行大模型赋能的安全分析尝试。

## 1.提取关键特征列

整个数据集包括6列内容，首先需要利用大模型提取关键的前3列特征。

* 第1列：家族名称
* 第2列：文件名称（MD5）
* 第3列：Word字符串特征
* 第4列：Token特征
* 第5列：API行为特征
* 第6列：AST特征

利用大模型构建提取前3列特征的提示词为：

> 提示1：
> 输入CSV文件包含6列，第一列为家族名称，第二列为文件名称，第三列为Word特征，第四列为Token特征，第五列为API行为特征，第六列为AST特征，每行对应一个样本。现需要仅保留前3列内容，从上往下顺序依次遍历，最终输出处理后的CSV文件。请给出对应的Python代码。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9RzmFdv3hicQ8ETdCgjPPWrjc8OL7U2j6ZrOTJFUka3AVyOS51X3vPUPA/640?wx_fmt=png&from=appmsg)

生成代码如下所示：

```
# By: Eastmount CSDN 2025-02-02import pandas as pd
# 读取CSV文件file_path = "filtered_final_features_with_ast_rela.csv"  # 请替换为您的文件路径df = pd.read_csv(file_path)
# 仅保留前3列df_filtered = df.iloc[:, :3]
# 保存处理后的CSV文件output_file = "filtered_final_features_reduced.csv"df_filtered.to_csv(output_file, index=False)
print(f"处理后的CSV文件已保存为：{output_file}")
```

输出结果如下图所示，成功提取前3列特征。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9R0jUzwkQPNaiaHuhYpDZS3KicdKANXrNkWw2tbgJ5qEq3Ra5r8e5txLYg/640?wx_fmt=png&from=appmsg)

---

## 2.恶意家族选择预处理

在某些情况下，存在某类家族或类别数据集较少的情况，此时可以通过数据增强或收集更多的样本丰富数据集。另一种比较暴力的方法是进行删除，不建议大家如此，但该博客是对LLM赋能安全分析的尝试，因此进行恶意家族选择处理。提示词如下：

> 提示2：
> 请撰写python代码处理CSV文件数据。输入CSV文件“data.csv”包含3列，第一列为家族名称，第二列为文件名称，第三列为Word特征，每行对应一个样本。现在需要仅保留四个家族的数据集，family\_features = [“zloader”, “dridex”, “encdoc”, “qakbot”]，家族名称为第一列，不在四个家族的数据删除。具体步骤为：与第一列家族名称进行匹配，匹配成功的整行数据保留。需要注意，输入CSV文件从上往下顺序依次不变，请撰写Python代码实现。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9Rt3h78oUvXCa79KyqZTTaYaDjviaibt1diaL1Dq0zqf9uCbTuvibIgDjiaog/640?wx_fmt=png&from=appmsg)

```
# By: Eastmount CSDN 2025-02-02import pandas as pd
# 指定要保留的家族名称family_features = ["zloader", "dridex", "encdoc", "qakbot"]
# 读取CSV文件file_path = "data.csv"  # 请确保data.csv在相应目录下df = pd.read_csv(file_path)
# 仅保留家族名称匹配的行df_filtered = df[df.iloc[:, 0].isin(family_features)]  # 第一列（家族名称）匹配
# 保存处理后的CSV文件output_file = "filtered_data.csv"df_filtered.to_csv(output_file, index=False, encoding="utf-8")
print(f"处理后的CSV文件已保存为：{output_file}")
```

输出结果如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9RQiaSYtka0GAxsNjWPicShiaKiaM47kA4q0o2FBsSbtdVR5rKOicBsJYnGFQ/640?wx_fmt=png&from=appmsg)

---

# 二.数据集划分及统计分析

接下来进行数据集划分，机器学习通常划分为训练集和测试集，深度学习还会划分验证集。数据集划分的提示如下：

> 提示3：
> 请撰写python代码处理CSV文件数据。输入CSV文件“filtered\_data.csv”包含3列，第一列为家族名称，第二列为文件名称，第三列为Word特征，每行对应一个样本。现在需要按照7:3的比例将整个CSV数据集随机划分为训练集和测试集，保证每个家族均按照该比例，输出训练集文件名称为“filtered\_data\_train.csv”，测试集文件名称为“filtered\_data\_test.csv”。需要注意，输入CSV文件从上往下顺序依次不变，请撰写Python代码实现。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9RaGiagLPgcxqUIDKicezoRA8keKyXI1bbsY5DjRVpMbq2NMTMObucibQJA/640?wx_fmt=png&from=appmsg)

此代码可确保每个家族都按照7:3的比例分割，并保持数据的原始顺序，适用于分类任务的数据准备。代码说明：

* 按家族（第一列）分组，确保每个家族独立划分训练集和测试集。
* 使用train\_test\_split()：test\_size=0.3（即 30% 的数据作为测试集）。random\_state=42 确保可复现性。shuffle=True 确保随机性，避免数据分布不均。
* 保持数据的原始顺序：分组时不排序（sort=False），保证原始顺序不变。每个家族分别划分，然后合并训练集和测试集，最终输出文件。
* 生成两个CSV文件：filtered\_data\_train.csv（训练集）、filtered\_data\_test.csv（测试集）。

```
# By: Eastmount CSDN 2025-02-02import pandas as pdfrom sklearn.model_selection import train_test_split
# 读取CSV文件file_path = "filtered_data.csv"  # 输入文件df = pd.read_csv(file_path)
# 按家族名称进行分组，分别划分训练集和测试集train_list = []test_list = []
for family, group in df.groupby(df.columns[0], sort=False):  # 按第一列（家族名称）分组，保持顺序    train, test = train_test_split(group, test_size=0.3, random_state=42, shuffle=True)  # 7:3划分    train_list.append(train)    test_list.append(test)
# 合并所有家族的数据train_data = pd.concat(train_list)test_data = pd.concat(test_list)
# 保存训练集和测试集train_output = "filtered_data_train.csv"test_output = "filtered_data_test.csv"
train_data.to_csv(train_output, index=False, encoding="utf-8")test_data.to_csv(test_output, index=False, encoding="utf-8")
print(f"训练集已保存为：{train_output}")print(f"测试集已保存为：{test_output}")
```

输出结果如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9Rn93Fo6OpoH8JmicUF9xQhHRjHgbrF7yhKG0WFictfzHrGjGD0IjAQ35Q/640?wx_fmt=png&from=appmsg)

此外，我们可以统计各家族数量，提示如下：

> 提示4：
> 请撰写python代码处理CSV文件数据。输入CSV文件“filtered\_data.csv”包含3列，第一列为家族名称，第二列为文件名称，第三列为Word特征，每行对应一个样本。现在需要撰写代码统计各个家族的数量，即第一列。

```
# By: Eastmount CSDN 2025-02-02import pandas as pd
# 读取CSV文件file_path = "filtered_data.csv"  # 输入文件df = pd.read_csv(file_path)
# 统计每个家族的数量family_counts = df.iloc[:, 0].value_counts()
# 打印统计结果print(family_counts)
# 可选：保存统计结果到CSV文件output_file = "family_counts.csv"family_counts.to_csv(output_file, header=["Count"])
print(f"各个家族的数量统计已保存至：{output_file}")
```

输出结果如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9R8UVqffRZl8MNBkFX3UBfLoyl6OMWxErv4RScQibByNxhVYFfZl4LlAA/640?wx_fmt=png&from=appmsg)

---

# 三.大模型构建机器学习代码

接下来我们将利用大模型GPT4o生成机器学习代码来实现恶意家族特征学习和分类。提示如下：

## 1.随机森林

> 提示5：
> 现在需要撰写Python机器学习代码，构建随机森林模型实现文本分类。输入文本为2个CSV文件，训练集“filtered\_data\_train.csv”、测试集“filtered\_data\_test.csv”。每个CSV文件包含3列，第一列为家族名称，第二列为文件名称，第三列为Word特征，每行对应一个样本，总共四个家族。现在需要完成：
> （1）分别提取CSV文件的第一列家族名称（标题Family），第三列Word特征（标题WordFeature），然后赋值到训练集、测试集中，家族名称作为类别，Word特征作为文本序列，已采用空格连接。
> （2）利用Sklearn构建随机森林模型，并进行训练和测试，需将文本表征为TF-IDF再进行训练学习。
> （3）最后实现对测试集文件的预测，并给出评估的结果，包括各个家族的精确率、召回率、F1值和准确率。同时将真实列表结果和预测结果存储至CSV文件中，便于后续分析。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9Rnx3fpp7Xbm5KW8hHG6Vy8AcYyH1w7ib49oW4M4DsRSVPM2Hib09ZakVA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9RbjTxCicYQ4B5CXWTYKDmBG06SufKzuUtjdhpRiaokGibz280wEWKf7YyQ/640?wx_fmt=png&from=appmsg)

生成代码如下所示：

```
# By: Eastmount CSDN 2025-02-02import pandas as pdfrom sklearn.feature_extraction.text import TfidfVectorizerfrom sklearn.ensemble import RandomForestClassifierfrom sklearn.metrics import classification_report, accuracy_score
# 读取训练集和测试集train_file = "filtered_data_train.csv"test_file = "filtered_data_test.csv"
train_df = pd.read_csv(train_file)test_df = pd.read_csv(test_file)
# 提取家族名称（类别标签）和Word特征（文本数据）X_train_text = train_df.iloc[:, 2]  # 第三列 WordFeature 作为文本输入y_train = train_df.iloc[:, 0]  # 第一列 Family 作为类别标签
X_test_text = test_df.iloc[:, 2]y_test = test_df.iloc[:, 0]
# TF-IDF 向量化vectorizer = TfidfVectorizer()X_train_tfidf = vectorizer.fit_transform(X_train_tex...