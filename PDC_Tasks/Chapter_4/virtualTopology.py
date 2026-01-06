from mpi4py import MPI
import numpy as np
from random import uniform

# =========================================
# Weather Simulation Function
# =========================================
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


# =========================================
# MPI Cartesian Grid Topology
# =========================================
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0, 0, 0, 0]

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    # Compute grid dimensions
    grid_row = int(np.floor(np.sqrt(size)))
    grid_column = size // grid_row

    if grid_row * grid_column > size:
        grid_column -= 1
    if grid_row * grid_column > size:
        grid_row -= 1

    if rank == 0:
        print(f"Building a {grid_row} x {grid_column} grid topology:\n")

    # Create Cartesian communicator
    cartesian_communicator = comm.Create_cart(
        (grid_row, grid_column),
        periods=(True, True),
        reorder=True
    )

    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.rank)

    # Determine neighboring processes
    neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)

    # Display topology info
    print(f"Process = {rank} | Row = {my_mpi_row} | Column = {my_mpi_col}\n"
          f"---->\nUP = {neighbour_processes[UP]}\n"
          f"DOWN = {neighbour_processes[DOWN]}\n"
          f"LEFT = {neighbour_processes[LEFT]}\n"
          f"RIGHT = {neighbour_processes[RIGHT]}\n")

    # Each process performs a weather simulation
    weather_value = weather_data_simulation()
    print(f"Process {rank} Weather Simulation Result: {weather_value:.2f}\n")
