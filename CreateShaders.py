from maya import cmds as mc


def create_shaders():
    """Create shader and wire the file node to it"""

    geo_name = get_selection()
    for geo in geo_name:
        str(geo)
    # print("Call: %s" % geo)
    ai_standard_surface_node = mc.rename(mc.shadingNode("aiStandardSurface", asShader=True), geo + "_mat")
    # print("Nod: %s" % ai_standard_surface_node)
    file_nod = file_texture2d_node()

    print(ai_standard_surface_node)
    print(file_nod)
    mc.connectAttr("%s.outColor" % file_nod, "%s.baseColor" % ai_standard_surface_node)

    # mc.defaultNavigation(ce=True,     s=file_nod, d=ai_standard_surface_node, )
    shader_group = mc.sets(r=True, nss=True, em=True, n="%sSG" % ai_standard_surface_node)
    mc.connectAttr("%s.outColor" % ai_standard_surface_node, "%s.surfaceShader" % shader_group)

    mc.sets(geo, e=True, fe=shader_group)
    # print(type(shader_group))
    # print(mc.sets(shader_group, q=True))

    mc.select(geo_name)


def file_texture2d_node():
    """Create a file and texture 2d node and wire the required attributes"""

    file_node = mc.shadingNode("file", at=True, icm=True)
    texture2d_node = mc.shadingNode("place2dTexture", au=True)
    # print(texture2d_node)

    attributes = ["%s.coverage", "%s.translateFrame", "%s.rotateFrame", "%s.mirrorU",
                  "%s.mirrorV", "%s.stagger", "%s.wrapU", "%s.wrapV", "%s.repeatUV", "%s.offset",
                  "%s.rotateUV", "%s.noiseUV", "%s.vertexUvOne", "%s.vertexUvTwo", "%s.vertexUvThree",
                  "%s.vertexCameraOne"]

    for attribute in attributes:
        mc.connectAttr(attribute % texture2d_node, attribute % file_node, f=True)

    mc.connectAttr("%s.outUV" % texture2d_node, "%s.uv" % file_node)
    mc.connectAttr("%s.outUvFilterSize" % texture2d_node, "%s.uvFilterSize" % file_node)
    # mc.connectAttr("%s.outUV" % texture2d_node, "%s.uv" % file_node)

    # mc.setAttr("%s.ftn" % t, r"sourceimages\bicycle_textures\body_2_Base_Color.png", typ="string")
    # mc.setAttr("%s.colorSpace" % t, "Raw", typ="string")

    return file_node



def get_selection():
    """Get a list of selection objects in the scene"""

    geo_selection = mc.ls(sl=True)
    print("In function: %s" % geo_selection)
    return geo_selection


create_shaders()


