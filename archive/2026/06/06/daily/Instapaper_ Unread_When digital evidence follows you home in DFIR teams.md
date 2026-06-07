---
title: When digital evidence follows you home in DFIR teams
url: https://andreafortuna.org/2026/06/05/dfir-analyst-psychological-impact/
source: Instapaper: Unread
date: 2026-06-06
fetch_date: 2026-06-07T06:16:39.323778
---

# When digital evidence follows you home in DFIR teams

[Andrea Fortuna](/)
[ ]

[About](/about/)[Search](/search/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# When digital evidence follows you home in DFIR teams

Jun 5, 2026

by [Andrea Fortuna](/about/)

There is a type of fatigue that does not show up in burnout surveys, does not get discussed in team retrospectives, and does not appear in any CISO dashboard. It accumulates quietly, over months, in people who spend their days reconstructing what happened on a murdered child’s phone, parsing chat logs from a grooming case, or reviewing CCTV footage of a violent assault frame by frame.

![cover](/assets/2026/dfir-analyst-trauma.jpg)

Digital forensic analysts and secondary investigators occupy a peculiar position in the broader law enforcement and cybersecurity ecosystem. They are not frontline officers, not emergency responders, not the people whose faces appear on documentaries about cold cases. They are the civilians in the back office who make the prosecutions possible: the ones who extract, triage, and catalogue evidence that most human beings would struggle to look at once. And because the work is technical rather than physical, because it happens on a screen in an office, the assumption has often been that it is somehow easier to bear.

That assumption does not survive contact with actual data. A [longitudinal study](https://link.springer.com/article/10.1007/s11896-026-09809-2) published in April 2026 in the *Journal of Police and Criminal Psychology*, conducted by Fazeelat Duran and Jessica Woodhams at the University of Birmingham, is among the first to follow newly recruited law enforcement staff from their first day through eighteen months on the job and document what repeated exposure to distressing material actually does to a person over time. The picture that emerges is not pretty.

## What the study found, and why it matters

The research followed twenty-one newly hired crime and intelligence analysts at a UK law enforcement organization across three interview rounds: at six months, twelve months, and eighteen months in post. Sixty-three interviews in total. The participants worked on cases involving sexual assault, homicide, and serious crime, regularly reviewing investigative reports, interview transcripts, recorded interviews, and crime scene or autopsy imagery.

At six months, nobody reported significant distress. The researchers describe participants as being in a training phase: engaged, motivated, still somewhat cushioned by novelty. Most said they “enjoyed” the role. A few noted growing awareness of how frequently crime occurs, a kind of peripheral vigilance starting to form. But no sleep problems. No intrusive thoughts. No significant psychological symptoms.

By twelve and eighteen months, the picture had changed substantially. More than half reported disturbed sleep patterns, including recurrent nightmares directly linked to cases they were working on. A large subset described intrusive thoughts, the kind that arrive unbidden on a quiet road at night or in the back of a taxi. Fourteen participants reported hypervigilance to perceived threats in their personal lives: excessive suspicion of strangers, anxiety about partners walking alone, compulsive security behaviors. Nine described feelings of isolation and loneliness, rooted in the simple fact that you cannot explain what you do all day to the people in your life.

The researchers frame these changes around the concept of “dosage”: the cumulative weight of repeated exposure to distressing material, which does not average out but compounds. Each new case adds to a growing reservoir of intrusive memory rather than displacing the old ones. The study found that as dosage increased, participants increasingly reported experiences consistent with PTSD-like symptoms, depression, and burnout.

The coping strategies evolved too, and not always in useful directions. Early on, participants mostly went with the flow. Later, sixteen of twenty-one described thought suppression as a primary technique, trying to push case-related imagery out of their heads. Eight reported reading material at a surface level as a protective mechanism, staying deliberately shallow to avoid emotional engagement. The researchers note that [both of these strategies](https://link.springer.com/article/10.1007/s11896-022-09532-8) are associated with poorer outcomes over time in the relevant psychological literature: suppression tends to backfire, and shallow engagement can coexist with growing underlying distress.

Eight participants, by the eighteen-month mark, were actively planning to leave the role.

## The DFIR angle that the study does not cover

The Duran and Woodhams research focuses specifically on law enforcement staff in the UK, and its findings are directly applicable to a category of professionals that the cybersecurity and DFIR community tends not to think about in these terms. Incident responders, digital forensic analysts, malware reverse engineers, child exploitation investigators working in digital evidence units, and threat hunters who sift through terabytes of logs looking for indicators of harm sit on the same spectrum.

The specific content varies. A DFIR analyst working a ransomware case is not reviewing CSAM. But the picture is not uniformly benign either. CSAM cases handled by digital forensic units are an obvious pressure point, and anyone who has spent time in a serious case unit will know that the material is rarely limited to the technical artifacts. You encounter what the files contain. You read the communications. You watch the footage.

And beyond the most extreme material, there are subtler accumulations. Months of working homicide cases leave sediment. So do years of processing the wreckage of domestic abuse, financial fraud, and child exploitation, even when you are technically focused only on the data layer. The dosage concept applies here too. Every case adds a frame to the reel.

The cybersecurity industry has invested considerable energy in the past decade into technical burnout: the kind caused by alert fatigue, undersized teams, and the permanent asymmetry between attackers and defenders. There is reasonable awareness that SOC analysts working twenty-four-hour shifts with a hundred alerts per hour is a sustainability problem, as discussed in my post on [24/7 security monitoring for small teams](https://andreafortuna.org/2026/02/05/24-7-security-monitoring-for-small-teams/). The psychological damage from content exposure is a different category of problem, less visible, less discussed, and possibly more corrosive precisely because it tends to be minimized or treated as simply part of the job.

## The organizational machinery that makes things worse

One of the more uncomfortable findings in the Duran and Woodhams study is not about the material itself but about how organizations respond, or fail to respond, to the people handling it. By twelve months, most participants perceived the wellbeing support offered by their employers as generic and institutional: a wellness email that goes to everyone, an online resource portal that no one reads, and the option to flag yourself to a line manager who is equally overloaded. This perception of inadequate support had a name in the study: psychological contract breach. Employees had entered the role with an implicit expectation that the organization would recognize the nature of the work and provide meaningful support. The organization had not delivered on that expectation, and the gap was itself a source of distress.

This will sound familiar to anyone who has led a DFIR team. The post-incident retrospective focuses on technical findings. The team debrief, if it happens at all, covers process improvements. The question of how analysts are doing after three weeks of working a ransomware case that hit a hospital network, where the artifacts they are reviewing inclu...