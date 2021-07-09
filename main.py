import lexical_analysis
import syntactic_analysis
import argparse

def parse_args():

    parser = argparse.ArgumentParser(description="Run lexical_analysis.")

    parser.add_argument('--input', type=str,
                        help='Input filename')

    parser.add_argument('--output', type=str,
                        help='Output filename')
    return parser.parse_args()

def main(args):
    lexical_result = lexical_analysis.make_lexical_analysis(args.input, args.output)
    syntactic_analysis.make_syntatic_analysis(lexical_result)

#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    args = parse_args()
    main(args)