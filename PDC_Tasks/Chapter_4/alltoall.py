from mpi4py import MPI
import numpy as np
from random import uniform

# ===========================
# Weather Data Simulation Function
# ===========================
def weather_data_simulation():
    temperature = uniform(20, 40)   # °C
    humidity = uniform(30, 90)      # %
    wind_speed = uniform(5, 25)     # km/h
    pressure = uniform(950, 1050)   # hPa

    # Basic weather calculations
    heat_index = temperature + 0.33 * humidity - 0.7 * wind_speed - 4
    dew_point = temperature - ((100 - humidity) / 5)
    comfort_level = (100 - abs(temperature - 25)) + (humidity / 2) - (wind_speed / 3)

    total = heat_index + dew_point + comfort_level + pressure
    return total


# ===========================
# MPI Setup
# ===========================
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Each process runs its own weather simulation
weather_value = weather_data_simulation()

# Prepare data for communication
senddata = np.array([(rank + 1) * (i + int(weather_value) % 10) for i in range(size)], dtype=int)
recvdata = np.empty(size, dtype=int)

# Perform All-to-All communication
comm.Alltoall(senddata, recvdata)

# Display process results
print(f"Process {rank}: Weather Total = {weather_value:.2f}")
print(f"Process {rank} sending {senddata} receiving {recvdata}\n")
