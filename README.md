# Instap Python API

## Installation

### Python 3.7

With dataclasses backport:

`pip install git+https://github.com/instap-app/python-api`

### Python 3.6

Without dataclasses backport:

`pip install git+https://github.com/instap-app/python-api@python-3.6`

## Usage

```python
from instapi.api import InstapAPI

api = InstapAPI("http://app.domain.com", "JWT_TOKEN")
```
