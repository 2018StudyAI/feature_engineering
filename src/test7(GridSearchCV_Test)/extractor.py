import pandas as pd
import argparse
import tqdm
import os
import sys
import core

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--datadir', help='trainset dir')
parser.add_argument('-l', '--label', help='trainset label(csv file)')
parser.add_argument('-o', '--output', help='output file(csv)')
args = parser.parse_args()

if not os.path.exists(args.datadir):
    parser.error("{} does not exist".format(args.datadir))
if not os.path.exists(args.label):
    parser.error("{} does not exist".format(args.label))

label = pd.read_csv(args.label, names=['hash', 'y'])

def main():    
    features = []
    
    for filename in tqdm.tqdm(os.listdir(args.datadir)):    
        try:
            data = []

            data.append(filename) #add filename
            data += (core.extractor(os.path.join(args.datadir, filename))) #add features
            y = label[label.hash==filename].values[0][1] 
            data.append(y) #add label
            
            features.append(data)
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass

    columns = [
        'filename',

        'NumberOfSectons', 'TimeDateStamp', 'PointerToSymbolTable', 'NumberOfSybols', 'SizeOfOptionalHeader', 'Characteristics',
       
        'Magic', 'MajorLinkerVersion', 'MinorLinkerVersion', 'SizeOfCode', 'SizeOfInitializeData', 'SizeOfUninitalizeData', 'AddressOfEntryPoint',
        'BaseOfCode', 'BaseOfData', 'ImageBase', 'sectionAlignment', 'FileAlignment', 'MajorOperationSystemVersion', 'MinorOperatingSystemVersion', 'MajorImageVersion', 'MinorImageVersion',
        'MajorSubsytemVersion', 'MinorSubsytemVersion', 
        'Reserved1', 'SizeOfImage', 'SimzeOfHeaders', 'CheckSum', 'DllCharacteristics', 'SizeOfStackRserve', 'SizeofStackCommit', 'SizeOfHeapRserve', 'SizeOfHeapCommit',
        'LoaderFlags', 'NumberOfRvaAndSizes',

        'has_debug', 'has_tls',

        'e_meagic', 'e_lfanew',

        'mal/benign'
    ]
    
    df = pd.DataFrame(features, columns=columns)
    df.to_csv(args.output, index=False)
    
if __name__=='__main__':
    main()