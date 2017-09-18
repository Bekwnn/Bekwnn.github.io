---
layout: post
title: Server and Client Game Rules
categories: blog
tags: [gamedev, networking, code-design]
---
This article is mostly a page taken from UE4's book, but generalized for any sort of
engine or framework. This is going to be about UE4's pattern of GameMode and GameState.
GameMode is a set of rule and game information held exclusively by the server, while
GameState is the set of rule and game information that gets replicated to all connected
clients. The main, clear advantage here is to prevent clients from cheating or having
access to information they shouldn't have access to.

With that explanation you may already be getting a vague idea of how this 2-class system
works and why it's useful, so from here on out I'm going to go more in depth.

## An Example in Action

## The Relationship of the Two Classes

## What Sort of Information is Sensitive?

## Tough Cases
