# Usage

1. Create virtual environment beforehand using `docker-python/`
2. Set the environment variable
    - `PROJECT_NAME`: Project name used in virtual environment
3. Build and Run the Docker

```sh
$ make build
$ make run
```

4. Activate venv

```sh
$ docker exec -it [PROJECT_NAME] bash
% source .venv/bin/activate
```