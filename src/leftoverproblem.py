"""
Copyright 2022 Glaucia Maria Bressan, Esdras Battosti da Silva,
Matheus Henrique Pimenta-Zanon, Elisângela Aparecida da Silva Lizzi

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import random as rnd

import numpy as np


def generate_dataset(
    n_itens,
    n_obj,
    l_types,
    L_types,
    d_types,
    l_min=20,
    l_max=444,
    L_min=600,
    L_max=1188,
    d_min=0,
    d_max=15,
):

    objs_length = np.linspace(L_min, L_max, L_types + 1)
    itens_length = np.linspace(l_min, l_max, l_types + 1)
    itens_demand = np.linspace(d_min, d_max, d_types + 1)

    iten_middle = [(itens_length[i] + itens_length[i + 1]) / 2 for i in range(l_types)]
    iten_sigma = (itens_length[1] - itens_length[0]) / 4

    obj_middle = [(objs_length[i] + objs_length[i + 1]) / 2 for i in range(L_types)]
    obj_sigma = (objs_length[1] - objs_length[0]) / 4

    iten_demand_middle = [
        (itens_demand[i] + itens_demand[i + 1]) / 2 for i in range(d_types)
    ]
    iten_demand_sigma = (itens_demand[1] - itens_demand[0]) / 4

    objs = create_objs(obj_middle, obj_sigma, n_obj, L_min, L_max, L_types)
    itens = create_itens(iten_middle, iten_sigma, n_itens, n_obj, l_min, l_max, l_types)
    demands = create_demands(
        iten_demand_middle, iten_demand_sigma, n_itens, n_obj, d_min, d_max, d_types
    )

    shuffle(objs, itens, demands)

    return objs, itens, demands


def create_objs(obj_middle, obj_sigma, n_obj, L_min, L_max, L_types):
    n = 0
    objs = []

    for i in range(n_obj):
        while True:
            L_ran = rnd.gauss(obj_middle[n], obj_sigma)

            if L_min <= L_ran <= L_max:
                n += 1
                if n >= L_types:
                    n = 0

                objs.append(L_ran)
                break
    return objs


def create_itens(iten_middle, iten_sigma, n_itens, n_obj, l_min, l_max, l_types):
    itens = []

    for i in range(n_obj):
        n = 0
        itens_vec = []

        for j in range(n_itens):
            while True:
                l_ran = rnd.gauss(iten_middle[n], iten_sigma)

                if l_min <= l_ran <= l_max:
                    n += 1
                    if n >= l_types:
                        n = 0

                    itens_vec.append(l_ran)
                    break
        itens.append(itens_vec)
    return itens


def create_demands(
    iten_demand_middle, iten_demand_sigma, n_itens, n_obj, d_min, d_max, d_types
):
    demands = []

    for i in range(n_obj):
        n = 0
        demands_vec = []

        for j in range(n_itens):
            while True:

                d_ran = round(rnd.gauss(iten_demand_middle[n], iten_demand_sigma))

                if d_min <= d_ran <= d_max:
                    n += 1
                    if n >= d_types:
                        n = 0

                    demands_vec.append(d_ran)
                    break
        demands.append(demands_vec)
    return demands


def shuffle(objs, itens, demands):
    rnd.shuffle(objs)
    rnd.shuffle(itens)
    rnd.shuffle(demands)


def save_dataset(objs, itens, demands, PATH):
    if not os.path.exists(PATH):
        os.mkdir(PATH)

    np.save(os.path.join(PATH, "objs.npy"), objs)
    np.save(os.path.join(PATH, "itens.npy"), itens)
    np.save(os.path.join(PATH, "demands.npy"), demands)


if __name__ == "__main__":
    DATASET_PATH = os.path.realpath("dataset")
    save = False

    objs, itens, demands = generate_dataset(
        n_itens=10, n_obj=20, l_types=5, L_types=3, d_types=2
    )

    if save:
        save_dataset(objs, itens, demands, DATASET_PATH)
