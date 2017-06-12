# afa-core
Generates lists of core/non-core sites from a multi-FASTA alignment for ClonalFrameML

## Author

Jason Kwong (@kwongjc)

## Dependencies
* Python 3.x
* BioPython

## Usage

```
$ afa-core.py -h
usage: 
  afa-core.py [--pre cfml] FASTA

Generates lists of core/non-core sites from a multi-FASTA alignment for ClonalFrameML

positional arguments:
  FASTA         multi-FASTA alignment file

optional arguments:
  -h, --help    show this help message and exit
  --pre PREFIX  specify output prefix for files (default="cfml")
  --version     show program's version number and exit
```

## Bugs

Please submit via the [GitHub issues page](https://github.com/kwongj/afa-core/issues).  

## Software Licence

[GPLv3](https://github.com/kwongj/afa-core/blob/master/LICENSE)
