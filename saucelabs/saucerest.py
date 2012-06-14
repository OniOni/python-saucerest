import base64
import httplib
import json

class SauceRest(object):
    """
    """
    
    def __init__(self, username, password, host="saucelabs.com", api="/rest/v1"):
        """
        
        Arguments:
        - `username`:
        - `password`:
        """
        self._username = username
        self._password = password
        self._host = host
        self._api = api
        self._base_url = 'https://%s/%s' % (host, api)

        self.base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
        
    def account_details(self):
        return self.rest(
            url="/users/%s" % self._username
            )


    def account_limits(self):
        return self.rest(
            url="/%s/limits" % self._username
            )

    def account_activity(self):
        return self.rest(
            url="/%s/activity" % self._username
            )

    def account_usage(self):
        return self.rest(
            url="/users/%s/usage" % self._username
            )

    def list_jobs(self, full=True):
        return self.rest(
            url="/%s/jobs%s" % (self._username, "?full=true" if full else "")
            )

    def show_job(self, id):
        return self.rest(
            url="/%s/jobs/%s" % (self._username, id)
            )

    def update_job(self, id, data):
        return self.rest(
            url="/%s/jobs/%s" % (self._username, id),
            method='PUT',
            data=data
            )

    def stop_job(self, id, data):
        return self.rest(
            url="/%s/jobs/%s/stop" % (self._username, id),
            method='PUT',
            data=data
            )

    def list_tunnels(self):
        return self.rest(
            url="/%s/tunnels" % self._username
            )

    def show_tunnel(self, id):
        return self.rest(
            url="/%s/tunnels/%s" % (self._username, id)
            )

    def delete_tunnel(self, id):
        return self.rest(
            url="/%s/tunnels/%s" % (self._username, id),
            method="DELETE"
            )

    def sauce_status(self):
        return self.rest(
            url="/info/status"
            )

    def sauce_browsers(self):
        return self.rest(
            url="/info/browsers"
            )

    def sauce_counter(self):
        return self.rest(
            url="/info/counter"
            )

    def create_subaccount(self, data):
        return self.rest(
            url="/users/%s" % self._username,
            method='POST',
            data=data
            )
    
    def update_subaccount(self, sub, data):
        return self.rest(
            url="/users/%s/subscription" % sub,
            method='POST',
            data=data
            )

    def unsubscribe_subaccount(self, sub):
        return self.rest(
            url="/users/%s/subscription" % sub,
            method='POST'
            )

    def rest(self, url, method='GET', data=None):
        ret= False
        connection =  httplib.HTTPSConnection(self._host)

        if (data != None):
            data = json.dumps(data)
        
        headers = {"Authorization": "Basic %s" % self.base64string,
                   "Content-type": "application/json"}

        connection.request(method, self._api + url, data, headers)
        res = connection.getresponse()

        if (res.status / 100 == 2):
            try:
                ret = json.loads(res.read())
            except Exception as e:
                ret = (False, e)
        else:
            ret = (False, res.status, res.reason)
            
        connection.close()

        return ret

if __name__ == '__main__':
    sauce = SauceRest(
        username="sauce-username",
        password="sauce-access-key",
        )
    
    print "\033[33mAccount details:\033[0m\n%s\n" % repr(sauce.account_details())
    print "\033[33mAccount limits:\033[0m\n%s\n" % repr(sauce.account_limits())
    print "\033[33mAccount activity:\033[0m\n%s\n" % repr(sauce.account_activity())
    print "\033[33mAccount usage:\033[0m\n%s\n" % repr(sauce.account_usage())
    print "\033[33mRan %s jobs\033[0m\n" % repr(len(sauce.list_jobs(full=False)))
    print "\033[33mJob 1:\033[0m\n%s\n" % repr(sauce.show_job(sauce.list_jobs(full=False)[1]['id']))
    print "\033[33mShow job 1:\033[0m\n%s\n" % repr(sauce.update_job(sauce.list_jobs(full=False)[1]['id'], {'name': 'updated_job'}))
    print "\033[33mUpate job 1:\033[0m\n%s\n" % repr(sauce.show_job(sauce.list_jobs(full=False)[1]['id']))
    print "\033[33mList tunnels:\033[0m\n%s\n" % repr(sauce.list_tunnels())
    print "\033[33mSauce status:\033[0m\n%s\n" % repr(sauce.sauce_status())
    print "\033[33m10 first Sauce browsers/os combinations:\033[0m\n%s\n" % repr([b for b in sauce.sauce_browsers()[:10]])
    print "\033[33m10%s tests have been run at sauce.\033[0m\n\n" % repr(sauce.sauce_counter())

