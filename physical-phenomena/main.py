import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

# 1. Projectile motion
def projectile_motion():
    t = np.linspace(0, 10, 1000)
    v0 = 50
    theta = np.pi/4
    g = 9.8
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_title('Projectile motion')
    plt.show()

# 2. Simple harmonic motion
def simple_harmonic_motion():
    t = np.linspace(0, 10, 1000)
    A = 1
    omega = 2*np.pi
    phi = 0
    x = A * np.cos(omega * t + phi)
    fig, ax = plt.subplots()
    ax.plot(t, x)
    ax.set_xlabel('t (s)')
    ax.set_ylabel('x (m)')
    ax.set_title('Simple harmonic motion')
    plt.show()

# 3. Diffraction pattern
def diffraction_pattern():
    x = np.linspace(-10, 10, 1000)
    y = np.linspace(-10, 10, 1000)
    X, Y = np.meshgrid(x, y)
    wavelength = 1
    k = 2*np.pi/wavelength
    distance = 1
    r = np.sqrt(X**2 + Y**2 + distance**2)
    I = (np.sin(k*r)/r)**2
    fig, ax = plt.subplots()
    ax.imshow(I, cmap='gray', extent=(-10, 10, -10, 10))
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_title('Diffraction pattern')
    plt.show()

# 4. Chaos game fractal
def chaos_game():
    n = 5000
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = 0.5
    y[0] = 0.5
    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    p3 = np.array([0.5, np.sqrt(3)/2])
    for i in range(1, n):
        r = np.random.randint(1, 4)
        if r == 1:
            x[i] = 0.5 * x[i-1]
            y[i] = 0.5 * y[i-1]
        elif r == 2:
            x[i] = 0.5 * x[i-1] + 0.5
            y[i] = 0.5 * y[i-1]
        else:
            x[i] = 0.5 * x[i-1] + 0.25
            y[i] = 0.5 * y[i-1] + 0.5*np.sqrt(3)/4
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=1, alpha=0.5)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, np.sqrt(3)/2])
    ax.set_aspect('equal')
    ax.set_title('Chaos game fractal')
    plt.show()


# 5. Fluid Flow
def fluid_flow():
    # Set up a grid for plotting
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)

    # Define the fluid flow equations
    U = Y
    V = -X

    # Create a quiver plot to visualize the fluid flow
    fig, ax = plt.subplots()
    ax.quiver(X, Y, U, V)

    # Add labels and a title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Fluid Flow')

    # Show the plot
    plt.show()


root = tk.Tk()
root.title("Physical Phenomena Visualization")

# Add buttons for each physical phenomenon
sine_button = tk.Button(root, text="Projectile Motion", command=projectile_motion)
sine_button.pack(side="left")

cosine_button = tk.Button(root, text="Simple Harmonic Motion", command=simple_harmonic_motion)
cosine_button.pack(side="left")

tangent_button = tk.Button(root, text="Diffraction Pattern", command=diffraction_pattern)
tangent_button.pack(side="left")

quadratic_button = tk.Button(root, text="Chaos Game", command=chaos_game)
quadratic_button.pack(side="left")

fluid_flow_button = tk.Button(root, text="Fluid Flow", command=fluid_flow)
fluid_flow_button.pack(side="left")

# Start the GUI event loop
root.mainloop()
