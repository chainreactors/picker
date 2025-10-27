---
title: Geedge & MESA Leak: Analyzing the Great Firewall’s Largest Document Leak
url: https://gfw.report/blog/geedge_and_mesa_leak/en/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-14
fetch_date: 2025-10-02T20:09:17.822326
---

# Geedge & MESA Leak: Analyzing the Great Firewall’s Largest Document Leak

[Great Firewall Report](../../../en)

* [Home](../../../en)
* Publications

  [FOCI 20](../../../publications/foci20_dns/en)
  [IMC 20](../../../publications/imc20/en)
  [USENIX Security 23](../../../publications/usenixsecurity23/en)
  [NDSS 25](../../../publications/ndss25/en)
  [S&P 25](../../../publications/sp25/en)
  [USENIX Security 25](../../../publications/usenixsecurity25/en)
* [English | 中文](../zh)

# Geedge & MESA Leak: Analyzing the Great Firewall’s Largest Document Leak

**Authors:** Mingshi Wu

[中文版: *积至公司与MESA实验室：防火长城史上最大规模文件外泄分析*](../zh)

* [Net4People Post](https://github.com/net4people/bbs/issues/519)
* [Related Tweets](https://x.com/gfw_report/status/1966669581302309018)
* [Related Telegram Channel Posts](https://t.me/GFWReportChannel/62)

Release Date: Friday, September 12, 2025

Last Modified: Friday, September 12, 2025

## 1. Introduction

The Great Firewall of China (GFW) experienced the largest leak of internal documents in its history on Thursday September 11, 2025. Over 500 GB of source code, work logs, and internal communication records were leaked, revealing details of the GFW’s research, development, and operations.

The leak originated from a core technical force behind the GFW: Geedge Networks (whose chief scientist is Fang Binxing) and the MESA Lab at the Institute of Information Engineering, Chinese Academy of Sciences. The documents show that the company not only provides services to governments in places like Xinjiang, Jiangsu, and Fujian, but also exports censorship and surveillance technology to countries such as Myanmar, Pakistan, Ethiopia, Kazakhstan, and other unidentified country under the “Belt and Road” framework.

The significance and far-reaching implications of this leak are substantial. Due to the massive volume of data, GFW Report will continue to analyze and provide updates on [the current page](https://gfw.report/blog/geedge_and_mesa_leak/en/) and on the [Net4People](https://github.com/net4people/bbs/issues/519).

## 2. Download Link

[Enlace Hacktivista](https://enlacehacktivista.org/index.php/Geedge_Networks) has provided the access to the leak:

* BitTorrent: <https://enlacehacktivista.org/geedge.torrent>
* Direct HTTPS download: <https://files.enlacehacktivista.org/geedge/>

The leaked files total about **600 GB**. Among them, the file `mirror/repo.tar` alone, as an archive of the RPM packaging server, takes up **500 GB**.

For detailed instructions on how to use the specific files, David Fifield has [already provided a more thorough explanation on Net4People](https://github.com/net4people/bbs/issues/519#issuecomment-3286329872).

```
     7206346  mirror/filelist.txt
497103482880  mirror/repo.tar
 14811058515  geedge_docs.tar.zst
  2724387262  geedge_jira.tar.zst
 35024722703  mesalab_docs.tar.zst
 63792097732  mesalab_git.tar.zst
       71382  A HAMSON-EN.docx
       16982  A Hamson.docx
      161765  BRI.docx
       14052  CPEC.docx
     2068705  CTF-AWD.docx
       19288  Schedule.docx
       26536  TSG Solution Review Description-20230208.docx
      704281  TSG-问题.docx
       35040  chat.docx
       27242  ty-Schedule.docx
      111244  待学习整理-23年MOTC-SWG合同草本V.1-2020230320.docx
       52049  打印.docx
      418620  替票证明.docx
      260551  领导修改版-待看Reponse to Customer's Suggestions-2022110-V001--1647350669.docx
```

## 3. Safety Considerations

Due to the highly sensitive nature of these leaked materials, we strongly advise anyone who chooses to download and analyze them to take proper operational security precautions. It may be possible that these files may contain potentially risky content and accessing them in an insecure environment could expose you to surveillance or malware.

Please consider analyzing these files only in an isolated (virtual) machine without internet access.

## 4. Background

Great Firewall of China (GFW) is an umbrella term for a series of Internet censorship systems. Behind it, teams for research and development, operations, hardware, and management each play their roles and coordinate with one another. In addition to fixed government agencies (such as the CNCERT), different entities provide technical support depending on individual contracts and tenders. This leak originates from an important branch of the GFW’s **R&D capacity**: Geedge Networks and MESA Lab. The MESA lab is affiliated with the Institute of Information Engineering, Chinese Academy of Sciences (IIE, CAS).

The origins trace back to Fang Binxing, the “Father of the Great Firewall”, coming to Beijing. At the end of 2008, he established the National Engineering Laboratory for Information Content Security (NELIST), initially based at the Institute of Computing Technology, Chinese Academy of Sciences. Beginning in 2012, the supporting institution changed to the Institute of Information Engineering, Chinese Academy of Sciences. In January 2012, some NELIST personnel formed a team at IIE, and in June 2012 the team was officially named the Processing Architecture Team, English name MESA (Massive Effective Stream Analysis). Below is an excerpt from MESA’s self-introduction:

```
MESA Timeline

   January 2012: Liu Qingyun, Sun Yong, Zheng Chao, Yang Rong, Qin Peng, Liu Yang, and Li Jia formed a team at IIE;
   June 2012: The team was officially named the Processing Architecture Team, English name MESA (Massive Effective Stream Analysis);
   2012: Liu Qingyun was selected for IIE’s inaugural “Rising Star” talent program;
   2012: Yang Wei and Zhou Zhou joined the team;
   2012: The team successfully completed the cybersecurity assurance task for the 18th National Congress;
   January 2013: MESA’s first PhD trainee, Liu Tingwen, graduated successfully;
   2013: Li Shu, Liu Junpeng, and Liu Xueli joined the team;
   December 2013: The MESA team received IIE’s 2013 Major Scientific and Technological Progress Award;
   2014: Zhou Zhou was selected for IIE’s “Rising Star” talent program;
   2014: The MESA component SAPP platform began large-scale engineering deployment;
   2014: Zhang Peng, Yu Lingjing, and Jia Mengdie joined the team;
   2015: Zheng Chao was selected for IIE’s “Rising Star” talent program, and Zhang Peng was selected for IIE’s “Outstanding Talent Introduction” program;
   August 2015: MESA moved from the Agriculture Bureau to the Huayan Beili office area;
   July 2015: PhD student Sha Hongzhou trained by MESA graduated successfully, and Liu Xiaomei received Outstanding Graduate honors;
   2016: Dou Fenghu, Zhu Yujia, Wang Fengmei, Li Zhao, Lu Qiuwen, Du Meijie, Shen Yan, and Fang Xupeng joined MESA in succession, and the team expanded rapidly;
   2016: The team undertook multiple major engineering projects, with annual contracted revenue exceeding 35 million;
   December 2016: The MESA team participated in winning the National Science and Technology Progress Award (Second Prize);
   2018: Sun Yong and Zhou Zhou received the 2017 National State Secrecy Science and Technology Award (Second Prize);
```

By 2018, Fang Binxing had also established himself in Hainan, and Geedge (Hainan) Information Technology Co., Ltd. (Geedge Networks Ltd.) was founded in the same year. Fang served as chief scientist, and the “core R&D personnel came from universities and research institutes such as the Chinese Academy of Sciences, Harbin Institute of Technology, and Beijing University of Posts and Telecommunications.” Much of this talent came from MESA—for example, Zheng Chao served as CTO. Attentive readers will notice that many mentors and students from the MESA timeline appear in the leaked Geedge company git commits.

## 5. Analysis of Non–Source Code Files

The non–source-code portion of the leaked files has already been analyzed in detail by multiple professional teams, including, but not limited to,
InterSecLab, Amnesty International, Justice for Myanmar, The Globe and Mail, Der Standard, and Follow the Money. David Fifield has [collected and compiled](https://github.com/net4people/bbs/issues/519#issue-3399074599) ...