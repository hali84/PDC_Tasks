from mpi4py import MPI
from random import uniform

# ===========================
# Weather Simulation Function
# ===========================
def weather_data_simulation(adjustment_factor):
    temperature = uniform(20, 40)   # °C
    humidity = uniform(30, 90)      # %
    wind_speed = uniform(5, 25)     # km/h
    pressure = uniform(950, 1050)   # hPa

    # Basic weather calculations
    heat_index = temperature + 0.33 * humidity - 0.7 * wind_speed - 4
    dew_point = temperature - ((100 - humidity) / 5)
    comfort_level = (100 - abs(temperature - 25)) + (humidity / 2) - (wind_speed / 3)

    # Use broadcasted variable to slightly modify total
    total = (heat_index + dew_point + comfort_level + pressure) + adjustment_factor
    return total


# ===========================
# MPI Setup and Broadcasting
# ===========================
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Rank 0 process defines the variable to broadcast
if rank == 0:
    variable_to_share = 100   # could be an adjustment factor for weather
else:
    variable_to_share = None

# Broadcast the variable to all processes
variable_to_share = comm.bcast(variable_to_share, root=0)

# Each process runs its weather simulation
weather_total = weather_data_simulation(variable_to_share)

# Print results per process
print(f"Process {rank}: variable shared = {variable_to_share}, weather total = {weather_total:.2f}")
