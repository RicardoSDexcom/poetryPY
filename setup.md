# Setup for Mac Os

## Installing Poetry
https://formulae.brew.sh/formula/poetry

https://python-poetry.org/docs/

```
brew install poetry
```
or you can install poetry using pip

```
pip3 install poetry
```

```
poetry -V
```

## Create a new project using Poetry
https://python-poetry.org/docs/cli/
```
mkdir poetry_demo

poetry new hello_project

ls

```

## add dependency using poetry
```
poetry add requests

poetry add --group dev requests numpy

```

## Run script using poetry
```
poetry run python  hello_project/__init__.py
```

