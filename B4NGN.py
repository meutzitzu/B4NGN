# M E T A D A T A ------------------\
bl_info = {
    "name": "B4NGN",
    "blender": (2, 80, 0),
    "category": "Add_Mesh",
}
# ----------------------------------/
        
# I M P O R T S --------------------\                                            
import bpy
import math
from bpy.types import Operator
from bpy_extras import object_utils
# ----------------------------------/


class ParametricSphere(Operator):
    """Adds a parametric sphere object"""           # Use this as a tooltip for menu items and buttons.
    bl_idname   = "object.add_parametric_sphere"      # Unique identifier for buttons and menu items to reference.
    bl_label    = "Add parametric Sphere"              # Display name in the interface.
    bl_options  = {'REGISTER', 'UNDO'}               # Enable undo for the operator.

    def execute(self, context):                     # execute() is called when running the operator.
        mesh = bpy.data.meshes.new("Sphere")
        mesh.from_pydata([(0.0, 0.0, 1.0)],[],[])
        mesh.validate()
        object_utils.object_data_add(context, mesh, operator=None)
        obj = context.object
        
        vx = obj.data.vertices[0]
        bpy.ops.object.empty_add(
            location=obj.matrix_world @ vx.co
            )
        p_radius = context.object
        p_radius.parent = obj
        hm = obj.modifiers.new(type='HOOK', name='#P_radius')
        hm.object = p_radius
        hm.vertex_indices_set([0])
        
        bpy.context.view_layer.objects.active = obj
        revU = obj.modifiers.new(type='SCREW', name='Revolution_U')
        revU.axis = "X"
        revU.angle = math.pi
        revV = obj.modifiers.new(type='SCREW', name='Revolution_V')
        revV.use_merge_vertices = True
        
        p_radius.lock_location  = [True, True, False]
        p_radius.lock_rotation  = [True, True, True]
        p_radius.lock_scale     = [True, True, True]
        #const = p_radius.constraints.new('LIMIT_LOCATION')
        #const.use_min_x = True
        #const.use_max_x = True
        #const.use_min_y = True
        #const.use_max_y = True
        #const.owner_space = 'LOCAL'
        p_radius.empty_display_type= 'SINGLE_ARROW'
                
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

        
        
def register():
    bpy.utils.register_class(ParametricSphere)


def unregister():
    bpy.utils.unregister_class(ParametricSphere)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
