# Job Scraper

A Python + Requests + BeautifulSoup script that scrapes job listings from the [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/) practice site, keeps only the ones that match your keywords, and saves them to a CSV file automatically

## What it does

- Asks you for keywords (like `python, developer`)
- Scrapes every job listing on the page
- Keeps only the jobs whose title contains one of your keywords (or all jobs if you leave it empty)
- Saves the title, company, location, date posted, and apply link of each job to a CSV file

## What you need to run it

- Python
- Requests and BeautifulSoup (the CSV library is built into Python)
- A code editor like [PyCharm](https://www.jetbrains.com/pycharm/download/) or [Visual Studio Code](https://code.visualstudio.com/Download) (VS Code needs the Python extension)

## Setup

1. Install Python and a code editor if you don't have them.
2. Install the libraries by typing this in the terminal:

```bash
   pip install requests beautifulsoup4
```

   If that doesn't work, try:

```bash
   py -m pip install requests beautifulsoup4
```

3. Clone or download this repo.

## The CSV file

You don't need to make this one, the script creates `job_found.csv` for you in the same folder as the Python file. The first row is a header, and every other row is one job, with the columns in this order:

```csv
title,company,location,date_posted,apply_link
```

If you run the script again, the old file gets replaced.

## Running it

```bash
py job_scraper.py
```

The script asks for your keywords, separated by commas. Press Enter without typing anything to get all the jobs:

```
enter keywords separated by commas (example: python, developer): python, engineer
```

When it finishes, it prints how many jobs it found and the name of the file it saved:

```
Found <number> matching jobs
saved job_found.csv
```

## Why I made this

I built this web scraping project to automate a repetitive task: going through a long list of job posts by hand and copying the ones that I care about.

## Need something similar?

If you need something like this for a different site or a different kind of data, message me
