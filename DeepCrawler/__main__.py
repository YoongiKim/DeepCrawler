import argparse
from Sampler import SAMPLER
from Trainer import TRAINER
from AutoCrawler import AUTOCRAWLER

# Argument setup
parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default='sample', help='sample | train | autocrawl')
args = parser.parse_args()

# Start process
if args.mode == 'sample':
    # Start Sampler
    sampler = SAMPLER()
elif args.mode == 'train':
    # Start Trainer
    trainer = TRAINER()
elif args.mode == 'autocrawl':
    # Start Crawler
    autocrawler = AUTOCRAWLER()
else:
    print('Mode Error | Please set up --mode environment variable correctly.')