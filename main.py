import requests
import pandas as pd

def fetch_article_data(article_id):
    """
    Fetch metadata for an article using Hacker News API.
    """
    url = f"https://hacker-news.firebaseio.com/v0/item/{article_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "title": data.get("title", "N/A"),
            "upvote_count": data.get("score", 0),
            "comment_count": data.get("descendants", 0),
            "link": f"https://news.ycombinator.com/item?id={article_id}"
        }
    return {
        "title": "N/A",
        "upvote_count": 0,
        "comment_count": 0,
        "link": f"https://news.ycombinator.com/item?id={article_id}"
    }

def parse_bookmark_file(file_path):
    """
    Parse the bookmark text file and extract article IDs.
    """
    with open(file_path, 'r') as file:
        content = file.read().strip()
    entries = content.split('-')
    article_ids = [entry.split('q')[0] for entry in entries]
    return article_ids

def create_excel(bookmark_file, output_file):
    """
    Create an Excel spreadsheet from the bookmark data.
    """
    article_ids = parse_bookmark_file(bookmark_file)
    data = []
    for article_id in article_ids:
        article_data = fetch_article_data(article_id)
        data.append(article_data)
    
    print("Successfully fetched all data.")

    # Create a DataFrame and save to Excel
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False, columns=["title", "upvote_count", "comment_count", "link"])
    print(f"Excel file created: {output_file}")



bookmark_file_path = "HarmonicBookmarks2025-1-5.txt"  # Replace with your bookmark file path
output_excel_path = "bookmarks.xlsx"
create_excel(bookmark_file_path, output_excel_path)

