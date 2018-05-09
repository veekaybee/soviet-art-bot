

# Soviet Art Bot v.20


[![Build Status](https://travis-ci.org/veekaybee/soviet-art-bot.svg?branch=master)](https://travis-ci.org/veekaybee/soviet-art-bot) 
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

Latest Updates: 
---

+ Fixing the html escape issue where apostrophes get rendered into hideous HTML representations by adding some [unescapes](https://github.com/veekaybee/soviet-art-bot/blob/35d13d788e1f8237b562176bb65de20ad5d3d598/lambda/lambda_function.py#L41-L42)
+ Adding some 12-factor principles by not storing my Twitter credentials in the app, but in SSM instead and pulling them in through [Travis-CI](https://github.com/veekaybee/soviet-art-bot/blob/master/build_env.sh)



![](https://raw.githubusercontent.com/veekaybee/soviet-art-bot/gh-pages/static/in_peaceful_fields.jpg)

A bot that finds socialist realism paintings and tweets them out.  For the official webpage, [check out here.](https://veekaybee.github.io/soviet-art-bot/) 

To see it in action, follow [@SovietArtBot](https://twitter.com/SovietArtBot)

## Why Soviet Art Bot

The TL;DR: Putting art on Twitter is fun and a great way to learn more about AWS. 

To read a really long post on Soviet Art Bot, [click here.](http://veekaybee.github.io/2018/02/19/creating-a-twitter-art-bot/) 

## Architecture 

![High-level](https://raw.githubusercontent.com/veekaybee/veekaybee.github.io/master/images/high-level-flow.png)

Low-Level
![architecture](https://raw.githubusercontent.com/veekaybee/veekaybee.github.io/master/images/architecture.png)

## Installation

In progress. 

## Contributing [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

It's really the alpha  Wild Wild West stages of this project so I don't have any specific guidelines. That said, if you see something, say something. Pull requests welcome. 
