# CrowdHuman for YOLO

[CrowdHuman](http://www.crowdhuman.org/download.html) dataset prepared for [darknet](https://github.com/AlexeyAB/darknet) implementation

Optional annotations were ignored, only visible boxes are used.  
All annotations are standartized to `<object-class> <x> <y> <width> <height>`, where:  

- `<object-class>` - string class of object from (person or mask)
- `<x> <y> <width> <height>` - float values relative to width and height of image, it can be set from 0.0 to 1.0
- for example: `<x> = <absolute_x> / <image_width>` or `<height> = <absolute_height> / <image_height>`
- **attention**: `<x> <y>` - is center of rectangle (not top left corner)

## Details

Annotation files are included in `/annotations` folder.  
Images are not part of this repo, please download it by yourself and put to matching folders:  
`/images_{suffix}`, where `{suffix}` is `test`, `train` or `val`

Algorithm creates `.txt` annotation file for each image (matching ID in each annotation row)  
Use `python3 main.py` to run script

### Requirements

Use `pip3 install -r requirements.txt` to install python dependencies
