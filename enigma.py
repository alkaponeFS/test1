# Embedded file name: /usr/lib/enigma2/python/enigma.py
from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _enigma.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):

    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_enigma', [dirname(__file__)])
        except ImportError:
            import _enigma
            return _enigma

        if fp is not None:
            try:
                _mod = imp.load_module('_enigma', fp, pathname, description)
            finally:
                fp.close()

            return _mod
        else:
            return


    _enigma = swig_import_helper()
    del swig_import_helper
else:
    import _enigma
del version_info
try:
    _swig_property = property
except NameError:
    pass

def _swig_setattr_nondynamic(self, class_type, name, value, static = 1):
    if name == 'thisown':
        return self.this.own(value)
    else:
        if name == 'this':
            if type(value).__name__ == 'SwigPyObject':
                self.__dict__[name] = value
                return
        method = class_type.__swig_setmethods__.get(name, None)
        if method:
            return method(self, value)
        if not static:
            self.__dict__[name] = value
        else:
            raise AttributeError('You cannot add attributes to %s' % self)
        return


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == 'thisown':
        return self.this.own()
    else:
        method = class_type.__swig_getmethods__.get(name, None)
        if method:
            return method(self)
        raise AttributeError(name)
        return


def _swig_repr(self):
    try:
        strthis = 'proxy of ' + self.this.__repr__()
    except:
        strthis = ''

    return '<%s.%s; %s >' % (self.__class__.__module__, self.__class__.__name__, strthis)


try:
    _object = object
    _newclass = 1
except AttributeError:

    class _object:
        pass


    _newclass = 0

def _swig_setattr_nondynamic_method(set):

    def set_attr(self, name, value):
        if name == 'thisown':
            return self.this.own(value)
        if hasattr(self, name) or name == 'this':
            set(self, name, value)
        else:
            raise AttributeError('You cannot add attributes to %s' % self)

    return set_attr


class iObject(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined - class is abstract')

    __repr__ = _swig_repr
    __swig_destroy__ = _enigma.delete_iObject


iObject_swigregister = _enigma.iObject_swigregister
iObject_swigregister(iObject)

class eEnv(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    resolve = staticmethod(_enigma.eEnv_resolve)

    def __init__(self):
        _enigma.eEnv_swiginit(self, _enigma.new_eEnv())

    __swig_destroy__ = _enigma.delete_eEnv


eEnv_swigregister = _enigma.eEnv_swigregister
eEnv_swigregister(eEnv)

def eEnv_resolve(*args):
    return _enigma.eEnv_resolve(*args)


eEnv_resolve = _enigma.eEnv_resolve
NULL = _enigma.NULL



def ePythonOutput(*args):
    return _enigma.ePythonOutput(*args)


ePythonOutput = _enigma.ePythonOutput


class eMainloop(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eMainloop_swiginit(self, _enigma.new_eMainloop())

    __swig_destroy__ = _enigma.delete_eMainloop


eMainloop.looplevel = new_instancemethod(_enigma.eMainloop_looplevel, None, eMainloop)
eMainloop.iterate = new_instancemethod(_enigma.eMainloop_iterate, None, eMainloop)
eMainloop.runLoop = new_instancemethod(_enigma.eMainloop_runLoop, None, eMainloop)
eMainloop.poll = new_instancemethod(_enigma.eMainloop_poll, None, eMainloop)
eMainloop.interruptPoll = new_instancemethod(_enigma.eMainloop_interruptPoll, None, eMainloop)
eMainloop.reset = new_instancemethod(_enigma.eMainloop_reset, None, eMainloop)
eMainloop.isIdle = new_instancemethod(_enigma.eMainloop_isIdle, None, eMainloop)
eMainloop.idleCount = new_instancemethod(_enigma.eMainloop_idleCount, None, eMainloop)
eMainloop_swigregister = _enigma.eMainloop_swigregister
eMainloop_swigregister(eMainloop)
cvar = _enigma.cvar

class eApplication(eMainloop):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eApplication_swiginit(self, _enigma.new_eApplication())

    __swig_destroy__ = _enigma.delete_eApplication


eApplication_swigregister = _enigma.eApplication_swigregister
eApplication_swigregister(eApplication)

def ptrAssert(*args):
    return _enigma.ptrAssert(*args)


ptrAssert = _enigma.ptrAssert

class eComponentDataPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eComponentDataPtr_swiginit(self, _enigma.new_eComponentDataPtr(*args))

    __swig_destroy__ = _enigma.delete_eComponentDataPtr


eComponentDataPtr.__ref__ = new_instancemethod(_enigma.eComponentDataPtr___ref__, None, eComponentDataPtr)
eComponentDataPtr.getPtrString = new_instancemethod(_enigma.eComponentDataPtr_getPtrString, None, eComponentDataPtr)
eComponentDataPtr.__deref__ = new_instancemethod(_enigma.eComponentDataPtr___deref__, None, eComponentDataPtr)
eComponentDataPtr.getStreamContent = new_instancemethod(_enigma.eComponentDataPtr_getStreamContent, None, eComponentDataPtr)
eComponentDataPtr.getComponentType = new_instancemethod(_enigma.eComponentDataPtr_getComponentType, None, eComponentDataPtr)
eComponentDataPtr.getComponentTag = new_instancemethod(_enigma.eComponentDataPtr_getComponentTag, None, eComponentDataPtr)
eComponentDataPtr.getIso639LanguageCode = new_instancemethod(_enigma.eComponentDataPtr_getIso639LanguageCode, None, eComponentDataPtr)
eComponentDataPtr.getText = new_instancemethod(_enigma.eComponentDataPtr_getText, None, eComponentDataPtr)
eComponentDataPtr_swigregister = _enigma.eComponentDataPtr_swigregister
eComponentDataPtr_swigregister(eComponentDataPtr)

class eGenreDataPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eGenreDataPtr_swiginit(self, _enigma.new_eGenreDataPtr(*args))

    __swig_destroy__ = _enigma.delete_eGenreDataPtr


eGenreDataPtr.__ref__ = new_instancemethod(_enigma.eGenreDataPtr___ref__, None, eGenreDataPtr)
eGenreDataPtr.getPtrString = new_instancemethod(_enigma.eGenreDataPtr_getPtrString, None, eGenreDataPtr)
eGenreDataPtr.__deref__ = new_instancemethod(_enigma.eGenreDataPtr___deref__, None, eGenreDataPtr)
eGenreDataPtr.getLevel1 = new_instancemethod(_enigma.eGenreDataPtr_getLevel1, None, eGenreDataPtr)
eGenreDataPtr.getLevel2 = new_instancemethod(_enigma.eGenreDataPtr_getLevel2, None, eGenreDataPtr)
eGenreDataPtr.getUser1 = new_instancemethod(_enigma.eGenreDataPtr_getUser1, None, eGenreDataPtr)
eGenreDataPtr.getUser2 = new_instancemethod(_enigma.eGenreDataPtr_getUser2, None, eGenreDataPtr)
eGenreDataPtr_swigregister = _enigma.eGenreDataPtr_swigregister
eGenreDataPtr_swigregister(eGenreDataPtr)

class eParentalDataPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eParentalDataPtr_swiginit(self, _enigma.new_eParentalDataPtr(*args))

    __swig_destroy__ = _enigma.delete_eParentalDataPtr


eParentalDataPtr.__ref__ = new_instancemethod(_enigma.eParentalDataPtr___ref__, None, eParentalDataPtr)
eParentalDataPtr.getPtrString = new_instancemethod(_enigma.eParentalDataPtr_getPtrString, None, eParentalDataPtr)
eParentalDataPtr.__deref__ = new_instancemethod(_enigma.eParentalDataPtr___deref__, None, eParentalDataPtr)
eParentalDataPtr.getCountryCode = new_instancemethod(_enigma.eParentalDataPtr_getCountryCode, None, eParentalDataPtr)
eParentalDataPtr.getRating = new_instancemethod(_enigma.eParentalDataPtr_getRating, None, eParentalDataPtr)
eParentalDataPtr_swigregister = _enigma.eParentalDataPtr_swigregister
eParentalDataPtr_swigregister(eParentalDataPtr)

class eServiceEvent(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eServiceEvent_swiginit(self, _enigma.new_eServiceEvent(*args))

    __swig_destroy__ = _enigma.delete_eServiceEvent
    setEPGLanguage = staticmethod(_enigma.eServiceEvent_setEPGLanguage)
    setEPGLanguageAlternative = staticmethod(_enigma.eServiceEvent_setEPGLanguageAlternative)


eServiceEvent.__ref__ = new_instancemethod(_enigma.eServiceEvent___ref__, None, eServiceEvent)
eServiceEvent.getPtrString = new_instancemethod(_enigma.eServiceEvent_getPtrString, None, eServiceEvent)
eServiceEvent.__deref__ = new_instancemethod(_enigma.eServiceEvent___deref__, None, eServiceEvent)
eServiceEvent.getBeginTime = new_instancemethod(_enigma.eServiceEvent_getBeginTime, None, eServiceEvent)
eServiceEvent.getDuration = new_instancemethod(_enigma.eServiceEvent_getDuration, None, eServiceEvent)
eServiceEvent.getEventId = new_instancemethod(_enigma.eServiceEvent_getEventId, None, eServiceEvent)
eServiceEvent.getPdcPil = new_instancemethod(_enigma.eServiceEvent_getPdcPil, None, eServiceEvent)
eServiceEvent.getRunningStatus = new_instancemethod(_enigma.eServiceEvent_getRunningStatus, None, eServiceEvent)
eServiceEvent.getEventName = new_instancemethod(_enigma.eServiceEvent_getEventName, None, eServiceEvent)
eServiceEvent.getShortDescription = new_instancemethod(_enigma.eServiceEvent_getShortDescription, None, eServiceEvent)
eServiceEvent.getExtendedDescription = new_instancemethod(_enigma.eServiceEvent_getExtendedDescription, None, eServiceEvent)
eServiceEvent.getBeginTimeString = new_instancemethod(_enigma.eServiceEvent_getBeginTimeString, None, eServiceEvent)
eServiceEvent.getExtraEventData = new_instancemethod(_enigma.eServiceEvent_getExtraEventData, None, eServiceEvent)
eServiceEvent.getEPGSource = new_instancemethod(_enigma.eServiceEvent_getEPGSource, None, eServiceEvent)
eServiceEvent.getComponentData = new_instancemethod(_enigma.eServiceEvent_getComponentData, None, eServiceEvent)
eServiceEvent.getNumOfLinkageServices = new_instancemethod(_enigma.eServiceEvent_getNumOfLinkageServices, None, eServiceEvent)
eServiceEvent.getLinkageService = new_instancemethod(_enigma.eServiceEvent_getLinkageService, None, eServiceEvent)
eServiceEvent.getGenreData = new_instancemethod(_enigma.eServiceEvent_getGenreData, None, eServiceEvent)
eServiceEvent.getParentalData = new_instancemethod(_enigma.eServiceEvent_getParentalData, None, eServiceEvent)
eServiceEvent_swigregister = _enigma.eServiceEvent_swigregister
eServiceEvent_swigregister(eServiceEvent)

def eServiceEvent_setEPGLanguage(*args):
    return _enigma.eServiceEvent_setEPGLanguage(*args)


eServiceEvent_setEPGLanguage = _enigma.eServiceEvent_setEPGLanguage

def eServiceEvent_setEPGLanguageAlternative(*args):
    return _enigma.eServiceEvent_setEPGLanguageAlternative(*args)


eServiceEvent_setEPGLanguageAlternative = _enigma.eServiceEvent_setEPGLanguageAlternative

class eServiceReference(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    idInvalid = _enigma.eServiceReference_idInvalid
    idStructure = _enigma.eServiceReference_idStructure
    idDVB = _enigma.eServiceReference_idDVB
    idFile = _enigma.eServiceReference_idFile
    idUser = _enigma.eServiceReference_idUser
    idServiceMP3 = _enigma.eServiceReference_idServiceMP3
    type = _swig_property(_enigma.eServiceReference_type_get, _enigma.eServiceReference_type_set)
    isDirectory = _enigma.eServiceReference_isDirectory
    mustDescent = _enigma.eServiceReference_mustDescent
    canDescent = _enigma.eServiceReference_canDescent
    flagDirectory = _enigma.eServiceReference_flagDirectory
    shouldSort = _enigma.eServiceReference_shouldSort
    hasSortKey = _enigma.eServiceReference_hasSortKey
    sort1 = _enigma.eServiceReference_sort1
    isMarker = _enigma.eServiceReference_isMarker
    isGroup = _enigma.eServiceReference_isGroup
    isNumberedMarker = _enigma.eServiceReference_isNumberedMarker
    flags = _swig_property(_enigma.eServiceReference_flags_get, _enigma.eServiceReference_flags_set)

    def __init__(self, *args):
        _enigma.eServiceReference_swiginit(self, _enigma.new_eServiceReference(*args))

    __swig_destroy__ = _enigma.delete_eServiceReference


eServiceReference.getSortKey = new_instancemethod(_enigma.eServiceReference_getSortKey, None, eServiceReference)
eServiceReference.getPath = new_instancemethod(_enigma.eServiceReference_getPath, None, eServiceReference)
eServiceReference.setPath = new_instancemethod(_enigma.eServiceReference_setPath, None, eServiceReference)
eServiceReference.getUnsignedData = new_instancemethod(_enigma.eServiceReference_getUnsignedData, None, eServiceReference)
eServiceReference.getData = new_instancemethod(_enigma.eServiceReference_getData, None, eServiceReference)
eServiceReference.setUnsignedData = new_instancemethod(_enigma.eServiceReference_setUnsignedData, None, eServiceReference)
eServiceReference.setData = new_instancemethod(_enigma.eServiceReference_setData, None, eServiceReference)
eServiceReference.getName = new_instancemethod(_enigma.eServiceReference_getName, None, eServiceReference)
eServiceReference.setName = new_instancemethod(_enigma.eServiceReference_setName, None, eServiceReference)
eServiceReference.toString = new_instancemethod(_enigma.eServiceReference_toString, None, eServiceReference)
eServiceReference.toCompareString = new_instancemethod(_enigma.eServiceReference_toCompareString, None, eServiceReference)
eServiceReference.__eq__ = new_instancemethod(_enigma.eServiceReference___eq__, None, eServiceReference)
eServiceReference.__ne__ = new_instancemethod(_enigma.eServiceReference___ne__, None, eServiceReference)
eServiceReference.__lt__ = new_instancemethod(_enigma.eServiceReference___lt__, None, eServiceReference)
eServiceReference.valid = new_instancemethod(_enigma.eServiceReference_valid, None, eServiceReference)
eServiceReference_swigregister = _enigma.eServiceReference_swigregister
eServiceReference_swigregister(eServiceReference)

def New_eServiceReference(*args):
    return _enigma.New_eServiceReference(*args)


New_eServiceReference = _enigma.New_eServiceReference

class iStaticServiceInformationPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iStaticServiceInformationPtr_swiginit(self, _enigma.new_iStaticServiceInformationPtr(*args))

    __swig_destroy__ = _enigma.delete_iStaticServiceInformationPtr


iStaticServiceInformationPtr.__ref__ = new_instancemethod(_enigma.iStaticServiceInformationPtr___ref__, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr.getPtrString = new_instancemethod(_enigma.iStaticServiceInformationPtr_getPtrString, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr.__deref__ = new_instancemethod(_enigma.iStaticServiceInformationPtr___deref__, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr.getName = new_instancemethod(_enigma.iStaticServiceInformationPtr_getName, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr.getLength = new_instancemethod(_enigma.iStaticServiceInformationPtr_getLength, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr.getEvent = new_instancemethod(_enigma.iStaticServiceInformationPtr_getEvent, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr.isPlayable = new_instancemethod(_enigma.iStaticServiceInformationPtr_isPlayable, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr.getInfo = new_instancemethod(_enigma.iStaticServiceInformationPtr_getInfo, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr.getInfoString = new_instancemethod(_enigma.iStaticServiceInformationPtr_getInfoString, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr.getInfoObject = new_instancemethod(_enigma.iStaticServiceInformationPtr_getInfoObject, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr.setInfo = new_instancemethod(_enigma.iStaticServiceInformationPtr_setInfo, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr.setInfoString = new_instancemethod(_enigma.iStaticServiceInformationPtr_setInfoString, None, iStaticServiceInformationPtr)
iStaticServiceInformationPtr_swigregister = _enigma.iStaticServiceInformationPtr_swigregister
iStaticServiceInformationPtr_swigregister(iStaticServiceInformationPtr)

class iServiceInformation(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    sIsCrypted = _enigma.iServiceInformation_ENUMS_sIsCrypted
    sAspect = _enigma.iServiceInformation_ENUMS_sAspect
    sFrameRate = _enigma.iServiceInformation_ENUMS_sFrameRate
    sProgressive = _enigma.iServiceInformation_ENUMS_sProgressive
    sIsMultichannel = _enigma.iServiceInformation_ENUMS_sIsMultichannel
    sVideoPID = _enigma.iServiceInformation_ENUMS_sVideoPID
    sAudioPID = _enigma.iServiceInformation_ENUMS_sAudioPID
    sPCRPID = _enigma.iServiceInformation_ENUMS_sPCRPID
    sPMTPID = _enigma.iServiceInformation_ENUMS_sPMTPID
    sTXTPID = _enigma.iServiceInformation_ENUMS_sTXTPID
    sSID = _enigma.iServiceInformation_ENUMS_sSID
    sONID = _enigma.iServiceInformation_ENUMS_sONID
    sTSID = _enigma.iServiceInformation_ENUMS_sTSID
    sNamespace = _enigma.iServiceInformation_ENUMS_sNamespace
    sProvider = _enigma.iServiceInformation_ENUMS_sProvider
    sDescription = _enigma.iServiceInformation_ENUMS_sDescription
    sServiceref = _enigma.iServiceInformation_ENUMS_sServiceref
    sTimeCreate = _enigma.iServiceInformation_ENUMS_sTimeCreate
    sFileSize = _enigma.iServiceInformation_ENUMS_sFileSize
    sCAIDs = _enigma.iServiceInformation_ENUMS_sCAIDs
    sCAIDPIDs = _enigma.iServiceInformation_ENUMS_sCAIDPIDs
    sVideoType = _enigma.iServiceInformation_ENUMS_sVideoType
    sTags = _enigma.iServiceInformation_ENUMS_sTags
    sDVBState = _enigma.iServiceInformation_ENUMS_sDVBState
    sVideoHeight = _enigma.iServiceInformation_ENUMS_sVideoHeight
    sVideoWidth = _enigma.iServiceInformation_ENUMS_sVideoWidth
    sTransponderData = _enigma.iServiceInformation_ENUMS_sTransponderData
    sCurrentChapter = _enigma.iServiceInformation_ENUMS_sCurrentChapter
    sCurrentTitle = _enigma.iServiceInformation_ENUMS_sCurrentTitle
    sTotalChapters = _enigma.iServiceInformation_ENUMS_sTotalChapters
    sTotalTitles = _enigma.iServiceInformation_ENUMS_sTotalTitles
    sTagTitle = _enigma.iServiceInformation_ENUMS_sTagTitle
    sTagTitleSortname = _enigma.iServiceInformation_ENUMS_sTagTitleSortname
    sTagArtist = _enigma.iServiceInformation_ENUMS_sTagArtist
    sTagArtistSortname = _enigma.iServiceInformation_ENUMS_sTagArtistSortname
    sTagAlbum = _enigma.iServiceInformation_ENUMS_sTagAlbum
    sTagAlbumSortname = _enigma.iServiceInformation_ENUMS_sTagAlbumSortname
    sTagComposer = _enigma.iServiceInformation_ENUMS_sTagComposer
    sTagDate = _enigma.iServiceInformation_ENUMS_sTagDate
    sTagGenre = _enigma.iServiceInformation_ENUMS_sTagGenre
    sTagComment = _enigma.iServiceInformation_ENUMS_sTagComment
    sTagExtendedComment = _enigma.iServiceInformation_ENUMS_sTagExtendedComment
    sTagTrackNumber = _enigma.iServiceInformation_ENUMS_sTagTrackNumber
    sTagTrackCount = _enigma.iServiceInformation_ENUMS_sTagTrackCount
    sTagAlbumVolumeNumber = _enigma.iServiceInformation_ENUMS_sTagAlbumVolumeNumber
    sTagAlbumVolumeCount = _enigma.iServiceInformation_ENUMS_sTagAlbumVolumeCount
    sTagLocation = _enigma.iServiceInformation_ENUMS_sTagLocation
    sTagHomepage = _enigma.iServiceInformation_ENUMS_sTagHomepage
    sTagDescription = _enigma.iServiceInformation_ENUMS_sTagDescription
    sTagVersion = _enigma.iServiceInformation_ENUMS_sTagVersion
    sTagISRC = _enigma.iServiceInformation_ENUMS_sTagISRC
    sTagOrganization = _enigma.iServiceInformation_ENUMS_sTagOrganization
    sTagCopyright = _enigma.iServiceInformation_ENUMS_sTagCopyright
    sTagCopyrightURI = _enigma.iServiceInformation_ENUMS_sTagCopyrightURI
    sTagContact = _enigma.iServiceInformation_ENUMS_sTagContact
    sTagLicense = _enigma.iServiceInformation_ENUMS_sTagLicense
    sTagLicenseURI = _enigma.iServiceInformation_ENUMS_sTagLicenseURI
    sTagPerformer = _enigma.iServiceInformation_ENUMS_sTagPerformer
    sTagCodec = _enigma.iServiceInformation_ENUMS_sTagCodec
    sTagVideoCodec = _enigma.iServiceInformation_ENUMS_sTagVideoCodec
    sTagAudioCodec = _enigma.iServiceInformation_ENUMS_sTagAudioCodec
    sTagBitrate = _enigma.iServiceInformation_ENUMS_sTagBitrate
    sTagNominalBitrate = _enigma.iServiceInformation_ENUMS_sTagNominalBitrate
    sTagMinimumBitrate = _enigma.iServiceInformation_ENUMS_sTagMinimumBitrate
    sTagMaximumBitrate = _enigma.iServiceInformation_ENUMS_sTagMaximumBitrate
    sTagSerial = _enigma.iServiceInformation_ENUMS_sTagSerial
    sTagEncoder = _enigma.iServiceInformation_ENUMS_sTagEncoder
    sTagEncoderVersion = _enigma.iServiceInformation_ENUMS_sTagEncoderVersion
    sTagTrackGain = _enigma.iServiceInformation_ENUMS_sTagTrackGain
    sTagTrackPeak = _enigma.iServiceInformation_ENUMS_sTagTrackPeak
    sTagAlbumGain = _enigma.iServiceInformation_ENUMS_sTagAlbumGain
    sTagAlbumPeak = _enigma.iServiceInformation_ENUMS_sTagAlbumPeak
    sTagReferenceLevel = _enigma.iServiceInformation_ENUMS_sTagReferenceLevel
    sTagLanguageCode = _enigma.iServiceInformation_ENUMS_sTagLanguageCode
    sTagImage = _enigma.iServiceInformation_ENUMS_sTagImage
    sTagPreviewImage = _enigma.iServiceInformation_ENUMS_sTagPreviewImage
    sTagAttachment = _enigma.iServiceInformation_ENUMS_sTagAttachment
    sTagBeatsPerMinute = _enigma.iServiceInformation_ENUMS_sTagBeatsPerMinute
    sTagKeywords = _enigma.iServiceInformation_ENUMS_sTagKeywords
    sTagCRC = _enigma.iServiceInformation_ENUMS_sTagCRC
    sTagChannelMode = _enigma.iServiceInformation_ENUMS_sTagChannelMode
    sTransferBPS = _enigma.iServiceInformation_ENUMS_sTransferBPS
    sHBBTVUrl = _enigma.iServiceInformation_ENUMS_sHBBTVUrl
    sLiveStreamDemuxId = _enigma.iServiceInformation_ENUMS_sLiveStreamDemuxId
    sIsScrambled = _enigma.iServiceInformation_ENUMS_sIsScrambled
    sIsIPStream = _enigma.iServiceInformation_ENUMS_sIsIPStream
    sUser = _enigma.iServiceInformation_ENUMS_sUser
    resNA = _enigma.iServiceInformation_ENUMS_resNA
    resIsString = _enigma.iServiceInformation_ENUMS_resIsString
    resIsPyObject = _enigma.iServiceInformation_ENUMS_resIsPyObject


iServiceInformation_swigregister = _enigma.iServiceInformation_ENUMS_swigregister
iServiceInformation_swigregister(iServiceInformation)

class iServiceInformationPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iServiceInformationPtr_swiginit(self, _enigma.new_iServiceInformationPtr(*args))

    __swig_destroy__ = _enigma.delete_iServiceInformationPtr


iServiceInformationPtr.__ref__ = new_instancemethod(_enigma.iServiceInformationPtr___ref__, None, iServiceInformationPtr)
iServiceInformationPtr.getPtrString = new_instancemethod(_enigma.iServiceInformationPtr_getPtrString, None, iServiceInformationPtr)
iServiceInformationPtr.__deref__ = new_instancemethod(_enigma.iServiceInformationPtr___deref__, None, iServiceInformationPtr)
iServiceInformationPtr.getName = new_instancemethod(_enigma.iServiceInformationPtr_getName, None, iServiceInformationPtr)
iServiceInformationPtr.getEvent = new_instancemethod(_enigma.iServiceInformationPtr_getEvent, None, iServiceInformationPtr)
iServiceInformationPtr.getInfo = new_instancemethod(_enigma.iServiceInformationPtr_getInfo, None, iServiceInformationPtr)
iServiceInformationPtr.getInfoString = new_instancemethod(_enigma.iServiceInformationPtr_getInfoString, None, iServiceInformationPtr)
iServiceInformationPtr.getInfoObject = new_instancemethod(_enigma.iServiceInformationPtr_getInfoObject, None, iServiceInformationPtr)
iServiceInformationPtr.setInfo = new_instancemethod(_enigma.iServiceInformationPtr_setInfo, None, iServiceInformationPtr)
iServiceInformationPtr.setInfoString = new_instancemethod(_enigma.iServiceInformationPtr_setInfoString, None, iServiceInformationPtr)
iServiceInformationPtr_swigregister = _enigma.iServiceInformationPtr_swigregister
iServiceInformationPtr_swigregister(iServiceInformationPtr)

class iFrontendInformation(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    bitErrorRate = _enigma.iFrontendInformation_ENUMS_bitErrorRate
    signalPower = _enigma.iFrontendInformation_ENUMS_signalPower
    signalQuality = _enigma.iFrontendInformation_ENUMS_signalQuality
    lockState = _enigma.iFrontendInformation_ENUMS_lockState
    syncState = _enigma.iFrontendInformation_ENUMS_syncState
    frontendNumber = _enigma.iFrontendInformation_ENUMS_frontendNumber
    signalQualitydB = _enigma.iFrontendInformation_ENUMS_signalQualitydB


iFrontendInformation_swigregister = _enigma.iFrontendInformation_ENUMS_swigregister
iFrontendInformation_swigregister(iFrontendInformation)

class iFrontendInformationPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iFrontendInformationPtr_swiginit(self, _enigma.new_iFrontendInformationPtr(*args))

    __swig_destroy__ = _enigma.delete_iFrontendInformationPtr


iFrontendInformationPtr.__ref__ = new_instancemethod(_enigma.iFrontendInformationPtr___ref__, None, iFrontendInformationPtr)
iFrontendInformationPtr.getPtrString = new_instancemethod(_enigma.iFrontendInformationPtr_getPtrString, None, iFrontendInformationPtr)
iFrontendInformationPtr.__deref__ = new_instancemethod(_enigma.iFrontendInformationPtr___deref__, None, iFrontendInformationPtr)
iFrontendInformationPtr.getFrontendInfo = new_instancemethod(_enigma.iFrontendInformationPtr_getFrontendInfo, None, iFrontendInformationPtr)
iFrontendInformationPtr.getFrontendData = new_instancemethod(_enigma.iFrontendInformationPtr_getFrontendData, None, iFrontendInformationPtr)
iFrontendInformationPtr.getFrontendStatus = new_instancemethod(_enigma.iFrontendInformationPtr_getFrontendStatus, None, iFrontendInformationPtr)
iFrontendInformationPtr.getTransponderData = new_instancemethod(_enigma.iFrontendInformationPtr_getTransponderData, None, iFrontendInformationPtr)
iFrontendInformationPtr.getAll = new_instancemethod(_enigma.iFrontendInformationPtr_getAll, None, iFrontendInformationPtr)
iFrontendInformationPtr_swigregister = _enigma.iFrontendInformationPtr_swigregister
iFrontendInformationPtr_swigregister(iFrontendInformationPtr)

class iPauseableServicePtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iPauseableServicePtr_swiginit(self, _enigma.new_iPauseableServicePtr(*args))

    __swig_destroy__ = _enigma.delete_iPauseableServicePtr


iPauseableServicePtr.__ref__ = new_instancemethod(_enigma.iPauseableServicePtr___ref__, None, iPauseableServicePtr)
iPauseableServicePtr.getPtrString = new_instancemethod(_enigma.iPauseableServicePtr_getPtrString, None, iPauseableServicePtr)
iPauseableServicePtr.__deref__ = new_instancemethod(_enigma.iPauseableServicePtr___deref__, None, iPauseableServicePtr)
iPauseableServicePtr.pause = new_instancemethod(_enigma.iPauseableServicePtr_pause, None, iPauseableServicePtr)
iPauseableServicePtr.unpause = new_instancemethod(_enigma.iPauseableServicePtr_unpause, None, iPauseableServicePtr)
iPauseableServicePtr.setSlowMotion = new_instancemethod(_enigma.iPauseableServicePtr_setSlowMotion, None, iPauseableServicePtr)
iPauseableServicePtr.setFastForward = new_instancemethod(_enigma.iPauseableServicePtr_setFastForward, None, iPauseableServicePtr)
iPauseableServicePtr_swigregister = _enigma.iPauseableServicePtr_swigregister
iPauseableServicePtr_swigregister(iPauseableServicePtr)

class iSeekableService(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    dirForward = _enigma.iSeekableService_ENUMS_dirForward
    dirBackward = _enigma.iSeekableService_ENUMS_dirBackward


iSeekableService_swigregister = _enigma.iSeekableService_ENUMS_swigregister
iSeekableService_swigregister(iSeekableService)

class iSeekableServicePtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iSeekableServicePtr_swiginit(self, _enigma.new_iSeekableServicePtr(*args))

    __swig_destroy__ = _enigma.delete_iSeekableServicePtr


iSeekableServicePtr.__ref__ = new_instancemethod(_enigma.iSeekableServicePtr___ref__, None, iSeekableServicePtr)
iSeekableServicePtr.getPtrString = new_instancemethod(_enigma.iSeekableServicePtr_getPtrString, None, iSeekableServicePtr)
iSeekableServicePtr.__deref__ = new_instancemethod(_enigma.iSeekableServicePtr___deref__, None, iSeekableServicePtr)
iSeekableServicePtr.getLength = new_instancemethod(_enigma.iSeekableServicePtr_getLength, None, iSeekableServicePtr)
iSeekableServicePtr.seekTo = new_instancemethod(_enigma.iSeekableServicePtr_seekTo, None, iSeekableServicePtr)
iSeekableServicePtr.seekRelative = new_instancemethod(_enigma.iSeekableServicePtr_seekRelative, None, iSeekableServicePtr)
iSeekableServicePtr.getPlayPosition = new_instancemethod(_enigma.iSeekableServicePtr_getPlayPosition, None, iSeekableServicePtr)
iSeekableServicePtr.setTrickmode = new_instancemethod(_enigma.iSeekableServicePtr_setTrickmode, None, iSeekableServicePtr)
iSeekableServicePtr.isCurrentlySeekable = new_instancemethod(_enigma.iSeekableServicePtr_isCurrentlySeekable, None, iSeekableServicePtr)
iSeekableServicePtr.seekChapter = new_instancemethod(_enigma.iSeekableServicePtr_seekChapter, None, iSeekableServicePtr)
iSeekableServicePtr.seekTitle = new_instancemethod(_enigma.iSeekableServicePtr_seekTitle, None, iSeekableServicePtr)
iSeekableServicePtr_swigregister = _enigma.iSeekableServicePtr_swigregister
iSeekableServicePtr_swigregister(iSeekableServicePtr)

class iAudioTrackInfo(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.iAudioTrackInfo_swiginit(self, _enigma.new_iAudioTrackInfo())

    __swig_destroy__ = _enigma.delete_iAudioTrackInfo


iAudioTrackInfo.getDescription = new_instancemethod(_enigma.iAudioTrackInfo_getDescription, None, iAudioTrackInfo)
iAudioTrackInfo.getLanguage = new_instancemethod(_enigma.iAudioTrackInfo_getLanguage, None, iAudioTrackInfo)
iAudioTrackInfo.getPID = new_instancemethod(_enigma.iAudioTrackInfo_getPID, None, iAudioTrackInfo)
iAudioTrackInfo_swigregister = _enigma.iAudioTrackInfo_swigregister
iAudioTrackInfo_swigregister(iAudioTrackInfo)

class iAudioTrackSelectionPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iAudioTrackSelectionPtr_swiginit(self, _enigma.new_iAudioTrackSelectionPtr(*args))

    __swig_destroy__ = _enigma.delete_iAudioTrackSelectionPtr


iAudioTrackSelectionPtr.__ref__ = new_instancemethod(_enigma.iAudioTrackSelectionPtr___ref__, None, iAudioTrackSelectionPtr)
iAudioTrackSelectionPtr.getPtrString = new_instancemethod(_enigma.iAudioTrackSelectionPtr_getPtrString, None, iAudioTrackSelectionPtr)
iAudioTrackSelectionPtr.__deref__ = new_instancemethod(_enigma.iAudioTrackSelectionPtr___deref__, None, iAudioTrackSelectionPtr)
iAudioTrackSelectionPtr.getNumberOfTracks = new_instancemethod(_enigma.iAudioTrackSelectionPtr_getNumberOfTracks, None, iAudioTrackSelectionPtr)
iAudioTrackSelectionPtr.selectTrack = new_instancemethod(_enigma.iAudioTrackSelectionPtr_selectTrack, None, iAudioTrackSelectionPtr)
iAudioTrackSelectionPtr.getTrackInfo = new_instancemethod(_enigma.iAudioTrackSelectionPtr_getTrackInfo, None, iAudioTrackSelectionPtr)
iAudioTrackSelectionPtr.getCurrentTrack = new_instancemethod(_enigma.iAudioTrackSelectionPtr_getCurrentTrack, None, iAudioTrackSelectionPtr)
iAudioTrackSelectionPtr_swigregister = _enigma.iAudioTrackSelectionPtr_swigregister
iAudioTrackSelectionPtr_swigregister(iAudioTrackSelectionPtr)

class iAudioChannelSelection(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    LEFT = _enigma.iAudioChannelSelection_ENUMS_LEFT
    STEREO = _enigma.iAudioChannelSelection_ENUMS_STEREO
    RIGHT = _enigma.iAudioChannelSelection_ENUMS_RIGHT


iAudioChannelSelection_swigregister = _enigma.iAudioChannelSelection_ENUMS_swigregister
iAudioChannelSelection_swigregister(iAudioChannelSelection)

class iAudioChannelSelectionPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iAudioChannelSelectionPtr_swiginit(self, _enigma.new_iAudioChannelSelectionPtr(*args))

    __swig_destroy__ = _enigma.delete_iAudioChannelSelectionPtr


iAudioChannelSelectionPtr.__ref__ = new_instancemethod(_enigma.iAudioChannelSelectionPtr___ref__, None, iAudioChannelSelectionPtr)
iAudioChannelSelectionPtr.getPtrString = new_instancemethod(_enigma.iAudioChannelSelectionPtr_getPtrString, None, iAudioChannelSelectionPtr)
iAudioChannelSelectionPtr.__deref__ = new_instancemethod(_enigma.iAudioChannelSelectionPtr___deref__, None, iAudioChannelSelectionPtr)
iAudioChannelSelectionPtr.getCurrentChannel = new_instancemethod(_enigma.iAudioChannelSelectionPtr_getCurrentChannel, None, iAudioChannelSelectionPtr)
iAudioChannelSelectionPtr.selectChannel = new_instancemethod(_enigma.iAudioChannelSelectionPtr_selectChannel, None, iAudioChannelSelectionPtr)
iAudioChannelSelectionPtr_swigregister = _enigma.iAudioChannelSelectionPtr_swigregister
iAudioChannelSelectionPtr_swigregister(iAudioChannelSelectionPtr)

class iAudioDelayPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iAudioDelayPtr_swiginit(self, _enigma.new_iAudioDelayPtr(*args))

    __swig_destroy__ = _enigma.delete_iAudioDelayPtr


iAudioDelayPtr.__ref__ = new_instancemethod(_enigma.iAudioDelayPtr___ref__, None, iAudioDelayPtr)
iAudioDelayPtr.getPtrString = new_instancemethod(_enigma.iAudioDelayPtr_getPtrString, None, iAudioDelayPtr)
iAudioDelayPtr.__deref__ = new_instancemethod(_enigma.iAudioDelayPtr___deref__, None, iAudioDelayPtr)
iAudioDelayPtr.getAC3Delay = new_instancemethod(_enigma.iAudioDelayPtr_getAC3Delay, None, iAudioDelayPtr)
iAudioDelayPtr.getPCMDelay = new_instancemethod(_enigma.iAudioDelayPtr_getPCMDelay, None, iAudioDelayPtr)
iAudioDelayPtr.setAC3Delay = new_instancemethod(_enigma.iAudioDelayPtr_setAC3Delay, None, iAudioDelayPtr)
iAudioDelayPtr.setPCMDelay = new_instancemethod(_enigma.iAudioDelayPtr_setPCMDelay, None, iAudioDelayPtr)
iAudioDelayPtr_swigregister = _enigma.iAudioDelayPtr_swigregister
iAudioDelayPtr_swigregister(iAudioDelayPtr)

class iRdsDecoder(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    RadioText = _enigma.iRdsDecoder_ENUMS_RadioText
    RtpText = _enigma.iRdsDecoder_ENUMS_RtpText


iRdsDecoder_swigregister = _enigma.iRdsDecoder_ENUMS_swigregister
iRdsDecoder_swigregister(iRdsDecoder)

class iRdsDecoderPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iRdsDecoderPtr_swiginit(self, _enigma.new_iRdsDecoderPtr(*args))

    __swig_destroy__ = _enigma.delete_iRdsDecoderPtr


iRdsDecoderPtr.__ref__ = new_instancemethod(_enigma.iRdsDecoderPtr___ref__, None, iRdsDecoderPtr)
iRdsDecoderPtr.getPtrString = new_instancemethod(_enigma.iRdsDecoderPtr_getPtrString, None, iRdsDecoderPtr)
iRdsDecoderPtr.__deref__ = new_instancemethod(_enigma.iRdsDecoderPtr___deref__, None, iRdsDecoderPtr)
iRdsDecoderPtr.getText = new_instancemethod(_enigma.iRdsDecoderPtr_getText, None, iRdsDecoderPtr)
iRdsDecoderPtr.showRassSlidePicture = new_instancemethod(_enigma.iRdsDecoderPtr_showRassSlidePicture, None, iRdsDecoderPtr)
iRdsDecoderPtr.showRassInteractivePic = new_instancemethod(_enigma.iRdsDecoderPtr_showRassInteractivePic, None, iRdsDecoderPtr)
iRdsDecoderPtr.getRassInteractiveMask = new_instancemethod(_enigma.iRdsDecoderPtr_getRassInteractiveMask, None, iRdsDecoderPtr)
iRdsDecoderPtr_swigregister = _enigma.iRdsDecoderPtr_swigregister
iRdsDecoderPtr_swigregister(iRdsDecoderPtr)

class iSubserviceListPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iSubserviceListPtr_swiginit(self, _enigma.new_iSubserviceListPtr(*args))

    __swig_destroy__ = _enigma.delete_iSubserviceListPtr


iSubserviceListPtr.__ref__ = new_instancemethod(_enigma.iSubserviceListPtr___ref__, None, iSubserviceListPtr)
iSubserviceListPtr.getPtrString = new_instancemethod(_enigma.iSubserviceListPtr_getPtrString, None, iSubserviceListPtr)
iSubserviceListPtr.__deref__ = new_instancemethod(_enigma.iSubserviceListPtr___deref__, None, iSubserviceListPtr)
iSubserviceListPtr.getNumberOfSubservices = new_instancemethod(_enigma.iSubserviceListPtr_getNumberOfSubservices, None, iSubserviceListPtr)
iSubserviceListPtr.getSubservice = new_instancemethod(_enigma.iSubserviceListPtr_getSubservice, None, iSubserviceListPtr)
iSubserviceListPtr_swigregister = _enigma.iSubserviceListPtr_swigregister
iSubserviceListPtr_swigregister(iSubserviceListPtr)

class iTimeshiftServicePtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iTimeshiftServicePtr_swiginit(self, _enigma.new_iTimeshiftServicePtr(*args))

    __swig_destroy__ = _enigma.delete_iTimeshiftServicePtr


iTimeshiftServicePtr.__ref__ = new_instancemethod(_enigma.iTimeshiftServicePtr___ref__, None, iTimeshiftServicePtr)
iTimeshiftServicePtr.getPtrString = new_instancemethod(_enigma.iTimeshiftServicePtr_getPtrString, None, iTimeshiftServicePtr)
iTimeshiftServicePtr.__deref__ = new_instancemethod(_enigma.iTimeshiftServicePtr___deref__, None, iTimeshiftServicePtr)
iTimeshiftServicePtr.startTimeshift = new_instancemethod(_enigma.iTimeshiftServicePtr_startTimeshift, None, iTimeshiftServicePtr)
iTimeshiftServicePtr.stopTimeshift = new_instancemethod(_enigma.iTimeshiftServicePtr_stopTimeshift, None, iTimeshiftServicePtr)
iTimeshiftServicePtr.setNextPlaybackFile = new_instancemethod(_enigma.iTimeshiftServicePtr_setNextPlaybackFile, None, iTimeshiftServicePtr)
iTimeshiftServicePtr.setTimeshiftFiletoSave = new_instancemethod(_enigma.iTimeshiftServicePtr_setTimeshiftFiletoSave, None, iTimeshiftServicePtr)
iTimeshiftServicePtr.seektoTimehshiftBufferEnd = new_instancemethod(_enigma.iTimeshiftServicePtr_seektoTimehshiftBufferEnd, None, iTimeshiftServicePtr)
iTimeshiftServicePtr.playNextTimeshiftFile = new_instancemethod(_enigma.iTimeshiftServicePtr_playNextTimeshiftFile, None, iTimeshiftServicePtr)
iTimeshiftServicePtr.getCurrentTSFile = new_instancemethod(_enigma.iTimeshiftServicePtr_getCurrentTSFile, None, iTimeshiftServicePtr)
iTimeshiftServicePtr.isTimeshiftActive = new_instancemethod(_enigma.iTimeshiftServicePtr_isTimeshiftActive, None, iTimeshiftServicePtr)
iTimeshiftServicePtr.activateTimeshift = new_instancemethod(_enigma.iTimeshiftServicePtr_activateTimeshift, None, iTimeshiftServicePtr)
iTimeshiftServicePtr_swigregister = _enigma.iTimeshiftServicePtr_swigregister
iTimeshiftServicePtr_swigregister(iTimeshiftServicePtr)

class iCueSheet(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    cutIn = _enigma.iCueSheet_ENUMS_cutIn
    cutOut = _enigma.iCueSheet_ENUMS_cutOut
    cutMark = _enigma.iCueSheet_ENUMS_cutMark


iCueSheet_swigregister = _enigma.iCueSheet_ENUMS_swigregister
iCueSheet_swigregister(iCueSheet)

class iCueSheetPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iCueSheetPtr_swiginit(self, _enigma.new_iCueSheetPtr(*args))

    __swig_destroy__ = _enigma.delete_iCueSheetPtr


iCueSheetPtr.__ref__ = new_instancemethod(_enigma.iCueSheetPtr___ref__, None, iCueSheetPtr)
iCueSheetPtr.getPtrString = new_instancemethod(_enigma.iCueSheetPtr_getPtrString, None, iCueSheetPtr)
iCueSheetPtr.__deref__ = new_instancemethod(_enigma.iCueSheetPtr___deref__, None, iCueSheetPtr)
iCueSheetPtr.getCutList = new_instancemethod(_enigma.iCueSheetPtr_getCutList, None, iCueSheetPtr)
iCueSheetPtr.setCutList = new_instancemethod(_enigma.iCueSheetPtr_setCutList, None, iCueSheetPtr)
iCueSheetPtr.setCutListEnable = new_instancemethod(_enigma.iCueSheetPtr_setCutListEnable, None, iCueSheetPtr)
iCueSheetPtr_swigregister = _enigma.iCueSheetPtr_swigregister
iCueSheetPtr_swigregister(iCueSheetPtr)

class iSubtitleOutput(iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined - class is abstract')

    __repr__ = _swig_repr
    __swig_destroy__ = _enigma.delete_iSubtitleOutput


iSubtitleOutput.enableSubtitles = new_instancemethod(_enigma.iSubtitleOutput_enableSubtitles, None, iSubtitleOutput)
iSubtitleOutput.disableSubtitles = new_instancemethod(_enigma.iSubtitleOutput_disableSubtitles, None, iSubtitleOutput)
iSubtitleOutput.getSubtitleList = new_instancemethod(_enigma.iSubtitleOutput_getSubtitleList, None, iSubtitleOutput)
iSubtitleOutput.getCachedSubtitle = new_instancemethod(_enigma.iSubtitleOutput_getCachedSubtitle, None, iSubtitleOutput)
iSubtitleOutput_swigregister = _enigma.iSubtitleOutput_swigregister
iSubtitleOutput_swigregister(iSubtitleOutput)

class iSubtitleOutputPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iSubtitleOutputPtr_swiginit(self, _enigma.new_iSubtitleOutputPtr(*args))

    __swig_destroy__ = _enigma.delete_iSubtitleOutputPtr


iSubtitleOutputPtr.__ref__ = new_instancemethod(_enigma.iSubtitleOutputPtr___ref__, None, iSubtitleOutputPtr)
iSubtitleOutputPtr.getPtrString = new_instancemethod(_enigma.iSubtitleOutputPtr_getPtrString, None, iSubtitleOutputPtr)
iSubtitleOutputPtr.__deref__ = new_instancemethod(_enigma.iSubtitleOutputPtr___deref__, None, iSubtitleOutputPtr)
iSubtitleOutputPtr.enableSubtitles = new_instancemethod(_enigma.iSubtitleOutputPtr_enableSubtitles, None, iSubtitleOutputPtr)
iSubtitleOutputPtr.disableSubtitles = new_instancemethod(_enigma.iSubtitleOutputPtr_disableSubtitles, None, iSubtitleOutputPtr)
iSubtitleOutputPtr.getCachedSubtitle = new_instancemethod(_enigma.iSubtitleOutputPtr_getCachedSubtitle, None, iSubtitleOutputPtr)
iSubtitleOutputPtr.getSubtitleList = new_instancemethod(_enigma.iSubtitleOutputPtr_getSubtitleList, None, iSubtitleOutputPtr)
iSubtitleOutputPtr_swigregister = _enigma.iSubtitleOutputPtr_swigregister
iSubtitleOutputPtr_swigregister(iSubtitleOutputPtr)

class iMutableServiceListPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iMutableServiceListPtr_swiginit(self, _enigma.new_iMutableServiceListPtr(*args))

    __swig_destroy__ = _enigma.delete_iMutableServiceListPtr


iMutableServiceListPtr.__ref__ = new_instancemethod(_enigma.iMutableServiceListPtr___ref__, None, iMutableServiceListPtr)
iMutableServiceListPtr.getPtrString = new_instancemethod(_enigma.iMutableServiceListPtr_getPtrString, None, iMutableServiceListPtr)
iMutableServiceListPtr.__deref__ = new_instancemethod(_enigma.iMutableServiceListPtr___deref__, None, iMutableServiceListPtr)
iMutableServiceListPtr.flushChanges = new_instancemethod(_enigma.iMutableServiceListPtr_flushChanges, None, iMutableServiceListPtr)
iMutableServiceListPtr.addService = new_instancemethod(_enigma.iMutableServiceListPtr_addService, None, iMutableServiceListPtr)
iMutableServiceListPtr.removeService = new_instancemethod(_enigma.iMutableServiceListPtr_removeService, None, iMutableServiceListPtr)
iMutableServiceListPtr.moveService = new_instancemethod(_enigma.iMutableServiceListPtr_moveService, None, iMutableServiceListPtr)
iMutableServiceListPtr.setListName = new_instancemethod(_enigma.iMutableServiceListPtr_setListName, None, iMutableServiceListPtr)
iMutableServiceListPtr_swigregister = _enigma.iMutableServiceListPtr_swigregister
iMutableServiceListPtr_swigregister(iMutableServiceListPtr)

class iListableServicePtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iListableServicePtr_swiginit(self, _enigma.new_iListableServicePtr(*args))

    __swig_destroy__ = _enigma.delete_iListableServicePtr


iListableServicePtr.__ref__ = new_instancemethod(_enigma.iListableServicePtr___ref__, None, iListableServicePtr)
iListableServicePtr.getPtrString = new_instancemethod(_enigma.iListableServicePtr_getPtrString, None, iListableServicePtr)
iListableServicePtr.__deref__ = new_instancemethod(_enigma.iListableServicePtr___deref__, None, iListableServicePtr)
iListableServicePtr.getContent = new_instancemethod(_enigma.iListableServicePtr_getContent, None, iListableServicePtr)
iListableServicePtr.getNext = new_instancemethod(_enigma.iListableServicePtr_getNext, None, iListableServicePtr)
iListableServicePtr.compareLessEqual = new_instancemethod(_enigma.iListableServicePtr_compareLessEqual, None, iListableServicePtr)
iListableServicePtr.startEdit = new_instancemethod(_enigma.iListableServicePtr_startEdit, None, iListableServicePtr)
iListableServicePtr_swigregister = _enigma.iListableServicePtr_swigregister
iListableServicePtr_swigregister(iListableServicePtr)

class iServiceOfflineOperationsPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iServiceOfflineOperationsPtr_swiginit(self, _enigma.new_iServiceOfflineOperationsPtr(*args))

    __swig_destroy__ = _enigma.delete_iServiceOfflineOperationsPtr


iServiceOfflineOperationsPtr.__ref__ = new_instancemethod(_enigma.iServiceOfflineOperationsPtr___ref__, None, iServiceOfflineOperationsPtr)
iServiceOfflineOperationsPtr.getPtrString = new_instancemethod(_enigma.iServiceOfflineOperationsPtr_getPtrString, None, iServiceOfflineOperationsPtr)
iServiceOfflineOperationsPtr.__deref__ = new_instancemethod(_enigma.iServiceOfflineOperationsPtr___deref__, None, iServiceOfflineOperationsPtr)
iServiceOfflineOperationsPtr.deleteFromDisk = new_instancemethod(_enigma.iServiceOfflineOperationsPtr_deleteFromDisk, None, iServiceOfflineOperationsPtr)
iServiceOfflineOperationsPtr.getListOfFilenames = new_instancemethod(_enigma.iServiceOfflineOperationsPtr_getListOfFilenames, None, iServiceOfflineOperationsPtr)
iServiceOfflineOperationsPtr.reindex = new_instancemethod(_enigma.iServiceOfflineOperationsPtr_reindex, None, iServiceOfflineOperationsPtr)
iServiceOfflineOperationsPtr_swigregister = _enigma.iServiceOfflineOperationsPtr_swigregister
iServiceOfflineOperationsPtr_swigregister(iServiceOfflineOperationsPtr)

class iStreamableServicePtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iStreamableServicePtr_swiginit(self, _enigma.new_iStreamableServicePtr(*args))

    __swig_destroy__ = _enigma.delete_iStreamableServicePtr


iStreamableServicePtr.__ref__ = new_instancemethod(_enigma.iStreamableServicePtr___ref__, None, iStreamableServicePtr)
iStreamableServicePtr.getPtrString = new_instancemethod(_enigma.iStreamableServicePtr_getPtrString, None, iStreamableServicePtr)
iStreamableServicePtr.__deref__ = new_instancemethod(_enigma.iStreamableServicePtr___deref__, None, iStreamableServicePtr)
iStreamableServicePtr.getStreamingData = new_instancemethod(_enigma.iStreamableServicePtr_getStreamingData, None, iStreamableServicePtr)
iStreamableServicePtr_swigregister = _enigma.iStreamableServicePtr_swigregister
iStreamableServicePtr_swigregister(iStreamableServicePtr)

class iStreamedServicePtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iStreamedServicePtr_swiginit(self, _enigma.new_iStreamedServicePtr(*args))

    __swig_destroy__ = _enigma.delete_iStreamedServicePtr


iStreamedServicePtr.__ref__ = new_instancemethod(_enigma.iStreamedServicePtr___ref__, None, iStreamedServicePtr)
iStreamedServicePtr.getPtrString = new_instancemethod(_enigma.iStreamedServicePtr_getPtrString, None, iStreamedServicePtr)
iStreamedServicePtr.__deref__ = new_instancemethod(_enigma.iStreamedServicePtr___deref__, None, iStreamedServicePtr)
iStreamedServicePtr.getBufferCharge = new_instancemethod(_enigma.iStreamedServicePtr_getBufferCharge, None, iStreamedServicePtr)
iStreamedServicePtr.setBufferSize = new_instancemethod(_enigma.iStreamedServicePtr_setBufferSize, None, iStreamedServicePtr)
iStreamedServicePtr_swigregister = _enigma.iStreamedServicePtr_swigregister
iStreamedServicePtr_swigregister(iStreamedServicePtr)

class iServiceKeys(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    keyLeft = _enigma.iServiceKeys_ENUMS_keyLeft
    keyRight = _enigma.iServiceKeys_ENUMS_keyRight
    keyUp = _enigma.iServiceKeys_ENUMS_keyUp
    keyDown = _enigma.iServiceKeys_ENUMS_keyDown
    keyOk = _enigma.iServiceKeys_ENUMS_keyOk
    keyUser = _enigma.iServiceKeys_ENUMS_keyUser


iServiceKeys_swigregister = _enigma.iServiceKeys_ENUMS_swigregister
iServiceKeys_swigregister(iServiceKeys)

class iServiceKeysPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iServiceKeysPtr_swiginit(self, _enigma.new_iServiceKeysPtr(*args))

    __swig_destroy__ = _enigma.delete_iServiceKeysPtr


iServiceKeysPtr.__ref__ = new_instancemethod(_enigma.iServiceKeysPtr___ref__, None, iServiceKeysPtr)
iServiceKeysPtr.getPtrString = new_instancemethod(_enigma.iServiceKeysPtr_getPtrString, None, iServiceKeysPtr)
iServiceKeysPtr.__deref__ = new_instancemethod(_enigma.iServiceKeysPtr___deref__, None, iServiceKeysPtr)
iServiceKeysPtr.keyPressed = new_instancemethod(_enigma.iServiceKeysPtr_keyPressed, None, iServiceKeysPtr)
iServiceKeysPtr_swigregister = _enigma.iServiceKeysPtr_swigregister
iServiceKeysPtr_swigregister(iServiceKeysPtr)

class iPlayableService(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    evStart = _enigma.iPlayableService_ENUMS_evStart
    evEnd = _enigma.iPlayableService_ENUMS_evEnd
    evTunedIn = _enigma.iPlayableService_ENUMS_evTunedIn
    evTuneFailed = _enigma.iPlayableService_ENUMS_evTuneFailed
    evUpdatedEventInfo = _enigma.iPlayableService_ENUMS_evUpdatedEventInfo
    evUpdatedInfo = _enigma.iPlayableService_ENUMS_evUpdatedInfo
    evSeekableStatusChanged = _enigma.iPlayableService_ENUMS_evSeekableStatusChanged
    evEOF = _enigma.iPlayableService_ENUMS_evEOF
    evSOF = _enigma.iPlayableService_ENUMS_evSOF
    evCuesheetChanged = _enigma.iPlayableService_ENUMS_evCuesheetChanged
    evUpdatedRadioText = _enigma.iPlayableService_ENUMS_evUpdatedRadioText
    evUpdatedRtpText = _enigma.iPlayableService_ENUMS_evUpdatedRtpText
    evUpdatedRassSlidePic = _enigma.iPlayableService_ENUMS_evUpdatedRassSlidePic
    evUpdatedRassInteractivePicMask = _enigma.iPlayableService_ENUMS_evUpdatedRassInteractivePicMask
    evVideoSizeChanged = _enigma.iPlayableService_ENUMS_evVideoSizeChanged
    evVideoFramerateChanged = _enigma.iPlayableService_ENUMS_evVideoFramerateChanged
    evVideoProgressiveChanged = _enigma.iPlayableService_ENUMS_evVideoProgressiveChanged
    evBuffering = _enigma.iPlayableService_ENUMS_evBuffering
    evStopped = _enigma.iPlayableService_ENUMS_evStopped
    evHBBTVInfo = _enigma.iPlayableService_ENUMS_evHBBTVInfo
    evFccFailed = _enigma.iPlayableService_ENUMS_evFccFailed
    evUser = _enigma.iPlayableService_ENUMS_evUser


iPlayableService_swigregister = _enigma.iPlayableService_ENUMS_swigregister
iPlayableService_swigregister(iPlayableService)

class iPlayableServicePtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iPlayableServicePtr_swiginit(self, _enigma.new_iPlayableServicePtr(*args))

    __swig_destroy__ = _enigma.delete_iPlayableServicePtr


iPlayableServicePtr.__ref__ = new_instancemethod(_enigma.iPlayableServicePtr___ref__, None, iPlayableServicePtr)
iPlayableServicePtr.getPtrString = new_instancemethod(_enigma.iPlayableServicePtr_getPtrString, None, iPlayableServicePtr)
iPlayableServicePtr.__deref__ = new_instancemethod(_enigma.iPlayableServicePtr___deref__, None, iPlayableServicePtr)
iPlayableServicePtr.start = new_instancemethod(_enigma.iPlayableServicePtr_start, None, iPlayableServicePtr)
iPlayableServicePtr.stop = new_instancemethod(_enigma.iPlayableServicePtr_stop, None, iPlayableServicePtr)
iPlayableServicePtr.setTarget = new_instancemethod(_enigma.iPlayableServicePtr_setTarget, None, iPlayableServicePtr)
iPlayableServicePtr.seek = new_instancemethod(_enigma.iPlayableServicePtr_seek, None, iPlayableServicePtr)
iPlayableServicePtr.pause = new_instancemethod(_enigma.iPlayableServicePtr_pause, None, iPlayableServicePtr)
iPlayableServicePtr.info = new_instancemethod(_enigma.iPlayableServicePtr_info, None, iPlayableServicePtr)
iPlayableServicePtr.audioTracks = new_instancemethod(_enigma.iPlayableServicePtr_audioTracks, None, iPlayableServicePtr)
iPlayableServicePtr.audioChannel = new_instancemethod(_enigma.iPlayableServicePtr_audioChannel, None, iPlayableServicePtr)
iPlayableServicePtr.subServices = new_instancemethod(_enigma.iPlayableServicePtr_subServices, None, iPlayableServicePtr)
iPlayableServicePtr.frontendInfo = new_instancemethod(_enigma.iPlayableServicePtr_frontendInfo, None, iPlayableServicePtr)
iPlayableServicePtr.timeshift = new_instancemethod(_enigma.iPlayableServicePtr_timeshift, None, iPlayableServicePtr)
iPlayableServicePtr.cueSheet = new_instancemethod(_enigma.iPlayableServicePtr_cueSheet, None, iPlayableServicePtr)
iPlayableServicePtr.subtitle = new_instancemethod(_enigma.iPlayableServicePtr_subtitle, None, iPlayableServicePtr)
iPlayableServicePtr.audioDelay = new_instancemethod(_enigma.iPlayableServicePtr_audioDelay, None, iPlayableServicePtr)
iPlayableServicePtr.rdsDecoder = new_instancemethod(_enigma.iPlayableServicePtr_rdsDecoder, None, iPlayableServicePtr)
iPlayableServicePtr.stream = new_instancemethod(_enigma.iPlayableServicePtr_stream, None, iPlayableServicePtr)
iPlayableServicePtr.streamed = new_instancemethod(_enigma.iPlayableServicePtr_streamed, None, iPlayableServicePtr)
iPlayableServicePtr.keys = new_instancemethod(_enigma.iPlayableServicePtr_keys, None, iPlayableServicePtr)
iPlayableServicePtr.setQpipMode = new_instancemethod(_enigma.iPlayableServicePtr_setQpipMode, None, iPlayableServicePtr)
iPlayableServicePtr_swigregister = _enigma.iPlayableServicePtr_swigregister
iPlayableServicePtr_swigregister(iPlayableServicePtr)

class iRecordableService(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    evStart = _enigma.iRecordableService_ENUMS_evStart
    evEnd = _enigma.iRecordableService_ENUMS_evEnd
    evTunedIn = _enigma.iRecordableService_ENUMS_evTunedIn
    evTuneFailed = _enigma.iRecordableService_ENUMS_evTuneFailed
    evRecordRunning = _enigma.iRecordableService_ENUMS_evRecordRunning
    evRecordStopped = _enigma.iRecordableService_ENUMS_evRecordStopped
    evNewProgramInfo = _enigma.iRecordableService_ENUMS_evNewProgramInfo
    evRecordFailed = _enigma.iRecordableService_ENUMS_evRecordFailed
    evRecordWriteError = _enigma.iRecordableService_ENUMS_evRecordWriteError
    evNewEventInfo = _enigma.iRecordableService_ENUMS_evNewEventInfo
    evTuneStart = _enigma.iRecordableService_ENUMS_evTuneStart
    evGstRecordEnded = _enigma.iRecordableService_ENUMS_evGstRecordEnded
    evPvrTuneStart = _enigma.iRecordableService_ENUMS_evPvrTuneStart
    evPvrEof = _enigma.iRecordableService_ENUMS_evPvrEof
    evRecServiceStart = _enigma.iRecordableService_ENUMS_evRecServiceStart
    evRecServiceStop = _enigma.iRecordableService_ENUMS_evRecServiceStop
    NoError = _enigma.iRecordableService_ENUMS_NoError
    errOpenRecordFile = _enigma.iRecordableService_ENUMS_errOpenRecordFile
    errNoDemuxAvailable = _enigma.iRecordableService_ENUMS_errNoDemuxAvailable
    errNoTsRecorderAvailable = _enigma.iRecordableService_ENUMS_errNoTsRecorderAvailable
    errDiskFull = _enigma.iRecordableService_ENUMS_errDiskFull
    errTuneFailed = _enigma.iRecordableService_ENUMS_errTuneFailed
    errMisconfiguration = _enigma.iRecordableService_ENUMS_errMisconfiguration
    errNoResources = _enigma.iRecordableService_ENUMS_errNoResources
    errNoCiConnected = _enigma.iRecordableService_ENUMS_errNoCiConnected


iRecordableService_swigregister = _enigma.iRecordableService_ENUMS_swigregister
iRecordableService_swigregister(iRecordableService)

class iRecordableServicePtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iRecordableServicePtr_swiginit(self, _enigma.new_iRecordableServicePtr(*args))

    __swig_destroy__ = _enigma.delete_iRecordableServicePtr


iRecordableServicePtr.__ref__ = new_instancemethod(_enigma.iRecordableServicePtr___ref__, None, iRecordableServicePtr)
iRecordableServicePtr.getPtrString = new_instancemethod(_enigma.iRecordableServicePtr_getPtrString, None, iRecordableServicePtr)
iRecordableServicePtr.__deref__ = new_instancemethod(_enigma.iRecordableServicePtr___deref__, None, iRecordableServicePtr)
iRecordableServicePtr.getError = new_instancemethod(_enigma.iRecordableServicePtr_getError, None, iRecordableServicePtr)
iRecordableServicePtr.prepare = new_instancemethod(_enigma.iRecordableServicePtr_prepare, None, iRecordableServicePtr)
iRecordableServicePtr.prepareStreaming = new_instancemethod(_enigma.iRecordableServicePtr_prepareStreaming, None, iRecordableServicePtr)
iRecordableServicePtr.prepareDummyService = new_instancemethod(_enigma.iRecordableServicePtr_prepareDummyService, None, iRecordableServicePtr)
iRecordableServicePtr.start = new_instancemethod(_enigma.iRecordableServicePtr_start, None, iRecordableServicePtr)
iRecordableServicePtr.stop = new_instancemethod(_enigma.iRecordableServicePtr_stop, None, iRecordableServicePtr)
iRecordableServicePtr.setMarker = new_instancemethod(_enigma.iRecordableServicePtr_setMarker, None, iRecordableServicePtr)
iRecordableServicePtr.setTransformedTimeshift = new_instancemethod(_enigma.iRecordableServicePtr_setTransformedTimeshift, None, iRecordableServicePtr)
iRecordableServicePtr.frontendInfo = new_instancemethod(_enigma.iRecordableServicePtr_frontendInfo, None, iRecordableServicePtr)
iRecordableServicePtr.stream = new_instancemethod(_enigma.iRecordableServicePtr_stream, None, iRecordableServicePtr)
iRecordableServicePtr.subServices = new_instancemethod(_enigma.iRecordableServicePtr_subServices, None, iRecordableServicePtr)
iRecordableServicePtr.getFilenameExtension = new_instancemethod(_enigma.iRecordableServicePtr_getFilenameExtension, None, iRecordableServicePtr)
iRecordableServicePtr.getServiceType = new_instancemethod(_enigma.iRecordableServicePtr_getServiceType, None, iRecordableServicePtr)
iRecordableServicePtr.doFastForward = new_instancemethod(_enigma.iRecordableServicePtr_doFastForward, None, iRecordableServicePtr)
iRecordableServicePtr.getEventRunningState = new_instancemethod(_enigma.iRecordableServicePtr_getEventRunningState, None, iRecordableServicePtr)
iRecordableServicePtr_swigregister = _enigma.iRecordableServicePtr_swigregister
iRecordableServicePtr_swigregister(iRecordableServicePtr)

def New_iRecordableServicePtr(*args):
    return _enigma.New_iRecordableServicePtr(*args)


New_iRecordableServicePtr = _enigma.New_iRecordableServicePtr

class iServiceHandlerPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iServiceHandlerPtr_swiginit(self, _enigma.new_iServiceHandlerPtr(*args))

    __swig_destroy__ = _enigma.delete_iServiceHandlerPtr


iServiceHandlerPtr.__ref__ = new_instancemethod(_enigma.iServiceHandlerPtr___ref__, None, iServiceHandlerPtr)
iServiceHandlerPtr.getPtrString = new_instancemethod(_enigma.iServiceHandlerPtr_getPtrString, None, iServiceHandlerPtr)
iServiceHandlerPtr.__deref__ = new_instancemethod(_enigma.iServiceHandlerPtr___deref__, None, iServiceHandlerPtr)
iServiceHandlerPtr.play = new_instancemethod(_enigma.iServiceHandlerPtr_play, None, iServiceHandlerPtr)
iServiceHandlerPtr.record = new_instancemethod(_enigma.iServiceHandlerPtr_record, None, iServiceHandlerPtr)
iServiceHandlerPtr.list = new_instancemethod(_enigma.iServiceHandlerPtr_list, None, iServiceHandlerPtr)
iServiceHandlerPtr.info = new_instancemethod(_enigma.iServiceHandlerPtr_info, None, iServiceHandlerPtr)
iServiceHandlerPtr.offlineOperations = new_instancemethod(_enigma.iServiceHandlerPtr_offlineOperations, None, iServiceHandlerPtr)
iServiceHandlerPtr_swigregister = _enigma.iServiceHandlerPtr_swigregister
iServiceHandlerPtr_swigregister(iServiceHandlerPtr)

class eServiceCenter(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined - class is abstract')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.eServiceCenter_getInstance)


eServiceCenter_swigregister = _enigma.eServiceCenter_swigregister
eServiceCenter_swigregister(eServiceCenter)

def eServiceCenter_getInstance():
    return _enigma.eServiceCenter_getInstance()


eServiceCenter_getInstance = _enigma.eServiceCenter_getInstance

class ePythonMessagePump(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    recv_msg = _swig_property(_enigma.ePythonMessagePump_recv_msg_get)

    def __init__(self):
        _enigma.ePythonMessagePump_swiginit(self, _enigma.new_ePythonMessagePump())

    __swig_destroy__ = _enigma.delete_ePythonMessagePump


ePythonMessagePump.send = new_instancemethod(_enigma.ePythonMessagePump_send, None, ePythonMessagePump)
ePythonMessagePump.start = new_instancemethod(_enigma.ePythonMessagePump_start, None, ePythonMessagePump)
ePythonMessagePump.stop = new_instancemethod(_enigma.ePythonMessagePump_stop, None, ePythonMessagePump)
ePythonMessagePump_swigregister = _enigma.ePythonMessagePump_swigregister
ePythonMessagePump_swigregister(ePythonMessagePump)

class eTPM(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eTPM_swiginit(self, _enigma.new_eTPM())

    __swig_destroy__ = _enigma.delete_eTPM
    TPMD_DT_LEVEL2_CERT = _enigma.eTPM_TPMD_DT_LEVEL2_CERT
    TPMD_DT_LEVEL3_CERT = _enigma.eTPM_TPMD_DT_LEVEL3_CERT


eTPM.getCert = new_instancemethod(_enigma.eTPM_getCert, None, eTPM)
eTPM.challenge = new_instancemethod(_enigma.eTPM_challenge, None, eTPM)
eTPM_swigregister = _enigma.eTPM_swigregister
eTPM_swigregister(eTPM)

class ePythonConfigQuery(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    setQueryFunc = staticmethod(_enigma.ePythonConfigQuery_setQueryFunc)


ePythonConfigQuery_swigregister = _enigma.ePythonConfigQuery_swigregister
ePythonConfigQuery_swigregister(ePythonConfigQuery)

def ePythonConfigQuery_setQueryFunc(*args):
    return _enigma.ePythonConfigQuery_setQueryFunc(*args)


ePythonConfigQuery_setQueryFunc = _enigma.ePythonConfigQuery_setQueryFunc

class eRCInput(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    kmNone = _enigma.eRCInput_kmNone
    kmAscii = _enigma.eRCInput_kmAscii
    kmAll = _enigma.eRCInput_kmAll
    getInstance = staticmethod(_enigma.eRCInput_getInstance)


eRCInput.setKeyboardMode = new_instancemethod(_enigma.eRCInput_setKeyboardMode, None, eRCInput)
eRCInput.getKeyboardMode = new_instancemethod(_enigma.eRCInput_getKeyboardMode, None, eRCInput)
eRCInput.lock = new_instancemethod(_enigma.eRCInput_lock, None, eRCInput)
eRCInput.unlock = new_instancemethod(_enigma.eRCInput_unlock, None, eRCInput)
eRCInput.islocked = new_instancemethod(_enigma.eRCInput_islocked, None, eRCInput)
eRCInput_swigregister = _enigma.eRCInput_swigregister
eRCInput_swigregister(eRCInput)

def eRCInput_getInstance():
    return _enigma.eRCInput_getInstance()


eRCInput_getInstance = _enigma.eRCInput_getInstance

def addInputDevice(*args):
    return _enigma.addInputDevice(*args)


addInputDevice = _enigma.addInputDevice

def removeInputDevice(*args):
    return _enigma.removeInputDevice(*args)


removeInputDevice = _enigma.removeInputDevice

class fbClass(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.fbClass_getInstance)


fbClass.lock = new_instancemethod(_enigma.fbClass_lock, None, fbClass)
fbClass.unlock = new_instancemethod(_enigma.fbClass_unlock, None, fbClass)
fbClass.islocked = new_instancemethod(_enigma.fbClass_islocked, None, fbClass)
fbClass_swigregister = _enigma.fbClass_swigregister
fbClass_swigregister(fbClass)

def fbClass_getInstance():
    return _enigma.fbClass_getInstance()


fbClass_getInstance = _enigma.fbClass_getInstance

class fontRenderClass(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.fontRenderClass_getInstance)


fontRenderClass.getLineHeight = new_instancemethod(_enigma.fontRenderClass_getLineHeight, None, fontRenderClass)
fontRenderClass_swigregister = _enigma.fontRenderClass_swigregister
fontRenderClass_swigregister(fontRenderClass)

def fontRenderClass_getInstance():
    return _enigma.fontRenderClass_getInstance()


fontRenderClass_getInstance = _enigma.fontRenderClass_getInstance

class gRGB(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    b = _swig_property(_enigma.gRGB_b_get, _enigma.gRGB_b_set)
    g = _swig_property(_enigma.gRGB_g_get, _enigma.gRGB_g_set)
    r = _swig_property(_enigma.gRGB_r_get, _enigma.gRGB_r_set)
    a = _swig_property(_enigma.gRGB_a_get, _enigma.gRGB_a_set)

    def __init__(self, *args):
        _enigma.gRGB_swiginit(self, _enigma.new_gRGB(*args))

    __swig_destroy__ = _enigma.delete_gRGB


gRGB.argb = new_instancemethod(_enigma.gRGB_argb, None, gRGB)
gRGB.__lt__ = new_instancemethod(_enigma.gRGB___lt__, None, gRGB)
gRGB.__eq__ = new_instancemethod(_enigma.gRGB___eq__, None, gRGB)
gRGB.__ne__ = new_instancemethod(_enigma.gRGB___ne__, None, gRGB)
gRGB.alpha_blend = new_instancemethod(_enigma.gRGB_alpha_blend, None, gRGB)
gRGB_swigregister = _enigma.gRGB_swigregister
gRGB_swigregister(gRGB)

class gPixmapPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.gPixmapPtr_swiginit(self, _enigma.new_gPixmapPtr(*args))

    __swig_destroy__ = _enigma.delete_gPixmapPtr


gPixmapPtr.__ref__ = new_instancemethod(_enigma.gPixmapPtr___ref__, None, gPixmapPtr)
gPixmapPtr.getPtrString = new_instancemethod(_enigma.gPixmapPtr_getPtrString, None, gPixmapPtr)
gPixmapPtr.__deref__ = new_instancemethod(_enigma.gPixmapPtr___deref__, None, gPixmapPtr)
gPixmapPtr.size = new_instancemethod(_enigma.gPixmapPtr_size, None, gPixmapPtr)
gPixmapPtr_swigregister = _enigma.gPixmapPtr_swigregister
gPixmapPtr_swigregister(gPixmapPtr)

class gMainDC(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.gMainDC_swiginit(self, _enigma.new_gMainDC(*args))

    __swig_destroy__ = _enigma.delete_gMainDC
    getInstance = staticmethod(_enigma.gMainDC_getInstance)


gMainDC.__ref__ = new_instancemethod(_enigma.gMainDC___ref__, None, gMainDC)
gMainDC.getPtrString = new_instancemethod(_enigma.gMainDC_getPtrString, None, gMainDC)
gMainDC.__deref__ = new_instancemethod(_enigma.gMainDC___deref__, None, gMainDC)
gMainDC.setResolution = new_instancemethod(_enigma.gMainDC_setResolution, None, gMainDC)
gMainDC.setAniMode = new_instancemethod(_enigma.gMainDC_setAniMode, None, gMainDC)
gMainDC_swigregister = _enigma.gMainDC_swigregister
gMainDC_swigregister(gMainDC)

def gMainDC_getInstance():
    return _enigma.gMainDC_getInstance()


gMainDC_getInstance = _enigma.gMainDC_getInstance

class ePoint(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.ePoint_swiginit(self, _enigma.new_ePoint(*args))

    __swig_destroy__ = _enigma.delete_ePoint


ePoint.isNull = new_instancemethod(_enigma.ePoint_isNull, None, ePoint)
ePoint.x = new_instancemethod(_enigma.ePoint_x, None, ePoint)
ePoint.y = new_instancemethod(_enigma.ePoint_y, None, ePoint)
ePoint.setX = new_instancemethod(_enigma.ePoint_setX, None, ePoint)
ePoint.setY = new_instancemethod(_enigma.ePoint_setY, None, ePoint)
ePoint.manhattanLength = new_instancemethod(_enigma.ePoint_manhattanLength, None, ePoint)
ePoint.rx = new_instancemethod(_enigma.ePoint_rx, None, ePoint)
ePoint.ry = new_instancemethod(_enigma.ePoint_ry, None, ePoint)
ePoint.__iadd__ = new_instancemethod(_enigma.ePoint___iadd__, None, ePoint)
ePoint.__isub__ = new_instancemethod(_enigma.ePoint___isub__, None, ePoint)
ePoint.__imul__ = new_instancemethod(_enigma.ePoint___imul__, None, ePoint)
ePoint.__idiv__ = new_instancemethod(_enigma.ePoint___idiv__, None, ePoint)
ePoint_swigregister = _enigma.ePoint_swigregister
ePoint_swigregister(ePoint)

class eRect(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eRect_swiginit(self, _enigma.new_eRect(*args))

    emptyRect = staticmethod(_enigma.eRect_emptyRect)
    invalidRect = staticmethod(_enigma.eRect_invalidRect)
    __swig_destroy__ = _enigma.delete_eRect


eRect.empty = new_instancemethod(_enigma.eRect_empty, None, eRect)
eRect.valid = new_instancemethod(_enigma.eRect_valid, None, eRect)
eRect.normalize = new_instancemethod(_enigma.eRect_normalize, None, eRect)
eRect.left = new_instancemethod(_enigma.eRect_left, None, eRect)
eRect.top = new_instancemethod(_enigma.eRect_top, None, eRect)
eRect.right = new_instancemethod(_enigma.eRect_right, None, eRect)
eRect.bottom = new_instancemethod(_enigma.eRect_bottom, None, eRect)
eRect.rLeft = new_instancemethod(_enigma.eRect_rLeft, None, eRect)
eRect.rTop = new_instancemethod(_enigma.eRect_rTop, None, eRect)
eRect.rRight = new_instancemethod(_enigma.eRect_rRight, None, eRect)
eRect.rBottom = new_instancemethod(_enigma.eRect_rBottom, None, eRect)
eRect.x = new_instancemethod(_enigma.eRect_x, None, eRect)
eRect.y = new_instancemethod(_enigma.eRect_y, None, eRect)
eRect.setLeft = new_instancemethod(_enigma.eRect_setLeft, None, eRect)
eRect.setTop = new_instancemethod(_enigma.eRect_setTop, None, eRect)
eRect.setRight = new_instancemethod(_enigma.eRect_setRight, None, eRect)
eRect.setBottom = new_instancemethod(_enigma.eRect_setBottom, None, eRect)
eRect.setX = new_instancemethod(_enigma.eRect_setX, None, eRect)
eRect.setY = new_instancemethod(_enigma.eRect_setY, None, eRect)
eRect.topLeft = new_instancemethod(_enigma.eRect_topLeft, None, eRect)
eRect.bottomRight = new_instancemethod(_enigma.eRect_bottomRight, None, eRect)
eRect.topRight = new_instancemethod(_enigma.eRect_topRight, None, eRect)
eRect.bottomLeft = new_instancemethod(_enigma.eRect_bottomLeft, None, eRect)
eRect.topLeft1 = new_instancemethod(_enigma.eRect_topLeft1, None, eRect)
eRect.bottomRight1 = new_instancemethod(_enigma.eRect_bottomRight1, None, eRect)
eRect.topRight1 = new_instancemethod(_enigma.eRect_topRight1, None, eRect)
eRect.bottomLeft1 = new_instancemethod(_enigma.eRect_bottomLeft1, None, eRect)
eRect.center = new_instancemethod(_enigma.eRect_center, None, eRect)
eRect.rect = new_instancemethod(_enigma.eRect_rect, None, eRect)
eRect.coords = new_instancemethod(_enigma.eRect_coords, None, eRect)
eRect.moveTopLeft = new_instancemethod(_enigma.eRect_moveTopLeft, None, eRect)
eRect.moveBottomRight = new_instancemethod(_enigma.eRect_moveBottomRight, None, eRect)
eRect.moveTopRight = new_instancemethod(_enigma.eRect_moveTopRight, None, eRect)
eRect.moveBottomLeft = new_instancemethod(_enigma.eRect_moveBottomLeft, None, eRect)
eRect.moveCenter = new_instancemethod(_enigma.eRect_moveCenter, None, eRect)
eRect.moveBy = new_instancemethod(_enigma.eRect_moveBy, None, eRect)
eRect.setRect = new_instancemethod(_enigma.eRect_setRect, None, eRect)
eRect.setCoords = new_instancemethod(_enigma.eRect_setCoords, None, eRect)
eRect.size = new_instancemethod(_enigma.eRect_size, None, eRect)
eRect.width = new_instancemethod(_enigma.eRect_width, None, eRect)
eRect.height = new_instancemethod(_enigma.eRect_height, None, eRect)
eRect.setWidth = new_instancemethod(_enigma.eRect_setWidth, None, eRect)
eRect.setHeight = new_instancemethod(_enigma.eRect_setHeight, None, eRect)
eRect.setSize = new_instancemethod(_enigma.eRect_setSize, None, eRect)
eRect.__or__ = new_instancemethod(_enigma.eRect___or__, None, eRect)
eRect.__and__ = new_instancemethod(_enigma.eRect___and__, None, eRect)
eRect.__ior__ = new_instancemethod(_enigma.eRect___ior__, None, eRect)
eRect.__iand__ = new_instancemethod(_enigma.eRect___iand__, None, eRect)
eRect.contains = new_instancemethod(_enigma.eRect_contains, None, eRect)
eRect.unite = new_instancemethod(_enigma.eRect_unite, None, eRect)
eRect.intersect = new_instancemethod(_enigma.eRect_intersect, None, eRect)
eRect.intersects = new_instancemethod(_enigma.eRect_intersects, None, eRect)
eRect.scale = new_instancemethod(_enigma.eRect_scale, None, eRect)
eRect_swigregister = _enigma.eRect_swigregister
eRect_swigregister(eRect)

def eRect_emptyRect():
    return _enigma.eRect_emptyRect()


eRect_emptyRect = _enigma.eRect_emptyRect

def eRect_invalidRect():
    return _enigma.eRect_invalidRect()


eRect_invalidRect = _enigma.eRect_invalidRect

class eSize(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eSize_swiginit(self, _enigma.new_eSize(*args))

    __swig_destroy__ = _enigma.delete_eSize


eSize.isNull = new_instancemethod(_enigma.eSize_isNull, None, eSize)
eSize.isEmpty = new_instancemethod(_enigma.eSize_isEmpty, None, eSize)
eSize.isValid = new_instancemethod(_enigma.eSize_isValid, None, eSize)
eSize.width = new_instancemethod(_enigma.eSize_width, None, eSize)
eSize.height = new_instancemethod(_enigma.eSize_height, None, eSize)
eSize.setWidth = new_instancemethod(_enigma.eSize_setWidth, None, eSize)
eSize.setHeight = new_instancemethod(_enigma.eSize_setHeight, None, eSize)
eSize.transpose = new_instancemethod(_enigma.eSize_transpose, None, eSize)
eSize.expandedTo = new_instancemethod(_enigma.eSize_expandedTo, None, eSize)
eSize.boundedTo = new_instancemethod(_enigma.eSize_boundedTo, None, eSize)
eSize.rwidth = new_instancemethod(_enigma.eSize_rwidth, None, eSize)
eSize.rheight = new_instancemethod(_enigma.eSize_rheight, None, eSize)
eSize.__iadd__ = new_instancemethod(_enigma.eSize___iadd__, None, eSize)
eSize.__isub__ = new_instancemethod(_enigma.eSize___isub__, None, eSize)
eSize.__imul__ = new_instancemethod(_enigma.eSize___imul__, None, eSize)
eSize.__idiv__ = new_instancemethod(_enigma.eSize___idiv__, None, eSize)
eSize_swigregister = _enigma.eSize_swigregister
eSize_swigregister(eSize)
MAX_LAYER = _enigma.MAX_LAYER

class eWidget(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eWidget_swiginit(self, _enigma.new_eWidget(*args))

    __swig_destroy__ = _enigma.delete_eWidget
    m_animation = _swig_property(_enigma.eWidget_m_animation_get, _enigma.eWidget_m_animation_set)
    wVisShow = _enigma.eWidget_wVisShow
    wVisTransparent = _enigma.eWidget_wVisTransparent
    m_vis = _swig_property(_enigma.eWidget_m_vis_get, _enigma.eWidget_m_vis_set)
    m_clip_region = _swig_property(_enigma.eWidget_m_clip_region_get, _enigma.eWidget_m_clip_region_set)
    m_visible_region = _swig_property(_enigma.eWidget_m_visible_region_get, _enigma.eWidget_m_visible_region_set)
    m_visible_with_childs = _swig_property(_enigma.eWidget_m_visible_with_childs_get, _enigma.eWidget_m_visible_with_childs_set)
    m_comp_buffer = _swig_property(_enigma.eWidget_m_comp_buffer_get, _enigma.eWidget_m_comp_buffer_set)
    evtPaint = _enigma.eWidget_evtPaint
    evtKey = _enigma.eWidget_evtKey
    evtChangedPosition = _enigma.eWidget_evtChangedPosition
    evtChangedSize = _enigma.eWidget_evtChangedSize
    evtParentChangedPosition = _enigma.eWidget_evtParentChangedPosition
    evtParentVisibilityChanged = _enigma.eWidget_evtParentVisibilityChanged
    evtWillChangePosition = _enigma.eWidget_evtWillChangePosition
    evtWillChangeSize = _enigma.eWidget_evtWillChangeSize
    evtAction = _enigma.eWidget_evtAction
    evtFocusGot = _enigma.eWidget_evtFocusGot
    evtFocusLost = _enigma.eWidget_evtFocusLost
    evtUserWidget = _enigma.eWidget_evtUserWidget


eWidget.move = new_instancemethod(_enigma.eWidget_move, None, eWidget)
eWidget.resize = new_instancemethod(_enigma.eWidget_resize, None, eWidget)
eWidget.position = new_instancemethod(_enigma.eWidget_position, None, eWidget)
eWidget.size = new_instancemethod(_enigma.eWidget_size, None, eWidget)
eWidget.csize = new_instancemethod(_enigma.eWidget_csize, None, eWidget)
eWidget.invalidate = new_instancemethod(_enigma.eWidget_invalidate, None, eWidget)
eWidget.child = new_instancemethod(_enigma.eWidget_child, None, eWidget)
eWidget.show = new_instancemethod(_enigma.eWidget_show, None, eWidget)
eWidget.hide = new_instancemethod(_enigma.eWidget_hide, None, eWidget)
eWidget.destruct = new_instancemethod(_enigma.eWidget_destruct, None, eWidget)
eWidget.getStyle = new_instancemethod(_enigma.eWidget_getStyle, None, eWidget)
eWidget.setStyle = new_instancemethod(_enigma.eWidget_setStyle, None, eWidget)
eWidget.setBackgroundColor = new_instancemethod(_enigma.eWidget_setBackgroundColor, None, eWidget)
eWidget.clearBackgroundColor = new_instancemethod(_enigma.eWidget_clearBackgroundColor, None, eWidget)
eWidget.setZPosition = new_instancemethod(_enigma.eWidget_setZPosition, None, eWidget)
eWidget.setTransparent = new_instancemethod(_enigma.eWidget_setTransparent, None, eWidget)
eWidget.isVisible = new_instancemethod(_enigma.eWidget_isVisible, None, eWidget)
eWidget.isTransparent = new_instancemethod(_enigma.eWidget_isTransparent, None, eWidget)
eWidget.getAbsolutePosition = new_instancemethod(_enigma.eWidget_getAbsolutePosition, None, eWidget)
eWidget.recalcClipRegionsWhenVisible = new_instancemethod(_enigma.eWidget_recalcClipRegionsWhenVisible, None, eWidget)
eWidget.event = new_instancemethod(_enigma.eWidget_event, None, eWidget)
eWidget.setFocus = new_instancemethod(_enigma.eWidget_setFocus, None, eWidget)

eWidget.notifyShowHide = new_instancemethod(_enigma.eWidget_notifyShowHide, None, eWidget)
eWidget_swigregister = _enigma.eWidget_swigregister
eWidget_swigregister(eWidget)

def getDesktop(*args):
    return _enigma.getDesktop(*args)


getDesktop = _enigma.getDesktop

class eLabel(eWidget):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eLabel_swiginit(self, _enigma.new_eLabel(*args))

    alignLeft = _enigma.eLabel_alignLeft
    alignTop = _enigma.eLabel_alignTop
    alignCenter = _enigma.eLabel_alignCenter
    alignRight = _enigma.eLabel_alignRight
    alignBottom = _enigma.eLabel_alignBottom
    alignBlock = _enigma.eLabel_alignBlock
    __swig_destroy__ = _enigma.delete_eLabel


eLabel.setText = new_instancemethod(_enigma.eLabel_setText, None, eLabel)
eLabel.setMarkedPos = new_instancemethod(_enigma.eLabel_setMarkedPos, None, eLabel)
eLabel.setFont = new_instancemethod(_enigma.eLabel_setFont, None, eLabel)
eLabel.getFont = new_instancemethod(_enigma.eLabel_getFont, None, eLabel)
eLabel.setVAlign = new_instancemethod(_enigma.eLabel_setVAlign, None, eLabel)
eLabel.setHAlign = new_instancemethod(_enigma.eLabel_setHAlign, None, eLabel)
eLabel.setForegroundColor = new_instancemethod(_enigma.eLabel_setForegroundColor, None, eLabel)
eLabel.setShadowColor = new_instancemethod(_enigma.eLabel_setShadowColor, None, eLabel)
eLabel.setShadowOffset = new_instancemethod(_enigma.eLabel_setShadowOffset, None, eLabel)
eLabel.setNoWrap = new_instancemethod(_enigma.eLabel_setNoWrap, None, eLabel)
eLabel.clearForegroundColor = new_instancemethod(_enigma.eLabel_clearForegroundColor, None, eLabel)
eLabel.calculateSize = new_instancemethod(_enigma.eLabel_calculateSize, None, eLabel)
eLabel_swigregister = _enigma.eLabel_swigregister
eLabel_swigregister(eLabel)

class eInput(eWidget):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eInput_swiginit(self, _enigma.new_eInput(*args))

    __swig_destroy__ = _enigma.delete_eInput
    changed = _swig_property(_enigma.eInput_changed_get)
    m_cursor = _swig_property(_enigma.eInput_m_cursor_get, _enigma.eInput_m_cursor_set)
    INPUT_ACTIONS = _enigma.eInput_INPUT_ACTIONS
    ASCII_ACTIONS = _enigma.eInput_ASCII_ACTIONS
    moveLeft = _enigma.eInput_moveLeft
    moveRight = _enigma.eInput_moveRight
    moveHome = _enigma.eInput_moveHome
    moveEnd = _enigma.eInput_moveEnd
    deleteForward = _enigma.eInput_deleteForward
    deleteBackward = _enigma.eInput_deleteBackward
    toggleOverwrite = _enigma.eInput_toggleOverwrite
    accept = _enigma.eInput_accept
    gotAsciiCode = _enigma.eInput_gotAsciiCode


eInput.setContent = new_instancemethod(_enigma.eInput_setContent, None, eInput)
eInput.setOverwriteMode = new_instancemethod(_enigma.eInput_setOverwriteMode, None, eInput)
eInput.setFont = new_instancemethod(_enigma.eInput_setFont, None, eInput)
eInput_swigregister = _enigma.eInput_swigregister
eInput_swigregister(eInput)

class eInputContent(iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined - class is abstract')

    __repr__ = _swig_repr
    dirLeft = _enigma.eInputContent_dirLeft
    dirRight = _enigma.eInputContent_dirRight
    dirHome = _enigma.eInputContent_dirHome
    dirEnd = _enigma.eInputContent_dirEnd
    dirUser = _enigma.eInputContent_dirUser
    deleteForward = _enigma.eInputContent_deleteForward
    deleteBackward = _enigma.eInputContent_deleteBackward
    __swig_destroy__ = _enigma.delete_eInputContent


eInputContent.setInput = new_instancemethod(_enigma.eInputContent_setInput, None, eInputContent)
eInputContent.getDisplay = new_instancemethod(_enigma.eInputContent_getDisplay, None, eInputContent)
eInputContent.moveCursor = new_instancemethod(_enigma.eInputContent_moveCursor, None, eInputContent)
eInputContent.deleteChar = new_instancemethod(_enigma.eInputContent_deleteChar, None, eInputContent)
eInputContent.haveKey = new_instancemethod(_enigma.eInputContent_haveKey, None, eInputContent)
eInputContent.isValid = new_instancemethod(_enigma.eInputContent_isValid, None, eInputContent)
eInputContent.validate = new_instancemethod(_enigma.eInputContent_validate, None, eInputContent)
eInputContent_swigregister = _enigma.eInputContent_swigregister
eInputContent_swigregister(eInputContent)

class eInputContentString(eInputContent):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eInputContentString_swiginit(self, _enigma.new_eInputContentString())

    __swig_destroy__ = _enigma.delete_eInputContentString


eInputContentString.setText = new_instancemethod(_enigma.eInputContentString_setText, None, eInputContentString)
eInputContentString.getText = new_instancemethod(_enigma.eInputContentString_getText, None, eInputContentString)
eInputContentString_swigregister = _enigma.eInputContentString_swigregister
eInputContentString_swigregister(eInputContentString)

class eInputContentNumber(eInputContent):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eInputContentNumber_swiginit(self, _enigma.new_eInputContentNumber(*args))

    __swig_destroy__ = _enigma.delete_eInputContentNumber


eInputContentNumber.setValue = new_instancemethod(_enigma.eInputContentNumber_setValue, None, eInputContentNumber)
eInputContentNumber.getValue = new_instancemethod(_enigma.eInputContentNumber_getValue, None, eInputContentNumber)
eInputContentNumber_swigregister = _enigma.eInputContentNumber_swigregister
eInputContentNumber_swigregister(eInputContentNumber)

class ePixmap(eWidget):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.ePixmap_swiginit(self, _enigma.new_ePixmap(*args))

    __swig_destroy__ = _enigma.delete_ePixmap


ePixmap.setPixmap = new_instancemethod(_enigma.ePixmap_setPixmap, None, ePixmap)
ePixmap.setPixmapFromFile = new_instancemethod(_enigma.ePixmap_setPixmapFromFile, None, ePixmap)
ePixmap.setAlphatest = new_instancemethod(_enigma.ePixmap_setAlphatest, None, ePixmap)
ePixmap.setScale = new_instancemethod(_enigma.ePixmap_setScale, None, ePixmap)
ePixmap.setBorderWidth = new_instancemethod(_enigma.ePixmap_setBorderWidth, None, ePixmap)
ePixmap.setBorderColor = new_instancemethod(_enigma.ePixmap_setBorderColor, None, ePixmap)
ePixmap_swigregister = _enigma.ePixmap_swigregister
ePixmap_swigregister(ePixmap)

class eCanvas(ePixmap):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eCanvas_swiginit(self, _enigma.new_eCanvas(*args))

    __swig_destroy__ = _enigma.delete_eCanvas


eCanvas.setSize = new_instancemethod(_enigma.eCanvas_setSize, None, eCanvas)
eCanvas.clear = new_instancemethod(_enigma.eCanvas_clear, None, eCanvas)
eCanvas.fillRect = new_instancemethod(_enigma.eCanvas_fillRect, None, eCanvas)
eCanvas.writeText = new_instancemethod(_enigma.eCanvas_writeText, None, eCanvas)
eCanvas_swigregister = _enigma.eCanvas_swigregister
eCanvas_swigregister(eCanvas)

class eButton(eLabel):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eButton_swiginit(self, _enigma.new_eButton(*args))

    selected = _swig_property(_enigma.eButton_selected_get)
    __swig_destroy__ = _enigma.delete_eButton


eButton.push = new_instancemethod(_enigma.eButton_push, None, eButton)
eButton_swigregister = _enigma.eButton_swigregister
eButton_swigregister(eButton)

class eWindow(eWidget):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eWindow_swiginit(self, _enigma.new_eWindow(*args))

    __swig_destroy__ = _enigma.delete_eWindow
    wfNoBorder = _enigma.eWindow_wfNoBorder


eWindow.setTitle = new_instancemethod(_enigma.eWindow_setTitle, None, eWindow)
eWindow.getTitle = new_instancemethod(_enigma.eWindow_getTitle, None, eWindow)
eWindow.show = new_instancemethod(_enigma.eWindow_show, None, eWindow)
eWindow.hide = new_instancemethod(_enigma.eWindow_hide, None, eWindow)
eWindow.setBackgroundColor = new_instancemethod(_enigma.eWindow_setBackgroundColor, None, eWindow)
eWindow.setFlag = new_instancemethod(_enigma.eWindow_setFlag, None, eWindow)
eWindow.clearFlag = new_instancemethod(_enigma.eWindow_clearFlag, None, eWindow)
eWindow.setAnimationMode = new_instancemethod(_enigma.eWindow_setAnimationMode, None, eWindow)
eWindow_swigregister = _enigma.eWindow_swigregister
eWindow_swigregister(eWindow)

class eSlider(eWidget):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eSlider_swiginit(self, _enigma.new_eSlider(*args))

    orHorizontal = _enigma.eSlider_orHorizontal
    orVertical = _enigma.eSlider_orVertical
    __swig_destroy__ = _enigma.delete_eSlider


eSlider.setValue = new_instancemethod(_enigma.eSlider_setValue, None, eSlider)
eSlider.setStartEnd = new_instancemethod(_enigma.eSlider_setStartEnd, None, eSlider)
eSlider.setRange = new_instancemethod(_enigma.eSlider_setRange, None, eSlider)
eSlider.setOrientation = new_instancemethod(_enigma.eSlider_setOrientation, None, eSlider)
eSlider.setBorderWidth = new_instancemethod(_enigma.eSlider_setBorderWidth, None, eSlider)
eSlider.setBorderColor = new_instancemethod(_enigma.eSlider_setBorderColor, None, eSlider)
eSlider.setSliderBorderColor = new_instancemethod(_enigma.eSlider_setSliderBorderColor, None, eSlider)
eSlider.setForegroundColor = new_instancemethod(_enigma.eSlider_setForegroundColor, None, eSlider)
eSlider.setSliderForegroundColor = new_instancemethod(_enigma.eSlider_setSliderForegroundColor, None, eSlider)
eSlider.setPixmap = new_instancemethod(_enigma.eSlider_setPixmap, None, eSlider)
eSlider.setScrollbarSliderPicture = new_instancemethod(_enigma.eSlider_setScrollbarSliderPicture, None, eSlider)
eSlider.setBackgroundPixmap = new_instancemethod(_enigma.eSlider_setBackgroundPixmap, None, eSlider)
eSlider.setScrollbarBackgroundPicture = new_instancemethod(_enigma.eSlider_setScrollbarBackgroundPicture, None, eSlider)
eSlider_swigregister = _enigma.eSlider_swigregister
eSlider_swigregister(eSlider)

class ePositionGauge(eWidget):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.ePositionGauge_swiginit(self, _enigma.new_ePositionGauge(*args))

    __swig_destroy__ = _enigma.delete_ePositionGauge


ePositionGauge.setLength = new_instancemethod(_enigma.ePositionGauge_setLength, None, ePositionGauge)
ePositionGauge.setPosition = new_instancemethod(_enigma.ePositionGauge_setPosition, None, ePositionGauge)
ePositionGauge.setInColor = new_instancemethod(_enigma.ePositionGauge_setInColor, None, ePositionGauge)
ePositionGauge.setPointer = new_instancemethod(_enigma.ePositionGauge_setPointer, None, ePositionGauge)
ePositionGauge.setInOutList = new_instancemethod(_enigma.ePositionGauge_setInOutList, None, ePositionGauge)
ePositionGauge.setForegroundColor = new_instancemethod(_enigma.ePositionGauge_setForegroundColor, None, ePositionGauge)
ePositionGauge.enableSeekPointer = new_instancemethod(_enigma.ePositionGauge_enableSeekPointer, None, ePositionGauge)
ePositionGauge.setSeekPosition = new_instancemethod(_enigma.ePositionGauge_setSeekPosition, None, ePositionGauge)
ePositionGauge_swigregister = _enigma.ePositionGauge_swigregister
ePositionGauge_swigregister(ePositionGauge)

class eWidgetDesktopCompBuffer(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    m_position = _swig_property(_enigma.eWidgetDesktopCompBuffer_m_position_get, _enigma.eWidgetDesktopCompBuffer_m_position_set)
    m_screen_size = _swig_property(_enigma.eWidgetDesktopCompBuffer_m_screen_size_get, _enigma.eWidgetDesktopCompBuffer_m_screen_size_set)
    m_dirty_region = _swig_property(_enigma.eWidgetDesktopCompBuffer_m_dirty_region_get, _enigma.eWidgetDesktopCompBuffer_m_dirty_region_set)
    m_background_region = _swig_property(_enigma.eWidgetDesktopCompBuffer_m_background_region_get, _enigma.eWidgetDesktopCompBuffer_m_background_region_set)
    m_dc = _swig_property(_enigma.eWidgetDesktopCompBuffer_m_dc_get, _enigma.eWidgetDesktopCompBuffer_m_dc_set)
    m_background_color = _swig_property(_enigma.eWidgetDesktopCompBuffer_m_background_color_get, _enigma.eWidgetDesktopCompBuffer_m_background_color_set)

    def __init__(self):
        _enigma.eWidgetDesktopCompBuffer_swiginit(self, _enigma.new_eWidgetDesktopCompBuffer())

    __swig_destroy__ = _enigma.delete_eWidgetDesktopCompBuffer


eWidgetDesktopCompBuffer_swigregister = _enigma.eWidgetDesktopCompBuffer_swigregister
eWidgetDesktopCompBuffer_swigregister(eWidgetDesktopCompBuffer)

class eWidgetDesktop(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eWidgetDesktop_swiginit(self, _enigma.new_eWidgetDesktop(*args))

    __swig_destroy__ = _enigma.delete_eWidgetDesktop
    cmImmediate = _enigma.eWidgetDesktop_cmImmediate
    cmBuffered = _enigma.eWidgetDesktop_cmBuffered


eWidgetDesktop.addRootWidget = new_instancemethod(_enigma.eWidgetDesktop_addRootWidget, None, eWidgetDesktop)
eWidgetDesktop.removeRootWidget = new_instancemethod(_enigma.eWidgetDesktop_removeRootWidget, None, eWidgetDesktop)
eWidgetDesktop.movedWidget = new_instancemethod(_enigma.eWidgetDesktop_movedWidget, None, eWidgetDesktop)
eWidgetDesktop.recalcClipRegions = new_instancemethod(_enigma.eWidgetDesktop_recalcClipRegions, None, eWidgetDesktop)
eWidgetDesktop.invalidateWidgetLayer = new_instancemethod(_enigma.eWidgetDesktop_invalidateWidgetLayer, None, eWidgetDesktop)
eWidgetDesktop.invalidateWidget = new_instancemethod(_enigma.eWidgetDesktop_invalidateWidget, None, eWidgetDesktop)
eWidgetDesktop.invalidate = new_instancemethod(_enigma.eWidgetDesktop_invalidate, None, eWidgetDesktop)
eWidgetDesktop.paintLayer = new_instancemethod(_enigma.eWidgetDesktop_paintLayer, None, eWidgetDesktop)
eWidgetDesktop.paint = new_instancemethod(_enigma.eWidgetDesktop_paint, None, eWidgetDesktop)
eWidgetDesktop.setDC = new_instancemethod(_enigma.eWidgetDesktop_setDC, None, eWidgetDesktop)
eWidgetDesktop.setBackgroundColor = new_instancemethod(_enigma.eWidgetDesktop_setBackgroundColor, None, eWidgetDesktop)
eWidgetDesktop.setPalette = new_instancemethod(_enigma.eWidgetDesktop_setPalette, None, eWidgetDesktop)
eWidgetDesktop.setRedrawTask = new_instancemethod(_enigma.eWidgetDesktop_setRedrawTask, None, eWidgetDesktop)
eWidgetDesktop.makeCompatiblePixmap = new_instancemethod(_enigma.eWidgetDesktop_makeCompatiblePixmap, None, eWidgetDesktop)
eWidgetDesktop.setCompositionMode = new_instancemethod(_enigma.eWidgetDesktop_setCompositionMode, None, eWidgetDesktop)
eWidgetDesktop.getStyleID = new_instancemethod(_enigma.eWidgetDesktop_getStyleID, None, eWidgetDesktop)
eWidgetDesktop.setStyleID = new_instancemethod(_enigma.eWidgetDesktop_setStyleID, None, eWidgetDesktop)
eWidgetDesktop.resize = new_instancemethod(_enigma.eWidgetDesktop_resize, None, eWidgetDesktop)
eWidgetDesktop.size = new_instancemethod(_enigma.eWidgetDesktop_size, None, eWidgetDesktop)
eWidgetDesktop.sendShow = new_instancemethod(_enigma.eWidgetDesktop_sendShow, None, eWidgetDesktop)
eWidgetDesktop.sendHide = new_instancemethod(_enigma.eWidgetDesktop_sendHide, None, eWidgetDesktop)
eWidgetDesktop_swigregister = _enigma.eWidgetDesktop_swigregister
eWidgetDesktop_swigregister(eWidgetDesktop)

class iListboxContent(iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined - class is abstract')

    __repr__ = _swig_repr
    __swig_destroy__ = _enigma.delete_iListboxContent


iListboxContent_swigregister = _enigma.iListboxContent_swigregister
iListboxContent_swigregister(iListboxContent)

class eListbox(eWidget):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eListbox_swiginit(self, _enigma.new_eListbox(*args))

    __swig_destroy__ = _enigma.delete_eListbox
    selectionChanged = _swig_property(_enigma.eListbox_selectionChanged_get)
    showOnDemand = _enigma.eListbox_showOnDemand
    showAlways = _enigma.eListbox_showAlways
    showNever = _enigma.eListbox_showNever
    alignLeft = _enigma.eListbox_alignLeft
    alignTop = _enigma.eListbox_alignTop
    alignCenter = _enigma.eListbox_alignCenter
    alignRight = _enigma.eListbox_alignRight
    alignBottom = _enigma.eListbox_alignBottom
    alignBlock = _enigma.eListbox_alignBlock
    moveUp = _enigma.eListbox_moveUp
    moveDown = _enigma.eListbox_moveDown
    moveTop = _enigma.eListbox_moveTop
    moveEnd = _enigma.eListbox_moveEnd
    pageUp = _enigma.eListbox_pageUp
    pageDown = _enigma.eListbox_pageDown
    justCheck = _enigma.eListbox_justCheck


eListbox.setScrollbarMode = new_instancemethod(_enigma.eListbox_setScrollbarMode, None, eListbox)
eListbox.setOnlyFullEntries = new_instancemethod(_enigma.eListbox_setOnlyFullEntries, None, eListbox)
eListbox.setWrapAround = new_instancemethod(_enigma.eListbox_setWrapAround, None, eListbox)
eListbox.setScrollbarSliderBorderWidth = new_instancemethod(_enigma.eListbox_setScrollbarSliderBorderWidth, None, eListbox)
eListbox.setScrollbarWidth = new_instancemethod(_enigma.eListbox_setScrollbarWidth, None, eListbox)
eListbox.setScrollbarBackgroundPicture = new_instancemethod(_enigma.eListbox_setScrollbarBackgroundPicture, None, eListbox)
eListbox.setScrollbarSliderPicture = new_instancemethod(_enigma.eListbox_setScrollbarSliderPicture, None, eListbox)
eListbox.setSliderBorderColor = new_instancemethod(_enigma.eListbox_setSliderBorderColor, None, eListbox)
eListbox.setSliderForegroundColor = new_instancemethod(_enigma.eListbox_setSliderForegroundColor, None, eListbox)
eListbox.setScrollbarGap = new_instancemethod(_enigma.eListbox_setScrollbarGap, None, eListbox)
eListbox.keepScrollbarGapColor = new_instancemethod(_enigma.eListbox_keepScrollbarGapColor, None, eListbox)
eListbox.setContent = new_instancemethod(_enigma.eListbox_setContent, None, eListbox)
eListbox.getCurrentIndex = new_instancemethod(_enigma.eListbox_getCurrentIndex, None, eListbox)
eListbox.moveSelection = new_instancemethod(_enigma.eListbox_moveSelection, None, eListbox)
eListbox.moveSelectionTo = new_instancemethod(_enigma.eListbox_moveSelectionTo, None, eListbox)
eListbox.moveToEnd = new_instancemethod(_enigma.eListbox_moveToEnd, None, eListbox)
eListbox.atBegin = new_instancemethod(_enigma.eListbox_atBegin, None, eListbox)
eListbox.atEnd = new_instancemethod(_enigma.eListbox_atEnd, None, eListbox)
eListbox.setItemHeight = new_instancemethod(_enigma.eListbox_setItemHeight, None, eListbox)
eListbox.setItemWidth = new_instancemethod(_enigma.eListbox_setItemWidth, None, eListbox)
eListbox.setSelectionEnable = new_instancemethod(_enigma.eListbox_setSelectionEnable, None, eListbox)
eListbox.setOrientation = new_instancemethod(_enigma.eListbox_setOrientation, None, eListbox)
eListbox.setScrollBarOrientation = new_instancemethod(_enigma.eListbox_setScrollBarOrientation, None, eListbox)
eListbox.setBackgroundColor = new_instancemethod(_enigma.eListbox_setBackgroundColor, None, eListbox)
eListbox.setBackgroundColorRows = new_instancemethod(_enigma.eListbox_setBackgroundColorRows, None, eListbox)
eListbox.setBackgroundColorSelected = new_instancemethod(_enigma.eListbox_setBackgroundColorSelected, None, eListbox)
eListbox.setForegroundColor = new_instancemethod(_enigma.eListbox_setForegroundColor, None, eListbox)
eListbox.setForegroundColorRows = new_instancemethod(_enigma.eListbox_setForegroundColorRows, None, eListbox)
eListbox.setForegroundColorSelected = new_instancemethod(_enigma.eListbox_setForegroundColorSelected, None, eListbox)
eListbox.setDescriptionColor = new_instancemethod(_enigma.eListbox_setDescriptionColor, None, eListbox)
eListbox.setBackgroundPicture = new_instancemethod(_enigma.eListbox_setBackgroundPicture, None, eListbox)
eListbox.setSelectionPicture = new_instancemethod(_enigma.eListbox_setSelectionPicture, None, eListbox)
eListbox.setFont = new_instancemethod(_enigma.eListbox_setFont, None, eListbox)
eListbox.setSecondFont = new_instancemethod(_enigma.eListbox_setSecondFont, None, eListbox)
eListbox.setDescriptionFont = new_instancemethod(_enigma.eListbox_setDescriptionFont, None, eListbox)
eListbox.setTextOffset = new_instancemethod(_enigma.eListbox_setTextOffset, None, eListbox)
eListbox.setNoWrap = new_instancemethod(_enigma.eListbox_setNoWrap, None, eListbox)
eListbox.setConfigTextWidth = new_instancemethod(_enigma.eListbox_setConfigTextWidth, None, eListbox)
eListbox.setVAlign = new_instancemethod(_enigma.eListbox_setVAlign, None, eListbox)
eListbox.setVAlignSecond = new_instancemethod(_enigma.eListbox_setVAlignSecond, None, eListbox)
eListbox_swigregister = _enigma.eListbox_swigregister
eListbox_swigregister(eListbox)

class eListboxPythonStringContent(iListboxContent):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eListboxPythonStringContent_swiginit(self, _enigma.new_eListboxPythonStringContent())

    __swig_destroy__ = _enigma.delete_eListboxPythonStringContent


eListboxPythonStringContent.setList = new_instancemethod(_enigma.eListboxPythonStringContent_setList, None, eListboxPythonStringContent)
eListboxPythonStringContent.getCurrentSelection = new_instancemethod(_enigma.eListboxPythonStringContent_getCurrentSelection, None, eListboxPythonStringContent)
eListboxPythonStringContent.getCurrentSelectionIndex = new_instancemethod(_enigma.eListboxPythonStringContent_getCurrentSelectionIndex, None, eListboxPythonStringContent)
eListboxPythonStringContent.invalidateEntry = new_instancemethod(_enigma.eListboxPythonStringContent_invalidateEntry, None, eListboxPythonStringContent)
eListboxPythonStringContent.invalidate = new_instancemethod(_enigma.eListboxPythonStringContent_invalidate, None, eListboxPythonStringContent)
eListboxPythonStringContent.getItemSize = new_instancemethod(_enigma.eListboxPythonStringContent_getItemSize, None, eListboxPythonStringContent)
eListboxPythonStringContent_swigregister = _enigma.eListboxPythonStringContent_swigregister
eListboxPythonStringContent_swigregister(eListboxPythonStringContent)

class eListboxPythonConfigContent(eListboxPythonStringContent):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eListboxPythonConfigContent_swiginit(self, _enigma.new_eListboxPythonConfigContent())

    __swig_destroy__ = _enigma.delete_eListboxPythonConfigContent


eListboxPythonConfigContent.paint = new_instancemethod(_enigma.eListboxPythonConfigContent_paint, None, eListboxPythonConfigContent)
eListboxPythonConfigContent.setSeperation = new_instancemethod(_enigma.eListboxPythonConfigContent_setSeperation, None, eListboxPythonConfigContent)
eListboxPythonConfigContent.currentCursorSelectable = new_instancemethod(_enigma.eListboxPythonConfigContent_currentCursorSelectable, None, eListboxPythonConfigContent)
eListboxPythonConfigContent.isDescription = new_instancemethod(_enigma.eListboxPythonConfigContent_isDescription, None, eListboxPythonConfigContent)
eListboxPythonConfigContent_swigregister = _enigma.eListboxPythonConfigContent_swigregister
eListboxPythonConfigContent_swigregister(eListboxPythonConfigContent)

class eListboxPythonMultiContent(eListboxPythonStringContent):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eListboxPythonMultiContent_swiginit(self, _enigma.new_eListboxPythonMultiContent())

    __swig_destroy__ = _enigma.delete_eListboxPythonMultiContent
    TYPE_TEXT = _enigma.eListboxPythonMultiContent_TYPE_TEXT
    TYPE_PROGRESS = _enigma.eListboxPythonMultiContent_TYPE_PROGRESS
    TYPE_PIXMAP = _enigma.eListboxPythonMultiContent_TYPE_PIXMAP
    TYPE_PIXMAP_ALPHATEST = _enigma.eListboxPythonMultiContent_TYPE_PIXMAP_ALPHATEST
    TYPE_PIXMAP_ALPHABLEND = _enigma.eListboxPythonMultiContent_TYPE_PIXMAP_ALPHABLEND
    TYPE_PROGRESS_PIXMAP = _enigma.eListboxPythonMultiContent_TYPE_PROGRESS_PIXMAP


eListboxPythonMultiContent.paint = new_instancemethod(_enigma.eListboxPythonMultiContent_paint, None, eListboxPythonMultiContent)
eListboxPythonMultiContent.currentCursorSelectable = new_instancemethod(_enigma.eListboxPythonMultiContent_currentCursorSelectable, None, eListboxPythonMultiContent)
eListboxPythonMultiContent.setList = new_instancemethod(_enigma.eListboxPythonMultiContent_setList, None, eListboxPythonMultiContent)
eListboxPythonMultiContent.setFont = new_instancemethod(_enigma.eListboxPythonMultiContent_setFont, None, eListboxPythonMultiContent)
eListboxPythonMultiContent.setBuildFunc = new_instancemethod(_enigma.eListboxPythonMultiContent_setBuildFunc, None, eListboxPythonMultiContent)
eListboxPythonMultiContent.setSelectableFunc = new_instancemethod(_enigma.eListboxPythonMultiContent_setSelectableFunc, None, eListboxPythonMultiContent)
eListboxPythonMultiContent.setItemHeight = new_instancemethod(_enigma.eListboxPythonMultiContent_setItemHeight, None, eListboxPythonMultiContent)
eListboxPythonMultiContent.setSelectionClip = new_instancemethod(_enigma.eListboxPythonMultiContent_setSelectionClip, None, eListboxPythonMultiContent)
eListboxPythonMultiContent.updateClip = new_instancemethod(_enigma.eListboxPythonMultiContent_updateClip, None, eListboxPythonMultiContent)
eListboxPythonMultiContent.entryRemoved = new_instancemethod(_enigma.eListboxPythonMultiContent_entryRemoved, None, eListboxPythonMultiContent)
eListboxPythonMultiContent.setTemplate = new_instancemethod(_enigma.eListboxPythonMultiContent_setTemplate, None, eListboxPythonMultiContent)
eListboxPythonMultiContent_swigregister = _enigma.eListboxPythonMultiContent_swigregister
eListboxPythonMultiContent_swigregister(eListboxPythonMultiContent)
RT_HALIGN_LEFT = _enigma.RT_HALIGN_LEFT
RT_HALIGN_RIGHT = _enigma.RT_HALIGN_RIGHT
RT_HALIGN_CENTER = _enigma.RT_HALIGN_CENTER
RT_HALIGN_BLOCK = _enigma.RT_HALIGN_BLOCK
RT_VALIGN_TOP = _enigma.RT_VALIGN_TOP
RT_VALIGN_CENTER = _enigma.RT_VALIGN_CENTER
RT_VALIGN_BOTTOM = _enigma.RT_VALIGN_BOTTOM
RT_WRAP = _enigma.RT_WRAP
BT_SCALE = _enigma.BT_SCALE
BT_FIXRATIO = _enigma.BT_FIXRATIO

class eWindowStyle(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    styleLabel = _enigma.eWindowStyle_ENUMS_styleLabel
    styleListboxSelected = _enigma.eWindowStyle_ENUMS_styleListboxSelected
    styleListboxNormal = _enigma.eWindowStyle_ENUMS_styleListboxNormal
    styleListboxMarked = _enigma.eWindowStyle_ENUMS_styleListboxMarked
    styleListboxMarkedAndSelected = _enigma.eWindowStyle_ENUMS_styleListboxMarkedAndSelected
    frameButton = _enigma.eWindowStyle_ENUMS_frameButton
    frameListboxEntry = _enigma.eWindowStyle_ENUMS_frameListboxEntry
    fontStatic = _enigma.eWindowStyle_ENUMS_fontStatic
    fontButton = _enigma.eWindowStyle_ENUMS_fontButton
    fontTitlebar = _enigma.eWindowStyle_ENUMS_fontTitlebar


eWindowStyle_swigregister = _enigma.eWindowStyle_ENUMS_swigregister
eWindowStyle_swigregister(eWindowStyle)

class eWindowStylePtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eWindowStylePtr_swiginit(self, _enigma.new_eWindowStylePtr(*args))

    __swig_destroy__ = _enigma.delete_eWindowStylePtr


eWindowStylePtr.__ref__ = new_instancemethod(_enigma.eWindowStylePtr___ref__, None, eWindowStylePtr)
eWindowStylePtr.getPtrString = new_instancemethod(_enigma.eWindowStylePtr_getPtrString, None, eWindowStylePtr)
eWindowStylePtr.__deref__ = new_instancemethod(_enigma.eWindowStylePtr___deref__, None, eWindowStylePtr)
eWindowStylePtr_swigregister = _enigma.eWindowStylePtr_swigregister
eWindowStylePtr_swigregister(eWindowStylePtr)

class eWindowStyleManager(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eWindowStyleManager_swiginit(self, _enigma.new_eWindowStyleManager(*args))

    __swig_destroy__ = _enigma.delete_eWindowStyleManager
    getInstance = staticmethod(_enigma.eWindowStyleManager_getInstance)


eWindowStyleManager.__ref__ = new_instancemethod(_enigma.eWindowStyleManager___ref__, None, eWindowStyleManager)
eWindowStyleManager.getPtrString = new_instancemethod(_enigma.eWindowStyleManager_getPtrString, None, eWindowStyleManager)
eWindowStyleManager.__deref__ = new_instancemethod(_enigma.eWindowStyleManager___deref__, None, eWindowStyleManager)
eWindowStyleManager.getStyle = new_instancemethod(_enigma.eWindowStyleManager_getStyle, None, eWindowStyleManager)
eWindowStyleManager.setStyle = new_instancemethod(_enigma.eWindowStyleManager_setStyle, None, eWindowStyleManager)
eWindowStyleManager_swigregister = _enigma.eWindowStyleManager_swigregister
eWindowStyleManager_swigregister(eWindowStyleManager)

def eWindowStyleManager_getInstance():
    return _enigma.eWindowStyleManager_getInstance()


eWindowStyleManager_getInstance = _enigma.eWindowStyleManager_getInstance

class eWindowStyleSkinned(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eWindowStyleSkinned_swiginit(self, _enigma.new_eWindowStyleSkinned())

    bsWindow = _enigma.eWindowStyleSkinned_bsWindow
    bsButton = _enigma.eWindowStyleSkinned_bsButton
    bsListboxEntry = _enigma.eWindowStyleSkinned_bsListboxEntry
    bpTopLeft = _enigma.eWindowStyleSkinned_bpTopLeft
    bpTop = _enigma.eWindowStyleSkinned_bpTop
    bpTopRight = _enigma.eWindowStyleSkinned_bpTopRight
    bpLeft = _enigma.eWindowStyleSkinned_bpLeft
    bpBackground = _enigma.eWindowStyleSkinned_bpBackground
    bpRight = _enigma.eWindowStyleSkinned_bpRight
    bpBottomLeft = _enigma.eWindowStyleSkinned_bpBottomLeft
    bpBottom = _enigma.eWindowStyleSkinned_bpBottom
    bpBottomRight = _enigma.eWindowStyleSkinned_bpBottomRight
    bpAll = _enigma.eWindowStyleSkinned_bpAll
    bpMax = _enigma.eWindowStyleSkinned_bpMax
    bpiTopLeft = _enigma.eWindowStyleSkinned_bpiTopLeft
    bpiTop = _enigma.eWindowStyleSkinned_bpiTop
    bpiTopRight = _enigma.eWindowStyleSkinned_bpiTopRight
    bpiLeft = _enigma.eWindowStyleSkinned_bpiLeft
    bpiBackground = _enigma.eWindowStyleSkinned_bpiBackground
    bpiRight = _enigma.eWindowStyleSkinned_bpiRight
    bpiBottomLeft = _enigma.eWindowStyleSkinned_bpiBottomLeft
    bpiBottom = _enigma.eWindowStyleSkinned_bpiBottom
    bpiBottomRight = _enigma.eWindowStyleSkinned_bpiBottomRight
    colBackground = _enigma.eWindowStyleSkinned_colBackground
    colLabelForeground = _enigma.eWindowStyleSkinned_colLabelForeground
    colListboxBackground = _enigma.eWindowStyleSkinned_colListboxBackground
    colListboxForeground = _enigma.eWindowStyleSkinned_colListboxForeground
    colListboxSelectedBackground = _enigma.eWindowStyleSkinned_colListboxSelectedBackground
    colListboxSelectedForeground = _enigma.eWindowStyleSkinned_colListboxSelectedForeground
    colListboxMarkedBackground = _enigma.eWindowStyleSkinned_colListboxMarkedBackground
    colListboxMarkedForeground = _enigma.eWindowStyleSkinned_colListboxMarkedForeground
    colListboxMarkedAndSelectedBackground = _enigma.eWindowStyleSkinned_colListboxMarkedAndSelectedBackground
    colListboxMarkedAndSelectedForeground = _enigma.eWindowStyleSkinned_colListboxMarkedAndSelectedForeground
    colWindowTitleForeground = _enigma.eWindowStyleSkinned_colWindowTitleForeground
    colWindowTitleBackground = _enigma.eWindowStyleSkinned_colWindowTitleBackground
    colMax = _enigma.eWindowStyleSkinned_colMax
    __swig_destroy__ = _enigma.delete_eWindowStyleSkinned


eWindowStyleSkinned.setStyle = new_instancemethod(_enigma.eWindowStyleSkinned_setStyle, None, eWindowStyleSkinned)
eWindowStyleSkinned.setPixmap = new_instancemethod(_enigma.eWindowStyleSkinned_setPixmap, None, eWindowStyleSkinned)
eWindowStyleSkinned.setColor = new_instancemethod(_enigma.eWindowStyleSkinned_setColor, None, eWindowStyleSkinned)
eWindowStyleSkinned.setTitleOffset = new_instancemethod(_enigma.eWindowStyleSkinned_setTitleOffset, None, eWindowStyleSkinned)
eWindowStyleSkinned.setTitleFont = new_instancemethod(_enigma.eWindowStyleSkinned_setTitleFont, None, eWindowStyleSkinned)
eWindowStyleSkinned_swigregister = _enigma.eWindowStyleSkinned_swigregister
eWindowStyleSkinned_swigregister(eWindowStyleSkinned)

class eWidgetAnimation(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eWidgetAnimation_swiginit(self, _enigma.new_eWidgetAnimation(*args))

    m_active = _swig_property(_enigma.eWidgetAnimation_m_active_get, _enigma.eWidgetAnimation_m_active_set)
    __swig_destroy__ = _enigma.delete_eWidgetAnimation


eWidgetAnimation.tick = new_instancemethod(_enigma.eWidgetAnimation_tick, None, eWidgetAnimation)
eWidgetAnimation.startMoveAnimation = new_instancemethod(_enigma.eWidgetAnimation_startMoveAnimation, None, eWidgetAnimation)
eWidgetAnimation_swigregister = _enigma.eWidgetAnimation_swigregister
eWidgetAnimation_swigregister(eWidgetAnimation)

class eVideoWidget(eLabel):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eVideoWidget_swiginit(self, _enigma.new_eVideoWidget(*args))

    __swig_destroy__ = _enigma.delete_eVideoWidget
    setFullsize = staticmethod(_enigma.eVideoWidget_setFullsize)


eVideoWidget.setDecoder = new_instancemethod(_enigma.eVideoWidget_setDecoder, None, eVideoWidget)
eVideoWidget.setFBSize = new_instancemethod(_enigma.eVideoWidget_setFBSize, None, eVideoWidget)
eVideoWidget.setAdjustPosition = new_instancemethod(_enigma.eVideoWidget_setAdjustPosition, None, eVideoWidget)
eVideoWidget.setOverscan = new_instancemethod(_enigma.eVideoWidget_setOverscan, None, eVideoWidget)
eVideoWidget_swigregister = _enigma.eVideoWidget_swigregister
eVideoWidget_swigregister(eVideoWidget)

def eVideoWidget_setFullsize(force_fullsize = False):
    return _enigma.eVideoWidget_setFullsize(force_fullsize)


eVideoWidget_setFullsize = _enigma.eVideoWidget_setFullsize
FONTSTYLE_NONE = _enigma.FONTSTYLE_NONE
FONTSTYLE_RAISED = _enigma.FONTSTYLE_RAISED
FONTSTYLE_DEPRESSED = _enigma.FONTSTYLE_DEPRESSED
FONTSTYLE_UNIFORM = _enigma.FONTSTYLE_UNIFORM

class ePangoSubtitlePageElement(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    m_color = _swig_property(_enigma.ePangoSubtitlePageElement_m_color_get, _enigma.ePangoSubtitlePageElement_m_color_set)
    m_have_color = _swig_property(_enigma.ePangoSubtitlePageElement_m_have_color_get, _enigma.ePangoSubtitlePageElement_m_have_color_set)
    m_pango_line = _swig_property(_enigma.ePangoSubtitlePageElement_m_pango_line_get, _enigma.ePangoSubtitlePageElement_m_pango_line_set)
    m_area = _swig_property(_enigma.ePangoSubtitlePageElement_m_area_get, _enigma.ePangoSubtitlePageElement_m_area_set)

    def __init__(self, *args):
        _enigma.ePangoSubtitlePageElement_swiginit(self, _enigma.new_ePangoSubtitlePageElement(*args))

    __swig_destroy__ = _enigma.delete_ePangoSubtitlePageElement


ePangoSubtitlePageElement_swigregister = _enigma.ePangoSubtitlePageElement_swigregister
ePangoSubtitlePageElement_swigregister(ePangoSubtitlePageElement)

class ePangoSubtitlePage(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    m_show_pts = _swig_property(_enigma.ePangoSubtitlePage_m_show_pts_get, _enigma.ePangoSubtitlePage_m_show_pts_set)
    m_timeout = _swig_property(_enigma.ePangoSubtitlePage_m_timeout_get, _enigma.ePangoSubtitlePage_m_timeout_set)
    m_elements = _swig_property(_enigma.ePangoSubtitlePage_m_elements_get, _enigma.ePangoSubtitlePage_m_elements_set)

    def __init__(self):
        _enigma.ePangoSubtitlePage_swiginit(self, _enigma.new_ePangoSubtitlePage())

    __swig_destroy__ = _enigma.delete_ePangoSubtitlePage


ePangoSubtitlePage.clear = new_instancemethod(_enigma.ePangoSubtitlePage_clear, None, ePangoSubtitlePage)
ePangoSubtitlePage_swigregister = _enigma.ePangoSubtitlePage_swigregister
ePangoSubtitlePage_swigregister(ePangoSubtitlePage)

class eVobSubtitlePage(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    m_show_pts = _swig_property(_enigma.eVobSubtitlePage_m_show_pts_get, _enigma.eVobSubtitlePage_m_show_pts_set)
    m_timeout = _swig_property(_enigma.eVobSubtitlePage_m_timeout_get, _enigma.eVobSubtitlePage_m_timeout_set)
    m_pixmap = _swig_property(_enigma.eVobSubtitlePage_m_pixmap_get, _enigma.eVobSubtitlePage_m_pixmap_set)

    def __init__(self):
        _enigma.eVobSubtitlePage_swiginit(self, _enigma.new_eVobSubtitlePage())

    __swig_destroy__ = _enigma.delete_eVobSubtitlePage


eVobSubtitlePage_swigregister = _enigma.eVobSubtitlePage_swigregister
eVobSubtitlePage_swigregister(eVobSubtitlePage)

class eSubtitleWidget(eWidget):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eSubtitleWidget_swiginit(self, _enigma.new_eSubtitleWidget(*args))

    Subtitle_TTX = _enigma.eSubtitleWidget_Subtitle_TTX
    Subtitle_Regular = _enigma.eSubtitleWidget_Subtitle_Regular
    Subtitle_Bold = _enigma.eSubtitleWidget_Subtitle_Bold
    Subtitle_Italic = _enigma.eSubtitleWidget_Subtitle_Italic
    Subtitle_MAX = _enigma.eSubtitleWidget_Subtitle_MAX
    setFontStyle = staticmethod(_enigma.eSubtitleWidget_setFontStyle)
    __swig_destroy__ = _enigma.delete_eSubtitleWidget


eSubtitleWidget.setPage = new_instancemethod(_enigma.eSubtitleWidget_setPage, None, eSubtitleWidget)
eSubtitleWidget.clearPage = new_instancemethod(_enigma.eSubtitleWidget_clearPage, None, eSubtitleWidget)
eSubtitleWidget.setPixmap = new_instancemethod(_enigma.eSubtitleWidget_setPixmap, None, eSubtitleWidget)
eSubtitleWidget.destroy = new_instancemethod(_enigma.eSubtitleWidget_destroy, None, eSubtitleWidget)
eSubtitleWidget_swigregister = _enigma.eSubtitleWidget_swigregister
eSubtitleWidget_swigregister(eSubtitleWidget)

def eSubtitleWidget_setFontStyle(*args):
    return _enigma.eSubtitleWidget_setFontStyle(*args)


eSubtitleWidget_setFontStyle = _enigma.eSubtitleWidget_setFontStyle

class iWallContent(iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined - class is abstract')

    __repr__ = _swig_repr
    __swig_destroy__ = _enigma.delete_iWallContent


iWallContent_swigregister = _enigma.iWallContent_swigregister
iWallContent_swigregister(iWallContent)

class eWall(eWidget):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eWall_swiginit(self, _enigma.new_eWall(*args))

    __swig_destroy__ = _enigma.delete_eWall
    selectionChanged = _swig_property(_enigma.eWall_selectionChanged_get)
    itemUpdated = _swig_property(_enigma.eWall_itemUpdated_get)
    moveUp = _enigma.eWall_moveUp
    moveDown = _enigma.eWall_moveDown
    moveLeft = _enigma.eWall_moveLeft
    moveRight = _enigma.eWall_moveRight
    nextPage = _enigma.eWall_nextPage
    prevPage = _enigma.eWall_prevPage
    justCheck = _enigma.eWall_justCheck
    MODE_WALL = _enigma.eWall_MODE_WALL
    MODE_LIST_HORIZONTAL = _enigma.eWall_MODE_LIST_HORIZONTAL
    MODE_LIST_VERTICAL = _enigma.eWall_MODE_LIST_VERTICAL
    SCROLLMODE_PAGE = _enigma.eWall_SCROLLMODE_PAGE
    SCROLLMODE_FLOW = _enigma.eWall_SCROLLMODE_FLOW
    BUILDMODE_SIZE = _enigma.eWall_BUILDMODE_SIZE
    BUILDMODE_GRID = _enigma.eWall_BUILDMODE_GRID
    ASPECT_DVD = _enigma.eWall_ASPECT_DVD
    ASPECT_CD = _enigma.eWall_ASPECT_CD
    ASPECT_SCREEN = _enigma.eWall_ASPECT_SCREEN
    ASPECT_BANNER = _enigma.eWall_ASPECT_BANNER
    POSITIONING_PIXEL = _enigma.eWall_POSITIONING_PIXEL
    POSITIONING_PERCENT = _enigma.eWall_POSITIONING_PERCENT


eWall.setWrapAround = new_instancemethod(_enigma.eWall_setWrapAround, None, eWall)
eWall.setContent = new_instancemethod(_enigma.eWall_setContent, None, eWall)
eWall.setPaintmode = new_instancemethod(_enigma.eWall_setPaintmode, None, eWall)
eWall.getCurrentIndex = new_instancemethod(_enigma.eWall_getCurrentIndex, None, eWall)
eWall.lock = new_instancemethod(_enigma.eWall_lock, None, eWall)
eWall.unlock = new_instancemethod(_enigma.eWall_unlock, None, eWall)
eWall.moveSelection = new_instancemethod(_enigma.eWall_moveSelection, None, eWall)
eWall.moveSelectionTo = new_instancemethod(_enigma.eWall_moveSelectionTo, None, eWall)
eWall.moveToEnd = new_instancemethod(_enigma.eWall_moveToEnd, None, eWall)
eWall.atBegin = new_instancemethod(_enigma.eWall_atBegin, None, eWall)
eWall.atEnd = new_instancemethod(_enigma.eWall_atEnd, None, eWall)
eWall.refresh = new_instancemethod(_enigma.eWall_refresh, None, eWall)
eWall.setBorderWidth = new_instancemethod(_enigma.eWall_setBorderWidth, None, eWall)
eWall.setBorderColor = new_instancemethod(_enigma.eWall_setBorderColor, None, eWall)
eWall.setItemHeight = new_instancemethod(_enigma.eWall_setItemHeight, None, eWall)
eWall.setItemWidth = new_instancemethod(_enigma.eWall_setItemWidth, None, eWall)
eWall.setItemScale = new_instancemethod(_enigma.eWall_setItemScale, None, eWall)
eWall.setItemScale_V = new_instancemethod(_enigma.eWall_setItemScale_V, None, eWall)
eWall.setItemScale_H = new_instancemethod(_enigma.eWall_setItemScale_H, None, eWall)
eWall.setItemSpace = new_instancemethod(_enigma.eWall_setItemSpace, None, eWall)
eWall.setShadow = new_instancemethod(_enigma.eWall_setShadow, None, eWall)
eWall.setOverlay = new_instancemethod(_enigma.eWall_setOverlay, None, eWall)
eWall.setColumnCount = new_instancemethod(_enigma.eWall_setColumnCount, None, eWall)
eWall.setRowCount = new_instancemethod(_enigma.eWall_setRowCount, None, eWall)
eWall.setViewMode = new_instancemethod(_enigma.eWall_setViewMode, None, eWall)
eWall.setScrollMode = new_instancemethod(_enigma.eWall_setScrollMode, None, eWall)
eWall.setBuildMode = new_instancemethod(_enigma.eWall_setBuildMode, None, eWall)
eWall.setPositioning = new_instancemethod(_enigma.eWall_setPositioning, None, eWall)
eWall.setAspectRatio = new_instancemethod(_enigma.eWall_setAspectRatio, None, eWall)
eWall.setAnimation = new_instancemethod(_enigma.eWall_setAnimation, None, eWall)
eWall.setSelectionEnable = new_instancemethod(_enigma.eWall_setSelectionEnable, None, eWall)
eWall.setTransparent = new_instancemethod(_enigma.eWall_setTransparent, None, eWall)
eWall.setGlobalBackgroundColor = new_instancemethod(_enigma.eWall_setGlobalBackgroundColor, None, eWall)
eWall.setBackgroundColor = new_instancemethod(_enigma.eWall_setBackgroundColor, None, eWall)
eWall.setBackgroundColorSelected = new_instancemethod(_enigma.eWall_setBackgroundColorSelected, None, eWall)
eWall.setForegroundColor = new_instancemethod(_enigma.eWall_setForegroundColor, None, eWall)
eWall.setForegroundColorSelected = new_instancemethod(_enigma.eWall_setForegroundColorSelected, None, eWall)
eWall.setBackgroundPicture = new_instancemethod(_enigma.eWall_setBackgroundPicture, None, eWall)
eWall.setSelectionPicture = new_instancemethod(_enigma.eWall_setSelectionPicture, None, eWall)
eWall.getCurrentPage = new_instancemethod(_enigma.eWall_getCurrentPage, None, eWall)
eWall.getPageCount = new_instancemethod(_enigma.eWall_getPageCount, None, eWall)
eWall.getPageItems = new_instancemethod(_enigma.eWall_getPageItems, None, eWall)
eWall.getItemsPerPage = new_instancemethod(_enigma.eWall_getItemsPerPage, None, eWall)
eWall.invalidate = new_instancemethod(_enigma.eWall_invalidate, None, eWall)
eWall_swigregister = _enigma.eWall_swigregister
eWall_swigregister(eWall)

class eOnlinePixmap(eWidget):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eOnlinePixmap_swiginit(self, _enigma.new_eOnlinePixmap(*args))

    __swig_destroy__ = _enigma.delete_eOnlinePixmap


eOnlinePixmap.setPixmap = new_instancemethod(_enigma.eOnlinePixmap_setPixmap, None, eOnlinePixmap)
eOnlinePixmap.setPixmapFromFile = new_instancemethod(_enigma.eOnlinePixmap_setPixmapFromFile, None, eOnlinePixmap)
eOnlinePixmap.setPixmapFromURL = new_instancemethod(_enigma.eOnlinePixmap_setPixmapFromURL, None, eOnlinePixmap)
eOnlinePixmap.setAlphatest = new_instancemethod(_enigma.eOnlinePixmap_setAlphatest, None, eOnlinePixmap)
eOnlinePixmap.setScale = new_instancemethod(_enigma.eOnlinePixmap_setScale, None, eOnlinePixmap)
eOnlinePixmap.setBorderWidth = new_instancemethod(_enigma.eOnlinePixmap_setBorderWidth, None, eOnlinePixmap)
eOnlinePixmap.setBorderColor = new_instancemethod(_enigma.eOnlinePixmap_setBorderColor, None, eOnlinePixmap)
eOnlinePixmap_swigregister = _enigma.eOnlinePixmap_swigregister
eOnlinePixmap_swigregister(eOnlinePixmap)

class eWallPythonStringContent(iWallContent, iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eWallPythonStringContent_swiginit(self, _enigma.new_eWallPythonStringContent())

    __swig_destroy__ = _enigma.delete_eWallPythonStringContent


eWallPythonStringContent.setWall = new_instancemethod(_enigma.eWallPythonStringContent_setWall, None, eWallPythonStringContent)
eWallPythonStringContent.getCurrentSelection = new_instancemethod(_enigma.eWallPythonStringContent_getCurrentSelection, None, eWallPythonStringContent)
eWallPythonStringContent.getCurrentSelectionIndex = new_instancemethod(_enigma.eWallPythonStringContent_getCurrentSelectionIndex, None, eWallPythonStringContent)
eWallPythonStringContent.invalidateEntry = new_instancemethod(_enigma.eWallPythonStringContent_invalidateEntry, None, eWallPythonStringContent)
eWallPythonStringContent.invalidate = new_instancemethod(_enigma.eWallPythonStringContent_invalidate, None, eWallPythonStringContent)
eWallPythonStringContent.getItemSize = new_instancemethod(_enigma.eWallPythonStringContent_getItemSize, None, eWallPythonStringContent)
eWallPythonStringContent.getSelItemSize = new_instancemethod(_enigma.eWallPythonStringContent_getSelItemSize, None, eWallPythonStringContent)
eWallPythonStringContent_swigregister = _enigma.eWallPythonStringContent_swigregister
eWallPythonStringContent_swigregister(eWallPythonStringContent)

class eWallPythonMultiContent(eWallPythonStringContent):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eWallPythonMultiContent_swiginit(self, _enigma.new_eWallPythonMultiContent())

    __swig_destroy__ = _enigma.delete_eWallPythonMultiContent
    TYPE_TEXT = _enigma.eWallPythonMultiContent_TYPE_TEXT
    TYPE_PROGRESS = _enigma.eWallPythonMultiContent_TYPE_PROGRESS
    TYPE_PIXMAP = _enigma.eWallPythonMultiContent_TYPE_PIXMAP
    TYPE_PIXMAP_ALPHATEST = _enigma.eWallPythonMultiContent_TYPE_PIXMAP_ALPHATEST
    TYPE_PIXMAP_ALPHABLEND = _enigma.eWallPythonMultiContent_TYPE_PIXMAP_ALPHABLEND
    TYPE_PROGRESS_PIXMAP = _enigma.eWallPythonMultiContent_TYPE_PROGRESS_PIXMAP
    TYPE_RECTANGLE = _enigma.eWallPythonMultiContent_TYPE_RECTANGLE
    TYPE_COVER = _enigma.eWallPythonMultiContent_TYPE_COVER
    TYPE_ONLINECOVER = _enigma.eWallPythonMultiContent_TYPE_ONLINECOVER
    SHOW_ALWAYS = _enigma.eWallPythonMultiContent_SHOW_ALWAYS
    SHOW_SELECTED = _enigma.eWallPythonMultiContent_SHOW_SELECTED
    SHOW_UNSELECTED = _enigma.eWallPythonMultiContent_SHOW_UNSELECTED
    MODE_WALL = _enigma.eWallPythonMultiContent_MODE_WALL
    MODE_LIST_HORIZONTAL = _enigma.eWallPythonMultiContent_MODE_LIST_HORIZONTAL
    MODE_LIST_VERTICAL = _enigma.eWallPythonMultiContent_MODE_LIST_VERTICAL
    ASPECT_DVD = _enigma.eWallPythonMultiContent_ASPECT_DVD
    ASPECT_CD = _enigma.eWallPythonMultiContent_ASPECT_CD
    ASPECT_SCREEN = _enigma.eWallPythonMultiContent_ASPECT_SCREEN
    ASPECT_BANNER = _enigma.eWallPythonMultiContent_ASPECT_BANNER
    POSITIONING_PIXEL = _enigma.eWallPythonMultiContent_POSITIONING_PIXEL
    POSITIONING_PERCENT = _enigma.eWallPythonMultiContent_POSITIONING_PERCENT
    SCROLLMODE_PAGE = _enigma.eWallPythonMultiContent_SCROLLMODE_PAGE
    SCROLLMODE_FLOW = _enigma.eWallPythonMultiContent_SCROLLMODE_FLOW
    BUILDMODE_SIZE = _enigma.eWallPythonMultiContent_BUILDMODE_SIZE
    BUILDMODE_GRID = _enigma.eWallPythonMultiContent_BUILDMODE_GRID


eWallPythonMultiContent.paint = new_instancemethod(_enigma.eWallPythonMultiContent_paint, None, eWallPythonMultiContent)
eWallPythonMultiContent.currentCursorSelectable = new_instancemethod(_enigma.eWallPythonMultiContent_currentCursorSelectable, None, eWallPythonMultiContent)
eWallPythonMultiContent.setWall = new_instancemethod(_enigma.eWallPythonMultiContent_setWall, None, eWallPythonMultiContent)
eWallPythonMultiContent.setFont = new_instancemethod(_enigma.eWallPythonMultiContent_setFont, None, eWallPythonMultiContent)
eWallPythonMultiContent.setBuildFunc = new_instancemethod(_enigma.eWallPythonMultiContent_setBuildFunc, None, eWallPythonMultiContent)
eWallPythonMultiContent.setSelectableFunc = new_instancemethod(_enigma.eWallPythonMultiContent_setSelectableFunc, None, eWallPythonMultiContent)
eWallPythonMultiContent.setDownloadPath = new_instancemethod(_enigma.eWallPythonMultiContent_setDownloadPath, None, eWallPythonMultiContent)
eWallPythonMultiContent.setItemHeight = new_instancemethod(_enigma.eWallPythonMultiContent_setItemHeight, None, eWallPythonMultiContent)
eWallPythonMultiContent.setItemWidth = new_instancemethod(_enigma.eWallPythonMultiContent_setItemWidth, None, eWallPythonMultiContent)
eWallPythonMultiContent.setItemScale = new_instancemethod(_enigma.eWallPythonMultiContent_setItemScale, None, eWallPythonMultiContent)
eWallPythonMultiContent.setItemScale_H = new_instancemethod(_enigma.eWallPythonMultiContent_setItemScale_H, None, eWallPythonMultiContent)
eWallPythonMultiContent.setItemScale_V = new_instancemethod(_enigma.eWallPythonMultiContent_setItemScale_V, None, eWallPythonMultiContent)
eWallPythonMultiContent.setItemSpace = new_instancemethod(_enigma.eWallPythonMultiContent_setItemSpace, None, eWallPythonMultiContent)
eWallPythonMultiContent.setAspectRatio = new_instancemethod(_enigma.eWallPythonMultiContent_setAspectRatio, None, eWallPythonMultiContent)
eWallPythonMultiContent.setPositioning = new_instancemethod(_enigma.eWallPythonMultiContent_setPositioning, None, eWallPythonMultiContent)
eWallPythonMultiContent.setColumnCount = new_instancemethod(_enigma.eWallPythonMultiContent_setColumnCount, None, eWallPythonMultiContent)
eWallPythonMultiContent.setFallbackImage = new_instancemethod(_enigma.eWallPythonMultiContent_setFallbackImage, None, eWallPythonMultiContent)
eWallPythonMultiContent.setRowCount = new_instancemethod(_enigma.eWallPythonMultiContent_setRowCount, None, eWallPythonMultiContent)
eWallPythonMultiContent.setShadow = new_instancemethod(_enigma.eWallPythonMultiContent_setShadow, None, eWallPythonMultiContent)
eWallPythonMultiContent.setOverlay = new_instancemethod(_enigma.eWallPythonMultiContent_setOverlay, None, eWallPythonMultiContent)
eWallPythonMultiContent.setViewMode = new_instancemethod(_enigma.eWallPythonMultiContent_setViewMode, None, eWallPythonMultiContent)
eWallPythonMultiContent.setScrollMode = new_instancemethod(_enigma.eWallPythonMultiContent_setScrollMode, None, eWallPythonMultiContent)
eWallPythonMultiContent.setGlobalBackgroundColor = new_instancemethod(_enigma.eWallPythonMultiContent_setGlobalBackgroundColor, None, eWallPythonMultiContent)
eWallPythonMultiContent.setSelectionClip = new_instancemethod(_enigma.eWallPythonMultiContent_setSelectionClip, None, eWallPythonMultiContent)
eWallPythonMultiContent.updateClip = new_instancemethod(_enigma.eWallPythonMultiContent_updateClip, None, eWallPythonMultiContent)
eWallPythonMultiContent.entryRemoved = new_instancemethod(_enigma.eWallPythonMultiContent_entryRemoved, None, eWallPythonMultiContent)
eWallPythonMultiContent.setTemplate = new_instancemethod(_enigma.eWallPythonMultiContent_setTemplate, None, eWallPythonMultiContent)
eWallPythonMultiContent_swigregister = _enigma.eWallPythonMultiContent_swigregister
eWallPythonMultiContent_swigregister(eWallPythonMultiContent)

class eListboxServiceContent(iListboxContent):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eListboxServiceContent_swiginit(self, _enigma.new_eListboxServiceContent())

    visModeSimple = _enigma.eListboxServiceContent_visModeSimple
    visModeComplex = _enigma.eListboxServiceContent_visModeComplex
    celServiceNumber = _enigma.eListboxServiceContent_celServiceNumber
    celMarkerPixmap = _enigma.eListboxServiceContent_celMarkerPixmap
    celFolderPixmap = _enigma.eListboxServiceContent_celFolderPixmap
    celPiconPixmap = _enigma.eListboxServiceContent_celPiconPixmap
    celPreViewPicPixmap = _enigma.eListboxServiceContent_celPreViewPicPixmap
    celRecordServicePixmap = _enigma.eListboxServiceContent_celRecordServicePixmap
    celAdIconPixmap = _enigma.eListboxServiceContent_celAdIconPixmap
    celServiceEventProgressbar = _enigma.eListboxServiceContent_celServiceEventProgressbar
    celServiceName = _enigma.eListboxServiceContent_celServiceName
    celServiceTime = _enigma.eListboxServiceContent_celServiceTime
    celServiceTypePixmap = _enigma.eListboxServiceContent_celServiceTypePixmap
    celServiceInfo = _enigma.eListboxServiceContent_celServiceInfo
    celNextEventInfo = _enigma.eListboxServiceContent_celNextEventInfo
    celElements = _enigma.eListboxServiceContent_celElements
    picDVB_S = _enigma.eListboxServiceContent_picDVB_S
    picDVB_T = _enigma.eListboxServiceContent_picDVB_T
    picDVB_C = _enigma.eListboxServiceContent_picDVB_C
    picServiceGroup = _enigma.eListboxServiceContent_picServiceGroup
    picFolder = _enigma.eListboxServiceContent_picFolder
    picMarker = _enigma.eListboxServiceContent_picMarker
    picPicon = _enigma.eListboxServiceContent_picPicon
    picPreViewPic = _enigma.eListboxServiceContent_picPreViewPic
    picRecordService = _enigma.eListboxServiceContent_picRecordService
    picServiceEventProgressbar = _enigma.eListboxServiceContent_picServiceEventProgressbar
    picAdvertismentService = _enigma.eListboxServiceContent_picAdvertismentService
    picElements = _enigma.eListboxServiceContent_picElements
    markedForeground = _enigma.eListboxServiceContent_markedForeground
    markedForegroundSelected = _enigma.eListboxServiceContent_markedForegroundSelected
    markedBackground = _enigma.eListboxServiceContent_markedBackground
    markedBackgroundSelected = _enigma.eListboxServiceContent_markedBackgroundSelected
    serviceNotAvail = _enigma.eListboxServiceContent_serviceNotAvail
    serviceEventProgressbarColor = _enigma.eListboxServiceContent_serviceEventProgressbarColor
    serviceEventProgressbarColorSelected = _enigma.eListboxServiceContent_serviceEventProgressbarColorSelected
    serviceEventProgressbarBorderColor = _enigma.eListboxServiceContent_serviceEventProgressbarBorderColor
    serviceEventProgressbarBorderColorSelected = _enigma.eListboxServiceContent_serviceEventProgressbarBorderColorSelected
    serviceDescriptionColor = _enigma.eListboxServiceContent_serviceDescriptionColor
    serviceDescriptionColorSelected = _enigma.eListboxServiceContent_serviceDescriptionColorSelected
    serviceRecordingColor = _enigma.eListboxServiceContent_serviceRecordingColor
    serviceAdvertismentColor = _enigma.eListboxServiceContent_serviceAdvertismentColor
    colorElements = _enigma.eListboxServiceContent_colorElements
    __swig_destroy__ = _enigma.delete_eListboxServiceContent


eListboxServiceContent.addService = new_instancemethod(_enigma.eListboxServiceContent_addService, None, eListboxServiceContent)
eListboxServiceContent.removeCurrent = new_instancemethod(_enigma.eListboxServiceContent_removeCurrent, None, eListboxServiceContent)
eListboxServiceContent.FillFinished = new_instancemethod(_enigma.eListboxServiceContent_FillFinished, None, eListboxServiceContent)
eListboxServiceContent.setIgnoreService = new_instancemethod(_enigma.eListboxServiceContent_setIgnoreService, None, eListboxServiceContent)
eListboxServiceContent.setPythonConfig = new_instancemethod(_enigma.eListboxServiceContent_setPythonConfig, None, eListboxServiceContent)
eListboxServiceContent.closeServiceList = new_instancemethod(_enigma.eListboxServiceContent_closeServiceList, None, eListboxServiceContent)
eListboxServiceContent.setRoot = new_instancemethod(_enigma.eListboxServiceContent_setRoot, None, eListboxServiceContent)
eListboxServiceContent.getCurrent = new_instancemethod(_enigma.eListboxServiceContent_getCurrent, None, eListboxServiceContent)
eListboxServiceContent.getPrev = new_instancemethod(_enigma.eListboxServiceContent_getPrev, None, eListboxServiceContent)
eListboxServiceContent.getNext = new_instancemethod(_enigma.eListboxServiceContent_getNext, None, eListboxServiceContent)
eListboxServiceContent.getList = new_instancemethod(_enigma.eListboxServiceContent_getList, None, eListboxServiceContent)
eListboxServiceContent.getNextBeginningWithChar = new_instancemethod(_enigma.eListboxServiceContent_getNextBeginningWithChar, None, eListboxServiceContent)
eListboxServiceContent.getPrevMarkerPos = new_instancemethod(_enigma.eListboxServiceContent_getPrevMarkerPos, None, eListboxServiceContent)
eListboxServiceContent.getNextMarkerPos = new_instancemethod(_enigma.eListboxServiceContent_getNextMarkerPos, None, eListboxServiceContent)
eListboxServiceContent.initMarked = new_instancemethod(_enigma.eListboxServiceContent_initMarked, None, eListboxServiceContent)
eListboxServiceContent.addMarked = new_instancemethod(_enigma.eListboxServiceContent_addMarked, None, eListboxServiceContent)
eListboxServiceContent.removeMarked = new_instancemethod(_enigma.eListboxServiceContent_removeMarked, None, eListboxServiceContent)
eListboxServiceContent.isMarked = new_instancemethod(_enigma.eListboxServiceContent_isMarked, None, eListboxServiceContent)
eListboxServiceContent.markedQueryStart = new_instancemethod(_enigma.eListboxServiceContent_markedQueryStart, None, eListboxServiceContent)
eListboxServiceContent.markedQueryNext = new_instancemethod(_enigma.eListboxServiceContent_markedQueryNext, None, eListboxServiceContent)
eListboxServiceContent.lookupService = new_instancemethod(_enigma.eListboxServiceContent_lookupService, None, eListboxServiceContent)
eListboxServiceContent.setCurrent = new_instancemethod(_enigma.eListboxServiceContent_setCurrent, None, eListboxServiceContent)
eListboxServiceContent.setPiconFunction = new_instancemethod(_enigma.eListboxServiceContent_setPiconFunction, None, eListboxServiceContent)
eListboxServiceContent.setPreViewPicFunction = new_instancemethod(_enigma.eListboxServiceContent_setPreViewPicFunction, None, eListboxServiceContent)
eListboxServiceContent.setTextXOffsetForIcon = new_instancemethod(_enigma.eListboxServiceContent_setTextXOffsetForIcon, None, eListboxServiceContent)
eListboxServiceContent.setProgressbarHeight = new_instancemethod(_enigma.eListboxServiceContent_setProgressbarHeight, None, eListboxServiceContent)
eListboxServiceContent.setProgressbarBorderWidth = new_instancemethod(_enigma.eListboxServiceContent_setProgressbarBorderWidth, None, eListboxServiceContent)
eListboxServiceContent.setPiconHeight = new_instancemethod(_enigma.eListboxServiceContent_setPiconHeight, None, eListboxServiceContent)
eListboxServiceContent.setPiconWidth = new_instancemethod(_enigma.eListboxServiceContent_setPiconWidth, None, eListboxServiceContent)
eListboxServiceContent.setPreViewPicHeight = new_instancemethod(_enigma.eListboxServiceContent_setPreViewPicHeight, None, eListboxServiceContent)
eListboxServiceContent.setPreViewPicWidth = new_instancemethod(_enigma.eListboxServiceContent_setPreViewPicWidth, None, eListboxServiceContent)
eListboxServiceContent.setVisualMode = new_instancemethod(_enigma.eListboxServiceContent_setVisualMode, None, eListboxServiceContent)
eListboxServiceContent.setAlternativeMode = new_instancemethod(_enigma.eListboxServiceContent_setAlternativeMode, None, eListboxServiceContent)
eListboxServiceContent.setSelectionOffset = new_instancemethod(_enigma.eListboxServiceContent_setSelectionOffset, None, eListboxServiceContent)
eListboxServiceContent.setElementPosition = new_instancemethod(_enigma.eListboxServiceContent_setElementPosition, None, eListboxServiceContent)
eListboxServiceContent.setElementFont = new_instancemethod(_enigma.eListboxServiceContent_setElementFont, None, eListboxServiceContent)
eListboxServiceContent.setPixmap = new_instancemethod(_enigma.eListboxServiceContent_setPixmap, None, eListboxServiceContent)
eListboxServiceContent.setElementAlignment = new_instancemethod(_enigma.eListboxServiceContent_setElementAlignment, None, eListboxServiceContent)
eListboxServiceContent.sort = new_instancemethod(_enigma.eListboxServiceContent_sort, None, eListboxServiceContent)
eListboxServiceContent.setCurrentMarked = new_instancemethod(_enigma.eListboxServiceContent_setCurrentMarked, None, eListboxServiceContent)
eListboxServiceContent.setNumberOffset = new_instancemethod(_enigma.eListboxServiceContent_setNumberOffset, None, eListboxServiceContent)
eListboxServiceContent.getItemHeight = new_instancemethod(_enigma.eListboxServiceContent_getItemHeight, None, eListboxServiceContent)
eListboxServiceContent.setItemHeight = new_instancemethod(_enigma.eListboxServiceContent_setItemHeight, None, eListboxServiceContent)
eListboxServiceContent.setColor = new_instancemethod(_enigma.eListboxServiceContent_setColor, None, eListboxServiceContent)
eListboxServiceContent.setSelectionEnable = new_instancemethod(_enigma.eListboxServiceContent_setSelectionEnable, None, eListboxServiceContent)
eListboxServiceContent_swigregister = _enigma.eListboxServiceContent_swigregister
eListboxServiceContent_swigregister(eListboxServiceContent)

class pNavigation(iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    m_event = _swig_property(_enigma.pNavigation_m_event_get)
    m_record_event = _swig_property(_enigma.pNavigation_m_record_event_get)

    def __init__(self):
        _enigma.pNavigation_swiginit(self, _enigma.new_pNavigation())

    __swig_destroy__ = _enigma.delete_pNavigation


pNavigation.playService = new_instancemethod(_enigma.pNavigation_playService, None, pNavigation)
pNavigation.stopService = new_instancemethod(_enigma.pNavigation_stopService, None, pNavigation)
pNavigation.pause = new_instancemethod(_enigma.pNavigation_pause, None, pNavigation)
pNavigation.getCurrentService = new_instancemethod(_enigma.pNavigation_getCurrentService, None, pNavigation)
pNavigation.recordService = new_instancemethod(_enigma.pNavigation_recordService, None, pNavigation)
pNavigation.stopRecordService = new_instancemethod(_enigma.pNavigation_stopRecordService, None, pNavigation)
pNavigation.getRecordings = new_instancemethod(_enigma.pNavigation_getRecordings, None, pNavigation)
pNavigation_swigregister = _enigma.pNavigation_swigregister
pNavigation_swigregister(pNavigation)

class eActionMap(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eActionMap_swiginit(self, _enigma.new_eActionMap(*args))

    __swig_destroy__ = _enigma.delete_eActionMap
    getInstance = staticmethod(_enigma.eActionMap_getInstance)


eActionMap.__ref__ = new_instancemethod(_enigma.eActionMap___ref__, None, eActionMap)
eActionMap.getPtrString = new_instancemethod(_enigma.eActionMap_getPtrString, None, eActionMap)
eActionMap.__deref__ = new_instancemethod(_enigma.eActionMap___deref__, None, eActionMap)
eActionMap.bindAction = new_instancemethod(_enigma.eActionMap_bindAction, None, eActionMap)
eActionMap.unbindAction = new_instancemethod(_enigma.eActionMap_unbindAction, None, eActionMap)
eActionMap.bindKey = new_instancemethod(_enigma.eActionMap_bindKey, None, eActionMap)
eActionMap.unbindKeyDomain = new_instancemethod(_enigma.eActionMap_unbindKeyDomain, None, eActionMap)
eActionMap.keyPressed = new_instancemethod(_enigma.eActionMap_keyPressed, None, eActionMap)
eActionMap_swigregister = _enigma.eActionMap_swigregister
eActionMap_swigregister(eActionMap)

def eActionMap_getInstance():
    return _enigma.eActionMap_getInstance()


eActionMap_getInstance = _enigma.eActionMap_getInstance

class gFont(iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    family = _swig_property(_enigma.gFont_family_get, _enigma.gFont_family_set)
    pointSize = _swig_property(_enigma.gFont_pointSize_get, _enigma.gFont_pointSize_set)
    __swig_destroy__ = _enigma.delete_gFont

    def __init__(self, *args):
        _enigma.gFont_swiginit(self, _enigma.new_gFont(*args))


gFont_swigregister = _enigma.gFont_swigregister
gFont_swigregister(gFont)

def loadPNG(*args):
    return _enigma.loadPNG(*args)


loadPNG = _enigma.loadPNG

def loadJPG(*args):
    return _enigma.loadJPG(*args)


loadJPG = _enigma.loadJPG

def savePNG(*args):
    return _enigma.savePNG(*args)


savePNG = _enigma.savePNG

class eDVBVolumecontrol(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.eDVBVolumecontrol_getInstance)


eDVBVolumecontrol.volumeUp = new_instancemethod(_enigma.eDVBVolumecontrol_volumeUp, None, eDVBVolumecontrol)
eDVBVolumecontrol.volumeDown = new_instancemethod(_enigma.eDVBVolumecontrol_volumeDown, None, eDVBVolumecontrol)
eDVBVolumecontrol.setVolume = new_instancemethod(_enigma.eDVBVolumecontrol_setVolume, None, eDVBVolumecontrol)
eDVBVolumecontrol.volumeMute = new_instancemethod(_enigma.eDVBVolumecontrol_volumeMute, None, eDVBVolumecontrol)
eDVBVolumecontrol.volumeUnMute = new_instancemethod(_enigma.eDVBVolumecontrol_volumeUnMute, None, eDVBVolumecontrol)
eDVBVolumecontrol.volumeToggleMute = new_instancemethod(_enigma.eDVBVolumecontrol_volumeToggleMute, None, eDVBVolumecontrol)
eDVBVolumecontrol.getVolume = new_instancemethod(_enigma.eDVBVolumecontrol_getVolume, None, eDVBVolumecontrol)
eDVBVolumecontrol.isMuted = new_instancemethod(_enigma.eDVBVolumecontrol_isMuted, None, eDVBVolumecontrol)
eDVBVolumecontrol_swigregister = _enigma.eDVBVolumecontrol_swigregister
eDVBVolumecontrol_swigregister(eDVBVolumecontrol)

def eDVBVolumecontrol_getInstance():
    return _enigma.eDVBVolumecontrol_getInstance()


eDVBVolumecontrol_getInstance = _enigma.eDVBVolumecontrol_getInstance

class eDVBSatelliteDiseqcParameters(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    AA = _enigma.eDVBSatelliteDiseqcParameters_AA
    AB = _enigma.eDVBSatelliteDiseqcParameters_AB
    BA = _enigma.eDVBSatelliteDiseqcParameters_BA
    BB = _enigma.eDVBSatelliteDiseqcParameters_BB
    SENDNO = _enigma.eDVBSatelliteDiseqcParameters_SENDNO
    NONE = _enigma.eDVBSatelliteDiseqcParameters_NONE
    V1_0 = _enigma.eDVBSatelliteDiseqcParameters_V1_0
    V1_1 = _enigma.eDVBSatelliteDiseqcParameters_V1_1
    V1_2 = _enigma.eDVBSatelliteDiseqcParameters_V1_2
    SMATV = _enigma.eDVBSatelliteDiseqcParameters_SMATV
    NO = _enigma.eDVBSatelliteDiseqcParameters_NO
    A = _enigma.eDVBSatelliteDiseqcParameters_A
    B = _enigma.eDVBSatelliteDiseqcParameters_B


eDVBSatelliteDiseqcParameters_swigregister = _enigma.eDVBSatelliteDiseqcParameters_swigregister
eDVBSatelliteDiseqcParameters_swigregister(eDVBSatelliteDiseqcParameters)

class eDVBSatelliteSwitchParameters(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    HILO = _enigma.eDVBSatelliteSwitchParameters_HILO
    ON = _enigma.eDVBSatelliteSwitchParameters_ON
    OFF = _enigma.eDVBSatelliteSwitchParameters_OFF
    HV = _enigma.eDVBSatelliteSwitchParameters_HV
    _14V = _enigma.eDVBSatelliteSwitchParameters__14V
    _18V = _enigma.eDVBSatelliteSwitchParameters__18V
    _0V = _enigma.eDVBSatelliteSwitchParameters__0V
    HV_13 = _enigma.eDVBSatelliteSwitchParameters_HV_13


eDVBSatelliteSwitchParameters_swigregister = _enigma.eDVBSatelliteSwitchParameters_swigregister
eDVBSatelliteSwitchParameters_swigregister(eDVBSatelliteSwitchParameters)

class eDVBSatelliteRotorParameters(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    NORTH = _enigma.eDVBSatelliteRotorParameters_NORTH
    SOUTH = _enigma.eDVBSatelliteRotorParameters_SOUTH
    EAST = _enigma.eDVBSatelliteRotorParameters_EAST
    WEST = _enigma.eDVBSatelliteRotorParameters_WEST
    FAST = _enigma.eDVBSatelliteRotorParameters_FAST
    SLOW = _enigma.eDVBSatelliteRotorParameters_SLOW


eDVBSatelliteRotorParameters_swigregister = _enigma.eDVBSatelliteRotorParameters_swigregister
eDVBSatelliteRotorParameters_swigregister(eDVBSatelliteRotorParameters)

class eDVBSatelliteLNBParameters(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    OFF = _enigma.eDVBSatelliteLNBParameters_OFF
    ON = _enigma.eDVBSatelliteLNBParameters_ON
    SatCR_positions = _swig_property(_enigma.eDVBSatelliteLNBParameters_SatCR_positions_get, _enigma.eDVBSatelliteLNBParameters_SatCR_positions_set)
    SatCR_idx = _swig_property(_enigma.eDVBSatelliteLNBParameters_SatCR_idx_get, _enigma.eDVBSatelliteLNBParameters_SatCR_idx_set)
    SatCR_format = _swig_property(_enigma.eDVBSatelliteLNBParameters_SatCR_format_get, _enigma.eDVBSatelliteLNBParameters_SatCR_format_set)
    SatCRvco = _swig_property(_enigma.eDVBSatelliteLNBParameters_SatCRvco_get, _enigma.eDVBSatelliteLNBParameters_SatCRvco_set)
    UnicableTuningWord = _swig_property(_enigma.eDVBSatelliteLNBParameters_UnicableTuningWord_get, _enigma.eDVBSatelliteLNBParameters_UnicableTuningWord_set)
    UnicableConfigWord = _swig_property(_enigma.eDVBSatelliteLNBParameters_UnicableConfigWord_get, _enigma.eDVBSatelliteLNBParameters_UnicableConfigWord_set)
    old_frequency = _swig_property(_enigma.eDVBSatelliteLNBParameters_old_frequency_get, _enigma.eDVBSatelliteLNBParameters_old_frequency_set)
    old_polarisation = _swig_property(_enigma.eDVBSatelliteLNBParameters_old_polarisation_get, _enigma.eDVBSatelliteLNBParameters_old_polarisation_set)
    old_orbital_position = _swig_property(_enigma.eDVBSatelliteLNBParameters_old_orbital_position_get, _enigma.eDVBSatelliteLNBParameters_old_orbital_position_set)
    guard_offset_old = _swig_property(_enigma.eDVBSatelliteLNBParameters_guard_offset_old_get, _enigma.eDVBSatelliteLNBParameters_guard_offset_old_set)
    guard_offset = _swig_property(_enigma.eDVBSatelliteLNBParameters_guard_offset_get, _enigma.eDVBSatelliteLNBParameters_guard_offset_set)
    LNBNum = _swig_property(_enigma.eDVBSatelliteLNBParameters_LNBNum_get, _enigma.eDVBSatelliteLNBParameters_LNBNum_set)


eDVBSatelliteLNBParameters_swigregister = _enigma.eDVBSatelliteLNBParameters_swigregister
eDVBSatelliteLNBParameters_swigregister(eDVBSatelliteLNBParameters)
guard_offset_min = _enigma.guard_offset_min
guard_offset_max = _enigma.guard_offset_max
guard_offset_step = _enigma.guard_offset_step
MAX_SATCR = _enigma.MAX_SATCR
MAX_LNBNUM = _enigma.MAX_LNBNUM

class eDVBSatelliteEquipmentControl(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    DELAY_AFTER_CONT_TONE_DISABLE_BEFORE_DISEQC = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_CONT_TONE_DISABLE_BEFORE_DISEQC
    DELAY_AFTER_FINAL_CONT_TONE_CHANGE = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_FINAL_CONT_TONE_CHANGE
    DELAY_AFTER_FINAL_VOLTAGE_CHANGE = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_FINAL_VOLTAGE_CHANGE
    DELAY_BETWEEN_DISEQC_REPEATS = _enigma.eDVBSatelliteEquipmentControl_DELAY_BETWEEN_DISEQC_REPEATS
    DELAY_AFTER_LAST_DISEQC_CMD = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_LAST_DISEQC_CMD
    DELAY_AFTER_TONEBURST = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_TONEBURST
    DELAY_AFTER_ENABLE_VOLTAGE_BEFORE_SWITCH_CMDS = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_ENABLE_VOLTAGE_BEFORE_SWITCH_CMDS
    DELAY_BETWEEN_SWITCH_AND_MOTOR_CMD = _enigma.eDVBSatelliteEquipmentControl_DELAY_BETWEEN_SWITCH_AND_MOTOR_CMD
    DELAY_AFTER_VOLTAGE_CHANGE_BEFORE_MEASURE_IDLE_INPUTPOWER = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_VOLTAGE_CHANGE_BEFORE_MEASURE_IDLE_INPUTPOWER
    DELAY_AFTER_ENABLE_VOLTAGE_BEFORE_MOTOR_CMD = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_ENABLE_VOLTAGE_BEFORE_MOTOR_CMD
    DELAY_AFTER_MOTOR_STOP_CMD = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_MOTOR_STOP_CMD
    DELAY_AFTER_VOLTAGE_CHANGE_BEFORE_MOTOR_CMD = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_VOLTAGE_CHANGE_BEFORE_MOTOR_CMD
    DELAY_BEFORE_SEQUENCE_REPEAT = _enigma.eDVBSatelliteEquipmentControl_DELAY_BEFORE_SEQUENCE_REPEAT
    MOTOR_COMMAND_RETRIES = _enigma.eDVBSatelliteEquipmentControl_MOTOR_COMMAND_RETRIES
    MOTOR_RUNNING_TIMEOUT = _enigma.eDVBSatelliteEquipmentControl_MOTOR_RUNNING_TIMEOUT
    DELAY_AFTER_VOLTAGE_CHANGE_BEFORE_SWITCH_CMDS = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_VOLTAGE_CHANGE_BEFORE_SWITCH_CMDS
    DELAY_AFTER_DISEQC_RESET_CMD = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_DISEQC_RESET_CMD
    DELAY_AFTER_DISEQC_PERIPHERIAL_POWERON_CMD = _enigma.eDVBSatelliteEquipmentControl_DELAY_AFTER_DISEQC_PERIPHERIAL_POWERON_CMD
    MAX_PARAMS = _enigma.eDVBSatelliteEquipmentControl_MAX_PARAMS
    getInstance = staticmethod(_enigma.eDVBSatelliteEquipmentControl_getInstance)
    setParam = staticmethod(_enigma.eDVBSatelliteEquipmentControl_setParam)


eDVBSatelliteEquipmentControl.clear = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_clear, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.addLNB = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_addLNB, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLNBSlotMask = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLNBSlotMask, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLNBLOFL = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLNBLOFL, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLNBLOFH = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLNBLOFH, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLNBThreshold = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLNBThreshold, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLNBIncreasedVoltage = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLNBIncreasedVoltage, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLNBPrio = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLNBPrio, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLNBNum = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLNBNum, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setDiSEqCMode = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setDiSEqCMode, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setToneburst = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setToneburst, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setRepeats = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setRepeats, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setCommittedCommand = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setCommittedCommand, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setUncommittedCommand = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setUncommittedCommand, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setCommandOrder = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setCommandOrder, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setFastDiSEqC = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setFastDiSEqC, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setSeqRepeat = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setSeqRepeat, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLongitude = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLongitude, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLatitude = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLatitude, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLoDirection = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLoDirection, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLaDirection = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLaDirection, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setUseInputpower = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setUseInputpower, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setInputpowerDelta = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setInputpowerDelta, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setRotorTurningSpeed = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setRotorTurningSpeed, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLNBSatCRformat = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLNBSatCRformat, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLNBSatCR = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLNBSatCR, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLNBSatCRvco = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLNBSatCRvco, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setLNBSatCRpositions = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setLNBSatCRpositions, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.getLNBSatCRformat = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_getLNBSatCRformat, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.getLNBSatCR = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_getLNBSatCR, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.getLNBSatCRvco = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_getLNBSatCRvco, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.getLNBSatCRpositions = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_getLNBSatCRpositions, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.addSatellite = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_addSatellite, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setVoltageMode = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setVoltageMode, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setToneMode = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setToneMode, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setRotorPosNum = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setRotorPosNum, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setTunerLinked = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setTunerLinked, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setTunerDepends = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setTunerDepends, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setSlotNotLinked = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setSlotNotLinked, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.setRotorMoving = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_setRotorMoving, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.isRotorMoving = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_isRotorMoving, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.canMeasureInputPower = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_canMeasureInputPower, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl.isOrbitalPositionConfigured = new_instancemethod(_enigma.eDVBSatelliteEquipmentControl_isOrbitalPositionConfigured, None, eDVBSatelliteEquipmentControl)
eDVBSatelliteEquipmentControl_swigregister = _enigma.eDVBSatelliteEquipmentControl_swigregister
eDVBSatelliteEquipmentControl_swigregister(eDVBSatelliteEquipmentControl)

def eDVBSatelliteEquipmentControl_getInstance():
    return _enigma.eDVBSatelliteEquipmentControl_getInstance()


eDVBSatelliteEquipmentControl_getInstance = _enigma.eDVBSatelliteEquipmentControl_getInstance

def eDVBSatelliteEquipmentControl_setParam(*args):
    return _enigma.eDVBSatelliteEquipmentControl_setParam(*args)


eDVBSatelliteEquipmentControl_setParam = _enigma.eDVBSatelliteEquipmentControl_setParam
ENABLE_PRIVATE_EPG = _enigma.ENABLE_PRIVATE_EPG
ENABLE_MHW_EPG = _enigma.ENABLE_MHW_EPG
ENABLE_FREESAT = _enigma.ENABLE_FREESAT
ENABLE_NETMED = _enigma.ENABLE_NETMED
ENABLE_VIRGIN = _enigma.ENABLE_VIRGIN

class freesatEITSubtableStatus(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.freesatEITSubtableStatus_swiginit(self, _enigma.new_freesatEITSubtableStatus(*args))

    __swig_destroy__ = _enigma.delete_freesatEITSubtableStatus


freesatEITSubtableStatus.isSectionPresent = new_instancemethod(_enigma.freesatEITSubtableStatus_isSectionPresent, None, freesatEITSubtableStatus)
freesatEITSubtableStatus.seen = new_instancemethod(_enigma.freesatEITSubtableStatus_seen, None, freesatEITSubtableStatus)
freesatEITSubtableStatus.isVersionChanged = new_instancemethod(_enigma.freesatEITSubtableStatus_isVersionChanged, None, freesatEITSubtableStatus)
freesatEITSubtableStatus.updateVersion = new_instancemethod(_enigma.freesatEITSubtableStatus_updateVersion, None, freesatEITSubtableStatus)
freesatEITSubtableStatus.isCompleted = new_instancemethod(_enigma.freesatEITSubtableStatus_isCompleted, None, freesatEITSubtableStatus)
freesatEITSubtableStatus_swigregister = _enigma.freesatEITSubtableStatus_swigregister
freesatEITSubtableStatus_swigregister(freesatEITSubtableStatus)

class eEPGCache(eMainloop):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.eEPGCache_getInstance)
    m_filename = _swig_property(_enigma.eEPGCache_m_filename_get, _enigma.eEPGCache_m_filename_set)
    m_epgstbmode = _swig_property(_enigma.eEPGCache_m_epgstbmode_get, _enigma.eEPGCache_m_epgstbmode_set)
    m_initialized = _swig_property(_enigma.eEPGCache_m_initialized_get, _enigma.eEPGCache_m_initialized_set)
    m_only_blacklist_dvb_epg = _swig_property(_enigma.eEPGCache_m_only_blacklist_dvb_epg_get, _enigma.eEPGCache_m_only_blacklist_dvb_epg_set)
    m_dvb_epg_blacklist = _swig_property(_enigma.eEPGCache_m_dvb_epg_blacklist_get, _enigma.eEPGCache_m_dvb_epg_blacklist_set)
    SIMILAR_BROADCASTINGS_SEARCH = _enigma.eEPGCache_SIMILAR_BROADCASTINGS_SEARCH
    EXAKT_TITLE_SEARCH = _enigma.eEPGCache_EXAKT_TITLE_SEARCH
    PARTIAL_TITLE_SEARCH = _enigma.eEPGCache_PARTIAL_TITLE_SEARCH
    SHORT_DESCRIPTION_SEARCH = _enigma.eEPGCache_SHORT_DESCRIPTION_SEARCH
    TITLE_SHORT_DESCRIPTION_SEARCH = _enigma.eEPGCache_TITLE_SHORT_DESCRIPTION_SEARCH
    EXTENDED_DESCRIPTION_SEARCH = _enigma.eEPGCache_EXTENDED_DESCRIPTION_SEARCH
    FULL_DESCRIPTION_SEARCH = _enigma.eEPGCache_FULL_DESCRIPTION_SEARCH
    START_TITLE_SEARCH = _enigma.eEPGCache_START_TITLE_SEARCH
    CASE_CHECK = _enigma.eEPGCache_CASE_CHECK
    NO_CASE_CHECK = _enigma.eEPGCache_NO_CASE_CHECK
    PRIVATE = _enigma.eEPGCache_PRIVATE
    NOWNEXT = _enigma.eEPGCache_NOWNEXT
    SCHEDULE = _enigma.eEPGCache_SCHEDULE
    SCHEDULE_OTHER = _enigma.eEPGCache_SCHEDULE_OTHER
    MHW = _enigma.eEPGCache_MHW
    FREESAT_NOWNEXT = _enigma.eEPGCache_FREESAT_NOWNEXT
    FREESAT_SCHEDULE = _enigma.eEPGCache_FREESAT_SCHEDULE
    FREESAT_SCHEDULE_OTHER = _enigma.eEPGCache_FREESAT_SCHEDULE_OTHER
    VIASAT = _enigma.eEPGCache_VIASAT
    NETMED_SCHEDULE = _enigma.eEPGCache_NETMED_SCHEDULE
    NETMED_SCHEDULE_OTHER = _enigma.eEPGCache_NETMED_SCHEDULE_OTHER
    VIRGIN_NOWNEXT = _enigma.eEPGCache_VIRGIN_NOWNEXT
    VIRGIN_SCHEDULE = _enigma.eEPGCache_VIRGIN_SCHEDULE
    PRIVATE_UPDATE = _enigma.eEPGCache_PRIVATE_UPDATE
    EPG_IMPORT = _enigma.eEPGCache_EPG_IMPORT


eEPGCache.save = new_instancemethod(_enigma.eEPGCache_save, None, eEPGCache)
eEPGCache.load = new_instancemethod(_enigma.eEPGCache_load, None, eEPGCache)
eEPGCache.timeUpdated = new_instancemethod(_enigma.eEPGCache_timeUpdated, None, eEPGCache)
eEPGCache.clearDB = new_instancemethod(_enigma.eEPGCache_clearDB, None, eEPGCache)
eEPGCache.clearServiceEPG = new_instancemethod(_enigma.eEPGCache_clearServiceEPG, None, eEPGCache)
eEPGCache.reloadBlacklistDVBEPG = new_instancemethod(_enigma.eEPGCache_reloadBlacklistDVBEPG, None, eEPGCache)
eEPGCache.crossepgImportEPGv21 = new_instancemethod(_enigma.eEPGCache_crossepgImportEPGv21, None, eEPGCache)
eEPGCache.setCacheFile = new_instancemethod(_enigma.eEPGCache_setCacheFile, None, eEPGCache)
eEPGCache.setEpgStbMode = new_instancemethod(_enigma.eEPGCache_setEpgStbMode, None, eEPGCache)
eEPGCache.setDVBEPGBlackListMode = new_instancemethod(_enigma.eEPGCache_setDVBEPGBlackListMode, None, eEPGCache)
eEPGCache.setEPGBuffer = new_instancemethod(_enigma.eEPGCache_setEPGBuffer, None, eEPGCache)
eEPGCache.Lock = new_instancemethod(_enigma.eEPGCache_Lock, None, eEPGCache)
eEPGCache.Unlock = new_instancemethod(_enigma.eEPGCache_Unlock, None, eEPGCache)
eEPGCache.startTimeQuery = new_instancemethod(_enigma.eEPGCache_startTimeQuery, None, eEPGCache)
eEPGCache.lookupEvent = new_instancemethod(_enigma.eEPGCache_lookupEvent, None, eEPGCache)
eEPGCache.search = new_instancemethod(_enigma.eEPGCache_search, None, eEPGCache)
eEPGCache.lookupEventId = new_instancemethod(_enigma.eEPGCache_lookupEventId, None, eEPGCache)
eEPGCache.lookupEventTime = new_instancemethod(_enigma.eEPGCache_lookupEventTime, None, eEPGCache)
eEPGCache.getNextTimeEntry = new_instancemethod(_enigma.eEPGCache_getNextTimeEntry, None, eEPGCache)
eEPGCache.setEpgHistorySeconds = new_instancemethod(_enigma.eEPGCache_setEpgHistorySeconds, None, eEPGCache)
eEPGCache.setEpgSources = new_instancemethod(_enigma.eEPGCache_setEpgSources, None, eEPGCache)
eEPGCache.getEpgSources = new_instancemethod(_enigma.eEPGCache_getEpgSources, None, eEPGCache)
eEPGCache.submitEventData = new_instancemethod(_enigma.eEPGCache_submitEventData, None, eEPGCache)
eEPGCache.importEvents = new_instancemethod(_enigma.eEPGCache_importEvents, None, eEPGCache)
eEPGCache.importEvent = new_instancemethod(_enigma.eEPGCache_importEvent, None, eEPGCache)
eEPGCache.importEventwithID = new_instancemethod(_enigma.eEPGCache_importEventwithID, None, eEPGCache)
eEPGCache.importEventswithID = new_instancemethod(_enigma.eEPGCache_importEventswithID, None, eEPGCache)
eEPGCache.importLockedEventwithID = new_instancemethod(_enigma.eEPGCache_importLockedEventwithID, None, eEPGCache)
eEPGCache.importLockedEventswithID = new_instancemethod(_enigma.eEPGCache_importLockedEventswithID, None, eEPGCache)
eEPGCache.updateEvents = new_instancemethod(_enigma.eEPGCache_updateEvents, None, eEPGCache)
eEPGCache.updateEvent = new_instancemethod(_enigma.eEPGCache_updateEvent, None, eEPGCache)
eEPGCache.prependEventsData = new_instancemethod(_enigma.eEPGCache_prependEventsData, None, eEPGCache)
eEPGCache.prependEventData = new_instancemethod(_enigma.eEPGCache_prependEventData, None, eEPGCache)
eEPGCache.appendEventsData = new_instancemethod(_enigma.eEPGCache_appendEventsData, None, eEPGCache)
eEPGCache.appendEventData = new_instancemethod(_enigma.eEPGCache_appendEventData, None, eEPGCache)
eEPGCache_swigregister = _enigma.eEPGCache_swigregister
eEPGCache_swigregister(eEPGCache)

def eEPGCache_getInstance():
    return _enigma.eEPGCache_getInstance()


eEPGCache_getInstance = _enigma.eEPGCache_getInstance

class eDVBFrontendParametersSatellite(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    Polarisation_Horizontal = _enigma.eDVBFrontendParametersSatellite_Polarisation_Horizontal
    Polarisation_Vertical = _enigma.eDVBFrontendParametersSatellite_Polarisation_Vertical
    Polarisation_CircularLeft = _enigma.eDVBFrontendParametersSatellite_Polarisation_CircularLeft
    Polarisation_CircularRight = _enigma.eDVBFrontendParametersSatellite_Polarisation_CircularRight
    Inversion_Off = _enigma.eDVBFrontendParametersSatellite_Inversion_Off
    Inversion_On = _enigma.eDVBFrontendParametersSatellite_Inversion_On
    Inversion_Unknown = _enigma.eDVBFrontendParametersSatellite_Inversion_Unknown
    FEC_Auto = _enigma.eDVBFrontendParametersSatellite_FEC_Auto
    FEC_1_2 = _enigma.eDVBFrontendParametersSatellite_FEC_1_2
    FEC_2_3 = _enigma.eDVBFrontendParametersSatellite_FEC_2_3
    FEC_3_4 = _enigma.eDVBFrontendParametersSatellite_FEC_3_4
    FEC_5_6 = _enigma.eDVBFrontendParametersSatellite_FEC_5_6
    FEC_7_8 = _enigma.eDVBFrontendParametersSatellite_FEC_7_8
    FEC_8_9 = _enigma.eDVBFrontendParametersSatellite_FEC_8_9
    FEC_3_5 = _enigma.eDVBFrontendParametersSatellite_FEC_3_5
    FEC_4_5 = _enigma.eDVBFrontendParametersSatellite_FEC_4_5
    FEC_9_10 = _enigma.eDVBFrontendParametersSatellite_FEC_9_10
    FEC_None = _enigma.eDVBFrontendParametersSatellite_FEC_None
    FEC_13_45 = _enigma.eDVBFrontendParametersSatellite_FEC_13_45
    FEC_9_20 = _enigma.eDVBFrontendParametersSatellite_FEC_9_20
    FEC_11_20 = _enigma.eDVBFrontendParametersSatellite_FEC_11_20
    FEC_23_36 = _enigma.eDVBFrontendParametersSatellite_FEC_23_36
    FEC_25_36 = _enigma.eDVBFrontendParametersSatellite_FEC_25_36
    FEC_13_18 = _enigma.eDVBFrontendParametersSatellite_FEC_13_18
    FEC_26_45 = _enigma.eDVBFrontendParametersSatellite_FEC_26_45
    FEC_28_45 = _enigma.eDVBFrontendParametersSatellite_FEC_28_45
    FEC_7_9 = _enigma.eDVBFrontendParametersSatellite_FEC_7_9
    FEC_77_90 = _enigma.eDVBFrontendParametersSatellite_FEC_77_90
    FEC_32_45 = _enigma.eDVBFrontendParametersSatellite_FEC_32_45
    FEC_11_15 = _enigma.eDVBFrontendParametersSatellite_FEC_11_15
    FEC_1_2_L = _enigma.eDVBFrontendParametersSatellite_FEC_1_2_L
    FEC_8_15_L = _enigma.eDVBFrontendParametersSatellite_FEC_8_15_L
    FEC_3_5_L = _enigma.eDVBFrontendParametersSatellite_FEC_3_5_L
    FEC_2_3_L = _enigma.eDVBFrontendParametersSatellite_FEC_2_3_L
    FEC_5_9_L = _enigma.eDVBFrontendParametersSatellite_FEC_5_9_L
    FEC_26_45_L = _enigma.eDVBFrontendParametersSatellite_FEC_26_45_L
    System_DVB_S = _enigma.eDVBFrontendParametersSatellite_System_DVB_S
    System_DVB_S2 = _enigma.eDVBFrontendParametersSatellite_System_DVB_S2
    System_DVB_S2X = _enigma.eDVBFrontendParametersSatellite_System_DVB_S2X
    Modulation_Auto = _enigma.eDVBFrontendParametersSatellite_Modulation_Auto
    Modulation_QPSK = _enigma.eDVBFrontendParametersSatellite_Modulation_QPSK
    Modulation_8PSK = _enigma.eDVBFrontendParametersSatellite_Modulation_8PSK
    Modulation_QAM16 = _enigma.eDVBFrontendParametersSatellite_Modulation_QAM16
    Modulation_16APSK = _enigma.eDVBFrontendParametersSatellite_Modulation_16APSK
    Modulation_32APSK = _enigma.eDVBFrontendParametersSatellite_Modulation_32APSK
    Modulation_8APSK = _enigma.eDVBFrontendParametersSatellite_Modulation_8APSK
    RollOff_alpha_0_35 = _enigma.eDVBFrontendParametersSatellite_RollOff_alpha_0_35
    RollOff_alpha_0_25 = _enigma.eDVBFrontendParametersSatellite_RollOff_alpha_0_25
    RollOff_alpha_0_20 = _enigma.eDVBFrontendParametersSatellite_RollOff_alpha_0_20
    Pilot_Off = _enigma.eDVBFrontendParametersSatellite_Pilot_Off
    Pilot_On = _enigma.eDVBFrontendParametersSatellite_Pilot_On
    Pilot_Unknown = _enigma.eDVBFrontendParametersSatellite_Pilot_Unknown
    PLS_Root = _enigma.eDVBFrontendParametersSatellite_PLS_Root
    PLS_Gold = _enigma.eDVBFrontendParametersSatellite_PLS_Gold
    PLS_Combo = _enigma.eDVBFrontendParametersSatellite_PLS_Combo
    PLS_Unknown = _enigma.eDVBFrontendParametersSatellite_PLS_Unknown
    no_rotor_command_on_tune = _swig_property(_enigma.eDVBFrontendParametersSatellite_no_rotor_command_on_tune_get, _enigma.eDVBFrontendParametersSatellite_no_rotor_command_on_tune_set)
    frequency = _swig_property(_enigma.eDVBFrontendParametersSatellite_frequency_get, _enigma.eDVBFrontendParametersSatellite_frequency_set)
    symbol_rate = _swig_property(_enigma.eDVBFrontendParametersSatellite_symbol_rate_get, _enigma.eDVBFrontendParametersSatellite_symbol_rate_set)
    polarisation = _swig_property(_enigma.eDVBFrontendParametersSatellite_polarisation_get, _enigma.eDVBFrontendParametersSatellite_polarisation_set)
    fec = _swig_property(_enigma.eDVBFrontendParametersSatellite_fec_get, _enigma.eDVBFrontendParametersSatellite_fec_set)
    inversion = _swig_property(_enigma.eDVBFrontendParametersSatellite_inversion_get, _enigma.eDVBFrontendParametersSatellite_inversion_set)
    orbital_position = _swig_property(_enigma.eDVBFrontendParametersSatellite_orbital_position_get, _enigma.eDVBFrontendParametersSatellite_orbital_position_set)
    system = _swig_property(_enigma.eDVBFrontendParametersSatellite_system_get, _enigma.eDVBFrontendParametersSatellite_system_set)
    modulation = _swig_property(_enigma.eDVBFrontendParametersSatellite_modulation_get, _enigma.eDVBFrontendParametersSatellite_modulation_set)
    rolloff = _swig_property(_enigma.eDVBFrontendParametersSatellite_rolloff_get, _enigma.eDVBFrontendParametersSatellite_rolloff_set)
    pilot = _swig_property(_enigma.eDVBFrontendParametersSatellite_pilot_get, _enigma.eDVBFrontendParametersSatellite_pilot_set)
    is_id = _swig_property(_enigma.eDVBFrontendParametersSatellite_is_id_get, _enigma.eDVBFrontendParametersSatellite_is_id_set)
    pls_mode = _swig_property(_enigma.eDVBFrontendParametersSatellite_pls_mode_get, _enigma.eDVBFrontendParametersSatellite_pls_mode_set)
    pls_code = _swig_property(_enigma.eDVBFrontendParametersSatellite_pls_code_get, _enigma.eDVBFrontendParametersSatellite_pls_code_set)

    def __init__(self):
        _enigma.eDVBFrontendParametersSatellite_swiginit(self, _enigma.new_eDVBFrontendParametersSatellite())

    __swig_destroy__ = _enigma.delete_eDVBFrontendParametersSatellite


eDVBFrontendParametersSatellite_swigregister = _enigma.eDVBFrontendParametersSatellite_swigregister
eDVBFrontendParametersSatellite_swigregister(eDVBFrontendParametersSatellite)

class eDVBFrontendParametersCable(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    Inversion_Off = _enigma.eDVBFrontendParametersCable_Inversion_Off
    Inversion_On = _enigma.eDVBFrontendParametersCable_Inversion_On
    Inversion_Unknown = _enigma.eDVBFrontendParametersCable_Inversion_Unknown
    FEC_Auto = _enigma.eDVBFrontendParametersCable_FEC_Auto
    FEC_1_2 = _enigma.eDVBFrontendParametersCable_FEC_1_2
    FEC_2_3 = _enigma.eDVBFrontendParametersCable_FEC_2_3
    FEC_3_4 = _enigma.eDVBFrontendParametersCable_FEC_3_4
    FEC_5_6 = _enigma.eDVBFrontendParametersCable_FEC_5_6
    FEC_7_8 = _enigma.eDVBFrontendParametersCable_FEC_7_8
    FEC_8_9 = _enigma.eDVBFrontendParametersCable_FEC_8_9
    FEC_None = _enigma.eDVBFrontendParametersCable_FEC_None
    Modulation_Auto = _enigma.eDVBFrontendParametersCable_Modulation_Auto
    Modulation_QAM16 = _enigma.eDVBFrontendParametersCable_Modulation_QAM16
    Modulation_QAM32 = _enigma.eDVBFrontendParametersCable_Modulation_QAM32
    Modulation_QAM64 = _enigma.eDVBFrontendParametersCable_Modulation_QAM64
    Modulation_QAM128 = _enigma.eDVBFrontendParametersCable_Modulation_QAM128
    Modulation_QAM256 = _enigma.eDVBFrontendParametersCable_Modulation_QAM256
    frequency = _swig_property(_enigma.eDVBFrontendParametersCable_frequency_get, _enigma.eDVBFrontendParametersCable_frequency_set)
    symbol_rate = _swig_property(_enigma.eDVBFrontendParametersCable_symbol_rate_get, _enigma.eDVBFrontendParametersCable_symbol_rate_set)
    modulation = _swig_property(_enigma.eDVBFrontendParametersCable_modulation_get, _enigma.eDVBFrontendParametersCable_modulation_set)
    inversion = _swig_property(_enigma.eDVBFrontendParametersCable_inversion_get, _enigma.eDVBFrontendParametersCable_inversion_set)
    fec_inner = _swig_property(_enigma.eDVBFrontendParametersCable_fec_inner_get, _enigma.eDVBFrontendParametersCable_fec_inner_set)

    def __init__(self):
        _enigma.eDVBFrontendParametersCable_swiginit(self, _enigma.new_eDVBFrontendParametersCable())

    __swig_destroy__ = _enigma.delete_eDVBFrontendParametersCable


eDVBFrontendParametersCable_swigregister = _enigma.eDVBFrontendParametersCable_swigregister
eDVBFrontendParametersCable_swigregister(eDVBFrontendParametersCable)

class eDVBFrontendParametersTerrestrial(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    Bandwidth_8MHz = _enigma.eDVBFrontendParametersTerrestrial_Bandwidth_8MHz
    Bandwidth_7MHz = _enigma.eDVBFrontendParametersTerrestrial_Bandwidth_7MHz
    Bandwidth_6MHz = _enigma.eDVBFrontendParametersTerrestrial_Bandwidth_6MHz
    Bandwidth_Auto = _enigma.eDVBFrontendParametersTerrestrial_Bandwidth_Auto
    Bandwidth_5MHz = _enigma.eDVBFrontendParametersTerrestrial_Bandwidth_5MHz
    Bandwidth_10MHz = _enigma.eDVBFrontendParametersTerrestrial_Bandwidth_10MHz
    Bandwidth_1_712MHz = _enigma.eDVBFrontendParametersTerrestrial_Bandwidth_1_712MHz
    FEC_1_2 = _enigma.eDVBFrontendParametersTerrestrial_FEC_1_2
    FEC_2_3 = _enigma.eDVBFrontendParametersTerrestrial_FEC_2_3
    FEC_3_4 = _enigma.eDVBFrontendParametersTerrestrial_FEC_3_4
    FEC_4_5 = _enigma.eDVBFrontendParametersTerrestrial_FEC_4_5
    FEC_5_6 = _enigma.eDVBFrontendParametersTerrestrial_FEC_5_6
    FEC_7_8 = _enigma.eDVBFrontendParametersTerrestrial_FEC_7_8
    FEC_Auto = _enigma.eDVBFrontendParametersTerrestrial_FEC_Auto
    FEC_6_7 = _enigma.eDVBFrontendParametersTerrestrial_FEC_6_7
    FEC_8_9 = _enigma.eDVBFrontendParametersTerrestrial_FEC_8_9
    TransmissionMode_2k = _enigma.eDVBFrontendParametersTerrestrial_TransmissionMode_2k
    TransmissionMode_8k = _enigma.eDVBFrontendParametersTerrestrial_TransmissionMode_8k
    TransmissionMode_Auto = _enigma.eDVBFrontendParametersTerrestrial_TransmissionMode_Auto
    TransmissionMode_4k = _enigma.eDVBFrontendParametersTerrestrial_TransmissionMode_4k
    TransmissionMode_1k = _enigma.eDVBFrontendParametersTerrestrial_TransmissionMode_1k
    TransmissionMode_16k = _enigma.eDVBFrontendParametersTerrestrial_TransmissionMode_16k
    TransmissionMode_32k = _enigma.eDVBFrontendParametersTerrestrial_TransmissionMode_32k
    GuardInterval_1_32 = _enigma.eDVBFrontendParametersTerrestrial_GuardInterval_1_32
    GuardInterval_1_16 = _enigma.eDVBFrontendParametersTerrestrial_GuardInterval_1_16
    GuardInterval_1_8 = _enigma.eDVBFrontendParametersTerrestrial_GuardInterval_1_8
    GuardInterval_1_4 = _enigma.eDVBFrontendParametersTerrestrial_GuardInterval_1_4
    GuardInterval_Auto = _enigma.eDVBFrontendParametersTerrestrial_GuardInterval_Auto
    GuardInterval_1_128 = _enigma.eDVBFrontendParametersTerrestrial_GuardInterval_1_128
    GuardInterval_19_128 = _enigma.eDVBFrontendParametersTerrestrial_GuardInterval_19_128
    GuardInterval_19_256 = _enigma.eDVBFrontendParametersTerrestrial_GuardInterval_19_256
    Hierarchy_None = _enigma.eDVBFrontendParametersTerrestrial_Hierarchy_None
    Hierarchy_1 = _enigma.eDVBFrontendParametersTerrestrial_Hierarchy_1
    Hierarchy_2 = _enigma.eDVBFrontendParametersTerrestrial_Hierarchy_2
    Hierarchy_4 = _enigma.eDVBFrontendParametersTerrestrial_Hierarchy_4
    Hierarchy_Auto = _enigma.eDVBFrontendParametersTerrestrial_Hierarchy_Auto
    Modulation_QPSK = _enigma.eDVBFrontendParametersTerrestrial_Modulation_QPSK
    Modulation_QAM16 = _enigma.eDVBFrontendParametersTerrestrial_Modulation_QAM16
    Modulation_QAM64 = _enigma.eDVBFrontendParametersTerrestrial_Modulation_QAM64
    Modulation_Auto = _enigma.eDVBFrontendParametersTerrestrial_Modulation_Auto
    Modulation_QAM256 = _enigma.eDVBFrontendParametersTerrestrial_Modulation_QAM256
    Inversion_Off = _enigma.eDVBFrontendParametersTerrestrial_Inversion_Off
    Inversion_On = _enigma.eDVBFrontendParametersTerrestrial_Inversion_On
    Inversion_Unknown = _enigma.eDVBFrontendParametersTerrestrial_Inversion_Unknown
    System_DVB_T = _enigma.eDVBFrontendParametersTerrestrial_System_DVB_T
    System_DVB_T2 = _enigma.eDVBFrontendParametersTerrestrial_System_DVB_T2
    frequency = _swig_property(_enigma.eDVBFrontendParametersTerrestrial_frequency_get, _enigma.eDVBFrontendParametersTerrestrial_frequency_set)
    bandwidth = _swig_property(_enigma.eDVBFrontendParametersTerrestrial_bandwidth_get, _enigma.eDVBFrontendParametersTerrestrial_bandwidth_set)
    code_rate_HP = _swig_property(_enigma.eDVBFrontendParametersTerrestrial_code_rate_HP_get, _enigma.eDVBFrontendParametersTerrestrial_code_rate_HP_set)
    code_rate_LP = _swig_property(_enigma.eDVBFrontendParametersTerrestrial_code_rate_LP_get, _enigma.eDVBFrontendParametersTerrestrial_code_rate_LP_set)
    modulation = _swig_property(_enigma.eDVBFrontendParametersTerrestrial_modulation_get, _enigma.eDVBFrontendParametersTerrestrial_modulation_set)
    transmission_mode = _swig_property(_enigma.eDVBFrontendParametersTerrestrial_transmission_mode_get, _enigma.eDVBFrontendParametersTerrestrial_transmission_mode_set)
    guard_interval = _swig_property(_enigma.eDVBFrontendParametersTerrestrial_guard_interval_get, _enigma.eDVBFrontendParametersTerrestrial_guard_interval_set)
    hierarchy = _swig_property(_enigma.eDVBFrontendParametersTerrestrial_hierarchy_get, _enigma.eDVBFrontendParametersTerrestrial_hierarchy_set)
    inversion = _swig_property(_enigma.eDVBFrontendParametersTerrestrial_inversion_get, _enigma.eDVBFrontendParametersTerrestrial_inversion_set)
    system = _swig_property(_enigma.eDVBFrontendParametersTerrestrial_system_get, _enigma.eDVBFrontendParametersTerrestrial_system_set)
    plpid = _swig_property(_enigma.eDVBFrontendParametersTerrestrial_plpid_get, _enigma.eDVBFrontendParametersTerrestrial_plpid_set)

    def __init__(self):
        _enigma.eDVBFrontendParametersTerrestrial_swiginit(self, _enigma.new_eDVBFrontendParametersTerrestrial())

    __swig_destroy__ = _enigma.delete_eDVBFrontendParametersTerrestrial


eDVBFrontendParametersTerrestrial_swigregister = _enigma.eDVBFrontendParametersTerrestrial_swigregister
eDVBFrontendParametersTerrestrial_swigregister(eDVBFrontendParametersTerrestrial)

class eDVBLocalTimeHandler(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    m_timeUpdated = _swig_property(_enigma.eDVBLocalTimeHandler_m_timeUpdated_get)
    getInstance = staticmethod(_enigma.eDVBLocalTimeHandler_getInstance)


eDVBLocalTimeHandler.getUseDVBTime = new_instancemethod(_enigma.eDVBLocalTimeHandler_getUseDVBTime, None, eDVBLocalTimeHandler)
eDVBLocalTimeHandler.setUseDVBTime = new_instancemethod(_enigma.eDVBLocalTimeHandler_setUseDVBTime, None, eDVBLocalTimeHandler)
eDVBLocalTimeHandler.nowTime = new_instancemethod(_enigma.eDVBLocalTimeHandler_nowTime, None, eDVBLocalTimeHandler)
eDVBLocalTimeHandler.ready = new_instancemethod(_enigma.eDVBLocalTimeHandler_ready, None, eDVBLocalTimeHandler)
eDVBLocalTimeHandler_swigregister = _enigma.eDVBLocalTimeHandler_swigregister
eDVBLocalTimeHandler_swigregister(eDVBLocalTimeHandler)

def eDVBLocalTimeHandler_getInstance():
    return _enigma.eDVBLocalTimeHandler_getInstance()


eDVBLocalTimeHandler_getInstance = _enigma.eDVBLocalTimeHandler_getInstance

class iDVBFrontendParameters(iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined - class is abstract')

    __repr__ = _swig_repr
    flagOnlyFree = _enigma.iDVBFrontendParameters_flagOnlyFree


iDVBFrontendParameters.getSystem = new_instancemethod(_enigma.iDVBFrontendParameters_getSystem, None, iDVBFrontendParameters)
iDVBFrontendParameters.getDVBS = new_instancemethod(_enigma.iDVBFrontendParameters_getDVBS, None, iDVBFrontendParameters)
iDVBFrontendParameters.getDVBC = new_instancemethod(_enigma.iDVBFrontendParameters_getDVBC, None, iDVBFrontendParameters)
iDVBFrontendParameters.getDVBT = new_instancemethod(_enigma.iDVBFrontendParameters_getDVBT, None, iDVBFrontendParameters)
iDVBFrontendParameters.getFlags = new_instancemethod(_enigma.iDVBFrontendParameters_getFlags, None, iDVBFrontendParameters)
iDVBFrontendParameters_swigregister = _enigma.iDVBFrontendParameters_swigregister
iDVBFrontendParameters_swigregister(iDVBFrontendParameters)

class iDVBFrontendParametersPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iDVBFrontendParametersPtr_swiginit(self, _enigma.new_iDVBFrontendParametersPtr(*args))

    __swig_destroy__ = _enigma.delete_iDVBFrontendParametersPtr


iDVBFrontendParametersPtr.__ref__ = new_instancemethod(_enigma.iDVBFrontendParametersPtr___ref__, None, iDVBFrontendParametersPtr)
iDVBFrontendParametersPtr.getPtrString = new_instancemethod(_enigma.iDVBFrontendParametersPtr_getPtrString, None, iDVBFrontendParametersPtr)
iDVBFrontendParametersPtr.__deref__ = new_instancemethod(_enigma.iDVBFrontendParametersPtr___deref__, None, iDVBFrontendParametersPtr)
iDVBFrontendParametersPtr.getSystem = new_instancemethod(_enigma.iDVBFrontendParametersPtr_getSystem, None, iDVBFrontendParametersPtr)
iDVBFrontendParametersPtr.getDVBS = new_instancemethod(_enigma.iDVBFrontendParametersPtr_getDVBS, None, iDVBFrontendParametersPtr)
iDVBFrontendParametersPtr.getDVBC = new_instancemethod(_enigma.iDVBFrontendParametersPtr_getDVBC, None, iDVBFrontendParametersPtr)
iDVBFrontendParametersPtr.getDVBT = new_instancemethod(_enigma.iDVBFrontendParametersPtr_getDVBT, None, iDVBFrontendParametersPtr)
iDVBFrontendParametersPtr.getFlags = new_instancemethod(_enigma.iDVBFrontendParametersPtr_getFlags, None, iDVBFrontendParametersPtr)
iDVBFrontendParametersPtr_swigregister = _enigma.iDVBFrontendParametersPtr_swigregister
iDVBFrontendParametersPtr_swigregister(iDVBFrontendParametersPtr)
MAX_DISEQC_LENGTH = _enigma.MAX_DISEQC_LENGTH

class eDVBDiseqcCommand(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eDVBDiseqcCommand_swiginit(self, _enigma.new_eDVBDiseqcCommand())

    __swig_destroy__ = _enigma.delete_eDVBDiseqcCommand


eDVBDiseqcCommand.setCommandString = new_instancemethod(_enigma.eDVBDiseqcCommand_setCommandString, None, eDVBDiseqcCommand)
eDVBDiseqcCommand_swigregister = _enigma.eDVBDiseqcCommand_swigregister
eDVBDiseqcCommand_swigregister(eDVBDiseqcCommand)

class iDVBFrontend(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    feSatellite = _enigma.iDVBFrontend_ENUMS_feSatellite
    feCable = _enigma.iDVBFrontend_ENUMS_feCable
    feTerrestrial = _enigma.iDVBFrontend_ENUMS_feTerrestrial
    stateIdle = _enigma.iDVBFrontend_ENUMS_stateIdle
    stateTuning = _enigma.iDVBFrontend_ENUMS_stateTuning
    stateFailed = _enigma.iDVBFrontend_ENUMS_stateFailed
    stateLock = _enigma.iDVBFrontend_ENUMS_stateLock
    stateLostLock = _enigma.iDVBFrontend_ENUMS_stateLostLock
    stateClosed = _enigma.iDVBFrontend_ENUMS_stateClosed
    toneOff = _enigma.iDVBFrontend_ENUMS_toneOff
    toneOn = _enigma.iDVBFrontend_ENUMS_toneOn
    voltageOff = _enigma.iDVBFrontend_ENUMS_voltageOff
    voltage13 = _enigma.iDVBFrontend_ENUMS_voltage13
    voltage18 = _enigma.iDVBFrontend_ENUMS_voltage18
    voltage13_5 = _enigma.iDVBFrontend_ENUMS_voltage13_5
    voltage18_5 = _enigma.iDVBFrontend_ENUMS_voltage18_5
    bitErrorRate = _enigma.iDVBFrontend_ENUMS_bitErrorRate
    signalPower = _enigma.iDVBFrontend_ENUMS_signalPower
    signalQuality = _enigma.iDVBFrontend_ENUMS_signalQuality
    locked = _enigma.iDVBFrontend_ENUMS_locked
    synced = _enigma.iDVBFrontend_ENUMS_synced
    frontendNumber = _enigma.iDVBFrontend_ENUMS_frontendNumber
    signalQualitydB = _enigma.iDVBFrontend_ENUMS_signalQualitydB
    isUsbTuner = _enigma.iDVBFrontend_ENUMS_isUsbTuner


iDVBFrontend_swigregister = _enigma.iDVBFrontend_ENUMS_swigregister
iDVBFrontend_swigregister(iDVBFrontend)

class iDVBFrontendPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iDVBFrontendPtr_swiginit(self, _enigma.new_iDVBFrontendPtr(*args))

    __swig_destroy__ = _enigma.delete_iDVBFrontendPtr


iDVBFrontendPtr.__ref__ = new_instancemethod(_enigma.iDVBFrontendPtr___ref__, None, iDVBFrontendPtr)
iDVBFrontendPtr.getPtrString = new_instancemethod(_enigma.iDVBFrontendPtr_getPtrString, None, iDVBFrontendPtr)
iDVBFrontendPtr.__deref__ = new_instancemethod(_enigma.iDVBFrontendPtr___deref__, None, iDVBFrontendPtr)
iDVBFrontendPtr.tune = new_instancemethod(_enigma.iDVBFrontendPtr_tune, None, iDVBFrontendPtr)
iDVBFrontendPtr.closeFrontend = new_instancemethod(_enigma.iDVBFrontendPtr_closeFrontend, None, iDVBFrontendPtr)
iDVBFrontendPtr.reopenFrontend = new_instancemethod(_enigma.iDVBFrontendPtr_reopenFrontend, None, iDVBFrontendPtr)
iDVBFrontendPtr.getState = new_instancemethod(_enigma.iDVBFrontendPtr_getState, None, iDVBFrontendPtr)
iDVBFrontendPtr.setTone = new_instancemethod(_enigma.iDVBFrontendPtr_setTone, None, iDVBFrontendPtr)
iDVBFrontendPtr.setVoltage = new_instancemethod(_enigma.iDVBFrontendPtr_setVoltage, None, iDVBFrontendPtr)
iDVBFrontendPtr.sendDiseqc = new_instancemethod(_enigma.iDVBFrontendPtr_sendDiseqc, None, iDVBFrontendPtr)
iDVBFrontendPtr.sendToneburst = new_instancemethod(_enigma.iDVBFrontendPtr_sendToneburst, None, iDVBFrontendPtr)
iDVBFrontendPtr.readFrontendData = new_instancemethod(_enigma.iDVBFrontendPtr_readFrontendData, None, iDVBFrontendPtr)
iDVBFrontendPtr.getFrontendStatus = new_instancemethod(_enigma.iDVBFrontendPtr_getFrontendStatus, None, iDVBFrontendPtr)
iDVBFrontendPtr.getTransponderData = new_instancemethod(_enigma.iDVBFrontendPtr_getTransponderData, None, iDVBFrontendPtr)
iDVBFrontendPtr.getFrontendData = new_instancemethod(_enigma.iDVBFrontendPtr_getFrontendData, None, iDVBFrontendPtr)
iDVBFrontendPtr_swigregister = _enigma.iDVBFrontendPtr_swigregister
iDVBFrontendPtr_swigregister(iDVBFrontendPtr)

class iDVBChannelPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iDVBChannelPtr_swiginit(self, _enigma.new_iDVBChannelPtr(*args))

    __swig_destroy__ = _enigma.delete_iDVBChannelPtr


iDVBChannelPtr.__ref__ = new_instancemethod(_enigma.iDVBChannelPtr___ref__, None, iDVBChannelPtr)
iDVBChannelPtr.__deref__ = new_instancemethod(_enigma.iDVBChannelPtr___deref__, None, iDVBChannelPtr)
iDVBChannelPtr.getFrontend = new_instancemethod(_enigma.iDVBChannelPtr_getFrontend, None, iDVBChannelPtr)
iDVBChannelPtr.requestTsidOnid = new_instancemethod(_enigma.iDVBChannelPtr_requestTsidOnid, None, iDVBChannelPtr)
iDVBChannelPtr.reserveDemux = new_instancemethod(_enigma.iDVBChannelPtr_reserveDemux, None, iDVBChannelPtr)
iDVBChannelPtr_swigregister = _enigma.iDVBChannelPtr_swigregister
iDVBChannelPtr_swigregister(iDVBChannelPtr)

class eDVBResourceManager(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eDVBResourceManager_swiginit(self, _enigma.new_eDVBResourceManager(*args))

    __swig_destroy__ = _enigma.delete_eDVBResourceManager
    getInstance = staticmethod(_enigma.eDVBResourceManager_getInstance)
    frontendUseMaskChanged = _swig_property(_enigma.eDVBResourceManager_frontendUseMaskChanged_get)


eDVBResourceManager.__ref__ = new_instancemethod(_enigma.eDVBResourceManager___ref__, None, eDVBResourceManager)
eDVBResourceManager.getPtrString = new_instancemethod(_enigma.eDVBResourceManager_getPtrString, None, eDVBResourceManager)
eDVBResourceManager.__deref__ = new_instancemethod(_enigma.eDVBResourceManager___deref__, None, eDVBResourceManager)
eDVBResourceManager.canAllocateFrontend = new_instancemethod(_enigma.eDVBResourceManager_canAllocateFrontend, None, eDVBResourceManager)
eDVBResourceManager.canMeasureFrontendInputPower = new_instancemethod(_enigma.eDVBResourceManager_canMeasureFrontendInputPower, None, eDVBResourceManager)
eDVBResourceManager.allocateRawChannel = new_instancemethod(_enigma.eDVBResourceManager_allocateRawChannel, None, eDVBResourceManager)
eDVBResourceManager.setFrontendSlotInformations = new_instancemethod(_enigma.eDVBResourceManager_setFrontendSlotInformations, None, eDVBResourceManager)
eDVBResourceManager.frontendIsCompatible = new_instancemethod(_enigma.eDVBResourceManager_frontendIsCompatible, None, eDVBResourceManager)
eDVBResourceManager.frontendIsMultistream = new_instancemethod(_enigma.eDVBResourceManager_frontendIsMultistream, None, eDVBResourceManager)
eDVBResourceManager.setFrontendType = new_instancemethod(_enigma.eDVBResourceManager_setFrontendType, None, eDVBResourceManager)
eDVBResourceManager_swigregister = _enigma.eDVBResourceManager_swigregister
eDVBResourceManager_swigregister(eDVBResourceManager)

def eDVBResourceManager_getInstance():
    return _enigma.eDVBResourceManager_getInstance()


eDVBResourceManager_getInstance = _enigma.eDVBResourceManager_getInstance

class eDVBFrontendParameters(iDVBFrontendParameters):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eDVBFrontendParameters_swiginit(self, _enigma.new_eDVBFrontendParameters())

    __swig_destroy__ = _enigma.delete_eDVBFrontendParameters


eDVBFrontendParameters.setDVBS = new_instancemethod(_enigma.eDVBFrontendParameters_setDVBS, None, eDVBFrontendParameters)
eDVBFrontendParameters.setDVBC = new_instancemethod(_enigma.eDVBFrontendParameters_setDVBC, None, eDVBFrontendParameters)
eDVBFrontendParameters.setDVBT = new_instancemethod(_enigma.eDVBFrontendParameters_setDVBT, None, eDVBFrontendParameters)
eDVBFrontendParameters.setFlags = new_instancemethod(_enigma.eDVBFrontendParameters_setFlags, None, eDVBFrontendParameters)
eDVBFrontendParameters_swigregister = _enigma.eDVBFrontendParameters_swigregister
eDVBFrontendParameters_swigregister(eDVBFrontendParameters)

class HbbTVApplicationInfo(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    m_OrgId = _swig_property(_enigma.HbbTVApplicationInfo_m_OrgId_get, _enigma.HbbTVApplicationInfo_m_OrgId_set)
    m_AppId = _swig_property(_enigma.HbbTVApplicationInfo_m_AppId_get, _enigma.HbbTVApplicationInfo_m_AppId_set)
    m_ControlCode = _swig_property(_enigma.HbbTVApplicationInfo_m_ControlCode_get, _enigma.HbbTVApplicationInfo_m_ControlCode_set)
    m_ProfileCode = _swig_property(_enigma.HbbTVApplicationInfo_m_ProfileCode_get, _enigma.HbbTVApplicationInfo_m_ProfileCode_set)
    m_HbbTVUrl = _swig_property(_enigma.HbbTVApplicationInfo_m_HbbTVUrl_get, _enigma.HbbTVApplicationInfo_m_HbbTVUrl_set)
    m_ApplicationName = _swig_property(_enigma.HbbTVApplicationInfo_m_ApplicationName_get, _enigma.HbbTVApplicationInfo_m_ApplicationName_set)

    def __init__(self, *args):
        _enigma.HbbTVApplicationInfo_swiginit(self, _enigma.new_HbbTVApplicationInfo(*args))

    __swig_destroy__ = _enigma.delete_HbbTVApplicationInfo


HbbTVApplicationInfo_swigregister = _enigma.HbbTVApplicationInfo_swigregister
HbbTVApplicationInfo_swigregister(HbbTVApplicationInfo)

class eDVBServicePMTHandler(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    eventNoResources = _enigma.eDVBServicePMTHandler_eventNoResources
    eventTuneFailed = _enigma.eDVBServicePMTHandler_eventTuneFailed
    eventNoPAT = _enigma.eDVBServicePMTHandler_eventNoPAT
    eventNoPATEntry = _enigma.eDVBServicePMTHandler_eventNoPATEntry
    eventNoPMT = _enigma.eDVBServicePMTHandler_eventNoPMT
    eventNewProgramInfo = _enigma.eDVBServicePMTHandler_eventNewProgramInfo
    eventTuned = _enigma.eDVBServicePMTHandler_eventTuned
    eventPreStart = _enigma.eDVBServicePMTHandler_eventPreStart
    eventSOF = _enigma.eDVBServicePMTHandler_eventSOF
    eventEOF = _enigma.eDVBServicePMTHandler_eventEOF
    eventHBBTVInfo = _enigma.eDVBServicePMTHandler_eventHBBTVInfo
    eventMisconfiguration = _enigma.eDVBServicePMTHandler_eventMisconfiguration
    eventNoDiskSpace = _enigma.eDVBServicePMTHandler_eventNoDiskSpace
    eventStartPvrDescramble = _enigma.eDVBServicePMTHandler_eventStartPvrDescramble
    eventChannelAllocated = _enigma.eDVBServicePMTHandler_eventChannelAllocated
    __swig_destroy__ = _enigma.delete_eDVBServicePMTHandler


eDVBServicePMTHandler_swigregister = _enigma.eDVBServicePMTHandler_swigregister
eDVBServicePMTHandler_swigregister(eDVBServicePMTHandler)

class eFastScan(iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eFastScan_swiginit(self, _enigma.new_eFastScan(*args))

    __swig_destroy__ = _enigma.delete_eFastScan
    scanProgress = _swig_property(_enigma.eFastScan_scanProgress_get)
    scanCompleted = _swig_property(_enigma.eFastScan_scanCompleted_get)


eFastScan.start = new_instancemethod(_enigma.eFastScan_start, None, eFastScan)
eFastScan.startFile = new_instancemethod(_enigma.eFastScan_startFile, None, eFastScan)
eFastScan.getVersion = new_instancemethod(_enigma.eFastScan_getVersion, None, eFastScan)
eFastScan_swigregister = _enigma.eFastScan_swigregister
eFastScan_swigregister(eFastScan)

class eCableScan(iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.eCableScan_swiginit(self, _enigma.new_eCableScan(*args))

    __swig_destroy__ = _enigma.delete_eCableScan
    scanProgress = _swig_property(_enigma.eCableScan_scanProgress_get)
    scanCompleted = _swig_property(_enigma.eCableScan_scanCompleted_get)


eCableScan.start = new_instancemethod(_enigma.eCableScan_start, None, eCableScan)
eCableScan_swigregister = _enigma.eCableScan_swigregister
eCableScan_swigregister(eCableScan)

class eComponentScan(iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eComponentScan_swiginit(self, _enigma.new_eComponentScan())

    __swig_destroy__ = _enigma.delete_eComponentScan
    statusChanged = _swig_property(_enigma.eComponentScan_statusChanged_get)
    newService = _swig_property(_enigma.eComponentScan_newService_get)
    scanNetworkSearch = _enigma.eComponentScan_scanNetworkSearch
    scanRemoveServices = _enigma.eComponentScan_scanRemoveServices
    scanDontRemoveFeeds = _enigma.eComponentScan_scanDontRemoveFeeds
    scanDontRemoveUnscanned = _enigma.eComponentScan_scanDontRemoveUnscanned
    clearToScanOnFirstNIT = _enigma.eComponentScan_clearToScanOnFirstNIT
    scanOnlyFree = _enigma.eComponentScan_scanOnlyFree


eComponentScan.getProgress = new_instancemethod(_enigma.eComponentScan_getProgress, None, eComponentScan)
eComponentScan.getNumServices = new_instancemethod(_enigma.eComponentScan_getNumServices, None, eComponentScan)
eComponentScan.isDone = new_instancemethod(_enigma.eComponentScan_isDone, None, eComponentScan)
eComponentScan.getLastServiceName = new_instancemethod(_enigma.eComponentScan_getLastServiceName, None, eComponentScan)
eComponentScan.getError = new_instancemethod(_enigma.eComponentScan_getError, None, eComponentScan)
eComponentScan.clear = new_instancemethod(_enigma.eComponentScan_clear, None, eComponentScan)
eComponentScan.clearAll = new_instancemethod(_enigma.eComponentScan_clearAll, None, eComponentScan)
eComponentScan.addInitial = new_instancemethod(_enigma.eComponentScan_addInitial, None, eComponentScan)
eComponentScan.start = new_instancemethod(_enigma.eComponentScan_start, None, eComponentScan)
eComponentScan.getFrontend = new_instancemethod(_enigma.eComponentScan_getFrontend, None, eComponentScan)
eComponentScan.getCurrentTransponder = new_instancemethod(_enigma.eComponentScan_getCurrentTransponder, None, eComponentScan)
eComponentScan_swigregister = _enigma.eComponentScan_swigregister
eComponentScan_swigregister(eComponentScan)

class eBackgroundFileEraser(eMainloop):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.eBackgroundFileEraser_getInstance)


eBackgroundFileEraser.erase = new_instancemethod(_enigma.eBackgroundFileEraser_erase, None, eBackgroundFileEraser)
eBackgroundFileEraser_swigregister = _enigma.eBackgroundFileEraser_swigregister
eBackgroundFileEraser_swigregister(eBackgroundFileEraser)

def eBackgroundFileEraser_getInstance():
    return _enigma.eBackgroundFileEraser_getInstance()


eBackgroundFileEraser_getInstance = _enigma.eBackgroundFileEraser_getInstance

class eTuxtxtApp(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.eTuxtxtApp_swiginit(self, _enigma.new_eTuxtxtApp())

    __swig_destroy__ = _enigma.delete_eTuxtxtApp
    getInstance = staticmethod(_enigma.eTuxtxtApp_getInstance)
    appClosed = _swig_property(_enigma.eTuxtxtApp_appClosed_get)


eTuxtxtApp.startUi = new_instancemethod(_enigma.eTuxtxtApp_startUi, None, eTuxtxtApp)
eTuxtxtApp.initCache = new_instancemethod(_enigma.eTuxtxtApp_initCache, None, eTuxtxtApp)
eTuxtxtApp.freeCache = new_instancemethod(_enigma.eTuxtxtApp_freeCache, None, eTuxtxtApp)
eTuxtxtApp.startCaching = new_instancemethod(_enigma.eTuxtxtApp_startCaching, None, eTuxtxtApp)
eTuxtxtApp.stopCaching = new_instancemethod(_enigma.eTuxtxtApp_stopCaching, None, eTuxtxtApp)
eTuxtxtApp.resetPid = new_instancemethod(_enigma.eTuxtxtApp_resetPid, None, eTuxtxtApp)
eTuxtxtApp.setEnableTtCachingOnOff = new_instancemethod(_enigma.eTuxtxtApp_setEnableTtCachingOnOff, None, eTuxtxtApp)
eTuxtxtApp_swigregister = _enigma.eTuxtxtApp_swigregister
eTuxtxtApp_swigregister(eTuxtxtApp)

def eTuxtxtApp_getInstance():
    return _enigma.eTuxtxtApp_getInstance()


eTuxtxtApp_getInstance = _enigma.eTuxtxtApp_getInstance

class eVTiApp(eMainloop):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.eVTiApp_getInstance)


eVTiApp.startApp = new_instancemethod(_enigma.eVTiApp_startApp, None, eVTiApp)
eVTiApp.stopApp = new_instancemethod(_enigma.eVTiApp_stopApp, None, eVTiApp)
eVTiApp.getServiceState = new_instancemethod(_enigma.eVTiApp_getServiceState, None, eVTiApp)
eVTiApp.addRecordingService = new_instancemethod(_enigma.eVTiApp_addRecordingService, None, eVTiApp)
eVTiApp.removeRecordingService = new_instancemethod(_enigma.eVTiApp_removeRecordingService, None, eVTiApp)
eVTiApp.isServiceRecording = new_instancemethod(_enigma.eVTiApp_isServiceRecording, None, eVTiApp)
eVTiApp.enableMarkRecordings = new_instancemethod(_enigma.eVTiApp_enableMarkRecordings, None, eVTiApp)
eVTiApp.getList = new_instancemethod(_enigma.eVTiApp_getList, None, eVTiApp)
eVTiApp.getAdvertismentServices = new_instancemethod(_enigma.eVTiApp_getAdvertismentServices, None, eVTiApp)
eVTiApp_swigregister = _enigma.eVTiApp_swigregister
eVTiApp_swigregister(eVTiApp)

def eVTiApp_getInstance():
    return _enigma.eVTiApp_getInstance()


eVTiApp_getInstance = _enigma.eVTiApp_getInstance

class eAVSwitch(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.eAVSwitch_getInstance)
    vcr_sb_notifier = _swig_property(_enigma.eAVSwitch_vcr_sb_notifier_get)


eAVSwitch.haveScartSwitch = new_instancemethod(_enigma.eAVSwitch_haveScartSwitch, None, eAVSwitch)
eAVSwitch.getVCRSlowBlanking = new_instancemethod(_enigma.eAVSwitch_getVCRSlowBlanking, None, eAVSwitch)
eAVSwitch.setColorFormat = new_instancemethod(_enigma.eAVSwitch_setColorFormat, None, eAVSwitch)
eAVSwitch.setAspectRatio = new_instancemethod(_enigma.eAVSwitch_setAspectRatio, None, eAVSwitch)
eAVSwitch.setVideomode = new_instancemethod(_enigma.eAVSwitch_setVideomode, None, eAVSwitch)
eAVSwitch.setInput = new_instancemethod(_enigma.eAVSwitch_setInput, None, eAVSwitch)
eAVSwitch.setWSS = new_instancemethod(_enigma.eAVSwitch_setWSS, None, eAVSwitch)
eAVSwitch_swigregister = _enigma.eAVSwitch_swigregister
eAVSwitch_swigregister(eAVSwitch)

def eAVSwitch_getInstance():
    return _enigma.eAVSwitch_getInstance()


eAVSwitch_getInstance = _enigma.eAVSwitch_getInstance

class iCECMessagePtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _enigma.iCECMessagePtr_swiginit(self, _enigma.new_iCECMessagePtr(*args))

    __swig_destroy__ = _enigma.delete_iCECMessagePtr


iCECMessagePtr.__ref__ = new_instancemethod(_enigma.iCECMessagePtr___ref__, None, iCECMessagePtr)
iCECMessagePtr.getPtrString = new_instancemethod(_enigma.iCECMessagePtr_getPtrString, None, iCECMessagePtr)
iCECMessagePtr.__deref__ = new_instancemethod(_enigma.iCECMessagePtr___deref__, None, iCECMessagePtr)
iCECMessagePtr.getAddress = new_instancemethod(_enigma.iCECMessagePtr_getAddress, None, iCECMessagePtr)
iCECMessagePtr.getCommand = new_instancemethod(_enigma.iCECMessagePtr_getCommand, None, iCECMessagePtr)
iCECMessagePtr.getData = new_instancemethod(_enigma.iCECMessagePtr_getData, None, iCECMessagePtr)
iCECMessagePtr_swigregister = _enigma.iCECMessagePtr_swigregister
iCECMessagePtr_swigregister(iCECMessagePtr)

def New_iCECMessagePtr(*args):
    return _enigma.New_iCECMessagePtr(*args)


New_iCECMessagePtr = _enigma.New_iCECMessagePtr

def PyFrom(*args):
    return _enigma.PyFrom(*args)


PyFrom = _enigma.PyFrom

class eHdmiCEC(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.eHdmiCEC_getInstance)
    messageReceived = _swig_property(_enigma.eHdmiCEC_messageReceived_get)
    messageReceivedKey = _swig_property(_enigma.eHdmiCEC_messageReceivedKey_get)
    cecMessageReceived = _swig_property(_enigma.eHdmiCEC_cecMessageReceived_get)


eHdmiCEC.sendMessage = new_instancemethod(_enigma.eHdmiCEC_sendMessage, None, eHdmiCEC)
eHdmiCEC_swigregister = _enigma.eHdmiCEC_swigregister
eHdmiCEC_swigregister(eHdmiCEC)

def eHdmiCEC_getInstance():
    return _enigma.eHdmiCEC_getInstance()


eHdmiCEC_getInstance = _enigma.eHdmiCEC_getInstance

class eRFmod(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.eRFmod_getInstance)


eRFmod.detected = new_instancemethod(_enigma.eRFmod_detected, None, eRFmod)
eRFmod.setFunction = new_instancemethod(_enigma.eRFmod_setFunction, None, eRFmod)
eRFmod.setTestmode = new_instancemethod(_enigma.eRFmod_setTestmode, None, eRFmod)
eRFmod.setSoundFunction = new_instancemethod(_enigma.eRFmod_setSoundFunction, None, eRFmod)
eRFmod.setSoundCarrier = new_instancemethod(_enigma.eRFmod_setSoundCarrier, None, eRFmod)
eRFmod.setChannel = new_instancemethod(_enigma.eRFmod_setChannel, None, eRFmod)
eRFmod.setFinetune = new_instancemethod(_enigma.eRFmod_setFinetune, None, eRFmod)
eRFmod_swigregister = _enigma.eRFmod_swigregister
eRFmod_swigregister(eRFmod)

def eRFmod_getInstance():
    return _enigma.eRFmod_getInstance()


eRFmod_getInstance = _enigma.eRFmod_getInstance

class Misc_Options(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.Misc_Options_getInstance)
    __swig_destroy__ = _enigma.delete_Misc_Options


Misc_Options.set_12V_output = new_instancemethod(_enigma.Misc_Options_set_12V_output, None, Misc_Options)
Misc_Options.get_12V_output = new_instancemethod(_enigma.Misc_Options_get_12V_output, None, Misc_Options)
Misc_Options.detected_12V_output = new_instancemethod(_enigma.Misc_Options_detected_12V_output, None, Misc_Options)
Misc_Options_swigregister = _enigma.Misc_Options_swigregister
Misc_Options_swigregister(Misc_Options)

def Misc_Options_getInstance():
    return _enigma.Misc_Options_getInstance()


Misc_Options_getInstance = _enigma.Misc_Options_getInstance

def e_tzset():
    return _enigma.e_tzset()


e_tzset = _enigma.e_tzset
LCD_CONTRAST_MIN = _enigma.LCD_CONTRAST_MIN
LCD_CONTRAST_MAX = _enigma.LCD_CONTRAST_MAX
LCD_BRIGHTNESS_MIN = _enigma.LCD_BRIGHTNESS_MIN
LCD_BRIGHTNESS_MAX = _enigma.LCD_BRIGHTNESS_MAX

class eLCD(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr


eLCD.lock = new_instancemethod(_enigma.eLCD_lock, None, eLCD)
eLCD.unlock = new_instancemethod(_enigma.eLCD_unlock, None, eLCD)
eLCD.islocked = new_instancemethod(_enigma.eLCD_islocked, None, eLCD)
eLCD.detected = new_instancemethod(_enigma.eLCD_detected, None, eLCD)
eLCD_swigregister = _enigma.eLCD_swigregister
eLCD_swigregister(eLCD)

class eDBoxLCD(eLCD):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.eDBoxLCD_getInstance)


eDBoxLCD.setLCDContrast = new_instancemethod(_enigma.eDBoxLCD_setLCDContrast, None, eDBoxLCD)
eDBoxLCD.setLCDBrightness = new_instancemethod(_enigma.eDBoxLCD_setLCDBrightness, None, eDBoxLCD)
eDBoxLCD.setInverted = new_instancemethod(_enigma.eDBoxLCD_setInverted, None, eDBoxLCD)
eDBoxLCD.isOled = new_instancemethod(_enigma.eDBoxLCD_isOled, None, eDBoxLCD)
eDBoxLCD.update = new_instancemethod(_enigma.eDBoxLCD_update, None, eDBoxLCD)
eDBoxLCD_swigregister = _enigma.eDBoxLCD_swigregister
eDBoxLCD_swigregister(eDBoxLCD)

def eDBoxLCD_getInstance():
    return _enigma.eDBoxLCD_getInstance()


eDBoxLCD_getInstance = _enigma.eDBoxLCD_getInstance
_POSIX_C_SOURCE = _enigma._POSIX_C_SOURCE

class eMMI_UI(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined - class is abstract')

    __repr__ = _swig_repr


eMMI_UI.getState = new_instancemethod(_enigma.eMMI_UI_getState, None, eMMI_UI)
eMMI_UI.setState = new_instancemethod(_enigma.eMMI_UI_setState, None, eMMI_UI)
eMMI_UI.getAppName = new_instancemethod(_enigma.eMMI_UI_getAppName, None, eMMI_UI)
eMMI_UI.setAppName = new_instancemethod(_enigma.eMMI_UI_setAppName, None, eMMI_UI)
eMMI_UI.availableMMI = new_instancemethod(_enigma.eMMI_UI_availableMMI, None, eMMI_UI)
eMMI_UI.getMMIScreen = new_instancemethod(_enigma.eMMI_UI_getMMIScreen, None, eMMI_UI)
eMMI_UI_swigregister = _enigma.eMMI_UI_swigregister
eMMI_UI_swigregister(eMMI_UI)

class eDVBCIInterfaces(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.eDVBCIInterfaces_getInstance)


eDVBCIInterfaces.getNumOfSlots = new_instancemethod(_enigma.eDVBCIInterfaces_getNumOfSlots, None, eDVBCIInterfaces)
eDVBCIInterfaces.getDescrambleRules = new_instancemethod(_enigma.eDVBCIInterfaces_getDescrambleRules, None, eDVBCIInterfaces)
eDVBCIInterfaces.setDescrambleRules = new_instancemethod(_enigma.eDVBCIInterfaces_setDescrambleRules, None, eDVBCIInterfaces)
eDVBCIInterfaces.readCICaIds = new_instancemethod(_enigma.eDVBCIInterfaces_readCICaIds, None, eDVBCIInterfaces)
eDVBCIInterfaces.announceCCK = new_instancemethod(_enigma.eDVBCIInterfaces_announceCCK, None, eDVBCIInterfaces)
eDVBCIInterfaces.setupBypass = new_instancemethod(_enigma.eDVBCIInterfaces_setupBypass, None, eDVBCIInterfaces)
eDVBCIInterfaces.revertBypass = new_instancemethod(_enigma.eDVBCIInterfaces_revertBypass, None, eDVBCIInterfaces)
eDVBCIInterfaces.add_ui_cmd = new_instancemethod(_enigma.eDVBCIInterfaces_add_ui_cmd, None, eDVBCIInterfaces)
eDVBCIInterfaces_swigregister = _enigma.eDVBCIInterfaces_swigregister
eDVBCIInterfaces_swigregister(eDVBCIInterfaces)

def eDVBCIInterfaces_getInstance():
    return _enigma.eDVBCIInterfaces_getInstance()


eDVBCIInterfaces_getInstance = _enigma.eDVBCIInterfaces_getInstance

class eDVBCI_UI(eMMI_UI):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    rateNormal = _enigma.eDVBCI_UI_rateNormal
    rateHigh = _enigma.eDVBCI_UI_rateHigh
    ciStateChanged = _swig_property(_enigma.eDVBCI_UI_ciStateChanged_get)
    getInstance = staticmethod(_enigma.eDVBCI_UI_getInstance)
    __swig_destroy__ = _enigma.delete_eDVBCI_UI


eDVBCI_UI.setInit = new_instancemethod(_enigma.eDVBCI_UI_setInit, None, eDVBCI_UI)
eDVBCI_UI.setReset = new_instancemethod(_enigma.eDVBCI_UI_setReset, None, eDVBCI_UI)
eDVBCI_UI.startMMI = new_instancemethod(_enigma.eDVBCI_UI_startMMI, None, eDVBCI_UI)
eDVBCI_UI.stopMMI = new_instancemethod(_enigma.eDVBCI_UI_stopMMI, None, eDVBCI_UI)
eDVBCI_UI.getMMIState = new_instancemethod(_enigma.eDVBCI_UI_getMMIState, None, eDVBCI_UI)
eDVBCI_UI.answerMenu = new_instancemethod(_enigma.eDVBCI_UI_answerMenu, None, eDVBCI_UI)
eDVBCI_UI.answerEnq = new_instancemethod(_enigma.eDVBCI_UI_answerEnq, None, eDVBCI_UI)
eDVBCI_UI.cancelEnq = new_instancemethod(_enigma.eDVBCI_UI_cancelEnq, None, eDVBCI_UI)
eDVBCI_UI.setClockRate = new_instancemethod(_enigma.eDVBCI_UI_setClockRate, None, eDVBCI_UI)
eDVBCI_UI_swigregister = _enigma.eDVBCI_UI_swigregister
eDVBCI_UI_swigregister(eDVBCI_UI)

def eDVBCI_UI_getInstance():
    return _enigma.eDVBCI_UI_getInstance()


eDVBCI_UI_getInstance = _enigma.eDVBCI_UI_getInstance

class eDVBDB(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError('No constructor defined')

    __repr__ = _swig_repr
    getInstance = staticmethod(_enigma.eDVBDB_getInstance)


eDVBDB.removeFlags = new_instancemethod(_enigma.eDVBDB_removeFlags, None, eDVBDB)
eDVBDB.removeServices = new_instancemethod(_enigma.eDVBDB_removeServices, None, eDVBDB)
eDVBDB.removeService = new_instancemethod(_enigma.eDVBDB_removeService, None, eDVBDB)
eDVBDB.addFlag = new_instancemethod(_enigma.eDVBDB_addFlag, None, eDVBDB)
eDVBDB.removeFlag = new_instancemethod(_enigma.eDVBDB_removeFlag, None, eDVBDB)
eDVBDB.readSatellites = new_instancemethod(_enigma.eDVBDB_readSatellites, None, eDVBDB)
eDVBDB.readTerrestrials = new_instancemethod(_enigma.eDVBDB_readTerrestrials, None, eDVBDB)
eDVBDB.readCables = new_instancemethod(_enigma.eDVBDB_readCables, None, eDVBDB)
eDVBDB.loadServicelist = new_instancemethod(_enigma.eDVBDB_loadServicelist, None, eDVBDB)
eDVBDB.reloadServicelist = new_instancemethod(_enigma.eDVBDB_reloadServicelist, None, eDVBDB)
eDVBDB.saveServicelist = new_instancemethod(_enigma.eDVBDB_saveServicelist, None, eDVBDB)
eDVBDB.reloadBouquets = new_instancemethod(_enigma.eDVBDB_reloadBouquets, None, eDVBDB)
eDVBDB.parseServiceData = new_instancemethod(_enigma.eDVBDB_parseServiceData, None, eDVBDB)
eDVBDB_swigregister = _enigma.eDVBDB_swigregister
eDVBDB_swigregister(eDVBDB)

def eDVBDB_getInstance():
    return _enigma.eDVBDB_getInstance()


eDVBDB_getInstance = _enigma.eDVBDB_getInstance

class ePicLoad(eMainloop, iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    PictureData = _swig_property(_enigma.ePicLoad_PictureData_get)

    def __init__(self):
        _enigma.ePicLoad_swiginit(self, _enigma.new_ePicLoad())

    __swig_destroy__ = _enigma.delete_ePicLoad


ePicLoad.waitFinished = new_instancemethod(_enigma.ePicLoad_waitFinished, None, ePicLoad)
ePicLoad.startDecode = new_instancemethod(_enigma.ePicLoad_startDecode, None, ePicLoad)
ePicLoad.getThumbnail = new_instancemethod(_enigma.ePicLoad_getThumbnail, None, ePicLoad)
ePicLoad.setPara = new_instancemethod(_enigma.ePicLoad_setPara, None, ePicLoad)
ePicLoad.getInfo = new_instancemethod(_enigma.ePicLoad_getInfo, None, ePicLoad)
ePicLoad.getData = new_instancemethod(_enigma.ePicLoad_getData, None, ePicLoad)
ePicLoad_swigregister = _enigma.ePicLoad_swigregister
ePicLoad_swigregister(ePicLoad)

def loadPic(*args):
    return _enigma.loadPic(*args)


loadPic = _enigma.loadPic

class FCCServiceChannels(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.FCCServiceChannels_swiginit(self, _enigma.new_FCCServiceChannels())

    __swig_destroy__ = _enigma.delete_FCCServiceChannels


FCCServiceChannels.addFCCService = new_instancemethod(_enigma.FCCServiceChannels_addFCCService, None, FCCServiceChannels)
FCCServiceChannels.removeFCCService = new_instancemethod(_enigma.FCCServiceChannels_removeFCCService, None, FCCServiceChannels)
FCCServiceChannels.getFCCChannelID = new_instancemethod(_enigma.FCCServiceChannels_getFCCChannelID, None, FCCServiceChannels)
FCCServiceChannels_swigregister = _enigma.FCCServiceChannels_swigregister
FCCServiceChannels_swigregister(FCCServiceChannels)

class FCCServiceElem(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    m_service_reference = _swig_property(_enigma.FCCServiceElem_m_service_reference_get, _enigma.FCCServiceElem_m_service_reference_set)
    m_service_event_conn = _swig_property(_enigma.FCCServiceElem_m_service_event_conn_get, _enigma.FCCServiceElem_m_service_event_conn_set)
    m_state = _swig_property(_enigma.FCCServiceElem_m_state_get, _enigma.FCCServiceElem_m_state_set)
    m_useNormalDecode = _swig_property(_enigma.FCCServiceElem_m_useNormalDecode_get, _enigma.FCCServiceElem_m_useNormalDecode_set)

    def __init__(self):
        _enigma.FCCServiceElem_swiginit(self, _enigma.new_FCCServiceElem())

    __swig_destroy__ = _enigma.delete_FCCServiceElem


FCCServiceElem_swigregister = _enigma.FCCServiceElem_swigregister
FCCServiceElem_swigregister(FCCServiceElem)

class eFCCServiceManager(iObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    m_fcc_event = _swig_property(_enigma.eFCCServiceManager_m_fcc_event_get)
    getInstance = staticmethod(_enigma.eFCCServiceManager_getInstance)

    def __init__(self, *args):
        _enigma.eFCCServiceManager_swiginit(self, _enigma.new_eFCCServiceManager(*args))

    __swig_destroy__ = _enigma.delete_eFCCServiceManager
    fcc_state_preparing = _enigma.eFCCServiceManager_fcc_state_preparing
    fcc_state_decoding = _enigma.eFCCServiceManager_fcc_state_decoding
    fcc_state_failed = _enigma.eFCCServiceManager_fcc_state_failed
    getFCCChannelID = staticmethod(_enigma.eFCCServiceManager_getFCCChannelID)
    checkAvailable = staticmethod(_enigma.eFCCServiceManager_checkAvailable)


eFCCServiceManager.playFCCService = new_instancemethod(_enigma.eFCCServiceManager_playFCCService, None, eFCCServiceManager)
eFCCServiceManager.stopFCCService = new_instancemethod(_enigma.eFCCServiceManager_stopFCCService, None, eFCCServiceManager)
eFCCServiceManager.cleanupFCCService = new_instancemethod(_enigma.eFCCServiceManager_cleanupFCCService, None, eFCCServiceManager)
eFCCServiceManager.tryFCCService = new_instancemethod(_enigma.eFCCServiceManager_tryFCCService, None, eFCCServiceManager)
eFCCServiceManager.isLocked = new_instancemethod(_enigma.eFCCServiceManager_isLocked, None, eFCCServiceManager)
eFCCServiceManager.getFCCServiceList = new_instancemethod(_enigma.eFCCServiceManager_getFCCServiceList, None, eFCCServiceManager)
eFCCServiceManager.printFCCServices = new_instancemethod(_enigma.eFCCServiceManager_printFCCServices, None, eFCCServiceManager)
eFCCServiceManager.setFCCEnable = new_instancemethod(_enigma.eFCCServiceManager_setFCCEnable, None, eFCCServiceManager)
eFCCServiceManager.isEnable = new_instancemethod(_enigma.eFCCServiceManager_isEnable, None, eFCCServiceManager)
eFCCServiceManager.isStateDecoding = new_instancemethod(_enigma.eFCCServiceManager_isStateDecoding, None, eFCCServiceManager)
eFCCServiceManager.setNormalDecoding = new_instancemethod(_enigma.eFCCServiceManager_setNormalDecoding, None, eFCCServiceManager)
eFCCServiceManager_swigregister = _enigma.eFCCServiceManager_swigregister
eFCCServiceManager_swigregister(eFCCServiceManager)

def eFCCServiceManager_getInstance():
    return _enigma.eFCCServiceManager_getInstance()


eFCCServiceManager_getInstance = _enigma.eFCCServiceManager_getInstance

def eFCCServiceManager_getFCCChannelID(*args):
    return _enigma.eFCCServiceManager_getFCCChannelID(*args)


eFCCServiceManager_getFCCChannelID = _enigma.eFCCServiceManager_getFCCChannelID

def eFCCServiceManager_checkAvailable(*args):
    return _enigma.eFCCServiceManager_checkAvailable(*args)


eFCCServiceManager_checkAvailable = _enigma.eFCCServiceManager_checkAvailable

class PSignal0V(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.PSignal0V_swiginit(self, _enigma.new_PSignal0V())

    __swig_destroy__ = _enigma.delete_PSignal0V


PSignal0V.get = new_instancemethod(_enigma.PSignal0V_get, None, PSignal0V)
PSignal0V_swigregister = _enigma.PSignal0V_swigregister
PSignal0V_swigregister(PSignal0V)

class PSignal1VI(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.PSignal1VI_swiginit(self, _enigma.new_PSignal1VI())

    __swig_destroy__ = _enigma.delete_PSignal1VI


PSignal1VI.get = new_instancemethod(_enigma.PSignal1VI_get, None, PSignal1VI)
PSignal1VI_swigregister = _enigma.PSignal1VI_swigregister
PSignal1VI_swigregister(PSignal1VI)

class PSignal1VS(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.PSignal1VS_swiginit(self, _enigma.new_PSignal1VS())

    __swig_destroy__ = _enigma.delete_PSignal1VS


PSignal1VS.get = new_instancemethod(_enigma.PSignal1VS_get, None, PSignal1VS)
PSignal1VS_swigregister = _enigma.PSignal1VS_swigregister
PSignal1VS_swigregister(PSignal1VS)

class PSignal1VoidICECMessage(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.PSignal1VoidICECMessage_swiginit(self, _enigma.new_PSignal1VoidICECMessage())

    __swig_destroy__ = _enigma.delete_PSignal1VoidICECMessage


PSignal1VoidICECMessage.get = new_instancemethod(_enigma.PSignal1VoidICECMessage_get, None, PSignal1VoidICECMessage)
PSignal1VoidICECMessage_swigregister = _enigma.PSignal1VoidICECMessage_swigregister
PSignal1VoidICECMessage_swigregister(PSignal1VoidICECMessage)

class PSignal2VoidIRecordableServiceInt(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.PSignal2VoidIRecordableServiceInt_swiginit(self, _enigma.new_PSignal2VoidIRecordableServiceInt())

    __swig_destroy__ = _enigma.delete_PSignal2VoidIRecordableServiceInt


PSignal2VoidIRecordableServiceInt.get = new_instancemethod(_enigma.PSignal2VoidIRecordableServiceInt_get, None, PSignal2VoidIRecordableServiceInt)
PSignal2VoidIRecordableServiceInt_swigregister = _enigma.PSignal2VoidIRecordableServiceInt_swigregister
PSignal2VoidIRecordableServiceInt_swigregister(PSignal2VoidIRecordableServiceInt)

class PSignal2VII(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _enigma.PSignal2VII_swiginit(self, _enigma.new_PSignal2VII())

    __swig_destroy__ = _enigma.delete_PSignal2VII


PSignal2VII.get = new_instancemethod(_enigma.PSignal2VII_get, None, PSignal2VII)
PSignal2VII_swigregister = _enigma.PSignal2VII_swigregister
PSignal2VII_swigregister(PSignal2VII)

def getBestPlayableServiceReference(*args):
    return _enigma.getBestPlayableServiceReference(*args)


getBestPlayableServiceReference = _enigma.getBestPlayableServiceReference

def setTunerTypePriorityOrder(*args):
    return _enigma.setTunerTypePriorityOrder(*args)


setTunerTypePriorityOrder = _enigma.setTunerTypePriorityOrder

def setPreferredTuner(*args):
    return _enigma.setPreferredTuner(*args)


setPreferredTuner = _enigma.setPreferredTuner

def setEnableTtCachingOnOff(*args):
    return _enigma.setEnableTtCachingOnOff(*args)


setEnableTtCachingOnOff = _enigma.setEnableTtCachingOnOff

def getLinkedSlotID(*args):
    return _enigma.getLinkedSlotID(*args)


getLinkedSlotID = _enigma.getLinkedSlotID

def setFCCEnable(*args):
    return _enigma.setFCCEnable(*args)


setFCCEnable = _enigma.setFCCEnable

def isFBCLink(*args):
    return _enigma.isFBCLink(*args)


isFBCLink = _enigma.isFBCLink

def addFont(*args):
    return _enigma.addFont(*args)


addFont = _enigma.addFont

def getPrevAsciiCode():
    return _enigma.getPrevAsciiCode()


getPrevAsciiCode = _enigma.getPrevAsciiCode

def runMainloop():
    return _enigma.runMainloop()


runMainloop = _enigma.runMainloop

def quitMainloop(*args):
    return _enigma.quitMainloop(*args)


quitMainloop = _enigma.quitMainloop

def getApplication():
    return _enigma.getApplication()


getApplication = _enigma.getApplication

def getEnigmaVersionString():
    return _enigma.getEnigmaVersionString()


getEnigmaVersionString = _enigma.getEnigmaVersionString

def getVTiVersionString():
    return _enigma.getVTiVersionString()


getVTiVersionString = _enigma.getVTiVersionString

def dump_malloc_stats():
    return _enigma.dump_malloc_stats()


dump_malloc_stats = _enigma.dump_malloc_stats

def setAnimation_current(*args):
    return _enigma.setAnimation_current(*args)


setAnimation_current = _enigma.setAnimation_current

def setAnimation_speed(*args):
    return _enigma.setAnimation_speed(*args)


setAnimation_speed = _enigma.setAnimation_speed

def setAnimation_current_listbox(*args):
    return _enigma.setAnimation_current_listbox(*args)


setAnimation_current_listbox = _enigma.setAnimation_current_listbox
