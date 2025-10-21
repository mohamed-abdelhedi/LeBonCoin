# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- CSV export functionality
- REST API wrapper
- Scheduled scraping support
- Web dashboard UI

## [1.2.0] - 2025-10-21

### Added
- 🆕 **JSON Scraper** (`scrape_json.py`)
  - Metadata generation (query, timestamp, scraper info)
  - Automatic price statistics (min, max, avg, median)
  - Two output formats: pretty (readable) and compact (minified)
  - UTF-8 encoding for French characters
  - Preview function before saving
- Comprehensive JSON Scraper Guide (`docs/JSON_SCRAPER_GUIDE.md`)
- GitHub-ready README with badges and professional formatting
- Contributing guidelines (`CONTRIBUTING.md`)
- This changelog file (`CHANGELOG.md`)

### Changed
- Updated README to include JSON scraper documentation
- Improved project structure documentation

### Fixed
- None

## [1.1.0] - 2025-10-15

### Added
- **Project Cleanup**
  - Created `.gitignore` for better repository management
  - Added `CLEANUP_SUMMARY.md` documenting all changes
  - Added `FOLDER_GUIDE.md` for project navigation
  - Organized documentation into `docs/` folder

### Removed
- Deleted 6 test/debug files:
  - `test_limits.py`
  - `test_scrapling.py`
  - `debug_scrapling.html`
  - `debug_results.txt`
  - `test_connection.py`
  - `quick_test.py`
- Deleted 8 outdated documentation files
- Removed all `__pycache__` directories
- Removed all log files from `logs/` directory
- Cleaned up 21 lines of debug code from `scrape_scrapling.py`

### Changed
- Reorganized project structure for better maintainability
- Consolidated documentation

## [1.0.0] - 2025-10-15

### Added
- **Scrapling Integration** (`scrape_scrapling.py`)
  - StealthyFetcher with Camoufox browser
  - Advanced anti-detection capabilities
  - Session mode for continuous scraping
  - Comprehensive error handling
  - Detailed logging
- Documentation suite:
  - `ANTI_BLOCKING_GUIDE.md` - Anti-detection strategies
  - `SCRAPLING_LIMITS_AND_RECOMMENDATIONS.md` - Usage guidelines
  - `QUICK_START.md` - Getting started guide
  - `PROXY_ROTATION_GUIDE.md` - Proxy configuration
  - `WHICH_SCRIPT.md` - Script comparison

### Performance
- 18 seconds per 20 ads (Scrapling method)
- 100% extraction rate for all fields
- 200 OK responses (no blocking detected)

## [0.9.0] - 2025-10-14

### Added
- **Selenium Scraper** (`scrape_search.py`)
  - Fast scraping with Chrome WebDriver
  - Excel export functionality
  - SQLite database integration
  - Basic anti-detection (random delays, user agents)
  
### Performance
- 13 seconds per 20 ads (Selenium method)
- 100% extraction rate for all fields

### Known Issues
- Limited stealth capabilities
- Higher blocking risk at scale

## [0.8.0] - 2025-10-13

### Added
- Database schema (`leboncoin_database_schema.sql`)
- Database handler (`src/database/db_handler.py`)
- SQLite integration for ad storage
- Data viewing script (`scripts/view_data.py`)

### Changed
- Improved data persistence
- Added duplicate detection

## [0.7.0] - 2025-10-12

### Added
- Proxy rotation system (`src/utils/proxy_rotator.py`)
- ScraperAPI integration (`src/utils/scraperapi_client.py`)
- Proxy configuration file (`config/proxies.txt`)
- Enhanced error handling

### Fixed
- Connection timeout issues
- Rate limiting problems

## [0.6.0] - 2025-10-11

### Added
- Base scraper class (`src/scrapers/base_scraper.py`)
- Enhanced Selenium scraper (`src/scrapers/enhanced_selenium_scraper.py`)
- Stealth scraper (`src/scrapers/stealth_scraper.py`)
- Multithreaded scraper (`src/scrapers/multithreaded_scraper.py`)

### Changed
- Refactored code into modular structure
- Improved error handling across all scrapers

## [0.5.0] - 2025-10-10

### Added
- Excel export functionality (`.xlsx` format)
- Export directory (`exports/`)
- Timestamp-based file naming

### Changed
- Improved data formatting in exports
- Added column headers

## [0.4.0] - 2025-10-09

### Added
- Price parsing with currency handling
- Location extraction
- URL extraction
- Title normalization

### Fixed
- Unicode character issues
- Price parsing for complex formats

## [0.3.0] - 2025-10-08

### Added
- Multi-page scraping
- Pagination support
- Progress tracking

### Performance
- Can scrape up to 100 ads per session

## [0.2.0] - 2025-10-07

### Added
- Basic Selenium scraper
- Chrome WebDriver integration
- Simple data extraction (title, price)

### Known Issues
- Single page scraping only
- Limited error handling

## [0.1.0] - 2025-10-06

### Added
- Initial project setup
- Basic project structure
- Requirements file
- Configuration files

---

## Legend

- 🆕 **New Feature**
- 🔧 **Bug Fix**
- 📝 **Documentation**
- ⚡ **Performance**
- 🔒 **Security**
- ⚠️ **Deprecated**
- 🗑️ **Removed**

## Version History Summary

| Version | Date | Key Feature |
|---------|------|-------------|
| 1.2.0 | 2025-10-21 | JSON Scraper with metadata |
| 1.1.0 | 2025-10-15 | Project cleanup & organization |
| 1.0.0 | 2025-10-15 | Scrapling integration (stealth) |
| 0.9.0 | 2025-10-14 | Selenium scraper |
| 0.8.0 | 2025-10-13 | Database integration |
| 0.7.0 | 2025-10-12 | Proxy rotation |
| 0.6.0 | 2025-10-11 | Modular architecture |
| 0.5.0 | 2025-10-10 | Excel export |
| 0.4.0 | 2025-10-09 | Enhanced data extraction |
| 0.3.0 | 2025-10-08 | Multi-page scraping |
| 0.2.0 | 2025-10-07 | Basic scraper |
| 0.1.0 | 2025-10-06 | Initial release |

---

**Note**: This project is for educational purposes only. Always respect leboncoin.fr's Terms of Service and robots.txt when scraping.
