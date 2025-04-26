# pypi-stats-timeline
**@readwithai** - [X](https://x.com/) - [blog](https://readwithai.substack.com/) - [machine-aided reading](https://www.reddit.com/r/machineAidedReading/)

Fetch and maintain timelines of downloads from Python's package Index PyPI. Query your data offline.

The website [PyPI stats](https://pypistats.org) keeps track of downloads for [Python's](https://www.python.org/) packaging system [PyPI](https://pypi.org/) used to install packages from [pip](https://github.com/pypa/pip) (and nowerdays  [pipx](https://github.com/pypa/pipx) and [uv](https://github.com/astral-sh/uv). PyPI stats provides [an API](https://pypistats.org/api/) to query this data.

This tool wraps this API for the convenience of parsing this data, the performance of caching data offline, the politeness of avoiding unnecessary API requests, and added functionality of maintaining historic data that would otherwise be removed from PyPI's window.

## Installation
You can install `pypi-stats-timeline` using [pipx](https://github.com/pypa/pipx):
```
pipx install pypi-stats-timeline
```
## Usage
To fetch statistics from the PyPI package `kitty-plotnine` you can run
```
pypi-stats-timeline kitty-plotnine
```

To display fetched data you can use the `-n` option
```
pypi-stats-timeline kitty-plotnine
```

Output is in JSON format.

To output the total number of downloads you can use `-T`.

You may well like to use anothe tools to do plotting or data analysis. I might recommend `jupyter` or a Python script with `matplotlib` for this sort of analysis. If you want to do quick and dirty analysis and plotting from the command-line I might recommend my tools [k-nine](https://github.com/talwrii/kitty-plotnine) and [npcli](https://github.com/talwrii/npcli).

## Some related tools
If you like this tool you might be interested in other [tools I have made](https://readwithai.substack.com/p/my-tools-for-statistics-about-code) to keep track of these sorts of statistics.

* [gh-views](https://github.com/talwrii/gh-views) fetches, maintains and queries the number of views and downloads for a github repo
* [gh-star-timeline](https://github.com/talwrii/gh-star-timeline) fetches, maintains and queries the number of stars for a github repo
* [obsidian-plugin-stats](https://github.com/talwrii/obsidian-plugin-stats) fetches, maintains and queries the number of downloads for a plugin for the markdown editor Obsidian.

## Support
If you like this tool, you could support it giving my money (maybe $1) on my [ko-fi](https://ko-fi.com/c/a0a71f1fbe).

This will incentivise me respond to any issues and [create similar tools](https://readwithai.substack.com/p/my-tools-for-statistics-about-code).

You could also reading some of my writing on other topics - maybe this [review of how people take notes in Obsidian](https://readwithai.substack.com/p/note-taking-with-obsidian-much-of).

# About me
I am **@readwithai**. I make tools for reading, research and agency sometimes using the note-taking tool [Obsidian](https://readwithai.substack.com/p/what-exactly-is-obsidian).

I also produce [a stream of tools](https://readwithai.substack.com/p/my-productivity-tools
) as a side effet of my work.

You can follow me on [X](https://x.com) where I talk about many things include this, or follow me on [my blog](https://readwithai.substack.com/) where I write more about Obsidian reading and research.

![logo](logo.png)
