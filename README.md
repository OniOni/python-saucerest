# python-saucerest -- Python wrapper around the Saucelabs REST API

## Install

Make sure you have python and pip.

Go ahead and install python-saucerest
```shell
pip install python-saucerest
```

## Writting a script

```python
import saucelabs.saucerest as saucerest

sauce = saucerest.SauceRest(
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
```

## Supported Methods

<table class="wikitable" width="90%" style="padding: 5%;">
  <tbody>
    <tr >
      <td width="50%"><strong>Rest</strong></td>
      <td width="50%"><strong>Node Wrapper</strong></td>
    </tr>
    <tr>
      <td>
	GET /users/:username <br />
	Access account details.
      </td>
      <td>account_details()</td>
    </tr>
    <tr>
      <td>
	GET /:username/limits <br />
	Access account limits
      </td>
      <td> account_limits() </td>
    </tr>
    <tr>
      <td>
	GET /:username/activity <br />
	Access current account activity.
      </td>
      <td>account_activity()</td>
    </tr>
    <tr>
      <td>
	GET /users/:username/usage <br />
	Access historical account usage data.
      </td>
      <td> account_usage()</td>
    </tr>
    <tr>
      <td>
	GET /:username/jobs <br />
	List all job Id's belonging to a given user. 
      </td>
      <td> 
	list_jobs(full=False)  <br />
	full: When true, forces full job information to be returned rather than just Id's.
      </td>
    </tr>
    <tr>
      <td>
	GET /:username/jobs/:id <br />
	Show the full information for a job given its ID. 
      </td>
      <td>show_job(id)</td>
    </tr>
    <tr>
      <td>
	PUT /:username/jobs/:id <br />
	Changes a pre-existing job. 
      </td>
      <td>update_job(id, data)</td>
    </tr>
    <tr>
      <td>
	PUT /:username/jobs/:id/stop <br />
	Terminates a running job. 
      </td>
      <td> stop_job(id, data) </td>
    </tr>
    <tr>
      <td>
	GET /:username/tunnels <br />
	Retrieves all running tunnels for a given user. 
      </td>
      <td>list_tunnels()</td>
    </tr>
    <tr>
      <td>
	GET /:username/tunnels/:id <br />
	Show the full information for a tunnel given its ID. 
      </td>
      <td>show_tunnel(id)</td>
    </tr>
    <tr>
      <td>
	DELETE /:username/tunnels/:id <br />
	Shuts down a tunnel given its ID. 
      </td>
      <td>delete_tunnel(id)</td> <br />
    </tr>
    <tr>
      <td>
	GET /info/status <br />
	Returns the current status of Sauce Labs' services. 
      </td>
      <td>sauce_status()</td>
    </tr>
    <tr>
      <td>
	GET /info/browsers <br />
	Returns an array of strings corresponding to all the browsers currently supported on Sauce Labs. 
      </td>
      <td>sauce_browsers()</td>
    </tr>
    <tr>
      <td>
	GET /info/counter <br />
	Returns the number of test executed so far on Sauce Labs. 
      </td>
      <td>sauce_counter()</td>
    </tr>
    <tr>
      <td>
	POST /users/:id <br />
	Create a new sub-account.
      </td>
      <td> 
      	create_subaccount(data) <br />
	data (dict): Information about your new subaccount <br />
	See saucerest <a href="http://saucelabs.com/docs/saucerest#partners">docs</a> for more information.
      </td>
    </tr>
    <tr>
      <td>
	POST /users/:id/subscription <br />
	Update a sub-account Sauce Labs service plan.
      </td>
      <td> 
      	update_subaccount(data)
	data (dict): Plan information
	See saucerest <a href="http://saucelabs.com/docs/saucerest#partners">docs</a> for more information.
      </td>
    </tr>
    <tr>
      <td>
	DELETE /users/:id/subscription <br />
	Unsubscribe a sub-account from it's Sauce Labs service plan.
      </td>
      <td> unsubscribe_subaccount() </td>
    </tr>
  </tbody>
</table>
	
## More Documentation

Check out the [Sauce REST API](http://saucelabs.com/docs/saucerest)
for more information
