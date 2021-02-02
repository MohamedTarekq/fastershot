# fastershot
- fastershot is a fast tool to take a screenshot from list of urls .

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
```
python3 fastershot.py -l urls.txt
python3 fastershot.py -l urls.txt -n 30
```
