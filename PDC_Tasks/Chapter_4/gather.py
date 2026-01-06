from mpi4py import MPI
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
# MPI Setup and Gather
# ===========================
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Each process simulates weather
weather_total = weather_data_simulation()

# Gather all results at the root process (rank 0)
all_data = comm.gather(weather_total, root=0)

# Print info per process
print(f"Process {rank}: simulated weather total = {weather_total:.2f}")

# Root process displays all gathered data
if rank == 0:
    print(f"\nRank {rank} receiving data from all other processes...\n")
    for i in range(size):
        print(f" Process {rank} received weather total = {all_data[i]:.2f} from process {i}")
