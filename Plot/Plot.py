import matplotlib
import matplotlib.pyplot as plt
import argparse

matplotlib.use('TkAgg')


def Plot(x=None, x_label=None, y1=None, y1_label=None, y2=None, y2_label=None,
         legend=None, linewidth=1, fig_path=None):
    """
    """
    print(legend)
    if legend is None:
        legend = [None, None]

    fig, ax = plt.subplots(1, 1)
    plot_settings = {'linewidth': linewidth}
    cmap = plt.get_cmap('tab10')

    ax.plot(x, y1, label=legend[0], color=cmap(0), **plot_settings)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y1_label)
    ax.legend()

    if y2 is not None:
        ax2 = ax.twinx()
        ax2.plot(x, y2, label=legend[1], color=cmap(1), **plot_settings)
        ax2.set_ylabel(y2_label)
        ax2.legend()
    # plt.show(block=False)
    plt.show()

    if fig_path is not None:
        fig.savefig(fig_path)


def parse_args():
    parser = argparse.ArgumentParser(description='parse argments')
    parser.add_argument('--x', dest='x', nargs='+', type=float, default=None,
                        help='')
    parser.add_argument('--x-label', dest='x_label', type=str, default=None,
                        help='')
    parser.add_argument('--y', dest='y1', nargs='+', type=float, default=None,
                        help='')
    parser.add_argument('--y-label', dest='y1_label', type=str, default=None,
                        help='')
    parser.add_argument('--y2', dest='y2', nargs='+', type=float, default=None,
                        help='')
    parser.add_argument('--y2-label', dest='y2_label', type=str, default=None,
                        help='')
    parser.add_argument('--legend', dest='legend', nargs='+', type=str,
                        default=None, help='')
    parser.add_argument('--linewidth', dest='linewidth', type=int,
                        default=1, help='')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    Plot(x=args.x, x_label=args.x_label,
         y1=args.y1, y1_label=args.y1_label,
         y2=args.y2, y2_label=args.y2_label,
         legend=args.legend,
         linewidth=args.linewidth)


if __name__ == '__main__':
    main()
