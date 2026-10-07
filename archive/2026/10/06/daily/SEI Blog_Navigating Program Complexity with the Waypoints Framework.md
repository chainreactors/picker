---
title: Navigating Program Complexity with the Waypoints Framework
url: https://www.sei.cmu.edu/blog/navigating-program-complexity-with-the-waypoints-framework/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-10-06
fetch_date: 2026-10-07T07:55:45.231523
---

# Navigating Program Complexity with the Waypoints Framework

[Skip to main content](#main-content)

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Research and Development

Publications and Media

Education

Careers

Search

Mobile Menu

[# SEI Blog](/blog/)

1. [Home](/)
2. [Publications and Media](/publications-media/)
3. [Blog](/blog/)
4. Navigating Program Complexity with the Waypoints Framework

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Dooley, K., 2026: Navigating Program Complexity with the Waypoints Framework. Software Engineering Institute blog, Accessed October 6, 2026, https://doi.org/10.58012/g7cv-0y35.

Copy

APA Citation

Dooley, K. (2026, October 6). Navigating Program Complexity with the Waypoints Framework. Retrieved October 6, 2026, from https://doi.org/10.58012/g7cv-0y35.

Copy

Chicago Citation

Dooley, Kevin. "Navigating Program Complexity with the Waypoints Framework." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, October 6, 2026. https://doi.org/10.58012/g7cv-0y35.

Copy

IEEE Citation

K. Dooley, "Navigating Program Complexity with the Waypoints Framework," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 6-Oct-2026 [Online]. Available: https://doi.org/10.58012/g7cv-0y35. [Accessed: 6-Oct-2026].

Copy

BibTeX Code

```
@misc{dooley_2026,
author={Dooley, Kevin},
title={Navigating Program Complexity with the Waypoints Framework},
month={Oct},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/g7cv-0y35},
url={https://doi.org/10.58012/g7cv-0y35},
note={Accessed: 2026-Oct-6}
}
```

Copy

# Navigating Program Complexity with the Waypoints Framework

![](/media/images/Kevin_Dooley_1959.max-180x180.format-webp.webp)

###### [Kevin Dooley](/authors/kevin-dooley)

###### October 6, 2026

##### PUBLISHED IN

[Acquisition Transformation](/blog/topics/acquisition-transformation/)

##### CITE

<https://doi.org/10.58012/g7cv-0y35>

Get Citation

##### SHARE

Large military programs face a coordination problem when taking on broad and interdependent program objectives. While small programs with decoupled teams can often rely on a more ad-hoc approach to planning and roadmaps, large programs with complex dependencies often must develop master schedules that can encompass as many as 50,000 elements. In such an environment, teams need to be able to coordinate efforts and meet cross-cutting objectives. In the absence of better tools, when tasked with a major program objective, teams turn to PowerPoint to outline quarterly activities. While such an approach affords some visibility into program activities, the end result is a slide deck that may only be current for four days per year, since there is no direct mechanism for updating the document between quarterly updates. In addition to creating overload, this approach is inadequate to answer three critical questions:

* Is there anything you planned to complete last quarter but didn’t? If so, what is the impact?
* How confident are you about completing commitments this quarter?
* Is there anyone you are dependent on, and are they aware?

In aviation, **waypoints** guide pilots through complex flight plans, providing structure while maintaining flexibility. Inspired by this aviation principle, I worked with Lieutenant Colonel Adam Satterfield of the United States Air Force to create a lightweight digital framework that will help major programs plan, track, and execute major objectives. This post explains how the Waypoints Framework can provide program managers with a lightweight digital approach to visualizing major activities, synchronizing dependencies across teams, and managing risks.

## The Origin of Waypoints

As a Program Management Officer in the United States Air Force, Lieutenant Colonel Satterfield oversees major defense programs. Lt. Col. Satterfield, a co-creator of Waypoints, had a sheet of paper hanging up in his cubicle that outlines the ideas that became the origin of Waypoints. Lt. Col. Satterfield had previously met with the Colonel in charge of his major program, who listed three requirements for Waypoints:

* It needs to be simple.
* It needs to be led by the team leaders.
* It needs to visualize the work.

To achieve these requirements, Lt. Col. Satterfield understood that a minimum viable framework was needed to bridge the gap between informal planning and comprehensive project management. The framework needed to be able to address coordination needs without overwhelming the organization.

Lt. Col. Satterfield began collaborating with us, and our initial step was to consolidate our planning efforts in Excel. While this shift improved dependency visibility and created a single source of data, quarterly accuracy problems persisted.

The breakthrough came when we migrated to Jira and Confluence. Jira allowed us to track individual waypoints as issues, while Confluence provided knowledge management and dynamic dashboards. It allowed teams to filter waypoints into quarterly buckets, sort by due date, and trace paths toward goals, reducing cognitive overload while enabling continuous updates.

More importantly, this digital approach fundamentally changed the organization’s planning mindset. Instead of waiting for quarterly reviews to discover that a milestone had been missed, program managers now had insight into issues and progress in near real time. Teams could adjust course immediately once an issue arose rather than discovering problems months after they emerged.

Far too often, program managers mistakenly ask, *Are we where we want to be?* Instead, they should be asking, *Are we on the right trajectory?*

The mindset associated with the first question involved missing a mark before correcting course. The latter allows for corrections *en route*, similar to a pilot adjusting the heading of an airplane between waypoints rather than discovering that they missed their destination because the winds pushed them off course.

## Building the Waypoints Framework

The Waypoints Framework uses a lightweight digital approach to visualize major activities, synchronize dependencies, and manage risks. Jira and Confluence are the two major digital tools that enable the framework. The Waypoints journey often begins with a **goal** that a program wants to achieve in two or three years that is often made public because of its significance to the entire organization, such as the first flight of the B-21 stealth bomber in November 2023. Achieving that major **goal** requires the effort of multiple teams.

Each team in the program enterprise establishes its own waypoints leading toward this major programmatic goal, which creates a visible path that everyone in an organization can follow. Each waypoint represents a promise, a planned activity that unlocks another programmatic activity toward a goal.

The Waypoints Framework rests on three principles:

* **Right-sizing:** To help distill complexity to a comprehensible level, the organization’s team leaders will identify two-to-eight activities per quarter per team with those teams maintaining detailed planning using whatever tools work best. When too many activities are planned, the effort to maintain accurate plans increases. Keeping the quarterly planned accomplishments to single digits helped ensure the plan’s accuracy. For each activity, each team will identify their definition of done and outline major contributions towards the major programmatic goal set forth. This step alone can often be an early indicator of mismatches and incorrect handoffs.

[![Figure 1: The first principle, right-sizing, limits the number of activities per quarter to improve plan accuracy.](/media/images/figure1_waypoints_10052026.max-1280x720.format-webp.webp)](/media/images/figure1_waypoints_10052026.original.jpg)

Figure 1: The first principle, rig...