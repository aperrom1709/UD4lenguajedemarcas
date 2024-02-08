import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
      "libreria": {
        "type": "object",
        "properties": {
          "libro": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "libro": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "autores": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "autor": {
                              "type": "array",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "titulo": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  },
                                  "escritor": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  },
                                  "titulo2": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  },
                                  "titulo1": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    }
                                  }
                                },
                                "required": [
                                  "titulo",
                                  "escritor"
                                ]
                              }
                            }
                          },
                          "required": [
                            "autor"
                          ]
                        }
                      },
                      "titulo": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "editorial": {
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
                      "ISBN": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "autores",
                      "titulo",
                      "editorial",
                      "fecha",
                      "ISBN"
                    ]
                  }
                }
              },
              "required": [
                "libro"
              ]
            }
          }
        },
        "required": [
          "libro"
        ]
      }
    },
    "required": [
      "libreria"
    ]
  }
# Archivo JSON a validar
archivo_json = '''
{
  "libreria": {
    "libro": [
      {
        "libro": [
          {
            "autores": [
              {
                "autor": [
                  {
                    "titulo": [
                      "firulais",
                      "ataca"
                    ],
                    "escritor": [
                      "popi"
                    ]
                  },
                  {
                    "titulo": [
                      "titanic"
                    ],
                    "titulo1": [
                      "volado"
                    ],
                    "escritor": [
                      "erulencio"
                    ]
                  }
                ]
              }
            ],
            "titulo": [
              "The post"
            ],
            "editorial": [
              "fiumba"
            ],
            "fecha": [
              "2033"
            ],
            "ISBN": [
              "9788408237044"
            ]
          },
          {
            "autores": [
              {
                "autor": [
                  {
                    "titulo": [
                      "planeta"
                    ],
                    "titulo2": [
                      "vegeta"
                    ],
                    "escritor": [
                      "vegeta"
                    ]
                  },
                  {
                    "titulo": [
                      "gargantua"
                    ],
                    "titulo1": [
                      "en occidente"
                    ],
                    "escritor": [
                      "pi"
                    ]
                  }
                ]
              }
            ],
            "titulo": [
              "The predator"
            ],
            "editorial": [
              "oxford"
            ],
            "fecha": [
              "2021"
            ],
            "ISBN": [
              "9788408237044"
            ]
          },
          {
            "autores": [
              {
                "autor": [
                  {
                    "titulo": [
                      "la vida"
                    ],
                    "titulo2": [
                      "de pi"
                    ],
                    "escritor": [
                      "pirri"
                    ]
                  },
                  {
                    "titulo": [
                      "super"
                    ],
                    "titulo1": [
                      "2"
                    ],
                    "escritor": [
                      "toriyama"
                    ]
                  }
                ]
              }
            ],
            "titulo": [
              "The fosil"
            ],
            "editorial": [
              "Planeta"
            ],
            "fecha": [
              "1999"
            ],
            "ISBN": [
              "9788408237044"
            ]
          },
          {
            "autores": [
              {
                "autor": [
                  {
                    "titulo": [
                      "popit"
                    ],
                    "titulo2": [
                      "popop"
                    ],
                    "escritor": [
                      "misterio"
                    ]
                  },
                  {
                    "titulo": [
                      "pepe"
                    ],
                    "titulo1": [
                      "pepito"
                    ],
                    "escritor": [
                      "pepe"
                    ]
                  }
                ]
              }
            ],
            "titulo": [
              " coches"
            ],
            "editorial": [
              "gran tour"
            ],
            "fecha": [
              "2005"
            ],
            "ISBN": [
              "293597829428"
            ]
          },
          {
            "autores": [
              {
                "autor": [
                  {
                    "titulo": [
                      "poropopo"
                    ],
                    "titulo2": [
                      "popero"
                    ],
                    "escritor": [
                      "pipo"
                    ]
                  },
                  {
                    "titulo": [
                      "el"
                    ],
                    "titulo1": [
                      "sismo"
                    ],
                    "escritor": [
                      "violin"
                    ]
                  }
                ]
              }
            ],
            "titulo": [
              " catstrofe"
            ],
            "editorial": [
              "bbc"
            ],
            "fecha": [
              "0011"
            ],
            "ISBN": [
              "9788408237044"
            ]
          },
          {
            "autores": [
              {
                "autor": [
                  {
                    "titulo": [
                      "pom"
                    ],
                    "titulo2": [
                      "pim"
                    ],
                    "escritor": [
                      "pompa"
                    ]
                  },
                  {
                    "titulo": [
                      "te"
                    ],
                    "titulo1": [
                      "invito"
                    ],
                    "escritor": [
                      "jugar"
                    ]
                  }
                ]
              }
            ],
            "titulo": [
              "The abism"
            ],
            "editorial": [
              "Planeta"
            ],
            "fecha": [
              "2021"
            ],
            "ISBN": [
              "9788408237044"
            ]
          },
          {
            "autores": [
              {
                "autor": [
                  {
                    "titulo": [
                      "ale"
                    ],
                    "titulo2": [
                      "canta"
                    ],
                    "escritor": [
                      "alejandro"
                    ]
                  },
                  {
                    "titulo": [
                      "alvaro"
                    ],
                    "titulo1": [
                      "juega"
                    ],
                    "escritor": [
                      "alvaro"
                    ]
                  }
                ]
              }
            ],
            "titulo": [
              "mounstruo "
            ],
            "editorial": [
              "Planeta"
            ],
            "fecha": [
              "2010"
            ],
            "ISBN": [
              "9788408237044"
            ]
          },
          {
            "autores": [
              {
                "autor": [
                  {
                    "titulo": [
                      "perro"
                    ],
                    "titulo2": [
                      "gato"
                    ],
                    "escritor": [
                      "abel"
                    ]
                  },
                  {
                    "titulo": [
                      "gato"
                    ],
                    "titulo1": [
                      "raton"
                    ],
                    "escritor": [
                      "jesus"
                    ]
                  }
                ]
              }
            ],
            "titulo": [
              "coche "
            ],
            "editorial": [
              "bcc"
            ],
            "fecha": [
              "2000"
            ],
            "ISBN": [
              "9788408237044"
            ]
          },
          {
            "autores": [
              {
                "autor": [
                  {
                    "titulo": [
                      "robot"
                    ],
                    "titulo2": [
                      "peligroso"
                    ],
                    "escritor": [
                      "J.r"
                    ]
                  },
                  {
                    "titulo": [
                      "aitor"
                    ],
                    "titulo1": [
                      "menta"
                    ],
                    "escritor": [
                      "tesla"
                    ]
                  }
                ]
              }
            ],
            "titulo": [
              "The fish"
            ],
            "editorial": [
              "Planeta"
            ],
            "fecha": [
              "1234"
            ],
            "ISBN": [
              "9788408237044"
            ]
          },
          {
            "autores": [
              {
                "autor": [
                  {
                    "titulo": [
                      "pez"
                    ],
                    "titulo2": [
                      "payaso"
                    ],
                    "escritor": [
                      "pescador"
                    ]
                  },
                  {
                    "titulo": [
                      "juan"
                    ],
                    "titulo1": [
                      "fantasma"
                    ],
                    "escritor": [
                      "fermando alonso"
                    ]
                  }
                ]
              }
            ],
            "titulo": [
              "f1"
            ],
            "editorial": [
              "dazn"
            ],
            "fecha": [
              "2017"
            ],
            "ISBN": [
              "9788408237044"
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