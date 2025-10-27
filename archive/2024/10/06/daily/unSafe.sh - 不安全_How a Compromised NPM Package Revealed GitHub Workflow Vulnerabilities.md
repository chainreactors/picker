---
title: How a Compromised NPM Package Revealed GitHub Workflow Vulnerabilities
url: https://buaq.net/go-265685.html
source: unSafe.sh - 不安全
date: 2024-10-06
fetch_date: 2025-10-06T18:48:11.911907
---

# How a Compromised NPM Package Revealed GitHub Workflow Vulnerabilities

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/a4b87c30976505e02a0eb14a6cc89d06.jpg)

How a Compromised NPM Package Revealed GitHub Workflow Vulnerabilities

In December 2023, it was discovered that an NPM package commonly used by decentralized web applicati
*2024-10-5 23:36:30
Author: [hackernoon.com(查看原文)](/jump-265685.htm)
阅读量:9
收藏*

---

In December 2023, it was discovered that an NPM package commonly used by decentralized web applications (dApps) had been compromised. The package in question, @ledgerhq/connect-kit, is maintained by Ledger, a well-known and arguably the most trusted provider of secure hardware wallets. Ironic right?

Well, not really, because the compromised package has nothing to do with the ledger's secure hardware wallets.

However, the incident understandably raised concerns among users about the security of their assets, despite those assets being stored offline in hardware wallets. While the compromised package posed no immediate threat to Ledger's hardware devices, the situation sparked widespread discussion and speculation.

The prevailing theory suggests that the compromise occurred due to a vulnerability in Ledger’s GitHub workflow. It is believed that an attacker exploited a GitHub pull request workflow to gain access to Ledger's NPM keys, enabling them to publish malicious code. The malicious update reportedly caused a secondary window to open when users attempted to connect their wallets.

## **The Experiment**

The incident piqued my curiosity, prompting me to question whether GitHub workflows were inherently flawed or if there was more nuance to the exploit. To explore this, I conducted an experiment to see if I could replicate the vulnerability.

Using an existing open-source repository, I attempted to recreate the exploit. During my testing, I discovered that:

### **1. A pull request can edit a workflow and the new workflow will run immediately after the pull request is made**

The screenshot below displays the contents of a `pipeline.yml` file from the repository I was working with. The pipeline is configured to trigger every push to the main branch, deploying the serverless application to [AWS](https://hackernoon.com/467-stories-to-learn-about-aws?ref=hackernoon.com).

![pipeline.yml](https://images.prismic.io/kadet/e056dae2-d055-4828-a4fd-24c82b9c7ab4_Screenshot+2023-12-14+at+4.17.26%E2%80%AFPM.png?auto=compress%2Cformat&fit=max&w=3840)

I proceeded by creating a new branch within the repository and modifying the pipeline file. The updated configuration was set to trigger the workflow on every pull request, regardless of the branch. The screenshot below illustrates the modified state of the file.

![pipeline.yml](https://images.prismic.io/kadet/07aba128-9326-4ccf-aa18-662b9fe1c563_Screenshot+2023-12-14+at+4.15.44%E2%80%AFPM.png?auto=compress%2Cformat&fit=max&w=3840)

Along with these modifications, I added an instruction to print the `AWS_REGION` GitHub secret, which was already present in the repository. I expected to see the value displayed in the workflow logs after the action was executed successfully.

I then submitted a pull request to the main branch with these changes, and as expected, the modified workflow was triggered and executed successfully, even though the pull request had not been reviewed, approved, or merged! Interesting.

![null](https://prismic-io.s3.amazonaws.com/kadet/da741fd8-162b-44f0-ab1a-7fbf198b6eb5_Screenshot+2023-12-16+at+12.48.37%E2%80%AFAM.png?auto=format&fit=max&w=3840)

As seen in the screenshot above, the workflows triggered by my pull request were executed successfully. You might notice there are two workflow runs displayed, which I will address in the next section. For now, let's focus on the workflow labeled "test: modified GitHub workflows" at the bottom.

Once the workflow was completed, I reviewed the logs, and as expected, the `AWS_REGION` GitHub secret was masked, as shown in the following image. This outcome was anticipated, as I had previously encountered a similar article detailing this kind of exploit, which informed my approach to this experiment.

![workflow logs](https://images.prismic.io/kadet/01424b06-7ee6-4de2-8cd5-955c7d263907_Image+14-12-2023+at+4.23%E2%80%AFPM.JPG?auto=compress%2Cformat&fit=max&w=3840)

Now, if the secrets were concealed, how did the attacker manage to access them? This question led to my second key finding:

### **2. GitHub secrets can be exposed by making** curl **requests to third-party APIs within a modified workflow**

Yeah, you read that right! To test this, I further edited the workflow to include a request to a RequestBin I created on [Pipedream](https://pipedream.com/requestbin?ref=hackernoon.com). The screenshot below illustrates the updated workflow.

![modified pipeline.yml](https://images.prismic.io/kadet/909e95d4-aea2-4f8a-aa58-c1e686cd7bd6_Screenshot+2023-12-14+at+4.16.24%E2%80%AFPM.png?auto=compress%2Cformat&fit=max&w=3840)

This explains the second workflow run shown in the earlier screenshot, confirming that both workflows were executed successfully.

On Pipedream's RequestBin, I was able to view the GitHub "secret" in plain text. This raised a concerning question: could anyone simply submit a pull request to an open-source project and easily access sensitive keys?

## **Securing Your Workflows**

Given the potential vulnerabilities uncovered during this experiment, it’s crucial to understand how to secure GitHub workflows to prevent unauthorized access to sensitive data. [GitHub](https://hackernoon.com/338-stories-to-learn-about-github?ref=hackernoon.com) provides several settings that can be configured to reduce the risk of exploitation:

* **Actions permissions setting:**

  By default, all actions are permitted to run, regardless of the author. For enhanced security, this setting should be updated to limit permissions, ensuring that only trusted workflows can execute.
* **Fork pull-request workflows from outside collaborators setting:**

  This setting defines which outside collaborators require approval to run workflows in pull requests. Properly configuring this setting is critical, as misconfiguration could expose your repository to potential exploits.

Additionally, GitHub’s documentation notes that workflows triggered from forks do not have access to sensitive data like secrets. This emphasizes the importance of reviewing the settings for repositories where sensitive data is handled.

By implementing these security measures, repositories can significantly reduce the likelihood of similar vulnerabilities being exploited.

## **Possible Explanations for the Exploit**

Taking all of the above factors into consideration, if the rumors are accurate and Ledger's NPM secrets were indeed compromised, a few scenarios might explain how this occurred:

* **CASE #1:** The package maintainers overlooked the configuration settings and allowed the compromised workflows to run.
* **CASE #2:** The attacker somehow obtained full write access to the repository.
* **CASE #3**: The attacker is, or was, a previous contributor to the project.
* **CASE #4:** The exploit was carried out as an inside job.

## **My Analysis**

Upon reviewing these scenarios, I believe that CASE #3 is the most plausible explanation. A previous contributor may not need explicit approval to trigger workflows in the repository, making it easier to exploit this vulnerability.

I have seen various discussions on social media suggesting that a former employee’s account might have been compromised, which would support CASE #3. However, until an official statement is released by Ledger, the exact cause remains speculative.

## **...