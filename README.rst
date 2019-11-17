.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

============
edi.checkapp
============

Add-On für das Web-CMS Plone zur Konfiguration von Checklisten und zur Ablaufsteuerung einer Applikation.


Features
--------

- Checklisten können über das CMS Plone konfiguriert werden.
- Die Fragestellungen der Checkliste können für ein Ablaufsteuerung in Abhängigkeit der Benutzereingagen verknüpft werden.


Translations
------------

Das Produkt steht derzeit nur in Deutscher Sprache zur Verfügung.


Installation
------------

Installation von edi.checkapp durch Hinzufügen zur buildout.cfg::

    [buildout]

    ...

    eggs =
        edi.checkapp


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/educorvi/edi.checkapp/issues
- Source Code: https://github.com/educorvi/edi.checkapp


Support
-------

lars.walther@educorvi.de


License
-------

The project is licensed under the GPLv2.
