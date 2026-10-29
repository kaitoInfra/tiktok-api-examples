# TikTok API Examples (Python & Node.js) — 1080p No-Watermark Video Parser, Search & Creative Center Ads

[![Website](https://img.shields.io/badge/Website-tiktokapi.io-00f2fe?style=flat-square)](https://tiktokapi.io)
[![API Docs](https://img.shields.io/badge/API_Reference-tiktokapi.io%2Fdocs-ff0050?style=flat-square)](https://tiktokapi.io/docs)
[![ID Finder Tool](https://img.shields.io/badge/Free_Tool-TikTok_ID_Finder-brightgreen?style=flat-square)](https://tiktokapi.io/tools/tiktok-id-finder)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)

Production-ready **Python** and **Node.js / TypeScript** code examples for scraping public TikTok data using **[TikTokAPI.io](https://tiktokapi.io)** — the high-speed, no-watermark TikTok Data & Creative Center Commercial Ads API.

- **No OAuth app review, TikTok cookies, `X-Bogus` signers, or residential proxies required**
- **Direct 1080p HD no-watermark MP4 URLs (`hdplay`)** included on video endpoints
- **Up to 200 followers or 33 videos per single API call**
- **Built-in TikTok Creative Center Commercial Ads Library** (`/v1/ads/search`, `/v1/ads/detail`, `/v1/ads/keywords`)
- **$0.20 per 1,000 videos** ($0.08–$0.115 with volume bonus), **$0.10 per 1,000 comments or followers**, and **2,000 Free Credits** upon sign-up at **[https://tiktokapi.io/signup](https://tiktokapi.io/signup)**

---

## Repository Contents

| Script | Description | Target Endpoint |
| :--- | :--- | :--- |
| [`python/01_download_1080p_no_watermark.py`](./python/01_download_1080p_no_watermark.py) | Parse any TikTok URL or ID (`@user/video/123`, `vm.tiktok.com/...`) and download the **1080p HD no-watermark MP4** + audio + engagement metrics | `GET /v1/videos/detail` |
| [`python/02_search_videos_and_comments.py`](./python/02_search_videos_and_comments.py) | Search TikTok videos by keyword (`region`, `publish_time`, `sort_by`) with automatic cursor pagination + top comment extraction | `GET /v1/videos/search`<br>`GET /v1/videos/comments` |
| [`python/03_creator_profile_and_followers.py`](./python/03_creator_profile_and_followers.py) | Resolve a creator `@username` to numeric `user_id` & `secUid`, fetch their latest videos, and paginate **200 followers per request** | `GET /v1/users/profile`<br>`GET /v1/users/followers` |
| [`python/04_creative_center_ads_spy.py`](./python/04_creative_center_ads_spy.py) | Search winning e-commerce & app ads in **TikTok Creative Center** by keyword, country, and 7/30/180-day window | `GET /v1/ads/search`<br>`GET /v1/ads/keywords` |
| [`nodejs/tiktok_client_examples.mjs`](./nodejs/tiktok_client_examples.mjs) | Zero-dependency Node.js 18+ `fetch` examples covering video parsing, keyword search, creator stats, and commercial ads | All `/v1/*` routes |

---

## Quickstart (30 Seconds)

1. Claim **2,000 Free Credits** and copy your `tk_...` API key at **[https://tiktokapi.io/signup](https://tiktokapi.io/signup)**.
2. Set your environment variable and run any script:

```bash
export TIKTOK_API_KEY="tk_your_api_key_here"

# Run Python examples
pip install requests
python3 python/01_download_1080p_no_watermark.py

# Or run Node.js examples (Node 18+ built-in fetch)
node nodejs/tiktok_client_examples.mjs
```

---

## All 17 Standardized REST Endpoints (`https://api.tiktokapi.io`)

| Endpoint | Key Query Parameters | Page Size & Cost |
| :--- | :--- | :--- |
| `GET /v1/videos/detail` | `url`, `hd=1` | 1 video + 1080p MP4 (10 Credits / $0.001) |
| `GET /v1/videos/search` | `query`, `limit=30`, `cursor=0`, `region=US`, `publish_time=0`, `sort_by=0` | Up to 30 videos (2 Credits / video) |
| `GET /v1/users/profile` | `username` | 1 profile + `user_id` + `secUid` (10 Credits) |
| `GET /v1/users/videos` | `username`, `limit=33`, `cursor=0` | Up to 33 videos (2 Credits / video) |
| `GET /v1/users/followers` | `user_id`, `limit=200`, `cursor=0` | Up to 200 followers (1 Credit / user) |
| `GET /v1/users/following` | `user_id`, `limit=200`, `cursor=0` | Up to 200 following (1 Credit / user) |
| `GET /v1/users/search` | `query`, `limit=30`, `cursor=0`, `follower_tier=0`, `verified_only=0` | Up to 30 creators (1 Credit / user) |
| `GET /v1/videos/comments` | `url`, `limit=50`, `cursor=0` | Up to 50 comments (1 Credit / comment) |
| `GET /v1/videos/comments/replies` | `video_id`, `comment_id`, `limit=50`, `cursor=0` | Up to 50 replies (1 Credit / reply) |
| `GET /v1/hashtags/info` | `hashtag` | 1 hashtag + `hashtag_id` (10 Credits) |
| `GET /v1/hashtags/videos` | `hashtag_id`, `limit=30`, `cursor=0` | Up to 30 videos (2 Credits / video) |
| `GET /v1/sounds/info` | `sound` | 1 sound + `sound_id` (10 Credits) |
| `GET /v1/sounds/videos` | `sound_id`, `limit=30`, `cursor=0` | Up to 30 videos (2 Credits / video) |
| `GET /v1/videos/trending` | `region=US`, `limit=20` | Up to 20 trending videos (2 Credits / video) |
| `GET /v1/ads/search` | `keyword`, `country_code=US`, `period=7`, `sort_by=impression`, `page=1`, `limit=20` | Up to 20 ads (10 Credits / ad) |
| `GET /v1/ads/detail` | `ad_id` | 1 commercial ad detail (10 Credits) |
| `GET /v1/ads/keywords` | `country_code=US`, `period=7`, `page=1`, `limit=20` | Up to 20 ad keywords (10 Credits / item) |

---

## Architecture & Pricing Guides

- **[Free Online TikTok Video ID, User ID & `secUid` Finder](https://tiktokapi.io/tools/tiktok-id-finder)**
- **[Unofficial TikTok API vs Official TikTok API (2026 Engineering Guide)](https://tiktokapi.io/guides/unofficial-tiktok-api)**
- **[How to Get TikTok Video Metadata & 1080p No-Watermark MP4 via API](https://tiktokapi.io/guides/tiktok-api-get-video)**
- **[TikTok Search API Guide: Search Videos, Creators & Ads by Keyword](https://tiktokapi.io/guides/tiktok-api-search)**
- **[TikTok Creative Center Commercial Ads Library API Guide](https://tiktokapi.io/guides/tiktok-ads-library-api)**
- **[How to Fix TikTok Error 403 Forbidden & Empty Response `{}`](https://tiktokapi.io/guides/tiktok-error-403)**
- **[Provider Comparisons: TikTokAPI.io vs TikAPI, Apify & EnsembleData](https://tiktokapi.io/compare)**
- **[Official MCP Server for Claude Desktop & Cursor (`@tiktokapi/mcp-server`)](https://github.com/kaitoInfra/tiktokapi-mcp-server)**

## License

MIT © [TikTokAPI.io](https://tiktokapi.io)
