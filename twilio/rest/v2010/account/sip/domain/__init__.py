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
from twilio.rest.v2010.account.sip.domain.credential_list_mapping import CredentialListMappingList
from twilio.rest.v2010.account.sip.domain.ip_access_control_list_mapping import IpAccessControlListMappingList


class DomainList(ListResource):

    def __init__(self, domain, account_sid):
        super(DomainList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/Domains.json".format(**self._instance_kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({})
        params.update(kwargs)
        
        return self._domain.read(
            self,
            DomainInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            DomainInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, domain_name, friendly_name=values.unset,
               voice_url=values.unset, voice_method=values.unset,
               voice_fallback_url=values.unset, voice_fallback_method=values.unset,
               voice_status_callback_url=values.unset,
               voice_status_callback_method=values.unset):
        data = values.of({
            "DomainName": domain_name,
            "FriendlyName": friendly_name,
            "VoiceUrl": voice_url,
            "VoiceMethod": voice_method,
            "VoiceFallbackUrl": voice_fallback_url,
            "VoiceFallbackMethod": voice_fallback_method,
            "VoiceStatusCallbackUrl": voice_status_callback_url,
            "VoiceStatusCallbackMethod": voice_status_callback_method,
        })
        
        return self._domain.create(
            DomainInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )


class DomainContext(InstanceContext):

    def __init__(self, domain, account_sid, sid):
        super(DomainContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/Domains/{sid}.json".format(**self._instance_kwargs)
        
        # Dependents
        self._ip_access_control_list_mappings = None
        self._credential_list_mappings = None

    def fetch(self):
        params = values.of({})
        
        return self._domain.fetch(
            DomainInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, api_version=values.unset, friendly_name=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_status_callback_method=values.unset,
               voice_status_callback_url=values.unset, voice_url=values.unset):
        data = values.of({
            "ApiVersion": api_version,
            "FriendlyName": friendly_name,
            "VoiceFallbackMethod": voice_fallback_method,
            "VoiceFallbackUrl": voice_fallback_url,
            "VoiceMethod": voice_method,
            "VoiceStatusCallbackMethod": voice_status_callback_method,
            "VoiceStatusCallbackUrl": voice_status_callback_url,
            "VoiceUrl": voice_url,
        })
        
        return self._domain.update(
            DomainInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._domain.delete("delete", self._uri)

    @property
    def ip_access_control_list_mappings(self):
        if self._ip_access_control_list_mappings is None:
            self._ip_access_control_list_mappings = IpAccessControlListMappingList(
                self._domain,
                account_sid=self._instance_kwargs['account_sid'],
                domain_sid=self._instance_kwargs['sid'],
            )
        return self._ip_access_control_list_mappings

    @property
    def credential_list_mappings(self):
        if self._credential_list_mappings is None:
            self._credential_list_mappings = CredentialListMappingList(
                self._domain,
                account_sid=self._instance_kwargs['account_sid'],
                domain_sid=self._instance_kwargs['sid'],
            )
        return self._credential_list_mappings


class DomainInstance(InstanceResource):

    def __init__(self, domain, payload, account_sid, sid=None):
        super(DomainInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._api_version = payload['api_version']
        self._auth_type = payload['auth_type']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._domain_name = payload['domain_name']
        self._friendly_name = payload['friendly_name']
        self._sid = payload['sid']
        self._uri = payload['uri']
        self._voice_fallback_method = payload['voice_fallback_method']
        self._voice_fallback_url = payload['voice_fallback_url']
        self._voice_method = payload['voice_method']
        self._voice_status_callback_method = payload['voice_status_callback_method']
        self._voice_status_callback_url = payload['voice_status_callback_url']
        self._voice_url = payload['voice_url']
        
        # Context
        self._lazy_context = None
        self._context_account_sid = account_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = DomainContext(
                self._domain,
                self._context_account_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The unique id of the account that sent the message """
        return self._account_sid

    @property
    def api_version(self):
        """ The Twilio API version used to process the message """
        return self._api_version

    @property
    def auth_type(self):
        """ The types of authentication mapped to the domain """
        return self._auth_type

    @property
    def date_created(self):
        """ The date this resource was created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date this resource was last updated """
        return self._date_updated

    @property
    def domain_name(self):
        """ The unique address on Twilio to route SIP traffic """
        return self._domain_name

    @property
    def friendly_name(self):
        """ A user-specified, human-readable name for the trigger. """
        return self._friendly_name

    @property
    def sid(self):
        """ A string that uniquely identifies the SIP Domain """
        return self._sid

    @property
    def uri(self):
        """ The URI for this resource """
        return self._uri

    @property
    def voice_fallback_method(self):
        """ HTTP method used with voice_fallback_url """
        return self._voice_fallback_method

    @property
    def voice_fallback_url(self):
        """ URL Twilio will request if an error occurs in executing TwiML """
        return self._voice_fallback_url

    @property
    def voice_method(self):
        """ HTTP method to use with voice_url """
        return self._voice_method

    @property
    def voice_status_callback_method(self):
        """ The voice_status_callback_method """
        return self._voice_status_callback_method

    @property
    def voice_status_callback_url(self):
        """ URL that Twilio will request with status updates """
        return self._voice_status_callback_url

    @property
    def voice_url(self):
        """ URL Twilio will request when receiving a call """
        return self._voice_url

    def fetch(self):
        self._context.fetch()

    def update(self, api_version=values.unset, friendly_name=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_status_callback_method=values.unset,
               voice_status_callback_url=values.unset, voice_url=values.unset):
        self._context.update(
            api_version=api_version,
            friendly_name=friendly_name,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_status_callback_method=voice_status_callback_method,
            voice_status_callback_url=voice_status_callback_url,
            voice_url=voice_url,
        )

    def delete(self):
        self._context.delete()
