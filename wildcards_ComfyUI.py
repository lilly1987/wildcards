import wildcards

class CLIPTextEncodeWildcards:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("STRING", {"multiline": True}), "clip": ("CLIP", )}}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = "conditioning"

    def encode(self, clip, text):
        return ([[clip.encode(wildcards.run(text)), {}]], )
        
        
NODE_CLASS_MAPPINGS = {
    "CLIPTextEncodeWildcards": CLIPTextEncodeWildcards
}
