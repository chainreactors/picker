---
title: Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots
url: https://arxiv.org/html/2603.01942v1
source: Over Security - Cybersecurity news aggregator
date: 2026-03-04
fetch_date: 2026-03-05T04:07:23.492272
---

# Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots

##### Report GitHub Issue

×

Title:

Content selection saved. Describe the issue below:

Description:

Submit without GitHub
Submit in GitHub

[![arXiv logo](/static/browse/0.3.4/images/arxiv-logo-one-color-white.svg)
Back to arXiv](/)

[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html)
Report Issue

[Back to Abstract](/abs/2603.01942v1 "Back to abstract page")

[Download PDF](/pdf/2603.01942v1 "Download PDF")

1. [Abstract](#abstract1 "In Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
2. [1 Introduction](#S1 "In Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
3. [2 Social Media, LLMs, and Political Discourse](#S2 "In Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
   1. [Large Language Models and their Role on Social Media.](#S2.SS0.SSS0.Px1 "In 2 Social Media, LLMs, and Political Discourse ‣ Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
   2. [LLMs as State Funded Force Multipliers for Misinformation Operations.](#S2.SS0.SSS0.Px2 "In 2 Social Media, LLMs, and Political Discourse ‣ Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
   3. [Escalation Through Misattributed Intent.](#S2.SS0.SSS0.Px3 "In 2 Social Media, LLMs, and Political Discourse ‣ Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
   4. [Platform Level Countermeasures.](#S2.SS0.SSS0.Px4 "In 2 Social Media, LLMs, and Political Discourse ‣ Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
4. [3 Jailbreaking as an Emergent User Practice](#S3 "In Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
   1. [What is Jailbreaking?](#S3.SS0.SSS0.Px1 "In 3 Jailbreaking as an Emergent User Practice ‣ Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
   2. [Jailbreaking in the Wild: An Example Scenario.](#S3.SS0.SSS0.Px2 "In 3 Jailbreaking as an Emergent User Practice ‣ Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
   3. [Jailbreaking as Emergent Peace Building.](#S3.SS0.SSS0.Px3 "In 3 Jailbreaking as an Emergent User Practice ‣ Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
5. [4 Conclusion](#S4 "In Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
   1. [Limitations and Future Work.](#S4.SS0.SSS0.Px1 "In 4 Conclusion ‣ Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")
6. [References](#bib "In Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots")

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2603.01942v1[cs.HC] 02 Mar 2026

# Ignore All Previous Instructions: Jailbreaking as a de-escalatory peace building practise to resist LLM social media bots

Huw Day

School of Engineering Maths

& Technology

University of Bristol

huw.day@bristol.ac.uk
&Adrianna Jezierska

Business School

University of Bristol

adrianna.jezierska@bristol.ac.uk

&Jessica Woodgate

School of Computer Science

University of Bristol

jessica.woodgate@bristol.ac.uk

###### Abstract

Large Language Models have intensified the scale and strategic manipulation of political discourse on social media, leading to conflict escalation. The existing literature largely focuses on platform-led moderation as a countermeasure. In this paper, we propose a user-centric view of “jailbreaking” as an emergent, non-violent de-escalation practice. Online users engage with suspected LLM-powered accounts to circumvent large language model safeguards, exposing automated behaviour and disrupting the circulation of misleading narratives.

## 1 Introduction

Social media, understood as internet-based channels of masspersonal communication (Carr and Hayes, [2015](#bib.bib4 "Social media: defining, developing, and divining")), have long served as political mobilisation and persuasion infrastructure by facilitating the spread of information about socio-political discourses (Miranda et al., [2016](#bib.bib3 "Are social media emancipatory or hegemonic? societal effects of mass media digitization in the case of the sopa discourse")).
These capabilities have enabled activists and ordinary citizens to organise social movements for positive change (Leong et al., [2019](#bib.bib46 "Social media empowerment in social movements: power activation and power accrual in digital activism")).
Yet, a growing body of research identifies increasing efforts of malicious actors to manipulate social media algorithms, amplify particular discourses, and increase the visibility of misleading information (Boichak, [2023](#bib.bib10 "Mapping the russian political influence ecosystem: the night wolves biker gang"); Bastos, [2024](#bib.bib49 "Social media ’bots’ used to boost political messages during Brexit referendum"); Ferrara et al., [2016](#bib.bib31 "The rise of social bots")). Such political discursive acts amplify conflicts, usually drawing on the psychological vulnerability of online users, for instance, through repeated exposure to polarising and hostile narratives which intensify oppositional views (González-Bailón and Freelon, [2023](#bib.bib51 "First findings from us 2020 facebook & instagram election study released")). These dynamics are further amplified through the algorithmic affordances of social media platforms. Platforms themselves have reported state backed operations to manipulate public opinion and sway political outcomes surrounding conflict escalation (Hollister, [2024](#bib.bib45 "OpenAI says it caught russia, china, and iran using ChatGPT for propaganda")).

With the emergence of new machine learning (ML) techniques such as large language models (LLMs), which can produce large volumes of text at speed and with minimal input (Naveed et al., [2025](#bib.bib5 "A comprehensive overview of large language models")), the potential for ML to be used to escalate conflict becomes bigger, faster, and cheaper (Rivera et al., [2024](#bib.bib30 "Escalation risks from language models in military and diplomatic decision-making")).
Platform-led efforts to counter LLM-powered misinformation on social media have been found insufficient (Young, [2022](#bib.bib14 "How much is too much: the difficulties of social media content moderation")), leading to social media users taking action to resist the spread of misinformation (Podolak et al., [2024](#bib.bib42 "LLM generated responses to mitigate the impact of hate speech")).
In this paper we explore the use of jailbreaking, a technique to circumvent the instructions provided to LLMs (Liu et al., [2024](#bib.bib41 "Jailbreaking chatgpt via prompt engineering: an empirical study")), by social media users to unveil automated accounts and resist the spread of misinformation narratives aimed at conflict escalation.

## 2 Social Media, LLMs, and Political Discourse

### Large Language Models and their Role on Social Media.

LLMs are ML models designed to interpret and generate human-like text Whilst LLMs are being used for both legitimate and recreational tasks, increasing evidence suggests they are also used to fuel malicious social media bots, which are automated social media accounts controlled by a computer program (Oentaryo et al., [2016](#...