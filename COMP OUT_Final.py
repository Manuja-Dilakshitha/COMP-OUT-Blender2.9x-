bl_info = {
    "name": "COMP OUT",
    "author": "Manuja Dilaksitha @ Thina Entertainment",
    "version": (1, 0),
    "blender": (2, 93),
    "description": "Set compositor nodes and generate related folder paths",
    "warning": "Clicking GENERATE buton multiple times creates multiple nodes and will override currently saved fiels!!!",
    "doc_url": "",
    "tracker_url": "",
}



import bpy

from bpy.types import Operator

from bpy.props import BoolProperty




######################    Create Checkboxed - BoolPrperties    ########################


bpy.types.Scene.Image = BoolProperty(
    name = "Image",
        description = "Image",
        default = True)

bpy.types.Scene.Alpha = BoolProperty(
    name = "Alpha",
        description = "Alpha",
        default = True)

bpy.types.Scene.Depth = BoolProperty(
    name = "Depth",
        description = "Depth",
        default = True)

bpy.types.Scene.Normal = BoolProperty(
    name = "Normal",
        description = "Normal",
        default = True)

bpy.types.Scene.Shadow = BoolProperty(
    name = "Shadow",
        description = "Shadow",
        default = True)
        
bpy.types.Scene.AO = BoolProperty(
    name = "AO",
        description = "AO",
        default = True)
        
        
        
        
        
bpy.types.Scene.DiffDir = BoolProperty(
    name = "Diffuse Direct",
        default = True)
        
bpy.types.Scene.DiffIndir = BoolProperty(
    name = "Diffuse Indirect",
        description = "Diffuse Indirect",
        default = True)
        
bpy.types.Scene.DiffCol = BoolProperty(
    name = "Diffuse Color",
        default = True)
        
        
        
        
        
bpy.types.Scene.GlossDir = BoolProperty(
    name = "Glossy Direct",
        default = True)
        
bpy.types.Scene.GlossIndir = BoolProperty(
    name = "Glossy Indirect",
        default = True)
        
bpy.types.Scene.GlossCol = BoolProperty(
    name = "Glossy Color",
        default = True)
        
        
        
        
        
bpy.types.Scene.TransDir = BoolProperty(
    name = "Transmission Direct",
        default = True)
        
bpy.types.Scene.TransIndir = BoolProperty(
    name = "Transmission Indirect",
        default = True)
        
bpy.types.Scene.TransCol = BoolProperty(
    name = "Transmission Color",
        default = True)
        
        
        
        
        
bpy.types.Scene.CryptoObj = BoolProperty(
    name = "Crypto Object",
        default = True)
        
bpy.types.Scene.CryptoMat = BoolProperty(
    name = "Crypto Material",
        default = True)
        
bpy.types.Scene.CryptoAsset = BoolProperty(
    name = "Crypto Asset",
        default = True)
        
        
        
        
        
######################    Panel    ########################

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Set Compositor Output Nodes"
    bl_idname = "NODE_PT_CompOut"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'COMP OUT'

    def draw(self, context):
        scene = context.scene
        layout = self.layout

        obj = context.object
        
        
        row = layout.row()
        row.label(text="Select Output Folder : ")
        
        row = layout.row()
        row.prop(scene, "my_string_prop")
        
        
        
        
        row = layout.row()
        row.label(text = "")
        
        
        

        row = layout.row()
        row.label(text="Select Passes", icon='RENDERLAYERS')
        
        
        
        ################  <RENDER PASSES CHECKBOXES>  ###################
        row = layout.row()
        row.prop(scene, "Image")
        
        row = layout.row()
        row.prop(scene, "AO")
        
        row = layout.row()
        row.prop(scene, "Depth")
        
        row = layout.row()
        row.prop(scene, "Alpha")
        
        row = layout.row()
        row.prop(scene, "Normal")
        
        row = layout.row()
        row.prop(scene, "Shadow")
        
        
        
        row = layout.row()
        row.label(text = "")
        
        
        
        row = layout.row()
        row.prop(scene, "DiffDir")
        
        row = layout.row()
        row.prop(scene, "DiffIndir")
        
        row = layout.row()
        row.prop(scene, "DiffCol")
        
        
        
        row = layout.row()
        row.label(text = "")
        
        
        
        row = layout.row()
        row.prop(scene, "GlossDir")
        
        row = layout.row()
        row.prop(scene, "GlossIndir")
        
        row = layout.row()
        row.prop(scene, "GlossCol")
        
        
        
        row = layout.row()
        row.label(text = "")
        
        
        
        row = layout.row()
        row.prop(scene, "TransDir")
        
        row = layout.row()
        row.prop(scene, "TransIndir")
        
        row = layout.row()
        row.prop(scene, "TransCol")
        
        
        
        row = layout.row()
        row.label(text = "")
        
            
        
        row = layout.row()
        row.prop(scene, "CryptoObj")
        
        row = layout.row()
        row.prop(scene, "CryptoMat")
        
        row = layout.row()
        row.prop(scene, "CryptoAsset")
        
        
        
        row = layout.row()
        row.label(text = "")
        
        
        
        ################  <RENDER PASSES CHECKBOXES/>  ###################
        
        
        ########## Buttons ###########
        
        
        row = layout.row()
        row.operator("compositorfilepaths.generate")
        
        
        row = layout.row()
        row.label(text = "")
        
        
        row = layout.row()
        row.label(text = "THINA ENTERTAINMENT", icon="GREASEPENCIL")
        
        
        
        
        
        
##############################      FUNCITON      ###########################
        
        

class create(bpy.types.Operator):
    
    bl_label = "Generate"
    bl_idname = 'compositorfilepaths.generate'
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context): 
        
        scene = bpy.context.scene
        nodes = scene.node_tree.nodes

        render_layers = nodes['Render Layers']

        layer_outputs = []
        
        if(context.scene.Image == True):
            layer_outputs.append("Image")
            
        if (context.scene.Alpha == True):
            layer_outputs.append("Alpha")
            
        if (context.scene.Depth == True):
            layer_outputs.append("Depth")
            
        if (context.scene.AO == True):
            layer_outputs.append("AO")
            
        if (context.scene.Normal == True):
            layer_outputs.append("Normal")
            
        if (context.scene.Shadow == True):
            layer_outputs.append("Shadow")
            
            
            
        if (context.scene.DiffDir == True):
            layer_outputs.append("DiffDir")
            
        if (context.scene.DiffIndir == True):
            layer_outputs.append("DiffInd")
            
        if (context.scene.DiffCol == True):
            layer_outputs.append("DiffCol") 
            
            
            
        if (context.scene.GlossDir == True):
            layer_outputs.append("GlossDir")
            
        if (context.scene.GlossIndir == True):
            layer_outputs.append("GlossInd")
            
        if (context.scene.GlossCol == True):
            layer_outputs.append("GlossCol")
            
            
            
        if (context.scene.TransDir == True):
            layer_outputs.append("TransDir")
            
        if (context.scene.TransIndir == True):
            layer_outputs.append("TransInd")
            
        if (context.scene.TransCol == True):
            layer_outputs.append("TransCol")
            
            
            
        if (context.scene.CryptoObj == True):
            layer_outputs.append("CryptoObject00")
            
        if (context.scene.CryptoMat == True):
            layer_outputs.append("CryptoMaterial00")
            
        if (context.scene.CryptoAsset == True):
            layer_outputs.append("CryptoAsset00")
            
        location = 100
        
        output_file = nodes.new("CompositorNodeOutputFile")
        output_file.location.y = 0
        output_file.location.x = 100
        
        for layer in layer_outputs:
            
            output_file.file_slots.new(layer)
            
            output_file.base_path = (context.scene.my_string_prop + "/")
            scene.node_tree.links.new(render_layers.outputs[layer], output_file.inputs[layer])
            
            
            
        return{'FINISHED'}
        
        


###################### REGISTER ####################        

def register():
    bpy.types.Scene.my_string_prop = bpy.props.StringProperty \
      (
        name = "Output",
        description = "Select Output Folder",
        default = "Desktop/Render/"
      )
    
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(create)
    


################### UNREGISTER #####################

def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.register_class(create)
    del bpy.types.Scene.my_string_prop


if __name__ == "__main__":
    register()
