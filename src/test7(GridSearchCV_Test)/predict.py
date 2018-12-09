import pandas as pd
import argparse
import tqdm
import os
import sys
import core
import joblib

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--datadir', help='trainset dir')
parser.add_argument('-o', '--output', help='output file')
parser.add_argument('-m', '--model', help='model path')

args = parser.parse_args()

if not os.path.exists(args.datadir):
    parser.error("{} does not exist".format(args.datadir))
if not os.path.exists(args.model):
    parser.error("{} model does not exist".format(args.model))

def main():    
    clf = joblib.load(args.model)
    y_pred = []
    name = []

    for filename in tqdm.tqdm(os.listdir(args.datadir)):    
        try:
            feature = core.extractor(os.path.join(args.datadir, filename))
            r = clf.predict([feature])            
            name.append(filename)
            y_pred.append(r[0])
        except KeyboardInterrupt:
            sys.exit()
        except:
            name.append(filename)
            y_pred.append(1)
            pass
    
    df = pd.DataFrame({'hash': name, 'y_pred': y_pred})
    df.to_csv(args.output, index=False, header=None)
    
if __name__=='__main__':
    main()