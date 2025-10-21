# 📁 Project Structure Guide# 📁 Complete Folder Structure Guide



## Overview## Overview



This is a clean, professional web scraping project for Leboncoin.fr with two scraping methods and comprehensive documentation.This document explains every folder and file in the project, what it does, and when to use it.



## Directory Layout---



```## 🎯 Quick Navigation

exported-assets/                    # Root directory

│- **Want to run scraper?** → Go to `scripts/` folder

├── 🎯 Main Scraper Files- **Want to modify code?** → Go to `src/` folder

│   ├── scrape_search.py           # Selenium-based scraper (fast, 13s/20 ads)- **Want to see data?** → Check `data/` and `exports/` folders

│   ├── scrape_scrapling.py        # Scrapling-based scraper (stealth, 18s/20 ads)- **Want configuration?** → Check `config/` folder

│   ├── config.py                  # Configuration management- **Want logs?** → Check `logs/` folder

│   ├── setup.py                   # Installation script

│   └── requirements.txt           # Python dependencies---

│

├── ⚙️ Configuration## 📂 Root Directory

│   ├── .env                       # Environment variables (gitignored)

│   ├── .env.template              # Environment template```

│   ├── .gitignore                 # Git ignore rulesC:\Users\wolfbios\Downloads\exported-assets\

│   └── leboncoin_database_schema.sql  # Database schema```

│

├── 📂 config/                     # Configuration files### Main Files:

│   ├── proxies.txt                # Proxy list (one per line)

│   ├── scraperapi_key.txt         # ScraperAPI key**`README.md`** - Start here! Main documentation

│   └── schema.sql                 # Database initialization

│**`requirements.txt`** - Python packages needed

├── 💾 data/                       # Database storage (gitignored)```bash

│   └── leboncoin.db               # SQLite database# Install all dependencies

│pip install -r requirements.txt

├── 📊 exports/                    # Excel exports (gitignored)```

│   └── *.xlsx                     # Generated spreadsheets

│---

├── 📝 logs/                       # Log files (gitignored)

│   └── *.log                      # Application logs## 📂 `src/` - Source Code (The Brain 🧠)

│

├── 🔧 scripts/                    # Utility scripts**What it is**: Organized Python modules containing all the scraping logic

│   └── view_data.py               # View database contents

│**When to edit**: Only if you want to modify how the scraper works

├── 📚 docs/                       # Documentation

│   ├── QUICK_START.md             # 5-minute getting started guide### `src/scrapers/` - Scraping Logic

│   ├── WHICH_SCRIPT.md            # Choose the right scraper

│   ├── PROXY_ROTATION_GUIDE.md    # Proxy setup instructions**`base_scraper.py`**

│   ├── SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md  # Detailed limits analysis- Base class with common functions

│   ├── ANTI_BLOCKING_GUIDE.md     # Avoid detection strategies- Rate limiting

│   ├── FOLDER_GUIDE.md            # This file- Price extraction

│   ├── leboncoin_architecture.png # Architecture diagram- URL parsing

│   └── database_schema.png        # Database schema diagram- Used by all other scrapers

│

└── 🐍 src/                        # Source code**`selenium_scraper.py`**

    ├── __init__.py- Main scraper using Selenium

    │- Opens Chrome browser

    ├── database/                  # Database layer- Handles cookie popups

    │   ├── __init__.py- Extracts ad data

    │   └── db_handler.py          # SQLite operations- **This is what actually scrapes Leboncoin!**

    │

    ├── scrapers/                  # Scraper implementations**`__init__.py`**

    │   ├── __init__.py- Makes `scrapers` a Python package

    │   ├── base_scraper.py        # Base class- Imports for easy use

    │   ├── fast_search_scraper.py # Selenium implementation

    │   └── selenium_scraper.py    # Legacy Selenium scraper### `src/database/` - Database Operations

    │

    └── utils/                     # Utility modules**`db_handler.py`**

        ├── __init__.py- Saves ads to SQLite database

        ├── proxy_rotator.py       # Proxy rotation logic- Retrieves data

        ├── scraperapi_client.py   # ScraperAPI integration- Exports to CSV

        └── proxy_config.py        # Proxy configuration- Calculates statistics

```- **This is where your data goes!**



## File Purposes**`__init__.py`**

- Makes `database` a Python package

### Main Scripts

---

| File | Purpose | When to Use |

|------|---------|-------------|## 📂 `scripts/` - Run These! (The Controls 🎮)

| `scrape_search.py` | Fast Selenium scraper | Daily use, < 200 ads/day |

| `scrape_scrapling.py` | Stealth scraper | When blocked, 200+ ads/day |**What it is**: Simple Python scripts you can run directly



### Configuration Files**When to use**: Every time you want to scrape or view data



| File | Purpose | Required? |### **`quick_start.py`** ⭐ RECOMMENDED FOR BEGINNERS

|------|---------|-----------|

| `.env` | Environment variables | No (uses defaults) |```bash

| `config/proxies.txt` | Proxy list | No (direct scraping) |python scripts/quick_start.py

| `config/scraperapi_key.txt` | ScraperAPI credentials | No (fallback only) |```



### Documentation Files**What it does:**

1. Scrapes BMW cars from Paris (5 ads)

| File | Description |2. Scrapes apartments from Lyon (5 ads)

|------|-------------|3. Saves to database

| `README.md` | Main project documentation |4. Exports to CSV

| `docs/QUICK_START.md` | Get started in 5 minutes |

| `docs/WHICH_SCRIPT.md` | Choose Selenium vs Scrapling |**When to use:**

| `docs/PROXY_ROTATION_GUIDE.md` | Set up proxy rotation |- First time using the scraper

| `docs/SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md` | Detailed limits testing results |- Want to test if everything works

| `docs/ANTI_BLOCKING_GUIDE.md` | Anti-detection strategies |- Don't want to configure anything



## What's Gitignored---



The following are excluded from version control:### **`run_scraper.py`** - Custom Searches



- `__pycache__/` - Python cache files```bash

- `*.pyc`, `*.pyo` - Compiled Python filespython scripts/run_scraper.py

- `*.log` - Log files```

- `.env` - Environment variables

- `data/*.db` - Database files**What it does:**

- `exports/*.xlsx` - Generated exports- Asks you for search parameters

- `debug_*.html` - Debug HTML files- Scrapes based on your input

- Saves results

## Clean Project Benefits

**Prompts you for:**

✅ **Professional Structure**: Well-organized directories- Search query (e.g., "BMW", "iPhone")

✅ **Clear Purpose**: Each file has a specific role- Location (e.g., "Paris", "Lyon")

✅ **No Clutter**: Removed all test/debug files- Category ID (optional)

✅ **Production Ready**: Only essential code remains- Maximum results

✅ **Good Documentation**: Comprehensive guides in docs/

✅ **Version Control**: Proper .gitignore setup**When to use:**

- Want specific search results

## Quick Navigation- Need different locations/categories

- Custom scraping needs

**Want to...**

- **Start scraping now?** → See `README.md` or `docs/QUICK_START.md`---

- **Choose a scraper?** → Read `docs/WHICH_SCRIPT.md`

- **Set up proxies?** → Follow `docs/PROXY_ROTATION_GUIDE.md`### **`view_data.py`** - View Your Data

- **Understand limits?** → Check `docs/SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md`

- **View scraped data?** → Run `python scripts/view_data.py````bash

- **Export to Excel?** → Automatic on save, check `exports/` folderpython scripts/view_data.py

```

## Maintenance

**What it does:**

### Adding New Scrapers- Shows database statistics

Place in: `src/scrapers/`- Lists recent ads

Inherit from: `BaseScraper`- Exports to CSV

- Filters by category

### Adding New Utilities

Place in: `src/utils/`**When to use:**

Import in main scripts as needed- After scraping

- Want to see what you collected

### Database Changes- Need to export data

Update: `leboncoin_database_schema.sql`- Check database contents

Apply: `config/schema.sql`

---

---

## 📂 `config/` - Configuration

**Keep it clean, keep it professional! 🚀**

**What it is**: Configuration files for the project

### **`schema.sql`**

**What it does:**
- Defines database structure
- Creates tables (ads, locations, sellers, etc.)
- Sets up relationships

**When to edit:**
- Want to add new database fields
- Modify table structure
- Advanced users only!

**Tables created:**
- `ads` - Main ad information
- `locations` - Location data
- `sellers` - Seller information
- `images` - Ad images
- `attributes` - Additional attributes
- `categories` - Category definitions
- `scraping_logs` - Scraping history

---

## 📂 `data/` - Database Storage (Your Treasure 💎)

**What it is**: Where scraped data is stored

**Auto-created**: Yes, when you first run a scraper

### **`leboncoin.db`**

**What it is:**
- SQLite database file
- Contains all your scraped ads
- Persistent storage

**How to view:**
- Use `scripts/view_data.py`
- Use SQLite Browser (GUI tool)
- Open with Python

**DO NOT DELETE** unless you want to lose all data!

---

## 📂 `exports/` - CSV Exports (Shareable Data 📊)

**What it is**: Exported CSV files for easy viewing

**Auto-created**: Yes, when you export data

### Files like: `leboncoin_export_20251015_165201.csv`

**Format**: `leboncoin_export_YYYYMMDD_HHMMSS.csv`

**What's inside:**
- All ad data in spreadsheet format
- Can open in Excel, Google Sheets
- Easy to share or analyze

**When created:**
- Automatically after scraping
- When you use "Export" option in view_data.py
- Programmatically via DatabaseHandler

**How to open:**
```bash
start exports/leboncoin_export_*.csv
```

---

## 📂 `logs/` - Log Files (The History Book 📖)

**What it is**: Logs of all scraping activities

**Auto-created**: Yes, when scraper runs

### **`scraper.log`**

**What's inside:**
- Timestamp of operations
- Success/error messages
- Browser initialization
- Ads found/saved
- Any errors that occurred

**Example:**
```
2025-10-15 16:29:41 - INFO - Chrome WebDriver initialized
2025-10-15 16:29:49 - INFO - Cookie consent accepted
2025-10-15 16:29:52 - INFO - Found 37 ad elements
2025-10-15 16:29:53 - INFO - Successfully extracted 2 ads
```

**When to check:**
- Something went wrong
- Want to see what happened
- Debugging issues
- Track scraping history

---

## 📂 `docs/` - Documentation

**What it is**: Additional documentation files

### Files:

**`FOLDER_GUIDE.md`** - This file!

**`OLD_README.md`** - Previous README (backup)

**`SCRAPING_NOTES.md`** - Technical details about scraping

**`SUCCESS_REPORT.md`** - Features and achievements

**`ISSUE_RESOLUTION.md`** - Problems solved

---

## 🗺️ Visual Map

### What You See:
```
exported-assets/
├── scripts/          ← RUN THESE!
├── src/              ← Code (don't need to touch)
├── config/           ← Configuration
├── data/             ← Your scraped data (database)
├── exports/          ← CSV files
├── logs/             ← What happened (logs)
└── docs/             ← Help files
```

### What You Use:
```
BEGINNERS:
scripts/quick_start.py  → Scrape automatically
scripts/view_data.py    → View your data
exports/*.csv           → Open in Excel

ADVANCED:
scripts/run_scraper.py  → Custom scraping
src/scrapers/           → Modify scraper code
src/database/           → Modify database code
```

---

## 🎓 Learning Path

### Level 1: Beginner (You are here!)
1. Read `README.md`
2. Run `python scripts/quick_start.py`
3. Run `python scripts/view_data.py`
4. Open CSV files in Excel

### Level 2: Intermediate
1. Run `python scripts/run_scraper.py` with custom searches
2. Explore `data/leboncoin.db` with SQLite Browser
3. Check `logs/scraper.log` to see what happened
4. Read `docs/SCRAPING_NOTES.md`

### Level 3: Advanced
1. Read code in `src/scrapers/`
2. Modify `src/database/db_handler.py` for custom exports
3. Edit `config/schema.sql` to add database fields
4. Write your own scripts using the modules

---

## 🔧 Common Tasks

### "I want to scrape"
→ Run `python scripts/quick_start.py` or `python scripts/run_scraper.py`

### "I want to see my data"
→ Run `python scripts/view_data.py` or open `exports/*.csv`

### "I want to export data"
→ Run `python scripts/view_data.py` and choose Export option

### "Something went wrong"
→ Check `logs/scraper.log`

### "I want to change how it works"
→ Edit files in `src/scrapers/` or `src/database/`

### "I want to reset everything"
→ Delete `data/` and `exports/` folders, they'll be recreated

---

## 📝 Summary

**Folders You Run:**
- `scripts/` - All runnable scripts

**Folders You View:**
- `data/` - Database files
- `exports/` - CSV exports
- `logs/` - Log files

**Folders You Read:**
- `docs/` - Documentation

**Folders You Edit (Advanced):**
- `src/` - Source code
- `config/` - Configuration

---

## 🎯 Remember

✅ **Start with** `scripts/quick_start.py`
✅ **View data with** `scripts/view_data.py`
✅ **Your data is in** `data/` and `exports/`
✅ **Logs are in** `logs/scraper.log`
✅ **Don't need to edit** `src/` unless you want to customize

---

Happy scraping! 🚀
