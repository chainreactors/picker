---
title: Google links axios supply chain attack to North Korean group
url: https://therecord.media/google-links-axios-supply-chain-attack-north-korea
source: Over Security - Cybersecurity news aggregator
date: 2026-03-31
fetch_date: 2026-04-01T04:47:25.726531
---

# Google links axios supply chain attack to North Korean group

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![malware](https://cms.therecord.media/uploads/large_files_malware_getty_images_1088969572.jpg)

Image: Getty Images via Unsplash

[Jonathan Greig](/author/jonathan-greig)March 31st, 2026

# Google links axios supply chain attack to North Korean group

Hackers connected to North Korea are responsible for the recent compromise of a wildly popular library used in both front-end apps and back-end systems, according to new researcher.

On Monday evening, news emerged that hackers launched a supply chain attack targeting the HTTP client [axios](https://www.npmjs.com/package/axios), which is downloaded 100 million times each week and embedded across frontend frameworks, backend services and enterprise applications.

Google Threat Intelligence Group (GTIG) joined several other researchers in attributing the attack to a North Korean threat actor they call UNC1069. SentinelOne [found](https://www.sentinelone.com/blog/bluenoroff-how-dprks-macos-rustbucket-seeks-to-evade-analysis-and-detection/) the same group using macOS-based malware in attacks dating back to 2023.

Last month, the financially-motivated group [was accused](https://therecord.media/north-korean-hackers-targeted-crypto-exec-clickfix) of targeting a cryptocurrency company with several unique pieces of malware deployed alongside multiple scams, including a fake Zoom meeting.

Several other researchers [backed](https://x.com/DefSecSentinel/status/2038846166394167324) Google’s assessment because the backdoors used during the axios attack resemble WAVESHAPER, a strain of malware North Korean actors used during the fake Zoom campaign.

John Hultquist, chief analyst at Google Threat Intelligence Group, said the axios incident is unrelated to [another recent supply chain attack](https://therecord.media/supply-chain-attack-hits-widely-used-ai-package) that caused alarm among security experts due to its widespread nature.

Hultquist noted that North Korean hackers “have deep experience with supply chain attacks, which they’ve historically used to steal cryptocurrency.” A [2023 supply-chain attack](https://therecord.media/3cx-attack-north-korea-lazarus-group) on the enterprise phone company 3CX was attributed to North Korean hackers.

“The full breadth of this incident is still unclear, but given the popularity of the compromised package, we expect it will have far reaching impacts,” Hultquist said.

Experts raised alarms early on Tuesday morning when two malicious versions of the axios package were published on the Node Package Manager (npm).

Security companies [Socket](https://socket.dev/blog/axios-npm-package-compromised) and [StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan) confirmed the packages were malicious and traced the incident back to the hijacking of the lead axios maintainer’s npm account.

Socket said the malicious package deploys a multi-stage payload, including a “remote access trojan (RAT) capable of executing arbitrary commands, exfiltrating system data, and persisting on infected machines.”

“When the attack first happened, axios maintainers were unable to regain control of the project. In a public GitHub issue, a collaborator stated they could not revoke access from the account responsible for the malicious publish, noting that the attacker’s permissions exceed their own,” Socket explained.

Axios is among the most popular JavaScript HTTP client libraries and is used by developers to connect apps to the internet. StepSecurity said that this is “among the most operationally sophisticated supply chain attacks ever documented against a top-10 npm package.”

The malicious version injects a new dependency that installs the malware, which impacts Windows, macOS and Linux. After executing, the malware deletes itself and replaces it with a clean version of the tool to evade detection, StepSecurity added.

“There are zero lines of malicious code inside axios itself, and that's exactly what makes this attack so dangerous,” the researchers said.

The incident marks the latest in a string of compromises involving the software supply chain, which is increasingly tied together through code pulled in from outside sources.

Last week’s attack on the widely used open-source Python package [LiteLLM](https://therecord.media/supply-chain-attack-hits-widely-used-ai-package) allowed cybercriminals to breach several organizations. Previous incidents involving [XZ Utils](https://therecord.media/researchers-stop-credible-takeover-xz-utils) and [self-replicating worm Shai-Hulud](https://therecord.media/cisa-urges-software-reviews-malicious-packages) stood out among a sea of research uncovering more and more npm packages [that have been corrupted](https://therecord.media/malware-found-in-npm-package-with-millions-of-weekly-downloads?cf=).

Mandiant CTO Charles Carmakal said the number of recent software supply chain attacks is overwhelming.

“The secrets stolen over the past two weeks will enable more software supply chain attacks, software-as-a-service environment compromises (leading to downstream customer compromises), ransomware and extortion events, and crypto heists over the next several days, weeks, and months,” he said.

“We are aware of hundreds of thousands of stolen credentials. A variety of actors with varied motivations are behind these attacks. The blast radius of yesterday's axios npm supply chain attack is broad and extends to other popular packages that have dependencies on it.”

Mike Puglia, a security leader at Kaseya, said the incidents are further evidence of the fragility of the world's software ecosystem.

“In this case, the attacker compromised one single account, the maintainer of axios, and the malicious code was ‘live’ for almost three hours before discovery. On a typical day, that could mean tens of thousands of organizations received the malware,” Puglia said.

To further complicate matters, after the attacker's remote access was deployed, the malware replaced itself with the legitimate axios files, making it difficult to know if you were compromised, he added.

Several other experts warned that the recent attacks on axios and LiteLLM would be templates for other hackers to replicate.

* [Cybercrime](/police-dismantle-dark-web-network-exploiting-child-abuse-images)
* [News](/)
* [Technology](/news/technology)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [CISA tells federal agencies to patch Citrix NetScaler bug by ThursdayMarch 31st, 2026](/cisa-tells-federal-agencies-to-patch-citr...