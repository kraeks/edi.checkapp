schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "ort": {
      "title": "Arbeitsstelle/Arbeitsort",
      "type": "string"
    },
    "dateTime": {
      "title": "Datum und Uhrzeit",
      "type": "string",
      "format": "date-time"
    },
    "anlageverantwortlicher": {
      "title": "Person in der Rolle des Anlagenverantwortlichen",
      "type": "string"
    },
    "arbeitsverantwortlicher": {
      "title": "Person in der Rolle des Arbeitsverantwortlichen",
      "type": "string"
    },
    "arbeitsausfuehrender": {
      "title": "Arbeitsausführende Person",
      "type": "string"
    },
    "zusaetzlicheAusruestung": {
      "title": "Zusätzliche persönliche Schutzausrüstung",
      "description": "Bei der ersten und fünften Sicherheitsregel",
      "type": "array",
      "enum": [
        "gegen elektrischen Schlag",
        "gegen Störlichtbogen"
      ]
    },
    "spannungAnAnlage": {
      "title": "Stehen andere Anlagenteile weiterhin unter Spannung, so dass der Arbeitsbereich z. B. mit Ketten oder Bändern gekennzeichnet oder abgegrenzt werden muss?",
      "type": "boolean"
    },
    "freischaltungWie": {
      "title": "Wie erfolgte die Freischaltung?",
      "type": "string",
      "enum": [
        "NH-Sicherungen",
        "NH-Lastschaltleiste",
        "Leistungsschalter",
        "Trafo außer Betrieb genommen",
        "Netzersatzungsanlage außer Betrieb genommen"
      ]
    },
    "ausloesestromS": {
      "title": "Auslösestrom in Ampere",
      "type": "number"
    },
    "ausloesestromLa": {
      "title": "Auslösestrom in Ampere",
      "type": "number"
    },
    "ausloesestromLe": {
      "title": "Auslösestrom in Ampere",
      "type": "number"
    },
    "freischaltungWo": {
      "title": "Wo erfolgte die Freischaltung?",
      "type": "string",
      "enum": [
        "Trafostation",
        "Umpannwerk/-anlage",
        "Kabelverteilerschrank"
      ]
    },
    "bezeichnungT": {
      "title": "Nr./Bezeichnung",
      "type": "string"
    },
    "bezeichnungU": {
      "title": "Nr./Bezeichnung",
      "type": "string"
    },
    "bezeichnungK": {
      "title": "Nr./Bezeichnung",
      "type": "string"
    },
    "schloss": {
      "title": "Wurde ein Vorhängeschloss am Schalter eingehängt und abgeschlossen?",
      "type": "boolean"
    },
    "tuer": {
      "title": "Wurde die Tür zum elektrischen Betriebsraum verschlossen?",
      "type": "boolean"
    },
    "schild": {
      "title": "Wurde ein Schild \"Schalten verboten\" zusätzlich angebracht?",
      "type": "string",
      "enum": [
        "angehängt",
        "geklebt",
        "magnetisch",
        "nein"
      ]
    },
    "spannungspruefer": {
      "title": "Zweipoliger Spannungsprüfer",
      "type": "string"
    },
    "vorrichtung": {
      "title": "Wo wurde die EuK-Vorrichtung eingebaut?",
      "type": "string",
      "enum": [
        "in die NH-Sicherungsunterteile",
        "unterspannungsseitig am Trafo",
        "an der Sammelschiene",
        "nicht geerdet und kurzgeschlossen"
      ]
    },
    "grund": {
      "type": "string"
    },
    "abdeckung": {
      "type": "string",
      "title": "Mit der Abdeckung soll erreicht werden",
      "enum": [
        "teilweiser Berührungsschutz",
        "vollständiger Berührungsschutz",
        "Abdeckung nicht notwendig"
      ]
    },
    "ada1": {
      "type": "array",
      "title": "Art der Abdeckung",
      "enum": [
        "isolierende Formteile",
        "isolierende Tücher"
      ]
    },
    "ada2": {
      "type": "array",
      "title": "Art der Abdeckung",
      "enum": [
        "isolierende Formteile",
        "isolierende Tücher"
      ]
    },
    "ka": {
      "type": "string",
      "title": "Keine Abdeckung angebracht, weil",
      "enum": ["keine unter Spannung stehenden Teile im Arbeitsbereich vorhanden sind", "Entfernung zu den Teilen groß genug ist"]
    },
    "entfernung":{
      "type": "number",
      "title": "Entfernung zu den Teilen"
    },
    "notiz": {
      "type": "string"
    }
  }
}

uischema = {
  "$schema": "../../schemas/ui/ui.schema.json",
  "type": "VerticalLayout",
  "elements": [
    {
      "type": "Control",
      "scope": "#/properties/ort"
    },
    {
      "type": "Control",
      "scope": "#/properties/dateTime"
    },
    {
      "type": "Control",
      "scope": "#/properties/anlageverantwortlicher"
    },
    {
      "type": "Control",
      "scope": "#/properties/arbeitsverantwortlicher",
      "options": {
        "multi": True
      }
    },
    {
      "type": "Control",
      "scope": "#/properties/arbeitsausfuehrender"
    },
    {
      "type": "Divider"
    },
    {
      "type": "Control",
      "scope": "#/properties/zusaetzlicheAusruestung"
    },
    {
      "type": "Control",
      "scope": "#/properties/spannungAnAnlage"
    },
    {
      "type": "Divider"
    },
    {
      "type": "HTML",
      "htmlData": "<h2>Die fünf Sicherheitsregeln</h2>"
    },
    {
      "type": "Group",
      "label": "1. Freigeschaltet",
      "elements": [
        {
          "type": "Control",
          "scope": "#/properties/freischaltungWie",
          "options": {
            "radiobuttons": True,
            "stacked": True
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/ausloesestromS",
          "options": {
            "append": "A"
          },
          "showOn": {
            "type": "EQUALS",
            "scope": "#/properties/freischaltungWie",
            "referenceValue": "NH-Sicherungen"
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/ausloesestromLa",
          "options": {
            "append": "A"
          },
          "showOn": {
            "type": "EQUALS",
            "scope": "#/properties/freischaltungWie",
            "referenceValue": "NH-Lastschaltleiste"
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/ausloesestromLe",
          "options": {
            "append": "A"
          },
          "showOn": {
            "type": "EQUALS",
            "scope": "#/properties/freischaltungWie",
            "referenceValue": "Leistungsschalter"
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/freischaltungWo",
          "options": {
            "radiobuttons": True,
            "stacked": True
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/bezeichnungT",
          "showOn": {
            "type": "EQUALS",
            "scope": "#/properties/freischaltungWo",
            "referenceValue": "Trafostation"
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/bezeichnungU",
          "showOn": {
            "type": "EQUALS",
            "scope": "#/properties/freischaltungWo",
            "referenceValue": "Umpannwerk/-anlage"
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/bezeichnungK",
          "showOn": {
            "type": "EQUALS",
            "scope": "#/properties/freischaltungWo",
            "referenceValue": "Kabelverteilerschrank"
          }
        }
      ]
    },
    {
      "type": "Group",
      "label": "2. Gegen Wiedereinschalten gesichert",
      "elements": [
        {
          "type": "Control",
          "scope": "#/properties/schloss"
        },
        {
          "type": "Control",
          "scope": "#/properties/tuer"
        },
        {
          "type": "Control",
          "scope": "#/properties/schild",
          "options": {
            "radiobuttons": True,
            "stacked": True
          }
        }
      ]
    },
    {
      "type": "Group",
      "label": "3. Spannungsfreiheit allpolig festgestellt an der Arbeitsstelle",
      "elements": [
        {
          "type": "Control",
          "scope": "#/properties/spannungspruefer",
          "options": {
            "placeholder": "Hersteller/Typ"
          }
        }
      ]
    },
    {
      "type": "Group",
      "label": "4. Geerdet und kurzgeschlossen",
      "elements": [
        {
          "type": "Control",
          "scope": "#/properties/vorrichtung",
          "options": {
            "radiobuttons": True,
            "stacked": True
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/grund",
          "showOn": {
            "scope": "#/properties/vorrichtung",
            "type": "EQUALS",
            "referenceValue": "nicht geerdet und kurzgeschlossen"
          },
          "options": {
            "multi": True
          }
        }
      ]
    },
    {
      "type": "Group",
      "label": "5. Benachbarte, unter Spannung stehende Teile abgedeckt",
      "elements": [
        {
          "type": "Control",
          "scope": "#/properties/abdeckung",
          "options": {
            "radiobuttons": True,
            "stacked": True
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/ada1",
          "showOn": {
            "type": "EQUALS",
            "scope": "#/properties/abdeckung",
            "referenceValue": "teilweiser Berührungsschutz"
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/ada2",
          "showOn": {
            "type": "EQUALS",
            "scope": "#/properties/abdeckung",
            "referenceValue": "vollständiger Berührungsschutz"
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/ka",
          "showOn": {
            "type": "EQUALS",
            "scope": "#/properties/abdeckung",
            "referenceValue": "Abdeckung nicht notwendig"
          },
          "options": {
            "radiobuttons": True,
            "stacked": True
          }
        },
        {
          "type": "Control",
          "scope": "#/properties/entfernung",
          "showOn": {
            "type": "EQUALS",
            "scope": "#/properties/ka",
            "referenceValue": "Entfernung zu den Teilen groß genug ist"
          },
          "options": {
            "append": "m"
          }
        }
      ]
    },
    {
      "type": "Divider"
    },
    {
      "type": "Control",
      "scope": "#/properties/notiz",
      "options": {
        "multi": True
      }
    }
  ]
}
