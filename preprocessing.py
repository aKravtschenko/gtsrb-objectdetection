import os 
import xml.etree.ElementTree as ET

def convert_box(size, box):
    dw, dh = 1. / size[0], 1. / size[1]
    x, y, w, h = (box[0] + box[1]) / 2.0 - 1, (box[2] + box[3]) / 2.0 - 1, box[1] - box[0], box[3] - box[2]
    return x * dw, y * dh, w * dw, h * dh


def convert_voc_to_yolo(annotation_dir, output_dir, class_names):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for anno in os.listdir(annotation_dir):
        if anno.endswith('.xml'):
            file_name = os.path.splitext(anno)[0]
            out_file = open(os.path.join(output_dir, f'{file_name}.txt'), 'w')

            tree = ET.parse(os.path.join(annotation_dir, anno))
            root = tree.getroot()
            size = root.find('size')        
            w = int(size.find('width').text)
            h = int(size.find('height').text)

            for obj in root.iter('object'):
                cls = obj.find('name').text
                if cls in class_names and int(obj.find('difficult').text) != 1:
                    xmlbox = obj.find('bndbox')
                    bb = convert_box((w, h), [float(xmlbox.find(x).text) for x in ('xmin', 'xmax', 'ymin', 'ymax')])
                    cls_id = class_names.index(cls)  # class id
                    out_file.write(" ".join([str(a) for a in (cls_id, *bb)]) + '\n')