import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate


def separate_even_columns(data_frame):
    return data_frame.iloc[:, [i for i in range(len(data_frame.columns)) if i % 2 == 1]]


def separate_odd_columns(data_frame):
    return data_frame.iloc[:, [i for i in range(len(data_frame.columns)) if i % 2 == 0]]


def is_valid_file(file_path):
    return True if file_path != "" and os.path.exists(file_path) else False


def ask_file_path(measurement_name):
    return input(f"Insira o caminho do arquivo do {measurement_name} ramptime \n")


def message_invalid_path():
    return print("Arquivo inválido ou inexistente \n")


def ask_file_name():
    return input("Insira o nome do arquivo para salvar \n")


def ask_x_axis():
    return input('Insira o cabeçalho do eixo x a ser considerado para o plote \n')


def ask_y_axis():
    return input('Insira o cabeçalho do eixo y a ser considerado para o plote \n')


def is_bigger_data_frame(data_frame_1, data_frame_2):
    return len(data_frame_1) < len(data_frame_2)


def slice_data_frame_rows(data_frame_1, data_frame_2):
    return data_frame_1.loc[0:len(data_frame_2)-1, :]


def sanitize_data_frames():
    global even_columns_subtracted, time_photo_celiv_ramp_time
    if is_bigger_data_frame(even_columns_subtracted, time_photo_celiv_ramp_time):
        time_photo_celiv_ramp_time = slice_data_frame_rows(time_photo_celiv_ramp_time, even_columns_subtracted)
        return
    even_columns_subtracted = slice_data_frame_rows(even_columns_subtracted, time_photo_celiv_ramp_time)


def integrate_current_over_time():
    global data_ramp_time_transposed_in_arrays
    i = 1
    integrated_values = []
    while i <= len(data_ramp_time_transposed_in_arrays) - 1:
        integrated_values.append(integrate.simps(data_ramp_time_transposed_in_arrays[i],
                                                 data_ramp_time_transposed_in_arrays[i - 1],
                                                 axis=-1, even='avg'))
        i = i + 2
    return integrated_values

# path_dark = ask_file_path("dark-CELIV")
#
# while not is_valid_file(path_dark):
#     message_invalid_path()
#     path_dark = ask_file_path("dark-CELIV")
#
current_dark_celiv_ramp_time = separate_even_columns(
    pd.read_table("C:/Users/robee/Desktop/2-dark-celiv-current-celiv-only-alterado.txt", sep='\t', header=None)).abs()

# path_photo = ask_file_path("photo_celiv")

# while not is_valid_file(path_photo):
#     message_invalid_path()
#     path_photo = ask_file_path("photo-celiv")

current_photo_celiv_ramp_time = (separate_even_columns(
    pd.read_table("C:/Users/robee/Desktop/3-photo-celiv-basic-current-celiv-only-alterado.txt", sep='\t',
                  header=None))).abs()

time_photo_celiv_ramp_time = separate_odd_columns(
    pd.read_table("C:/Users/robee/Desktop/3-photo-celiv-basic-current-celiv-only-alterado.txt", sep='\t', header=None))

even_columns_subtracted = current_photo_celiv_ramp_time.\
    subtract(current_dark_celiv_ramp_time).dropna()

sanitize_data_frames()

data_ramp_time = pd.concat([time_photo_celiv_ramp_time, even_columns_subtracted],
                           axis=1).sort_index(axis=1)

# data_ramp_time.to_csv(ask_file_name(), sep='\t') #line commented to run tests

data_ramp_time_transposed_in_arrays = data_ramp_time.transpose().to_numpy()

integration_results = integrate_current_over_time()

print(integration_results)
