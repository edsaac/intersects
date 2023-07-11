import numpy as np
import matplotlib.pyplot as plt

def set_initial_condition(solution_array:np.array, interior_temperature:float):
    solution_array = interior_temperature

def set_boundary_conditions(solution_array:np.array, temp_outside:float, temp_inside:float):
    solution_array[0] = temp_outside
    solution_array[-1] = temp_inside

def create_mesh(nsize:int):
    return np.zeros(nsize)

def integrator(solution_array:np.array, diffusivity:float):
    r = diffusivity
    next_array = np.copy(solution_array)
    for i in range(1,len(solution_array) - 1):
        next_array[i] = r*solution_array[i+1] + (1-2*r)*solution_array[i] + r*solution_array[i-1]
    return next_array

def main():
    NSIZE = 10
    mesh = create_mesh(NSIZE)
    print(mesh)
    set_initial_condition(mesh, 75)
    
    set_boundary_conditions(mesh, -40, 75)
    print(mesh)

    fig, ax = plt.subplots()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.plot(mesh)
    plt.show()

    mesh = integrator(mesh, 1)
    print(mesh)

if __name__ == "__main__":
    main()
