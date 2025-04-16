!pip install atproto

from atproto import Client

# Configure your credentials
BLUESKY_HANDLE = 'thanhthuy280501.bsky.social'  # e.g., 'myname.bsky.social'
APP_PASSWORD = '3ama-sxb5-zqvw-nqsf'  # From bsky.app/settings/app-passwords

def bluesky_search(query, limit=5):
    try:
        # Initialize and login
        client = Client()
        client.login(BLUESKY_HANDLE, APP_PASSWORD)

        print(f"🔍 Searching for: '{query}'...\n")

        # Correct search method with params
        results = client.app.bsky.feed.search_posts(
            params={'q': query, 'limit': limit}
        )

        if not results.posts:
            print("No results found")
            return

        for i, post in enumerate(results.posts, 1):
            text = post.record.text.replace('\n', ' ')[:100]
            print(f"\n📝 Result {i}: {text}...")
            print(f"👤 @{post.author.handle}")
            print(f"🔗 https://bsky.app/profile/{post.author.handle}/post/{post.uri.split('/')[-1]}")    #what does it show in the post??? What i can get from the post???
            print("―" * 50)                                                                               #What people reactions about that??? And compare to other platforms
                                                                                                          #Different social media platforms(Youtube, #google(not really), bluesky, reddit)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        if "AuthenticationRequired" in str(e):
            print("Tip: Verify your credentials and app password")

# Run search
bluesky_search("Python programming", limit=3)
