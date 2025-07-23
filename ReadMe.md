#  Sinking Yacht Adguard List converter API.

This is a small API which takes the phishing URL links from
the Sinking Yacht Site and converts them into a format
which Adguard can use.

# SOURCES
[The Sinking Yacht](https://sinking.yachts/docs/)

[Sinking Yacht Github](https://github.com/SinkingYachts)

# Usage
# ENVS

`VERSION` The App Version

`BASE_URL` the base URL of the Sinking Yacht. (https://phish.sinking.yachts/v2/all)

## CLI
To run this API in your cli use the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 5000
```

Remember to also set your ENVS!
## DOCKER
```bash
docker run -d \
    --name sinking-yacht-adguard-converter \
    -p 5000:5000 \
    -e VERSION=1.0.0 \
    -e BASE_URL=https://phish.sinking.yachts/v2/all \
    ghcr.io/wolfswolke/sinking-yacht-api:latest
```