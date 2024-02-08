import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
      "InformeVentas": {
        "type": "object",
        "properties": {
          "Encabezado": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "Fecha": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              },
              "required": [
                "Fecha"
              ]
            }
          },
          "Region": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "$": {
                  "type": "object",
                  "properties": {
                    "nombre": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "nombre"
                  ]
                },
                "Trimestre1": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "semestre1": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "LibrosVendidos1": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "semestre1",
                      "LibrosVendidos1"
                    ]
                  }
                },
                "Trimestre2": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "semestre2": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "LibrosVendidos2": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "semestre2",
                      "LibrosVendidos2"
                    ]
                  }
                },
                "Trimestre3": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "semestre3": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "LibrosVendidos3": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "semestre3",
                      "LibrosVendidos3"
                    ]
                  }
                },
                "Trimestre4": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "semestre4": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "LibrosVendidos4": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "semestre4",
                      "LibrosVendidos4"
                    ]
                  }
                }
              },
              "required": [
                "$",
                "Trimestre1",
                "Trimestre2",
                "Trimestre3",
                "Trimestre4"
              ]
            }
          }
        },
        "required": [
          "Encabezado",
          "Region"
        ]
      }
    },
    "required": [
      "InformeVentas"
    ]
  }

# Archivo JSON a validar
archivo_json = '''
{
  "InformeVentas": {
    "Encabezado": [
      {
        "Fecha": [
          "30/12/2009"
        ]
      }
    ],
    "Region": [
      {
        "$": {
          "nombre": "Norte"
        },
        "Trimestre1": [
          {
            "semestre1": [
              "1"
            ],
            "LibrosVendidos1": [
              "24000"
            ]
          }
        ],
        "Trimestre2": [
          {
            "semestre2": [
              "2"
            ],
            "LibrosVendidos2": [
              "38600"
            ]
          }
        ],
        "Trimestre3": [
          {
            "semestre3": [
              "3"
            ],
            "LibrosVendidos3": [
              "NO INFO"
            ]
          }
        ],
        "Trimestre4": [
          {
            "semestre4": [
              "4"
            ],
            "LibrosVendidos4": [
              "NO INFO"
            ]
          }
        ]
      },
      {
        "$": {
          "nombre": "Centro"
        },
        "Trimestre1": [
          {
            "semestre1": [
              "1"
            ],
            "LibrosVendidos1": [
              "NO INFO"
            ]
          }
        ],
        "Trimestre2": [
          {
            "semestre2": [
              "2"
            ],
            "LibrosVendidos2": [
              "16080"
            ]
          }
        ],
        "Trimestre3": [
          {
            "semestre3": [
              "3"
            ],
            "LibrosVendidos3": [
              "25000"
            ]
          }
        ],
        "Trimestre4": [
          {
            "semestre4": [
              "4"
            ],
            "LibrosVendidos4": [
              "29000"
            ]
          }
        ]
      },
      {
        "$": {
          "nombre": "Sur"
        },
        "Trimestre1": [
          {
            "semestre1": [
              "1"
            ],
            "LibrosVendidos1": [
              "27000"
            ]
          }
        ],
        "Trimestre2": [
          {
            "semestre2": [
              "2"
            ],
            "LibrosVendidos2": [
              "31400"
            ]
          }
        ],
        "Trimestre3": [
          {
            "semestre3": [
              "3"
            ],
            "LibrosVendidos3": [
              "40100"
            ]
          }
        ],
        "Trimestre4": [
          {
            "semestre4": [
              "4"
            ],
            "LibrosVendidos4": [
              "30000"
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