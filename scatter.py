import argparse
import sys
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def plot(out_file, x_label, y_label):

    X = []
    Y = []
    i = 0
    for l in sys.stdin:
        A = l.rstrip().split()
        if len(A) == 2:
            X.append(float(A[0]))
            Y.append(float(A[1]))
        elif len(A) == 1:
            X.append(float(i))
            Y.append(float(A[0]))
            i += 1

    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.plot(X, Y, '.', ms=1, alpha=0.5)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.savefig(out_file, bbox_inches='tight')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Visualize hash data from a file')
    parser.add_argument(
        '--out_file',
        type=str,
        help='The file name of the data')
    parser.add_argument(
        '--x_label',
        type=str,
        help='The x label for the plot')
    parser.add_argument(
        '--y_label',
        type=str,
        help='The y label for the plot')

    args = parser.parse_args()

    plot(args.out_file, args.x_label, args.y_label)
