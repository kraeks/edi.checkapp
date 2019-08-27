from Products.Five import BrowserView
import jsonlib
import json
import hashlib

class ChecklistLogin(BrowserView):

    def __call__(self):
        data = {}
        body = self.request.get('BODY')
        if body:
            body_unicode = self.request.get('BODY').decode('utf-8')
            data = json.loads(body_unicode)
        #self.request.response.setHeader("Content-type", "application/json")
        #self.request.response.setHeader("Access-Control-Allow-Origin", "*")
        datainput = "%s%s" %(data.get('email'), data.get('pin'))
        m = hashlib.md5()
        keyword = m.update(datainput)
        data['keyword'] = m.hexdigest()
        payload = jsonlib.write(data)
        return payload


class ChecklistData(BrowserView):

    def __call__(self):
        data = {}
        body = self.request.get('BODY')
        if body:
            body_unicode = self.request.get('BODY').decode('utf-8')
            data = json.loads(body_unicode)
        self.request.response.setHeader("Content-type", "application/json")
        self.request.response.setHeader("Access-Control-Allow-Origin", "*")
        retdict = data
        payload = jsonlib.write(retdict)
        return payload
