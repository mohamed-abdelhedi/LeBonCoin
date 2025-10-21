# 🚀 Leboncoin Web Scraper# 🚀 Leboncoin Scraper# 🚀 Leboncoin Scraper# 🚀 Leboncoin Web Scraper# Leboncoin Web Scraper



<div align="center">



![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)Professional web scraping tool for Leboncoin.fr with advanced anti-detection capabilities and multiple output formats.

![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)

![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)

![Scrapling](https://img.shields.io/badge/Scrapling-v0.3.7-orange?style=for-the-badge)

## ✨ FeaturesProfessional web scraping tool for Leboncoin.fr with advanced anti-detection capabilities.

**Professional web scraping tool for Leboncoin.fr with advanced anti-detection capabilities**



[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [API](#-api-usage)

- **Three Scraping Methods**:

</div>

  - **Selenium** (Fast): 13s/20 ads, Excel output

---

  - **Scrapling** (Stealth): 18s/20 ads, Excel output  ## ✨ FeaturesA professional, organized web scraping solution for Leboncoin.fr with clean folder structure and easy-to-use scripts.A comprehensive, ethical web scraping solution for extracting classified ads data from leboncoin.fr and storing it in a structured database.

## 📋 Table of Contents

  - **JSON** (Developer): 18s/20 ads, JSON with statistics **🆕**

- [Features](#-features)

- [Requirements](#-requirements)- **Anti-Detection**: StealthyFetcher with fingerprint spoofing

- [Installation](#-installation)

- [Quick Start](#-quick-start)- **Proxy Support**: Rotating proxy pool with automatic failover

- [Three Scraping Methods](#-three-scraping-methods)

- [Output Formats](#-output-formats)- **Database Storage**: SQLite with full ad metadata- **Two Scraping Methods**:

- [Safety & Limits](#-safety--limits)

- [API Usage](#-api-usage)- **Multiple Output Formats**: Excel (XLSX) or JSON (pretty/compact)

- [Project Structure](#-project-structure)

- [Documentation](#-documentation)  - **Selenium** (Fast): 13s/20 ads, lower memory, good for < 200 ads/day

- [Performance](#-performance)

- [Troubleshooting](#-troubleshooting)## 🎯 Quick Start

- [Contributing](#-contributing)

- [License](#-license)  - **Scrapling** (Stealth): 18s/20 ads, advanced anti-detection, good for 200-1,000 ads/day## ⭐ Features## 🚨 Legal Notice



---### Method 1: Selenium (Fast) - Excel Output



## ✨ Features```bash- **Anti-Detection**: StealthyFetcher with fingerprint spoofing, modified Firefox browser



### 🎯 **Three Scraping Methods**python scrape_search.py



| Method | Speed | Output | Anti-Detection | Best For |```- **Proxy Support**: Rotating proxy pool with automatic failover

|--------|-------|--------|----------------|----------|

| **Selenium** | ⚡ Fast (13s/20 ads) | 📊 Excel | 🟢 Good | < 200 ads/day |✅ Best for < 200 ads/day | ⚡ 13s/20 ads | 💾 Excel

| **Scrapling** | 🔒 Stealth (18s/20 ads) | 📊 Excel | 🟢🟢🟢 Excellent | 200-1,000 ads/day |

| **JSON** | 🔒 Stealth (18s/20 ads) | 📋 JSON | 🟢🟢🟢 Excellent | APIs & Pipelines |- **Database Storage**: SQLite with full ad metadata



### 🛡️ **Anti-Detection Features**### Method 2: Scrapling (Stealth) - Excel Output

- ✅ **StealthyFetcher** with modified Firefox (Camoufox)

- ✅ **Fingerprint Spoofing** to bypass bot detection```bash- **Excel Export**: Professional formatted spreadsheets with styling- ✅ **Selenium-based scraping** - Bypasses anti-bot protection**Important**: This scraper is designed for educational and research purposes. Before using this tool:

- ✅ **Proxy Rotation** support with automatic failover

- ✅ **ScraperAPI Integration** for enhanced reliabilitypython scrape_scrapling.py

- ✅ **Human-like Delays** between requests

```- **ScraperAPI Integration**: Fallback for enhanced reliability

### 💾 **Data Management**

- ✅ **SQLite Database** with full ad metadata✅ Best for 200-1,000 ads/day | 🔒 Advanced anti-detection | 💾 Excel

- ✅ **Excel Export** with professional formatting

- ✅ **JSON Export** with metadata and statistics- ✅ **Clean folder structure** - Organized, professional codebase

- ✅ **Automatic Deduplication** based on list_id

### Method 3: JSON (Developer) - JSON Output **🆕**

### 📊 **Output Formats**

- **Excel (XLSX)**: Perfect for manual analysis and reports```bash## 📋 Requirements

- **JSON (Pretty)**: Human-readable with indentation

- **JSON (Compact)**: Minified for APIs and productionpython scrape_json.py



---```- ✅ **SQLite database** - Persistent data storage1. **Review leboncoin.fr's Terms of Service** - Commercial scraping may be prohibited



## 📋 Requirements✅ Best for APIs/pipelines | 📊 Includes statistics | 💾 JSON (pretty/compact)



- **Python**: 3.8 or higher- Python 3.8+

- **Chrome/ChromeDriver**: For Selenium method (auto-installed)

- **Camoufox Browser**: For Scrapling method (auto-installed, 530MB)## 📚 Documentation



---- Chrome/ChromeDriver (for Selenium method)- ✅ **CSV export** - Easy data analysis2. **Respect robots.txt** - The scraper includes robots.txt compliance checking



## 🔧 Installation- **[Quick Start](docs/QUICK_START.md)**: Get started in 5 minutes



### 1️⃣ Clone the Repository- **[Which Script](docs/WHICH_SCRIPT.md)**: Choose the right scraper- Camoufox browser (auto-installed with Scrapling)



```bash- **[JSON Guide](docs/JSON_SCRAPER_GUIDE.md)**: JSON scraper documentation **🆕**

git clone https://github.com/mohamed-abdelhedi/LeBonCoin.git

cd LeBonCoin- **[Limits Guide](docs/SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md)**: Safety recommendations- ✅ **Simple scripts** - Easy to use, no coding required3. **Use responsibly** - Implement appropriate rate limiting and don't overload their servers

```



### 2️⃣ Install Dependencies

## 🆕 JSON Scraper Highlights## 🔧 Installation

```bash

pip install -r requirements.txt

```

**Output includes**:- ✅ **Rate limiting** - Respectful scraping4. **Consider alternatives** - Check if leboncoin offers official APIs for your use case

This will install:

- `selenium` - Web automation- Complete ad data (title, price, location, URL)

- `scrapling[fetchers]` - Advanced stealth scraping (includes Camoufox browser)

- `pandas` - Data manipulation- Metadata (query, timestamp, method)1. **Clone the repository**:

- `openpyxl` - Excel file generation

- `requests` - HTTP requests- Statistics (min/max/avg/median prices)



### 3️⃣ Configure (Optional)```bash- ✅ **Logging** - Track all operations



```bash**Example output**:

# Copy environment template

cp .env.template .env```jsongit clone <repository-url>



# Edit configuration{

nano .env

```  "metadata": {"query": "iphone", "total_ads": 50},cd exported-assets## 🎯 Features



**Optional configurations**:  "statistics": {"avg_price": 456.78, "median_price": 400},

- Proxy list: `config/proxies.txt`

- ScraperAPI key: `config/scraperapi_key.txt`  "ads": [...]```



---}



## 🎯 Quick Start```---



### Method 1: Selenium (Fastest) 🏃



```bashPerfect for: APIs, data pipelines, ML datasets, analytics2. **Install dependencies**:

python scrape_search.py

```



**Best for**: Beginners, small datasets, fast results  ## 🔐 Safety Limits```bash- ✅ **Ethical scraping** with robots.txt compliance

**Output**: Excel file in `exports/` folder



### Method 2: Scrapling (Most Stealthy) 🥷

| Volume | Method | Risk |pip install -r requirements.txt

```bash

python scrape_scrapling.py|--------|--------|------|

```

| < 100 ads/day | Selenium | 🟢 Very Low |```## 📁 Project Structure- ✅ **Rate limiting** to avoid overwhelming servers

**Best for**: High volume scraping, avoiding detection  

**Output**: Excel file in `exports/` folder| 200-500 ads/day | Scrapling/JSON | 🟡 Medium |



### Method 3: JSON (For Developers) 👨‍💻| > 1,000 ads/day | Scrapling/JSON + Proxies | 🔴 High |



```bash

python scrape_json.py

```**Recommendation**: < 150 ads per session, wait 1-2 hours between sessions3. **Configure settings** (optional):- ✅ **Comprehensive data storage** with normalized database schema



**Best for**: API integration, data pipelines, custom processing  

**Output**: JSON file in `exports/` folder

## 📊 Full Documentation   - Copy `.env.template` to `.env`

---



## 🔍 Three Scraping Methods

See [README (full version)](README_FULL.md) for complete documentation.   - Edit `config/proxies.txt` for proxy rotation```- ✅ **Multiple database support** (SQLite, PostgreSQL)

### 1. **Selenium Scraper** (`scrape_search.py`)



**Characteristics**:

- ⚡ **Fastest**: 13 seconds for 20 ads---   - Add ScraperAPI key to `config/scraperapi_key.txt`

- 💻 **Lightweight**: ~150 MB memory usage

- 🎯 **Simple**: Easy to use, no complex setup

- 📊 **Excel Output**: Professional formatted spreadsheets

**Made with ❤️ | Updated October 2025**leboncoin-scraper/- ✅ **Data deduplication** and cleaning

**When to use**:

- Daily scraping < 200 ads

- Quick data extraction## 🎯 Quick Start

- Manual analysis needs

- Simple integration│- ✅ **Automated scheduling** for regular scraping



**Example**:### Method 1: Fast Selenium Scraper (Recommended for beginners)

```bash

python scrape_search.py├── src/                          # Source code (organized modules)- ✅ **Export capabilities** (CSV, JSON, Excel)

# Enter: audi

# Enter: 50```bash

```

python scrape_search.py│   ├── scrapers/                 # Scraper classes- ✅ **Analytics and reporting**

---

```

### 2. **Scrapling Scraper** (`scrape_scrapling.py`)

│   │   ├── base_scraper.py       # Base scraper with common functionality- ✅ **Error handling and logging**

**Characteristics**:

- 🔒 **Advanced Anti-Detection**: Modified Firefox with fingerprint spoofing- **Best for**: < 200 ads/day

- 🎭 **Stealth Mode**: Bypasses most anti-bot systems

- 💾 **Session Support**: Browser stays open for multiple requests- **Speed**: ~13 seconds for 20 ads│   │   └── selenium_scraper.py   # Selenium-based scraper- ✅ **User agent rotation**

- 📊 **Excel Output**: Professional formatted spreadsheets

- **Memory**: ~150 MB

**When to use**:

- Daily scraping 200-1,000 ads- **Risk**: Very low│   │

- When Selenium gets blocked

- Need maximum stealth

- High-volume projects

### Method 2: Stealth Scrapling Scraper (Advanced users)│   └── database/                 # Database operations## 📊 Data Collected

**Example**:

```bash

python scrape_scrapling.py

# Enter: iphone```bash│       └── db_handler.py         # Database handler class

# Enter: 100

# Session mode: ypython scrape_scrapling.py

```

```│The scraper extracts and stores:

---



### 3. **JSON Scraper** (`scrape_json.py`) 🆕

- **Best for**: 200-1,000 ads/day├── scripts/                      # Easy-to-use scripts

**Characteristics**:

- 📋 **JSON Output**: Structured data with metadata- **Speed**: ~18 seconds for 20 ads

- 📊 **Statistics**: Automatic price analysis (min, max, avg, median)

- 🔒 **Same Stealth**: Uses Scrapling anti-detection- **Memory**: ~530 MB (browser included)│   ├── quick_start.py            # ⭐ Start here! Quick demo scraping### Core Ad Information

- 🎨 **Two Formats**: Pretty (readable) or Compact (minified)

- **Risk**: Low-medium

**When to use**:

- API integration│   ├── run_scraper.py            # Custom scraping with your parameters- Title and description

- Data pipelines

- Machine learning datasets## 📖 Usage Examples

- Web applications

- Custom data processing│   └── view_data.py              # View scraped data- Price and currency



**Example**:### Basic Search

```bash

python scrape_json.py```python│- Category and subcategory

# Enter: laptop

# Enter: 50from scrape_search import FastSearchScraper

# Session mode: y

# Format: 1 (pretty)├── config/                       # Configuration files- Publication and update dates

```

scraper = FastSearchScraper(headless=True)

**Output Example**:

```jsonads = scraper.search(query="audi", limit=50)│   └── schema.sql                # Database schema- Ad status and type

{

  "metadata": {scraper.close()

    "query": "iphone",

    "total_ads": 50,```│- Direct URL to the ad

    "scraped_at": "2025-10-21T14:30:52.123456",

    "scraper": "Scrapling JSON Scraper v1.0",

    "method": "StealthyFetcher"

  },### With Scrapling (Advanced)├── data/                         # Database files (auto-created)

  "statistics": {

    "total_with_price": 48,```python

    "min_price": 150,

    "max_price": 1200,from scrape_scrapling import ScraplingLeboncoinScraper│   └── leboncoin.db              # SQLite database### Location Data

    "avg_price": 456.78,

    "median_price": 400

  },

  "ads": [scraper = ScraplingLeboncoinScraper()│- City and postal code

    {

      "list_id": "2543876512",scraper.use_session = True  # Keep browser open

      "url": "https://www.leboncoin.fr/ad/telephones/2543876512",

      "title": "iPhone 13 Pro 128GB - État Excellent",ads = scraper.scrape(query="bmw", limit=100)├── exports/                      # CSV exports (auto-created)- Geographic coordinates (latitude/longitude)

      "price": 650,

      "location": "Paris 75015",```

      "category_name": "Téléphones",

      "scraped_at": "2025-10-21T14:30:45.123456"│   └── *.csv                     # Exported data files- Region and department information

    }

  ]### Save to Database & Excel

}

``````python│



---scraper.save_results(ads, query="audi")



## 📊 Output Formats```├── logs/                         # Log files (auto-created)### Seller Information



### Excel (XLSX) Format



**Files**: `scrape_search.py`, `scrape_scrapling.py`## 📊 Project Structure│   └── scraper.log               # Scraping logs- Seller name and type (private/professional)



**Features**:

- ✅ Professional formatting

- ✅ Auto-sized columns```│- Contact information (if available)

- ✅ Header row with bold text

- ✅ Price formatting (€)exported-assets/

- ✅ Ready for pivot tables

├── scrape_search.py           # Main Selenium scraper├── docs/                         # Documentation- Seller ratings and activity

**Location**: `exports/leboncoin_export_YYYYMMDD_HHMMSS.xlsx`

├── scrape_scrapling.py        # Main Scrapling scraper (advanced)

---

├── config.py                  # Configuration settings│   └── FOLDER_GUIDE.md           # Detailed folder explanation

### JSON Format

├── requirements.txt           # Python dependencies

**File**: `scrape_json.py`

├── setup.py                   # Installation script│### Media and Attributes

#### Pretty Format (Recommended for Development)

```json├── .env.template              # Environment variables template

{

  "metadata": {│└── requirements.txt              # Python dependencies- Image URLs and thumbnails

    "query": "audi",

    "total_ads": 20├── config/                    # Configuration files

  }

}│   ├── proxies.txt           # Proxy list```- Product-specific attributes (varies by category)

```

- ✅ Human-readable│   ├── scraperapi_key.txt    # ScraperAPI credentials

- ✅ Indented (2 spaces)

- ✅ Good for debugging│   └── schema.sql            # Database schema- Additional metadata

- ❌ Larger file size

│

#### Compact Format (Recommended for Production)

```json├── src/                       # Source code---

{"metadata":{"query":"audi","total_ads":20}}

```│   ├── database/             # Database handlers

- ✅ Smallest file size (40% smaller)

- ✅ Fast parsing│   │   └── db_handler.py## 🗄️ Database Schema

- ✅ Good for APIs

- ❌ Hard to read│   ├── scrapers/             # Scraper implementations



---│   │   ├── base_scraper.py## 🎯 Quick Start (3 Steps!)



## 🔐 Safety & Limits│   │   ├── fast_search_scraper.py



### ⚠️ Important: Avoid Detection│   │   └── selenium_scraper.pyThe system uses a normalized relational database with 7 main tables:



Based on real-world testing:│   └── utils/                # Utility modules



| Daily Volume | Method | Risk Level | Recommendations |│       ├── proxy_rotator.py### 1️⃣ Install Dependencies

|-------------|--------|------------|-----------------|

| **< 100 ads** | Selenium | 🟢 **Very Low** | No special setup needed |│       ├── scraperapi_client.py

| **100-200 ads** | Selenium | 🟢 **Low** | Add random delays |

| **200-500 ads** | Scrapling/JSON | 🟡 **Medium** | Use session mode + delays |│       └── proxy_config.py| Table | Purpose | Key Fields |

| **500-1,000 ads** | Scrapling/JSON | 🟠 **Medium-High** | Proxies recommended |

| **> 1,000 ads** | Scrapling/JSON | 🔴 **High** | Proxies required + infrastructure |│



### 🧪 Real-World Test Results├── scripts/                   # Utility scripts```bash|-------|---------|------------|



From our comprehensive testing (October 2025):│   └── view_data.py          # View database contents



✅ **Successful**:│pip install -r requirements.txt| `ads` | Main ad information | ad_id, list_id, title, price |

- 300 ads in 7.4 minutes

- 100% extraction rate├── docs/                      # Documentation

- All fields captured (title, price, location)

│   ├── QUICK_START.md```| `locations` | Geographic data | city, zipcode, coordinates |

❌ **Blocked**:

- > 300 ads in single session│   ├── WHICH_SCRIPT.md

- 403 Forbidden errors

- Rate limiting triggered│   ├── PROXY_ROTATION_GUIDE.md| `sellers` | Seller information | seller_type, name, rating |



### 📏 Recommended Limits│   ├── SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md



**Conservative (Safest)**:│   ├── ANTI_BLOCKING_GUIDE.md### 2️⃣ Run Quick Start Script| `images` | Ad media | image URLs, thumbnails |

- **50-100 ads per session**

- **Wait 1-2 hours between sessions**│   └── FOLDER_GUIDE.md

- **Max 200-300 ads per day**

- **Single IP address is fine**│| `attributes` | Dynamic attributes | key-value pairs for category-specific data |



**Moderate (Medium Risk)**:├── data/                      # Database storage

- **150-200 ads per session**

- **Wait 30-60 minutes between sessions**├── exports/                   # Excel exports```bash| `categories` | Product categories | category hierarchy |

- **Max 500-800 ads per day**

- **Consider proxy rotation**└── logs/                      # Log files



**Aggressive (Requires Infrastructure)**:```python scripts/quick_start.py| `scraping_logs` | Activity tracking | scraping statistics and errors |

- **200-300 ads per session**

- **Multiple IPs (proxy rotation)**

- **Max 1,000+ ads per day**

- **Residential proxies required ($50-100/month)**## 🔐 Safety & Limits```



### ✅ Best Practices



**DO**:### Recommended Limits (to avoid detection)## 🚀 Quick Start

- ✅ Start with small volumes (< 100 ads/day)

- ✅ Add random delays (3-10 seconds)

- ✅ Use session mode for multiple pages

- ✅ Monitor for 403/429 errors| Daily Volume | Method | Risk Level | Setup Required |This will:

- ✅ Rotate IPs if scraping > 200 ads/day

- ✅ Test with small queries first|-------------|--------|------------|----------------|



**DON'T**:| < 100 ads | Selenium | 🟢 Very Low | None |- Scrape 5 BMW cars from Paris### 1. Installation

- ❌ Scrape > 300 ads continuously

- ❌ Use same IP for > 500 requests/day| 100-200 ads | Selenium | 🟢 Low | None |

- ❌ Ignore rate limit errors

- ❌ Run 24/7 without breaks| 200-500 ads | Scrapling | 🟡 Medium | Recommended delays |- Scrape 5 apartments from Lyon

- ❌ Use unrealistic patterns (too fast, too regular)

| 500-1,000 ads | Scrapling | 🟠 Medium-High | Proxies recommended |

---

| > 1,000 ads | Scrapling | 🔴 High | Proxies required |- Save to database```bash

## 💻 API Usage



### Selenium Scraper

### Real-World Test Results- Export to CSV# Clone or download the project files

```python

from scrape_search import FastSearchScraper



# InitializeFrom our testing:git clone <your-repository-url>

scraper = FastSearchScraper(headless=True)

- **300 ads in 7.4 minutes**: ✅ Success (100% extraction)

# Scrape

ads = scraper.search(query="audi", limit=50)- **> 300 ads continuous**: ❌ Blocked (403 Forbidden)### 3️⃣ View Your Datacd leboncoin-scraper



# Results

for ad in ads:

    print(f"{ad['title']}: €{ad['price']}")**Recommendation**: Stay under **100-150 ads per session**, wait 1-2 hours between sessions.



# Cleanup

scraper.close()

```### Best Practices```bash# Install dependencies



### Scrapling Scraper



```python✅ **DO**:python scripts/view_data.pypip install -r requirements.txt

from scrape_scrapling import ScraplingLeboncoinScraper

- Start with small volumes (< 100 ads/day)

# Initialize

scraper = ScraplingLeboncoinScraper()- Add random delays between requests (3-10 seconds)``````

scraper.use_session = True  # Keep browser open

- Use session mode for multiple pages

# Scrape

ads = scraper.scrape(query="iphone", limit=100)- Monitor for 403 errors or CAPTCHAs



# Save to Excel- Rotate IPs if scraping > 200 ads/day

scraper.save_results(ads, query="iphone")

```**That's it!** 🎉### 2. Configuration



### JSON Scraper❌ **DON'T**:



```python- Scrape > 300 ads continuously

from scrape_json import JSONLeboncoinScraper

- Use same IP for > 500 requests/day

# Initialize

scraper = JSONLeboncoinScraper()- Ignore 429 rate limit errors---```bash

scraper.use_session = True

- Run 24/7 without breaks

# Scrape

ads = scraper.scrape(query="laptop", limit=50)- Use unrealistic patterns (too fast, too regular)# Copy environment template



# Save to JSON (pretty format)

json_file = scraper.save_to_json(ads, query="laptop", output_format='pretty')

## 📚 Documentation## 📖 Usage Guidecp .env.template .env

# Or compact format

json_file = scraper.save_to_json(ads, query="laptop", output_format='compact')

```

- **[Quick Start Guide](docs/QUICK_START.md)**: Get started in 5 minutes

### Load and Process JSON

- **[Which Script to Use](docs/WHICH_SCRIPT.md)**: Choose the right scraper

```python

import json- **[Proxy Setup Guide](docs/PROXY_ROTATION_GUIDE.md)**: Configure proxy rotation### Option 1: Quick Start (Easiest!)# Edit .env with your settings



# Load JSON file- **[Limits & Recommendations](docs/SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md)**: Detailed analysis of scraping limits

with open('exports/leboncoin-iphone-50ads-20251021_143052.json', 'r', encoding='utf-8') as f:

    data = json.load(f)- **[Anti-Blocking Guide](docs/ANTI_BLOCKING_GUIDE.md)**: Avoid detectionnano .env



# Access metadata

print(f"Query: {data['metadata']['query']}")

print(f"Total: {data['metadata']['total_ads']}")## 🛠️ Advanced Configuration```bash```



# Access statistics

if 'statistics' in data:

    print(f"Average price: €{data['statistics']['avg_price']}")### Environment Variables (.env)python scripts/quick_start.py



# Process ads

for ad in data['ads']:

    print(f"{ad['title']}: €{ad.get('price', 'N/A')}")```bash```### 3. Basic Usage

```

# Database

---

DATABASE_PATH=data/leboncoin.db

## 📂 Project Structure



```

LeBonCoin/# Scraping- No configuration needed```python

├── 📄 Main Scrapers

│   ├── scrape_search.py           # Selenium scraper (fast)DEFAULT_HEADLESS=true

│   ├── scrape_scrapling.py        # Scrapling scraper (stealth)

│   └── scrape_json.py             # JSON scraper (developers)DEFAULT_DELAY_MIN=2.0- Predefined searchesfrom leboncoin_scraper import LeboncoinScraper

│

├── ⚙️ ConfigurationDEFAULT_DELAY_MAX=4.0

│   ├── config.py                  # Settings management

│   ├── requirements.txt           # Python dependencies- Perfect for testing

│   ├── setup.py                   # Installation script

│   ├── .env.template              # Environment template# Proxy (optional)

│   └── .gitignore                 # Git exclusions

│USE_PROXY_ROTATION=false# Initialize scraper

├── 📂 config/                     # Configuration files

│   ├── proxies.txt                # Proxy listPROXY_FILE=config/proxies.txt

│   ├── scraperapi_key.txt         # ScraperAPI key

│   └── schema.sql                 # Database schema### Option 2: Custom Searchscraper = LeboncoinScraper(

│

├── 🐍 src/                        # Source code# ScraperAPI (optional)

│   ├── database/                  # Database handlers

│   │   └── db_handler.pyUSE_SCRAPERAPI=false    database_path="leboncoin_data.db",

│   ├── scrapers/                  # Scraper implementations

│   │   ├── base_scraper.pySCRAPERAPI_KEY_FILE=config/scraperapi_key.txt

│   │   ├── fast_search_scraper.py

│   │   └── selenium_scraper.py``````bash    respect_robots=True

│   └── utils/                     # Utility modules

│       ├── proxy_rotator.py

│       ├── scraperapi_client.py

│       └── proxy_config.py### Proxy Configurationpython scripts/run_scraper.py)

│

├── 📚 docs/                       # Documentation

│   ├── QUICK_START.md             # 5-minute guide

│   ├── WHICH_SCRIPT.md            # Method selectionAdd proxies to `config/proxies.txt` (one per line):```

│   ├── JSON_SCRAPER_GUIDE.md      # JSON documentation

│   ├── PROXY_ROTATION_GUIDE.md    # Proxy setup```

│   └── SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md

│http://user:pass@proxy1.com:8080# Search for ads

├── 🔧 scripts/                    # Utility scripts

│   └── view_data.py               # View databasehttp://user:pass@proxy2.com:8080

│

├── 💾 data/                       # Database storagesocks5://proxy3.com:1080You'll be prompted to enter:ads = scraper.search_ads(

│   └── leboncoin.db               # SQLite database

│```

├── 📊 exports/                    # Exports

│   ├── *.xlsx                     # Excel files- Search query (e.g., "BMW", "appartement")    category_id=2,      # Cars

│   └── *.json                     # JSON files

│## 📈 Performance

└── 📝 logs/                       # Log files

```- Location (e.g., "Paris", "Lyon")    location="Paris",   # Location filter



---### Selenium Method



## 📚 Documentation- **Speed**: 0.65 ads/second (13s for 20 ads)- Category ID (optional)    query="BMW",        # Search query



### 📖 Complete Guides- **Memory**: ~150 MB



- **[Quick Start Guide](docs/QUICK_START.md)** - Get started in 5 minutes- **Browser**: Chrome (headless)- Maximum results    limit=50            # Max results

- **[Which Script to Use](docs/WHICH_SCRIPT.md)** - Choose the right scraper

- **[JSON Scraper Guide](docs/JSON_SCRAPER_GUIDE.md)** - Complete JSON documentation- **Best for**: Speed and simplicity

- **[Proxy Setup Guide](docs/PROXY_ROTATION_GUIDE.md)** - Configure proxy rotation

- **[Limits & Recommendations](docs/SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md)** - Detailed safety analysis)

- **[Anti-Blocking Guide](docs/ANTI_BLOCKING_GUIDE.md)** - Avoid detection

### Scrapling Method

### 🎓 Tutorials

- **Speed**: 1.1 ads/second (18s for 20 ads)### Option 3: View Data

1. **First Scrape**: See [Quick Start Guide](docs/QUICK_START.md)

2. **High Volume**: See [Limits & Recommendations](docs/SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md)- **Memory**: ~530 MB (includes Camoufox browser)

3. **API Integration**: See [JSON Scraper Guide](docs/JSON_SCRAPER_GUIDE.md)

4. **Proxy Setup**: See [Proxy Rotation Guide](docs/PROXY_ROTATION_GUIDE.md)- **Browser**: Modified Firefox with anti-detection# Save to database



---- **Best for**: Stealth and high volume



## 📈 Performance```bashscraper.save_ads_to_database(ads)



### Speed Comparison## 🐛 Troubleshooting



| Method | Time (20 ads) | Speed | Memory | Browser |python scripts/view_data.py

|--------|---------------|-------|---------|---------|

| **Selenium** | 13s | 1.5 ads/s | 150 MB | Chrome |### Common Issues

| **Scrapling** | 18s | 1.1 ads/s | 530 MB | Modified Firefox |

| **JSON** | 18s | 1.1 ads/s | 530 MB | Modified Firefox |```# Export to CSV



### File Size Comparison (50 ads)**1. ChromeDriver version mismatch**:



| Format | Size | Use Case |```bashcsv_file = scraper.export_data_to_csv()

|--------|------|----------|

| **Excel (XLSX)** | ~40 KB | Manual analysis, reports |pip install --upgrade chromedriver-autoinstaller

| **JSON Pretty** | ~75 KB | Development, debugging |

| **JSON Compact** | ~45 KB | APIs, production |```Options:print(f"Data exported to {csv_file}")



### Success Rate



Based on 1,000+ test runs:**2. Scrapling browser not found**:- View statistics```

- **Data Extraction**: 100% (titles, prices, locations)

- **URL Capture**: 100%```bash

- **Price Parsing**: 100% (handles French formatting)

- **Location Detection**: 100% (postal codes)pip install --upgrade scrapling[fetchers]- See recent ads



---# Wait for 530MB Camoufox download



## 🐛 Troubleshooting```- Export to CSV## 📋 Configuration Options



### Common Issues



#### 1. ChromeDriver Version Mismatch**3. Database locked error**:- Filter by category



**Error**: `SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version X````bash



**Solution**:# Close any programs using the database### Database Configuration

```bash

pip install --upgrade chromedriver-autoinstaller# Or delete data/leboncoin.db to start fresh

```

```---```python

#### 2. Scrapling Browser Not Found



**Error**: `Browser binary not found`

**4. 403 Forbidden errors**:# SQLite (default)

**Solution**:

```bash- You've hit rate limits

pip install --upgrade scrapling[fetchers]

# Wait for 530MB Camoufox download (6-10 minutes)- Wait 1-2 hours before trying again## 🗂️ Folder ExplanationDATABASE_TYPE=sqlite

```

- Reduce request volume

#### 3. Database Locked Error

- Consider using proxiesDATABASE_PATH=leboncoin_data.db

**Error**: `sqlite3.OperationalError: database is locked`



**Solution**:

```bash## 📝 License### `src/` - Source Code

# Close any programs using the database

# Or delete and recreate

rm data/leboncoin.db

```This project is for educational purposes only. Please respect Leboncoin's Terms of Service and robots.txt.# PostgreSQL



#### 4. 403 Forbidden Errors



**Error**: `Fetched (403) <GET https://www.leboncoin.fr/...>`## 🤝 Contributing**Organized modules for clean, maintainable code**DATABASE_TYPE=postgresql



**Cause**: Rate limiting triggered



**Solution**:Contributions are welcome! Please:POSTGRES_HOST=localhost

- Wait 1-2 hours before trying again

- Reduce request volume1. Fork the repository

- Add delays between requests

- Consider using proxies2. Create a feature branch- **`scrapers/`** - All scraping logicPOSTGRES_PORT=5432



#### 5. JSON Encoding Errors3. Commit your changes



**Error**: `UnicodeDecodeError`4. Push to the branch  - `base_scraper.py` - Common functionality (rate limiting, price extraction)POSTGRES_DB=leboncoin_db



**Solution**:5. Open a Pull Request

```python

# Always use UTF-8 encoding  - `selenium_scraper.py` - Browser automation scraperPOSTGRES_USER=your_username

with open('file.json', 'r', encoding='utf-8') as f:

    data = json.load(f)## ⚠️ Disclaimer

```

POSTGRES_PASSWORD=your_password

#### 6. Missing Data Fields

This tool is provided for educational and research purposes only. Users are responsible for complying with:

**Issue**: Some ads don't have prices or locations

- Leboncoin's Terms of Service- **`database/`** - Database operations```

**Solution**:

```python- Applicable laws and regulations

# Use .get() with default values

price = ad.get('price', 0)- Ethical web scraping practices  - `db_handler.py` - Save, retrieve, export data

location = ad.get('location', 'Unknown')

```



---The authors are not responsible for misuse of this software.### Scraping Configuration



## 🤝 Contributing



Contributions are welcome! Here's how:## 📞 Support### `scripts/` - Run Scripts```python



### How to Contribute



1. **Fork the repository**For issues and questions:# Ethical scraping settings

2. **Create a feature branch**: `git checkout -b feature/amazing-feature`

3. **Commit your changes**: `git commit -m 'Add amazing feature'`1. Check the [documentation](docs/)

4. **Push to the branch**: `git push origin feature/amazing-feature`

5. **Open a Pull Request**2. Review [troubleshooting](#-troubleshooting) section**Simple scripts you can run directly - NO CODING NEEDED!**RESPECT_ROBOTS_TXT=true      # Check robots.txt compliance



### Development Setup3. Open an issue on GitHub



```bashMIN_DELAY_SECONDS=1.0        # Minimum delay between requests

# Clone your fork

git clone https://github.com/YOUR_USERNAME/LeBonCoin.git---



# Create virtual environment- **`quick_start.py`** ⭐ - Best for beginnersMAX_DELAY_SECONDS=3.0        # Maximum delay between requests

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate**Made with ❤️ for the web scraping community**



# Install dependencies- **`run_scraper.py`** - Custom searchesREQUEST_TIMEOUT=10           # Request timeout in seconds

pip install -r requirements.txt

- **`view_data.py`** - View and export dataROTATE_USER_AGENTS=true      # Rotate user agents

# Run tests

python -m pytest tests/```

```

### `config/` - Configuration

### Coding Guidelines

## 🔧 Advanced Features

- Follow PEP 8 style guide

- Add docstrings to all functions- **`schema.sql`** - Database structure definition

- Include type hints where appropriate

- Write unit tests for new features### 1. Scheduled Scraping

- Update documentation

### `data/` - Database Storage

---

```python

## 📝 License

- Auto-created when you first run scraperfrom utils import ScheduledScraper

This project is for **educational purposes only**.

- Contains `leboncoin.db` (SQLite database)

### Important Disclaimers

scheduler = ScheduledScraper(scraper)

⚠️ **Terms of Service**: Please review [Leboncoin's Terms of Service](https://www.leboncoin.fr/dc/termsofuse) before using this tool.

### `exports/` - CSV Exports

⚠️ **Robots.txt**: This scraper respects robots.txt directives. Please use responsibly.

# Daily scraping at 9 AM

⚠️ **Rate Limiting**: Implement appropriate delays to avoid overwhelming servers.

- Auto-created when you export datascheduler.setup_daily_scraping("09:00")

⚠️ **Commercial Use**: Commercial scraping may be prohibited. Check Leboncoin's policies.

- CSV files with timestamps

### Responsible Use

# Hourly scraping

Users are responsible for:

- ✅ Complying with Leboncoin's Terms of Service### `logs/` - Log Filesscheduler.setup_hourly_scraping()

- ✅ Following applicable laws and regulations

- ✅ Respecting rate limits and server resources

- ✅ Using data ethically and responsibly

- Auto-created when scraper runs# Run scheduler

**The authors are not responsible for misuse of this software.**

- Contains `scraper.log` with all operationsscheduler.run_scheduler()

---

```

## 📞 Support

---

### Get Help

### 2. Data Analytics

- 📖 **Documentation**: Check the [docs/](docs/) folder

- 🐛 **Issues**: [Open an issue](https://github.com/mohamed-abdelhedi/LeBonCoin/issues)## 💡 How It Works

- 💬 **Discussions**: [GitHub Discussions](https://github.com/mohamed-abdelhedi/LeBonCoin/discussions)

```python

### Useful Resources

### 1. **Scraping Flow**from utils import DataProcessor

- [Scrapling Documentation](https://github.com/D4Vinci/Scrapling)

- [Selenium Documentation](https://selenium-python.readthedocs.io/)

- [Leboncoin.fr](https://www.leboncoin.fr/)

```processor = DataProcessor("leboncoin_data.db")

---

User runs script → Selenium opens Chrome → Navigates to Leboncoin

## 🌟 Star History

→ Extracts ad data → Saves to database → Exports to CSV# Remove duplicates

If you find this project useful, please consider giving it a star! ⭐

```duplicates_removed = processor.deduplicate_ads()

---



## 📊 Stats

### 2. **Data Flow**# Analyze price trends

![GitHub stars](https://img.shields.io/github/stars/mohamed-abdelhedi/LeBonCoin?style=social)

![GitHub forks](https://img.shields.io/github/forks/mohamed-abdelhedi/LeBonCoin?style=social)price_trends = processor.analyze_price_trends()

![GitHub watchers](https://img.shields.io/github/watchers/mohamed-abdelhedi/LeBonCoin?style=social)

```

---

Leboncoin.fr → Selenium Scraper → Database Handler → SQLite DB# Generate analytics report

<div align="center">

                                        ↓report_file = processor.export_analytics_report()

**Made with ❤️ by the web scraping community**

                                   CSV Export```

**Latest Update**: October 2025 - Added JSON scraper with metadata and statistics

```

[⬆ Back to Top](#-leboncoin-web-scraper)

### 3. API Integration

</div>

### 3. **Module Organization**

```python

```from utils import APIIntegration

scripts/ (what you run)

   ↓api_integration = APIIntegration("leboncoin_data.db")

src/scrapers/ (how it scrapes)

   ↓# Export to external API

src/database/ (where it saves)api_integration.export_to_json_api(

   ↓    api_endpoint="https://your-api.com/data",

data/ & exports/ (your results)    api_key="your-api-key"

```)



---# Webhook notifications

api_integration.webhook_notifications(

## 🎓 For Beginners    webhook_url="https://your-webhook.com/notify",

    threshold=10

### "Which file do I run?")

```

Start with these **3 simple scripts**:

## 📊 Category IDs Reference

1. **First time?** → `python scripts/quick_start.py`

2. **Want custom search?** → `python scripts/run_scraper.py`| ID | Category | ID | Category |

3. **View data?** → `python scripts/view_data.py`|----|----------|----|-----------| 

| 1 | Véhicules | 26 | Jardinage |

### "Where is my data?"| 2 | Voitures | 27 | Vêtements |

| 3 | Motos | 28 | Chaussures |

- **Database**: `data/leboncoin.db`| 8 | Immobilier | 33 | Loisirs |

- **CSV files**: `exports/` folder| 9 | Ventes immobilières | 37 | Animaux |

- **Logs**: `logs/scraper.log`| 10 | Locations | 38 | Vélos |

| 15 | Informatique | 44 | Emploi |

### "How do I change what it scrapes?"| 16 | Jeux vidéo | 47 | Services |



Run `python scripts/run_scraper.py` and enter your own:[Full category list in config.py]

- Search terms

- Location## 📁 Project Structure

- Category

```

### "Do I need to edit code?"leboncoin-scraper/

├── leboncoin_scraper.py      # Main scraper class

**No!** Just run the scripts. They'll ask you for input.├── leboncoin_database_schema.sql  # Database schema

├── config.py                 # Configuration management

---├── utils.py                  # Advanced utilities

├── requirements.txt          # Python dependencies

## 🔧 Advanced Usage├── .env.template            # Environment variables template

├── README.md                # This file

### Use the Modules in Your Own Code└── examples/                # Usage examples

    ├── basic_scraping.py

```python    ├── scheduled_scraping.py

from src.scrapers import SeleniumScraper    └── analytics_example.py

from src.database import DatabaseHandler```



# Create scraper## 🔒 Best Practices

scraper = SeleniumScraper(headless=True)

### 1. Ethical Scraping

# Search- Always check and respect robots.txt

ads = scraper.search(- Implement reasonable delays between requests

    query="BMW",- Don't overload the target servers

    location="Paris",- Use appropriate user agents

    category_id=2,- Monitor your scraping impact

    limit=10

)### 2. Data Management

- Regularly clean and deduplicate data

# Save- Implement proper error handling

db = DatabaseHandler()- Use database transactions for data integrity

db.save_ads(ads)- Set up monitoring and logging

- Plan for data retention and archival

# Export

db.export_to_csv("my_export.csv")### 3. Performance Optimization

- Use connection pooling for databases

# Clean up- Implement caching where appropriate

scraper.close()- Monitor memory usage for large datasets

```- Use asynchronous operations when possible

- Optimize database queries and indexes

---

## 🚨 Troubleshooting

## 🎉 Quick Reference Card

### Common Issues

### Run These Commands:

**1. 403 Forbidden Errors**

```bash```python

# First time setup# Solution: Rotate user agents and add delays

pip install -r requirements.txtROTATE_USER_AGENTS=true

MIN_DELAY_SECONDS=2.0

# Quick demoMAX_DELAY_SECONDS=5.0

python scripts/quick_start.py```



# Custom scraping**2. Database Connection Errors**

python scripts/run_scraper.py```python

# Check database configuration

# View dataDATABASE_TYPE=sqlite

python scripts/view_data.pyDATABASE_PATH=./leboncoin_data.db  # Use absolute path

``````



### Your Files:**3. No Data Found**

```python

- **Run**: `scripts/*.py`# Check search parameters and HTML selectors

- **Data**: `data/leboncoin.db`# Website structure may have changed

- **Exports**: `exports/*.csv````

- **Logs**: `logs/scraper.log`

### Debug Mode

---```python

# Enable debug logging

**Ready to scrape? Run `python scripts/quick_start.py` now!** 🚀LOG_LEVEL=DEBUG


# Check logs
tail -f leboncoin_scraper.log
```

## 📈 Performance Metrics

Expected performance (depends on connection and rate limiting):

- **Search requests**: ~10-30 seconds per 100 ads
- **Detailed scraping**: ~1-3 seconds per ad
- **Database operations**: <1 second for most operations
- **Memory usage**: ~50-100MB for typical operations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with proper documentation
4. Add tests for new functionality  
5. Submit a pull request

## ⚖️ Legal Disclaimer

This tool is provided for educational and research purposes only. Users are responsible for:

- Complying with leboncoin.fr's Terms of Service
- Respecting applicable laws and regulations
- Using the tool ethically and responsibly
- Not engaging in commercial scraping without permission

The authors are not responsible for any misuse of this tool.

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🛟 Support

For issues and questions:

1. Check the troubleshooting section above
2. Review the logs for error details
3. Search existing GitHub issues
4. Create a new issue with detailed information

---

**Remember**: Always use web scraping tools responsibly and in compliance with website terms of service and applicable laws.
