# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.oauth.v1 import V1


class Oauth(Domain):

    def __init__(self, twilio):
        """
        Initialize the Oauth Domain

        :returns: Domain for Oauth
        :rtype: twilio.rest.oauth.Oauth
        """
        super(Oauth, self).__init__(twilio)

        self.base_url = 'https://oauth.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of oauth
        :rtype: twilio.rest.oauth.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def oauth(self):
        """
        :rtype: twilio.rest.oauth.v1.oauth.OauthList
        """
        return self.v1.oauth

    @property
    def openid_discovery(self):
        """
        :rtype: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryList
        """
        return self.v1.openid_discovery

    @property
    def token(self):
        """
        :rtype: twilio.rest.oauth.v1.token.TokenList
        """
        return self.v1.token

    @property
    def user_info(self):
        """
        :rtype: twilio.rest.oauth.v1.user_info.UserInfoList
        """
        return self.v1.user_info

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Oauth>'
