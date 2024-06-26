# Math functions and volume calculator   
  > This program is a graphical user interface (GUI) application developed based on the Tkinter library. It is used to draw mathematical functions, calculate the integral of the function, and calculate the three-dimensional volume obtained by rotating the function around the specified axis according to the user's selection.

**Here is the DEMO https://youtu.be/uiwxuDXgogU?feature=shared**

# #

### Features
- Users can enter a mathematical function and specify the domain of the function.
- The program plots the original function and its integral and displays the integration result.
- The user can choose whether to calculate the solid volume obtained by rotating the function around an axis.
- The user can choose which axis to rotate around, which can be the x-axis or the y-axis.
- The program will draw the rotated three-dimensional volume according to the user's selection and display the calculation results.

# #
### Usage
#### Prerequisites: (need to install these packages in your Python IDE before you do the next steps)
- Python 3.x
- NumPy
- Matplotlib
- Sympy
- Tkinter
#### Steps:

1. Copy and paste the code into your Python IDE.
    - if you want to use vscode, (https://code.visualstudio.com/learn/get-started/basics) can help you how to set up
2. Run the code.
3. In the GUI, enter the following：
    - The function expression (e.g., x**2)
    - The start value of the integration range (e.g., 0)
    - The end value of the integration range (e.g., 1)
    - Optionally, choose to calculate the volume around the X or Y axis
4. Click the "Plot Function and Integral" button.
   
> If next time you want to conveniently open this code and create a shortcut in .exe format, you can search the information in https://blog.csdn.net/2301_81337765/article/details/135012811
   
#### Code Explanation:

- The code creates a GUI application that allows the user to input a function and calculate its integral and volume.
- The user can choose to calculate the volume around the X or Y axis.
- The code uses Sympy to parse the function and perform the integration.
- It uses Matplotlib and Tkinter to plot the function, integral, and volume.

#### Example:

To plot the integral of the function x^2 and calculate the volume around the X axis, follow these steps:
1. Enter the function expression x**2.
2. Enter the start value of the integration range 0.
3. Enter the end value of the integration range 1.
4. Select the "Around X axis" option.
5. Click the "Plot Function and Integral" button.

**Result:**
The program will plot the function x^2, its integral, and the volume around the X axis. The volume result will be displayed in the GUI.

# #

### Code structure
The code structure of the program is as follows：

1. Import required libraries and modules

    - **tkinter library**: used to create GUI interfaces.
    - **numpy library**: used for numerical calculations and array operations.
    - **matplotlib library**: used for drawing graphics.
    - **mpl_toolkits.mplot3d module**: used to draw 3D graphics.
    - **sympy library**: for symbolic calculations.
    - **ttk** for themed Tkinter widgets

2. Define the function plot_volume_around_axis:

    - This function calculates the volume of the solid generated by rotating the function around the x or y-axis and plots it using Matplotlib.

3. Define the event handler function on_plot_hover:

    - This function handles the hover event on the plot and displays the coordinates of the hovered point.
    
4. Define the function plot_function_integral_volume:

    - This function is called when the "Plot Function and Integral" button is clicked.
    - It retrieves the user input for the function, range, and axis of rotation.
    - It plots the original function, its integral, and displays the integral result using Matplotlib.
    - If the user selects the "Calculate Volume" option, it calls the plot_volume_around_axis function to calculate and plot the volume.

5. Create the Tkinter window and set its properties:

    - Create the Tk window object.
    - Set the window title, size, and style.
    - Create a main frame to hold the widgets and configure its layout.
      
6. Create Tkinter widgets:

    - Create labels, entry fields, checkboxes, and buttons for user input.
    - Grid these widgets within the main frame.
      
7. configure layout and event handling:

    - Configure the layout of the main frame using columnconfigure and rowconfigure.
    - Bind the event handler function to the Matplotlib plot using canvas.mpl_connect.
      
8. Run the Tkinter main event loop:

    - Start the Tkinter event loop to display the GUI window and handle user interactions.
      
# #

### Graphical Abstract* (What does this software look like?)
<img width="700" height="400" src="https://github.com/StevenWangYuxuan/Software-Development-Project/blob/main/img/5.png"/>

<img width="700" height="400" src="https://github.com/StevenWangYuxuan/Software-Development-Project/blob/main/img/6.png"/>

<img width="700" height="400" src="https://github.com/StevenWangYuxuan/Software-Development-Project/blob/main/img/8.png"/>

# #

### The type of software development process is applied.
- Agile

# #

### The reason why we choose (Agile) ?
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
### Possible usage of the software (i.e., target market for the students preparing for advanced mathematics)
- **Educational institutions (e.g., schools, universities)** ：The code can be used as a teaching tool to help students visualize functions, integrals, and volumes of revolution. It can also be used to demonstrate the concepts of calculus in a more interactive and engaging way.
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
    
UML
- use case diagram:

<img width="700" height="400" src="https://github.com/StevenWangYuxuan/Software-Development-Project/blob/main/img/4.png"/>

- sequence diagram:
<img width="700" height="400" src="https://github.com/StevenWangYuxuan/Software-Development-Project/blob/main/img/3.png"/>


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

**Task 1**: Create User Interface and Graphical Display (Shay)
- Create input fields, buttons, and graphical displays.
- Ensure that the application is easy to use and has an intuitive user experience.

**Task 2**: Implement Function Parsing, Integral Calculation, and Volume Calculation (Steven)
- Implement algorithms to parse functions, calculate integrals, and calculate volumes.
- Ensure that the application is mathematically accurate and can handle a variety of functions.

**Task 3**: Design and Implement Data Visualization, make a demo video through youtube (James)
- Design and implement visual representations of the function, integral, and volume results.
- Ensure that the graphics are clear, informative, and easy to understand.

**Task 4**: Testing and Documentation (All 3 people)
- Write and execute test cases to verify the functionality and accuracy of the application.
- Write user manuals and documentation explaining the application's functionality and how to use it.

#### Timeline:
- Week 1 (3/11-3/18): Start Tasks 1 and 2
- Week 2 (3/23-3/30): Start Task 3
- Week 3 (4/5-4/12): Complete Tasks 1, 2, and 3
- Week 4 (4/13-4/20): Complete Task 4

#### Communication Plan:

- **Daily stand-up meetings**: Short daily meetings to discuss progress, roadblocks, and next steps.
- **Code reviews**: Code reviews will be conducted before code is committed to ensure quality and consistency.
- **Instant messaging**: An instant messaging platform (such as Slack or Microsoft Teams) will be used for quick communication and problem-solving.

# #

### Schedule

1. Import the necessary modules and libraries, including Tkinter, matplotlib, numpy, and sympy.
2. Define a function called plot_volume_around_axis to calculate and plot the volume around the specified axis.
3. Define a function called on_plot_hover to handle mouse hover events and display the coordinates of data points on the graph.
4. Define a function called plot_function_integral_volume to plot the function and its integral and display the computed volume.
6. Create a Tkinter window called window and set the window title, size, and style.
7. Create the main frame main_frame within the window to hold other GUI elements.
8. Create labels, input fields, checkboxes, buttons, and text labels within the main frame to receive user input and display results.
9. Configure the weights of rows and columns within the main frame to ensure adaptive layout adjustments when the window size changes.
10. Start the Tkinter event loop to wait for user interactions.

# #

### Algorithm*
Function and integral plotting:
- Sympy calculation:
  
```

    x_symbol = sp.symbols('x')
original_function = sp.sympify(function_input)
integral_function = sp.integrate(original_function, x_symbol)

```
- Matplotlib drawing:
  
```
fig, axs = plt.subplots(3, 1, figsize=(8, 12), gridspec_kw={'height_ratios': [1, 1, 0.5], 'hspace': 0.5})
x_vals = np.linspace(start, end, 400)

# Plot original function
f_original_lambdified = sp.lambdify(x_symbol, original_function, 'numpy')
y_vals_original = f_original_lambdified(x_vals)
axs[0].plot(x_vals, y_vals_original, label=f'f(x)={original_function}')
axs[0].set_title('Original Function Plot')
axs[0].grid(True)
axs[0].legend()

# Plot integral function
f_integral_lambdified = sp.lambdify(x_symbol, integral_function, 'numpy')
y_vals_integral = f_integral_lambdified(x_vals)
axs[1].plot(x_vals, y_vals_integral, label=f'Integral of f(x)={integral_function}')
axs[1].set_title('Integral Plot(Withou C)')
axs[1].grid(True)
axs[1].legend()

# Display integral result
integral_result = integral_function.subs(x_symbol, end) - integral_function.subs(x_symbol, start)
axs[2].text(0.5, 0.5, f'Integral Result: {integral_result.evalf()}', horizontalalignment='center', verticalalignment='center', transform=axs[2].transAxes)
axs[2].axis('off')

```
Volume calculation and drawing:
- Sympy calculation:
  
```
if axis == 'x':
    volume = sp.pi * sp.integrate(original_function**2, (x_symbol, start, end))
else:  # y-axis
    volume = sp.pi * sp.integrate(original_function**2, (x_symbol, start, end))

```
- Matplotlib drawing:
```
if axis == 'x':
    volume = sp.pi * sp.integrate(function**2, (x_symbol, start, end))
else:  # y-axis
    volume = sp.pi * sp.integrate(function**2, (x_symbol, start, end))
    
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
# 在标题中显示体积结果
ax.set_title(f'Volume around {axis.upper()}-axis: {volume.evalf()}')

plt.show()

```
Mouse hover event:

- Matplotlib event handling：
  
```
def on_plot_hover(event, axs, fig, canvas):
    for ax in axs:
        if event.inaxes == ax:
            for line in ax.get_lines():
                cont, ind = line.contains(event)
                if cont:
                    xdata, ydata = line.get_data()
                    x, y = xdata[ind["ind"][0]], ydata[ind["ind"][0]]
                    annot = ax.annotate(f"({x:.2f}, {y:.2f})", xy=(x, y), xytext=(20, 20), textcoords="offset points",
                                        bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5),
                                        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))
                    fig.canvas.draw_idle()
                    def remove_annot():
                        annot.remove()
                        fig.canvas.draw_idle()
                    fig.canvas.mpl_connect("motion_notify_event", lambda event: remove_annot())
```
other functions
- Tkinter widget:
  
```
window = tk.Tk()
window.title("Calculus Visualizer")
style = ttk.Style()
style.theme_use('clam')
window.minsize(600, 400)
main_frame = ttk.Frame(window, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

```
- NavigationToolbar2Tk：
  
```
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas_widget.grid(row=5, column=0, columnspan=4)
canvas.mpl_connect('motion_notify_event', lambda event: on_plot_hover(event, axs, fig, canvas))

toolbar_frame = ttk.Frame(window) 
toolbar_frame.grid(row=4, column=0, columnspan=4, sticky=(tk.W, tk.E))  
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)  
toolbar.update()

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

### Declaration

**Specifically, the code snippet uses these packages to:**
- **Sympy**: parse functions, compute integrals, and calculate volumes.
- **NumPy**: generate data points and create meshes.
- **Matplotlib**: create 3D surface plots, original function plots, and integral function plots.
- **Tkinter**: create a GUI window, buttons, labels, and other widgets.
  
<img width="850" height="400" src="https://github.com/StevenWangYuxuan/Software-Development-Project/blob/main/img/9.png"/>

> By leveraging these external packages, the code snippet can focus on its core functionality, such as computing and visualizing functions and integrals, without having to implement these features from scratch.

### Reference
https://code.visualstudio.com/learn/get-started/basics

https://blog.csdn.net/2301_81337765/article/details/135012811

















