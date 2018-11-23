import argparse

# Argument setup
parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default='sample', help='sample | train | crawl')
args = parser.parse_args()

# Start process
if args.mode is 'sample':
    # Start Sampler
    print('Start Sampling')
elif args.mode is 'train':
    # Start Trainer
    print('Start Training')
elif args.mode is 'crawl':
    # Start Crawler
    print('Start Crawling')
else:
    print('Mode Error | Please set up --mode environment variable correctly.')