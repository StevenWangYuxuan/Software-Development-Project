import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import sympy as sp



def plot_volume_around_axis(function_input, start, end, axis='x'):
    x_symbol = sp.symbols('x')
    function = sp.sympify(function_input)
    # 计算体积
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

def plot_function_integral_volume():
    
    function_input = function_entry.get()
    start = float(range_start_entry.get())
    end = float(range_end_entry.get())
    axis = 'x' if axis_var.get() == 1 else 'y'

    x_symbol = sp.symbols('x')
    original_function = sp.sympify(function_input)
    integral_function = sp.integrate(original_function, x_symbol)

    # 调整子图之间的间距
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

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=5, column=0, columnspan=4)
    canvas.draw()
    canvas.mpl_connect('motion_notify_event', lambda event: on_plot_hover(event, axs, fig, canvas))

    if calculate_volume.get():
        plot_volume_around_axis(function_input, start, end, axis)
    if axis == 'x':
        volume = sp.pi * sp.integrate(original_function**2, (x_symbol, start, end))
    else:  # y-axis
        volume = sp.pi * sp.integrate(original_function**2, (x_symbol, start, end))
    volume_result_label.config(text=f"Volume around {axis.upper()}-axis: {volume}")
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas_widget.grid(row=5, column=0, columnspan=4)
    canvas.mpl_connect('motion_notify_event', lambda event: on_plot_hover(event, axs, fig, canvas))

    toolbar_frame = ttk.Frame(window)  # 创建一个框架来放置工具栏
    toolbar_frame.grid(row=4, column=0, columnspan=4, sticky=(tk.W, tk.E))  # 定位工具栏框架
    toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)  # 创建工具栏
    toolbar.update()
    
# 创建Tkinter窗口
window = tk.Tk()
window.title("Calculus Visualizer")
style = ttk.Style()
style.theme_use('clam')
window.minsize(600, 400)
main_frame = ttk.Frame(window, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
function_label = ttk.Label(main_frame, text="Enter function:", font=('Arial', 12))
function_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
function_entry = ttk.Entry(main_frame, font=('Arial', 10))
function_entry.grid(row=0, column=1, columnspan=3, sticky=(tk.W, tk.E), padx=5, pady=5)

range_start_label = ttk.Label(main_frame, text="Start of range:", font=('Arial', 12))
range_start_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
range_start_entry = ttk.Entry(main_frame, font=('Arial', 10))
range_start_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

range_end_label = ttk.Label(main_frame, text="End of range:", font=('Arial', 12))
range_end_label.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
range_end_entry = ttk.Entry(main_frame, font=('Arial', 10))
range_end_entry.grid(row=1, column=3, sticky=(tk.W, tk.E), padx=5, pady=5)

calculate_volume = tk.BooleanVar()
calc_volume_check = ttk.Checkbutton(main_frame, text="Calculate Volume", variable=calculate_volume)
calc_volume_check.grid(row=2, column=0, columnspan=2, sticky=tk.W, padx=5, pady=5)

volume_result_label = ttk.Label(main_frame, text="", font=('Arial', 10))
volume_result_label.grid(row=6, column=0, columnspan=4, sticky=(tk.W, tk.E), padx=5, pady=5)

axis_var = tk.IntVar(value=1)
axis_x_radio = ttk.Radiobutton(main_frame, text="Around X-axis", variable=axis_var, value=1)
axis_x_radio.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)
axis_y_radio = ttk.Radiobutton(main_frame, text="Around Y-axis", variable=axis_var, value=2)
axis_y_radio.grid(row=2, column=3, sticky=tk.W, padx=5, pady=5)

plot_button = ttk.Button(main_frame, text="Plot Function and Integral", command=lambda: plot_function_integral_volume())
plot_button.grid(row=3, column=0, columnspan=4, sticky=(tk.W, tk.E), padx=5, pady=10)


for i in range(4):
    main_frame.columnconfigure(i, weight=1)
for i in range(7):
    main_frame.rowconfigure(i, weight=1)

window.mainloop()
