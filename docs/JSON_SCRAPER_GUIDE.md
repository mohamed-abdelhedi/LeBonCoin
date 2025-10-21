# 📋 JSON Scraper Guide

## Overview

`scrape_json.py` is a specialized version of the Scrapling scraper that outputs results in **JSON format** instead of Excel. Perfect for:
- API integration
- Data pipelines
- Custom processing
- Web applications
- Machine learning datasets

## 🎯 Features

### JSON-Specific Features
- **Pretty or Compact Format**: Choose readable (indented) or minified JSON
- **Rich Metadata**: Includes scraping timestamp, query, method
- **Statistics**: Automatic price analysis (min, max, avg, median)
- **Structured Output**: Clean, consistent JSON schema
- **UTF-8 Encoding**: Proper French character support

### Inherited Features (from Scrapling)
- ✅ Advanced anti-detection with StealthyFetcher
- ✅ Modified Firefox browser (530MB Camoufox)
- ✅ Fingerprint spoofing
- ✅ Session mode (browser stays open)
- ✅ One-shot mode (browser per request)
- ✅ 100% data extraction rate

## 🚀 Quick Start

### Basic Usage

```bash
python scrape_json.py
```

**Interactive prompts**:
1. Enter search query (e.g., "iphone", "audi")
2. Enter number of ads (default: 20)
3. Choose session mode (y/n)
4. Choose JSON format (pretty/compact)

### Example Session

```
Search query: iphone
Number of ads: 30
Use session mode? y
Choose format (1=Pretty, 2=Compact): 1

✅ Scraped 30 ads
💾 Saved: exports/leboncoin-iphone-30ads-20251021_143052.json
```

## 📊 JSON Output Format

### Structure

```json
{
  "metadata": {
    "query": "iphone",
    "total_ads": 30,
    "scraped_at": "2025-10-21T14:30:52.123456",
    "scraper": "Scrapling JSON Scraper v1.0",
    "method": "StealthyFetcher"
  },
  "statistics": {
    "total_with_price": 28,
    "min_price": 150,
    "max_price": 1200,
    "avg_price": 456.78,
    "median_price": 400
  },
  "ads": [
    {
      "list_id": "2543876512",
      "url": "https://www.leboncoin.fr/ad/telephones/2543876512",
      "title": "iPhone 13 Pro 128GB - État Excellent",
      "price": 650,
      "location": "Paris 75015",
      "category_name": "Téléphones",
      "scraped_at": "2025-10-21T14:30:45.123456"
    },
    {
      "list_id": "2543876513",
      "url": "https://www.leboncoin.fr/ad/telephones/2543876513",
      "title": "iPhone 12 64GB Noir",
      "price": 450,
      "location": "Lyon 69001",
      "category_name": "Téléphones",
      "scraped_at": "2025-10-21T14:30:46.234567"
    }
  ]
}
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `list_id` | string | Unique ad identifier |
| `url` | string | Full URL to ad page |
| `title` | string | Ad title |
| `price` | integer | Price in euros (may be null) |
| `location` | string | Location with postal code |
| `category_name` | string | Product category |
| `scraped_at` | string | ISO 8601 timestamp |

### Metadata Fields

| Field | Description |
|-------|-------------|
| `query` | Search term used |
| `total_ads` | Number of ads scraped |
| `scraped_at` | When scraping completed |
| `scraper` | Tool name and version |
| `method` | Scraping method used |

### Statistics Fields

| Field | Description |
|-------|-------------|
| `total_with_price` | Ads with price information |
| `min_price` | Lowest price found |
| `max_price` | Highest price found |
| `avg_price` | Average price (rounded to 2 decimals) |
| `median_price` | Median price |

## 🎨 Output Formats

### 1. Pretty Format (Recommended)

**Characteristics**:
- ✅ Human-readable
- ✅ Indented with 2 spaces
- ✅ Easy to debug
- ✅ Good for version control
- ❌ Larger file size

**File size**: ~50-100 KB for 50 ads

**Example**:
```json
{
  "metadata": {
    "query": "audi",
    "total_ads": 20
  },
  "ads": [
    {
      "title": "Audi A3",
      "price": 15000
    }
  ]
}
```

### 2. Compact Format

**Characteristics**:
- ✅ Smallest file size
- ✅ Fast parsing
- ✅ Good for APIs
- ❌ Hard to read
- ❌ Difficult to debug

**File size**: ~30-60 KB for 50 ads (40% smaller)

**Example**:
```json
{"metadata":{"query":"audi","total_ads":20},"ads":[{"title":"Audi A3","price":15000}]}
```

## 💻 Programmatic Usage

### As a Module

```python
from scrape_json import JSONLeboncoinScraper

# Initialize
scraper = JSONLeboncoinScraper()
scraper.use_session = True  # Keep browser open

# Scrape
ads = scraper.scrape(query="laptop", limit=50)

# Save with pretty format
json_file = scraper.save_to_json(ads, query="laptop", output_format='pretty')
print(f"Saved to: {json_file}")

# Or compact format
json_file = scraper.save_to_json(ads, query="laptop", output_format='compact')
```

### Load and Process JSON

```python
import json

# Load JSON file
with open('exports/leboncoin-iphone-30ads-20251021_143052.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Access metadata
print(f"Query: {data['metadata']['query']}")
print(f"Total: {data['metadata']['total_ads']}")

# Access statistics
if 'statistics' in data:
    stats = data['statistics']
    print(f"Average price: €{stats['avg_price']}")

# Process ads
for ad in data['ads']:
    print(f"{ad['title']}: €{ad.get('price', 'N/A')}")
```

## 🔄 Integration Examples

### 1. Data Pipeline

```python
import json
import pandas as pd

# Load JSON
with open('exports/leboncoin-cars-100ads.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data['ads'])

# Process
df['price_k'] = df['price'] / 1000
df.to_csv('processed_data.csv', index=False)
```

### 2. API Integration

```python
import requests
import json

# Scrape data
scraper = JSONLeboncoinScraper()
ads = scraper.scrape("laptop", 50)

# Send to API
response = requests.post(
    'https://your-api.com/ads',
    json={'ads': ads},
    headers={'Content-Type': 'application/json'}
)
```

### 3. Database Import

```python
import json
import sqlite3

# Load JSON
with open('exports/leboncoin-phones-50ads.json', 'r') as f:
    data = json.load(f)

# Import to database
conn = sqlite3.connect('ads.db')
cursor = conn.cursor()

for ad in data['ads']:
    cursor.execute('''
        INSERT INTO ads (list_id, title, price, location)
        VALUES (?, ?, ?, ?)
    ''', (ad['list_id'], ad['title'], ad.get('price'), ad.get('location')))

conn.commit()
```

## 📈 Performance

### Speed
- **Same as scrape_scrapling.py**: ~18 seconds for 20 ads
- **Session mode**: Faster for multiple pages
- **One-shot mode**: Slower but more stealthy

### File Sizes (approximate)

| Ads | Pretty | Compact | Savings |
|-----|--------|---------|---------|
| 10 | 15 KB | 9 KB | 40% |
| 20 | 30 KB | 18 KB | 40% |
| 50 | 75 KB | 45 KB | 40% |
| 100 | 150 KB | 90 KB | 40% |

## ⚠️ Important Notes

### Same Limits as Scrapling
- **300 ads per session**: Maximum before blocking
- **100-150 ads recommended**: Stay safe
- **Wait between sessions**: 1-2 hours minimum

### JSON-Specific Considerations

1. **Encoding**: Always use UTF-8 for French characters
2. **Large Files**: Compact format for > 100 ads
3. **Parsing**: Use `json.load()` not `eval()`
4. **Null Values**: Some ads may have missing fields

## 🆚 When to Use JSON vs Excel

### Use JSON When:
- ✅ Building APIs or web services
- ✅ Creating data pipelines
- ✅ Need machine-readable format
- ✅ Integrating with other systems
- ✅ Version control friendly
- ✅ Processing with Python/JavaScript

### Use Excel (scrape_scrapling.py) When:
- ✅ Manual data analysis
- ✅ Sharing with non-technical users
- ✅ Using Excel formulas/pivots
- ✅ Creating reports
- ✅ Visual data exploration

## 🛠️ Advanced Options

### Custom JSON Processing

```python
import json

# Load and filter
with open('exports/leboncoin-cars-50ads.json', 'r') as f:
    data = json.load(f)

# Filter by price
affordable = [ad for ad in data['ads'] if ad.get('price', 0) < 10000]

# Save filtered data
with open('affordable_cars.json', 'w', encoding='utf-8') as f:
    json.dump({
        'metadata': data['metadata'],
        'ads': affordable
    }, f, ensure_ascii=False, indent=2)
```

### Merge Multiple JSON Files

```python
import json
import glob

all_ads = []
for filename in glob.glob('exports/leboncoin-*.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
        all_ads.extend(data['ads'])

# Save merged
with open('merged_ads.json', 'w', encoding='utf-8') as f:
    json.dump({
        'metadata': {
            'total_ads': len(all_ads),
            'merged_at': datetime.now().isoformat()
        },
        'ads': all_ads
    }, f, ensure_ascii=False, indent=2)
```

## 📝 Best Practices

### 1. File Naming
- ✅ Include query in filename
- ✅ Include ad count
- ✅ Include timestamp
- ✅ Use descriptive names

### 2. Format Selection
- Use **pretty** for development/debugging
- Use **compact** for production/APIs
- Use **pretty** for git repositories

### 3. Data Validation
```python
import json

def validate_json_output(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    assert 'metadata' in data
    assert 'ads' in data
    assert len(data['ads']) > 0
    
    for ad in data['ads']:
        assert 'list_id' in ad
        assert 'url' in ad
        assert 'title' in ad
```

## 🔍 Troubleshooting

### Issue: JSON decode error
**Solution**: Ensure UTF-8 encoding when reading
```python
with open('file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
```

### Issue: Large file size
**Solution**: Use compact format
```python
scraper.save_to_json(ads, query, output_format='compact')
```

### Issue: Missing fields
**Solution**: Check for null values
```python
price = ad.get('price', 0)  # Default to 0 if missing
```

---

**📋 JSON scraper is ready! Perfect for developers and data pipelines! 🚀**
