# encoding: utf-8
# module PySide.QtSql
# from /corp.blizzard.net/BFD/Deploy/Packages/Published/ThirdParty/Qt4.8.4/2015-05-15.163857/prebuilt/linux_x64_gcc41_python2.7_ucs4/PySide/QtSql.so
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


class QSql(_Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AfterLastRow = None
    AllTables = None
    BeforeFirstRow = None
    Binary = None
    HighPrecision = None
    In = None
    InOut = None
    Location = None
    LowPrecisionDouble = None
    LowPrecisionInt32 = None
    LowPrecisionInt64 = None
    NumericalPrecisionPolicy = None
    Out = None
    ParamType = None
    ParamTypeFlag = None
    SystemTables = None
    Tables = None
    TableType = None
    Views = None


class QSqlDatabase(_Object):
    # no doc
    def addDatabase(self, *args, **kwargs): # real signature unknown
        pass

    def cloneDatabase(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        pass

    def connectionName(self, *args, **kwargs): # real signature unknown
        pass

    def connectionNames(self, *args, **kwargs): # real signature unknown
        pass

    def connectOptions(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, *args, **kwargs): # real signature unknown
        pass

    def database(self, *args, **kwargs): # real signature unknown
        pass

    def databaseName(self, *args, **kwargs): # real signature unknown
        pass

    def driver(self, *args, **kwargs): # real signature unknown
        pass

    def driverName(self, *args, **kwargs): # real signature unknown
        pass

    def drivers(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, *args, **kwargs): # real signature unknown
        pass

    def hostName(self, *args, **kwargs): # real signature unknown
        pass

    def isDriverAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def isOpen(self, *args, **kwargs): # real signature unknown
        pass

    def isOpenError(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def numericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def password(self, *args, **kwargs): # real signature unknown
        pass

    def port(self, *args, **kwargs): # real signature unknown
        pass

    def primaryIndex(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def registerSqlDriver(self, *args, **kwargs): # real signature unknown
        pass

    def removeDatabase(self, *args, **kwargs): # real signature unknown
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        pass

    def setConnectOptions(self, *args, **kwargs): # real signature unknown
        pass

    def setDatabaseName(self, *args, **kwargs): # real signature unknown
        pass

    def setHostName(self, *args, **kwargs): # real signature unknown
        pass

    def setNumericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def setPassword(self, *args, **kwargs): # real signature unknown
        pass

    def setPort(self, *args, **kwargs): # real signature unknown
        pass

    def setUserName(self, *args, **kwargs): # real signature unknown
        pass

    def tables(self, *args, **kwargs): # real signature unknown
        pass

    def transaction(self, *args, **kwargs): # real signature unknown
        pass

    def userName(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    defaultConnection = 'qt_sql_default_connection'
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


class QSqlDriver(__PySide_QtCore.QObject):
    # no doc
    def beginTransaction(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def commitTransaction(self, *args, **kwargs): # real signature unknown
        pass

    def createResult(self, *args, **kwargs): # real signature unknown
        pass

    def escapeIdentifier(self, *args, **kwargs): # real signature unknown
        pass

    def formatValue(self, *args, **kwargs): # real signature unknown
        pass

    def hasFeature(self, *args, **kwargs): # real signature unknown
        pass

    def isIdentifierEscaped(self, *args, **kwargs): # real signature unknown
        pass

    def isIdentifierEscapedImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def isOpen(self, *args, **kwargs): # real signature unknown
        pass

    def isOpenError(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def numericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def primaryIndex(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def rollbackTransaction(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setNumericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def setOpen(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenError(self, *args, **kwargs): # real signature unknown
        pass

    def sqlStatement(self, *args, **kwargs): # real signature unknown
        pass

    def stripDelimiters(self, *args, **kwargs): # real signature unknown
        pass

    def stripDelimitersImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def subscribedToNotifications(self, *args, **kwargs): # real signature unknown
        pass

    def subscribedToNotificationsImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def subscribeToNotification(self, *args, **kwargs): # real signature unknown
        pass

    def subscribeToNotificationImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def tables(self, *args, **kwargs): # real signature unknown
        pass

    def unsubscribeFromNotification(self, *args, **kwargs): # real signature unknown
        pass

    def unsubscribeFromNotificationImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    BatchOperations = None
    BLOB = None
    DeleteStatement = None
    DriverFeature = None
    EventNotifications = None
    FieldName = None
    FinishQuery = None
    IdentifierType = None
    InsertStatement = None
    LastInsertId = None
    LowPrecisionNumbers = None
    MultipleResultSets = None
    NamedPlaceholders = None
    notification = None
    PositionalPlaceholders = None
    PreparedQueries = None
    QuerySize = None
    SelectStatement = None
    SimpleLocking = None
    StatementType = None
    staticMetaObject = None
    TableName = None
    Transactions = None
    Unicode = None
    UpdateStatement = None
    WhereStatement = None
    __new__ = None


class QSqlDriverCreatorBase(_Object):
    # no doc
    def createObject(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class QSqlError(_Object):
    # no doc
    def databaseText(self, *args, **kwargs): # real signature unknown
        pass

    def driverText(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def number(self, *args, **kwargs): # real signature unknown
        pass

    def setDatabaseText(self, *args, **kwargs): # real signature unknown
        pass

    def setDriverText(self, *args, **kwargs): # real signature unknown
        pass

    def setNumber(self, *args, **kwargs): # real signature unknown
        pass

    def setType(self, *args, **kwargs): # real signature unknown
        pass

    def text(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    ConnectionError = None
    ErrorType = None
    NoError = None
    StatementError = None
    TransactionError = None
    UnknownError = None
    __new__ = None


class QSqlField(_Object):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def defaultValue(self, *args, **kwargs): # real signature unknown
        pass

    def isAutoValue(self, *args, **kwargs): # real signature unknown
        pass

    def isGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isReadOnly(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def length(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def precision(self, *args, **kwargs): # real signature unknown
        pass

    def requiredStatus(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoValue(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultValue(self, *args, **kwargs): # real signature unknown
        pass

    def setGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def setLength(self, *args, **kwargs): # real signature unknown
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        pass

    def setPrecision(self, *args, **kwargs): # real signature unknown
        pass

    def setReadOnly(self, *args, **kwargs): # real signature unknown
        pass

    def setRequired(self, *args, **kwargs): # real signature unknown
        pass

    def setRequiredStatus(self, *args, **kwargs): # real signature unknown
        pass

    def setSqlType(self, *args, **kwargs): # real signature unknown
        pass

    def setType(self, *args, **kwargs): # real signature unknown
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def typeID(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
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

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    Optional = None
    Required = None
    RequiredStatus = None
    Unknown = None
    __new__ = None


class QSqlRecord(_Object):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def clearValues(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def field(self, *args, **kwargs): # real signature unknown
        pass

    def fieldName(self, *args, **kwargs): # real signature unknown
        pass

    def indexOf(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        pass

    def isGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        pass

    def setGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def setNull(self, *args, **kwargs): # real signature unknown
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
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

    __new__ = None


class QSqlIndex(QSqlRecord):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def cursorName(self, *args, **kwargs): # real signature unknown
        pass

    def isDescending(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def setCursorName(self, *args, **kwargs): # real signature unknown
        pass

    def setDescending(self, *args, **kwargs): # real signature unknown
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class QSqlQuery(_Object):
    # no doc
    def addBindValue(self, *args, **kwargs): # real signature unknown
        pass

    def at(self, *args, **kwargs): # real signature unknown
        pass

    def bindValue(self, *args, **kwargs): # real signature unknown
        pass

    def boundValue(self, *args, **kwargs): # real signature unknown
        pass

    def boundValues(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def driver(self, *args, **kwargs): # real signature unknown
        pass

    def execBatch(self, *args, **kwargs): # real signature unknown
        pass

    def executedQuery(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, *args, **kwargs): # real signature unknown
        pass

    def finish(self, *args, **kwargs): # real signature unknown
        pass

    def first(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        pass

    def isForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isSelect(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def last(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def lastInsertId(self, *args, **kwargs): # real signature unknown
        pass

    def lastQuery(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def nextResult(self, *args, **kwargs): # real signature unknown
        pass

    def numericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def numRowsAffected(self, *args, **kwargs): # real signature unknown
        pass

    def prepare(self, *args, **kwargs): # real signature unknown
        pass

    def previous(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def result(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def setForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def setNumericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    BatchExecutionMode = None
    ValuesAsColumns = None
    ValuesAsRows = None
    __new__ = None


class _QAbstractTableModel(__PySide_QtCore.QAbstractItemModel):
    # no doc
    def dropMimeData(self, *args, **kwargs): # real signature unknown
        pass

    def hasChildren(self, *args, **kwargs): # real signature unknown
        pass

    def index(self, *args, **kwargs): # real signature unknown
        pass

    def parent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    __new__ = None


class QSqlQueryModel(__PySide_QtCore.QAbstractTableModel):
    # no doc
    def canFetchMore(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def columnCount(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def fetchMore(self, *args, **kwargs): # real signature unknown
        pass

    def headerData(self, *args, **kwargs): # real signature unknown
        pass

    def indexInQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def query(self, *args, **kwargs): # real signature unknown
        pass

    def queryChange(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self, *args, **kwargs): # real signature unknown
        pass

    def setHeaderData(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    __new__ = None


class QSqlRelation(_Object):
    # no doc
    def displayColumn(self, *args, **kwargs): # real signature unknown
        pass

    def indexColumn(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def tableName(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    __new__ = None


class _QItemDelegate(__PySide_QtGui.QAbstractItemDelegate):
    # no doc
    def check(self, *args, **kwargs): # real signature unknown
        pass

    def createEditor(self, *args, **kwargs): # real signature unknown
        pass

    def decoration(self, *args, **kwargs): # real signature unknown
        pass

    def drawBackground(self, *args, **kwargs): # real signature unknown
        pass

    def drawCheck(self, *args, **kwargs): # real signature unknown
        pass

    def drawDecoration(self, *args, **kwargs): # real signature unknown
        pass

    def drawDisplay(self, *args, **kwargs): # real signature unknown
        pass

    def drawFocus(self, *args, **kwargs): # real signature unknown
        pass

    def editorEvent(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def hasClipping(self, *args, **kwargs): # real signature unknown
        pass

    def itemEditorFactory(self, *args, **kwargs): # real signature unknown
        pass

    def paint(self, *args, **kwargs): # real signature unknown
        pass

    def rect(self, *args, **kwargs): # real signature unknown
        pass

    def setClipping(self, *args, **kwargs): # real signature unknown
        pass

    def setEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def setItemEditorFactory(self, *args, **kwargs): # real signature unknown
        pass

    def setModelData(self, *args, **kwargs): # real signature unknown
        pass

    def setOptions(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def textRectangle(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    __new__ = None


class QSqlRelationalDelegate(__PySide_QtGui.QItemDelegate):
    # no doc
    def createEditor(self, *args, **kwargs): # real signature unknown
        pass

    def setEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def setModelData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    __new__ = None


class QSqlTableModel(QSqlQueryModel):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def database(self, *args, **kwargs): # real signature unknown
        pass

    def deleteRowFromTable(self, *args, **kwargs): # real signature unknown
        pass

    def editStrategy(self, *args, **kwargs): # real signature unknown
        pass

    def fieldIndex(self, *args, **kwargs): # real signature unknown
        pass

    def filter(self, *args, **kwargs): # real signature unknown
        pass

    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def headerData(self, *args, **kwargs): # real signature unknown
        pass

    def indexInQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertRecord(self, *args, **kwargs): # real signature unknown
        pass

    def insertRowIntoTable(self, *args, **kwargs): # real signature unknown
        pass

    def insertRows(self, *args, **kwargs): # real signature unknown
        pass

    def isDirty(self, *args, **kwargs): # real signature unknown
        pass

    def orderByClause(self, *args, **kwargs): # real signature unknown
        pass

    def primaryKey(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, *args, **kwargs): # real signature unknown
        pass

    def removeRows(self, *args, **kwargs): # real signature unknown
        pass

    def revert(self, *args, **kwargs): # real signature unknown
        pass

    def revertAll(self, *args, **kwargs): # real signature unknown
        pass

    def revertRow(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *args, **kwargs): # real signature unknown
        pass

    def selectStatement(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def setEditStrategy(self, *args, **kwargs): # real signature unknown
        pass

    def setFilter(self, *args, **kwargs): # real signature unknown
        pass

    def setPrimaryKey(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setRecord(self, *args, **kwargs): # real signature unknown
        pass

    def setSort(self, *args, **kwargs): # real signature unknown
        pass

    def setTable(self, *args, **kwargs): # real signature unknown
        pass

    def sort(self, *args, **kwargs): # real signature unknown
        pass

    def submit(self, *args, **kwargs): # real signature unknown
        pass

    def submitAll(self, *args, **kwargs): # real signature unknown
        pass

    def tableName(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    beforeDelete = None
    beforeInsert = None
    beforeUpdate = None
    EditStrategy = None
    OnFieldChange = None
    OnManualSubmit = None
    OnRowChange = None
    primeInsert = None
    staticMetaObject = None
    __new__ = None


class QSqlRelationalTableModel(QSqlTableModel):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def insertRowIntoTable(self, *args, **kwargs): # real signature unknown
        pass

    def orderByClause(self, *args, **kwargs): # real signature unknown
        pass

    def relation(self, *args, **kwargs): # real signature unknown
        pass

    def relationModel(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, *args, **kwargs): # real signature unknown
        pass

    def revertRow(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *args, **kwargs): # real signature unknown
        pass

    def selectStatement(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def setRelation(self, *args, **kwargs): # real signature unknown
        pass

    def setTable(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    staticMetaObject = None
    __new__ = None


class QSqlResult(_Object):
    # no doc
    def addBindValue(self, *args, **kwargs): # real signature unknown
        pass

    def at(self, *args, **kwargs): # real signature unknown
        pass

    def bindingSyntax(self, *args, **kwargs): # real signature unknown
        pass

    def bindValue(self, *args, **kwargs): # real signature unknown
        pass

    def bindValueType(self, *args, **kwargs): # real signature unknown
        pass

    def boundValue(self, *args, **kwargs): # real signature unknown
        pass

    def boundValueCount(self, *args, **kwargs): # real signature unknown
        pass

    def boundValueName(self, *args, **kwargs): # real signature unknown
        pass

    def boundValues(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def detachFromResultSet(self, *args, **kwargs): # real signature unknown
        pass

    def driver(self, *args, **kwargs): # real signature unknown
        pass

    def execBatch(self, *args, **kwargs): # real signature unknown
        pass

    def executedQuery(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, *args, **kwargs): # real signature unknown
        pass

    def fetch(self, *args, **kwargs): # real signature unknown
        pass

    def fetchFirst(self, *args, **kwargs): # real signature unknown
        pass

    def fetchLast(self, *args, **kwargs): # real signature unknown
        pass

    def fetchNext(self, *args, **kwargs): # real signature unknown
        pass

    def fetchPrevious(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def hasOutValues(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        pass

    def isForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isSelect(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def lastInsertId(self, *args, **kwargs): # real signature unknown
        pass

    def lastQuery(self, *args, **kwargs): # real signature unknown
        pass

    def nextResult(self, *args, **kwargs): # real signature unknown
        pass

    def numericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def numRowsAffected(self, *args, **kwargs): # real signature unknown
        pass

    def prepare(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def savePrepare(self, *args, **kwargs): # real signature unknown
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        pass

    def setAt(self, *args, **kwargs): # real signature unknown
        pass

    def setForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setNumericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setSelect(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *more): # real signature unknown; restored from __doc__
        """ x.__init__(...) initializes x; see help(type(x)) for signature """
        pass

    BatchOperation = None
    BindingSyntax = None
    DetachFromResultSet = None
    NamedBinding = None
    NextResult = None
    PositionalBinding = None
    SetNumericalPrecision = None
    VirtualHookOperation = None
    __new__ = None


