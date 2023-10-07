import sys
sys.dont_write_bytecode = True

import numpy as np
import os

from harbor3d.specification import Spec
from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

from path_info import Const as PathInfo

class Const:

    bone_default_len = 10.
    bone_default_small_len = 1.

    bone_length = {
        "base": 10.,
        "body_lower": bone_default_len, # parts body
        "body_spine": bone_default_len,
        "body_upper": bone_default_len,
        "neck_collar": bone_default_small_len,  # parts head
        "neck_cylinder_left": bone_default_len,
        "neck_cylinder_right": bone_default_len,
        "neck_spine_1": bone_default_len,
        "neck_spine_2": bone_default_len,
        "head": bone_default_len,
        "shoulder_adapter_r": bone_default_len, # parts arm right
        "upper_arm_r": bone_default_len,
        "elbow_r": bone_default_len,
        "forearm_r": bone_default_len,
        "palm_r": bone_default_len,
        "shoulder_adapter_l": bone_default_len, # parts arm left
        "upper_arm_l": bone_default_len,
        "elbow_l": bone_default_len,
        "forearm_l": bone_default_len,
        "palm_l": bone_default_len,
        "thigh_r": bone_default_len, # parts leg right
        "shin_r": bone_default_len,
        "shin_cover_r": bone_default_len,
        "foot_cylinder_r": bone_default_len,
        "foot_r": bone_default_len,
        "toe_r": bone_default_len,
        "thigh_l": bone_default_len, # parts leg left
        "shin_l": bone_default_len,
        "shin_cover_l": bone_default_len,
        "foot_cylinder_l": bone_default_len,
        "foot_l": bone_default_len,
        "toe_l": bone_default_len,
        "thumb_proximal_phalanx_r": bone_default_small_len, # parts hand right
        "thumb_distal_phalanx_r": bone_default_small_len,
        "index_f_proximal_phalanx_r": bone_default_small_len,
        "index_f_middle_phalanx_r": bone_default_small_len,
        "index_f_distal_phalanx_r": bone_default_small_len,
        "middle_f_proximal_phalanx_r": bone_default_small_len,
        "middle_f_middle_phalanx_r": bone_default_small_len,
        "middle_f_distal_phalanx_r": bone_default_small_len,
        "ring_f_proximal_phalanx_r": bone_default_small_len,
        "ring_f_middle_phalanx_r": bone_default_small_len,
        "ring_f_distal_phalanx_r": bone_default_small_len,
        "little_f_proximal_phalanx_r": bone_default_small_len,
        "little_f_middle_phalanx_r": bone_default_small_len,
        "little_f_distal_phalanx_r": bone_default_small_len,
        "thumb_proximal_phalanx_l": bone_default_small_len, # parts hand left
        "thumb_distal_phalanx_l": bone_default_small_len,
        "index_f_proximal_phalanx_l": bone_default_small_len,
        "index_f_middle_phalanx_l": bone_default_small_len,
        "index_f_distal_phalanx_l": bone_default_small_len,
        "middle_f_proximal_phalanx_l": bone_default_small_len,
        "middle_f_middle_phalanx_l": bone_default_small_len,
        "middle_f_distal_phalanx_l": bone_default_small_len,
        "ring_f_proximal_phalanx_l": bone_default_small_len,
        "ring_f_middle_phalanx_l": bone_default_small_len,
        "ring_f_distal_phalanx_l": bone_default_small_len,
        "little_f_proximal_phalanx_l": bone_default_small_len,
        "little_f_middle_phalanx_l": bone_default_small_len,
        "little_f_distal_phalanx_l": bone_default_small_len,
        "weapon_r": bone_default_len, # parts weapon right
    }

    bones = bone_length.keys()

    alias = {
        "neck_cylinder_left": "neck_cylinder",
        "neck_cylinder_right": "neck_cylinder",
        "neck_spine_1": "neck_spine",
        "neck_spine_2": "neck_spine",
        "shoulder_adapter_r": "shoulder_adapter",
        "shoulder_adapter_l": "shoulder_adapter",
        "elbow_r": "elbow",
        "elbow_l": "elbow",
        "shin_cover_r": "shin_cover",
        "foot_cylinder_r": "foot_cylinder",
        "shin_cover_l": "shin_cover",
        "foot_cylinder_l": "foot_cylinder",
        "thumb_proximal_phalanx_r": "thumb_proximal_phalanx",
        "thumb_distal_phalanx_r": "thumb_distal_phalanx",
        "index_f_proximal_phalanx_r": "f_proximal_phalanx",
        "index_f_middle_phalanx_r": "f_middle_phalanx",
        "index_f_distal_phalanx_r": "f_distal_phalanx",
        "middle_f_proximal_phalanx_r": "f_proximal_phalanx",
        "middle_f_middle_phalanx_r": "f_middle_phalanx",
        "middle_f_distal_phalanx_r": "f_distal_phalanx",
        "ring_f_proximal_phalanx_r": "f_proximal_phalanx",
        "ring_f_middle_phalanx_r": "f_middle_phalanx",
        "ring_f_distal_phalanx_r": "f_distal_phalanx",
        "little_f_proximal_phalanx_r": "f_proximal_phalanx",
        "little_f_middle_phalanx_r": "f_middle_phalanx",
        "little_f_distal_phalanx_r": "f_distal_phalanx",
        "thumb_proximal_phalanx_l": "thumb_proximal_phalanx",
        "thumb_distal_phalanx_l": "thumb_distal_phalanx",
        "index_f_proximal_phalanx_l": "f_proximal_phalanx",
        "index_f_middle_phalanx_l": "f_middle_phalanx",
        "index_f_distal_phalanx_l": "f_distal_phalanx",
        "middle_f_proximal_phalanx_l": "f_proximal_phalanx",
        "middle_f_middle_phalanx_l": "f_middle_phalanx",
        "middle_f_distal_phalanx_l": "f_distal_phalanx",
        "ring_f_proximal_phalanx_l": "f_proximal_phalanx",
        "ring_f_middle_phalanx_l": "f_middle_phalanx",
        "ring_f_distal_phalanx_l": "f_distal_phalanx",
        "little_f_proximal_phalanx_l": "f_proximal_phalanx",
        "little_f_middle_phalanx_l": "f_middle_phalanx",
        "little_f_distal_phalanx_l": "f_distal_phalanx",
    }

def main():
    fnames = [PathInfo.file_posture_model_default, PathInfo.file_posture_model_posed]
    for fname in fnames:
        apply_const(os.path.join(PathInfo.dir_posture_json,fname))

def apply_const(posture_file):
    json_loader = JsonLoader(posture_file)
    pw = PostureWrapper(json_loader.fetch())
    for key in Const.bone_length.keys():
        if pw.has_key(key):
            pw.set_length(key, Const.bone_length[key])

    json_loader.dictionary = pw.postures
    json_loader.dump()
    
if __name__ == "__main__":
    main()
