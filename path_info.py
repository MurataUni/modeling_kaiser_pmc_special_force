import sys
sys.dont_write_bytecode = True

import os

class Const:
    dir_posture_json = os.sep.join([os.path.dirname(os.path.abspath(__file__)), '_postures'])

    folder_divided = 'divided'

    dir_parts_default = os.sep.join([os.path.dirname(os.path.abspath(__file__)), '_parts'])
    dir_parts_reverse = os.sep.join([os.path.dirname(os.path.abspath(__file__)), '_parts_reversed'])
    dirs_parts = [
        dir_parts_default,
        dir_parts_reverse,
    ]
    dir_parts_renamed = os.sep.join([os.path.dirname(os.path.abspath(__file__)), '_parts_renamed', folder_divided])
    
    file_posture_model_default = 'model.json'
    file_posture_model_posed = 'model_posed.json'

def output_list():
    file_absdir = os.path.dirname(os.path.abspath(__file__))
    output = {
        "model": {
            "parts": os.path.join(file_absdir, Const.dir_parts_renamed),
            "default": os.path.join(Const.dir_posture_json, Const.file_posture_model_default),
        },
    }
    file_full_name =  os.sep.join([os.path.dirname(os.path.abspath(__file__)), 'path_list.txt'])
    f = open(file_full_name, "w", encoding="ascii")
    for name, path_dict in output.items():
        f.write("[" + name + "]\n")
        max_path_name = len(max(path_dict.keys(), key=len))
        for path_name, path_value in path_dict.items():
            f.write(path_name.ljust(max_path_name, ' ') + ": " + path_value + "\n")
        f.write("\n")
    f.close()

if __name__ == "__main__":
    output_list()
