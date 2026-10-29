#!/usr/bin/env python3
"""Example 02: Search TikTok videos by keyword with filters + fetch top video comments.

Docs: https://tiktokapi.io/guides/tiktok-api-search
Get 2,000 Free Credits: https://tiktokapi.io/signup
"""
import os
import requests

API_KEY = os.environ.get("TIKTOK_API_KEY", "tk_your_api_key_here")
BASE_URL = "https://api.tiktokapi.io"


def search_videos(query: str, region: str = "US", publish_time: int = 7, sort_by: int = 1, limit: int = 20) -> dict:
    """Search videos by keyword.
    sort_by: 0 = Relevance, 1 = Most Liked, 3 = Newest
    publish_time: 0 = All time, 1 = Yesterday, 7 = Last 7 days, 30 = Last 30 days
    """
    resp = requests.get(
        f"{BASE_URL}/v1/videos/search",
        params={
            "query": query,
            "region": region,
            "publish_time": publish_time,
            "sort_by": sort_by,
            "limit": limit,
            "cursor": 0,
        },
        headers={"x-api-key": API_KEY},
        timeout=25,
    )
    resp.raise_for_status()
    return resp.json()["data"]


def get_video_comments(video_url_or_id: str, limit: int = 50) -> list[dict]:
    resp = requests.get(
        f"{BASE_URL}/v1/videos/comments",
        params={"url": video_url_or_id, "limit": limit, "cursor": 0},
        headers={"x-api-key": API_KEY},
        timeout=20,
    )
    resp.raise_for_status()
    return resp.json().get("data", {}).get("comments", [])


if __name__ == "__main__":
    data = search_videos("ai coding tools", region="US", publish_time=30, sort_by=1)
    videos = data.get("videos", [])
    print(f"Found {len(videos)} videos:")
    for v in videos[:5]:
        vid = v.get("video_id") or v.get("id")
        print(f"- [{vid}] @{v.get('author', {}).get('unique_id')}: {v.get('title', '')[:60]} ({v.get('digg_count')} likes)")
