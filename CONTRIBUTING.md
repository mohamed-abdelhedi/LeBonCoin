# Contributing to Leboncoin Scraper

First off, thank you for considering contributing to this project! 🎉

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Submitting Changes](#submitting-changes)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code.

### Our Standards

- ✅ Be respectful and inclusive
- ✅ Welcome newcomers and help them learn
- ✅ Focus on what is best for the community
- ✅ Show empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Python version and OS**
- **Error messages and logs**

### Suggesting Enhancements

Enhancement suggestions are welcome! Include:

- **Clear use case**
- **Why this would be useful**
- **Possible implementation approach**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. Add tests if applicable
3. Ensure tests pass
4. Update documentation
5. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.8+
- Git
- Virtual environment tool

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/LeBonCoin.git
cd LeBonCoin

# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install dev dependencies
pip install pytest black flake8 mypy
```

## Coding Guidelines

### Python Style

- Follow [PEP 8](https://pep8.org/)
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use meaningful variable names

### Documentation

- Add docstrings to all functions
- Use Google-style docstrings
- Update README if adding features
- Comment complex logic

### Example Docstring

```python
def scrape(self, query, limit=20):
    """
    Scrape leboncoin ads for given query.
    
    Args:
        query (str): Search term
        limit (int): Maximum number of ads to scrape
        
    Returns:
        list: List of ad dictionaries
        
    Raises:
        ValueError: If query is empty
        ConnectionError: If network fails
    """
    pass
```

### Testing

- Write tests for new features
- Ensure existing tests pass
- Aim for > 80% code coverage

```bash
# Run tests
python -m pytest tests/

# With coverage
python -m pytest --cov=src tests/
```

### Code Formatting

```bash
# Format code
black .

# Check linting
flake8 .

# Type checking
mypy src/
```

## Submitting Changes

### Commit Messages

Use clear, descriptive commit messages:

```
feat: Add JSON export functionality
fix: Handle Unicode characters in price parsing
docs: Update README with JSON scraper info
refactor: Simplify proxy rotation logic
test: Add tests for JSON export
```

Prefixes:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Tests
- `chore`: Maintenance

### Pull Request Process

1. **Update documentation**
2. **Add tests** for new features
3. **Ensure all tests pass**
4. **Update CHANGELOG.md**
5. **Request review** from maintainers

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe testing performed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed code
- [ ] Commented complex code
- [ ] Updated documentation
- [ ] Added tests
- [ ] All tests pass
```

## Project Structure

```
LeBonCoin/
├── src/              # Source code
│   ├── database/     # Database handlers
│   ├── scrapers/     # Scraper implementations
│   └── utils/        # Utilities
├── tests/            # Test files
├── docs/             # Documentation
├── config/           # Configuration
├── scripts/          # Helper scripts
└── examples/         # Usage examples
```

## Areas for Contribution

### High Priority

- [ ] Add support for more search filters
- [ ] Implement category-specific scrapers
- [ ] Add image download functionality
- [ ] Create detailed seller information extraction

### Medium Priority

- [ ] Add PostgreSQL database support
- [ ] Implement scheduling/cron job support
- [ ] Add email notification system
- [ ] Create web dashboard

### Documentation

- [ ] Add more usage examples
- [ ] Create video tutorials
- [ ] Translate documentation to French
- [ ] Add FAQ section

## Questions?

Feel free to:
- Open an issue
- Start a discussion
- Reach out to maintainers

Thank you for contributing! 🚀
