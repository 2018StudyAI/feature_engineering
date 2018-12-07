import pefile
import os
import lief
import numpy as np
from sklearn.feature_extraction import DictVectorizer

def transformBool(data):
    if data is True:
        return 1
    else:
        return 0

def ByteHistogram(path):
    bytesBuffer = open(path, 'rb').read()
    counts = np.bincount(np.frombuffer(bytesBuffer, dtype=np.uint8), minlength=256)
    histogram_sum = counts.sum()
    normalized = counts / histogram_sum

    return normalized
    #hstack = np.hstack(normalized).astype(np.float32)
    #return hstack
    #print(type(hstack))
    #return hstack
    #return np.memmap(normalized, dtype=np.float32, shape=(1, 1))

def extractor(path):
    pe = pefile.PE(path)

    file_header = pe.FILE_HEADER
    optional_header = pe.OPTIONAL_HEADER
    dos_header = pe.DOS_HEADER
    
    features = []
    #file_header
    features.append(file_header.NumberOfSections)
    features.append(file_header.TimeDateStamp)
    features.append(file_header.PointerToSymbolTable)
    features.append(file_header.NumberOfSymbols)
    features.append(file_header.SizeOfOptionalHeader)
    features.append(file_header.Characteristics)

    #optional_header
    features.append(optional_header.Magic)
    features.append(optional_header.MajorLinkerVersion)
    features.append(optional_header.MinorLinkerVersion)
    features.append(optional_header.SizeOfCode)
    features.append(optional_header.SizeOfInitializedData)
    features.append(optional_header.SizeOfUninitializedData)
    features.append(optional_header.AddressOfEntryPoint)
    features.append(optional_header.BaseOfCode)
    features.append(optional_header.BaseOfData)
    features.append(optional_header.ImageBase)
    features.append(optional_header.SectionAlignment)
    features.append(optional_header.FileAlignment)
    features.append(optional_header.MajorOperatingSystemVersion)
    features.append(optional_header.MinorOperatingSystemVersion)
    features.append(optional_header.MajorImageVersion)
    features.append(optional_header.MinorImageVersion)
    features.append(optional_header.MajorSubsystemVersion)
    features.append(optional_header.MinorSubsystemVersion)
    features.append(optional_header.Reserved1)
    features.append(optional_header.SizeOfImage)
    features.append(optional_header.SizeOfHeaders)
    features.append(optional_header.CheckSum)
    features.append(optional_header.DllCharacteristics)
    features.append(optional_header.SizeOfStackReserve)
    features.append(optional_header.SizeOfStackCommit)
    features.append(optional_header.SizeOfHeapReserve)
    features.append(optional_header.SizeOfHeapCommit)
    features.append(optional_header.LoaderFlags)
    features.append(optional_header.NumberOfRvaAndSizes)

    #has_tls
    lief_binary = lief.parse(path)
    features.append(transformBool(lief_binary.has_debug))
    features.append(transformBool(lief_binary.has_tls))

    #DOS_HEADER
    features.append(dos_header.e_magic)
    features.append(dos_header.e_lfanew)
    
    return features