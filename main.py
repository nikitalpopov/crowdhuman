import json
import os
import pandas as pd
from pprint import pprint
from PIL import Image

cwd = os.getcwd()

pictures = {
    'test': [],
    'train': [],
    'val': []
}
classes = []

def generate_annotations(filename, classes, pictures):
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
            image = { 'annotations': [] }
            image['id'] = annotation['ID']
            pictures[suffix].append(image['id'])

            picture = Image.open(f"{cwd}/images_{suffix}/{image['id']}.jpg")
            width, height = picture.size

            for box in annotation['gtboxes']:
                tag = box['tag'].strip().lower()
                classes.append(tag)
                classes = list(dict.fromkeys(classes))
                image['annotations'].append({
                    'tag': classes.index(tag),
                    'x': float(box['vbox'][0] + 0.5 * float(box['vbox'][2])) / float(width),
                    'y': float(box['vbox'][1] + 0.5 * float(box['vbox'][3])) / float(height),
                    'w': float(box['vbox'][2]) / float(width),
                    'h': float(box['vbox'][3]) / float(height)
                })

            images.append(image)
            with open(f"{cwd}/images_{suffix}/{image['id']}.txt", 'w') as output:
                output.writelines([f"{line['tag']} {line['x']} {line['y']} {line['w']} {line['h']}\n" for line in image['annotations']])



if __name__ == '__main__':
    files = os.listdir(f"{cwd}/annotations/")
    try:
        files.remove('.DS_Store')  # for macOS
    except:
        pass
    for filename in files:
        print(filename)
        generate_annotations(filename, classes, pictures)

    with open(f"{cwd}/results/classes.names", 'w') as objects:
        objects.writelines("\n".join(classes))

    for suffix in pictures.keys():
        with open(f"{cwd}/results/{suffix}.txt", 'w') as dataset:
            [dataset.write(f"./images_{suffix}/{path}.jpg\n") for path in pictures[suffix]]
