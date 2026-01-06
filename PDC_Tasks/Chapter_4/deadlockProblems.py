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
# MPI Setup and Communication
# ===========================
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(f"My rank is {rank}")

# Har process apna weather simulate karega
weather_total = weather_data_simulation()
print(f"Process {rank}: simulated weather total = {weather_total:.2f}")

# Only rank 1 and rank 5 exchange messages
if rank == 1:
    data_send = f"Weather data from rank 1 = {weather_total:.2f}"
    destination_process = 5
    source_process = 5

    # Receive first from rank 5, then send
    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)

    print(f"Process {rank} sending data: {data_send} to process {destination_process}")
    print(f"Process {rank} received data: {data_received}")

elif rank == 5:
    data_send = f"Weather data from rank 5 = {weather_total:.2f}"
    destination_process = 1
    source_process = 1

    # Send first to rank 1, then receive
    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=source_process)

    print(f"Process {rank} sending data: {data_send} to process {destination_process}")
    print(f"Process {rank} received data: {data_received}")
