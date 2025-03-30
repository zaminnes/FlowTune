
# Flowtune Simplified

Flowtune simplified edition with an automatic resource loading tracking algorithm.

## What's New in v1.1.0

- Automatic tracking and avoiding repeated loading of the same resources.
- Simplified and cleaner executor structure.
- Enhanced security by ensuring no redundant loads.

## Installation

```bash
pip install flowtune
```

## Usage

```python
from flowtune.executor import SimpleFlowtuneExecutor

resources = {
    'logo': {'url': 'https://cdn.example.com/logo.png', 'priority': 1},
    'video': {'url': 'https://cdn.example.com/intro.mp4', 'priority': 2},
}

executor = SimpleFlowtuneExecutor(resources)
executor.run()
```

## License

MIT
