Simple tool to split coco annotations file and images file into the two sets of training and validation. 

No external module is neaded, only python.

The data is shuffled before splitting, it creates valid annotation file with 'images', 'categories', 'annotations' and 'info' keys if it exist.

## How it's splitted

The file organisation will be as follows :

```
data/
  ├── traindir/
  ├── testdir/
  └── annotations/
  	├── instances_train.json
  	└── instances_test.json
```

## How it works

```
> python cocosplitter.py -h
usage: cocosplitter.py [-h] --annotation-file ANNOT --destination-dirtrain DESTTRAIN --destination-dirtest DESTTEST
                       --split SPLIT

Split Coco annotation file and image file into training and test set

optional arguments:
  -h, --help            show this help message and exit
  --annotation-file ANNOT
                        Name of the file containing Coco annotations
  --destination-dirtrain DESTTRAIN
                        Name of the directory that will contain the train set images
  --destination-dirtest DESTTEST
                        Name of the directory that will contain the test set images
  --split SPLIT         Percentage of data that will be put in the train set, a float between [0;1]
```

both annotation file will be placed under the directory name `annotations`, file will be named `instances_train.json` and  `instances_test.json`, it is your wish to rename them or relocate them later on. 

## Example running 

``` 
python cocosplitter.py --annotation-file result.json --destination-dirtrain traindir --destination-dirtest testdir --split 0.9
```

Useful in the task of object detection when you want to follow the file organisation of https://github.com/Sense-X/Co-DETR/blob/main/README.md or https://github.com/facebookresearch/detr/blob/master/README.md
