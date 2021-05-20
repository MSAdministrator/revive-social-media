![CI](https://github.com/MSAdministrator/revive-social-media/workflows/CI/badge.svg)

# Revive Social Media

My original path for automating the `reviving` of older blog posts & Open Source Projects I develop was using AppVeyor in a CI pipeline within a GitHub repository.  You can find details about this process here: https://letsautomate.it/article/using-github-to-revive-blog-posts/

Recently I wanted to also share out, randomly and on a scheduled basis, open-source projects & blog posts to both Twitter & LinkedIn.  This repository contains Python code to do just that using GitHub Actions.

## Using GitHub Actions to Post to Twitter & LinkedIn

This repository contains code to revive or re-share blog posts & open-source projects to Twitter & LinkedIn on a scheduled basis.  There are two workflow files.  blogs.yml and projects.yml

This new method is actually using Python and will run on a scheduled basis.  The schedule is based on a cron job defined within my GitHub Action workflow. [Blogs Yaml](
.github/workflows/blogs.yml) & [Projects Yaml](.github/workflows/projects.yml)

An example can be found below yml file is below with comments explaining the process:

```yaml
name: CI

on:
  schedule: # Defining that I want this workflow to run on a schedule
    - cron: "0 21,13 * * *" # Defining the schedule to run (21 & 13 UTC every day)
  push: # I am also defining that I want pushes to master to run this workflow here
    branches:
      - master

jobs:
  build: #you can define different stages but lets just keep it to this build stage for now

    runs-on: ubuntu-latest # The base image to use you can find more info here about the available runners here: https://help.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners

    steps:
    - uses: actions/checkout@v2 # using the latest version of github actions which checkouts the code in the repository
    - name: Installing setup-tools  # Giving this step a name
      run: sudo apt-get install python3-setuptools # what to run in this step
    - name: Install requirements # again a name is given for this step
      run: pip3 install -r requirements.txt # and what to run 
    - name: Run script
      env: # This is the important part - storing your secrets in your github account and accessing them here which sets them as environmental variables
        TWITTER_TOKEN: ${{ secrets.TWITTER_TOKEN }}
        TWITTER_SECRET_KEY: ${{ secrets.TWITTER_SECRET_KEY }}
        TWITTER_ACCESS_TOKEN: ${{ secrets.TWITTER_ACCESS_TOKEN }}
        TWITTER_ACCESS_SECRET: ${{ secrets.TWITTER_ACCESS_SECRET }}
      run: python3 run.py # now let's run our code to scrape, parse, and submit to Twitter using the above API keys
```

## Environmental Variables & Secrets

If you read the previous blog post you will know you need to create an App in Twitter and then generate a Token, Secret Key, Access Token, and Access Secret keys in order to use and post to Twitter via their APIs.

For LinkedIn, you must authenticate using OAuth2.  Please read the documentation about [Signing In with LinkedIn](https://docs.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin?context=linkedin/consumer/context) for more information.

You will need to generate a `client_id` and `client_secret` from LinkedIn.  Additionally, if you want this process to automatically authenticate you via a browser using their `Client Credential Grant Flow` (which requires selenium & chromedriver to be installed) then you must provide your username & password to linkedin as well.  If not, then generate an `access_token` and provide this.

Once you have done that then you need to store them in your GitHub account (DO NOT STORE THEM IN THE CLEAR!)

You can find info here about this process: https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets

Basically, go to your repository and click on `Settings` and then click `Secrets`. Give each of the environmental variables a name and the value will be your key value

```
TWITTER_TOKEN = ''
TWITTER_SECRET_KEY = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_SECRET = ''
LINKEDIN_CLIENT_ID = ''
LINKEDIN_CLIENT_SECRET = ''
LINKEDIN_USERNAME = ''
LINKEDIN_PASSWORD = ''
LINKEDIN_ACCESS_TOKEN = '' # Optional
```

## The Code

This project utilizes Python to parse a given HTML page and create formatted twitter posts from this data and then post them to Twitter.

This code is specifically looking for certain pieces of information within the HTML content so you will need to modify it to fit your needs.  

To start, modify the `get_data()` method to retrieve the data you want.  Next you will need to modify how the data is formatted as well, but I leave this all to you.

## Updates
Another update 
