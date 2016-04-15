# encoding: utf-8
# module PySide.QtMultimedia
# from /corp.blizzard.net/BFD/Deploy/Packages/Published/ThirdParty/Qt4.8.4/2015-05-15.163857/prebuilt/linux_x64_gcc41_python2.7_ucs4/PySide/QtMultimedia.so
# by generator 1.138
# no doc

# imports
import PySide.QtCore as __PySide_QtCore


# no functions
# classes

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


class QAbstractAudioDeviceInfo(__PySide_QtCore.QObject):
    # no doc
    def byteOrderList(self, *args, **kwargs): # real signature unknown
        pass

    def channelsList(self, *args, **kwargs): # real signature unknown
        pass

    def codecList(self, *args, **kwargs): # real signature unknown
        pass

    def deviceName(self, *args, **kwargs): # real signature unknown
        pass

    def frequencyList(self, *args, **kwargs): # real signature unknown
        pass

    def isFormatSupported(self, *args, **kwargs): # real signature unknown
        pass

    def nearestFormat(self, *args, **kwargs): # real signature unknown
        pass

    def preferredFormat(self, *args, **kwargs): # real signature unknown
        pass

    def sampleSizeList(self, *args, **kwargs): # real signature unknown
        pass

    def sampleTypeList(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    __new__ = None


class QAbstractAudioInput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesReady(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    notify = None
    stateChanged = None
    staticMetaObject = None
    __new__ = None


class QAbstractAudioOutput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesFree(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    notify = None
    stateChanged = None
    staticMetaObject = None
    __new__ = None


class _Object(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class QAbstractVideoBuffer(_Object):
    # no doc
    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def handleType(self, *args, **kwargs): # real signature unknown
        pass

    def mapMode(self, *args, **kwargs): # real signature unknown
        pass

    def unmap(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    CoreImageHandle = None
    GLTextureHandle = None
    HandleType = None
    MapMode = None
    NoHandle = None
    NotMapped = None
    QPixmapHandle = None
    ReadOnly = None
    ReadWrite = None
    UserHandle = None
    WriteOnly = None
    XvShmImageHandle = None
    __new__ = None


class QAbstractVideoSurface(__PySide_QtCore.QObject):
    # no doc
    def error(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        pass

    def isFormatSupported(self, *args, **kwargs): # real signature unknown
        pass

    def nearestFormat(self, *args, **kwargs): # real signature unknown
        pass

    def present(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def supportedPixelFormats(self, *args, **kwargs): # real signature unknown
        pass

    def surfaceFormat(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    activeChanged = None
    Error = None
    IncorrectFormatError = None
    NoError = None
    ResourceError = None
    staticMetaObject = None
    StoppedError = None
    supportedFormatsChanged = None
    surfaceFormatChanged = None
    UnsupportedFormatError = None
    __new__ = None


class QAudio(_Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ActiveState = None
    AudioInput = None
    AudioOutput = None
    Error = None
    FatalError = None
    IdleState = None
    IOError = None
    Mode = None
    NoError = None
    OpenError = None
    State = None
    StoppedState = None
    SuspendedState = None
    UnderrunError = None


class QAudioDeviceInfo(_Object):
    # no doc
    def availableDevices(self, *args, **kwargs): # real signature unknown
        pass

    def defaultInputDevice(self, *args, **kwargs): # real signature unknown
        pass

    def defaultOutputDevice(self, *args, **kwargs): # real signature unknown
        pass

    def deviceName(self, *args, **kwargs): # real signature unknown
        pass

    def isFormatSupported(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def nearestFormat(self, *args, **kwargs): # real signature unknown
        pass

    def preferredFormat(self, *args, **kwargs): # real signature unknown
        pass

    def supportedByteOrders(self, *args, **kwargs): # real signature unknown
        pass

    def supportedChannelCounts(self, *args, **kwargs): # real signature unknown
        pass

    def supportedChannels(self, *args, **kwargs): # real signature unknown
        pass

    def supportedCodecs(self, *args, **kwargs): # real signature unknown
        pass

    def supportedFrequencies(self, *args, **kwargs): # real signature unknown
        pass

    def supportedSampleRates(self, *args, **kwargs): # real signature unknown
        pass

    def supportedSampleSizes(self, *args, **kwargs): # real signature unknown
        pass

    def supportedSampleTypes(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    __new__ = None


class _QFactoryInterface(__PySide_QtCore._Object):
    # no doc
    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class QAudioEngineFactoryInterface(__PySide_QtCore.QFactoryInterface):
    # no doc
    def availableDevices(self, *args, **kwargs): # real signature unknown
        pass

    def createDeviceInfo(self, *args, **kwargs): # real signature unknown
        pass

    def createInput(self, *args, **kwargs): # real signature unknown
        pass

    def createOutput(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class QAudioEnginePlugin(__PySide_QtCore.QObject, QAudioEngineFactoryInterface):
    # no doc
    def availableDevices(self, *args, **kwargs): # real signature unknown
        pass

    def createDeviceInfo(self, *args, **kwargs): # real signature unknown
        pass

    def createInput(self, *args, **kwargs): # real signature unknown
        pass

    def createOutput(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    __new__ = None


class QAudioFormat(_Object):
    # no doc
    def byteOrder(self, *args, **kwargs): # real signature unknown
        pass

    def channelCount(self, *args, **kwargs): # real signature unknown
        pass

    def channels(self, *args, **kwargs): # real signature unknown
        pass

    def codec(self, *args, **kwargs): # real signature unknown
        pass

    def frequency(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def sampleRate(self, *args, **kwargs): # real signature unknown
        pass

    def sampleSize(self, *args, **kwargs): # real signature unknown
        pass

    def sampleType(self, *args, **kwargs): # real signature unknown
        pass

    def setByteOrder(self, *args, **kwargs): # real signature unknown
        pass

    def setChannelCount(self, *args, **kwargs): # real signature unknown
        pass

    def setChannels(self, *args, **kwargs): # real signature unknown
        pass

    def setCodec(self, *args, **kwargs): # real signature unknown
        pass

    def setFrequency(self, *args, **kwargs): # real signature unknown
        pass

    def setSampleRate(self, *args, **kwargs): # real signature unknown
        pass

    def setSampleSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSampleType(self, *args, **kwargs): # real signature unknown
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

    BigEndian = None
    Endian = None
    Float = None
    LittleEndian = None
    SampleType = None
    SignedInt = None
    Unknown = None
    UnSignedInt = None
    __new__ = None


class QAudioInput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesReady(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    notify = None
    stateChanged = None
    staticMetaObject = None
    __new__ = None


class QAudioOutput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesFree(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    notify = None
    stateChanged = None
    staticMetaObject = None
    __new__ = None


class QVideoFrame(_Object):
    # no doc
    def bits(self, *args, **kwargs): # real signature unknown
        pass

    def bytesPerLine(self, *args, **kwargs): # real signature unknown
        pass

    def endTime(self, *args, **kwargs): # real signature unknown
        pass

    def fieldType(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def handleType(self, *args, **kwargs): # real signature unknown
        pass

    def height(self, *args, **kwargs): # real signature unknown
        pass

    def imageFormatFromPixelFormat(self, *args, **kwargs): # real signature unknown
        pass

    def isMapped(self, *args, **kwargs): # real signature unknown
        pass

    def isReadable(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def isWritable(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def mapMode(self, *args, **kwargs): # real signature unknown
        pass

    def mappedBytes(self, *args, **kwargs): # real signature unknown
        pass

    def pixelFormat(self, *args, **kwargs): # real signature unknown
        pass

    def pixelFormatFromImageFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setEndTime(self, *args, **kwargs): # real signature unknown
        pass

    def setFieldType(self, *args, **kwargs): # real signature unknown
        pass

    def setStartTime(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def startTime(self, *args, **kwargs): # real signature unknown
        pass

    def unmap(self, *args, **kwargs): # real signature unknown
        pass

    def width(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    BottomField = None
    FieldType = None
    Format_ARGB32 = None
    Format_ARGB32_Premultiplied = None
    Format_ARGB8565_Premultiplied = None
    Format_AYUV444 = None
    Format_AYUV444_Premultiplied = None
    Format_BGR24 = None
    Format_BGR32 = None
    Format_BGR555 = None
    Format_BGR565 = None
    Format_BGRA32 = None
    Format_BGRA32_Premultiplied = None
    Format_BGRA5658_Premultiplied = None
    Format_IMC1 = None
    Format_IMC2 = None
    Format_IMC3 = None
    Format_IMC4 = None
    Format_Invalid = None
    Format_NV12 = None
    Format_NV21 = None
    Format_RGB24 = None
    Format_RGB32 = None
    Format_RGB555 = None
    Format_RGB565 = None
    Format_User = None
    Format_UYVY = None
    Format_Y16 = None
    Format_Y8 = None
    Format_YUV420P = None
    Format_YUV444 = None
    Format_YUYV = None
    Format_YV12 = None
    InterlacedFrame = None
    PixelFormat = None
    ProgressiveFrame = None
    TopField = None
    __new__ = None


class QVideoSurfaceFormat(_Object):
    # no doc
    def frameHeight(self, *args, **kwargs): # real signature unknown
        pass

    def frameRate(self, *args, **kwargs): # real signature unknown
        pass

    def frameSize(self, *args, **kwargs): # real signature unknown
        pass

    def frameWidth(self, *args, **kwargs): # real signature unknown
        pass

    def handleType(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def pixelAspectRatio(self, *args, **kwargs): # real signature unknown
        pass

    def pixelFormat(self, *args, **kwargs): # real signature unknown
        pass

    def property(self, *args, **kwargs): # real signature unknown
        pass

    def propertyNames(self, *args, **kwargs): # real signature unknown
        pass

    def scanLineDirection(self, *args, **kwargs): # real signature unknown
        pass

    def setFrameRate(self, *args, **kwargs): # real signature unknown
        pass

    def setFrameSize(self, *args, **kwargs): # real signature unknown
        pass

    def setPixelAspectRatio(self, *args, **kwargs): # real signature unknown
        pass

    def setProperty(self, *args, **kwargs): # real signature unknown
        pass

    def setScanLineDirection(self, *args, **kwargs): # real signature unknown
        pass

    def setViewport(self, *args, **kwargs): # real signature unknown
        pass

    def setYCbCrColorSpace(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def viewport(self, *args, **kwargs): # real signature unknown
        pass

    def yCbCrColorSpace(self, *args, **kwargs): # real signature unknown
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

    BottomToTop = None
    Direction = None
    TopToBottom = None
    YCbCrColorSpace = None
    YCbCr_BT601 = None
    YCbCr_BT709 = None
    YCbCr_CustomMatrix = None
    YCbCr_JPEG = None
    YCbCr_Undefined = None
    YCbCr_xvYCC601 = None
    YCbCr_xvYCC709 = None
    __new__ = None


