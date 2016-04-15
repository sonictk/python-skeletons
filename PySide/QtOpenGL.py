# encoding: utf-8
# module PySide.QtOpenGL
# from /corp.blizzard.net/BFD/Deploy/Packages/Published/ThirdParty/Qt4.8.4/2015-05-15.163857/prebuilt/linux_x64_gcc41_python2.7_ucs4/PySide/QtOpenGL.so
# by generator 1.138
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import PySide.QtGui as __PySide_QtGui


# no functions
# classes

class _Object(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class QGL(_Object):
    # no doc
    def setPreferredPaintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AccumBuffer = None
    AlphaChannel = None
    ColorIndex = None
    DebugContext = None
    DeprecatedFunctions = None
    DepthBuffer = None
    DirectRendering = None
    DoubleBuffer = None
    FormatOption = None
    FormatOptions = None
    HasOverlay = None
    IndirectRendering = None
    NoAccumBuffer = None
    NoAlphaChannel = None
    NoDebugContext = None
    NoDeprecatedFunctions = None
    NoDepthBuffer = None
    NoOverlay = None
    NoSampleBuffers = None
    NoStencilBuffer = None
    NoStereoBuffers = None
    Rgba = None
    SampleBuffers = None
    SingleBuffer = None
    StencilBuffer = None
    StereoBuffers = None


class QGLBuffer(_Object):
    # no doc
    def allocate(self, *args, **kwargs): # real signature unknown
        pass

    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def bufferId(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def isCreated(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def setUsagePattern(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def unmap(self, *args, **kwargs): # real signature unknown
        pass

    def usagePattern(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    Access = None
    DynamicCopy = None
    DynamicDraw = None
    DynamicRead = None
    IndexBuffer = None
    PixelPackBuffer = None
    PixelUnpackBuffer = None
    ReadOnly = None
    ReadWrite = None
    StaticCopy = None
    StaticDraw = None
    StaticRead = None
    StreamCopy = None
    StreamDraw = None
    StreamRead = None
    Type = None
    UsagePattern = None
    VertexBuffer = None
    WriteOnly = None
    __new__ = None


class QGLColormap(_Object):
    # no doc
    def entryColor(self, *args, **kwargs): # real signature unknown
        pass

    def entryRgb(self, *args, **kwargs): # real signature unknown
        pass

    def find(self, *args, **kwargs): # real signature unknown
        pass

    def findNearest(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        pass

    def setEntry(self, *args, **kwargs): # real signature unknown
        pass

    def setHandle(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class QGLContext(_Object):
    # no doc
    def areSharing(self, *args, **kwargs): # real signature unknown
        pass

    def bindTexture(self, *args, **kwargs): # real signature unknown
        pass

    def chooseContext(self, *args, **kwargs): # real signature unknown
        pass

    def colorIndex(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentContext(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, *args, **kwargs): # real signature unknown
        pass

    def device(self, *args, **kwargs): # real signature unknown
        pass

    def deviceIsPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def getContext(self, *args, **kwargs): # real signature unknown
        pass

    def getProcAddress(self, *args, **kwargs): # real signature unknown
        pass

    def initialized(self, *args, **kwargs): # real signature unknown
        pass

    def isSharing(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def overlayTransparentColor(self, *args, **kwargs): # real signature unknown
        pass

    def requestedFormat(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def setDevice(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setInitialized(self, *args, **kwargs): # real signature unknown
        pass

    def setTextureCacheLimit(self, *args, **kwargs): # real signature unknown
        pass

    def setValid(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowCreated(self, *args, **kwargs): # real signature unknown
        pass

    def swapBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def textureCacheLimit(self, *args, **kwargs): # real signature unknown
        pass

    def updatePaintDevice(self, *args, **kwargs): # real signature unknown
        pass

    def windowCreated(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    BindOption = None
    BindOptions = None
    CanFlipNativePixmapBindOption = None
    DefaultBindOption = None
    InternalBindOption = None
    InvertedYBindOption = None
    LinearFilteringBindOption = None
    MemoryManagedBindOption = None
    MipmapBindOption = None
    NoBindOption = None
    PremultipliedAlphaBindOption = None
    __new__ = None


class QGLFormat(_Object):
    # no doc
    def accum(self, *args, **kwargs): # real signature unknown
        pass

    def accumBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def alpha(self, *args, **kwargs): # real signature unknown
        pass

    def alphaBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def blueBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def defaultFormat(self, *args, **kwargs): # real signature unknown
        pass

    def defaultOverlayFormat(self, *args, **kwargs): # real signature unknown
        pass

    def depth(self, *args, **kwargs): # real signature unknown
        pass

    def depthBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def directRendering(self, *args, **kwargs): # real signature unknown
        pass

    def doubleBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def greenBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGL(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLOverlays(self, *args, **kwargs): # real signature unknown
        pass

    def hasOverlay(self, *args, **kwargs): # real signature unknown
        pass

    def majorVersion(self, *args, **kwargs): # real signature unknown
        pass

    def minorVersion(self, *args, **kwargs): # real signature unknown
        pass

    def openGLVersionFlags(self, *args, **kwargs): # real signature unknown
        pass

    def plane(self, *args, **kwargs): # real signature unknown
        pass

    def profile(self, *args, **kwargs): # real signature unknown
        pass

    def redBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def rgba(self, *args, **kwargs): # real signature unknown
        pass

    def sampleBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def samples(self, *args, **kwargs): # real signature unknown
        pass

    def setAccum(self, *args, **kwargs): # real signature unknown
        pass

    def setAccumBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setAlpha(self, *args, **kwargs): # real signature unknown
        pass

    def setAlphaBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setBlueBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultOverlayFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setDepth(self, *args, **kwargs): # real signature unknown
        pass

    def setDepthBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setDirectRendering(self, *args, **kwargs): # real signature unknown
        pass

    def setDoubleBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def setGreenBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setOption(self, *args, **kwargs): # real signature unknown
        pass

    def setOverlay(self, *args, **kwargs): # real signature unknown
        pass

    def setPlane(self, *args, **kwargs): # real signature unknown
        pass

    def setProfile(self, *args, **kwargs): # real signature unknown
        pass

    def setRedBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setRgba(self, *args, **kwargs): # real signature unknown
        pass

    def setSampleBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def setSamples(self, *args, **kwargs): # real signature unknown
        pass

    def setStencil(self, *args, **kwargs): # real signature unknown
        pass

    def setStencilBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setStereo(self, *args, **kwargs): # real signature unknown
        pass

    def setSwapInterval(self, *args, **kwargs): # real signature unknown
        pass

    def setVersion(self, *args, **kwargs): # real signature unknown
        pass

    def stencil(self, *args, **kwargs): # real signature unknown
        pass

    def stencilBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def stereo(self, *args, **kwargs): # real signature unknown
        pass

    def swapInterval(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    CompatibilityProfile = None
    CoreProfile = None
    NoProfile = None
    OpenGLContextProfile = None
    OpenGLVersionFlag = None
    OpenGLVersionFlags = None
    OpenGL_ES_CommonLite_Version_1_0 = None
    OpenGL_ES_CommonLite_Version_1_1 = None
    OpenGL_ES_Common_Version_1_0 = None
    OpenGL_ES_Common_Version_1_1 = None
    OpenGL_ES_Version_2_0 = None
    OpenGL_Version_1_1 = None
    OpenGL_Version_1_2 = None
    OpenGL_Version_1_3 = None
    OpenGL_Version_1_4 = None
    OpenGL_Version_1_5 = None
    OpenGL_Version_2_0 = None
    OpenGL_Version_2_1 = None
    OpenGL_Version_3_0 = None
    OpenGL_Version_3_1 = None
    OpenGL_Version_3_2 = None
    OpenGL_Version_3_3 = None
    OpenGL_Version_4_0 = None
    OpenGL_Version_None = None
    __new__ = None


class _QPaintDevice(__PySide_QtGui._Object):
    # no doc
    def colorCount(self, *args, **kwargs): # real signature unknown
        pass

    def depth(self, *args, **kwargs): # real signature unknown
        pass

    def devType(self, *args, **kwargs): # real signature unknown
        pass

    def height(self, *args, **kwargs): # real signature unknown
        pass

    def heightMM(self, *args, **kwargs): # real signature unknown
        pass

    def logicalDpiX(self, *args, **kwargs): # real signature unknown
        pass

    def logicalDpiY(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def numColors(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def paintingActive(self, *args, **kwargs): # real signature unknown
        pass

    def physicalDpiX(self, *args, **kwargs): # real signature unknown
        pass

    def physicalDpiY(self, *args, **kwargs): # real signature unknown
        pass

    def width(self, *args, **kwargs): # real signature unknown
        pass

    def widthMM(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    PaintDeviceMetric = None
    painters = None
    PdmDepth = None
    PdmDpiX = None
    PdmDpiY = None
    PdmHeight = None
    PdmHeightMM = None
    PdmNumColors = None
    PdmPhysicalDpiX = None
    PdmPhysicalDpiY = None
    PdmWidth = None
    PdmWidthMM = None
    __new__ = None


class QGLFramebufferObject(__PySide_QtGui.QPaintDevice):
    # no doc
    def attachment(self, *args, **kwargs): # real signature unknown
        pass

    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def bindDefault(self, *args, **kwargs): # real signature unknown
        pass

    def blitFramebuffer(self, *args, **kwargs): # real signature unknown
        pass

    def devType(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLFramebufferBlit(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLFramebufferObjects(self, *args, **kwargs): # real signature unknown
        pass

    def isBound(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def texture(self, *args, **kwargs): # real signature unknown
        pass

    def toImage(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    Attachment = None
    CombinedDepthStencil = None
    Depth = None
    NoAttachment = None
    __new__ = None


class QGLFramebufferObjectFormat(_Object):
    # no doc
    def attachment(self, *args, **kwargs): # real signature unknown
        pass

    def internalTextureFormat(self, *args, **kwargs): # real signature unknown
        pass

    def mipmap(self, *args, **kwargs): # real signature unknown
        pass

    def samples(self, *args, **kwargs): # real signature unknown
        pass

    def setAttachment(self, *args, **kwargs): # real signature unknown
        pass

    def setInternalTextureFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setMipmap(self, *args, **kwargs): # real signature unknown
        pass

    def setSamples(self, *args, **kwargs): # real signature unknown
        pass

    def setTextureTarget(self, *args, **kwargs): # real signature unknown
        pass

    def textureTarget(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __new__ = None


class QGLPixelBuffer(__PySide_QtGui.QPaintDevice):
    # no doc
    def bindTexture(self, *args, **kwargs): # real signature unknown
        pass

    def bindToDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, *args, **kwargs): # real signature unknown
        pass

    def devType(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def generateDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLPbuffers(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def releaseFromDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def toImage(self, *args, **kwargs): # real signature unknown
        pass

    def updateDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class _QObject(__PySide_QtCore._Object):
    # no doc
    def blockSignals(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def children(self, *args, **kwargs): # real signature unknown
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deleteLater(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dumpObjectInfo(self, *args, **kwargs): # real signature unknown
        pass

    def dumpObjectTree(self, *args, **kwargs): # real signature unknown
        pass

    def dynamicPropertyNames(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def findChild(self, *args, **kwargs): # real signature unknown
        pass

    def findChildren(self, *args, **kwargs): # real signature unknown
        pass

    def inherits(self, *args, **kwargs): # real signature unknown
        pass

    def installEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def isWidgetType(self, *args, **kwargs): # real signature unknown
        pass

    def killTimer(self, *args, **kwargs): # real signature unknown
        pass

    def metaObject(self, *args, **kwargs): # real signature unknown
        pass

    def moveToThread(self, *args, **kwargs): # real signature unknown
        pass

    def objectName(self, *args, **kwargs): # real signature unknown
        pass

    def parent(self, *args, **kwargs): # real signature unknown
        pass

    def property(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerUserData(self, *args, **kwargs): # real signature unknown
        pass

    def removeEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setObjectName(self, *args, **kwargs): # real signature unknown
        pass

    def setParent(self, *args, **kwargs): # real signature unknown
        pass

    def setProperty(self, *args, **kwargs): # real signature unknown
        pass

    def signalsBlocked(self, *args, **kwargs): # real signature unknown
        pass

    def startTimer(self, *args, **kwargs): # real signature unknown
        pass

    def thread(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tr(self, *args, **kwargs): # real signature unknown
        pass

    def trUtf8(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    destroyed = None
    staticMetaObject = None
    __new__ = None


class QGLShader(__PySide_QtCore.QObject):
    # no doc
    def compileSourceCode(self, *args, **kwargs): # real signature unknown
        pass

    def compileSourceFile(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLShaders(self, *args, **kwargs): # real signature unknown
        pass

    def isCompiled(self, *args, **kwargs): # real signature unknown
        pass

    def log(self, *args, **kwargs): # real signature unknown
        pass

    def shaderId(self, *args, **kwargs): # real signature unknown
        pass

    def shaderType(self, *args, **kwargs): # real signature unknown
        pass

    def sourceCode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    Fragment = None
    Geometry = None
    ShaderType = None
    ShaderTypeBit = None
    staticMetaObject = None
    Vertex = None
    __new__ = None


class QGLShaderProgram(__PySide_QtCore.QObject):
    # no doc
    def addShader(self, *args, **kwargs): # real signature unknown
        pass

    def addShaderFromSourceCode(self, *args, **kwargs): # real signature unknown
        pass

    def addShaderFromSourceFile(self, *args, **kwargs): # real signature unknown
        pass

    def attributeLocation(self, *args, **kwargs): # real signature unknown
        pass

    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def bindAttributeLocation(self, *args, **kwargs): # real signature unknown
        pass

    def disableAttributeArray(self, *args, **kwargs): # real signature unknown
        pass

    def enableAttributeArray(self, *args, **kwargs): # real signature unknown
        pass

    def geometryInputType(self, *args, **kwargs): # real signature unknown
        pass

    def geometryOutputType(self, *args, **kwargs): # real signature unknown
        pass

    def geometryOutputVertexCount(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLShaderPrograms(self, *args, **kwargs): # real signature unknown
        pass

    def isLinked(self, *args, **kwargs): # real signature unknown
        pass

    def link(self, *args, **kwargs): # real signature unknown
        pass

    def log(self, *args, **kwargs): # real signature unknown
        pass

    def maxGeometryOutputVertices(self, *args, **kwargs): # real signature unknown
        pass

    def programId(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def removeAllShaders(self, *args, **kwargs): # real signature unknown
        pass

    def removeShader(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray2D(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray3D(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray4D(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeValue(self, *args, **kwargs): # real signature unknown
        pass

    def setGeometryInputType(self, *args, **kwargs): # real signature unknown
        pass

    def setGeometryOutputType(self, *args, **kwargs): # real signature unknown
        pass

    def setGeometryOutputVertexCount(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValue(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2D(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2x2(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2x3(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2x4(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3D(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3x2(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3x3(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3x4(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4D(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4x2(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4x3(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4x4(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArrayInt(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArrayUint(self, *args, **kwargs): # real signature unknown
        pass

    def shaders(self, *args, **kwargs): # real signature unknown
        pass

    def uniformLocation(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    __new__ = None


class _QWidget(__PySide_QtCore.QObject, __PySide_QtGui.QPaintDevice):
    # no doc
    def acceptDrops(self, *args, **kwargs): # real signature unknown
        pass

    def accessibleDescription(self, *args, **kwargs): # real signature unknown
        pass

    def accessibleName(self, *args, **kwargs): # real signature unknown
        pass

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def actions(self, *args, **kwargs): # real signature unknown
        pass

    def activateWindow(self, *args, **kwargs): # real signature unknown
        pass

    def addAction(self, *args, **kwargs): # real signature unknown
        pass

    def addActions(self, *args, **kwargs): # real signature unknown
        pass

    def adjustSize(self, *args, **kwargs): # real signature unknown
        pass

    def autoFillBackground(self, *args, **kwargs): # real signature unknown
        pass

    def backgroundRole(self, *args, **kwargs): # real signature unknown
        pass

    def baseSize(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childAt(self, *args, **kwargs): # real signature unknown
        pass

    def childrenRect(self, *args, **kwargs): # real signature unknown
        pass

    def childrenRegion(self, *args, **kwargs): # real signature unknown
        pass

    def clearFocus(self, *args, **kwargs): # real signature unknown
        pass

    def clearMask(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def contentsMargins(self, *args, **kwargs): # real signature unknown
        pass

    def contentsRect(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def createWinId(self, *args, **kwargs): # real signature unknown
        pass

    def cursor(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def devType(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def effectiveWinId(self, *args, **kwargs): # real signature unknown
        pass

    def ensurePolished(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusProxy(self, *args, **kwargs): # real signature unknown
        pass

    def focusWidget(self, *args, **kwargs): # real signature unknown
        pass

    def font(self, *args, **kwargs): # real signature unknown
        pass

    def fontInfo(self, *args, **kwargs): # real signature unknown
        pass

    def fontMetrics(self, *args, **kwargs): # real signature unknown
        pass

    def foregroundRole(self, *args, **kwargs): # real signature unknown
        pass

    def frameGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def frameSize(self, *args, **kwargs): # real signature unknown
        pass

    def geometry(self, *args, **kwargs): # real signature unknown
        pass

    def getContentsMargins(self, *args, **kwargs): # real signature unknown
        pass

    def grabGesture(self, *args, **kwargs): # real signature unknown
        pass

    def grabKeyboard(self, *args, **kwargs): # real signature unknown
        pass

    def grabMouse(self, *args, **kwargs): # real signature unknown
        pass

    def grabShortcut(self, *args, **kwargs): # real signature unknown
        pass

    def graphicsEffect(self, *args, **kwargs): # real signature unknown
        pass

    def graphicsProxyWidget(self, *args, **kwargs): # real signature unknown
        pass

    def hasFocus(self, *args, **kwargs): # real signature unknown
        pass

    def hasMouseTracking(self, *args, **kwargs): # real signature unknown
        pass

    def height(self, *args, **kwargs): # real signature unknown
        pass

    def heightForWidth(self, *args, **kwargs): # real signature unknown
        pass

    def hide(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputContext(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodHints(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertAction(self, *args, **kwargs): # real signature unknown
        pass

    def insertActions(self, *args, **kwargs): # real signature unknown
        pass

    def instanceCounter(self, *args, **kwargs): # real signature unknown
        pass

    def instanceOperationsCounter(self, *args, **kwargs): # real signature unknown
        pass

    def isActiveWindow(self, *args, **kwargs): # real signature unknown
        pass

    def isAncestorOf(self, *args, **kwargs): # real signature unknown
        pass

    def isEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def isEnabledTo(self, *args, **kwargs): # real signature unknown
        pass

    def isFullScreen(self, *args, **kwargs): # real signature unknown
        pass

    def isHidden(self, *args, **kwargs): # real signature unknown
        pass

    def isLeftToRight(self, *args, **kwargs): # real signature unknown
        pass

    def isMaximized(self, *args, **kwargs): # real signature unknown
        pass

    def isMinimized(self, *args, **kwargs): # real signature unknown
        pass

    def isModal(self, *args, **kwargs): # real signature unknown
        pass

    def isRightToLeft(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self, *args, **kwargs): # real signature unknown
        pass

    def isVisibleTo(self, *args, **kwargs): # real signature unknown
        pass

    def isWindow(self, *args, **kwargs): # real signature unknown
        pass

    def isWindowModified(self, *args, **kwargs): # real signature unknown
        pass

    def keyboardGrabber(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def layout(self, *args, **kwargs): # real signature unknown
        pass

    def layoutDirection(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def locale(self, *args, **kwargs): # real signature unknown
        pass

    def lower(self, *args, **kwargs): # real signature unknown
        pass

    def macCGHandle(self, *args, **kwargs): # real signature unknown
        pass

    def macQDHandle(self, *args, **kwargs): # real signature unknown
        pass

    def mapFrom(self, *args, **kwargs): # real signature unknown
        pass

    def mapFromGlobal(self, *args, **kwargs): # real signature unknown
        pass

    def mapFromParent(self, *args, **kwargs): # real signature unknown
        pass

    def mapTo(self, *args, **kwargs): # real signature unknown
        pass

    def mapToGlobal(self, *args, **kwargs): # real signature unknown
        pass

    def mapToParent(self, *args, **kwargs): # real signature unknown
        pass

    def mask(self, *args, **kwargs): # real signature unknown
        pass

    def maximumHeight(self, *args, **kwargs): # real signature unknown
        pass

    def maximumSize(self, *args, **kwargs): # real signature unknown
        pass

    def maximumWidth(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumHeight(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSize(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def minimumWidth(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseGrabber(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def move(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeParentWidget(self, *args, **kwargs): # real signature unknown
        pass

    def nextInFocusChain(self, *args, **kwargs): # real signature unknown
        pass

    def normalGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def overrideWindowFlags(self, *args, **kwargs): # real signature unknown
        pass

    def overrideWindowState(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def palette(self, *args, **kwargs): # real signature unknown
        pass

    def parentWidget(self, *args, **kwargs): # real signature unknown
        pass

    def pos(self, *args, **kwargs): # real signature unknown
        pass

    def previousInFocusChain(self, *args, **kwargs): # real signature unknown
        pass

    def raise_(self, *args, **kwargs): # real signature unknown
        pass

    def rect(self, *args, **kwargs): # real signature unknown
        pass

    def releaseKeyboard(self, *args, **kwargs): # real signature unknown
        pass

    def releaseMouse(self, *args, **kwargs): # real signature unknown
        pass

    def releaseShortcut(self, *args, **kwargs): # real signature unknown
        pass

    def removeAction(self, *args, **kwargs): # real signature unknown
        pass

    def render(self, *args, **kwargs): # real signature unknown
        pass

    def repaint(self, *args, **kwargs): # real signature unknown
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resize(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def restoreGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def saveGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def scroll(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptDrops(self, *args, **kwargs): # real signature unknown
        pass

    def setAccessibleDescription(self, *args, **kwargs): # real signature unknown
        pass

    def setAccessibleName(self, *args, **kwargs): # real signature unknown
        pass

    def setAttribute(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoFillBackground(self, *args, **kwargs): # real signature unknown
        pass

    def setBackgroundRole(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseSize(self, *args, **kwargs): # real signature unknown
        pass

    def setContentsMargins(self, *args, **kwargs): # real signature unknown
        pass

    def setContextMenuPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def setCursor(self, *args, **kwargs): # real signature unknown
        pass

    def setDisabled(self, *args, **kwargs): # real signature unknown
        pass

    def setEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def setFixedHeight(self, *args, **kwargs): # real signature unknown
        pass

    def setFixedSize(self, *args, **kwargs): # real signature unknown
        pass

    def setFixedWidth(self, *args, **kwargs): # real signature unknown
        pass

    def setFocus(self, *args, **kwargs): # real signature unknown
        pass

    def setFocusPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def setFocusProxy(self, *args, **kwargs): # real signature unknown
        pass

    def setFont(self, *args, **kwargs): # real signature unknown
        pass

    def setForegroundRole(self, *args, **kwargs): # real signature unknown
        pass

    def setGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def setGraphicsEffect(self, *args, **kwargs): # real signature unknown
        pass

    def setHidden(self, *args, **kwargs): # real signature unknown
        pass

    def setInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def setInputMethodHints(self, *args, **kwargs): # real signature unknown
        pass

    def setLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setLayoutDirection(self, *args, **kwargs): # real signature unknown
        pass

    def setLocale(self, *args, **kwargs): # real signature unknown
        pass

    def setMask(self, *args, **kwargs): # real signature unknown
        pass

    def setMaximumHeight(self, *args, **kwargs): # real signature unknown
        pass

    def setMaximumSize(self, *args, **kwargs): # real signature unknown
        pass

    def setMaximumWidth(self, *args, **kwargs): # real signature unknown
        pass

    def setMinimumHeight(self, *args, **kwargs): # real signature unknown
        pass

    def setMinimumSize(self, *args, **kwargs): # real signature unknown
        pass

    def setMinimumWidth(self, *args, **kwargs): # real signature unknown
        pass

    def setMouseTracking(self, *args, **kwargs): # real signature unknown
        pass

    def setPalette(self, *args, **kwargs): # real signature unknown
        pass

    def setParent(self, *args, **kwargs): # real signature unknown
        pass

    def setShortcutAutoRepeat(self, *args, **kwargs): # real signature unknown
        pass

    def setShortcutEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def setSizeIncrement(self, *args, **kwargs): # real signature unknown
        pass

    def setSizePolicy(self, *args, **kwargs): # real signature unknown
        pass

    def setStatusTip(self, *args, **kwargs): # real signature unknown
        pass

    def setStyle(self, *args, **kwargs): # real signature unknown
        pass

    def setStyleSheet(self, *args, **kwargs): # real signature unknown
        pass

    def setTabOrder(self, *args, **kwargs): # real signature unknown
        pass

    def setToolTip(self, *args, **kwargs): # real signature unknown
        pass

    def setUpdatesEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def setVisible(self, *args, **kwargs): # real signature unknown
        pass

    def setWhatsThis(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowFilePath(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowFlags(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowIcon(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowIconText(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowModality(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowModified(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowOpacity(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowRole(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowState(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowTitle(self, *args, **kwargs): # real signature unknown
        pass

    def show(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def showFullScreen(self, *args, **kwargs): # real signature unknown
        pass

    def showMaximized(self, *args, **kwargs): # real signature unknown
        pass

    def showMinimized(self, *args, **kwargs): # real signature unknown
        pass

    def showNormal(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def sizeIncrement(self, *args, **kwargs): # real signature unknown
        pass

    def sizePolicy(self, *args, **kwargs): # real signature unknown
        pass

    def stackUnder(self, *args, **kwargs): # real signature unknown
        pass

    def statusTip(self, *args, **kwargs): # real signature unknown
        pass

    def style(self, *args, **kwargs): # real signature unknown
        pass

    def styleSheet(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testAttribute(self, *args, **kwargs): # real signature unknown
        pass

    def toolTip(self, *args, **kwargs): # real signature unknown
        pass

    def underMouse(self, *args, **kwargs): # real signature unknown
        pass

    def ungrabGesture(self, *args, **kwargs): # real signature unknown
        pass

    def unsetCursor(self, *args, **kwargs): # real signature unknown
        pass

    def unsetLayoutDirection(self, *args, **kwargs): # real signature unknown
        pass

    def unsetLocale(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def updatesEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def visibleRegion(self, *args, **kwargs): # real signature unknown
        pass

    def whatsThis(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def width(self, *args, **kwargs): # real signature unknown
        pass

    def window(self, *args, **kwargs): # real signature unknown
        pass

    def windowFilePath(self, *args, **kwargs): # real signature unknown
        pass

    def windowFlags(self, *args, **kwargs): # real signature unknown
        pass

    def windowIcon(self, *args, **kwargs): # real signature unknown
        pass

    def windowIconText(self, *args, **kwargs): # real signature unknown
        pass

    def windowModality(self, *args, **kwargs): # real signature unknown
        pass

    def windowOpacity(self, *args, **kwargs): # real signature unknown
        pass

    def windowRole(self, *args, **kwargs): # real signature unknown
        pass

    def windowState(self, *args, **kwargs): # real signature unknown
        pass

    def windowTitle(self, *args, **kwargs): # real signature unknown
        pass

    def windowType(self, *args, **kwargs): # real signature unknown
        pass

    def winId(self, *args, **kwargs): # real signature unknown
        pass

    def x(self, *args, **kwargs): # real signature unknown
        pass

    def y(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    customContextMenuRequested = None
    DrawChildren = None
    DrawWindowBackground = None
    IgnoreMask = None
    RenderFlag = None
    RenderFlags = None
    staticMetaObject = None
    __new__ = None


class QGLWidget(__PySide_QtGui.QWidget):
    # no doc
    def autoBufferSwap(self, *args, **kwargs): # real signature unknown
        pass

    def bindTexture(self, *args, **kwargs): # real signature unknown
        pass

    def colormap(self, *args, **kwargs): # real signature unknown
        pass

    def context(self, *args, **kwargs): # real signature unknown
        pass

    def convertToGLFormat(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def doubleBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def glDraw(self, *args, **kwargs): # real signature unknown
        pass

    def glInit(self, *args, **kwargs): # real signature unknown
        pass

    def grabFrameBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def initializeGL(self, *args, **kwargs): # real signature unknown
        pass

    def initializeOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def isSharing(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def makeOverlayCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def overlayContext(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintGL(self, *args, **kwargs): # real signature unknown
        pass

    def paintOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def qglClearColor(self, *args, **kwargs): # real signature unknown
        pass

    def qglColor(self, *args, **kwargs): # real signature unknown
        pass

    def renderPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def renderText(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeGL(self, *args, **kwargs): # real signature unknown
        pass

    def resizeOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoBufferSwap(self, *args, **kwargs): # real signature unknown
        pass

    def setColormap(self, *args, **kwargs): # real signature unknown
        pass

    def setMouseTracking(self, *args, **kwargs): # real signature unknown
        pass

    def swapBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def updateGL(self, *args, **kwargs): # real signature unknown
        pass

    def updateOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    __new__ = None


