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
from mathutils import Vector
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
        revV.use_normal_calculate = True
        
        
        #const = p_radius.constraints.new('LIMIT_LOCATION')
        #const.use_min_x = True
        #const.use_max_x = True
        #const.use_min_y = True
        #const.use_max_y = True
        #const.owner_space = 'LOCAL'
        p_radius.empty_display_type= 'SINGLE_ARROW'
        p_radius.lock_location  = [True, True, False]
        p_radius.lock_rotation  = [True, True, True]
        p_radius.lock_scale     = [True, True, True]
                
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

        
class ParametricCylinder(Operator):
    """Adds a cylinder object"""           # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.add_cylinder_sphere"      # Unique identifier for buttons and menu items to reference.
    bl_label = "Add parametric Cylinder"              # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}               # Enable undo for the operator.

    def execute(self, context):                     # execute() is called when running the operator.
        mesh = bpy.data.meshes.new("Cylinder")
        mesh.from_pydata([(0.0, 0.0, 0.0),(0.0, 0.5, 0.0)],[(0,1)],[])
        mesh.validate()
        object_utils.object_data_add(context, mesh, operator=None)
        obj = context.object
        
        bpy.ops.object.empty_add(
            location=obj.matrix_world @ Vector((0.0, 0.5, 1.0,))
            )
        p_ctrl = context.object
        p_ctrl.name = '#p_ctrl'
        p_ctrl.parent = obj
        p_ctrl.empty_display_size= 0.2
        p_ctrl.lock_location  = [True, False, False]
        p_ctrl.lock_rotation  = [True, True, True]
        p_ctrl.lock_scale     = [True, True, True]
        
        vx = obj.data.vertices[1]
        bpy.ops.object.empty_add(
            location=obj.matrix_world @ vx.co
            )
        p_radius = context.object
        p_radius.name = '#p_radius'

        p_radius.parent = obj
        hm = obj.modifiers.new(type='HOOK', name='radius')
        hm.object = p_radius
        hm.vertex_indices_set([1])
        
        bpy.context.view_layer.objects.active = obj
        rev = obj.modifiers.new(type='SCREW', name='Revolution')
        rev.axis = "Z"
        #rev.angle = 2*math.pi
        rev.screw_offset = 0
        rev.use_merge_vertices = True
        ext = obj.modifiers.new(type='SOLIDIFY', name='Extrude')
        ext.thickness = 1
        ext.offset = 1
        
        #const = p_radius.constraints.new('LIMIT_LOCATION')
        #const.use_min_x = True
        #const.use_max_x = True
        #const.use_min_y = True
        #const.use_max_y = True
        #const.owner_space = 'LOCAL'
        p_radius.empty_display_type= 'SINGLE_ARROW'
        p_radius.rotation_euler[0] = -0.5*math.pi
        p_radius.empty_display_size= 0.5
        p_radius.lock_location  = [True, False, True]
        p_radius.lock_rotation  = [True, True, True]
        p_radius.lock_scale     = [True, True, True]
        
        const = p_radius.constraints.new('COPY_LOCATION')
        const.target = p_ctrl
        const.use_x = False
        const.use_z = False
        const.owner_space = 'LOCAL'
        
        height_Fc = ext.driver_add('thickness')
        var_h = height_Fc.driver.variables.new()
        var_h.name = 'h'
        var_h.type = 'TRANSFORMS'
        var_h.targets[0].transform_type = 'LOC_Z'
        var_h.targets[0].transform_space = 'LOCAL_SPACE'
        var_h.targets[0].id = p_ctrl
        height_Fc.driver.expression = 'h'
        
        
                
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

        
def register():
    bpy.utils.register_class(ParametricSphere)
    bpy.utils.register_class(ParametricCylinder)


def unregister():
    bpy.utils.unregister_class(ParametricSphere)
    bpy.utils.unregister_class(ParametricCylinder)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
