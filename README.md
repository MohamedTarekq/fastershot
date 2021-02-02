# fastershot
- fastershot is a fast tool to take a screenshot from list of urls .
### Setup:
```
pip3 install -r requirement.txt
```

### Usage:
```
python3 fastershot.py -h
usage: fastershot.py [-h] [-l L] [-n N]

faster tool to take a screenshot to list of urls

optional arguments:
  -h, --help  show this help message and exit
  -l L        List of urls
  -n N        Number of requests per seconde default is 15
```
### Examples:
```
python3 fastershot.py -l urls.txt
python3 fastershot.py -l urls.txt -n 30
```
