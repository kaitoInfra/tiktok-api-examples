#!/usr/bin/env python3
"""Example 04: Search winning commercial ads & trending ad keywords from TikTok Creative Center.

Docs: https://tiktokapi.io/guides/tiktok-ads-library-api
Get 2,000 Free Credits: https://tiktokapi.io/signup
"""
import os
import requests

API_KEY = os.environ.get("TIKTOK_API_KEY", "tk_your_api_key_here")
BASE_URL = "https://api.tiktokapi.io"


def search_commercial_ads(keyword: str, country_code: str = "US", period: int = 7, sort_by: str = "impression"):
    resp = requests.get(
        f"{BASE_URL}/v1/ads/search",
        params={
            "keyword": keyword,
            "country_code": country_code,
            "period": period,
            "sort_by": sort_by,
            "page": 1,
            "limit": 20,
        },
        headers={"x-api-key": API_KEY},
        timeout=25,
    )
    resp.raise_for_status()
    return resp.json()["data"]


if __name__ == "__main__":
    data = search_commercial_ads("bracelet", country_code="US", period=7)
    ads = data.get("materials", data.get("ads", []))
    print(f"Fetched {len(ads)} commercial ads for 'bracelet':")
    for ad in ads[:5]:
        print(f"- Ad ID: {ad.get('id')} | Brand: {ad.get('brand_name')} | CTR: {ad.get('ctr')} | Title: {ad.get('ad_title', '')[:50]}")
