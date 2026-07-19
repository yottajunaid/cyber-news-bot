# Cyber News Bot

Automated daily cybersecurity news fetcher powered by GitHub Actions.

Every day at 10:00 AM UTC, a GitHub Actions workflow runs `fetch_news.py` to pull the latest 5 articles from [The Hacker News](https://feeds.feedburner.com/TheHackersNews) RSS feed and updates `latest_news.md` with the results.

You can also trigger the workflow manually via the Actions tab.

## Files

- `fetch_news.py` — Fetches and parses the RSS feed, writes formatted news to `latest_news.md`
- `latest_news.md` — Auto-generated file with the latest articles
- `.github/workflows/daily_news.yml` — GitHub Actions workflow (cron + manual dispatch)
- `requirements.txt` — Python dependencies
