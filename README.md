
# Flowtune SDK (v1.2.0)

Flowtune is a quantum-inspired DSL and SDK for optimizing how resources are loaded based on priority, size, and scale.

## 🚀 Features
- Automatic configuration using `auto_config` blocks
- Resource loading with priority and scale (micro/macro)
- Python and JavaScript SDKs supported
- Great for web, app, and performance-focused projects

## 🐍 Python Usage

```bash
pip install flowtune
```

```python
from flowtune.parser import QuantumFlowtuneParser
from flowtune.executor import QuantumFlowtuneExecutor

parser = QuantumFlowtuneParser('example.ft')
parser.parse(auto_config=True)

executor = QuantumFlowtuneExecutor(parser.resources, parser.groups, parser.execution_plan)
executor.run()
```

## 📦 JavaScript Usage

```bash
npm install flowtune-js
```

```js
import FlowtuneJS from 'flowtune-js';

fetch('example.ft.json')
  .then(res => res.json())
  .then(data => {
    const flowtune = new FlowtuneJS(data, {
      autoConfig: {
        security: 'strict',
        optimization: 'speed'
      }
    });
    flowtune.run();
  });
```

## 📄 License

MIT © 2025 zaminnes
