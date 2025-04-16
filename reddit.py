!pip install praw --quiet  # Install PRAW quietly
import praw  # Import after installation

# Initialize Reddit instance (using script app authentication)
reddit = praw.Reddit(
    client_id="q6ss1j9cykB3vAgWFRcPIQ",
    client_secret="kmEkjdviivBwAFIh-hIiistSwP2QPg",
    user_agent="script:my_reddit_scraper:v1.0 (by /u/YOUR_USERNAME)",
    username="YOUR_REDDIT_USERNAME",  # Required for script-type apps
    password="YOUR_REDDIT_PASSWORD",  # Required for script-type apps
)

def search_reddit(query, limit=5):
    try:
        print(f"Searching Reddit for: '{query}'...\n")
        subreddit = reddit.subreddit("all")
        results = subreddit.search(query, limit=limit, sort='relevance')

        for i, post in enumerate(results, 1):
            print(f"Result #{i}:")
            print(f"Title: {post.title}")
            print(f"Author: u/{post.author}" if post.author else "Author: [deleted]")
            print(f"Subreddit: r/{post.subreddit}")
            print(f"Upvotes: {post.score}")
            print(f"Comments: {post.num_comments}")
            print(f"URL: https://reddit.com{post.permalink}")
            print("-" * 80)

    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage
search_reddit("C++ introduction")
