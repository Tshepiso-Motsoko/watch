import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Search for the src attribute within the iframe tag using a regular expression
    match = re.search(r'<iframe.*?src="(.*?)".*?>', s)
    if match:
        # Extract the URL from the src attribute
        url = match.group(1)
        if "youtube.com/embed" in url:
            # Extract the video ID from the URL
            video_id = url.split("/")[-1]
            # Construct the shortened YouTube URL
            youtube_url = f"https://youtu.be/{video_id}"
            return youtube_url
    # Return None if no YouTube URL was found or the URL is not a YouTube link
    return None


if __name__ == "__main__":
    main()
