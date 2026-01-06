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
# MPI Setup + Communication
# ===========================
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(f"My rank is: {rank}")

# Har process apna weather simulate karega
weather_total = weather_data_simulation()
print(f"Process {rank}: simulated weather total = {weather_total:.2f}")

# Communication logic
if rank == 0:
    data = int(weather_total)  # sending simulated data instead of static number
    destination_process = 4
    comm.send(data, dest=destination_process)
    print(f"Process {rank}: sending data {data} to process {destination_process}")

elif rank == 1:
    destination_process = 8
    data = f"Weather hello from rank {rank} (value={weather_total:.2f})"
    comm.send(data, dest=destination_process)
    print(f"Process {rank}: sending data '{data}' to process {destination_process}")

elif rank == 4:
    data = comm.recv(source=0)
    print(f"Process {rank}: received data = {data} from process 0")

elif rank == 8:
    data1 = comm.recv(source=1)
    print(f"Process {rank}: received data1 = {data1} from process 1")
