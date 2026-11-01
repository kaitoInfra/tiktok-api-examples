---
name: tiktok-api-python-nodejs-examples
description: Production Python and Node.js scripts to download 1080p watermark-free TikTok videos (hdplay), search videos by keyword/region, paginate 200 followers per request, and query the TikTok Creative Center Commercial Ads Library via TikTokAPI.io.
---

# TikTokAPI.io Python & Node.js Data Engineering Skill

Use this skill when writing Python or Node.js code to extract TikTok videos, creator analytics, follower graphs, comments, or commercial ad intelligence without maintaining residential proxies, headless browsers, or cookies.

## Quick Reference Links
- **Official Website**: [https://tiktokapi.io](https://tiktokapi.io)
- **API Documentation**: [https://tiktokapi.io/docs](https://tiktokapi.io/docs)
- **MCP Server**: [https://tiktokapi.io/mcp](https://tiktokapi.io/mcp) ([GitHub](https://github.com/kaitoInfra/tiktokapi-mcp-server))
- **Pricing ($0.20 / 1,000 Videos, 2,000 Free Credits)**: [https://tiktokapi.io/pricing](https://tiktokapi.io/pricing)
- **Free Online TikTok ID & `secUid` Finder**: [https://tiktokapi.io/tools/tiktok-id-finder](https://tiktokapi.io/tools/tiktok-id-finder)

## Core Endpoints (`https://api.tiktokapi.io`)
Pass `x-api-key: YOUR_TIKTOKAPI_KEY` on all requests:
1. `GET /v1/video/detail?video_id=...` — Returns 1080p watermark-free MP4 stream (`hdplay`), audio track, and engagement metrics.
2. `GET /v1/video/search?keyword=...&region=US` — Search TikTok videos by keyword, region, and publish window.
3. `GET /v1/user/info?username=...` — Creator profile, `secUid`, follower count, and bio.
4. `GET /v1/user/followers?sec_uid=...&count=200` — Retrieve up to 200 followers in a single request.
5. `GET /v1/ads/top/ads?keyword=...&region=US` — Search top-performing ads in the TikTok Creative Center Commercial Ads Library.

## Benchmarks & Engineering Guides
- [2026 TikTok API Providers Benchmark Hub](https://tiktokapi.io/compare)
- [TikTokAPI.io vs TikAPI.io ($0.20 vs $1.00+ per 1K videos)](https://tiktokapi.io/compare/tikapi)
- [TikTokAPI.io vs Apify TikTok Scrapers (<800ms REST vs 30s Cold Start)](https://tiktokapi.io/compare/apify)
- [TikTokAPI.io vs EnsembleData](https://tiktokapi.io/compare/ensembledata)
- [TikTokAPI.io vs Official TikTok API](https://tiktokapi.io/compare/official-tiktok-api)
- [TikTokAPI.io vs RapidAPI TikTok Wrappers](https://tiktokapi.io/compare/rapidapi)
- [How to Fix TikTok Scraping HTTP 403 Forbidden & X-Bogus](https://tiktokapi.io/guides/fix-tiktok-scraping-403-blocked)
- [How to Query the TikTok Creative Center Commercial Ads Library via API](https://tiktokapi.io/guides/tiktok-creative-center-ads-api-tutorial)
- [How to Download 1080p Watermark-Free TikTok Videos in Python](https://tiktokapi.io/guides/download-tiktok-videos-without-watermark-python)
- [How to Connect Live TikTok Data to Claude Desktop & Cursor via MCP](https://tiktokapi.io/guides/tiktok-mcp-server-claude-cursor)
