import argparse

def process_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', help="scanning ip")
    parser.add_argument('--count', type=int, default=10, help="the counts for scanning ip")

    return parser.parse_args()

if __name__ == "__main__":
    args = process_parser()
    print(args.count)
