---
title: History of Labirong
date: 2022-05-03 17:06:00
tags:
    - game
categories:
    - game
    - development
keywords:
    - game
    - art
    - multiplayer
    - labirong
---

For those curious why I have so many labyrinth stuff (mainly named labirong) on my GitHub, I'm going to share the history of labirong and some pictures of its progress throughout the years.

It all started back in 2017, my friend was on his last years of computer science course and received a home task to create a script that would read a .txt file containing 0s and 1s and display a block on the screen where it was 1 and a blank space where it was 0. So I joined him just for fun and we made it.

So if we created a .txt like this:

```
1111111111111111
0011111111111111
1011111000000111
1011111011110111
1011111011110111
1011100011110011
1000001111111011
1011111101101011
1011111000001011
1011111101101011
1000000011101011
1011111000001011
1001111111111001
1100000001000110
1111111100010000
1111111111111111
```

It would look like this:

![maze](/images/history-of-labirong/maze-version-0.png)

As an extra challenge for the task, it also asked to create a square that would walk in the loaded map, so we added that as well:

![maze](/images/history-of-labirong/maze-version-1.png)

It was pretty simple, but it was awesome. But since we created the maps ourselves, it was always very easy to beat the labyrinth. So we thought about generating the labyrinth randomly based on the size we wanted. We did some research and started implementing it:

![maze](/images/history-of-labirong/maze-version-2.png)

Now as you can see it was much harder to solve.

It was feeling a bit game-ish and we started to think what if it became an actual game. So I asked my brother to draw some sprites and I looked for others free online. With the sprites it looked like an actual game.

I did some changes on the camera distance and made it follow the player instead of showing the whole map (it was very hard to see on really large maps):

![maze](/images/history-of-labirong/maze-version-3.png)

Right now it was looking very nice and it was pretty fun trying to finish the labyrinth. But I always enjoyed multiplayer games more, so it was the last thing missing. Multiplayer was added and if someone found the exit the map would be regenerated automatically:

![maze](/images/history-of-labirong/maze-version-4.png)

We named it labirong because it was a fun word that sounded like labyrinth. And this is how labirong was born.

Throughout the years whenever I wanted to try a new language or framework and didn't have any ideas of what to do, I tried to recreate labirong in it, just for fun. So I end up creating a labirong in Go, Rust, BabylonJS, Phaser...

Here's some other versions:

LabironGO (terminal)

![labironGO](/images/history-of-labirong/labirongo.png)

Labirong 3D (BabylonJS)

![labirong3D](/images/history-of-labirong/labirong3d.png)
