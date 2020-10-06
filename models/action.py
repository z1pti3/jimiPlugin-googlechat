import requests
import json
from pathlib import Path

from core.models import action
from core import helpers

# Based on jimi API plugin
class _googlechatWebHook(action._action):
	url = str()
	body = str()
	timeout = int()
	proxy = dict()
	ca = str()

	def run(self,data,persistentData,actionResult):
		headers = { "Content-Type": "application/json; charset=UTF-8" }
		url = helpers.evalString(self.url,{"data" : data})
		body = helpers.evalString(self.body,{"data" : data})

		timeout = 60
		if self.timeout > 0:
			timeout = self.timeout

		kwargs={}
		kwargs["headers"] = headers
		kwargs["timeout"] = timeout
		kwargs["data"] = json.dumps({"text" : body })
		if self.ca:
			kwargs["verify"] == Path(self.ca)
		if self.proxy:
			kwargs["proxies"] = self.proxy

		response = requests.post(url,**kwargs)

		actionResult["result"] = True
		actionResult["rc"] = response.status_code
		actionResult["data"] = { "headers" : response.headers, "text" : response.text }
		return actionResult
