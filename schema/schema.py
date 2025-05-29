book_is_not_exist = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "isSuccessful": {
      "type": "boolean"
    },
    "isWarning": {
      "type": "boolean"
    },
    "messages": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "data": {
      "type": "object",
      "properties": {
        "Errors": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "number": {
                  "type": "integer"
                },
                "state": {
                  "type": "integer"
                },
                "class": {
                  "type": "integer"
                },
                "server": {
                  "type": "string"
                },
                "message": {
                  "type": "string"
                },
                "procedure": {
                  "type": "string"
                },
                "lineNumber": {
                  "type": "integer"
                }
              },
              "required": [
                "source",
                "number",
                "state",
                "class",
                "server",
                "message",
                "procedure",
                "lineNumber"
              ]
            },
            {
              "type": "object",
              "properties": {
                "source": {
                  "type": "string"
                },
                "number": {
                  "type": "integer"
                },
                "state": {
                  "type": "integer"
                },
                "class": {
                  "type": "integer"
                },
                "server": {
                  "type": "string"
                },
                "message": {
                  "type": "string"
                },
                "procedure": {
                  "type": "string"
                },
                "lineNumber": {
                  "type": "integer"
                }
              },
              "required": [
                "source",
                "number",
                "state",
                "class",
                "server",
                "message",
                "procedure",
                "lineNumber"
              ]
            }
          ]
        },
        "ClientConnectionId": {
          "type": "string"
        },
        "ClassName": {
          "type": "string"
        },
        "Message": {
          "type": "string"
        },
        "Data": {
          "type": "object",
          "properties": {
            "helpLink.ProdName": {
              "type": "string"
            },
            "helpLink.ProdVer": {
              "type": "string"
            },
            "helpLink.EvtSrc": {
              "type": "string"
            },
            "helpLink.EvtID": {
              "type": "string"
            },
            "helpLink.BaseHelpUrl": {
              "type": "string"
            },
            "helpLink.LinkId": {
              "type": "string"
            }
          },
          "required": [
            "helpLink.ProdName",
            "helpLink.ProdVer",
            "helpLink.EvtSrc",
            "helpLink.EvtID",
            "helpLink.BaseHelpUrl",
            "helpLink.LinkId"
          ]
        },
        "InnerException": {
          "type": "null"
        },
        "HelpURL": {
          "type": "null"
        },
        "StackTraceString": {
          "type": "string"
        },
        "RemoteStackTraceString": {
          "type": "null"
        },
        "RemoteStackIndex": {
          "type": "integer"
        },
        "ExceptionMethod": {
          "type": "string"
        },
        "HResult": {
          "type": "integer"
        },
        "Source": {
          "type": "string"
        },
        "WatsonBuckets": {
          "type": "null"
        }
      },
      "required": [
        "Errors",
        "ClientConnectionId",
        "ClassName",
        "Message",
        "Data",
        "InnerException",
        "HelpURL",
        "StackTraceString",
        "RemoteStackTraceString",
        "RemoteStackIndex",
        "ExceptionMethod",
        "HResult",
        "Source",
        "WatsonBuckets"
      ]
    }
  },
  "required": [
    "isSuccessful",
    "isWarning",
    "messages",
    "data"
  ]
}

unsuccessful_login = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "isSuccessful": {
      "type": "boolean"
    },
    "isWarning": {
      "type": "boolean"
    },
    "messages": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "data": {
      "type": "null"
    }
  },
  "required": [
    "isSuccessful",
    "isWarning",
    "messages",
    "data"
  ]
}