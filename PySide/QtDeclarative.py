# encoding: utf-8
# module PySide.QtDeclarative
# from /corp.blizzard.net/BFD/Deploy/Packages/Published/ThirdParty/Qt4.8.4/2015-05-15.163857/prebuilt/linux_x64_gcc41_python2.7_ucs4/PySide/QtDeclarative.so
# by generator 1.138
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import PySide.QtGui as __PySide_QtGui


# Variables with simple values

QML_HAS_ATTACHED_PROPERTIES = 1

# functions

def qmlRegisterType(*args, **kwargs): # reliably restored by inspect
    # no doc
    pass

# classes

class _Property(object):
    # no doc
    def getter(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def setter(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __new__ = None


class ListProperty(_Property):
    # no doc
    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass


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


class QDeclarativeComponent(__PySide_QtCore.QObject):
    # no doc
    def beginCreate(self, *args, **kwargs): # real signature unknown
        pass

    def completeCreate(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def creationContext(self, *args, **kwargs): # real signature unknown
        pass

    def errors(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def isError(self, *args, **kwargs): # real signature unknown
        pass

    def isLoading(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isReady(self, *args, **kwargs): # real signature unknown
        pass

    def loadUrl(self, *args, **kwargs): # real signature unknown
        pass

    def progress(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def status(self, *args, **kwargs): # real signature unknown
        pass

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    Error = None
    Loading = None
    Null = None
    progressChanged = None
    Ready = None
    staticMetaObject = None
    Status = None
    statusChanged = None
    __new__ = None


class QDeclarativeContext(__PySide_QtCore.QObject):
    # no doc
    def baseUrl(self, *args, **kwargs): # real signature unknown
        pass

    def contextObject(self, *args, **kwargs): # real signature unknown
        pass

    def contextProperty(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def parentContext(self, *args, **kwargs): # real signature unknown
        pass

    def resolvedUrl(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseUrl(self, *args, **kwargs): # real signature unknown
        pass

    def setContextObject(self, *args, **kwargs): # real signature unknown
        pass

    def setContextProperty(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    __new__ = None


class QDeclarativeEngine(__PySide_QtCore.QObject):
    # no doc
    def addImageProvider(self, *args, **kwargs): # real signature unknown
        pass

    def addImportPath(self, *args, **kwargs): # real signature unknown
        pass

    def addPluginPath(self, *args, **kwargs): # real signature unknown
        pass

    def baseUrl(self, *args, **kwargs): # real signature unknown
        pass

    def clearComponentCache(self, *args, **kwargs): # real signature unknown
        pass

    def contextForObject(self, *args, **kwargs): # real signature unknown
        pass

    def imageProvider(self, *args, **kwargs): # real signature unknown
        pass

    def importPathList(self, *args, **kwargs): # real signature unknown
        pass

    def importPlugin(self, *args, **kwargs): # real signature unknown
        pass

    def networkAccessManager(self, *args, **kwargs): # real signature unknown
        pass

    def networkAccessManagerFactory(self, *args, **kwargs): # real signature unknown
        pass

    def objectOwnership(self, *args, **kwargs): # real signature unknown
        pass

    def offlineStoragePath(self, *args, **kwargs): # real signature unknown
        pass

    def outputWarningsToStandardError(self, *args, **kwargs): # real signature unknown
        pass

    def pluginPathList(self, *args, **kwargs): # real signature unknown
        pass

    def removeImageProvider(self, *args, **kwargs): # real signature unknown
        pass

    def rootContext(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseUrl(self, *args, **kwargs): # real signature unknown
        pass

    def setContextForObject(self, *args, **kwargs): # real signature unknown
        pass

    def setImportPathList(self, *args, **kwargs): # real signature unknown
        pass

    def setNetworkAccessManagerFactory(self, *args, **kwargs): # real signature unknown
        pass

    def setObjectOwnership(self, *args, **kwargs): # real signature unknown
        pass

    def setOfflineStoragePath(self, *args, **kwargs): # real signature unknown
        pass

    def setOutputWarningsToStandardError(self, *args, **kwargs): # real signature unknown
        pass

    def setPluginPathList(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    CppOwnership = None
    JavaScriptOwnership = None
    ObjectOwnership = None
    quit = None
    staticMetaObject = None
    warnings = None
    __new__ = None


class _Object(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class QDeclarativeError(_Object):
    # no doc
    def column(self, *args, **kwargs): # real signature unknown
        pass

    def description(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def line(self, *args, **kwargs): # real signature unknown
        pass

    def setColumn(self, *args, **kwargs): # real signature unknown
        pass

    def setDescription(self, *args, **kwargs): # real signature unknown
        pass

    def setLine(self, *args, **kwargs): # real signature unknown
        pass

    def setUrl(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self, *args, **kwargs): # real signature unknown
        pass

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __new__ = None


class QDeclarativeExpression(__PySide_QtCore.QObject):
    # no doc
    def clearError(self, *args, **kwargs): # real signature unknown
        pass

    def context(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def evaluate(self, *args, **kwargs): # real signature unknown
        pass

    def expression(self, *args, **kwargs): # real signature unknown
        pass

    def hasError(self, *args, **kwargs): # real signature unknown
        pass

    def lineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def notifyOnValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def scopeObject(self, *args, **kwargs): # real signature unknown
        pass

    def setExpression(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyOnValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setSourceLocation(self, *args, **kwargs): # real signature unknown
        pass

    def sourceFile(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    valueChanged = None
    __new__ = None


class QDeclarativeExtensionInterface(_Object):
    # no doc
    def initializeEngine(self, *args, **kwargs): # real signature unknown
        pass

    def registerTypes(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class QDeclarativeExtensionPlugin(__PySide_QtCore.QObject, QDeclarativeExtensionInterface):
    # no doc
    def initializeEngine(self, *args, **kwargs): # real signature unknown
        pass

    def registerTypes(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    __new__ = None


class QDeclarativeImageProvider(_Object):
    # no doc
    def imageType(self, *args, **kwargs): # real signature unknown
        pass

    def requestImage(self, *args, **kwargs): # real signature unknown
        pass

    def requestPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    Image = None
    ImageType = None
    Pixmap = None
    __new__ = None


class QDeclarativeParserStatus(_Object):
    # no doc
    def classBegin(self, *args, **kwargs): # real signature unknown
        pass

    def componentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class _QGraphicsObject(__PySide_QtCore.QObject, __PySide_QtGui.QGraphicsItem):
    # no doc
    def grabGesture(self, *args, **kwargs): # real signature unknown
        pass

    def ungrabGesture(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    childrenChanged = None
    enabledChanged = None
    heightChanged = None
    opacityChanged = None
    parentChanged = None
    rotationChanged = None
    scaleChanged = None
    staticMetaObject = None
    visibleChanged = None
    widthChanged = None
    xChanged = None
    yChanged = None
    zChanged = None
    __new__ = None


class QDeclarativeItem(__PySide_QtGui.QGraphicsObject, QDeclarativeParserStatus):
    # no doc
    def baselineOffset(self, *args, **kwargs): # real signature unknown
        pass

    def boundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def childAt(self, *args, **kwargs): # real signature unknown
        pass

    def childrenRect(self, *args, **kwargs): # real signature unknown
        pass

    def classBegin(self, *args, **kwargs): # real signature unknown
        pass

    def clip(self, *args, **kwargs): # real signature unknown
        pass

    def componentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def forceActiveFocus(self, *args, **kwargs): # real signature unknown
        pass

    def geometryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def hasActiveFocus(self, *args, **kwargs): # real signature unknown
        pass

    def hasFocus(self, *args, **kwargs): # real signature unknown
        pass

    def height(self, *args, **kwargs): # real signature unknown
        pass

    def heightValid(self, *args, **kwargs): # real signature unknown
        pass

    def implicitHeight(self, *args, **kwargs): # real signature unknown
        pass

    def implicitWidth(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodPreHandler(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def isComponentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, *args, **kwargs): # real signature unknown
        pass

    def keepMouseGrab(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressPreHandler(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleasePreHandler(self, *args, **kwargs): # real signature unknown
        pass

    def paint(self, *args, **kwargs): # real signature unknown
        pass

    def parentItem(self, *args, **kwargs): # real signature unknown
        pass

    def resetHeight(self, *args, **kwargs): # real signature unknown
        pass

    def resetWidth(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def setBaselineOffset(self, *args, **kwargs): # real signature unknown
        pass

    def setClip(self, *args, **kwargs): # real signature unknown
        pass

    def setFocus(self, *args, **kwargs): # real signature unknown
        pass

    def setHeight(self, *args, **kwargs): # real signature unknown
        pass

    def setImplicitHeight(self, *args, **kwargs): # real signature unknown
        pass

    def setImplicitWidth(self, *args, **kwargs): # real signature unknown
        pass

    def setKeepMouseGrab(self, *args, **kwargs): # real signature unknown
        pass

    def setParentItem(self, *args, **kwargs): # real signature unknown
        pass

    def setSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSmooth(self, *args, **kwargs): # real signature unknown
        pass

    def setTransformOrigin(self, *args, **kwargs): # real signature unknown
        pass

    def setWidth(self, *args, **kwargs): # real signature unknown
        pass

    def smooth(self, *args, **kwargs): # real signature unknown
        pass

    def transformOrigin(self, *args, **kwargs): # real signature unknown
        pass

    def width(self, *args, **kwargs): # real signature unknown
        pass

    def widthValid(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    activeFocusChanged = None
    baselineOffsetChanged = None
    Bottom = None
    BottomLeft = None
    BottomRight = None
    Center = None
    childrenRectChanged = None
    clipChanged = None
    focusChanged = None
    implicitHeightChanged = None
    implicitWidthChanged = None
    Left = None
    parentChanged = None
    Right = None
    smoothChanged = None
    stateChanged = None
    staticMetaObject = None
    Top = None
    TopLeft = None
    TopRight = None
    TransformOrigin = None
    transformOriginChanged = None
    __new__ = None


class QDeclarativeListReference(_Object):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def at(self, *args, **kwargs): # real signature unknown
        pass

    def canAppend(self, *args, **kwargs): # real signature unknown
        pass

    def canAt(self, *args, **kwargs): # real signature unknown
        pass

    def canClear(self, *args, **kwargs): # real signature unknown
        pass

    def canCount(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def listElementType(self, *args, **kwargs): # real signature unknown
        pass

    def object(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class QDeclarativeNetworkAccessManagerFactory(_Object):
    # no doc
    def create(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class QDeclarativeProperty(_Object):
    # no doc
    def connectNotifySignal(self, *args, **kwargs): # real signature unknown
        pass

    def hasNotifySignal(self, *args, **kwargs): # real signature unknown
        pass

    def index(self, *args, **kwargs): # real signature unknown
        pass

    def isDesignable(self, *args, **kwargs): # real signature unknown
        pass

    def isProperty(self, *args, **kwargs): # real signature unknown
        pass

    def isResettable(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalProperty(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def isWritable(self, *args, **kwargs): # real signature unknown
        pass

    def method(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def needsNotifySignal(self, *args, **kwargs): # real signature unknown
        pass

    def object(self, *args, **kwargs): # real signature unknown
        pass

    def property(self, *args, **kwargs): # real signature unknown
        pass

    def propertyType(self, *args, **kwargs): # real signature unknown
        pass

    def propertyTypeCategory(self, *args, **kwargs): # real signature unknown
        pass

    def propertyTypeName(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
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

    Invalid = None
    InvalidCategory = None
    List = None
    Normal = None
    Object = None
    Property = None
    PropertyTypeCategory = None
    SignalProperty = None
    Type = None
    __new__ = None


class QDeclarativePropertyMap(__PySide_QtCore.QObject):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    valueChanged = None
    __new__ = None


class QDeclarativePropertyValueSource(_Object):
    # no doc
    def setTarget(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class QDeclarativeScriptString(_Object):
    # no doc
    def context(self, *args, **kwargs): # real signature unknown
        pass

    def scopeObject(self, *args, **kwargs): # real signature unknown
        pass

    def script(self, *args, **kwargs): # real signature unknown
        pass

    def setContext(self, *args, **kwargs): # real signature unknown
        pass

    def setScopeObject(self, *args, **kwargs): # real signature unknown
        pass

    def setScript(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class _QGraphicsView(__PySide_QtGui.QAbstractScrollArea):
    # no doc
    def alignment(self, *args, **kwargs): # real signature unknown
        pass

    def backgroundBrush(self, *args, **kwargs): # real signature unknown
        pass

    def cacheMode(self, *args, **kwargs): # real signature unknown
        pass

    def centerOn(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMode(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawBackground(self, *args, **kwargs): # real signature unknown
        pass

    def drawForeground(self, *args, **kwargs): # real signature unknown
        pass

    def drawItems(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def ensureVisible(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def fitInView(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def foregroundBrush(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def invalidateScene(self, *args, **kwargs): # real signature unknown
        pass

    def isInteractive(self, *args, **kwargs): # real signature unknown
        pass

    def isTransformed(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, *args, **kwargs): # real signature unknown
        pass

    def items(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mapFromScene(self, *args, **kwargs): # real signature unknown
        pass

    def mapToScene(self, *args, **kwargs): # real signature unknown
        pass

    def matrix(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def optimizationFlags(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def render(self, *args, **kwargs): # real signature unknown
        pass

    def renderHints(self, *args, **kwargs): # real signature unknown
        pass

    def resetCachedContent(self, *args, **kwargs): # real signature unknown
        pass

    def resetMatrix(self, *args, **kwargs): # real signature unknown
        pass

    def resetTransform(self, *args, **kwargs): # real signature unknown
        pass

    def resizeAnchor(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        pass

    def rubberBandSelectionMode(self, *args, **kwargs): # real signature unknown
        pass

    def scale(self, *args, **kwargs): # real signature unknown
        pass

    def scene(self, *args, **kwargs): # real signature unknown
        pass

    def sceneRect(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, *args, **kwargs): # real signature unknown
        pass

    def setAlignment(self, *args, **kwargs): # real signature unknown
        pass

    def setBackgroundBrush(self, *args, **kwargs): # real signature unknown
        pass

    def setCacheMode(self, *args, **kwargs): # real signature unknown
        pass

    def setDragMode(self, *args, **kwargs): # real signature unknown
        pass

    def setForegroundBrush(self, *args, **kwargs): # real signature unknown
        pass

    def setInteractive(self, *args, **kwargs): # real signature unknown
        pass

    def setMatrix(self, *args, **kwargs): # real signature unknown
        pass

    def setOptimizationFlag(self, *args, **kwargs): # real signature unknown
        pass

    def setOptimizationFlags(self, *args, **kwargs): # real signature unknown
        pass

    def setRenderHint(self, *args, **kwargs): # real signature unknown
        pass

    def setRenderHints(self, *args, **kwargs): # real signature unknown
        pass

    def setResizeAnchor(self, *args, **kwargs): # real signature unknown
        pass

    def setRubberBandSelectionMode(self, *args, **kwargs): # real signature unknown
        pass

    def setScene(self, *args, **kwargs): # real signature unknown
        pass

    def setSceneRect(self, *args, **kwargs): # real signature unknown
        pass

    def setTransform(self, *args, **kwargs): # real signature unknown
        pass

    def setTransformationAnchor(self, *args, **kwargs): # real signature unknown
        pass

    def setupViewport(self, *args, **kwargs): # real signature unknown
        pass

    def setViewportUpdateMode(self, *args, **kwargs): # real signature unknown
        pass

    def shear(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def transform(self, *args, **kwargs): # real signature unknown
        pass

    def transformationAnchor(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        pass

    def updateScene(self, *args, **kwargs): # real signature unknown
        pass

    def updateSceneRect(self, *args, **kwargs): # real signature unknown
        pass

    def viewportEvent(self, *args, **kwargs): # real signature unknown
        pass

    def viewportTransform(self, *args, **kwargs): # real signature unknown
        pass

    def viewportUpdateMode(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    AnchorUnderMouse = None
    AnchorViewCenter = None
    BoundingRectViewportUpdate = None
    CacheBackground = None
    CacheMode = None
    CacheModeFlag = None
    CacheNone = None
    DontAdjustForAntialiasing = None
    DontClipPainter = None
    DontSavePainterState = None
    DragMode = None
    FullViewportUpdate = None
    IndirectPainting = None
    MinimalViewportUpdate = None
    NoAnchor = None
    NoDrag = None
    NoViewportUpdate = None
    OptimizationFlag = None
    OptimizationFlags = None
    RubberBandDrag = None
    ScrollHandDrag = None
    SmartViewportUpdate = None
    staticMetaObject = None
    ViewportAnchor = None
    ViewportUpdateMode = None
    __new__ = None


class QDeclarativeView(__PySide_QtGui.QGraphicsView):
    # no doc
    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def errors(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def initialSize(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeMode(self, *args, **kwargs): # real signature unknown
        pass

    def rootContext(self, *args, **kwargs): # real signature unknown
        pass

    def rootObject(self, *args, **kwargs): # real signature unknown
        pass

    def setResizeMode(self, *args, **kwargs): # real signature unknown
        pass

    def setRootObject(self, *args, **kwargs): # real signature unknown
        pass

    def setSource(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def source(self, *args, **kwargs): # real signature unknown
        pass

    def status(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    Error = None
    Loading = None
    Null = None
    Ready = None
    ResizeMode = None
    sceneResized = None
    SizeRootObjectToView = None
    SizeViewToRootObject = None
    staticMetaObject = None
    Status = None
    statusChanged = None
    __new__ = None


