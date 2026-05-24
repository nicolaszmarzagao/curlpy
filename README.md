# cURLpy
A curl implementation from scratch using Python3.

The **goal** of this project is to use as few dependencies as possible (PREFERABLY NONE!)

**Current Status:** This project currently has no dependencies.

### Install using pip
```bash
pip install curlpy-nicolaszmarzagao
```

### Usage
curlpy works the same way as curl does, here are some features already implemented:

### GET Requests 

- To ```HTTP```
```bash
python3 -m curlpy example.com
```

- To ```HTTPS```
```bash
python3 -m curlpy https://example.com
```

- To specific ```path```
```bash
python3 -m curlpy https://example.com/hello/world
```

- To specific ```port```
```bash
python3 -m curlpy https://example.com:8080
```
or
```bash
python3 -m curlpy https://example.com/ -p 8080
```

- Include ```HTTP header```
```bash
python3 -m curlpy example.com -i
```

### Local Package
```bash
# Clone the repository using ssh
git clone git@github.com:nicolaszmarzagao/curlpy.git
cd curlpy

# Activate the python3 virtual enviroument then install cURLpy locally
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
```
And that's it!
```bash
# use this command to test curlpy
python3 -m unittest
# and this one to run
python3 -m curlpy
```

### Contributing
Feel free to fork and repository as this project is under the MIT License.
You can also contribute to any issues, report issues or suggest features.
