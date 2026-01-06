from mpi4py import MPI
import numpy as np
from random import uniform

# ===========================
# Weather Simulation Function
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
# MPI Reduce Example
# ===========================
comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

array_size = 10
recvdata = np.zeros(array_size, dtype=np.int_)
senddata = (rank + 1) * np.arange(array_size, dtype=np.int_)

print(f"Process {rank} sending data: {senddata}")

# Perform reduction (sum) of all process data at root process
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)

if rank == 0:
    print(f"\nAfter MPI Reduce operation on root process {rank}:")
    print("Reduced data:", recvdata)

    # Run the weather simulation only on root process
    weather_result = weather_data_simulation()
    print(f"\nWeather Simulation Result: {weather_result:.2f}")
