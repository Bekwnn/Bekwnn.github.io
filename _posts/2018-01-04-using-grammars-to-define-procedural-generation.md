---
layout: post
title: Using Grammars to Define Procedural Generation
date: 2018-01-04 15:00:00 -0700
categories: blog
tags: [graphics, gamedev, procedural]
---
I've always been fascinated by games which ship with detailed map editors. Specifically, the way they attempt to expose game logic
in such a way that inexperienced players can create their own. Recently I've been working on an experimental method for authoring
landscapes which in a similar way uses a grammar to expose the rules of procedural generation to be manipulated by an inexperienced
user.

Grammars are intuitive to most people, since every spoken language has some form of grammar. It's such a basic idea:
there's an alphabet (symbols/words) and a set of rules. At some point I can't quite pin down, I had the thought of creating
some interface where a user defines their own grammar to describe rules for procedural generation.

A while later, and here's a glimpse of what I came up with:

<p align="center">
<img src="{{site.url}}/assets/LTerrainResults.png">
</p>
<p align="center">
<img src="{{site.url}}/assets/LTerrainUI.png">
</p>
<p align="center">
<img src="{{site.url}}/assets/LTerrainRule.png">
</p>
<p align="center">
<img src="{{site.url}}/assets/LTerrainFoliage.png">
</p>

The gist of what you're looking at is a tile-based 2D editor. You provide parameters for how textures/foliage/heighmap rougness 
translates from the different symbols into the final 3D terrain. The 2D tile map you paint gets fed as input into a terrain generation system
to create the 3D results as shown above.

But what I've just described is barely a grammar; you're just defining parameters for a procedural generation system.
The 3rd picture is the definition of a rule. It basically says "match the beach symbol and replace it with this map". That's where the grammar
part comes in.

<p align="center">
<img src="{{site.url}}/assets/LTerrainLoD.png">
</p>

The grammar I chose in this case is a modified [L-System grammar.](https://en.wikipedia.org/wiki/L-system) Though it's not pictured above, I'm hoping to implement more ways of defining rules
such as defining a randomized version of the match and replacement, or choosing randomly from a set of maps.

A terrain such as the one above can be created using this system in a few minutes. It accomplishes the goal of creating a roughly 80% completed terrain
faster (generally speaking) than traditional landscape scuplting and foliage/texture painting tools. The result generated by the above system is fully compatible
with those engine tools so the last 20% of polish and fine-tuning can be done using those traditional tools.

But my goal here isn't to talk too much about the specifics of this system I made. This terrain editor itself was originally started just as
a proof-of-concept for the idea that grammars can be used to expose procedural generation to non-developers.

When you boil down procedural generation in almost all cases, you're trying to generate *some* resulting output which has unpredictably generated features.
To make a result that's not just *visual gibberish*, you embed rules in your system about how different elements of the result should be composed.

The goal of this project was to create an example where a grammar is mapped to a procedural system:

* the primitive elements which combine to create the final result are the **alphabet** of the grammar.
* the rules of the system need to be parameterized and mapped to some user interface which allows a user to define the **rules** of the grammar.

Similar to my ["3D Modeling Seems Problematic"]({{site.url}}/blog/2017/10/17/3d-modeling-seems-problematic.html) post, this is more of an "idea" post, except unlike that post
which is pretty open-ended and in which I didn't really put forth any effort into exploring the idea, here I hope to demonstrate an example as a proof-of-concept.

I've applied the idea to generating terrains and it was lucky that turned out to be a good fit. The idea could just as easily be applied to creating procedural interiors such as dungeons or
the inside of buildings. It could be applied to the creation of alien life forms, similar to the procedural creatures generated by No Man's Sky. I've written a paper about the "L Terrain System"
I created above, but it mainly focuses on the system itself, the implementation details, and how it stands to improve the creation of terrains. This post is a more general look at procedural
generation using grammars.

<p align="center">
<img src="{{site.url}}/assets/no-mans-sky-procedural-creatures.jpg">
</p>

L-Systems themselves are "procedural generation" (though not in the way people tend to think of procedural generation) and L-Systems have long been used to generate and model plant life.
To some extent, L-Systems themselves are already an application of this idea, as they use a grammar to model a procedurally generated graphic. I think there's unexplored territory in
"grammar-based procedural modelling" which goes beyond L-Systems or the terrain generation system I've presented here. Even without any desire to create
a user-interface, grammars can be used to create better defined procedural systems, whether it's galaxies, cities, living beings, or even gameplay/interaction related content.
