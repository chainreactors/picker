---
title: COBALT ILLUSION Masquerades as Atlantic Council Employee
url: https://www.secureworks.com/blog/cobalt-illusion-masquerades-as-atlantic-council-employee
source: Secureworks Blog
date: 2023-03-10
fetch_date: 2025-10-04T09:10:50.799069
---

# COBALT ILLUSION Masquerades as Atlantic Council Employee

[Skip to Main Content](#main-content)[Skip to Footer](#cmp-footer-a1fbb96a)

[Sophos completes Secureworks acquisition](https://www.sophos.com/en-us/press/press-releases/2025/02/sophos-completes-secureworks-acquisition)

* [Experiencing a Breach?](https://www.sophos.com/en-us/products/incident-response-services/emergency-response)
* Contact Us
* Support
* [Blog](/blog)
* English

[![logo](/-/media/images/logos/logo_new.svg?iar=0&hash=61254867B6545667A8E17DD1352849AF)](/ "Secureworks")

* Platform
* Services
* Solutions
* About
* Partners
* Resources

[Request Demo](/contact/request-demo-xdr)

Research & Intelligence

# COBALT ILLUSION Masquerades as Atlantic Council Employee

The phishing campaign targets researchers who document the suppression of women and minority groups in Iran.

![hands keyboard](/-/media/images/thumbnails/blog/thing-hands-laptop-04.jpg?h=722&iar=0&w=1284&hash=787FDBFE357DC892847E80BCAC627DEB?io=transform:fit,width:4568,height:2568)

[Counter Threat Unit Research Team](/author/Counter-Threat-Unit-Research-Team)

March 9, 2023

Secureworks® Counter Threat Unit™ (CTU) researchers are investigating suspicious activity reported via Twitter on February 24, 2023. Multiple individuals involved in Middle Eastern political affairs research [tweeted](https://twitter.com/_RDadpur_/status/1628733517785075712) that than an individual claiming to work for the U.S. Atlantic Council think tank had contacted them about contributing to an Atlantic Council report in progress. This individual used the name Sara Shokouhi and the [@SaShokouhi](https://twitter.com/SaShokouhi) ([archived](https://archive.is/POxkj)) Twitter account (see Figure 1).

![](/-/media/images/insights/blog/2023/cobalt-illusion-masquerades-as-atlantic-council-employee/figure-01.png)

*Figure 1. Twitter profile for Sara Shokouhi (@SaShokouhi). (Source: Secureworks)*

In these solicitations, the SaShokouhi persona claimed to work with Holly Dagres, an Atlantic Council Senior Fellow. Dagres has publicly denied working with Shokouhi (see Figure 2).

![](/-/media/images/insights/blog/2023/cobalt-illusion-masquerades-as-atlantic-council-employee/figure-02.png)

*Figure 2. Holly Dagres publicly denying that Sara Shokouhi is a colleague. (Source: Secureworks)*

CTU™ researchers discovered that the individual in these photos is not Sara Shokouhi. The image belongs to a psychologist and tarot card reader based in Russia. The threat group responsible for the fake Sara Shokouhi persona stole these images from an Instagram account (see Figure 3) and used them as the basis for the SaShokouhi Twitter account and a corresponding Instagram account (@sarashokouhii). The fake Instagram profile claims Shokouhi was studying for or holds a “PhD in Middle East Polotics [sic]”.

![](/-/media/images/insights/blog/2023/cobalt-illusion-masquerades-as-atlantic-council-employee/figure-03.png)

*Figure 3. Photos stolen from Instagram to create the @SaShokouhi Twitter persona. Secureworks blurred the images for privacy purposes. (Source: Secureworks)*

Multiple hallmarks of this activity suggest involvement of the Iranian [COBALT ILLUSION](https://www.secureworks.com/research/threat-profiles/cobalt-illusion) threat group (also known as Charming Kitten, APT42, Phosphorous, TA453, and Yellow Garuda), which is suspected of operating on behalf of the Intelligence Organization of the Islamic Revolutionary Guard Corp (IRGC-IO) in Iran. COBALT ILLUSION targets a wide range of individuals and is particularly interested in academics, journalists, human rights defenders, political activists, intergovernmental organizations (IGOs), and non-governmental organizations (NGOs) that focus on Iran. The threat actors create a fake persona and then use it to contact a target with a request for an interview, assistance on a report, or to discuss a shared interest. Over a period of days or weeks, COBALT ILLUSION develops a rapport with the target and then attempts to phish credentials or deploy malware to the target's computer or mobile device. The UK National Cyber Security Centre (NCSC) issued an [advisory](https://www.ncsc.gov.uk/files/NCSC_Advisory-SEABORGIUM-and-TA453.pdf) in January that included details of COBALT ILLUSION spearphishing activity.

This would not be the first time the threat actors masqueraded as Atlantic Council employees. In September 2022, CERTFA [identified](https://blog.certfa.com/posts/charming-kitten-can-we-wave-a-meeting/) numerous real individuals that COBALT ILLUSION impersonated, including an Atlantic Council employee. In that campaign, the group attempted to engage targets in video calls and delivered phishing links via the chat function at an appropriate point in the conversation.

The @SaShokouhi account has been operating since October 2022. It tweets or retweets posts supportive of the Mahsa Amini [protests](https://www.theguardian.com/world/ng-interactive/2022/oct/31/mapping-irans-unrest-how-mahsa-aminis-death-led-to-nationwide-protests) in Iran. To appear sympathetic to the protestors' interests and demands, the account owner has posted cynical content such as images of dead children, physical abuse suffered by protesters, anti-Iranian government commentary, and anti-Iranian symbolism.

CERTFA Lab reported a set of phishing [indicators](https://twitter.com/certfalab/status/1629083616268394496) related to this suspicious activity. As of this publication, CTU researchers cannot independently verify an association between the CERTFA indicators and the @SaShokouhi account. However, these indicators align with patterns observed in past COBALT ILLUSION activity.

Multiple targets reported that the SaShokouhi persona engaged them in discussion (see Figure 4). The interactions included requests to visit multiple links.

![](/-/media/images/insights/blog/2023/cobalt-illusion-masquerades-as-atlantic-council-employee/figure-04.png)

*Figure 4. Twitter user reporting that SaShokouhi had contacted them. (Source: Secureworks)*

It is common for COBALT ILLUSION to interact with its targets multiple times over different messaging platforms. The threat actors first send benign links and documents to build rapport. They then send a malicious link or document to phish credentials for systems that COBALT ILLUSION seeks to access. These systems include online email services, social media services, and other systems used by the target.

Phishing and bulk data collection are core tactics of COBALT ILLUSION operations. In August 2022, Human Rights Watch [reported](https://www.hrw.org/news/2022/12/05/iran-state-backed-hacking-activists-journalists-politicians) that COBALT ILLUSION targeted their staff and obtained user credentials. The threat actors then used the [Google Takeout](https://en.wikipedia.org/wiki/Google_Takeout) service to export data from the various services associated with the compromised account, including email, cloud data storage, and contacts. This information could feed into additional rounds of phishing attacks, targeting users of interest who have had contact with the initial victim. In December 2021, the Google Threat Analysis Group (TAG) [reported](https://blog.google/threat-analysis-group/new-iranian-apt-data-extraction-tool/) on COBALT ILLUSION's use of the custom HYPERSCRAPE (also known as EmailDownloader) tool to steal user data from Gmail, Yahoo, and Microsoft accounts. PwC [identified](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/old-cat-new-tricks.html) a similar tool called TelegramGrabber that enabled bulk data collection from Telegram accounts after the threat actor had obtained the victim's credentials. Data stolen from victims' accounts could be used to inform intelligence priorities for the IRGC-IO and other COBALT ILLUSION customers.

To mitigate exposure to this malware, CTU researchers recommend that organizations use available controls to review and restrict access using the indicators listed in Table 1. Note that IP addresses can be reallocate...