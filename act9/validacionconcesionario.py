import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "Concesionario": {
      "type": "object",
      "properties": {
        "Coche": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "$": {
                "type": "object",
                "properties": {
                  "matricula": {
                    "type": "string"
                  }
                },
                "required": [
                  "matricula"
                  
                 
                
                ]
              },
              "Marca": {
                "type": "array",
                "items": {
                  "type": "string",
                  "minLength":1
                
                }
              },
              "Modelo": {
                "type": "array",
                "items": {
                  "type": "string",
                  "minLength":1
                }
              },
              "Año": {
                "type": "array",
                "items": {
                  "type": "string",
                  "minLength":1
                }
              },
              "Precio": {
                "type": "array",
                "items": {
                  "type": "string",
                  "minLength":1
                }
              }
            },
            "required": [
              "$",
              "Marca",
              "Modelo",
              "Año",
              "Precio",
              
            ]
          }
        }
      },
      "required": [
        "Coche" 
      ]
    }
  },
  "required": [
    "Concesionario"
  ]
}

# Archivo JSON a validar
archivo_json = '''
{
  "Concesionario": {
    "Coche": [
      {
        "$": {
          "matricula": "1111AAA"
        },
        "Marca": [
          "AUDI"
        ],
        "Modelo": [
          "A4"
        ],
        "Año": [
          "2018"
        ],
        "Precio": [
          "30000"
        ]
      },
      {
        "$": {
          "matricula": "2222BBB"
        },
        "Marca": [
          "SEAT"
        ],
        "Modelo": [
          "Leon"
        ],
        "Año": [
          "2019"
        ],
        "Precio": [
          "10000"
        ]
      },
      {
        "$": {
          "matricula": "3333CCC"
        },
        "Marca": [
          "RENAULT"
        ],
        "Modelo": [
          "Clio"
        ],
        "Año": [
          "2020"
        ],
        "Precio": [
          "15000"
        ]
      },
      {
        "$": {
          "matricula": "4444DDD"
        },
        "Marca": [
          "VOLVO"
        ],
        "Modelo": [
          "V70"
        ],
        "Año": [
          "2018"
        ],
        "Precio": [
          "25000"
        ]
      },
      {
        "$": {
          "matricula": "5555EEE"
        },
        "Marca": [
          "PEUGEOT"
        ],
        "Modelo": [
          "308"
        ],
        "Año": [
          "2021"
        ],
        "Precio": [
          "20000"
        ]
      },
      {
        "$": {
          "matricula": "6666FFF"
        },
        "Marca": [
          "MERCEDES"
        ],
        "Modelo": [
          "CLK"
        ],
        "Año": [
          "2017"
        ],
        "Precio": [
          "35000"
        ]
      },
      {
        "$": {
          "matricula": "7777GGG"
        },
        "Marca": [
          "JAGUAR"
        ],
        "Modelo": [
          "F-TYPE"
        ],
        "Año": [
          "2020"
        ],
        "Precio": [
          "40000"
        ]
      },
      {
        "$": {
          "matricula": "8888HHH"
        },
        "Marca": [
          "MAZDA"
        ],
        "Modelo": [
          "MX-5"
        ],
        "Año": [
          "2019"
        ],
        "Precio": [
          "20000"
        ]
      },
      {
        "$": {
          "matricula": "9999III"
        },
        "Marca": [
          "LAND ROVER"
        ],
        "Modelo": [
          "Range Rover"
        ],
        "Año": [
          "2021"
        ],
        "Precio": [
          "50000"
        ]
      },
      {
        "$": {
          "matricula": "0000JJJ"
        },
        "Marca": [
          "MINI"
        ],
        "Modelo": [
          "Clubman"
        ],
        "Año": [
          "2020"
        ],
        "Precio": [
          "25000"
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