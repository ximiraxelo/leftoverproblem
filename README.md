# Leftover Problem Dataset Generator

This **dataset generator** from the **leftover problem** is based in the work: 

> Classification of leftovers from the stock cutting process, G. M. Bressan *et al.*, 2022

See the full article in [LINK]

This project is licensed under the [Apache-2.0 License](https://www.apache.org/licenses/LICENSE-2.0)

## Dependencies

This project is build with the Python 3.10.2

You need to have installed the [NumPy package](https://numpy.org/doc/stable/index.html). if you already have Python, you can install NumPy with:

```conda install numpy``` or ```pip install numpy```

## Usage

### Generating a dataset

To generate a dataset call the function `generate_dataset()`

```
objs, itens, demands = generate_dataset(n_itens, n_obj, l_types, L_types, d_types, l_min, l_max, L_min, L_max, d_min, d_max)
```

Inputs:

* `n_itens`: the number of the itens per object
* `n_obj`: the number of objects
* `l_types`: the amount of types of sizes of the itens
* `L_tpyes`: the amount of types of sizes of the objects
* `d_types`: the amount of types of the itens demands
* `l_min` and `l_max`: the minimum and maximum size of the itens
* `L_min` and `L_min`: the minimum and maximum size of the objects
* `d_min` and `d_max`: the minimum and maximum of the itens demands

Outputs:

* `objs`: a list with `n_objs` length that contains the objects sizes
* `itens`: a list with the shape (`n_obs, n_itens`) that contains the itens sizes
* `demands`: a list with the shape (`n_obs, n_itens`) that contains the itens demands

### Saving the dataset

The generated dataset can be saved in `.npy` files.

See more about `.npy` files in the [NumPy documentation](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format)

To save a generated dataset call the function `save_dataset()`

```
save_dataset(objs, itens, demands, DATASET_PATH)
```

Inputs:

* `objs, itens, demands`: the generated data from the `generate_dataset()` function
* `DATASET_PATH`: the absolute path to save the `.npy` files