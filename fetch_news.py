import feedparser
import requests


RSS_URL = "https://feeds.feedburner.com/TheHackersNews"
OUTPUT_FILE = "README.md"
NUM_ARTICLES = 5

README_HEADER = """# Cyber News Bot

Automated daily cybersecurity news fetcher powered by GitHub Actions.

Every day at 10:00 AM UTC, a GitHub Actions workflow runs `fetch_news.py` to pull the latest 5 articles from [The Hacker News](https://feeds.feedburner.com/TheHackersNews) RSS feed and updates this README with the results.

You can also trigger the workflow manually via the Actions tab.

## Files

- `fetch_news.py` — Fetches and parses the RSS feed, writes formatted news to `README.md`
- `.github/workflows/daily_news.yml` — GitHub Actions workflow (cron + manual dispatch)
- `requirements.txt` — Python dependencies

---

"""


def fetch_news():
    response = requests.get(RSS_URL, timeout=30)
    response.raise_for_status()
    return feedparser.parse(response.content)


def format_news(feed):
    articles = feed.entries[:NUM_ARTICLES]
    lines = ["## Latest Cybersecurity News\n"]
    lines.append(f"*Last updated: {feed.feed.get('updated', 'N/A')}*\n")

    for i, entry in enumerate(articles, 1):
        title = entry.get("title", "No title")
        link = entry.get("link", "#")
        description = entry.get("summary", "No description available.")

        lines.append(f"### {i}. {title}\n")
        lines.append(f"{description}\n")
        lines.append(f"[Read more]({link})\n")
        lines.append("---\n")

    return README_HEADER + "\n".join(lines)


def main():
    try:
        feed = fetch_news()
        content = format_news(feed)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully wrote {len(feed.entries[:NUM_ARTICLES])} articles to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error fetching news: {e}")
        raise


if __name__ == "__main__":
    main()
