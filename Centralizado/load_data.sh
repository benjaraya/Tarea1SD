#!/bin/bash

# Lee el archivo línea por línea
while IFS=, read -r key value; do
    # Inserta la clave y el valor en Redis
    redis-cli SET "$key" "$value"
done < dataset.csv
