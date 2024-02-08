import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
      "modulos": {
        "type": "object",
        "properties": {
          "modulo": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "nombre": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "contenidos": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "ud": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "tipo": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            },
                            "descripcion": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            }
                          },
                          "required": [
                            "tipo",
                            "descripcion"
                          ]
                        }
                      }
                    },
                    "required": [
                      "ud"
                    ]
                  }
                }
              },
              "required": [
                "nombre",
                "contenidos"
              ]
            }
          }
        },
        "required": [
          "modulo"
        ]
      }
    },
    "required": [
      "modulos"
    ]
  }

# Archivo JSON a validar
archivo_json = '''
{
  "modulos": {
    "modulo": [
      {
        "nombre": [
          "Base de datos"
        ],
        "contenidos": [
          {
            "ud": [
              {
                "tipo": [
                  "lenguaje sql"
                ],
                "descripcion": [
                  "creacion de base de datos"
                ]
              },
              {
                "tipo": [
                  "interfaz de bases de datos"
                ],
                "descripcion": [
                  "formaremos graficamente una base de datos con smartdraw"
                ]
              }
            ]
          }
        ]
      },
      {
        "nombre": [
          "Sistemas informaticos"
        ],
        "contenidos": [
          {
            "ud": [
              {
                "tipo": [
                  "creacion de maquina virtual con debian 12"
                ],
                "descripcion": [
                  "creacion practica de  maquina virtual"
                ]
              },
              {
                "tipo": [
                  "Sistemas de gestores de ficheros"
                ],
                "descripcion": [
                  "aprenderemos a gestionar ficheros por comandos por consola"
                ]
              }
            ]
          }
        ]
      },
      {
        "nombre": [
          "Formacion y orientacion laboral"
        ],
        "contenidos": [
          {
            "ud": [
              {
                "tipo": [
                  "contrato de trabajo"
                ],
                "descripcion": [
                  "aprenderemos todo lo necesario sobre contratos de trabajo"
                ]
              },
              {
                "tipo": [
                  "Derechos del trabajador"
                ],
                "descripcion": [
                  "Aprenderemos todos los derechos y deberes del trabajador"
                ]
              }
            ]
          }
        ]
      },
      {
        "nombre": [
          "Lenguaje de marcas"
        ],
        "contenidos": [
          {
            "ud": [
              {
                "tipo": [
                  "xml y html"
                ],
                "descripcion": [
                  "aprenderemos todo lo necesario para crear archivos xmlk y html con adiciones de css y json"
                ]
              },
              {
                "tipo": [
                  "xsd y dtd"
                ],
                "descripcion": [
                  "Aprenderemos todo lo necesario par usar el dtd y xsd con nuestros xml "
                ]
              }
            ]
          }
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