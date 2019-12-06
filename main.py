import argparse
import os

from balls_generation import train_word2ball, initialize_dictionaries
from tree_generation.generate_tree import generate_files
from visualization.circles_fixer import reduce_and_fix
from visualization.ploting import visualize


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_nball')
    parser.add_argument('--w2v')
    parser.add_argument('--ws_child')
    parser.add_argument('--ws_catcode')
    parser.add_argument('--log')
    parser.add_argument('--sample')
    parser.add_argument('--input')
    parser.add_argument('--output')
    parser.add_argument('--balls')
    parser.add_argument('--children')
    parser.add_argument('--circles')
    parser.add_argument('--showenWords')
    parser.add_argument('-g', '--gen',  action='store_true')
    parser.add_argument('-v', '--vis',  action='store_true')
    parser.add_argument('-rf', '--reduceAndFix', action='store_true')

    args = parser.parse_args()

    if args.train_nball and args.w2v and args.ws_child and args.ws_catcode and args.log:
        outputPath, nballFile = os.path.split(args.train_nball)
        logFile = os.path.join(outputPath, 'traing.log')
        outputPath = os.path.join(outputPath, "data_out")

        wsChildrenDic, word2vecDic, wscatCodeDic = initialize_dictionaries(word2vecFile=args.w2v,
                                                                           catDicFile=args.ws_catcode,
                                                                           wsChildrenFile=args.ws_child)

        train_word2ball(root="*root*", outputPath=outputPath, wsChildrenDic=wsChildrenDic,
                        word2vecDic=word2vecDic, wscatCodeDic=wscatCodeDic, logFile=logFile,
                        word2ballDic=dict(),
                        outputBallFile=args.train_nball)

    if args.gen:
        if args.w2v and (args.input or args.sample) and args.output:
            print("Start generating files...")
            generate_files(args.w2v, args.input, args.sample, args.output)
            print("Finish generating files...")

    if args.reduceAndFix:
        if args.balls and args.children and args.output:
            reduce_and_fix(args.balls, args.children, args.output)

    if args.vis and args.circles:
        visualize(args.circles, args.showenWords)


if __name__ == "__main__":
    main()
