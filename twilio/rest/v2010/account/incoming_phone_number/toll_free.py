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


class TollFreeList(ListResource):

    def __init__(self, domain, owner_account_sid):
        super(TollFreeList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'owner_account_sid': owner_account_sid,
        }
        self._uri = "/Accounts/{owner_account_sid}/IncomingPhoneNumbers/TollFree.json".format(**self._instance_kwargs)

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
            TollFreeInstance,
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
            TollFreeInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, area_code, phone_number, api_version=values.unset,
               friendly_name=values.unset, sms_application_sid=values.unset,
               sms_fallback_method=values.unset, sms_fallback_url=values.unset,
               sms_method=values.unset, sms_url=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset):
        data = values.of({
            "AreaCode": area_code,
            "PhoneNumber": phone_number,
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
            TollFreeInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )


class TollFreeContext(InstanceContext):

    def __init__(self, domain, owner_account_sid, sid):
        super(TollFreeContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'owner_account_sid': owner_account_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{owner_account_sid}/IncomingPhoneNumbers/{sid}.json".format(**self._instance_kwargs)


class TollFreeInstance(InstanceResource):

    def __init__(self, domain, payload, owner_account_sid, sid=None):
        super(TollFreeInstance, self).__init__(domain)
        
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
            self._lazy_context = TollFreeContext(
                self._domain,
                self._context_owner_account_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._account_sid

    @property
    def address_requirements(self):
        """ The address_requirements """
        return self._address_requirements

    @property
    def api_version(self):
        """ The api_version """
        return self._api_version

    @property
    def beta(self):
        """ The beta """
        return self._beta

    @property
    def capabilities(self):
        """ The capabilities """
        return self._capabilities

    @property
    def date_created(self):
        """ The date_created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date_updated """
        return self._date_updated

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._friendly_name

    @property
    def phone_number(self):
        """ The phone_number """
        return self._phone_number

    @property
    def sid(self):
        """ The sid """
        return self._sid

    @property
    def sms_application_sid(self):
        """ The sms_application_sid """
        return self._sms_application_sid

    @property
    def sms_fallback_method(self):
        """ The sms_fallback_method """
        return self._sms_fallback_method

    @property
    def sms_fallback_url(self):
        """ The sms_fallback_url """
        return self._sms_fallback_url

    @property
    def sms_method(self):
        """ The sms_method """
        return self._sms_method

    @property
    def sms_url(self):
        """ The sms_url """
        return self._sms_url

    @property
    def status_callback(self):
        """ The status_callback """
        return self._status_callback

    @property
    def status_callback_method(self):
        """ The status_callback_method """
        return self._status_callback_method

    @property
    def uri(self):
        """ The uri """
        return self._uri

    @property
    def voice_application_sid(self):
        """ The voice_application_sid """
        return self._voice_application_sid

    @property
    def voice_caller_id_lookup(self):
        """ The voice_caller_id_lookup """
        return self._voice_caller_id_lookup

    @property
    def voice_fallback_method(self):
        """ The voice_fallback_method """
        return self._voice_fallback_method

    @property
    def voice_fallback_url(self):
        """ The voice_fallback_url """
        return self._voice_fallback_url

    @property
    def voice_method(self):
        """ The voice_method """
        return self._voice_method

    @property
    def voice_url(self):
        """ The voice_url """
        return self._voice_url
