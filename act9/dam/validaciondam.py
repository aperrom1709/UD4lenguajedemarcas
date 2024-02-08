import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
      "Alumnos": {
        "type": "object",
        "properties": {
          "Alumno": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "NIF": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "Resultado": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "Observaciones": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "IP": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "MAC": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              },
              "required": [
                "NIF",
                "Resultado",
                "Observaciones",
                "IP",
                "MAC"
              ]
            }
          }
        },
        "required": [
          "Alumno"
        ]
      }
    },
    "required": [
      "Alumnos"
    ]
  }

# Archivo JSON a validar
archivo_json = '''
{
  "Alumnos": {
    "Alumno": [
      {
        "NIF": [
          "12345678Z"
        ],
        "Resultado": [
          "apto"
        ],
        "Observaciones": [
          ""
        ],
        "IP": [
          "192.168.1.1"
        ],
        "MAC": [
          ""
        ]
      },
      {
        "NIF": [
          "23456789Y"
        ],
        "Resultado": [
          "No apto"
        ],
        "Observaciones": [
          "Falta de entusiasmo"
        ],
        "IP": [
          ""
        ],
        "MAC": [
          "00:11:22:33:44:55"
        ]
      },
      {
        "NIF": [
          "34567890X"
        ],
        "Resultado": [
          "apto"
        ],
        "Observaciones": [
          ""
        ],
        "IP": [
          ""
        ],
        "MAC": [
          "00:66:77:88:99:AA"
        ]
      },
      {
        "NIF": [
          "45678901W"
        ],
        "Resultado": [
          "No apto"
        ],
        "Observaciones": [
          "Falta de participación"
        ],
        "IP": [
          "192.168.1.2"
        ],
        "MAC": [
          ""
        ]
      },
      {
        "NIF": [
          "56789012V"
        ],
        "Resultado": [
          "apto"
        ],
        "Observaciones": [
          ""
        ],
        "IP": [
          ""
        ],
        "MAC": [
          "00:BB:CC:DD:EE:FF"
        ]
      },
      {
        "NIF": [
          "67890123U"
        ],
        "Resultado": [
          "No apto"
        ],
        "Observaciones": [
          "Falta de compromiso"
        ],
        "IP": [
          "192.168.1.3"
        ],
        "MAC": [
          ""
        ]
      },
      {
        "NIF": [
          "78901234T"
        ],
        "Resultado": [
          "apto"
        ],
        "Observaciones": [
          ""
        ],
        "IP": [
          ""
        ],
        "MAC": [
          "00:GG:HH:II:JJ:KK"
        ]
      },
      {
        "NIF": [
          "89012345S"
        ],
        "Resultado": [
          "No apto"
        ],
        "Observaciones": [
          "Falta de dedicación"
        ],
        "IP": [
          "192.168.1.4"
        ],
        "MAC": [
          ""
        ]
      },
      {
        "NIF": [
          "90123456R"
        ],
        "Resultado": [
          "apto"
        ],
        "Observaciones": [
          ""
        ],
        "IP": [
          ""
        ],
        "MAC": [
          "00:LL:MM:NN:OO:PP"
        ]
      },
      {
        "NIF": [
          "01234567Q"
        ],
        "Resultado": [
          "No apto"
        ],
        "Observaciones": [
          "Falta de profesionalismo"
        ],
        "IP": [
          "192.168.1.5"
        ],
        "MAC": [
          ""
        ]
      }
    ]
  }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.