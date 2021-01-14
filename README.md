# academy.tutorials.scrapy
Academy, tutorial, scrapping, linkedin

Tutorial is about showing You, how to make use of now days open source 
technologies and free services to automate data gathering processes.

In tutorial we will explain the process of data extraction although the
tutorial itself is not enough to give You all the information to create 
this solution on Your own. 

Example provided in this tutorial is fully functional. 

## goals

1. Automate extraction of publicly available information from LinkedIn.

## technology 
Python
scrapy
proxycrawl
chromedriver
Selenium
docker
docker-compose
cron
Ubuntu

## resources
google.com
linkedin.com
github.com

## blueprint
As LinkedIn profiles are publicly available we can access them 
by using google search website: https://google.com/search?q=.
But that maybe not enough by itself. Google.com has many policies
that it apply depending on Your location, previous searches and
many mechanisms that we are not aware of.

Github.com is a website for anyone who work in IT, from there
we can get information about how much somebody is coding, if the
person is coding in open source projects, are those projects
well know to open source community and so on. Github.com has as
well more detail information about technologies which are
not the most important when searching for ideal candidates but
it is something who one must know and that's it.

Github.com is important if You need a person who is professional,
but if soft skills are equally important maybe other resources
will be of equal importance too.

Linkedin contains information about employment, recommendations,
certifications.

At the beginning I thought about using google.com/search as
start point but this will be a different topic, more things needs
to be considered when using google.com/search.

So first we scrape github.com that is publicly available. Than
we use information from github.com to find person on linkedin.com. 
At the end we will try to find extra information by using google
.com/search.

  

### advance use of google search
As a rule of thumb it is always good to make use of what is
available out of the box. If You are not familiar with
google.com search syntax, check those articles:
1. https://support.google.com/websearch/answer/2466433

Try to find more information about it "Google Search Operators"
on Your own. **You will need it latter to make real use of this
tutorial.**

Try this which return developers who possibly know docker and live
or come from Argentina.
https://www.google.com/search?q=%3Asite+www.linkedin.com+docker+AND+argentina

### advance use of github search
Github has search syntax which allow You to narrow the results.
1. https://docs.github.com/en/free-pro-team@latest/github/searching-for-information-on-github/about-searching-on-github
2. https://docs.github.com/en/free-pro-team@latest/github/searching-for-information-on-github/searching-users

### using linkedin public information
The problem with linkedin is that it quickly discover that too many
resources or user information was requested from specific IP and it
will force You to do some test. The best approach would be to 
change IP address each time the linkedin test(captcha) is forced.

## implementation


## development
##### Run github spider. It will create GithubSearchSpider.json
```bash
scrapy runspider atscrapy/spiders/github_search_spider.py -a location=Poland -a language=Python
```

##### Run linkedin extraction based on data from GithubSearchSpider.json.

##### Get additional information from google search