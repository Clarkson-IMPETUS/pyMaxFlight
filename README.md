# pyMaxFlight
Python module for interfacing with the MaxFlight Motion Client.

<https://pymaxflight.readthedocs.io/en/latest/>

## Updating Documentation

```bash
rm -R docs && rm -R site && python3 -m handsdown --external `git config --get remote.origin.url` --create-configs --exclude src/pyMaxFlight/Interface/__init__.py --cleanup && python3 -m mkdocs build
```

Afterwards, serve to test locally:

```bash
serve site
```