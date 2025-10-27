---
title: Risky Biz News: Intel and Arm processors open themselves to timing attacks
url: https://riskybiznews.substack.com/p/risky-biz-news-intel-and-arm-processors
source: Over Security - Cybersecurity news aggregator
date: 2023-01-28
fetch_date: 2025-10-04T05:05:14.716802
---

# Risky Biz News: Intel and Arm processors open themselves to timing attacks

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Intel and Arm processors open themselves to timing attacks

### In other news: FBI hacks Hive ransomware infrastructure; Yandex source code leaked online; Google disrupts major Chinese influence operation.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Jan 27, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

Modern Intel and Arm CPUs expose cryptographic data to timing attacks, Eric Biggers, a software engineer at Google on the Platform Encryption Team, has highlighted in a series of discussions on [mailing](https://www.openwall.com/lists/oss-security/2023/01/25/3) [lists](https://lore.kernel.org/lkml/YwgCrqutxmX0W72r%40gmail.com/T/#u) for the past months.

Timing attacks against cryptography algorithms were discovered in the mid-90s and were proven practically at the start of the 2000s. Researchers proved that by measuring the time it takes for a CPU to process data, they could infer private information, such as an RSA private key. To prevent timing attacks, [constant-time code](https://www.bearssl.org/constanttime.html) capabilities were added to CPUs so the time needed to perform an operation would be relatively constant and independent from the value of the data handled inside the processor.

But Biggers says that for the past few years, both [Intel](https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/best-practices/data-operand-independent-timing-isa-guidance.html) and [Arm](https://developer.arm.com/documentation/ddi0601/2020-12/AArch64-Registers/DIT--Data-Independent-Timing) have disabled by default features in their CPUs that enforce constant-time operations, namely DIT on Arm and DOITM on Intel.

Biggers says the upcoming 6.2 version of the Linux kernel will re-enable DIT inside Arm CPUs, but only for kernel-level code.

"Without any additional patches, userspace code will still get data-dependent timing by default," Biggers says, while no patch is currently scheduled to re-enable DOITM on Intel CPUs at all.

"Thus, as-is, it's not really possible to safely execute cryptographic algorithms on Linux systems that use an Intel processor with Ice Lake or later," Biggers says.

The issue appears to be a disaster waiting to happen, especially as more Arm and Intel CPUs are being shipped worldwide without what any cryptography expert would consider a must-have security feature.

"Constant-time code is super important in crypto to avoid timing attacks," [Jean-Philippe Aumasson](https://www.aumasson.jp/), cryptographer and co-founder & chief security officer at Taurus, a digital assets platform for the banking sector, told *Risky Business News*.

"It's definitely a potential major issue, but I've yet to see an attack PoC that could be exploited in real applications," Aumasson says.

Nevertheless, while attacks have not been spotted in the wild as of yet, research exploring timing attacks has continued over the past two decades, exploring new ways to carry them out. The latest example is new research published last year on a timing attack named [Hertzbleed](https://www.hertzbleed.com/) that can be carried out remotely and impacts all AMD and Intel CPUs on the market.

### **Breaches and hacks**

**Duolingo breach:** A threat actor claims to have collected data on more than 2.6 million Duolingo users by exploiting an exposed application programming interface (API). The hacker is selling the data for $1,500 on a popular underground cybercrime forum. Duolingo said it is investigating the incident. [*See coverage in [The Record](https://therecord.media/duolingo-investigating-dark-web-post-offering-data-from-2-6-million-accounts/)*]

**US federal agencies breached:** The US Cybersecurity and Infrastructure Security Agency (CISA) says that two federal civilian agencies were hacked last year after employees were tricked into downloading legitimate remote access software onto their work computers. Despite gaining access to federal networks, the intruders didn't go after government data and instead focused on performing a refund scam to steal money from the employee's personal bank accounts. CISA says the intrusions appear to be part of a financially motivated phishing campaign that has been going on for months and was previously analyzed by cybersecurity firm [SilentPush](https://www.silentpush.com/blog/silent-push-uncovers-a-large-phishing-operation-featuring-amazon-geek-squad-mcafee-microsoft-norton-and-paypal-domains). The campaign uses various themes to trick victims into installing legitimate remote monitoring and management (RMM) software on their systems, through which the threat actors modify a victim's bank account statements to show extra funds that they want "refunded." CISA has a [technical write-up](https://www.cisa.gov/uscert/ncas/alerts/aa23-025a) on the whole thing.

**South Korean intrusions:** South Korea's cybersecurity agency says that a Chinese hacking group named the Cyber Security Team has launched cyberattacks against South Korean academic institutions. The hackers claimed to have breached more than 70 organizations around the Lunar New Year holiday that took place over the last weekend. The group says it plans to release more than 54 GB of data from the hacked institutions. KISA officials confirmed the attacks but said that only 12 educational institutions suffered breaches. [*Additional coverage via the [Yonhap News Agency](https://en.yna.co.kr/view/AEN20230125002552320)*]

**Digg founder hacked:** Digg founder and crypto enthusiast [Kevin Rose](https://archive.ph/gXYzE) has fallen victim to a phishing attack and signed a malicious transaction that has allowed a hacker to steal more than 40 NFTs. The stolen assets were worth $2 million on Wednesday, $1.4 million on early Thursday, and just $1 million by the afternoon. What a [spectacularly stable](https://archive.ph/z6von) financial ecosystem you have there, crypto-bros!

**Yandex source code leaks:** Some of the source code of Yandex, a Russian search engine and IT software giant, was leaked on the Breached cybercrime forum. The leak appears to be authentic, according to [different](https://arseniyshestakov.com/2023/01/26/yandex-services-source-code-leak/) [sources](https://habr.com/ru/news/t/712992/). Yandex said the source code was leaked by a [former employee](https://habr.com/ru/news/t/712902/). The code contains the source for most major Yandex services, such as Search, Maps, Taxi, Mail, Market, Travel, Cloud, Pay, and many more. Several hardcoded credentials for various cloud servers were also exposed in the leak. All leaked files are dated February 24, 2022, the date of Russia's invasion of Ukraine.

**ADS-B Exchange attacks:** ADS-B Exchange, the website that tracks international flights and the service behind the Elon Musk Tracker, has been the [target](https://mastodon.social/%40JxckS/109756875975085314) of DDoS attacks this week.

### **G...