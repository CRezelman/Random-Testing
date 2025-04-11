import matplotlib.pyplot as plt

def plot_results(random_inputs, random_results, fscs_inputs, fscs_results, clusters):
    def plot_3d(ax, inputs, results, title):
        passes = inputs[results == 'pass']
        fails = inputs[results == 'fail']

        ax.scatter(passes[:, 0], passes[:, 1], passes[:, 2], c='green', label='Pass', alpha=0.4)
        ax.scatter(fails[:, 0], fails[:, 1], fails[:, 2], c='red', label='Fail', alpha=0.8)

        for cluster in clusters:
            cx, cy, cz = cluster['center']
            ax.text(cx, cy, cz, "Fail Zone", color='red')

        ax.set_title(f"{title} - 3D")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.legend()

    def plot_2d(ax, inputs, results, title, idx1, idx2, labels):
        passes = inputs[results == 'pass']
        fails = inputs[results == 'fail']

        ax.scatter(passes[:, idx1], passes[:, idx2], c='green', label='Pass', alpha=0.4)
        ax.scatter(fails[:, idx1], fails[:, idx2], c='red', label='Fail', alpha=0.8)

        for cluster in clusters:
            coord = cluster['center']
            ax.text(coord[idx1], coord[idx2], "Fail Zone", color='red')

        ax.set_title(f"{title} - {labels[0]}{labels[1]} Plane")
        ax.set_xlabel(labels[0])
        ax.set_ylabel(labels[1])
        ax.legend()

    # --- First GUI: 3D Plots ---
    fig_3d = plt.figure(figsize=(14, 6))
    ax1 = fig_3d.add_subplot(121, projection='3d')
    plot_3d(ax1, random_inputs, random_results, "Random Testing")

    ax2 = fig_3d.add_subplot(122, projection='3d')
    plot_3d(ax2, fscs_inputs, fscs_results, "FSCS-ART Testing")

    fig_3d.tight_layout()
    fig_3d.canvas.manager.set_window_title('3D Visualisation')

    # --- Second GUI: 2D Projections ---
    fig_2d = plt.figure(figsize=(14, 12))
    ax3 = fig_2d.add_subplot(321)
    plot_2d(ax3, random_inputs, random_results, "Random", 0, 1, ('X', 'Y'))

    ax4 = fig_2d.add_subplot(322)
    plot_2d(ax4, fscs_inputs, fscs_results, "FSCS-ART", 0, 1, ('X', 'Y'))

    ax5 = fig_2d.add_subplot(323)
    plot_2d(ax5, random_inputs, random_results, "Random", 0, 2, ('X', 'Z'))

    ax6 = fig_2d.add_subplot(324)
    plot_2d(ax6, fscs_inputs, fscs_results, "FSCS-ART", 0, 2, ('X', 'Z'))

    ax7 = fig_2d.add_subplot(325)
    plot_2d(ax7, random_inputs, random_results, "Random", 1, 2, ('Y', 'Z'))

    ax8 = fig_2d.add_subplot(326)
    plot_2d(ax8, fscs_inputs, fscs_results, "FSCS-ART", 1, 2, ('Y', 'Z'))

    fig_2d.tight_layout()
    fig_2d.canvas.manager.set_window_title('2D Plane Projections')

    # Show both windows
    plt.show()
