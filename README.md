# FoodKenya

> An analysis of food security in Kenya in areas whose effects would be felt across the country


![FoodSecurity](./preview/foodsecurity.mp4)

## Development setup

## Bare metal

```bash
bash develop.sh
```


## Docker setup
Running the analysis requires the following dependencies:


```bash
docker run -p 8888:8888 -v $(pwd):/home/joyvan/work jupyter/scipy-notebook

```