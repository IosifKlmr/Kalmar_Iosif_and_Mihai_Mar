import os
import googleapiclient.discovery

def youtube_search(query, max_results, api_key, region_code):
    # Build the YouTube service
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    # Perform the search
    request = youtube.search().list(
        q=query,
        part="id,snippet",
        maxResults=max_results,
        regionCode=region_code
    )
    response = request.execute()

    # Extract and return relevant data
    video_data = []
    for item in response.get("items", []):
        if item["id"]["kind"] == "youtube#video":  # Check if the item is a video
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            published_at = item["snippet"]["publishedAt"]
            channel_title = item["snippet"]["channelTitle"]

            video_data.append({
                "video_id": video_id,
                "title": title,
                "description": description,
                "published_at": published_at,
                "channel_title": channel_title
            })

    return video_data

if __name__ == "__main__":
    API_KEY = 'AIzaSyAkmvSyPZfcVL8fGBT368SoYXvZVkQQPz0'  # Replace with your API key
    QUERY = 'programming'  # The chosen domain
    MAX_RESULTS = 5  # Maximum number of results
    REGION_CODE = 'us'  # The region code (e.g., 'FR' for Romania)

    videos = youtube_search(QUERY, MAX_RESULTS, API_KEY, REGION_CODE)

    for video in videos:
        print(f"ID: {video['video_id']}, Titlu: {video['title']}, Canal: {video['channel_title']}")
