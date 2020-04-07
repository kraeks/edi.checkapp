# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.pdfbase.ttfonts import TTFont
from Products.Five import BrowserView
from plone.i18n.normalizer import idnormalizer
from plone import api
import requests
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
        datainput = "%s%s" %(data.get('email'), data.get('pin'))
        m = hashlib.md5()
        m.update(datainput)
        keyword = m.hexdigest()
        data['created'] = False
        if not self.context.has_key(keyword):
            data['created'] = True
            obj = api.content.create(
              type='Benutzerordner',
              id = keyword,
              title=keyword,
              container=self.context)
        data['keyword'] = keyword
        payload = jsonlib.write(data)
        return payload

class MediaLogin(BrowserView):

    def get_databases(self, token):
        myheaders ={'Accept': 'application/json'}
        myauth = ('admin', '!krks.d3print/edi_sicherinvestieren!')
        response = requests.get('https://couch.kraeks.de/_all_dbs', headers=myheaders, auth=myauth)
        databases = response.json()
        compare = "listen_user_%s" %token
        if compare in databases:
            return True
        return False

    def create_database(self, token):
        myheaders ={'Accept': 'application/json', 'Content-Type': 'application/json'}
        myauth = ('admin', '!krks.d3print/edi_sicherinvestieren!')

        database_url = 'https://couch.kraeks.de/listen_user_%s' %token
        new_database = requests.put(database_url, headers=myheaders, auth=myauth)

        newuser_url = 'https://couch.kraeks.de/_users/org.couchdb.user:%s' %token
        data = {"name": token, "password": token, "roles": [], "type": "user"}
        newuser = requests.put(newuser_url, headers=myheaders, auth=myauth, json=data)

        security_url = 'https://couch.kraeks.de/listen_user_%s/_security' %token
        data = {"admins":{"names":[], "roles":[]}, "members":{"names":[token], "roles":[]}}
        security = requests.put(security_url, headers=myheaders, auth=myauth, json=data)
        
        if new_database.status_code == 200 and newuser.status_code == 200 and security.status_code == 200:
            return True
        return False

    def __call__(self):
        data = {}
        body = self.request.get('BODY')
        if body:
            body_unicode = self.request.get('BODY').decode('utf-8')
            data = json.loads(body_unicode)
        username = data.get('username')
        print(username)
        password = data.get('password')
        print(password)
        #Authentication against SAP Backend##
        auth = False
        if username:
            if u'@' in username and len(password) >= 8 :
                auth = True
        ####
        data['token'] = False
        data['database'] = False
        if auth:
            datainput = u"%s%s" %(api.portal.get().absolute_url(), username)
            datainput = datainput.encode('utf-8')
            m = hashlib.md5()
            m.update(datainput)
            token = m.hexdigest()
            database = True
            if not self.get_databases(token):
                database = self.create_database(token)
            data['token'] = token
            data['database'] = database
        payload = jsonlib.write(data)
        return payload


class ChckRegister(BrowserView):

    def __call__(self):
        data = {}
        body = self.request.get('BODY')
        if body:
            body_unicode = self.request.get('BODY').decode('utf-8')
            data = json.loads(body_unicode)
        print(data)
        #ToDo send RegisterData to SAP
        data['registered'] = True
        payload = jsonlib.write(data)
        return payload


class ChckKontakt(BrowserView):

    def __call__(self):
        data = {}
        body = self.request.get('BODY')
        if body:
            body_unicode = self.request.get('BODY').decode('utf-8')
            data = json.loads(body_unicode)
        print(data)
        #ToDo send KontaktData via Mail
        data['sent'] = True
        payload = jsonlib.write(data)
        return payload


class ChecklistData(BrowserView):

    def __call__(self):
        data = {}
        body = self.request.get('BODY')
        if body:
            body_unicode = self.request.get('BODY').decode('utf-8')
            data = json.loads(body_unicode)
            if data:
                contentid = idnormalizer.normalize(data.get('maschine').get('title'))
                mycontext = self.context[data.get('keyword')]
                checkdaten = {}
                checkdaten[data.get('id')] = data.get('optionen')
                notizdaten = {}
                notizdaten[data.get('id')] = data.get('notiz', u'')
                if not mycontext.has_key(contentid):
                    obj = api.content.create(
                        type='Ergebnisdaten',
                        id = contentid,
                        title = data.get('maschine').get('title'),
                        maschnr = data.get('maschine').get('maschnr'),
                        hersteller = data.get('maschine').get('hersteller'),
                        fragebogen = data.get('fragebogen'),
                        history = [data.get('id')],
                        notizen = notizdaten,
                        fortschritt = float(data.get('fortschritt', 0.0)),
                        daten = checkdaten,
                        container=mycontext)
                else:
                    obj = mycontext[contentid]
                    checkdaten = obj.daten
                    checkdaten[data.get('id')] = data.get('optionen')
                    obj.daten = checkdaten
                    history = obj.history
                    if not history:
                        history = []
                    history.append(data.get('id'))
                    obj.history = history
                    notizdaten = obj.notizen
                    if not notizdaten:
                        notizdaten = {}
                    notizdaten[data.get('id')] = data.get('notiz', u'')
                    obj.notizen = notizdaten
                    obj.fortschritt = data.get('fortschritt', 0.0)
        retdict = data
        payload = jsonlib.write(retdict)
        return payload


class PDFDownload(BrowserView):

    def createpdf(self, contentid):
        dateiname = '/tmp/%s.pdf' % contentid
        c = canvas.Canvas(dateiname, pagesize=A4)
        c.setAuthor(u"Pascal Daniel Paul")
        c.setTitle(u"Elektronische Unfallanzeige")
        return c

    def drawpdf(self, c, mycontext):
        schriftart = "Helvetica"
        schriftartfett = "Helvetica-Bold"
        c.rect(2.5*cm, 1.8*cm, 17.2*cm, 25.4*cm)
        c.drawString(10*cm, 15*cm, u'Hallo Welt')
        return c

    def savepdf(self, c):
        c.showPage()
        c.save()

    def __call__(self):
        maschine = self.request.get('maschine')
        contentid = idnormalizer.normalize(maschine)
        mycontext = self.context[contentid]
        c = self.createpdf(contentid)
        c = self.drawpdf(c, mycontext)
        c = self.savepdf(c)
        myfile = open('/tmp/%s.pdf' % contentid, 'r')
        myfile.seek(0)
        RESPONSE = self.request.response
        RESPONSE.setHeader('content-type', 'application/pdf')
        RESPONSE.setHeader('content-disposition', 'attachment; filename=%s.pdf' %contentid)
        return myfile.read()
