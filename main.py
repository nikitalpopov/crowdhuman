import json
import os
import pandas as pd
from pprint import pprint
from PIL import Image

cwd = os.getcwd()

def generate_annotations(filename):
    with open(f"{cwd}/annotations/{filename}", 'r') as file:
        suffix = filename.split('.')[0].split('_')[1]

        data = file.read()
        lines = data.split('\n')
        annotations = []
        for line in lines:
            try:
                annotations.append(json.loads(line))
            except:
                pass

        images = []
        for annotation in annotations:
            image = {}
            image['id'] = annotation['ID']

            picture = Image.open(f"{cwd}/images_{suffix}/{image['id']}.jpg")
            width, height = picture.size
            image['annotations'] = [
                {
                    'tag': box['tag'],
                    'x': float(box['vbox'][0] + 0.5 * float(box['vbox'][2])) / float(width),
                    'y': float(box['vbox'][1] + 0.5 * float(box['vbox'][3])) / float(height),
                    'w': float(box['vbox'][2]) / float(width),
                    'h': float(box['vbox'][3]) / float(height)
                } for box in annotation['gtboxes']]
            images.append(image)
            with open(f"{cwd}/results/{image['id']}.txt", 'w') as output:
                output.writelines([f"{line['tag']} {line['x']} {line['y']} {line['w']} {line['h']}\n" for line in image['annotations']])


if __name__ == '__main__':
    list = os.listdir(f"{cwd}/annotations/")
    try:
        list.remove('.DS_Store')  # for macOS
    except:
        pass
    for filename in list:
        print(filename)
        generate_annotations(filename)
