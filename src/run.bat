python .\test6\extractor.py -d C:\Users\kgg19\Documents\dataset\TrainSet -l C:\Users\kgg19\Documents\dataset\TrainSet.csv -o ./test6/[test6]features.csv 
python .\test6\train.py -f ./test6/[test6]features.csv -o .\test6\model1.pkl
python .\test6\predict.py -m .\test6\model1.pkl -d C:\Users\kgg19\Documents\dataset\TestSet_final1_VX -o .\test6\result.csv