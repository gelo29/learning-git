#Understanding Python and MEL types Page 75
import pymel.core as pmc
import sys
import types

obj = pmc.ls(sl=True)


def info(obj):
    lines = ["Info for %s" % obj.name(),"Attributes:"]
    for a in obj.listAttr():
        lines.append(" " + a.name())
    lines.append("MEL type: %s" % obj.type())
    lines.append("MRO:")
    lines.extend([" " + t.__name__ for t in type(obj).__mro__])
    result = "\n".join(lines)
    print result

def pyto_helpstr(obj):
    if isinstance(obj, basestring):
        return "search.html?q=%s" % (obj.replace(" ", '+'))
    if isinstance(obj, types.ModuleType):
        return ("generated/%(module)s.html#module-%(module)s" %
        dict(module=obj.__name__))
        
    return None
    
def testpyto_helpstr():
    def dotest(obj, ideal):
        result = pyto_helpstr(obj)
        assert result == ideal, "%s != %s" % (result, ideal)
    dotest("maya rocks", "search.html?q=maya+rocks")
    
    dotest(pmc.nodetypes,
    "generated/pymel.core.nodetypes.html"
    "#module-pymel.core.nodetypes")
    
    dotest(pmc.nodetypes.Joint,
    "generated/classes/pymel.core.nodetypes/"
    "pymel.core.nodetypes.Joint.html"
    "#pymel.core.nodetypes.Joint")
    
    dotest(pmc.nodetypes.Joint(),
    "generated/classes/pymel.core.nodetypes/"
    "pymel.core.nodetypes.Joint.html"
    "#pymel.core.nodetypes.Joint")
    
    dotest(pmc.nodetypes.Joint().getTranslation,
    "generated/classes/pymel.core.nodetypes/"
    "pymel.core.nodetypes.Joint.html"
    "#pymel.core.nodetypes.Joint.getTranslation")
    
    dotest(pmc.Joint,
    "generated/functions/pymel.core.animnation/"
    "pymel.core.animation.Joint.html"
    "#pymel.core.animation.joint")


#import maya.standalone
#maya.standalone.initialize()
#import pymel.core as pmc
#xform, shape = pmc.polySphere()