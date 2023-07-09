import json
import random
import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Split Coco annotation file and image file into training and test set') 
parser.add_argument('--annotation-file',type=str,required=True,dest="annot", help="Name of the file containing Coco annotations")
parser.add_argument('--destination-dirtrain',type=str,required=True,dest="desttrain", help="Name of the directory that will contain the train set images")
parser.add_argument('--destination-dirtest',type=str,required=True,dest="desttest", help="Name of the directory that will contain the test set images")
parser.add_argument('--split',type=float,required=True,dest="split", help="Percentage of data that will be put in the train set, a float between [0;1]")

args = parser.parse_args()

def main(args):
    
    with open(args.annot,'r') as f:
        coco = json.load(f)
        try:
            categories = coco['categories']
            images = coco['images']
            annotations = coco['annotations']
            infos = coco['info']
        except:
            pass
        
    nb_images = len(images)
    image_index = list(range(nb_images))
    random.shuffle(image_index)
    train_indexes = image_index[:int(nb_images*args.split)]
    test_indexes = image_index[int(nb_images*args.split):]
    
    # for annotations files
    train_images = [images[i] for i in train_indexes]
    test_images = [images[i] for i in test_indexes]
    
    tr_images = []
    for elem in train_images:
        if 'image' in elem['file_name']:
            elem['file_name'] = elem['file_name'][7:]
            tr_images.append(elem)
        else :
            tr_images.append(elem)
            
    te_images = []
    for elem in test_images:
        if 'image' in elem['file_name']:
            elem['file_name'] = elem['file_name'][7:]
            te_images.append(elem)
        else :
            te_images.append(elem)

    train_annotations = [annot for i in train_indexes for annot in annotations if annot['image_id'] == i]
    test_annotations = [annot for i in test_indexes for annot in annotations if annot['image_id'] == i]
    
    if infos : 
        result_train = {'images':train_images, 'categories':categories, 'annnotations':train_annotations, 'info':infos}
        result_test = {'images':test_images, 'categories':categories, 'annnotations':test_annotations, 'info':infos}
    else :
        result_train = {'images':train_images, 'categories':categories, 'annnotations':train_annotations}
        result_test = {'images':test_images, 'categories':categories, 'annnotations':test_annotations}
    
    os.mkdir('annotations')
    with open('annotations/instances_train.json','w') as f:
        json.dump(result_test,f,indent=4)
    
    with open('annotations/instances_test.json','w') as f:
        json.dump(result_test,f,indent=4)
    
    # for images files
    os.mkdir(args.desttrain)
    [shutil.copy(f'{filename}',args.desttrain) for filename in [tr['file_name'] for tr in train_images]]

    os.mkdir(args.desttest)
    [shutil.copy(f'{filename}',args.desttest) for filename in [tr['file_name'] for tr in test_images]]

if __name__=="__main__":
    main(args)
    
