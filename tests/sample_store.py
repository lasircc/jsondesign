SCHEMA = { 

'las://recording.json' : {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Schema for a recording",
  "type": "object",
  "properties": {
    "id": {"type": "number"},
    "work": {
      "type": "object",
      "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "composer": {"$ref": "las://artist.json"}
      }
    },

    "recording_artists": {
      "type": "array",
      "items": {"$ref": "las://artist.json"}
    }
  },
  "required": ["id", "work", "recording_artists"]
},

'las://artist.json' : {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Schema for an artist",
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "functions": {
        "type": "array",
        "items": {"type": "string"}
        }
    },
    "required": ["id", "name", "functions"]
    }

}