from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk

def plot_results(result_sets, clusters):
    root = tk.Tk()
    root.title("Test Results Visualisation")

    datasets = {
        name: (inputs, results, tk.BooleanVar(value=True, master=root))
        for name, (inputs, results) in result_sets.items()
    }

    colours = [
        "blue", "orange", "purple", "green", "red", "cyan", "magenta", "yellow"
    ]
    markers = ['o', 'x', '^', 's', 'D', 'p', '*']

    def create_figure():
        return Figure(figsize=(7, 6), dpi=100)

    def draw_plot(axs, is_3d):
        for ax in axs:
            ax.clear()

        for idx, (name, (inputs, results, var)) in enumerate(datasets.items()):
            if not var.get():
                continue

            passes = inputs[results == 'pass']
            fails = inputs[results == 'fail']

            colour = colours[idx % len(colours)]
            pass_marker = markers[0]
            fail_marker = markers[1]

            if is_3d:
                axs[0].scatter(passes[:, 0], passes[:, 1], passes[:, 2], label=f"{name} Pass", 
                               color=colour, marker=pass_marker, alpha=0.3)
                axs[0].scatter(fails[:, 0], fails[:, 1], fails[:, 2], label=f"{name} Fail", 
                               color=colour, marker=fail_marker, alpha=0.8)
                for cluster in clusters:
                    cx, cy, cz = cluster['center']
                    axs[0].text(cx, cy, cz, "Fail Zone", color='red')
            else:
                axs[0].scatter(passes[:, 0], passes[:, 1], label=f"{name} Pass", 
                               color=colour, marker=pass_marker, alpha=0.3)
                axs[0].scatter(fails[:, 0], fails[:, 1], label=f"{name} Fail", 
                               color=colour, marker=fail_marker, alpha=0.8)

                axs[1].scatter(passes[:, 0], passes[:, 2], label=f"{name} Pass", 
                               color=colour, marker=pass_marker, alpha=0.3)
                axs[1].scatter(fails[:, 0], fails[:, 2], label=f"{name} Fail", 
                               color=colour, marker=fail_marker, alpha=0.8)

                axs[2].scatter(passes[:, 1], passes[:, 2], label=f"{name} Pass", 
                               color=colour, marker=pass_marker, alpha=0.3)
                axs[2].scatter(fails[:, 1], fails[:, 2], label=f"{name} Fail", 
                               color=colour, marker=fail_marker, alpha=0.8)

                for cluster in clusters:
                    cx, cy, cz = cluster['center']
                    axs[0].text(cx, cy, "Fail Zone", color='red')
                    axs[1].text(cx, cz, "Fail Zone", color='red')
                    axs[2].text(cy, cz, "Fail Zone", color='red')

        titles = ["3D View"] if is_3d else ["XY Plane", "XZ Plane", "YZ Plane"]
        for ax, title in zip(axs, titles):
            ax.set_title(title)
            ax.legend()

    def create_3d_tab(parent):
        fig = create_figure()
        ax = fig.add_subplot(111, projection='3d')
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        draw_plot([ax], True)
        return canvas, fig, [ax]

    def create_2d_tab(parent):
        fig = create_figure()
        axs = [fig.add_subplot(311), fig.add_subplot(312), fig.add_subplot(313)]
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        draw_plot(axs, False)
        return canvas, fig, axs

    def update_all():
        draw_plot(three_d_axs, True)
        three_d_canvas.draw()
        draw_plot(two_d_axs, False)
        two_d_canvas.draw()

    tab_control = ttk.Notebook(root)
    tab_3d = ttk.Frame(tab_control)
    tab_2d = ttk.Frame(tab_control)
    tab_control.add(tab_3d, text='3D View')
    tab_control.add(tab_2d, text='2D Views')
    tab_control.pack(expand=1, fill="both")

    three_d_canvas, three_d_fig, three_d_axs = create_3d_tab(tab_3d)
    two_d_canvas, two_d_fig, two_d_axs = create_2d_tab(tab_2d)

    control_frame = ttk.Frame(root)
    control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)
    ttk.Label(control_frame, text="Toggle Test Sets").pack(anchor=tk.W)
    for name, (_, _, var) in datasets.items():
        cb = ttk.Checkbutton(control_frame, text=name, variable=var, command=update_all)
        cb.pack(anchor=tk.W)

    root.mainloop()
