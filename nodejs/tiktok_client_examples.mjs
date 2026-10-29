#!/usr/bin/env node
/**
 * Node.js 18+ Quickstart Examples for TikTokAPI.io
 * Docs: https://tiktokapi.io/docs
 * Free Trial (2,000 Credits): https://tiktokapi.io/signup
 */

const API_KEY = process.env.TIKTOK_API_KEY || "tk_your_api_key_here";
const BASE_URL = "https://api.tiktokapi.io";

async function tiktokGet(path, params = {}) {
  const url = new URL(`${BASE_URL}${path}`);
  for (const [k, v] of Object.entries(params)) {
    if (v !== undefined && v !== null) url.searchParams.set(k, String(v));
  }
  const res = await fetch(url, {
    headers: { "x-api-key": API_KEY, Accept: "application/json" },
  });
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}: ${await res.text()}`);
  }
  return res.json();
}

async function main() {
  // 1. Parse a TikTok video & get 1080p HD no-watermark stream
  const video = await tiktokGet("/v1/videos/detail", {
    url: "https://www.tiktok.com/@tiktok/video/7231338487075638570",
    hd: 1,
  });
  console.log("1080p Video Stream:", video.data?.hdplay);

  // 2. Get creator profile & numeric user_id
  const profile = await tiktokGet("/v1/users/profile", { username: "tiktok" });
  console.log("Creator user_id:", profile.data?.user?.id);

  // 3. Search TikTok Creative Center Commercial Ads
  const ads = await tiktokGet("/v1/ads/search", {
    keyword: "bracelet",
    country_code: "US",
    period: 7,
    sort_by: "impression",
    limit: 5,
  });
  console.log("Commercial Ads count:", (ads.data?.materials || ads.data?.ads || []).length);
}

main().catch(console.error);
