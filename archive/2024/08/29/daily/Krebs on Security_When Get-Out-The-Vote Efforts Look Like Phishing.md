---
title: When Get-Out-The-Vote Efforts Look Like Phishing
url: https://krebsonsecurity.com/2024/08/when-get-out-the-vote-efforts-look-like-phishing/
source: Krebs on Security
date: 2024-08-29
fetch_date: 2025-10-06T18:12:51.584283
---

# When Get-Out-The-Vote Efforts Look Like Phishing

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# When Get-Out-The-Vote Efforts Look Like Phishing

August 28, 2024

[42 Comments](https://krebsonsecurity.com/2024/08/when-get-out-the-vote-efforts-look-like-phishing/#comments)

Multiple media reports this week warned Americans to be on guard against a new phishing scam that arrives in a text message informing recipients they are not yet registered to vote. A bit of digging reveals the missives were sent by a California political consulting firm as part of a well-meaning but potentially counterproductive get-out-the-vote effort that had all the hallmarks of a phishing campaign.

![](https://krebsonsecurity.com/wp-content/uploads/2024/08/wdiv-sms.png)

On Aug. 27, the local Channel 4 affiliate **WDIV** in Detroit [warned](https://www.youtube.com/watch?v=kXkKZ4T25h0) about a new SMS message wave that they said could prevent registered voters from casting their ballot. The story didn’t explain how or why the scam could block eligible voters from casting ballots, but it did show one of the related text messages, which linked to the site **all-vote.com**.

“We have you in our records as not registered to vote,” the unbidden SMS advised. “Check your registration status & register in 2 minutes.”

Similar warnings came from [an ABC station in Arizona](https://www.abc15.com/news/political/elections/spam-or-real-unsolicited-text-messages-say-you-arent-registered-to-vote), and from [an NBC affiliate in Pennsylvania](https://www.wgal.com/article/south-central-pennsylvania-voters-question-text-message-about-registration-status/61960563), where election officials [just issued an alert](https://co.lancaster.pa.us/CivicAlerts.aspx?AID=2204) to be on the lookout for scam messages coming from all-vote.com. Some people interviewed who received the messages said they figured it was a scam because they knew for a fact they *were* registered to vote in their state. WDIV even interviewed a seventh-grader from Canada who said he also got the SMS saying he wasn’t registered to vote.

Someone trying to determine whether all-vote.com was legitimate might visit the main URL first (as opposed to just clicking the link in the SMS) to find out more about the organization. But visiting all-vote.com directly presents one with a login page to an online service called bl.ink. [DomainTools.com](https://www.domaintools.com) finds all-vote.com was registered on July 10, 2024. Red flag #1.

![](https://krebsonsecurity.com/wp-content/uploads/2024/08/winvotecheckstatus.png)

Another version of this SMS campaign told recipients to check their voter status at a site called **votewin.org**, which DomainTools says was registered July 9, 2024. There is little information about who runs votewin.org on its website, and the contact page leads to generic contact form. Red Flag #2.

What’s more, Votewin.org asks visitors to supply their name, address, email address, date of birth, mobile phone number, while pre-checking options to sign the visitor up for more notifications. Big Red Flag #3.

Votewin.org’s Terms of Service referenced a California-based voter engagement platform called **VoteAmerica LLC.** The same voter registration query form advertised in the SMS messages is available if one clicks the “check your registration status” link on voteamerica.org.

VoteAmerica founder **Debra Cleaver** told KrebsOnSecurity the entity responsible for the SMS campaigns telling people they weren’t registered is **Movement Labs**, a political consulting firm in San Francisco.

Cleaver said her office had received several inquiries about the messages, which violate a key tenet of election outreach: Never tell the recipient what their voter status may be.

“That’s one of the worst practices,” Cleaver said. “You never tell someone what the voter file says because voter files are not reliable, and are often out of date.”

Reached via email, Movement Labs founder **Yoni Landau** said the SMS campaigns targeted “underrepresented groups in the electorate, young people, folks who are moving, low income households and the like, who are unregistered in our databases, with the intent to help them register to vote.”

Landau said filling out the form on Votewin.org merely checks to see if the visitor is registered to vote in their state, and then attempts to help them register if not.

“We understand that many people are jarred by the messages – we tested hundreds of variations of messages and found that these had the largest impact on someone’s likelihood to register,” he said. “I’m deeply sorry for anyone that may have gotten the message in error, who is registered to vote, and we’re looking into our content now to see if there are any variations that might be less certain but still as effective in generating new legal registrations.”

Cleaver said Movement Labs’ SMS campaign may have been incompetent, but it wasn’t malicious.

“When you work in voter mobilization, it’s not enough to want to do good, you actually need to be good,” she said. “At the end of the day the end result of incompetence and maliciousness is the same: increased chaos, reduced voter turnout, and long-term harm to our democracy.”

To register to vote or to update your voter registration, visit [vote.gov](https://www.vote.gov) and select your state or region.

*This entry was posted on Wednesday 28th of August 2024 07:55 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Breadcrumbs](https://krebsonsecurity.com/category/breadcrumbs/)

[all-vote.com](https://krebsonsecurity.com/tag/all-vote-com/) [Debra Cleaver](https://krebsonsecurity.com/tag/debra-cleaver/) [DomainTools.com](https://krebsonsecurity.com/tag/domaintools-com/) [Movement Labs](https://krebsonsecurity.com/tag/movement-labs/) [Vote America](https://krebsonsecurity.com/tag/vote-america/) [votewin.org](https://krebsonsecurity.com/tag/votewin-org/) [WDIV](https://krebsonsecurity.com/tag/wdiv/) [Yoni Landau](https://krebsonsecurity.com/tag/yoni-landau/)

Post navigation

[← New 0-Day Attacks Linked to China’s ‘Volt Typhoon’](https://krebsonsecurity.com/2024/08/new-0-day-attacks-linked-to-chinas-volt-typhoon/)
[Owners of 1-Time Passcode Theft Service Plead Guilty →](https://krebsonsecurity.com/2024/09/owners-of-1-time-passcode-theft-service-plead-guilty/)

## 42 thoughts on “When Get-Out-The-Vote Efforts Look Like Phishing”

1. Rex Fermier [August 28, 2024](https://krebsonsecurity.com/2024/08/when-get-out-the-vote-efforts-look-like-phishing/#comment-614487)

   Too bad you didn’t press them to name who their client was.

   1. Benny Cemoli [August 29, 2024](https://krebsonsecurity.com/2024/08/when-get-out-the-vote-efforts-look-like-phishing/#comment-614525)

      Kamala Harris and Big Daddy Walz. Seems like something they’d do.

      1. R.Cake [August 30, 2024](https://krebsonsecurity.com/2024/08/when-get-out-the-vote-efforts-look-like-phishing/#comment-614584)

         Well and – just a stupid question from across the pond – why would you even care?

         1. Ben [August 31, 2024](https://krebsonsecurity.com/2024/08/when-get-out-the-vote-efforts-look-like-phishing/#comment-614623)

            We do care I believe limiting corporate donations like the limit on personal ones at the ...