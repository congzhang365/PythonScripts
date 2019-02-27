import os
import argparse

source = "D:\\Rokid\\Projects\\English\\toklin\\interval"


def replace_name_batch_post_fix(source, suffix, target_suffix):
    for f in os.listdir(source):
        old = os.path.join(source, f)
        # print(old)
        new = old.replace('.' + suffix, '.' + target_suffix)
        os.rename(old, new)


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('--source', type=str, default='123')
    parse.add_argument('--suffix', type=str)
    parse.add_argument('--target', type=str)
    args = parse.parse_args()
    replace_name_batch_post_fix(args.source, args.suffix, args.target)
    print(args.source)
