# Usage

## Create virtual environment

1. Change the `PROJECT_NAME` of the Makefile
2. Execute following command

```
$ make poetry-new
```

3. Edit `PROJECT_NAME/pyproject.toml`

## Add dependencies

```
$ make poetry-add
```

## If `The container name "/poetry" is already in use by container "xxxx". ...`, then remove the container.

```
$ make rm-poetry
```
