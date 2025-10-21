# Leboncoin Scraper - Clean Version

## 🎯 Two Main Scripts

### 1. Search Page Scraper (Fast) ⚡
**File:** `scrape_search.py`

**What it does:**
- Extracts data from search results only
- No individual page visits
- Fast (20 ads in ~15 seconds)
- Gets: title, price, URL

**When to use:**
- Quick data collection
- Large number of ads (100+)
- Price comparisons
- Fast scanning

**Usage:**
```bash
python scrape_search.py
```

**Prompts:**
1. Query: iphone, audi, laptop, etc.
2. Limit: 20 (recommended)
3. Use proxies?: y/n
4. Use ScraperAPI fallback?: y/n

---

### 2. Detailed Scraper (Complete) 🔍
**File:** `scrape_detailed.py`

**What it does:**
- Visits each product page individually
- Extracts complete details
- Slower (20 ads in ~5 minutes)
- Gets: title, price, URL, description, seller info, images

**When to use:**
- Need full descriptions
- Small number of ads (5-20)
- Detailed analysis
- Complete data required

**Usage:**
```bash
python scrape_detailed.py
```

**Prompts:**
1. Query: iphone, audi, laptop, etc.
2. Limit: 10 (recommended - slower!)
3. Confirm (slower warning)
4. Use proxies?: y/n
5. Use ScraperAPI fallback?: y/n

---

## 🔧 Configuration

### Proxies (Optional)
**File:** `config/proxies.txt`

Add your working proxies (one per line):
```
203.142.68.62:8080
user:pass@proxy.com:3128
http://proxy.example.com:8080
```

**Tips:**
- Free proxies often don't work
- Paid proxies recommended for production
- Test proxies before using

### ScraperAPI (Fallback)
**File:** `config/scraperapi_key.txt`

Your API key: `8ec58460acff1a080001e4d930718392`

**Credits:** 4,990 / 5,000 remaining

**When it's used:**
- All proxies fail
- Direct connection blocked
- Guaranteed success

---

## 📊 Feature Comparison

| Feature | Search Scraper | Detailed Scraper |
|---------|---------------|------------------|
| Speed | ⚡ Fast (15s) | 🐌 Slow (5min) |
| Data | Basic | Complete |
| Title | ✅ | ✅ |
| Price | ✅ | ✅ |
| URL | ✅ | ✅ |
| Location | ❌ | ✅ |
| Description | ❌ | ✅ |
| Images | ❌ | ✅ |
| Seller info | ❌ | ✅ |
| Pagination | ✅ | ✅ |
| Proxy support | ✅ | ✅ |
| ScraperAPI | ✅ | ✅ |

---

## 🚀 Quick Start

### First Time Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. (Optional) Add your proxies
notepad config\proxies.txt

# 3. Run search scraper (fast)
python scrape_search.py
```

### Recommended Workflow

**For quick data collection:**
```bash
python scrape_search.py
# Query: iphone
# Limit: 50
# Proxies: y (if you have good ones)
# ScraperAPI: y (as fallback)
```

**For detailed information:**
```bash
python scrape_detailed.py
# Query: iphone 13 pro
# Limit: 10
# Proxies: y
# ScraperAPI: y
```

---

## 🔄 How It Works

### Both Scripts Follow Same Pattern:

```
1. Ask for query and limit
   ↓
2. Setup (proxies? ScraperAPI?)
   ↓
3. Try Method 1: Direct connection
   ↓ (if fails)
4. Try Method 2: Proxy rotation (if enabled)
   ↓ (if fails)
5. Try Method 3: ScraperAPI fallback (if enabled)
   ↓
6. Show results (statistics + samples)
   ↓
7. Save to database + CSV (optional)
```

---

## 💾 Output

### Database
- **File:** `data/leboncoin.db` (SQLite)
- **Auto-created** on first run
- Stores all scraped ads
- Prevents duplicates (by URL)

### CSV Export
- **Location:** `exports/` folder
- **Format:** `leboncoin-{query}-{count}ads-{timestamp}.csv`
- **Example:** `leboncoin-iphone-20ads-20251015_230439.csv`
- Can be opened in Excel

---

## ⚠️ Important Notes

### Blocking Prevention
1. **Use proxies** for large scraping jobs
2. **Add delays** between requests (built-in)
3. **Limit requests** per session (20-50 ads)
4. **Wait between runs** (5-10 minutes)

### Proxy Tips
- Free proxies: 95% don't work
- Paid proxies: Much better reliability
- Test before using: `python scripts/test_proxy.py` (if needed)

### ScraperAPI Usage
- **Free tier:** 5,000 credits/month
- **1 credit** = 1 search page request
- **5 credits** = 1 request with JavaScript rendering
- Monitor usage: Script shows remaining credits

---

## 📁 Project Structure

```
leboncoin-scraper/
├── scrape_search.py       # Main: Search page scraper (FAST)
├── scrape_detailed.py     # Main: Detailed scraper (SLOW)
├── config/
│   ├── proxies.txt        # Your proxies (optional)
│   └── scraperapi_key.txt # Your API key
├── src/
│   ├── scrapers/          # Scraper classes
│   ├── database/          # Database handler
│   └── utils/             # Utilities (proxy, API)
├── data/                  # SQLite database
├── exports/               # CSV exports
├── logs/                  # Log files
└── requirements.txt       # Dependencies
```

---

## 🆘 Troubleshooting

### "All methods failed"
**Solutions:**
1. Check internet connection
2. Try direct connection first (say 'n' to proxies)
3. Enable ScraperAPI fallback
4. Wait 1-2 hours if blocked

### "Proxy connection failed"
**Solutions:**
1. Remove dead proxies from `config/proxies.txt`
2. Use direct connection instead
3. Get fresh proxies

### "ScraperAPI error"
**Solutions:**
1. Check API key in `config/scraperapi_key.txt`
2. Verify credits remaining
3. Check scraperapi.com status

### "No results found"
**Solutions:**
1. Check query spelling
2. Try different search term
3. Verify leboncoin.fr is accessible

---

## 📈 Performance Tips

### For Speed
- Use `scrape_search.py`
- Direct connection (no proxies if not blocked)
- Limit: 20-50 ads
- Run time: 15-30 seconds

### For Reliability
- Enable proxy rotation
- Enable ScraperAPI fallback
- Start with small limits (10-20)
- Monitor for blocks

### For Complete Data
- Use `scrape_detailed.py`
- Limit: 5-10 ads max per run
- Add delays (built-in)
- Use proxies if scraping often

---

## 🎓 Examples

### Example 1: Quick iPhone Search
```bash
python scrape_search.py

Query: iphone 13
Limit: 20
Proxies: n
ScraperAPI: y

Result: 20 ads in 15 seconds
```

### Example 2: Detailed Audi Analysis
```bash
python scrape_detailed.py

Query: audi a3
Limit: 5
Proxies: y
ScraperAPI: y

Result: 5 ads with full descriptions in 2 minutes
```

### Example 3: Large Dataset Collection
```bash
python scrape_search.py

Query: laptop
Limit: 100
Proxies: y
ScraperAPI: y

Result: 100 ads in 5 minutes (with proxy rotation)
```

---

## 📞 Support

- Check `BACKGROUND_SCRAPER_FIXED.md` for detailed technical info
- Review `PROXY_ROTATION_GUIDE.md` for proxy setup
- See `exports/` folder for your scraped data

---

**Version:** 3.0 (Cleaned & Simplified)  
**Last Updated:** October 15, 2025  
**Status:** Production Ready ✅
