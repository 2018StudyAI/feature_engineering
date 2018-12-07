import pandas as pd
import argparse
import tqdm
import os
import sys
import core

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--datadir', help='trainset dir')
parser.add_argument('-l', '--label', help='trainset label(csv file)')
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

    output = '[test3]features.csv'
    columns = [
        'filename',

        'NumberOfSectons', 'TimeDateStamp', 'PointerToSymbolTable', 'NumberOfSybols', 'SizeOfOptionalHeader', 'Characteristics',

        'IMAGE_FILE_DEBUG_STRIPPED', 'IMAGE_FILE_DLL', 'IMAGE_FILE_EXECUTABLE_IMAGE', 'IMAGE_FILE_LARGE_ADDRESS_AWARE', 'IMAGE_FILE_LINE_NUMS_STRIPPED', 'IMAGE_FILE_LOCAL_SYMS_STRIPPED',
        'IMAGE_FILE_NET_RUN_FROM_SWAP', 'IMAGE_FILE_RELOCS_STRIPPED', 'IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP', 'IMAGE_FILE_SYSTEM', 'IMAGE_FILE_UP_SYSTEM_ONLY',

        'Magic', 'MajorLinkerVersion', 'MinorLinkerVersion', 'SizeOfCode', 'SizeOfInitializeData', 'SizeOfUninitalizeData', 'AddressOfEntryPoint',
        'BaseOfCode', 'BaseOfData', 'ImageBase', 'sectionAlignment', 'FileAlignment', 'MajorOperationSystemVersion', 'MinorOperatingSystemVersion', 'MajorImageVersion', 'MinorImageVersion',
        'MajorSubsytemVersion', 'MinorSubsytemVersion', 
        'Reserved1', 'SizeOfImage', 'SimzeOfHeaders', 'CheckSum', 'DllCharacteristics', 'SizeOfStackRserve', 'SizeofStackCommit', 'SizeOfHeapRserve', 'SizeOfHeapCommit',
        'LoaderFlags', 'NumberOfRvaAndSizes',

        'has_tls', 'has_debug',

        'e_meagic', 'e_lfanew',

        'mal/benign'
    ]
    
    df = pd.DataFrame(features, columns=columns)
    df.to_csv(output, index=False)
    
if __name__=='__main__':
    main()