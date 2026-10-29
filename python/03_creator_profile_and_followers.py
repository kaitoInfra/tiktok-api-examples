#!/usr/bin/env python3
"""Example 03: Resolve @username to numeric user_id & secUid, then paginate 200 followers/call.

Online ID Finder Tool: https://tiktokapi.io/tools/tiktok-id-finder
Get 2,000 Free Credits: https://tiktokapi.io/signup
"""
import os
import requests

API_KEY = os.environ.get("TIKTOK_API_KEY", "tk_your_api_key_here")
BASE_URL = "https://api.tiktokapi.io"


def get_creator_profile(username: str) -> dict:
    resp = requests.get(
        f"{BASE_URL}/v1/users/profile",
        params={"username": username.lstrip("@")},
        headers={"x-api-key": API_KEY},
        timeout=20,
    )
    resp.raise_for_status()
    return resp.json()["data"]


def get_creator_followers(user_id: str, limit: int = 200, cursor: str = "0") -> dict:
    resp = requests.get(
        f"{BASE_URL}/v1/users/followers",
        params={"user_id": user_id, "limit": limit, "cursor": cursor},
        headers={"x-api-key": API_KEY},
        timeout=20,
    )
    resp.raise_for_status()
    return resp.json()["data"]


if __name__ == "__main__":
    profile = get_creator_profile("tiktok")
    user = profile["user"]
    stats = profile["stats"]
    print(f"@tiktok -> user_id={user['id']} | secUid={user['secUid'][:24]}... | followers={stats['followerCount']:,}")

    followers_page = get_creator_followers(user["id"], limit=200)
    followers = followers_page.get("followers", [])
    print(f"Fetched {len(followers)} followers in a single API call.")
