# IMAGE PassThrough (Aegis72)
# this node takes an image as an input andpasses it through. It is used for remote
# targeting with an "Anything Everywhere" node sender

import sys
import torch

p310_plus = (sys.version_info >= (3, 10))

MANIFEST = {
    "name": "Aegisflow Utility Nodes",
    "version": (1,0,0),
    "author": "Aegis72",
    "project": "https://majorstudio.gumroad.com",
    "description": "UtilityNodes for Aegisflow comfyui workflow",
}


class aegisflow_image_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "image to pass": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image pass-->",)
    FUNCTION = "image_passer"
    CATEGORY = "AegisFlow"

    def _check_image_dimensions(self, tensors, names):
        dimensions = [tensor.shape for tensor in tensors]
        if len(set(dimensions)) > 1:
            mismatched_indices = [i for i, dim in enumerate(dimensions) if dim[1:] != dimensions[0][1:]]
            mismatched_images = [names[i] for i in mismatched_indices]
            if mismatched_images:
                raise ValueError(f"Image pass Warning: Input image dimensions do not match for images: {mismatched_images}")

    def image_passer(self, **kwargs):
        batched_tensors = [kwargs[key] for key in kwargs if kwargs[key] is not None]
        image_names = [key for key in kwargs if kwargs[key] is not None]

        if not batched_tensors:
            raise ValueError("AEGISFLOW IMAGE PASS MESSAGE: At least one input image must be provided. The most likely cause of this is that your image name in the passer node (blue) does not match the name you have in the black image pass node in your sampler. Check for typos; it must match the name exactly, or conform to a regex pattern.")

        self._check_image_dimensions(batched_tensors, image_names)
        batched_tensors = torch.cat(batched_tensors, dim=0)
        return (batched_tensors,) 

# LATENT PassThrough (Aegis72)
# this node takes an latent as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_latent_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "latent to pass": ("LATENT",),
            },
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent pass-->",)
    FUNCTION = "latent_passer"
    CATEGORY = "AegisFlow"
 
    def _check_image_dimensions(self, tensors, names):
        dimensions = [tensor.shape for tensor in tensors]
        if len(set(dimensions)) > 1:
            mismatched_indices = [i for i, dim in enumerate(dimensions) if dim[1:] != dimensions[0][1:]]
            mismatched_images = [names[i] for i in mismatched_indices]
            if mismatched_images:
                raise ValueError(f"Image pass Warning: Input image dimensions do not match for images: {mismatched_images}")
 
    def latent_passer(self, **kwargs):
        batched_tensors = [kwargs[key] for key in kwargs if kwargs[key] is not None]
        image_names = [key for key in kwargs if kwargs[key] is not None]

        if not batched_tensors:
            raise ValueError("AEGISFLOW IMAGE PASS MESSAGE: At least one input image must be provided. The most likely cause of this is that your image name in the passer node (blue) does not match the name you have in the black image pass node in your sampler. Check for typos; it must match the name exactly, or conform to a regex pattern.")

        self._check_image_dimensions(batched_tensors, image_names)
        batched_tensors = torch.cat(batched_tensors, dim=0)
        return (batched_tensors,) 

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Aegisflow Image Pass": aegisflow_latent_pass,
}



#---------------------------------------------------------------------------------------------------------------------#
#This is an input switch for Controlnet Preprocessors.  Can pick an input and that image will be the one picked for the workflow.
class af_preproc_chooser:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 9}),
            },
            "optional": {
                "c1_passthrough": ("IMAGE",),
                "c2_normal_lineart": ("IMAGE",),
                "c3_anime_lineart": ("IMAGE",),
                "c4_manga_lineart": ("IMAGE",),
                "c5_midas_depthmap": ("IMAGE",),
                "c6_color_palette": ("IMAGE",),
                "c7_canny_edge": ("IMAGE",),
                "c8_openpose_recognizer": ("IMAGE",), 
                "c9_scribble_lines": ("IMAGE",), 
                "c10_yourchoice1": ("IMAGE",), 
                "c11_yourchoice2": ("IMAGE",), 

            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "af_preproc_chooser"
    CATEGORY = "AegisFlow"    

    def af_preproc_chooser(self, Input, to_process=None,  c1_passthrough=None, c2_normal_lineart=None, c3_anime_lineart=None, c4_manga_lineart=None, c5_midas_depthmap=None, c6_color_palette=None, c7_canny_edge=None, c8_openpose_recognizer=None, c9_scribble_lines=None,c10_yourchoice1=None,c11_yourchoice2=None,):
        if Input == 1:
            return (c1_passthrough, )
        elif Input == 2:
            return (c2_normal_lineart, )
        elif Input == 3:
            return (c3_anime_lineart, )
        elif Input == 4:
            return (c4_manga_lineart, )
        elif Input == 5:
            return (c5_midas_depthmap, )
        elif Input == 6:
            return (c6_color_palette, )
        elif Input == 7:
            return (c7_canny_edge, )
        elif Input == 8:
            return (c8_openpose_recognizer, )                
        elif Input == 8:
            return (c9_scribble_lines, )  
        elif Input == 8:
            return (c10_yourchoice1, ) 
        else:
            return (c11_yourchoice2, )
        

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Aegisflow Image Pass": aegisflow_image_pass,
    "Aegisflow Latent  Pass": aegisflow_latent_pass,    
    "Aegisflow controlnet preprocessor bus": af_preproc_chooser,
}