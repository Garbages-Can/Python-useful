<small>update.py</small>
```python
#!/usr/bin/env python3
from pip._internal import get_installed_distributions
from subprocess import call

for dist in get_installed_distributions():
    call('pip3 install --upgrade ' + dist.project_name, shell=True)
```

通过pip,更新电脑上全部的依赖库.

使用方法：

> python3 update.py

or

> ./update.py
