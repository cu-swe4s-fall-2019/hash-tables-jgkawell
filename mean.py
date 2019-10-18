import sys
import statistics


if __name__ == "__main__":
    V = []
    for l in sys.stdin:
        V.append(float(l))
    print(statistics.mean(V))
