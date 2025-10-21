#!/usr/bin/env python3
"""
Setup script for Leboncoin Scraper
"""

import os
import sys
import subprocess
import sqlite3

def install_requirements():
    """Install Python requirements"""
    print("📦 Installing Python requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def setup_environment():
    """Setup environment configuration"""
    print("⚙️ Setting up environment...")

    if not os.path.exists('.env'):
        import shutil
        shutil.copy('.env.template', '.env')
        print("✓ Environment file created from template")
        print("ℹ️ Please edit .env file to configure your settings")
    else:
        print("ℹ️ Environment file already exists")

    return True

def create_directories():
    """Create necessary directories"""
    print("📁 Creating directories...")

    directories = ['exports', 'logs', 'data']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    print("✓ Directories created")
    return True

def test_database():
    """Test database setup"""
    print("🗄️ Testing database setup...")

    try:
        from leboncoin_scraper import LeboncoinScraper

        # Initialize scraper (this will create the database)
        scraper = LeboncoinScraper(database_path="test_setup.db")

        # Test database connection
        conn = sqlite3.connect("test_setup.db")
        cursor = conn.cursor()

        # Check if tables were created
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        expected_tables = {'ads', 'locations', 'sellers', 'images', 'attributes', 'categories', 'scraping_logs'}
        found_tables = {table[0] for table in tables}

        if expected_tables.issubset(found_tables):
            print("✓ Database schema created successfully")
            print(f"✓ Created tables: {', '.join(found_tables)}")
        else:
            print("⚠️ Some tables missing from database schema")
            missing = expected_tables - found_tables
            print(f"Missing tables: {', '.join(missing)}")

        conn.close()

        # Clean up test database
        os.remove("test_setup.db")

        return True

    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Leboncoin Scraper Setup")
    print("=" * 30)

    steps = [
        ("Install Requirements", install_requirements),
        ("Setup Environment", setup_environment),
        ("Create Directories", create_directories), 
        ("Test Database", test_database)
    ]

    success_count = 0

    for step_name, step_function in steps:
        print(f"\n{step_name}...")
        if step_function():
            success_count += 1
        else:
            print(f"❌ {step_name} failed")

    print("\n" + "=" * 30)
    print(f"Setup completed: {success_count}/{len(steps)} steps successful")

    if success_count == len(steps):
        print("\n🎉 Setup completed successfully!")
        print("\nNext steps:")
        print("1. Edit .env file with your configuration")
        print("2. Run examples/basic_scraping.py to test")
        print("3. Check README.md for detailed usage instructions")
    else:
        print("\n⚠️ Setup completed with some issues")
        print("Please check error messages above and resolve issues")

    return success_count == len(steps)

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⏹️ Setup interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Setup failed with error: {e}")
        sys.exit(1)
