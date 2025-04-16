from googleapiclient.discovery import build                                   #Import the library(Google APIs)

# Replace with your own API key
api_key = "AIzaSyAva8XO08as8RBlrthcFjs4mInsxi5vnXg"                           #Youtube API

# Create a YouTube service object
youtube = build('youtube', 'v3', developerKey=api_key)                        #Interact with Youtube Data API v3

# Define the search query
query = "C++ introduction"

# Perform the search
request = youtube.search().list(
    part="snippet",                                                           #Video resource that API respone will include(snippet)
    q=query,
    type="video",                                                             #The search results to videos only
    maxResults=3                                                              #Maximum 5 videos
)
response = request.execute()

# Print the results
for item in response['items']:
    video_id = item['id']['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    print(f"Title: {item['snippet']['title']}")
    print(f"Description: {item['snippet']['description']}")
    print(f"Video URL: {video_url}")
    print()
