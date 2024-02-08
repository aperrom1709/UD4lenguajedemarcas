import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
      "clientes": {
        "type": "object",
        "properties": {
          "sede": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "dir1": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "dir2": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "empleado": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "fecha": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "cliente1": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "cod": {
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
                      },
                      "numero": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "coste": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "resumen": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "plazo": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "cod",
                      "descripcion",
                      "numero",
                      "coste",
                      "resumen",
                      "plazo"
                    ]
                  }
                },
                "cliente2": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "cod": {
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
                      },
                      "numero": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "coste": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "resumen": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "plazo": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "cod",
                      "descripcion",
                      "numero",
                      "coste",
                      "resumen",
                      "plazo"
                    ]
                  }
                },
                "cliente3": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "cod": {
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
                      },
                      "numero": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "coste": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "resumen": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "plazo": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "cod",
                      "descripcion",
                      "numero",
                      "coste",
                      "resumen",
                      "plazo"
                    ]
                  }
                },
                "cliente4": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "cod": {
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
                      },
                      "numero": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "coste": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "resumen": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "plazo": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "cod",
                      "descripcion",
                      "numero",
                      "coste",
                      "resumen",
                      "plazo"
                    ]
                  }
                },
                "cliente5": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "cod": {
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
                      },
                      "numero": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "coste": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "resumen": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "plazo": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "cod",
                      "descripcion",
                      "numero",
                      "coste",
                      "resumen",
                      "plazo"
                    ]
                  }
                },
                "cliente6": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "cod": {
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
                      },
                      "numero": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "coste": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "resumen": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "plazo": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "cod",
                      "descripcion",
                      "numero",
                      "coste",
                      "resumen",
                      "plazo"
                    ]
                  }
                },
                "cliente7": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "cod": {
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
                      },
                      "numero": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "coste": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "resumen": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "plazo": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "cod",
                      "descripcion",
                      "numero",
                      "coste",
                      "resumen",
                      "plazo"
                    ]
                  }
                },
                "cliente8": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "cod": {
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
                      },
                      "numero": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "coste": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "resumen": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "plazo": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "cod",
                      "descripcion",
                      "numero",
                      "coste",
                      "resumen",
                      "plazo"
                    ]
                  }
                },
                "cliente9": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "cod": {
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
                      },
                      "numero": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "coste": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "resumen": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "plazo": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "cod",
                      "descripcion",
                      "numero",
                      "coste",
                      "resumen",
                      "plazo"
                    ]
                  }
                },
                "cliente10": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "cod": {
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
                      },
                      "numero": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "coste": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "resumen": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "plazo": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "cod",
                      "descripcion",
                      "numero",
                      "coste",
                      "resumen",
                      "plazo"
                    ]
                  }
                }
              },
              "required": [
                "dir1",
                "dir2",
                "empleado",
                "fecha",
                "cliente1",
                "cliente2",
                "cliente3",
                "cliente4",
                "cliente5",
                "cliente6",
                "cliente7",
                "cliente8",
                "cliente9",
                "cliente10"
              ]
            }
          }
        },
        "required": [
          "sede"
        ]
      }
    },
    "required": [
      "clientes"
    ]
  }

# Archivo JSON a validar
archivo_json = '''
{
  "clientes": {
    "sede": [
      {
        "dir1": [
          "Palacio Real de Riofrío"
        ],
        "dir2": [
          "Bosque de Riofrío"
        ],
        "empleado": [
          "Empleado 1"
        ],
        "fecha": [
          "01/01/2024"
        ],
        "cliente1": [
          {
            "cod": [
              "001"
            ],
            "descripcion": [
              "Real Sitio de Riofrío"
            ],
            "numero": [
              "100"
            ],
            "coste": [
              "$200"
            ],
            "resumen": [
              "Resumen del Real Sitio de Riofrío"
            ],
            "plazo": [
              "30 días"
            ]
          }
        ],
        "cliente2": [
          {
            "cod": [
              "002"
            ],
            "descripcion": [
              "Pirriland "
            ],
            "numero": [
              "50"
            ],
            "coste": [
              "$100"
            ],
            "resumen": [
              "Resumen de Pirriland"
            ],
            "plazo": [
              "60 días"
            ]
          }
        ],
        "cliente3": [
          {
            "cod": [
              "003"
            ],
            "descripcion": [
              "Nurburgringo"
            ],
            "numero": [
              "75"
            ],
            "coste": [
              "$150"
            ],
            "resumen": [
              "Resumen de Nurburgringo"
            ],
            "plazo": [
              "45 días"
            ]
          }
        ],
        "cliente4": [
          {
            "cod": [
              "004"
            ],
            "descripcion": [
              "red bull ring"
            ],
            "numero": [
              "60"
            ],
            "coste": [
              "$120"
            ],
            "resumen": [
              "Resumen de red bull ring"
            ],
            "plazo": [
              "50 días"
            ]
          }
        ],
        "cliente5": [
          {
            "cod": [
              "005"
            ],
            "descripcion": [
              "trial mountain"
            ],
            "numero": [
              "80"
            ],
            "coste": [
              "$180"
            ],
            "resumen": [
              "Resumen de trial mountain"
            ],
            "plazo": [
              "65 días"
            ]
          }
        ],
        "cliente6": [
          {
            "cod": [
              "006"
            ],
            "descripcion": [
              "montmelo"
            ],
            "numero": [
              "90"
            ],
            "coste": [
              "$210"
            ],
            "resumen": [
              "Resumen de montmelo"
            ],
            "plazo": [
              "70 días"
            ]
          }
        ],
        "cliente7": [
          {
            "cod": [
              "007"
            ],
            "descripcion": [
              "jarama"
            ],
            "numero": [
              "100"
            ],
            "coste": [
              "$240"
            ],
            "resumen": [
              "Resumen de jarama"
            ],
            "plazo": [
              "75 días"
            ]
          }
        ],
        "cliente8": [
          {
            "cod": [
              "008"
            ],
            "descripcion": [
              "le mans"
            ],
            "numero": [
              "110"
            ],
            "coste": [
              "$270"
            ],
            "resumen": [
              "Resumen de le mans"
            ],
            "plazo": [
              "80 días"
            ]
          }
        ],
        "cliente9": [
          {
            "cod": [
              "009"
            ],
            "descripcion": [
              "monaco"
            ],
            "numero": [
              "120"
            ],
            "coste": [
              "$300"
            ],
            "resumen": [
              "Resumen de monaco"
            ],
            "plazo": [
              "85 días"
            ]
          }
        ],
        "cliente10": [
          {
            "cod": [
              "010"
            ],
            "descripcion": [
              "dragon trail"
            ],
            "numero": [
              "130"
            ],
            "coste": [
              "$330"
            ],
            "resumen": [
              "Resumen de dragon trail"
            ],
            "plazo": [
              "90 días"
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