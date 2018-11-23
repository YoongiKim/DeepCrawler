import argparse
from Sampler import SAMPLER
from Trainer import TRAINER
from Crawler import CRAWLER

# Argument setup
parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default='sample', help='sample | train | crawl')
args = parser.parse_args()

# Start process
if args.mode == 'sample':
    # Start Sampler
    sampler = SAMPLER()
elif args.mode == 'train':
    # Start Trainer
    trainer = TRAINER()
elif args.mode == 'crawl':
    # Start Crawler
    crawler = CRAWLER()
else:
    print('Mode Error | Please set up --mode environment variable correctly.')