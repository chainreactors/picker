---
title: Interview #9 MedusaLocker
url: https://deepdarkcti.com/interview-9-medusalocker/
source: Over Security
date: 2026-05-16
fetch_date: 2026-05-17T05:48:10.687108
---

# Interview #9 MedusaLocker

[![deepdarkCTI](https://deepdarkcti.com/wp-content/uploads/2025/02/deepdarkCTI_150_150.png)](https://deepdarkcti.com/)

# [deepdarkCTI](https://deepdarkcti.com)

* [Who Am I](https://deepdarkcti.com/who-am-i/)
* [Blog](https://deepdarkcti.com/blog/)

* [Twitter](https://x.com/fastfire)
* [Telegram](https://t.me/fastfire83)
* [Bluesky](https://bsky.app/profile/fastfire.bsky.social)
* [LinkedIn](https://www.linkedin.com/in/massimo-giaimo-b78ba0a/)

# [Interview #9 MedusaLocker](https://deepdarkcti.com/interview-9-medusalocker/)

May 11, 2026

[![Interview #9 MedusaLocker](https://deepdarkcti.com/wp-content/uploads/2026/05/medusalockerpng.png)](https://deepdarkcti.com/interview-9-medusalocker/)

The following interview, which we publish in full, was conducted in May 2026 by Erez, a member of the deepdarkCTI community.

The MedusaLocker ransomware gang is a persistent cybercriminal operation first observed in late 2019. It operates primarily as a Ransomware-as-a-Service (RaaS) model, where developers provide the malware to affiliates in exchange for a percentage of the ransom profits.

It is critical to distinguish between MedusaLocker and the Medusa (Spearwing/Storm-1175) RaaS group. While both are active in 2026, they are unrelated entities. MedusaLocker is a long-standing family known for its “v3” or BabyLockerKZ variant, whereas the Medusa RaaS group has gained notoriety for triple extortion tactics and massive surges in victim counts during 2025 and 2026.

![](https://deepdarkcti.com/wp-content/uploads/2026/05/image-1024x663.png)

**Q (Erez):** You call yourselves MedusaLocker, but some researchers suggest that your currentoperation may be connected to names such as BAGAJAI or BARADAI. Can you explain the relationship between these names?

**A (Benzona):** MedusaLocker is the name of a family of software used in attacks. BAGAJAI, BARADAI, locked, blackheart and others are file extensions attached to encrypted files so we can identify the victim and apply the correct key.

Changing the file extension may make it impossible to restore the files later. Therefore, I do not see any contradiction regarding the relationship between MedusaLocker and, for example, BAGAJAI.

**Q (Erez):** MedusaLocker is a well-known ransomware group, with 52 published victims, but the original operation appears to have become inactive since November 2025. If you are the same MedusaLocker, why does your new site not include the victims that were published on the original MedusaLocker site, and why do you not clearly use the MedusaLocker name on the new site?

**A (Benzona):** We were busy updating the software and developing a new blog and file manager for publishing files, so the old blog was not updated. I don’t see the point in shoving the name MedusaLocker into every possible place. We earn our name through business, not aggressive marketing. n fact, we have a very strict selection of companies whose files we publish, because we do
not intend to destroy the business. Our philosophy is to show companies that saving money on infrastructure protection is much more expensive.

**Q (Erez):** Does MedusaLocker define itself primarily as a financially motivated organization, a politically motivated organization, or a mix of both?

**A (Benzona):** Yes, we are financially oriented. We do not pursue any political goals.

**Q (Erez):** Where does MedusaLocker draw the line when choosing targets? Are there specific sectors or organizations you refuse to attack for moral, ethical, or humanitarian reasons, such as hospitals, schools, or emergency services?

**A (Benzona)**: We do not work with socially significant organizations, such as social welfare organizations. If we get access to such an organization, we notify them about the vulnerability for free.

**Q (Erez):** For some of the victims listed on your site, the ransom demand is visible, usually
ranging between $10,000 and $80,000. How do you decide the ransom amount for each victim?

**A (Benzona):** This is the price for selling information, which includes an assessment of the potential harm to the company itself, as well as the value of the data. For example, CourtSmart even has the SSN numbers of all their employees, including those who have been laid off. We contacted the organization in various ways, but they apparently did not care about their employees or their profits. They provided video surveillance services for ships. In any case, we are ready to negotiate a price and make some concessions.

**Q (Erez):** Does MedusaLocker use double extortion, meaning both encryption and data exfiltration, or do you sometimes use only one of these methods?

**A (Benzona):** I would not call this “double” extortion, as these are all parts of the same chain. First of all, we discover a vulnerability in the system, and everything else is a consequence.

We consider the so-called “ransom” to be a reward for our work. In any case, the company has the opportunity to neutralize the consequences by preventing data leakage and loss, including user accounts on various web services. Sometimes it does not make sense to copy data or carry out full encryption, so we limit ourselves to one thing.

**Q (Erez):** If you do not encrypt a company’s servers, how do you deliver the ransom note and make sure the victim actually sees it?

**A (Benzona):** As a rule, this is done through an email campaign or a call to the company. Sometimes we send our representative if the company is ready for negotiations. There are situations when we fail to reach the management of the organization, such as with CourtSmart. Then we just publish the data. I am sure they will feel it.

**Q (Erez):** The FBI and global law enforcement agencies have disrupted many ransomware operations in recent years. How has this pressure affected the way ransomware groups operate today? Are you concerned that MedusaLocker could become a law enforcement target?

**A (Benzona):** Everything that happens is quite understandable, logical and expected. The only thing that worries us is the lies from law enforcement and similar agencies, including all kinds of cybersecurity organizations, claiming that the company will not receive anything even if it pays.

We invest a lot of money in improving data decryption approaches, adding file integrity protection and similar features, but we are considered scammers precisely because of law enforcement agencies.

It is doubly disappointing that they do this with their own hands and at the expense of the organizations themselves. That is, both we and the victim suffer simply because someone wanted it that way. And given the intimidation of victims by such authorities, they are ordinary extortionists who offer nothing in return. It would be better for them to switch to “intermediaries”, since they do not help either.

**Q (Erez):** What is the strangest or most unexpected request you have ever received from a victim during negotiations?

**A (Benzona):** In fact, everything is very monotonous. Negotiations usually begin with a story about how hard life is for everyone, and how a company with a turnover of, for example, more than $100 million cannot find $50,000 to pay us.

Then they hide behind illnesses, children who do not exist, as it turns out later, and the like.Therefore, for me, the strangest question was: “How much and where should we transfer the money?” And they transferred it without further discussion.

**Q (Erez):** How is the adoption of AI technologies changing the ransomware ecosystem? Is MedusaLocker using machine learning or generative AI in any part of its activity, such as malware development, automation, victim research, or negotiations?

**A (Benzona**): No, we do not use machine learning in our work.

**Q (Erez):** Every individual, even on unconventional paths, draws inspiration from somewhere. Is there a particular book, film, or public figure that shaped your worldview or influenced your approach?

**A (Benzona):** In fact, the...