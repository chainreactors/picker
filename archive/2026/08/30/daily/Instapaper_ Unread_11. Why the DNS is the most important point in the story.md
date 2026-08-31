---
title: 11. Why the DNS is the most important point in the story
url: https://www.inventati.org/campaign/press
source: Instapaper: Unread
date: 2026-08-30
fetch_date: 2026-08-31T07:53:53.293027
---

# 11. Why the DNS is the most important point in the story

[![autistici.org](/static/img/Rstar-32-transparent.png)](https://www.inventati.org)
[**Login**](https://accounts.inventati.org)

* [Help](/get_help)
* [Policy](/who/policy)
* [About](/about)
* [Contact](/contact)
* [Code](https://git.autistici.org/public)
* [Donate](/donate)

* + Italiano
  + English

Press Release â August 28, 2026

# 1. Quick summary

On August 26, 2026, the U.S. Department of the Treasury, through OFAC (Office of Foreign Assets Control â the authority responsible for managing and enforcing economic and financial sanctions) sanctioned Autistici/Inventati (A/I), an Italian collective that has been providing digital infrastructure â email, hosting, mailing lists, chat, videoconferencing, streaming, and services related to privacy and anonymity â to movements and activists since 2001. Washington designated it as a Specially Designated Global Terrorist (SDGT), alleging that it has provided financial, material or technological support to terrorism and to organizations already subjected to sanctions. A/I rejects the allegations and declares that its activities consist in providing tools for digital self-defence and infrastructure for the freedom of communication.

On August 28 the autistici.org web domain was found to be unreachable. The collective attributed the problem to the DNS level and to the .org domain registry, Public Interest Registry (PIR). This technical point is important: it does not necessarily mean that the server was shut down; a domain can be made unreachable by preventing the normal DNS publication or resolution. Technical findings indicated a `serverHold` status for the domain (see below, “10. The blocking of autistici.org: facts and attributions”). The exact cause and the formal chain of decision-making must be however distinguished from the collective’s inferences: there is no public statement from PIR explicitly saying that it acted on OFAC’s orders.

# 2. Who is Autistici/Inventati

Autistici/Inventati was born in Italy in March 2001 from the meeting of individuals and collectives active in the fields of technology, privacy, digital rights and political activism. The collective offers free infrastructure as an alternative to large commercial platforms. A/I presents itself as an anti-fascist, anti-racist, anti-sexist and anti-militarist organization, opposed to capitalism and to authoritarianism, and selects the projects it hosts based on their compatibility with these principles.

The infrastructure is managed through a formally recognised association. This means that A/I is not an informal group: its activities are run by an association complying with all existing legal regulations, with legal responsibilities, contractual relationships and the associated obligations and controls.

This does not mean that the association has never had to deal with the justice system. Over the years there have been proceedings and interventions by the authorities, also on an international scale. Among the episodes recalled by the collective are the 2004-2005 intervention on the servers hosted by Aruba, in the context of an investigation launched by the public prosecutor’s office in Bologna, as well as subsequent disputes concerning individual pieces of content or accounts. In another case, following a suit by Trenitalia concerning a satirical site, the court of Milan ruled in defense of satire.

# 3. What the United States has decided

On August 26, OFAC placed Autistici/Inventati on the Specially Designated Nationals and Blocked Persons List with the SDGT designation. The legal basis is Executive Order 13224, issued in 2001 and subsequently amended, which allows for action to be taken against those who, in the view of the US administration, provide material, financial or technological support to terrorist activities.

The SDGT designation should not be confused with the Foreign Terrorist Organization (FTO) category. It is primarily a sanctions designation: assets and property interests subject to the US jurisdiction are frozen, and US citizens are generally prohibited from conducting transactions with the designated entity, subject to OFAC authorization.

# 4. What Washington accuses A/I of

According to the US Treasury, A/I provides digital infrastructure, tools and services to “violent Antifa cells” and other left-wing extremists. The statement cites hosting, encrypted email, chat and videoconferencing, streaming, and the infrastructure associated with Noblogs. Washington also claims that the infrastructure was made available to organizations already subjected to sanctions, specifically naming the PKK.

The logic behind this accusation is therefore not simply “A/I carried out a terrorist attack”. The point is so-called *material support*: according to Washington, the technological infrastructure constitutes a means of supporting individuals or activities qualified as terrorist.

The point at issue is therefore less straightforward than the phrase “has carried out terrorist acts” suggests: the charge concerns the role of the infrastructure and of the services provided to users. In this perspective, the question becomes to what extent the provision of technological services â email, hosting, chat, streaming or other communication tools â can be considered material support to a subject qualified as terrorist.

OFAC further maintains that the sanctions do not target the mere protected political expression, but rather support for conduct falling within the definition of terrorism in Executive Order 13224.

# 5. The collective’s response

A/I firmly rejects the US qualification. The collective describes itself as composed of volunteers and digital activists, saying that it merely provides digital self-defence tools for activists, individuals, groups and associations.

# 6. OFAC in a nutshell

The SDN List is the list of designated entities. In A/I’s case the acronym SDGT stands for Specially Designated Global Terrorist: it is a US sanctions designation, distinct from the Foreign Terrorist Organization (FTO) category, but with concrete economic consequences. The OFAC entry file on A/I also includes the notation “Secondary sanctions risk”.

The strength of this system does not stem solely from the fact that the United States can block assets within the US. The influence of the financial system, the US dollar and US companies can produce indirect effects abroad as well: banks, platforms and providers may sever ties to avoid compliance risk. This phenomenon is often called *de-risking*.

# 7. Why the sanction may have effects outside the US

The US designation does not automatically amount to a ban on A/I in Italy or the European Union. The US, the EU and individual states have distinct legal systems and counter-terrorism lists. Inclusion on the OFAC list does however produce significant pressure on operators dealing with the designated entity.

OFAC has also issued General License 36, which authorises the wind-down of certain transactions involving A/I within September 25, 2026. In this context, the term “wind-down” refers to the possibility of closing or bringing pre-existing relationships and transactions with the sanctioned entity to an orderly conclusion within a timeframe set by OFAC. It is therefore not an authorisation to maintain relationships indefinitely, but rather a deadline. It is important to distinguish between the period granted for the wind-down, any applicable legal obligations, and the independent decisions of operators who choose to sever the relationship earlier.

# 8. August 28: what happened to the DNS

When a user types autistici.org in their browser, the computer needs to know which IP address it should connect to. The DNS (Domain Name System) performs this function: it translates a human-readable name, such as autistici.org, into the server’s numerical address.

Simplified diagram: user â DNS â IP address â server â website.

If the DNS stops returning the correct match, the server may rem...