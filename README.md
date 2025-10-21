# 🚀 Leboncoin Scraper# 🚀 Leboncoin Scraper# 🚀 Leboncoin Web Scraper# Leboncoin Web Scraper



Professional web scraping tool for Leboncoin.fr with advanced anti-detection capabilities and multiple output formats.



## ✨ FeaturesProfessional web scraping tool for Leboncoin.fr with advanced anti-detection capabilities.



- **Three Scraping Methods**:

  - **Selenium** (Fast): 13s/20 ads, Excel output

  - **Scrapling** (Stealth): 18s/20 ads, Excel output  ## ✨ FeaturesA professional, organized web scraping solution for Leboncoin.fr with clean folder structure and easy-to-use scripts.A comprehensive, ethical web scraping solution for extracting classified ads data from leboncoin.fr and storing it in a structured database.

  - **JSON** (Developer): 18s/20 ads, JSON with statistics **🆕**

- **Anti-Detection**: StealthyFetcher with fingerprint spoofing

- **Proxy Support**: Rotating proxy pool with automatic failover

- **Database Storage**: SQLite with full ad metadata- **Two Scraping Methods**:

- **Multiple Output Formats**: Excel (XLSX) or JSON (pretty/compact)

  - **Selenium** (Fast): 13s/20 ads, lower memory, good for < 200 ads/day

## 🎯 Quick Start

  - **Scrapling** (Stealth): 18s/20 ads, advanced anti-detection, good for 200-1,000 ads/day## ⭐ Features## 🚨 Legal Notice

### Method 1: Selenium (Fast) - Excel Output

```bash- **Anti-Detection**: StealthyFetcher with fingerprint spoofing, modified Firefox browser

python scrape_search.py

```- **Proxy Support**: Rotating proxy pool with automatic failover

✅ Best for < 200 ads/day | ⚡ 13s/20 ads | 💾 Excel

- **Database Storage**: SQLite with full ad metadata

### Method 2: Scrapling (Stealth) - Excel Output

```bash- **Excel Export**: Professional formatted spreadsheets with styling- ✅ **Selenium-based scraping** - Bypasses anti-bot protection**Important**: This scraper is designed for educational and research purposes. Before using this tool:

python scrape_scrapling.py

```- **ScraperAPI Integration**: Fallback for enhanced reliability

✅ Best for 200-1,000 ads/day | 🔒 Advanced anti-detection | 💾 Excel

- ✅ **Clean folder structure** - Organized, professional codebase

### Method 3: JSON (Developer) - JSON Output **🆕**

```bash## 📋 Requirements

python scrape_json.py

```- ✅ **SQLite database** - Persistent data storage1. **Review leboncoin.fr's Terms of Service** - Commercial scraping may be prohibited

✅ Best for APIs/pipelines | 📊 Includes statistics | 💾 JSON (pretty/compact)

- Python 3.8+

## 📚 Documentation

- Chrome/ChromeDriver (for Selenium method)- ✅ **CSV export** - Easy data analysis2. **Respect robots.txt** - The scraper includes robots.txt compliance checking

- **[Quick Start](docs/QUICK_START.md)**: Get started in 5 minutes

- **[Which Script](docs/WHICH_SCRIPT.md)**: Choose the right scraper- Camoufox browser (auto-installed with Scrapling)

- **[JSON Guide](docs/JSON_SCRAPER_GUIDE.md)**: JSON scraper documentation **🆕**

- **[Limits Guide](docs/SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md)**: Safety recommendations- ✅ **Simple scripts** - Easy to use, no coding required3. **Use responsibly** - Implement appropriate rate limiting and don't overload their servers



## 🆕 JSON Scraper Highlights## 🔧 Installation



**Output includes**:- ✅ **Rate limiting** - Respectful scraping4. **Consider alternatives** - Check if leboncoin offers official APIs for your use case

- Complete ad data (title, price, location, URL)

- Metadata (query, timestamp, method)1. **Clone the repository**:

- Statistics (min/max/avg/median prices)

```bash- ✅ **Logging** - Track all operations

**Example output**:

```jsongit clone <repository-url>

{

  "metadata": {"query": "iphone", "total_ads": 50},cd exported-assets## 🎯 Features

  "statistics": {"avg_price": 456.78, "median_price": 400},

  "ads": [...]```

}

```---



Perfect for: APIs, data pipelines, ML datasets, analytics2. **Install dependencies**:



## 🔐 Safety Limits```bash- ✅ **Ethical scraping** with robots.txt compliance



| Volume | Method | Risk |pip install -r requirements.txt

|--------|--------|------|

| < 100 ads/day | Selenium | 🟢 Very Low |```## 📁 Project Structure- ✅ **Rate limiting** to avoid overwhelming servers

| 200-500 ads/day | Scrapling/JSON | 🟡 Medium |

| > 1,000 ads/day | Scrapling/JSON + Proxies | 🔴 High |



**Recommendation**: < 150 ads per session, wait 1-2 hours between sessions3. **Configure settings** (optional):- ✅ **Comprehensive data storage** with normalized database schema



## 📊 Full Documentation   - Copy `.env.template` to `.env`



See [README (full version)](README_FULL.md) for complete documentation.   - Edit `config/proxies.txt` for proxy rotation```- ✅ **Multiple database support** (SQLite, PostgreSQL)



---   - Add ScraperAPI key to `config/scraperapi_key.txt`



**Made with ❤️ | Updated October 2025**leboncoin-scraper/- ✅ **Data deduplication** and cleaning


## 🎯 Quick Start

│- ✅ **Automated scheduling** for regular scraping

### Method 1: Fast Selenium Scraper (Recommended for beginners)

├── src/                          # Source code (organized modules)- ✅ **Export capabilities** (CSV, JSON, Excel)

```bash

python scrape_search.py│   ├── scrapers/                 # Scraper classes- ✅ **Analytics and reporting**

```

│   │   ├── base_scraper.py       # Base scraper with common functionality- ✅ **Error handling and logging**

- **Best for**: < 200 ads/day

- **Speed**: ~13 seconds for 20 ads│   │   └── selenium_scraper.py   # Selenium-based scraper- ✅ **User agent rotation**

- **Memory**: ~150 MB

- **Risk**: Very low│   │



### Method 2: Stealth Scrapling Scraper (Advanced users)│   └── database/                 # Database operations## 📊 Data Collected



```bash│       └── db_handler.py         # Database handler class

python scrape_scrapling.py

```│The scraper extracts and stores:



- **Best for**: 200-1,000 ads/day├── scripts/                      # Easy-to-use scripts

- **Speed**: ~18 seconds for 20 ads

- **Memory**: ~530 MB (browser included)│   ├── quick_start.py            # ⭐ Start here! Quick demo scraping### Core Ad Information

- **Risk**: Low-medium

│   ├── run_scraper.py            # Custom scraping with your parameters- Title and description

## 📖 Usage Examples

│   └── view_data.py              # View scraped data- Price and currency

### Basic Search

```python│- Category and subcategory

from scrape_search import FastSearchScraper

├── config/                       # Configuration files- Publication and update dates

scraper = FastSearchScraper(headless=True)

ads = scraper.search(query="audi", limit=50)│   └── schema.sql                # Database schema- Ad status and type

scraper.close()

```│- Direct URL to the ad



### With Scrapling (Advanced)├── data/                         # Database files (auto-created)

```python

from scrape_scrapling import ScraplingLeboncoinScraper│   └── leboncoin.db              # SQLite database### Location Data



scraper = ScraplingLeboncoinScraper()│- City and postal code

scraper.use_session = True  # Keep browser open

ads = scraper.scrape(query="bmw", limit=100)├── exports/                      # CSV exports (auto-created)- Geographic coordinates (latitude/longitude)

```

│   └── *.csv                     # Exported data files- Region and department information

### Save to Database & Excel

```python│

scraper.save_results(ads, query="audi")

```├── logs/                         # Log files (auto-created)### Seller Information



## 📊 Project Structure│   └── scraper.log               # Scraping logs- Seller name and type (private/professional)



```│- Contact information (if available)

exported-assets/

├── scrape_search.py           # Main Selenium scraper├── docs/                         # Documentation- Seller ratings and activity

├── scrape_scrapling.py        # Main Scrapling scraper (advanced)

├── config.py                  # Configuration settings│   └── FOLDER_GUIDE.md           # Detailed folder explanation

├── requirements.txt           # Python dependencies

├── setup.py                   # Installation script│### Media and Attributes

├── .env.template              # Environment variables template

│└── requirements.txt              # Python dependencies- Image URLs and thumbnails

├── config/                    # Configuration files

│   ├── proxies.txt           # Proxy list```- Product-specific attributes (varies by category)

│   ├── scraperapi_key.txt    # ScraperAPI credentials

│   └── schema.sql            # Database schema- Additional metadata

│

├── src/                       # Source code---

│   ├── database/             # Database handlers

│   │   └── db_handler.py## 🗄️ Database Schema

│   ├── scrapers/             # Scraper implementations

│   │   ├── base_scraper.py## 🎯 Quick Start (3 Steps!)

│   │   ├── fast_search_scraper.py

│   │   └── selenium_scraper.pyThe system uses a normalized relational database with 7 main tables:

│   └── utils/                # Utility modules

│       ├── proxy_rotator.py### 1️⃣ Install Dependencies

│       ├── scraperapi_client.py

│       └── proxy_config.py| Table | Purpose | Key Fields |

│

├── scripts/                   # Utility scripts```bash|-------|---------|------------|

│   └── view_data.py          # View database contents

│pip install -r requirements.txt| `ads` | Main ad information | ad_id, list_id, title, price |

├── docs/                      # Documentation

│   ├── QUICK_START.md```| `locations` | Geographic data | city, zipcode, coordinates |

│   ├── WHICH_SCRIPT.md

│   ├── PROXY_ROTATION_GUIDE.md| `sellers` | Seller information | seller_type, name, rating |

│   ├── SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md

│   ├── ANTI_BLOCKING_GUIDE.md### 2️⃣ Run Quick Start Script| `images` | Ad media | image URLs, thumbnails |

│   └── FOLDER_GUIDE.md

│| `attributes` | Dynamic attributes | key-value pairs for category-specific data |

├── data/                      # Database storage

├── exports/                   # Excel exports```bash| `categories` | Product categories | category hierarchy |

└── logs/                      # Log files

```python scripts/quick_start.py| `scraping_logs` | Activity tracking | scraping statistics and errors |



## 🔐 Safety & Limits```



### Recommended Limits (to avoid detection)## 🚀 Quick Start



| Daily Volume | Method | Risk Level | Setup Required |This will:

|-------------|--------|------------|----------------|

| < 100 ads | Selenium | 🟢 Very Low | None |- Scrape 5 BMW cars from Paris### 1. Installation

| 100-200 ads | Selenium | 🟢 Low | None |

| 200-500 ads | Scrapling | 🟡 Medium | Recommended delays |- Scrape 5 apartments from Lyon

| 500-1,000 ads | Scrapling | 🟠 Medium-High | Proxies recommended |

| > 1,000 ads | Scrapling | 🔴 High | Proxies required |- Save to database```bash



### Real-World Test Results- Export to CSV# Clone or download the project files



From our testing:git clone <your-repository-url>

- **300 ads in 7.4 minutes**: ✅ Success (100% extraction)

- **> 300 ads continuous**: ❌ Blocked (403 Forbidden)### 3️⃣ View Your Datacd leboncoin-scraper



**Recommendation**: Stay under **100-150 ads per session**, wait 1-2 hours between sessions.



### Best Practices```bash# Install dependencies



✅ **DO**:python scripts/view_data.pypip install -r requirements.txt

- Start with small volumes (< 100 ads/day)

- Add random delays between requests (3-10 seconds)``````

- Use session mode for multiple pages

- Monitor for 403 errors or CAPTCHAs

- Rotate IPs if scraping > 200 ads/day

**That's it!** 🎉### 2. Configuration

❌ **DON'T**:

- Scrape > 300 ads continuously

- Use same IP for > 500 requests/day

- Ignore 429 rate limit errors---```bash

- Run 24/7 without breaks

- Use unrealistic patterns (too fast, too regular)# Copy environment template



## 📚 Documentation## 📖 Usage Guidecp .env.template .env



- **[Quick Start Guide](docs/QUICK_START.md)**: Get started in 5 minutes

- **[Which Script to Use](docs/WHICH_SCRIPT.md)**: Choose the right scraper

- **[Proxy Setup Guide](docs/PROXY_ROTATION_GUIDE.md)**: Configure proxy rotation### Option 1: Quick Start (Easiest!)# Edit .env with your settings

- **[Limits & Recommendations](docs/SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md)**: Detailed analysis of scraping limits

- **[Anti-Blocking Guide](docs/ANTI_BLOCKING_GUIDE.md)**: Avoid detectionnano .env



## 🛠️ Advanced Configuration```bash```



### Environment Variables (.env)python scripts/quick_start.py



```bash```### 3. Basic Usage

# Database

DATABASE_PATH=data/leboncoin.db



# Scraping- No configuration needed```python

DEFAULT_HEADLESS=true

DEFAULT_DELAY_MIN=2.0- Predefined searchesfrom leboncoin_scraper import LeboncoinScraper

DEFAULT_DELAY_MAX=4.0

- Perfect for testing

# Proxy (optional)

USE_PROXY_ROTATION=false# Initialize scraper

PROXY_FILE=config/proxies.txt

### Option 2: Custom Searchscraper = LeboncoinScraper(

# ScraperAPI (optional)

USE_SCRAPERAPI=false    database_path="leboncoin_data.db",

SCRAPERAPI_KEY_FILE=config/scraperapi_key.txt

``````bash    respect_robots=True



### Proxy Configurationpython scripts/run_scraper.py)



Add proxies to `config/proxies.txt` (one per line):```

```

http://user:pass@proxy1.com:8080# Search for ads

http://user:pass@proxy2.com:8080

socks5://proxy3.com:1080You'll be prompted to enter:ads = scraper.search_ads(

```

- Search query (e.g., "BMW", "appartement")    category_id=2,      # Cars

## 📈 Performance

- Location (e.g., "Paris", "Lyon")    location="Paris",   # Location filter

### Selenium Method

- **Speed**: 0.65 ads/second (13s for 20 ads)- Category ID (optional)    query="BMW",        # Search query

- **Memory**: ~150 MB

- **Browser**: Chrome (headless)- Maximum results    limit=50            # Max results

- **Best for**: Speed and simplicity

)

### Scrapling Method

- **Speed**: 1.1 ads/second (18s for 20 ads)### Option 3: View Data

- **Memory**: ~530 MB (includes Camoufox browser)

- **Browser**: Modified Firefox with anti-detection# Save to database

- **Best for**: Stealth and high volume

```bashscraper.save_ads_to_database(ads)

## 🐛 Troubleshooting

python scripts/view_data.py

### Common Issues

```# Export to CSV

**1. ChromeDriver version mismatch**:

```bashcsv_file = scraper.export_data_to_csv()

pip install --upgrade chromedriver-autoinstaller

```Options:print(f"Data exported to {csv_file}")



**2. Scrapling browser not found**:- View statistics```

```bash

pip install --upgrade scrapling[fetchers]- See recent ads

# Wait for 530MB Camoufox download

```- Export to CSV## 📋 Configuration Options



**3. Database locked error**:- Filter by category

```bash

# Close any programs using the database### Database Configuration

# Or delete data/leboncoin.db to start fresh

```---```python



**4. 403 Forbidden errors**:# SQLite (default)

- You've hit rate limits

- Wait 1-2 hours before trying again## 🗂️ Folder ExplanationDATABASE_TYPE=sqlite

- Reduce request volume

- Consider using proxiesDATABASE_PATH=leboncoin_data.db



## 📝 License### `src/` - Source Code



This project is for educational purposes only. Please respect Leboncoin's Terms of Service and robots.txt.# PostgreSQL



## 🤝 Contributing**Organized modules for clean, maintainable code**DATABASE_TYPE=postgresql



Contributions are welcome! Please:POSTGRES_HOST=localhost

1. Fork the repository

2. Create a feature branch- **`scrapers/`** - All scraping logicPOSTGRES_PORT=5432

3. Commit your changes

4. Push to the branch  - `base_scraper.py` - Common functionality (rate limiting, price extraction)POSTGRES_DB=leboncoin_db

5. Open a Pull Request

  - `selenium_scraper.py` - Browser automation scraperPOSTGRES_USER=your_username

## ⚠️ Disclaimer

POSTGRES_PASSWORD=your_password

This tool is provided for educational and research purposes only. Users are responsible for complying with:

- Leboncoin's Terms of Service- **`database/`** - Database operations```

- Applicable laws and regulations

- Ethical web scraping practices  - `db_handler.py` - Save, retrieve, export data



The authors are not responsible for misuse of this software.### Scraping Configuration



## 📞 Support### `scripts/` - Run Scripts```python



For issues and questions:# Ethical scraping settings

1. Check the [documentation](docs/)

2. Review [troubleshooting](#-troubleshooting) section**Simple scripts you can run directly - NO CODING NEEDED!**RESPECT_ROBOTS_TXT=true      # Check robots.txt compliance

3. Open an issue on GitHub

MIN_DELAY_SECONDS=1.0        # Minimum delay between requests

---

- **`quick_start.py`** ⭐ - Best for beginnersMAX_DELAY_SECONDS=3.0        # Maximum delay between requests

**Made with ❤️ for the web scraping community**

- **`run_scraper.py`** - Custom searchesREQUEST_TIMEOUT=10           # Request timeout in seconds

- **`view_data.py`** - View and export dataROTATE_USER_AGENTS=true      # Rotate user agents

```

### `config/` - Configuration

## 🔧 Advanced Features

- **`schema.sql`** - Database structure definition

### 1. Scheduled Scraping

### `data/` - Database Storage

```python

- Auto-created when you first run scraperfrom utils import ScheduledScraper

- Contains `leboncoin.db` (SQLite database)

scheduler = ScheduledScraper(scraper)

### `exports/` - CSV Exports

# Daily scraping at 9 AM

- Auto-created when you export datascheduler.setup_daily_scraping("09:00")

- CSV files with timestamps

# Hourly scraping

### `logs/` - Log Filesscheduler.setup_hourly_scraping()



- Auto-created when scraper runs# Run scheduler

- Contains `scraper.log` with all operationsscheduler.run_scheduler()

```

---

### 2. Data Analytics

## 💡 How It Works

```python

### 1. **Scraping Flow**from utils import DataProcessor



```processor = DataProcessor("leboncoin_data.db")

User runs script → Selenium opens Chrome → Navigates to Leboncoin

→ Extracts ad data → Saves to database → Exports to CSV# Remove duplicates

```duplicates_removed = processor.deduplicate_ads()



### 2. **Data Flow**# Analyze price trends

price_trends = processor.analyze_price_trends()

```

Leboncoin.fr → Selenium Scraper → Database Handler → SQLite DB# Generate analytics report

                                        ↓report_file = processor.export_analytics_report()

                                   CSV Export```

```

### 3. API Integration

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
