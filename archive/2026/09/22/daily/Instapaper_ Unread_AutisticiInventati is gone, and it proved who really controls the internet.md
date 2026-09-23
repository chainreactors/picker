---
title: AutisticiInventati is gone, and it proved who really controls the internet
url: https://andreafortuna.org/2026/09/17/autistici-inventati-digital-sovereignty/
source: Instapaper: Unread
date: 2026-09-22
fetch_date: 2026-09-23T06:54:54.549345
---

# AutisticiInventati is gone, and it proved who really controls the internet

[Andrea Fortuna](/)
[ ]

[About](/about/)[Search](/search/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# Autistici/Inventati is gone, and it proved who really controls the internet

Sep 17, 2026

by [Andrea Fortuna](/about/)

Three weeks ago on this blog I wrote about [Autistici/Inventati](https://andreafortuna.org/2026/08/31/autistici-inventati-privacy-digital-freedom/), the Italian hacktivist collective that spent twenty five years running privacy first email, hosting and mailing lists for activists who wanted infrastructure that would not sell them out. I closed that piece with an open question about where the line sits between offering secure tools and being blamed for what people do with them. I did not expect an answer this fast, and I certainly did not expect it to arrive not from a courtroom but from a domain registry status flag and a compliance officer’s spreadsheet. This story is too important to let go after a single post, so I am back on it, because what happened to A/I in the weeks since is less a tale about one small Italian collective and more a live demonstration of how little sovereignty Europe actually has over the piece of the internet it thinks it owns.

## In brief

* On 26 August 2026 the US designated Autistici/Inventati a Specially Designated Global Terrorist, and by 6 September the collective had announced its shutdown.
* The kill chain never touched an Italian courtroom: a serverHold flag on autistici.org placed by the US based Public Interest Registry, a closed PayPal gateway and a frozen Banca Etica account did the work.
* An OFAC listing carries no freezing obligation under Italian law, as the UIF states explicitly, yet Banca Etica suspended the account anyway on a secondary sanctions risk calculation.
* Autistici/Inventati filed an urgent injunction against Banca Etica at the Tribunale di Pisa on 8 September, asking for the account to be restored or the balance released.
* The same chokepoints, from .org domains to Visa and Mastercard rails to US headquartered clouds under the CLOUD Act, sit under every layer of Europe’s digital stack.
* France’s Linux migration and the EU Cloud Sovereignty Framework show the direction of travel, but the scale gap with US hyperscalers remains enormous.

## Twelve days from a press release to a blackout

On 26 August 2026 the US Departments of State and the Treasury designated Autistici/Inventati a Specially Designated Global Terrorist under Executive Order 13224, giving the collective a wind down deadline of 25 September and warning that anyone who kept engaging with it risked exposure to secondary sanctions. What followed was a cascade of infrastructure failures that happened almost entirely outside Italy’s jurisdiction, without a single legal step along the way. Within days, one of A/I’s core domains became unreachable at the DNS level, its **PayPal** donation gateway was shut down, and its Italian bank account was frozen. On 6 September the collective announced it would shut down for good, explicitly to protect its roughly twenty thousand mailbox holders, twenty thousand blogs and thousands of mailing lists from further exposure, a sequence of events reconstructed in detail by [TechRadar’s investigation into the case](https://www.techradar.com/vpn/vpn-privacy-security/infrastructure-as-a-weapon-why-the-us-action-against-italys-autistici-inventati-puts-global-digital-rights-on-notice).

The domain failure is the detail worth sitting with. A/I’s own account, relayed by the same investigation, points to the **Public Interest Registry**, the US based nonprofit that operates the entire `.org` namespace, as having placed *autistici.org* into a serverHold status as a direct consequence of the sanctions, severing the mapping between the name and the servers behind it without touching a single physical machine. Nobody had to raid a data center in San Giuliano Terme. Nobody had to prove anything in front of an Italian judge. A single administrative decision, taken by an organization headquartered in Virginia and governed by US law, was enough to make a piece of Italian civil society vanish from the browsers of people who typed its name.

The reactions from digital rights organizations were sharp. [EDRi](https://www.techradar.com/vpn/vpn-privacy-security/infrastructure-as-a-weapon-why-the-us-action-against-italys-autistici-inventati-puts-global-digital-rights-on-notice), together with more than thirty other groups, described the designation as an attack on independent internet infrastructure and on the democratic integrity of the EU. The Electronic Frontier Foundation’s Jillian York told Italian broadcaster Rai News that the move effectively targets the messenger rather than anyone who committed an act of violence, since what the US government is really punishing is the freedom to host anonymously, not a specific crime. Harry Halpin, who runs the privacy focused **Nym Technologies**, drew the obvious lesson for anyone still building centralized privacy infrastructure: a government can take down centralized domains and bank accounts in a matter of days, so resilience now has to be designed in from the start rather than assumed. It is a hard thing to hear if you have spent a career, as I have, thinking about DFIR and OSINT in terms of servers, logs and jurisdictions that map neatly onto physical geography. A/I’s shutdown shows that the actual chokepoints are administrative, contractual and largely invisible until the day someone decides to pull the lever.

## A blacklist that, legally, freezes nothing

The most instructive part of this story, and the one least reported outside Italy, is what happened at **Banca Etica**, the ethical bank where A/I had held its current account since 2018. On 1 September, six days after the OFAC designation, Banca Etica suspended all operations on the account, citing the risk of secondary sanctions that could theoretically cascade onto its own 130,000 customers through their Visa and Mastercard linked cards, as reported by [il manifesto](https://ilmanifesto.it/autistici-inventati-ci-opponiamo-alle-sanzioni) and [Valori.it](https://valori.it/autistici-inventati-ofac-banca-etica/). The bank then moved toward closing the relationship outright and, according to A/I’s lawyer Fausto Gianelli, effectively froze the funds in a way that prevented the collective from even transferring its own donation money elsewhere, a move that pushed A/I to file an urgent injunction against Banca Etica at the Tribunale di Pisa on 8 September, asking either for the account to be reinstated or for the balance to be released to an account of its choosing, as detailed by [Altreconomia](https://altreconomia.it/perche-autistici-inventati-ha-fatto-causa-a-banca-etica-dopo-la-chiusura-del-conto/) and [Byte.it](https://www.byte.it/autistici-inventati-porta-banca-etica-in-tribunale-per-riavere-i-fondi-bloccati-dopo-le-sanzioni-usa/).

Here is the part that gets lost in most of the coverage: an entry on the OFAC Specially Designated Nationals list does not, by itself, create a legal obligation for an Italian bank to freeze anything. Italy’s anti terrorism financing framework runs through EU regulations and the consolidated European sanctions list managed at the EU level, and Italy’s own Financial Intelligence Unit, the **UIF** at Banca d’Italia, states plainly on its website that while it circulates the OFAC list to support banks’ own monitoring, inclusion on that list does not carry a freezing obligation under Italian law, a distinction confirmed independently by [legal analysis published on dirittobancario.it](https://www.dirittobancario.it/art/il-difficile-connubio-tra-banche-ofac-e-clienti-iscritti-nella-sdn-lst/). What actually froze A/I’s account was not a legal duty but a risk calculation: US law allows secondary sanctions against foreign financial institutions that keep serving a designated entity, and no Italian ...