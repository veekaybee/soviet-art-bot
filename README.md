![](https://raw.githubusercontent.com/veekaybee/soviet-art-bot/gh-pages/static/in_peaceful_fields.jpg)

*Andrei Mylnikov, "In Peaceful Fields" 1950*

<a class="github-button" href="https://github.com/veekaybee/soviet-art-bot" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star soviet-art-bot on GitHub">Star</a>

<a class="twitter-follow-button"
  href="https://twitter.com/SovietArtBot"
  data-size="large">
Follow @SovietArtBot Here</a>

## What's Soviet Art Bot? 

A bot that tweets out a socialist realist painting, along with their painters, every six hours. 

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">&quot;Discussion of a Bad Grade&quot;<br>Sergiy Grigoriev, 1950 <a href="https://t.co/cNQ8HT6Biw">pic.twitter.com/cNQ8HT6Biw</a></p>&mdash; SovietArtBot (@SovietArtBot) <a href="https://twitter.com/SovietArtBot/status/963618544775811073?ref_src=twsrc%5Etfw">February 14, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

The data comes from [WikiArt](https://www.wikiart.org/), a "non-profit project featuring some 150,000 artworks by 2,500 artists, localized in 5 languages.", from their [Socialist Realism](https://www.wikiart.org/en/paintings-by-style/socialist-realism?select=featured) category. 

## How does Soviet Art Work? 

For an extremely in-depth post, please read [here.](http://veekaybee.github.io/)

Tools: 

+ Python
  + Requests
  + Twython
  + Boto
+ AWS
  + S3
  + Lambda
  + Code Pipeline
+ GitHub
  + Git
  +Travis-CI integration 


The high-level overview: 

+ Paintings are downloaded through the WikiArt API
+ Local processing cleans up JSON metadata
+ Paintings and metadata are uploaded to an S3 bucket on AWS
+ A Lambda picks up the files from S3 and tweets out a timed cron job to Twitter through Twython
+ You see beautiful socialist realism art

# GitHub Repo

Find all the code here: 
[veekaybee/soviet-art-bot](https://github.com/veekaybee/soviet-art-bot)


## ToDo

1) Source more paintings. WikiArt is fantastic, but has only 500ish paintngs available in the socialist realism category. I'd like to find more sources with high-quality metadata and a significant collection of artworks. 
2) Fix the code so that no painting repeats more than once a week. That seems like the right amount of time for Twitter followers to not get annoyed. 
3) Create a front-end where anyone can upload a work of socialist realism for the bot to tweet out. 
4) Machine learning and deep learning potential possibilities: 
  + Mash with #devart to see if the bot can create fun headlines for paintings based on painting content 
  + Extract colors from artworks by genre and see how they differ between genres


## About Me

I'm Vicki and I do data science and engineering work using tools like Python, Spark, and R. I [write about that here.](http://veekaybee.github.io/). In my spare time, I [read books](http://blog.vickiboykis.com/2018/01/02/favorite-books/) and [wrangle toddlers.](http://blog.vickiboykis.com/2017/06/27/moana/) 

<a href="https://github.com/veekaybee/soviet-art-bot" class="github-corner"><svg width="80" height="80" viewBox="0 0 250 250" style="fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg></a><style>.github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}@keyframes octocat-wave{0%,100%{transform:rotate(0)}20%,60%{transform:rotate(-25deg)}40%,80%{transform:rotate(10deg)}}@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}</style><script async defer src="https://buttons.github.io/buttons.js"></script>
