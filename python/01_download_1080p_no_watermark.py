#!/usr/bin/env python3
"""Example 01: Fetch TikTok video metadata & download 1080p HD no-watermark MP4 stream.

Docs: https://tiktokapi.io/guides/tiktok-api-get-video
Get 2,000 Free Credits: https://tiktokapi.io/signup
"""
import os
import requests

API_KEY = os.environ.get("TIKTOK_API_KEY", "tk_your_api_key_here")
BASE_URL = "https://api.tiktokapi.io"


def get_tiktok_video(video_url_or_id: str) -> dict:
    resp = requests.get(
        f"{BASE_URL}/v1/videos/detail",
        params={"url": video_url_or_id, "hd": 1},
        headers={"x-api-key": API_KEY},
        timeout=20,
    )
    resp.raise_for_status()
    payload = resp.json()
    if payload.get("code") != 0:
        raise RuntimeError(f"Lookup failed (0 credits charged): {payload.get('msg')}")
    return payload["data"]


if __name__ == "__main__":
    sample_url = "https://www.tiktok.com/@tiktok/video/7231338487075638570"
    video = get_tiktok_video(sample_url)
    print(f"Video ID:      {video.get('id')}")
    print(f"Caption:       {video.get('title')}")
    print(f"Author:        @{video.get('author', {}).get('unique_id')} (user_id={video.get('author', {}).get('id')})")
    print(f"Plays / Likes: {video.get('play_count'):,} plays | {video.get('digg_count'):,} likes")
    print(f"1080p MP4 URL: {video.get('hdplay') or video.get('play')}")
