import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_results(random_inputs, random_results, fscs_inputs, fscs_results, clusters):
    fig = plt.figure(figsize=(14, 6))

    def plot(ax, inputs, results, title):
        passes = inputs[results == 'pass']
        fails = inputs[results == 'fail']

        ax.scatter(passes[:, 0], passes[:, 1], passes[:, 2], c='green', label='Pass', alpha=0.4)
        ax.scatter(fails[:, 0], fails[:, 1], fails[:, 2], c='red', label='Fail', alpha=0.8)

        for cluster in clusters:
            cx, cy, cz = cluster['center']
            ax.text(cx, cy, cz, "Fail Zone", color='red')

        ax.set_title(title)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.legend()

    ax1 = fig.add_subplot(121, projection='3d')
    plot(ax1, random_inputs, random_results, "Pure Random Testing")

    ax2 = fig.add_subplot(122, projection='3d')
    plot(ax2, fscs_inputs, fscs_results, "FSCS-ART Testing")

    plt.tight_layout()
    plt.show()
