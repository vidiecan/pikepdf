from __future__ import annotations

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore

with open('pyproject.toml', 'rb') as f:
    t = tomllib.load(f)
env = t['tool']['cibuildwheel']['environment']
print('\n'.join(f'{k}={v}' for k, v in env.items()))
