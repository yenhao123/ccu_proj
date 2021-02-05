import argparse

def process_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default="140.123.0.0/16", help="scanning ip, default is 140.123.0.0/16")
    parser.add_argument('--count', type=int, default=10, help="the counts for scanning ip, default is 10")

    return parser.parse_args()

if __name__ == "__main__":
    args = process_parser()
    print(args.count)
