# Math functions and volume calculator   
  > This program is a graphical user interface (GUI) application developed based on the Tkinter library. It is used to draw mathematical functions, calculate the integral of the function, and calculate the three-dimensional volume obtained by rotating the function around the specified axis according to the user's selection.

# #

### Features
- Users can enter a mathematical function and specify the domain of the function.
- The program plots the original function and its integral and displays the integration result.
- The user can choose whether to calculate the solid volume obtained by rotating the function around an axis.
- The user can choose which axis to rotate around, which can be the x-axis or the y-axis.
- The program will draw the rotated three-dimensional volume according to the user's selection and display the calculation results.

# #

### Code structure
The code structure of the program is as follows：

1. Import required libraries and modules

    - **tkinter library**: used to create GUI interfaces.
    - **numpy library**: used for numerical calculations and array operations.
    - **matplotlib library**: used for drawing graphics.
    - **mpl_toolkits.mplot3d module**: used to draw 3D graphics.
    - **sympy library**: for symbolic calculations.

2. Function Definitions:

    - **plot_volume_around_axis(function_input, start, end, axis)**: Plots the volume of revolution around the specified axis.
    - **on_plot_hover(event, axs, fig, canvas)**: Handles mouse hover events on the plot to display data point coordinates.
    - **plot_function_integral_volume()**: Plots the original function, its integral, and the volume of revolution.

3. Main Program:

    - Creates a Tkinter window (window) and sets its title.
    - Defines the layout of the window using a grid system.
    - Creates widgets for user input (function, range, options) and a button for plotting.
    - Defines a callback function (plot_function_integral_volume) that is executed when the plot button is clicked.

4. Callback Function(plot_function_integral_volume):

    - Retrieves user input from the GUI.
    - Parses the function input and calculates its integral using Sympy.
    - Plots the original function, its integral, and the volume of revolution.
    - Displays the volume result in a label.

5. Main Event Loop:

    - Enters the main event loop (window.mainloop()) to listen for user interactions and handle events.
# #

### Graphical Abstract*
![1](https://github.com/StevenWangYuxuan/RW-project/blob/main/README-project/1.png)
![2](https://github.com/StevenWangYuxuan/RW-project/blob/main/README-project/2.png)

# #

### Which type of software development process is applied.
- Agile

# #

### Why you choses this type (Waterfall vs. Agile)?
#### Background

> In the absence of robust mathematical tools, we are committed to developing a powerful and easy-to-use software that will allow students and educators to visualize and understand complex mathematical concepts with ease.

- **Time2M** is of the essence

- Time to Market (TTM) is crucial for any software product, especially in a competitive market such as educational technology. By adopting an Agile development approach, we will be able to iterate and improve our software rapidly, allowing us to bring our product to market faster than our competitors. This will enable us to capture market share and build a strong user base.

What is Agile and why is it a great fit?

> Agile is a software development methodology that emphasizes iterative and incremental development, team collaboration, and adaptability to change. It is a great fit for our Calculus Visualizer project for the following reasons:

1. Iterative and incremental development: Agile allows us to build our software in stages, starting with basic functionality and then adding more features and refinements based on user feedback. This enables us to get our product into users' hands quickly and adjust our development roadmap based on their needs.

2. Team collaboration: Agile stresses teamwork and cross-functional collaboration. This is essential for our project, as we will need mathematicians, software engineers, and UX designers working together to create software that is both accurate and user-friendly.

3. Adaptability to change: Agile development is adaptable to changing requirements and priorities. As we gather user feedback and learn more about their needs, we can adjust our development roadmap with agility to ensure that we are focused on the most important features. Therefore, we choose Agile



> In conclusion, Agile development is the optimal approach for developing our Calculus Visualizer software. It will allow us to iterate quickly, adapt to change, collaborate with our users, and capture market share. We are confident that by embracing Agile methodologies, we can create a groundbreaking software that will revolutionize the way students and educators learn and teach mathematics.
# #
### Possible usage of your software (i.e., target market)
- **Educational institutions (e.g., schools, universities)**
- **Students and educators in calculus courses**
- Individuals interested in visualizing calculus concepts

# #
### Development Process
- Agile: Scrum methodology  

**Components:**
1. **Requirements Gathering and Analysis:**

- Functional Requirements:   

  - Plot mathematical functions.
  - Calculate the integral of functions.
  - Calculate the volume of revolution around specified axes.
- Non-Functional Requirements:
  - User-friendly graphical interface.
  - Efficient and accurate calculations.
  - Extensible for future features.

2. **Design:**

- High-Level Architecture:
  - GUI for user input and visualization.
  - Mathematical engine for calculations.
  - Data storage for function and integral data.
- Modules and Components:
  - Function plotting module.
  - Integral calculation module.
  - Volume calculation module.
  - GUI module.
3. **Implementation:**

- Programming Languages and Tools:
  - Python.
  - Tkinter for GUI.
  - NumPy for numerical calculations.
  - Matplotlib for plotting.
  - Sympy for symbolic calculations.

- Coding Standards:
  - PEP 8 style guide.
  - Unit tests for individual modules.

4. **Testing:**

   - Unit Tests: Verify the functionality of individual modules.
   - Integration Tests: Ensure that modules work together correctly.
   - System Tests: Evaluate the overall functionality and performance of the software.

5. **Deployment:**

   - Packaging: Create an executable or installer for - distribution.
   - Installation: Provide clear instructions for installing the software.
   - Documentation: User manual and technical documentation.

6. **Maintenance:**

   - Bug Tracking: Monitor and fix any bugs reported by users.
   - Updates and Patches: Release updates to improve functionality and fix issues.
   - Technical Support: Provide support to users experiencing problems.


# #

### Members (Roles & Responsibilities & Portion)
- Product Owner (Shay) : Manages the product backlog and prioritizes user stories
- Development Team (Shay, Steven, James) : Designs, develops, and tests the software
- Scrum Master (Shay, Steven, James): Facilitates the Scrum process and removes roadblocks

# #

### Schedule

  Sprint 1: Function and integral plotting  
  Sprint 2: Volume calculation and visualization  
  Sprint 3: User interface enhancements and bug fixes

# #

### Algorithm*

- Function and Integral Plotting: Numerical integration using Sympy's integrate function
```

    f_original_lambdified = sp.lambdify(x_symbol, original_function, 'numpy')
    y_vals_original = f_original_lambdified(x_vals)
    axs[0].plot(x_vals, y_vals_original, label=f'f(x)={original_function}')
    axs[0].set_title('Original Function Plot')
    axs[0].grid(True)
    axs[0].legend()


    f_integral_lambdified = sp.lambdify(x_symbol, integral_function, 'numpy')
    y_vals_integral = f_integral_lambdified(x_vals)
    axs[1].plot(x_vals, y_vals_integral, label=f'Integral of f(x)={integral_function}')
    axs[1].set_title('Integral Plot')
    axs[1].grid(True)
    axs[1].legend()
```
- Volume Calculation: Integration of the function squared
```
if calculate_volume.get():
        plot_volume_around_axis(function_input, start, end, axis)
    if axis == 'x':
        volume = sp.pi * sp.integrate(original_function**2, (x_symbol, start, end))
    else:  # y-axis
        volume = sp.pi * sp.integrate(original_function**2, (x_symbol, start, end))
```
- 3D Volume Visualization: Matplotlib's plot_surface function
```
def plot_volume_around_axis(function_input, start, end, axis='x'):
    x_symbol = sp.symbols('x')
    function = sp.sympify(function_input)
    integral_function = sp.integrate(function, x_symbol)
    f_lambdified = sp.lambdify(x_symbol, integral_function, 'numpy')

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(start, end, 100)
    phi = np.linspace(0, 2 * np.pi, 100)
    X, P = np.meshgrid(x, phi)

    R = f_lambdified(X)
    if axis == 'x':
        Y = R * np.cos(P)
        Z = R * np.sin(P)
    else:  # Around y-axis
        Y = X
        X = R * np.cos(P)
        Z = R * np.sin(P)

    ax.plot_surface(X, Y, Z, color='b', alpha=0.6)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title(f'Volume around {axis.upper()}-axis')

    plt.show()
```

# #

### Current status of your software
- Alpha Release: Basic functionality is implemented, including function and integral plotting.
- Beta Release (Planned): Volume calculation and visualization will be added.
- Stable Release (Planned): User interface improvements and bug fixes will be implemented.

# #

### Future plan
- Advanced Features:
  - Plotting of curves in 3D space
  - Integration of user-defined functions
- Educational Resources:
  - Integration with online learning platforms
  - Development of interactive tutorials and simulations
- Collaboration:
  - Open-source the software for community contributions
  - Collaborate with educators to enhance its educational value 


