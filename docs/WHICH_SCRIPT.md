# Which Script Should I Use?

## 🤔 Quick Decision Guide

### Use `scrape_search.py` when:
- ✅ You need data quickly
- ✅ You want many ads (50-100+)
- ✅ Price and title are enough
- ✅ You don't need descriptions
- ✅ Time is important

### Use `scrape_detailed.py` when:
- ✅ You need full descriptions
- ✅ You want complete product details
- ✅ You're analyzing 5-20 ads
- ✅ Quality over quantity
- ✅ Time doesn't matter

---

## 📊 Side-by-Side Comparison

| Aspect | scrape_search.py | scrape_detailed.py |
|--------|------------------|-------------------|
| **Speed** | ⚡ Fast (15-30s) | 🐌 Slow (5-10min) |
| **Method** | Search page only | Visits each page |
| **Data Completeness** | ⭐⭐ Basic | ⭐⭐⭐⭐⭐ Complete |
| **Blocking Risk** | Low | Medium |
| **Best For** | Large datasets | Deep analysis |
| **Recommended Limit** | 20-100 | 5-20 |

---

## 💡 Real Examples

### Example 1: Find Cheapest iPhone
**Goal:** Find 50 iPhones and compare prices

**Use:** `scrape_search.py`
```bash
python scrape_search.py
Query: iphone
Limit: 50
```

**Why:** Fast, price is all you need, large dataset

---

### Example 2: Detailed Audi Research
**Goal:** Find 10 Audi A3 with full descriptions

**Use:** `scrape_detailed.py`
```bash
python scrape_detailed.py
Query: audi a3
Limit: 10
```

**Why:** Need descriptions, seller info, small dataset

---

### Example 3: Market Analysis
**Goal:** Analyze 200 laptops for price trends

**Use:** `scrape_search.py` (multiple runs)
```bash
python scrape_search.py
Query: laptop macbook
Limit: 50
(Run 4 times with different queries)
```

**Why:** Large dataset, price focus, need speed

---

### Example 4: Verify Specific Product
**Goal:** Check 5 specific products in detail

**Use:** `scrape_detailed.py`
```bash
python scrape_detailed.py
Query: iphone 13 pro max 256gb
Limit: 5
```

**Why:** Need everything, small number, quality check

---

## 🎯 Common Scenarios

### Scenario: "I'm blocked, what do I do?"

**Short term:** Use ScraperAPI fallback
```bash
python scrape_search.py
Proxies: n
ScraperAPI: y
```

**Long term:** Get good proxies
```bash
python scrape_search.py
Proxies: y (add paid proxies to config/proxies.txt)
ScraperAPI: y (as backup)
```

---

### Scenario: "I need 1000 ads"

**Solution:** Multiple runs with search scraper
```bash
# Run 1
python scrape_search.py
Query: laptop
Limit: 100

# Wait 10 minutes

# Run 2  
python scrape_search.py
Query: laptop
Limit: 100
(Continue...)
```

**Tips:**
- Enable proxies
- Add delays between runs
- Use ScraperAPI as fallback
- Split into smaller batches

---

### Scenario: "I need complete info but for 50 ads"

**Solution:** Use both scripts
```bash
# Step 1: Get 200 ads fast
python scrape_search.py
Query: iphone 13
Limit: 200

# Step 2: Filter in database/CSV to best 50

# Step 3: Get details for those 50
python scrape_detailed.py
Query: iphone 13 (specific filters)
Limit: 50
```

---

## ⚡ Performance Guide

### Fast Scraping (scrape_search.py)
```
20 ads  → 15 seconds
50 ads  → 30 seconds
100 ads → 1 minute
```

### Detailed Scraping (scrape_detailed.py)
```
5 ads  → 2 minutes
10 ads → 4 minutes
20 ads → 8 minutes
```

---

## 🔧 Setup Recommendations

### For Search Scraper
```
Proxies: Optional (only if scraping 100+ ads)
ScraperAPI: Yes (as safety net)
Limit: 20-100
Frequency: Can run multiple times per hour
```

### For Detailed Scraper
```
Proxies: Highly recommended
ScraperAPI: Yes (as safety net)
Limit: 5-20
Frequency: Wait 10-15 minutes between runs
```

---

## 🎓 Learning Path

### Beginner (First Time)
```bash
# Start here - simple and fast
python scrape_search.py
Query: iphone
Limit: 10
Proxies: n
ScraperAPI: y
```

### Intermediate (Know the Basics)
```bash
# Try with proxies
python scrape_search.py
Query: laptop
Limit: 50
Proxies: y
ScraperAPI: y
```

### Advanced (Production Use)
```bash
# Detailed scraping with full setup
python scrape_detailed.py
Query: audi a3 2020
Limit: 20
Proxies: y (with good paid proxies)
ScraperAPI: y
```

---

## ✅ Quick Checklist

**Before using scrape_search.py:**
- [ ] Do I only need basic data (title, price)?
- [ ] Am I OK with no descriptions?
- [ ] Do I want 20+ ads?
- [ ] Is speed important?

**Before using scrape_detailed.py:**
- [ ] Do I need descriptions?
- [ ] Am I scraping 20 or fewer ads?
- [ ] Is quality more important than speed?
- [ ] Can I wait a few minutes?

---

## 🚀 Commands Summary

### Quick Start (Beginners)
```bash
# Search scraper (fast, recommended first)
python scrape_search.py

# Detailed scraper (slow, complete)
python scrape_detailed.py
```

### With Proxies (Advanced)
```bash
# Setup proxies first
notepad config\proxies.txt
# Add your proxies, save

# Then run with proxies enabled
python scrape_search.py
# When asked: Proxies? → y
```

### Cleanup Old Files
```bash
# Remove unnecessary old files
cleanup.bat
```

---

## 📈 Success Rate

### scrape_search.py
- Direct: 95% success
- With proxies: 99% success
- With ScraperAPI: 99.9% success

### scrape_detailed.py
- Direct: 70% success (more easily blocked)
- With proxies: 95% success
- With ScraperAPI: 99% success (basic data only)

---

**Remember:** 
- Start simple (search scraper)
- Add proxies if needed
- ScraperAPI is your safety net
- Both scripts work together!
