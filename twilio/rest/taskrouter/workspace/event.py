# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest import serialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class EventList(ListResource):

    def __init__(self, domain, workspace_sid):
        super(EventList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Events".format(**self._instance_kwargs)

    def read(self, end_date=values.unset, event_type=values.unset,
             minutes=values.unset, reservation_sid=values.unset,
             start_date=values.unset, task_queue_sid=values.unset,
             task_sid=values.unset, worker_sid=values.unset,
             workflow_sid=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({
            "EndDate": serialize.iso8601_date(end_date),
            "EventType": event_type,
            "Minutes": minutes,
            "ReservationSid": reservation_sid,
            "StartDate": serialize.iso8601_date(start_date),
            "TaskQueueSid": task_queue_sid,
            "TaskSid": task_sid,
            "WorkerSid": worker_sid,
            "WorkflowSid": workflow_sid,
        })
        params.update(kwargs)
        
        return self._domain.read(
            self,
            EventInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, end_date=values.unset, event_type=values.unset,
             minutes=values.unset, reservation_sid=values.unset,
             start_date=values.unset, task_queue_sid=values.unset,
             task_sid=values.unset, worker_sid=values.unset,
             workflow_sid=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            "EndDate": serialize.iso8601_date(end_date),
            "EventType": event_type,
            "Minutes": minutes,
            "ReservationSid": reservation_sid,
            "StartDate": serialize.iso8601_date(start_date),
            "TaskQueueSid": task_queue_sid,
            "TaskSid": task_sid,
            "WorkerSid": worker_sid,
            "WorkflowSid": workflow_sid,
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            EventInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )


class EventContext(InstanceContext):

    def __init__(self, domain, workspace_sid, sid):
        super(EventContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Events/{sid}".format(**self._instance_kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._domain.fetch(
            EventInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )


class EventInstance(InstanceResource):

    def __init__(self, domain, payload, workspace_sid, sid=None):
        super(EventInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._actor_sid = payload['actor_sid']
        self._actor_type = payload['actor_type']
        self._actor_url = payload['actor_url']
        self._description = payload['description']
        self._event_data = payload['event_data']
        self._event_date = deserialize.iso8601_datetime(payload['event_date'])
        self._event_type = payload['event_type']
        self._resource_sid = payload['resource_sid']
        self._resource_type = payload['resource_type']
        self._resource_url = payload['resource_url']
        self._sid = payload['sid']
        self._source = payload['source']
        self._source_ip_address = payload['source_ip_address']
        self._url = payload['url']
        
        # Context
        self._lazy_context = None
        self._context_workspace_sid = workspace_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = EventContext(
                self._domain,
                self._context_workspace_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._account_sid

    @property
    def actor_sid(self):
        """ The actor_sid """
        return self._actor_sid

    @property
    def actor_type(self):
        """ The actor_type """
        return self._actor_type

    @property
    def actor_url(self):
        """ The actor_url """
        return self._actor_url

    @property
    def description(self):
        """ The description """
        return self._description

    @property
    def event_data(self):
        """ The event_data """
        return self._event_data

    @property
    def event_date(self):
        """ The event_date """
        return self._event_date

    @property
    def event_type(self):
        """ The event_type """
        return self._event_type

    @property
    def resource_sid(self):
        """ The resource_sid """
        return self._resource_sid

    @property
    def resource_type(self):
        """ The resource_type """
        return self._resource_type

    @property
    def resource_url(self):
        """ The resource_url """
        return self._resource_url

    @property
    def sid(self):
        """ The sid """
        return self._sid

    @property
    def source(self):
        """ The source """
        return self._source

    @property
    def source_ip_address(self):
        """ The source_ip_address """
        return self._source_ip_address

    @property
    def url(self):
        """ The url """
        return self._url

    def fetch(self):
        self._context.fetch()
