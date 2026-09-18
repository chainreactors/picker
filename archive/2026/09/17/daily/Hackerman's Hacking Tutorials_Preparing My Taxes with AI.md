---
title: Preparing My Taxes with AI
url: https://parsiya.net/blog/tax-ai/
source: Hackerman's Hacking Tutorials
date: 2026-09-17
fetch_date: 2026-09-18T06:52:21.658363
---

# Preparing My Taxes with AI

# [Hackerman's Hacking Tutorials](https://parsiya.net/)

## The knowledge of anything, since all things have causes, is not acquired or complete unless it is known by its causes. - Avicenna

Navigate…» About Me!» Cheat Sheet» My Clone» Source Repo» Manual Work is a Bug» The Other Guy from Wham!

* [About Me!](https://parsiya.net/about/ "About Me!")
* [Cheat Sheet](https://parsiya.net/cheatsheet/ "Cheat Sheet")
* [My Clone](https://parsiya.io/ "My Clone")
* [Source Repo](https://github.com/parsiya/parsiya.net "Source Repo")
* [Manual Work is a Bug](https://queue.acm.org/detail.cfm?id=3197520 "Manual Work is a Bug")
* [The Other Guy from Wham!](https://www.google.com/search?q=andrew+ridgeley "The Other Guy from Wham!")

Sep 17, 2026
- 10 minute read - [Not Security](https://parsiya.net/categories/not-security/) [AI](https://parsiya.net/categories/ai/)

# Preparing My Taxes with AI

* [Motivation and Problem Statement](#motivation-and-problem-statement)
* [Methodology](#methodology)
  + [Steps 1 and 2: PDF Conversion and Audit](#steps-1-and-2-pdf-conversion-and-audit)
    - [IRS Wage and Income Transcript](#irs-wage-and-income-transcript)
  + [Step 3: Creating the Packet for the Tax Preparer](#step-3-creating-the-packet-for-the-tax-preparer)
    - [Estimated Tax Payments and Extensions](#estimated-tax-payments-and-extensions)
  + [Step 4: Using the Previous Return as a Blueprint](#step-4-using-the-previous-return-as-a-blueprint)
    - [Currency Conversion Needed Its Own Check](#currency-conversion-needed-its-own-check)
    - [States and US-Canada Tax Treaty](#states-and-us-canada-tax-treaty)
  + [Step 5: Reviewing the Draft Return](#step-5-reviewing-the-draft-return)
    - [The Mega Backdoor Roth Example](#the-mega-backdoor-roth-example)
* [What Did We Learn Here Today?](#what-did-we-learn-here-today)
* [The Final Workflow](#the-final-workflow)

How I used LLMs to put together a packet for my tax preparer and review my
return. What worked and what didn't. I also created a public skill.

**This is not tax or investment advice**. This is not about "filing taxes with
AI." I have an awesome tax preparer because my taxes are complicated and
FBAR/FATCA penalties are steep. I need the human in the loop for my threat model
(the IRS).

Skills are at <https://github.com/parsiya/parsia-plugins>.

# Motivation and Problem Statement

My taxes are complicated. You think yours are, too, and I am sure they are, but
being a US citizen living abroad or holding foreign assets adds another
difficulty level. You have to worry about things like FBAR, FATCA, PFIC, FEIE,
and FTC.

In my opinion, the US government (regardless of party) and the general public
doesn't want US citizens to move abroad, work abroad, or marry abroad. Just ask
anyone with a foreign spouse.

[Worldwide taxation rant omitted because I am channeling my inner [patio11](https://x.com/patio11)].

> ngl, ur lowkey cooked
>
> **Anonymous teammate**

The best things you can do are 1. find a great CPA and immigration attorney
and 2. become very familiar with the tax treaty between the US and the country
where you live or hold assets and the US immigration system.

I am American-Canadian[1](#fn:1), among other things, and have financial accounts
in Canada. Fortunately, I have a great preparer and know the US-Canada tax
treaty (and our immigration system) to some extent. I am lucky because it's
probably one of the most comprehensive tax treaties (as far as these go).

# Methodology

LLMs excel at categorization, summarization, and data extraction. Every year I
gather information from many forms. This year I used AI to:

1. Convert all tax forms from PDF to Markdown.
2. Verify that the conversion was correct.
3. Organize the information into a packet for my tax preparer.
4. Check the previous year's filed return as a blueprint for things I might have forgotten.
5. Review the draft return from the preparer against the source documents.

This sounds straightforward. It was not.

## Steps 1 and 2: PDF Conversion and Audit

Tax returns and source forms are mostly PDFs. Fortunately, all my tax forms are
"True PDFs," not image-based PDFs.

1. True PDF: You can select the text.
2. Image-based PDF: Scans.

Source: <https://nlsblog.org/2020/06/12/three-types-of-pdfs/>

True PDFs convert well to text. I used [microsoft/MarkItDown](https://github.com/microsoft/markitdown) to convert
my tax forms to Markdown. Here's a section of my converted W-2.

```
| 5  Medicare wages and tips |     |      | 6  Medicare tax withheld        |      |
| -------------------------- | --- | ---- | ------------------------------- | ---- |
|                            |     | 1234 |                                 | 123  |
| 7  Social security tips    |     |      | 8  Allocated tips               |      |
| 9                          |     |      | 10 Dependent care benefits      |      |
| 11 Nonqualified plans      |     |      | 12a See instructions for box 12 |      |
|                            |     |      | C                               | 111  |
|                            |     |      |                                 |      |
|                            |     |      | 12b D                           | 1122 |
| 14 Other                   |     |      | 12c W                           | 3344 |
```

But our work is not finished. We need to confirm the conversion is actually
correct because:

1. Not all forms are true PDFs.
2. Even true PDFs can contain text rendered as images.
3. Tax forms have complicated layouts with many boxes.
4. The numbers are the most important thing in taxes and they have to be right.
5. Some PDFs have highlights, strikeouts, and annotations.

I ended up creating two skills[2](#fn:2) in my own plugin marketplace[3](#fn:3):

* [Render PDF pages to PNG](https://github.com/parsiya/parsia-plugins/blob/main/plugins/pdf-to-image/skills/pdf-to-image/SKILL.md) and check the original layout.
* [Convert the PDF with MarkItDown](https://github.com/parsiya/parsia-plugins/blob/main/plugins/pdf-to-markdown/skills/pdf-to-markdown/SKILL.md) and audit it for correctness.
  + Compare the Markdown with independent text from `pdftotext -layout`.

Converting PDFs to images might seem like overkill, but AI reads them well. This
was a cost-effective way to add another number check for a total of three:

1. PDF to markdown by deterministic tooling.
2. Image rendering by AI.
3. Manual checks by a human (me).

![The unfashionable 'Human in the loop'](01.webp "The unfashionable 'Human in the loop'")
The unfashionable 'Human in the loop'

### IRS Wage and Income Transcript

The IRS website lets you download past tax information (10 years, I think?). The
"Wage and Income Transcript" consolidates forms the IRS has for you.
Unfortunately, these generally become available towards the end of the following
year, after you've finished your taxes. If you apply for an extension like me,
you may be able to use them. This is how my W-2 looks on that form followed by
an ESPP form (you need those numbers when you sell the shares).

![Redacted W-2](02.webp "Redacted W-2")
Redacted W-2

I've redacted parts of the screenshot, but each number appears next to its box
name. This true PDF shows only the relevant fields and is much easier to convert
and read than the original. Still, double-check it against your own records to
see if the IRS has the correct info or not.

You can also download previous years' returns and transcripts as similar forms.

## Step 3: Creating the Packet for the Tax Preparer

The packet is not a tax return. It is a summary of the source documents and the
facts the preparer needs.

I organize it by the categories the preparer expects:

* Taxpayer information and filing status.
  + E.g., names, address, SSN.
* W-2 wages and withholding.
* Dividends.
* Interest.
* Capital gains and basis.
* Retirement distributions.
* HSA contributions and distributions.
* Estimated payments and withholding.
* Foreign income and foreign accounts.
* C...