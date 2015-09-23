# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource
from twilio.rest.v2010.account.incoming_phone_number.local import LocalList
from twilio.rest.v2010.account.incoming_phone_number.mobile import MobileList
from twilio.rest.v2010.account.incoming_phone_number.toll_free import TollFreeList


class IncomingPhoneNumberList(ListResource):

    def __init__(self, domain, owner_account_sid):
        super(IncomingPhoneNumberList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'owner_account_sid': owner_account_sid,
        }
        self._uri = "/Accounts/{owner_account_sid}/IncomingPhoneNumbers.json".format(**self._instance_kwargs)
        
        # Components
        self._local = None
        self._mobile = None
        self._toll_free = None

    def read(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({
            "Beta": beta,
            "FriendlyName": friendly_name,
            "PhoneNumber": phone_number,
        })
        params.update(kwargs)
        
        return self._domain.read(
            self,
            IncomingPhoneNumberInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            "Beta": beta,
            "FriendlyName": friendly_name,
            "PhoneNumber": phone_number,
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            IncomingPhoneNumberInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, api_version=values.unset, friendly_name=values.unset,
               sms_application_sid=values.unset, sms_fallback_method=values.unset,
               sms_fallback_url=values.unset, sms_method=values.unset,
               sms_url=values.unset, status_callback=values.unset,
               status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset,
               phone_number=values.unset, area_code=values.unset):
        data = values.of({
            "PhoneNumber": phone_number,
            "AreaCode": area_code,
            "ApiVersion": api_version,
            "FriendlyName": friendly_name,
            "SmsApplicationSid": sms_application_sid,
            "SmsFallbackMethod": sms_fallback_method,
            "SmsFallbackUrl": sms_fallback_url,
            "SmsMethod": sms_method,
            "SmsUrl": sms_url,
            "StatusCallback": status_callback,
            "StatusCallbackMethod": status_callback_method,
            "VoiceApplicationSid": voice_application_sid,
            "VoiceCallerIdLookup": voice_caller_id_lookup,
            "VoiceFallbackMethod": voice_fallback_method,
            "VoiceFallbackUrl": voice_fallback_url,
            "VoiceMethod": voice_method,
            "VoiceUrl": voice_url,
        })
        
        return self._domain.create(
            IncomingPhoneNumberInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def local(self):
        if self._local is None:
            self._local = LocalList(self._domain, **self._instance_kwargs)
        return self._local

    @property
    def mobile(self):
        if self._mobile is None:
            self._mobile = MobileList(self._domain, **self._instance_kwargs)
        return self._mobile

    @property
    def toll_free(self):
        if self._toll_free is None:
            self._toll_free = TollFreeList(self._domain, **self._instance_kwargs)
        return self._toll_free


class IncomingPhoneNumberContext(InstanceContext):

    def __init__(self, domain, owner_account_sid, sid):
        super(IncomingPhoneNumberContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'owner_account_sid': owner_account_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{owner_account_sid}/IncomingPhoneNumbers/{sid}.json".format(**self._instance_kwargs)

    def update(self, account_sid=values.unset, api_version=values.unset,
               friendly_name=values.unset, sms_application_sid=values.unset,
               sms_fallback_method=values.unset, sms_fallback_url=values.unset,
               sms_method=values.unset, sms_url=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset):
        data = values.of({
            "AccountSid": account_sid,
            "ApiVersion": api_version,
            "FriendlyName": friendly_name,
            "SmsApplicationSid": sms_application_sid,
            "SmsFallbackMethod": sms_fallback_method,
            "SmsFallbackUrl": sms_fallback_url,
            "SmsMethod": sms_method,
            "SmsUrl": sms_url,
            "StatusCallback": status_callback,
            "StatusCallbackMethod": status_callback_method,
            "VoiceApplicationSid": voice_application_sid,
            "VoiceCallerIdLookup": voice_caller_id_lookup,
            "VoiceFallbackMethod": voice_fallback_method,
            "VoiceFallbackUrl": voice_fallback_url,
            "VoiceMethod": voice_method,
            "VoiceUrl": voice_url,
        })
        
        return self._domain.update(
            IncomingPhoneNumberInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def fetch(self):
        params = values.of({})
        
        return self._domain.fetch(
            IncomingPhoneNumberInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._domain.delete("delete", self._uri)


class IncomingPhoneNumberInstance(InstanceResource):

    def __init__(self, domain, payload, owner_account_sid, sid=None):
        super(IncomingPhoneNumberInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._address_requirements = payload['address_requirements']
        self._api_version = payload['api_version']
        self._beta = payload['beta']
        self._capabilities = payload['capabilities']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._friendly_name = payload['friendly_name']
        self._phone_number = payload['phone_number']
        self._sid = payload['sid']
        self._sms_application_sid = payload['sms_application_sid']
        self._sms_fallback_method = payload['sms_fallback_method']
        self._sms_fallback_url = payload['sms_fallback_url']
        self._sms_method = payload['sms_method']
        self._sms_url = payload['sms_url']
        self._status_callback = payload['status_callback']
        self._status_callback_method = payload['status_callback_method']
        self._uri = payload['uri']
        self._voice_application_sid = payload['voice_application_sid']
        self._voice_caller_id_lookup = payload['voice_caller_id_lookup']
        self._voice_fallback_method = payload['voice_fallback_method']
        self._voice_fallback_url = payload['voice_fallback_url']
        self._voice_method = payload['voice_method']
        self._voice_url = payload['voice_url']
        
        # Context
        self._lazy_context = None
        self._context_owner_account_sid = owner_account_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = IncomingPhoneNumberContext(
                self._domain,
                self._context_owner_account_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The unique sid that identifies this account """
        return self._account_sid

    @property
    def address_requirements(self):
        """ Indicates if the customer requires an address """
        return self._address_requirements

    @property
    def api_version(self):
        """ The Twilio REST API version to use """
        return self._api_version

    @property
    def beta(self):
        """ Indicates if the phone number is a beta number """
        return self._beta

    @property
    def capabilities(self):
        """ Indicate if a phone can receive calls or messages """
        return self._capabilities

    @property
    def date_created(self):
        """ The date this resource was created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date this resource was last updated """
        return self._date_updated

    @property
    def friendly_name(self):
        """ A human readable description of this resouce """
        return self._friendly_name

    @property
    def phone_number(self):
        """ The incoming phone number """
        return self._phone_number

    @property
    def sid(self):
        """ A string that uniquely identifies this resource """
        return self._sid

    @property
    def sms_application_sid(self):
        """ Unique string that identifies the application """
        return self._sms_application_sid

    @property
    def sms_fallback_method(self):
        """ HTTP method used with sms fallback url """
        return self._sms_fallback_method

    @property
    def sms_fallback_url(self):
        """ URL Twilio will request if an error occurs in executing TwiML """
        return self._sms_fallback_url

    @property
    def sms_method(self):
        """ HTTP method to use with sms url """
        return self._sms_method

    @property
    def sms_url(self):
        """ URL Twilio will request when receiving an SMS """
        return self._sms_url

    @property
    def status_callback(self):
        """ URL Twilio will use to pass status parameters """
        return self._status_callback

    @property
    def status_callback_method(self):
        """ HTTP method twilio will use with status callback """
        return self._status_callback_method

    @property
    def uri(self):
        """ The URI for this resource """
        return self._uri

    @property
    def voice_application_sid(self):
        """ The unique sid of the application to handle this number """
        return self._voice_application_sid

    @property
    def voice_caller_id_lookup(self):
        """ Look up the caller's caller-ID """
        return self._voice_caller_id_lookup

    @property
    def voice_fallback_method(self):
        """ HTTP method used with fallback_url """
        return self._voice_fallback_method

    @property
    def voice_fallback_url(self):
        """ URL Twilio will request when an error occurs in TwiML """
        return self._voice_fallback_url

    @property
    def voice_method(self):
        """ HTTP method used with the voice url """
        return self._voice_method

    @property
    def voice_url(self):
        """ URL Twilio will request when receiving a call """
        return self._voice_url

    def update(self, account_sid=values.unset, api_version=values.unset,
               friendly_name=values.unset, sms_application_sid=values.unset,
               sms_fallback_method=values.unset, sms_fallback_url=values.unset,
               sms_method=values.unset, sms_url=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset):
        self._context.update(
            account_sid=account_sid,
            api_version=api_version,
            friendly_name=friendly_name,
            sms_application_sid=sms_application_sid,
            sms_fallback_method=sms_fallback_method,
            sms_fallback_url=sms_fallback_url,
            sms_method=sms_method,
            sms_url=sms_url,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            voice_application_sid=voice_application_sid,
            voice_caller_id_lookup=voice_caller_id_lookup,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
        )

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()
