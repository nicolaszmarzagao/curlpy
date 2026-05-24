# cURLpy

A simple `curl` implementation built from scratch using Python 3.

The goal of this project is to use as few dependencies as possible — preferably none.

**Current status:** This project currently has no dependencies.

## Installation

Install from PyPI:

```bash
pip install curlpy-nicolaszmarzagao
```

## Usage

cURLpy works similarly to `curl`. Here are some features already implemented:

### GET Requests

#### HTTP

```bash
python3 -m curlpy example.com
```

#### HTTPS

```bash
python3 -m curlpy https://example.com
```

#### Specific path

```bash
python3 -m curlpy https://example.com/hello/world
```

#### Specific port

```bash
python3 -m curlpy https://example.com:8080
```

Or:

```bash
python3 -m curlpy https://example.com/ -p 8080
```

#### Include HTTP headers

```bash
python3 -m curlpy example.com -i
```

### POST Requests

Use the `-d` / `--data` flag to send data in the request body. This automatically makes it a POST request.

#### Form data

```bash
python3 -m curlpy example.com/api -d "name=john&age=30"
```

#### JSON

```bash
python3 -m curlpy example.com/api -d '{"name": "john"}' -H "Content-Type: application/json"
```

#### Override the method

`-d` defaults to POST, but you can override it with `-X`:

```bash
python3 -m curlpy example.com/api -d '{"name": "john"}' -X PUT
```

## Local Development

Clone the repository using SSH:

```bash
git clone git@github.com:nicolaszmarzagao/curlpy.git
cd curlpy
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install cURLpy locally in editable mode:

```bash
python3 -m pip install -e .
```

Run the tests:

```bash
python3 -m unittest discover -s tests -v
```

Run cURLpy:

```bash
python3 -m curlpy
```

## Contributing

Feel free to fork this repository, open issues, suggest features, or contribute with pull requests.

This project is licensed under the MIT License.
