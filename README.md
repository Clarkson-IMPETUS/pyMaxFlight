# pyMaxFlight
Python module for interfacing with the MaxFlight Motion Client.

<https://pymaxflight.readthedocs.io/en/latest/>

## Updating Documentation

```bash
python3 -m handsdown -n pyMaxFlight --external `git config --get remote.origin.url` && python3 -m mkdocs build
```

Afterwards, serve to test locally:

```bash
serve site
```