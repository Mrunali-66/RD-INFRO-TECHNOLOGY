import requests
import json
import csv
from datetime import datetime

API_KEY = "77d5b5a284f8d53d97e7122f3bd91bff"  
URL = f"https://gnews.io/api/v4/top-headlines?country=in&lang=en&token={API_KEY}"

print(" Fetching latest Indian news...\n")

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    data = response.json()

    if data.get("articles"):
        print(" Top News Headlines from India:\n")

        news_list = []

        for i, article in enumerate(data["articles"][:10], start=1):
            title = article.get("title", "No Title")
            source = article.get("source", {}).get("name", "Unknown Source")
            url = article.get("url", "No URL")

            print(f"{i}. {title}")
            print(f"   Source: {source}")
            print(f"   URL: {url}\n")

            news_list.append({
                "S.No": i,
                "Title": title,
                "Source": source,
                "URL": url
            })

        json_filename = "indian_news.json"
        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(news_list, f, indent=2, ensure_ascii=False)
        print(f" News data saved to {json_filename}")

        csv_filename = "indian_news.csv"
        with open(csv_filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["S.No", "Title", "Source", "URL"])
            writer.writeheader()
            writer.writerows(news_list)
        print(f" News data also saved to {csv_filename}")

    else:
        print(" No news articles found. Please try again later or check your API key.")

except requests.exceptions.RequestException as e:
    print("Network error:", e)
except Exception as e:
    print("Unexpected error:", e)

print(f"\n Data fetched on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(" Task completed successfully!")
