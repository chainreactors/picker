---
title: Speedrunning the New York Subway
url: https://blog.trailofbits.com/2025/08/25/speedrunning-the-new-york-subway/
source: The Trail of Bits Blog
date: 2025-08-26
fetch_date: 2025-10-07T00:48:08.735343
---

# Speedrunning the New York Subway

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Speedrunning the New York Subway

Evan Sultanik

August 25, 2025

[empire-hacking](/categories/empire-hacking/)

It all began, as many great adventures do, at [Empire Hacking](https://www.empirehacking.nyc/). There, I encountered the inimitable [@ImmigrantJackson](https://www.youtube.com/%40immigrantjackson), a YouTuber with a penchant for public transit and a dream: to break the world record for visiting every subway stop in New York City in the least time possible. (And, of course, to film the journey, what for those delicious likes, comments, and subscriptions.)

The only problem was: Immigrant Jackson didn’t know the fastest route. Surrounded by a room full of Trail of Bits computer scientists, he figured he’d ask our advice. The rules were simple. He didn’t need to exit the subway car; simply passing through a stop, even on an express train, counted as a “visit.” Stops could be visited multiple times, although this would of course be suboptimal. And there was no need to visit Staten Island … because we’re civilized. We live in a society. So, where should he start, and what would be the best route?

The coterie of curious computer coders coalescing around the inquisitor quickly classified this question as a case of the Traveling Salesman Problem (TSP). TSP is a classical problem in computer science in which one must find the shortest route for a traveling salesman to visit each city on a map. TSP is known to be computationally intractable to solve optimally for networks even as small as the New York subway system. Therefore, everyone dismissed the problem as “impossible.”

Except for me.

You see, [my now-ancient PhD dissertation](https://youtu.be/Q3NnEuCLADE) was on *combinatorial optimization* and *approximation algorithms*: tools for solving problems like TSP efficiently with a result that is not necessarily optimal, but at least close to optimal. I knew that there were algorithms capable of solving TSP very quickly, producing a route guaranteed to be at most 50% longer than the optimal solution. In fact, [one of the results of my dissertation](https://arxiv.org/abs/1402.0423) was the surprising revelation that even if you choose a feasible route at random, it will, on average, be only thrice the length of the optimal solution.

This, dear reader, was how I was [nerd-sniped](https://xkcd.com/356/) into optimizing (speedrunning?) the NYC subway.

The first challenge was that, even when you discard Staten Italy, the subway system still has *a lot* of stations. There are close to 500. This exercise was fun and all, but I wasn’t about to spend hours encoding hundreds of stations, lines, transfer points, headways, and average trip times into a program.

There is an open standard for specifying public transit data: the [General Transit Feed Specification (GTFS)](https://gtfs.org/). Fortunately, the [MTA has a public API implementing GTFS](https://www.mta.info/developers). It’s just a collection of CSV files that are quite straightforward to parse. The dataset is sufficient to construct a graph with a node for each subway station and an edge if there is a subway line that connects the two stations. Actually, the data represents subway *platforms* rather than stations, which is necessary to calculate things like transfer times between train lines.

The New York Subway network is a *directed* graph: some neighboring stations are accessible to each other only in one direction. For example, the [Aqueduct Racetrack station](https://en.wikipedia.org/wiki/Aqueduct_Racetrack_station) only has a platform for northbound trains, not southbound trains. [The best algorithms for approximating a solution to TSP on directed graphs](https://www.cs.cmu.edu/~odonnell/hits09/asadpour-goemans-madry-oveis-gharan-saberi-ATSP.pdf) are not great, only guaranteeing a solution of three or four times the length of the optimal solution. Therefore, I decided to relax the problem to an undirected graph (i.e., I assume that every station has trains to its neighbors bidirectionally). This turned out not to be an issue and permitted the use of the [Christofides algorithm](https://en.wikipedia.org/wiki/Christofides_algorithm), which guarantees a solution at most 50% longer than optimal.

The next and final relaxation is to partially ignore actual timetables and headways. When a transfer between lines is necessary, I assume that the transfer will require the “minimum transfer time” reported by GTFS (i.e.*,* the amount of time required to walk from one platform to another) plus one-half the average headway for that line throughout the day. Therefore, the resulting route has the potential to strand the poor YouTuber on the last train at the end of a line. Validating the resulting route’s real-world feasibility is left as an exercise to the reader.

The Christofides algorithm was able to approximate a solution to the TSP for my relaxed subway network graph in a matter of milliseconds. This is compared to the unfathomable amount of computation required to brute-force calculate the optimal solution, an amount so large that it afforded me the horrifying opportunity to learn that [there is a whole community of “googologists” who compete with each other to name large numbers](https://googology.fandom.com/wiki/Googolchime). We’re talking *googolchime* levels of computation. *Guppybell* levels, even!

The resulting tour visits all 474 stations, 155 of which are visited more than once. The tour requires 34 transfers. The expected time for completing this tour is 20 hours, 42 minutes. That’s about [45 minutes faster than the record](https://www.youtube.com/watch?v=6xoWvBAUVIg), which was about 21 and a half hours.

[
](/img/speedrunning-ny-subway.mp4)

Figure 1. The resulting subway tour route

This is neat and all, but we spent an unnecessary amount of energy encoding the New York subway system as a graph. What else might we do with it? One straightforward computation is to calculate each station’s [*eigenvector centrality*](https://en.wikipedia.org/wiki/Eigenvector_centrality). Imagine you’re given the Sisyphean task of riding the subway for all eternity. Every time you arrive at a station, you flip a coin. If it’s heads, you stay on the current train. If it’s tails, you get off and transfer to another line or direction. If you were to pause your infinite tour at any arbitrary point in time, what’s the probability that you are at a particular station? The higher the probability, the more “centrally connected” the station. That’s exactly what eigenvector centrality calculates.

Eigenvector centrality is actually what Google originally used in its [PageRank algorithm](https://en.wikipedia.org/wiki/PageRank) to rank the relative importance (centrality) of web pages. Each page is like a subway station, and hyperlinks on the page are like the subway lines connecting them. Eigenvector centrality is relatively easy to calculate, either directly (it’s related to the eigenspectrum of the graph’s adjacency matrix, thanks to spooky [spectral graph theory](https://en.wikipedia.org/wiki/Spectral_graph_theory) magic) or using a technique called [*power iteration*](https://en.wikipedia.org/wiki/Power_iteration) (which relies on a convergence that happens when you multiply the adjacency matrix by a vector a bunch of times). Either way, you can calculate it with a single function call in [NetworkX](https://networkx.org/).

What do you think will be the most probable stop on your infinite subway tour? Or, another way to ask the same question: Which stop will you visit most often on your tour? Unsurprisingly, it will be Times Square, with a probability of a little over 30%. The next most probable station is 42nd St. Port Authority Bus Terminal, coming in at about 8%. Then 50th St., 59th St. Columbus Circle, Grand Central 42nd St., and 34th St. Penn Station are all between 4% and...