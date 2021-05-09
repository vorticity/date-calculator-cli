# date-calculator-cli
Simple command line interface to the [date-calculator](https://github.com/vorticity/date-calculator) library.

## Installation
Clone this repository, navigate to the repository root and run:
```bash
poetry install
```

## Usage
Navigate to the repository root and run:
```bash
poetry shell
```
Then you can run the cli from a poetry shell like so:
```bash
date-calculator-cli <DD/MM/YYYY> <DD/MM/YYYY>
```

## Examples
```bash
date-calculator-cli 02/06/1983 22/06/1983   
19
date-calculator-cli 04/07/1984 25/12/1984
173
date-calculator-cli 03/01/1989 03/08/1983
1979
```

## References

* https://click.palletsprojects.com/en/7.x/
* https://www.pluralsight.com/tech-blog/python-cli-utilities-with-poetry-and-typer/
* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code
