-- Leboncoin Web Scraping Database Schema
-- Created: 2025-10-15 14:52:43

CREATE TABLE IF NOT EXISTS ads (
    ad_id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_id INTEGER UNIQUE,
    title TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10,2),
    price_cents INTEGER,
    currency VARCHAR(3) DEFAULT 'EUR',
    category_id INTEGER,
    category_name VARCHAR(100),
    ad_type VARCHAR(20),
    status VARCHAR(20) DEFAULT 'active',
    first_publication_date DATETIME,
    index_date DATETIME,
    url TEXT,
    has_phone BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad_id INTEGER,
    country_id VARCHAR(2),
    region_id VARCHAR(10),
    region_name VARCHAR(100),
    department_id VARCHAR(10),
    department_name VARCHAR(100),
    city VARCHAR(100),
    city_label VARCHAR(200),
    zipcode VARCHAR(10),
    latitude DECIMAL(10,7),
    longitude DECIMAL(10,7),
    source VARCHAR(50),
    provider VARCHAR(50),
    FOREIGN KEY (ad_id) REFERENCES ads(ad_id)
);

CREATE TABLE IF NOT EXISTS sellers (
    seller_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad_id INTEGER,
    store_id VARCHAR(50),
    user_id VARCHAR(100),
    seller_type VARCHAR(20),
    name VARCHAR(100),
    no_salesmen BOOLEAN DEFAULT FALSE,
    activity_sector VARCHAR(100),
    rating_score DECIMAL(3,2),
    rating_count INTEGER,
    profile_picture_url TEXT,
    phone_number VARCHAR(20),
    FOREIGN KEY (ad_id) REFERENCES ads(ad_id)
);

CREATE TABLE IF NOT EXISTS images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad_id INTEGER,
    thumb_url TEXT,
    small_url TEXT,
    large_url TEXT,
    image_order INTEGER DEFAULT 0,
    FOREIGN KEY (ad_id) REFERENCES ads(ad_id)
);

CREATE TABLE IF NOT EXISTS attributes (
    attribute_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad_id INTEGER,
    key VARCHAR(100),
    value TEXT,
    key_label VARCHAR(200),
    value_label TEXT,
    is_generic BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (ad_id) REFERENCES ads(ad_id)
);

CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY,
    category_name VARCHAR(100),
    parent_category_id INTEGER,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS scraping_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scraping_session_id VARCHAR(50),
    url_scraped TEXT,
    ads_found INTEGER,
    ads_inserted INTEGER,
    ads_updated INTEGER,
    errors TEXT,
    scraping_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    execution_time_seconds DECIMAL(10,3)
);

