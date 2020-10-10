import argparse
from converter import smartify 

parser = argparse.ArgumentParser(description="Smartify input sentence")
parser.add_argument("sentence", type=str, nargs='*')

# extract the sentence
sentence = ' '.join(parser.parse_args().sentence)

smartified = smartify(sentence)

print("Original: {:>10}".format(sentence))
print("Smartified: {:>10}".format(smartified))