
import os.path
Ici3Dn_data_Conf="G:\\GenezIA_Working_G\\WorkSpace_Python\\PyRun_Comfyui_Data\\nodes"	
class Ici3Dn_Identity:
    @classmethod
   
    
        # return {
        #     "required": {
        #         "text": ("STRING", {"forceInput": True}),
        #     },
        #     "hidden": {
        #         "unique_id": "UNIQUE_ID",
        #         "extra_pnginfo": "EXTRA_PNGINFO",
        #     },
        # }
    def INPUT_TYPES(s):
        return {
            "required": {
                "ID": ("STRING", {"multiline": False}),
                "Original": ("STRING", {"multiline": False}),
            },
        }
   
    INPUT_IS_LIST = True
    RETURN_NAMES = ()
    RETURN_TYPES = ()
    FUNCTION = "notify"
    OUTPUT_NODE = True
    #OUTPUT_IS_LIST = (True,)

    CATEGORY = "Ici3Dn_Nodes"
    def notify(self, ID, Original ): 
    #def notify(self, ID, unique_id=None, extra_pnginfo=None):
        # if unique_id is not None and extra_pnginfo is not None:
        #     if not isinstance(extra_pnginfo, list):
        #         print("Error: extra_pnginfo is not a list")
        #     elif (
        #         not isinstance(extra_pnginfo[0], dict)
        #         or "workflow" not in extra_pnginfo[0]
        #     ):
        #         print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
        #     else:
        #         workflow = extra_pnginfo[0]["workflow"]
        #         node = next(
        #             (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
        #             None,
        #         )
        #         if node:
        #             node["widgets_values"] = [ID]
        #self.original=Originale 
        # {"ui": {"text": ID}, "result": (ID,)}
        #dir = get_config_value("ConfData")
        file=(f"{Ici3Dn_data_Conf}\\{ID}.json")
        isConfFil=False
        if os.path.exists(file):
            isConfFil="True"
        conf=f"Conf = {isConfFil}"    
        return  {"ui": {"text": "ConfData"}, "result": (conf,)}


NODE_CLASS_MAPPINGS = {
    "Ici3Dn_Identity": Ici3Dn_Identity,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Ici3Dn_Identity": "Ici3Dn Identity",
}
