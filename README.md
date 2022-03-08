# FoodSecurity

> An analysis of food security in Kenya


## Introduction

```bash
mercury runserver --runworker
```


## Development

Running the analysis requires the following dependencies:

Docker:
```bash
docker run -p 8888:8888 -v $(pwd):/home/joyvan/work jupyter/scipy-notebook

```

Above command will run the analysis in a docker container.

## Documentation:

https://towardsdatascience.com/how-to-run-jupyter-notebook-on-docker-7c9748ed209f

https://simplernerd.com/docker-jupyter-notebook/

## Local Development

Requirements file
```
Fiona @ git+https://github.com/Toblerity/Fiona.git@d36e0c897c545e0e51fe759e540c85c117bf3fc1
```

> still in development