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
# MPI Hello World + Simulation
# ===========================
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Each process prints its Hello World message
print(f"Hello world from process {rank} of {size}")

# Each process performs its own weather simulation
weather_total = weather_data_simulation()

# Display result for each process
print(f"Process {rank}: simulated weather total = {weather_total:.2f}")
