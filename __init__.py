# IMAGE PassThrough (Aegis72)
# this node takes an image as an input andpasses it through. It is used for remote
# targeting with an "Anything Everywhere" node sender

import sys
import torch
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from PIL import Image
import subprocess
import math

p310_plus = (sys.version_info >= (3, 10))

MANIFEST = {
    "name": "Aegisflow Utility Nodes",
    "version": (1, 1, 0),
    "author": "Aegis72",
    "project": "https://majorstudio.gumroad.com",
    "description": "UtilityNodes for Aegisflow comfyui workflow, based heavily on WASquatch's image batch node",
}

#Passer for SDXL

class aegisflow_multi_passxl:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
                "latent": ("LATENT",),
                "model": ("MODEL",),                
                "vae": ("VAE",),
                "clip": ("CLIP",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "refiner model":("MODEL",),
                "refiner clip":("CLIP",),
                "refiner positive":("CONDITIONING",),
                "refiner negative":("CONDITIONING",),
                "sdxl tuple": ("SDXL_TUPLE",),
            },
        }

    RETURN_TYPES = ("IMAGE", "MASK", "LATENT", "MODEL", "VAE", "CLIP", "CONDITIONING", "CONDITIONING", "MODEL", "CLIP", "CONDITIONING", "CONDITIONING", "SDXL_TUPLE",)
    RETURN_NAMES = ("image", "mask", "latent", "model", "vae", "clip", "positive", "negative", "refiner model", "refiner clip", "refiner positive", "refiner negative", "sdxl tuple",)
    FUNCTION = "af_passnodesxl"
    CATEGORY = "AegisFlow/passers"

    def af_passnodesxl(self, **kwargs):
        output_order = ("image", "mask", "latent", "model", "vae", "clip", "positive", "negative", "refiner model", "refiner clip", "refiner positive", "refiner negative", "sdxl tuple",)
        return [kwargs.setdefault(key, '0') for key in output_order]
    

#Passer for SD 1.5

class aegisflow_multi_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
                "latent": ("LATENT",),
                "model": ("MODEL",),                
                "vae": ("VAE",),
                "clip": ("CLIP",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "sdxl tuple": ("SDXL_TUPLE",),

            },
        }

    RETURN_TYPES = ("IMAGE", "MASK", "LATENT", "MODEL", "VAE", "CLIP", "CONDITIONING", "CONDITIONING", "SDXL_TUPLE",)
    RETURN_NAMES = ("image", "mask", "latent", "model", "vae", "clip", "positive", "negative", "sdxl tuple",)
    FUNCTION = "af_passnodes"
    CATEGORY = "AegisFlow/passers"

    def af_passnodes(self, **kwargs):
        output_order = ("image", "mask", "latent", "model", "vae", "clip", "positive", "negative", "sdxl tuple",)
        return [kwargs.setdefault(key, '0') for key in output_order]


# model PassThrough (Aegis72)
# this node takes a model as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_model_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "model": ("MODEL",),
            },
        }

    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "model_passer"
    CATEGORY = "AegisFlow/passers"

    def model_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None] 

# model PassThrough (Aegis72)
# this node takes a model as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_clip_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "clip": ("CLIP",),
            },
        }

    RETURN_TYPES = ("CLIP",)
    RETURN_NAMES = ("clip",)
    FUNCTION = "clip_passer"
    CATEGORY = "AegisFlow/passers"

    def clip_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None] 


# vae PassThrough (Aegis72)
# this node takes a vae as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_vae_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "vae": ("VAE",),
            },
        }

    RETURN_TYPES = ("VAE",)
    RETURN_NAMES = ("vae",)
    FUNCTION = "vae_passer"
    CATEGORY = "AegisFlow/passers"

    def vae_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None] 


class aegisflow_image_pass:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "image": ("IMAGE",),
                "mask": ("MASK",),    
            },
        }

    RETURN_TYPES = ("IMAGE", "MASK",)
    RETURN_NAMES = ("image", "mask",)
    FUNCTION = "image_passer"
    CATEGORY = "AegisFlow/passers"

    def image_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None]  


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
                "latent": ("LATENT",),
            },
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "latent_passer"
    CATEGORY = "AegisFlow/passers"

    def latent_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None]  

# MASK PassThrough (Aegis72)
# this node takes a mask as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_mask_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "mask": ("MASK",),
            },
        }

    RETURN_TYPES = ("MASK",)
    RETURN_NAMES = ("mask",)
    FUNCTION = "mask_passer"
    CATEGORY = "AegisFlow/passers"

    def mask_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None] 

# PosNeg PassThrough (Aegis72)
# this node takes CLIP as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_posneg_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
            },
        }

    RETURN_TYPES = ("CONDITIONING","CONDITIONING",)
    RETURN_NAMES = ("positive","negative",)
    FUNCTION = "posneg_passer"
    CATEGORY = "AegisFlow/passers"

    def posneg_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None] 

# Conditioning PassThrough (Aegis72)
# this node takes CONDITIONING as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_cond_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "conditioning": ("CONDITIONING",),
            },
        }

    RETURN_TYPES = ("CONDITIONING",)
    RETURN_NAMES = ("conditioning",)
    FUNCTION = "conditioning_passer"
    CATEGORY = "AegisFlow/passers"

    def conditioning_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None] 
    
# SDXL Tuple PassThrough (Aegis72)
# this node takes CONDITIONING as an input and passes it through. It is used for remote
# targeting with an "Anything Everywhere" node sender


class aegisflow_sdxltuple_pass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "sdxl tuple": ("SDXL_TUPLE",),
            },
        }

    RETURN_TYPES = ("SDXL_TUPLE",)
    RETURN_NAMES = ("sdxl tuple",)
    FUNCTION = "tuple_passer"
    CATEGORY = "AegisFlow/passers"

    def tuple_passer(self, **kwargs):
        return [kwargs[key] for key in kwargs if kwargs[key] is not None]


# ---------------------------------------------------------------------------------------------------------------------#
# This is an input switch for Controlnet Preprocessors.  Can pick an input and that image will be the one picked for the workflow.
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
    CATEGORY = "AegisFlow/passers"

    def af_preproc_chooser(self, Input, to_process=None, c1_passthrough=None, c2_normal_lineart=None, c3_anime_lineart=None, c4_manga_lineart=None, c5_midas_depthmap=None, c6_color_palette=None, c7_canny_edge=None, c8_openpose_recognizer=None, c9_scribble_lines=None, c10_yourchoice1=None, c11_yourchoice2=None,):
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
        elif Input == 9:
            return (c9_scribble_lines, )
        elif Input == 10:
            return (c10_yourchoice1, )
        else:
            return (c11_yourchoice2, )

# Developed by Ally - https://www.patreon.com/theally
# https://civitai.com/user/theally

# This node provides a simple interface to adjust the brightness/contrast of the output image prior to saving
# many users were having difficulties with both installing and keeping theAlly nodes consistent and so I am integrating the three required them into this node set.


class BrightnessContrast_theAlly:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types

        """
        return {
            "required": {
                "image": ("IMAGE",),
                "mode": (["brightness", "contrast"],),
                "strength": ("FLOAT", {"default": 0.5, "min": -1.0, "max": 1.0, "step": 0.01}),
                "enabled": ("BOOLEAN", {"default": True},),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_filter"

    CATEGORY = "AegisFlow/fx"

    def apply_filter(self, image, mode, strength, enabled):
        # Choose a filter based on the 'mode' value
        if enabled:
            if mode == "brightness":
                image = np.clip(image + strength, 0.0, 1.0)
            elif mode == "contrast":
                image = np.clip(image * strength, 0.0, 1.0)
            else:
                print(f"Invalid filter option: {mode}. No changes applied.")
        return (image,)


# Developed by Ally - https://www.patreon.com/theally
# https://civitai.com/user/theally

# This node provides a simple interface to flip the image horizontally or vertically prior to saving

class ImageFlip_theAlly:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "flip_type": (["horizontal", "vertical"],),
                "enabled": ("BOOLEAN", {"default": True},),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "flip_image"
    CATEGORY = "AegisFlow/fx"

    def flip_image(self, image, flip_type, enabled):

        # Convert the input image tensor to a NumPy array
        image_np = 255. * image.cpu().numpy().squeeze()

        if not enabled:
            return (image,)

        if flip_type == "horizontal":
            flipped_image_np = np.flip(image_np, axis=1)
        elif flip_type == "vertical":
            flipped_image_np = np.flip(image_np, axis=0)
        else:
            print("Invalid flip_type. Must be either 'horizontal' or 'vertical'. No changes applied.")
            return (image,)
        # Convert the flipped NumPy array back to a tensor
        flipped_image_np = flipped_image_np.astype(np.float32) / 255.0
        flipped_image_tensor = torch.from_numpy(flipped_image_np).unsqueeze(0)

        return (flipped_image_tensor,)


# Developed by Ally - https://www.patreon.com/theally
# https://civitai.com/user/theally

# This node provides a simple interface to apply a gaussian blur approximation (with box blur) to the image prior to output

class GaussianBlur_theAlly:
    """
    This node provides a simple interface to apply Gaussian blur to the output image.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {
            "required": {
                "image": ("IMAGE",),
                "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 200.0, "step": 0.01}),
                "enabled": ("BOOLEAN", {"default": True},),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_filter"

    CATEGORY = "AegisFlow/fx"

    def apply_filter(self, image, strength, enabled):

        if not enabled:
            return (image,)

        i = 255. * image.cpu().numpy().squeeze()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

        # Apply Gaussian blur using the strength value
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius=strength))

        # Convert the blurred PIL Image back to a tensor
        blurred_image_np = np.array(blurred_img).astype(np.float32) / 255.0
        blurred_image_tensor = torch.from_numpy(blurred_image_np).unsqueeze(0)
        return (blurred_image_tensor,)


class af_placeholdertuple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {}}

    RETURN_TYPES = ("SDXL_TUPLE",)
    FUNCTION = "placeholdertuple"
    CATEGORY = "AegisFlow/placeholders"

    def placeholdertuple(self,):

        provided_tuple_string = "(<comfy.model_patcher.ModelPatcher object at 0x00000215AF92E410>, " \
                                "<comfy.sd.CLIP object at 0x0000021582576110>, " \
                                "[[tensor([[[-0.3921,  0.0278, -0.0675,  ..., -0.4916, -0.3165,  0.0655], " \
                                "[-0.6300, -0.3306,  0.3012,  ...,  0.2379, -0.3163,  0.4271], " \
                                "[ 0.2102,  0.3428,  0.3694,  ..., -1.1688, -1.4279, -0.7521], " \
                                "..., " \
                                "[-0.3279, -0.1775, -1.6074,  ..., -0.3802, -1.1385, -0.0408], " \
                                "[-0.3222, -0.1721, -1.5919,  ..., -0.3691, -1.1436, -0.0270], " \
                                "[-0.3520, -0.0728, -1.5434,  ..., -0.3932, -1.0915, -0.0713]]]), {'pooled_output': None}]], " \
                                "[[tensor([[[-0.3921,  0.0278, -0.0675,  ..., -0.4916, -0.3165,  0.0655], " \
                                "[-0.6300, -0.3306,  0.3012,  ...,  0.2379, -0.3163,  0.4271], " \
                                "[ 0.2102,  0.3428,  0.3694,  ..., -1.1688, -1.4279, -0.7521], " \
                                "..., " \
                                "[-0.2891, -0.6821, -1.5167,  ..., -0.6290, -1.7984,  0.3385], " \
                                "[-0.2864, -0.6799, -1.5096,  ..., -0.6233, -1.7977,  0.3522], " \
                                "[-0.2866, -0.5871, -1.4560,  ..., -0.6451, -1.7306,  0.2990]]]), {'pooled_output': None}]], " \
                                "None, None, None, None)"
        result = tuple(provided_tuple_string.split(", "))
        return (result,)
    
class af_pipe_in_15:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
            "optional": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
                "latent": ("LATENT",),
                "model": ("MODEL",),                
                "vae": ("VAE",),
                "clip": ("CLIP",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "imagewidth": ("INT", {"default": 512, "min": 64, "max": 0xffffffffffffffff, "forceInput": True}),
                "imageheight": ("INT", {"default": 512, "min": 64, "max": 0xffffffffffffffff, "forceInput": True}),
                "latentwidth": ("INT", {"default": 512, "min": 64, "max": 0xffffffffffffffff, "forceInput": True}),
                "latentheight": ("INT", {"default": 512, "min": 64, "max": 0xffffffffffffffff, "forceInput": True}),
            },
        }

    RETURN_TYPES = ("PIPE_LINE", "STRING", )
    RETURN_NAMES = ("pipe", "discord", )
    FUNCTION = "af_pipe_in"
    CATEGORY = "AegisFlow/passers"

    def af_pipe_in(self, image=0, mask=0, latent=0, model=0, vae=0, clip=0, positive=0, negative=0, image_width=0, image_height=0, latent_width=0, latent_height=0):
        discord = "https://discord.gg/fVQB2XAKTM"
        pipe_line = (image, mask, latent, model, vae, clip, positive, negative, image_width, image_height, latent_width, latent_height)

        return (pipe_line, discord, )
    
class af_pipe_out_15:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"pipe": ("PIPE_LINE",)},
        }

    RETURN_TYPES = ("PIPE_LINE", "IMAGE", "MASK", "LATENT", "MODEL", "VAE", "CLIP", "CONDITIONING", "CONDITIONING", "INT", "INT", "INT", "INT", "STRING", )
    RETURN_NAMES = ("pipe", "image", "mask", "latent", "model", "vae", "clip", "positive", "negative", "image_width", "image_height", "latent_width", "latent_height", "discord link", )
    FUNCTION = "af_pipe_out"
    CATEGORY = "AegisFlow/passers"

    def af_pipe_out(self, pipe):
        discord = "https://discord.gg/fVQB2XAKTM"
        image, mask, latent, model, vae, clip, positive, negative, image_width, image_height, latent_width, latent_height = pipe

        return (pipe, image, mask, latent, model, vae, clip, positive, negative, image_width, image_height, latent_width, latent_height, discord, )
    
class af_pipe_in_xl:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
            "optional": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
                "sdxl_tuple": ("SDXL_TUPLE",),
                "latent": ("LATENT",),
                "model": ("MODEL",),                
                "vae": ("VAE",),
                "clip": ("CLIP",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "refiner_model": ("MODEL",),
                "refiner_vae": ("VAE",),                                
                "refiner_clip": ("CLIP",),
                "refiner_positive": ("CONDITIONING",),
                "refiner_negative": ("CONDITIONING",),                
                "imagewidth": ("INT", {"default": 1024, "min": 64, "max": 0xffffffffffffffff, "forceInput": True}),
                "imageheight": ("INT", {"default": 1024, "min": 64, "max": 0xffffffffffffffff, "forceInput": True}),
                "latentwidth": ("INT", {"default": 1024, "min": 64, "max": 0xffffffffffffffff, "forceInput": True}),
                "latentheight": ("INT", {"default": 1024, "min": 64, "max": 0xffffffffffffffff, "forceInput": True}),
            },
        }

    RETURN_TYPES = ("PIPE_LINE", "STRING", )
    RETURN_NAMES = ("pipe", "discord", )
    FUNCTION = "af_pipe_in_xl"
    CATEGORY = "AegisFlow/passers"

    def af_pipe_in_xl(self, image=0, sdxl_tuple=0, mask=0, latent=0, model=0, vae=0, clip=0, positive=0, negative=0, refiner_model=0, refiner_vae=0, refiner_clip=0, refiner_positive=0, refiner_negative=0, image_width=0, image_height=0, latent_width=0, latent_height=0):
        discord = "https://discord.gg/fVQB2XAKTM"
        pipe_line = (image, mask, sdxl_tuple, latent, model, vae, clip, positive, negative, refiner_model, refiner_vae, refiner_clip, refiner_positive, refiner_negative, image_width, image_height, refiner_negative, latent_width, latent_height)

        return (pipe_line, discord, )
    
class af_pipe_out_xl:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"pipe": ("PIPE_LINE",)},
        }

    RETURN_TYPES = ("IMAGE", "MASK", "SDXL_TUPLE", "LATENT", "MODEL", "VAE", "CLIP", "CONDITIONING", "CONDITIONING", "MODEL", "VAE", "CLIP", "CONDITIONING", "CONDITIONING", "INT", "INT", "INT", "INT", "STRING", )
    RETURN_NAMES = ("image", "mask", "sdxl_tuple", "latent", "model", "vae", "clip", "positive", "negative", "refiner_model", "refiner_vae", "refiner_clip", "refiner_positive", "refiner_negative", "image_width", "image_height", "latent_width", "latent_height", "discord link", )
    FUNCTION = "af_pipe_out_xl"
    CATEGORY = "AegisFlow/passers"

    def af_pipe_out_xl(self, pipe):
        discord = "https://discord.gg/fVQB2XAKTM"
        image, mask, sdxl_tuple, latent, model, vae, clip, positive, negative, refiner_model, refiner_vae, refiner_clip, refiner_positive, refiner_negative, image_width, image_height, refiner_negative, latent_width, latent_height = pipe

        return (image, mask, sdxl_tuple, latent, model, vae, clip, positive, negative, refiner_model, refiner_vae, refiner_clip, refiner_positive, refiner_negative, image_width, image_height, refiner_negative, latent_width, latent_height, discord, )

# Vextra Nodes; These are having issues being imported due to some errors occurring on the original nodes; maintainer has not been available to fix the issue and as such we are including them here
# with full credit to the original developer diontimmer. Not all of their nodes are present, but just the ones we use:
    
class Flatten_Colors():
    """
    This node provides a simple interface to apply PixelSort blur to the output image.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {
            "required": {
                "images": ("IMAGE",),},
            "optional": {
                "number_of_colors": ("INT", {"default": 5, "min": 1, "max": 4000, "step": 1}),
                },
            }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "flatten"

    CATEGORY = "AegisFlow/fx"

    def tensor_to_pil(self, img):
        if img is not None:
            i = 255. * img.cpu().numpy().squeeze()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        return img

    def flatten(self, images, number_of_colors):
        #create empty tensor with the same shape as images
        total_images = []
        for image in images:
            image = self.tensor_to_pil(image)
            image = image.convert('P', palette=Image.ADAPTIVE, colors=number_of_colors)
            
            # convert to tensor
            out_image = np.array(image.convert("RGB")).astype(np.float32) / 255.0
            out_image = torch.from_numpy(out_image).unsqueeze(0)
            total_images.append(out_image)


        total_images = torch.cat(total_images, 0)
        return (total_images,)


def or_convert(im, mode):
    return im if im.mode == mode else im.convert(mode)

def hue_rotate(im, deg=0):
    cos_hue = math.cos(math.radians(deg))
    sin_hue = math.sin(math.radians(deg))

    matrix = [
        .213 + cos_hue * .787 - sin_hue * .213,
        .715 - cos_hue * .715 - sin_hue * .715,
        .072 - cos_hue * .072 + sin_hue * .928,
        0,
        .213 - cos_hue * .213 + sin_hue * .143,
        .715 + cos_hue * .285 + sin_hue * .140,
        .072 - cos_hue * .072 - sin_hue * .283,
        0,
        .213 - cos_hue * .213 - sin_hue * .787,
        .715 - cos_hue * .715 + sin_hue * .715,
        .072 + cos_hue * .928 + sin_hue * .072,
        0,
    ]

    rotated = or_convert(im, 'RGB').convert('RGB', matrix)
    return or_convert(rotated, im.mode)


class HueRotation():

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {
            "required": {
                "images": ("IMAGE",),},
            "optional": {
                "hue_rotation": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 360.0, "step": 0.1}),
                },
            }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_hr"

    CATEGORY = "AegisFlow/fx"

    def tensor_to_pil(self, img):
        if img is not None:
            i = 255. * img.cpu().numpy().squeeze()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        return img

    def apply_hr(self, images, hue_rotation):
        #create empty tensor with the same shape as images
        total_images = []
        for image in images:
            image = self.tensor_to_pil(image)
            image = hue_rotate(image, hue_rotation)
            # convert to tensor
            out_image = np.array(image.convert("RGB")).astype(np.float32) / 255.0
            out_image = torch.from_numpy(out_image).unsqueeze(0)
            total_images.append(out_image)


        total_images = torch.cat(total_images, 0)
        return (total_images,)


COLOR_MODES = {
    'RGB': 'RGB',
    'RGBA': 'RGBA',
    'luminance': 'L',
    'luminance_alpha': 'LA',
    'cmyk': 'CMYK',
    'ycbcr': 'YCbCr',
    'lab': 'LAB',
    'hsv': 'HSV',
    'single_channel': '1',
}

class Swap_Color_Mode():
    """
    This node provides a simple interface to apply PixelSort blur to the output image.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {
            "required": {
                "images": ("IMAGE",),},
            "optional": {
                "color_mode": (['default', 'luminance', 'single_channel', 'RGB', 'RGBA', 'lab', 'hsv', 'cmyk', 'ycbcr'],),
                },
            }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "do_swap"

    CATEGORY = "AegisFlow/fx"

    def tensor_to_pil(self, img):
        if img is not None:
            i = 255. * img.cpu().numpy().squeeze()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        return img

    def do_swap(self, images, color_mode='default'):
        total_images = []
        for image in images:
            image = self.tensor_to_pil(image)
            if color_mode != 'default':
                correct_color_mode = COLOR_MODES[color_mode]
                image = image.convert(correct_color_mode)
            # convert to tensor
            out_image = np.array(image).astype(np.float32) / 255.0
            out_image = torch.from_numpy(out_image).unsqueeze(0)
            total_images.append(out_image)


        total_images = torch.cat(total_images, 0)
        return (total_images,)


try:
    import pilgram
except ModuleNotFoundError:
    # install pixelsort in current venv
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pilgram"])
    import pilgram

class ApplyFilter():

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {
            "required": {
                "images": ("IMAGE",),},
            "optional": {
                "instagram_filter": ([
                        "_1977",
                        "aden",
                        "brannan",
                        "brooklyn",
                        "clarendon",
                        "earlybird",
                        "gingham",
                        "hudson",
                        "inkwell",
                        "kelvin",
                        "lark",
                        "lofi",
                        "maven",
                        "mayfair",
                        "moon",
                        "nashville",
                        "perpetua",
                        "reyes",
                        "rise",
                        "slumber",
                        "stinson",
                        "toaster",
                        "valencia",
                        "walden",
                        "willow",
                        "xpro2",
                            ],),
                },
            }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_filter"

    CATEGORY = "AegisFlow/fx"

    def tensor_to_pil(self, img):
        if img is not None:
            i = 255. * img.cpu().numpy().squeeze()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        return img

    def apply_filter(self, images, instagram_filter):
        #create empty tensor with the same shape as images
        total_images = []
        filter_fn = getattr(pilgram, instagram_filter)
        for image in images:
            image = self.tensor_to_pil(image)
            image = filter_fn(image)

            # convert to tensor
            out_image = np.array(image.convert("RGB")).astype(np.float32) / 255.0
            out_image = torch.from_numpy(out_image).unsqueeze(0)
            total_images.append(out_image)


        total_images = torch.cat(total_images, 0)
        return (total_images,)



try:
    from glitch_this import ImageGlitcher
except ModuleNotFoundError:
    # install pixelsort in current venv
    subprocess.check_call([sys.executable, "-m", "pip", "install", "glitch-this"])
    from glitch_this import ImageGlitcher

class GlitchThis():

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {
            "required": {
                "images": ("IMAGE",),},
            "optional": {
                "glitch_amount": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 10.0, "step": 0.01}),
                "color_offset": (['Disable', 'Enable'],),
                "scan_lines": (['Disable', 'Enable'],),
                "seed": ("INT", {"default": 0, "min": 0, "max": 100, "step": 1}),
                },
            }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_glitch"

    CATEGORY = "AegisFlow/fx"

    def tensor_to_pil(self, img):
        if img is not None:
            i = 255. * img.cpu().numpy().squeeze()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        return img

    def string2bool(self, v):
        return v == 'Enable'

    def apply_glitch(self, images, glitch_amount=1, color_offset='Disable', scan_lines='Disable', seed=0):
        color_offset = self.string2bool(color_offset)
        scan_lines = self.string2bool(scan_lines)
        glitcher = ImageGlitcher()
        #create empty tensor with the same shape as images
        total_images = []
        for image in images:
            image = self.tensor_to_pil(image)
            image = glitcher.glitch_image(image, glitch_amount, color_offset=color_offset, scan_lines=scan_lines, seed=seed)

            # convert to tensor
            out_image = np.array(image.convert("RGB")).astype(np.float32) / 255.0
            out_image = torch.from_numpy(out_image).unsqueeze(0)
            total_images.append(out_image)


        total_images = torch.cat(total_images, 0)
        return (total_images,)
    



class FontText():
    """
    This node provides a simple interface to apply PixelSort blur to the output image.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {
            "required": {
                "images": ("IMAGE",),},
            "optional": {
                "font_ttf": ("STRING", {"default": 'C:/Windows/Fonts/arial.ttf'}),
                "size": ("INT", {"default": 50, "min": 2, "max": 1000, "step": 1}),
                "x": ("INT", {"default": 50, "min": 2, "max": 10000, "step": 1}),
                "y": ("INT", {"default": 50, "min": 2, "max": 10000, "step": 1}),
                "text": ("STRING", {"default": "Hello World", "multiline": True}),
                "color": ("STRING", {"default": 'rgba(255, 255, 255, 255)'}),
                "anchor": (["Bottom Left Corner", "Center"],),
                "rotate": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 360.0, "step": 0.1}),
                "color_mode": (["RGB", "RGBA"],),
                },
            }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "do_font"

    CATEGORY = "AegisFlow/fx"

    def tensor_to_pil(self, img):
        if img is not None:
            i = 255. * img.cpu().numpy().squeeze()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        return img

    def do_font(self, images, font_ttf, size, x, y, color, anchor, rotate, color_mode, text):
        #create empty tensor with the same shape as images
        total_images = []
        center_anchor = True if anchor == 'Center' else False
        if color.startswith('#'):
            color_rgba = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        else:
            color_rgba = tuple(map(int, color.strip('rgba()').split(',')))
        for image in images:
            image = self.tensor_to_pil(image)
            
            add_text_to_image(image, font_ttf, size, x, y, text, color_rgba, center_anchor, rotate)






            # convert to tensor
            out_image = np.array(image.convert(color_mode)).astype(np.float32) / 255.0
            out_image = torch.from_numpy(out_image).unsqueeze(0)
            total_images.append(out_image)


        total_images = torch.cat(total_images, 0)
        return (total_images,)



def add_text_to_image(img, font_ttf, size, x, y, text, color_rgb, center=False, rotate=0):
    draw = ImageDraw.Draw(img)
    myFont = ImageFont.truetype(font_ttf, size)
    text_width, text_height = draw.textsize(text, font=myFont)

    if center:
        x -= text_width // 2
        y -= text_height // 2

    if rotate != 0:
        text_img = Image.new('RGBA', img.size, (255, 255, 255, 0))
        text_draw = ImageDraw.Draw(text_img)
        text_draw.text((x, y), text, font=myFont, fill=color_rgb)
        text_img = text_img.rotate(rotate, resample=Image.BICUBIC, expand=True)
        img.paste(text_img, (0, 0), text_img)
    else:
        draw.text((x, y), text, font=myFont, fill=color_rgb)

    return img



# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "aegisflow Multi_Pass": aegisflow_multi_pass,
    "aegisflow Multi_Pass XL": aegisflow_multi_passxl,
    "Aegisflow Image Pass": aegisflow_image_pass,
    "Aegisflow Mask Pass": aegisflow_mask_pass,    
    "Aegisflow Latent Pass": aegisflow_latent_pass,
    "Aegisflow Model Pass": aegisflow_model_pass,
    "Aegisflow VAE Pass": aegisflow_vae_pass,
    "Aegisflow CLIP Pass": aegisflow_clip_pass,
    "Aegisflow Conditioning Pass": aegisflow_cond_pass,
    "Aegisflow Pos/Neg Pass": aegisflow_posneg_pass,
    "Aegisflow SDXL Tuple Pass": aegisflow_sdxltuple_pass,    
    "Aegisflow controlnet preprocessor bus": af_preproc_chooser,
    "Brightness_Contrast_Ally": BrightnessContrast_theAlly,
    "Image Flip_ally": ImageFlip_theAlly,
    "Gaussian Blur_Ally": GaussianBlur_theAlly,
    "Placeholder Tuple": af_placeholdertuple,
    "af_pipe_in_15": af_pipe_in_15,
    "af_pipe_out_15": af_pipe_out_15,
    "af_pipe_in_xl": af_pipe_in_xl,
    "af_pipe_out_xl": af_pipe_out_xl,    
    "Flatten Colors": Flatten_Colors,
    "Hue Rotation": HueRotation,
    "Swap Color Mode": Swap_Color_Mode,
    "Apply Instagram Filter": ApplyFilter,
    "GlitchThis Effect": GlitchThis,
    "Add Text To Image": FontText    
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "aegisflow Multi_Pass": "multi pass",
    "aegisflow Multi_Pass XL": "multi pass xl",
    "Aegisflow Image Pass": "image pass",
    "Aegisflow Mask Pass": "mask pass",
    "Aegisflow Latent Pass": "latent pass",
    "Aegisflow Model Pass": "model pass",
    "Aegisflow VAE Pass": "vae pass",
    "Aegisflow CLIP Pass": "clip pass",
    "Aegisflow Conditioning Pass": "conditioning pass",
    "Aegisflow Pos/Neg Pass": "posneg pass",
    "Aegisflow SDXL Tuple Pass": "sdxl tuple pass",    
    "Aegisflow controlnet preprocessor bus": "controlnet preprocessor bus",
    "Brightness_Contrast_Ally": "brightness contrast",
    "Image Flip_ally": "imageflip",
    "Gaussian Blur_Ally": "gaussian blur",
    "Placeholder Tuple": "placeholder tuple",
    "af_pipe_in_15": "MultiPipe 1.5 In",
    "af_pipe_out_15": "MultiPipe 1.5 Out",
    "af_pipe_in_xl": "MultiPipe XL In",
    "af_pipe_out_xl": "MultiPipe XL Out",
    "Flatten Colors": "Flatten Colors-Vextra",
    "Hue Rotation": "Hue Rotation-Vextra",
    "Swap Color Mode": "Swap Color Mode-Vextra",
    "Apply Instagram Filter": "Instagram Filters-Vextra",
    "GlitchThis Effect": "Glitch-Vextra",
    "Add Text To Image": "Add Font Text-Vextra"    
}


WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
