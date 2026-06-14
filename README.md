# Gestión de Datos de Países

Aplicación de consola desarrollada en Python para la materia Programación 1 de la
Tecnicatura Universitaria en Programación a Distancia.

El programa permite persistir, leer y actualizar información de países en un archivo
**CSV**, aplicando los conceptos de manejo de archivos; abrir, leer,escribir y cerrar
(usando **open()** y bloques **with**), distinguiendo entre los datos volátiles en memoria RAM
y el almacenamiento persistente en disco.

---

##  Lista de contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Uso](#uso)
- [Formato de datos](#formato-de-datos)
- [Autores](#autores)

---

## Características

El menú principal ofrece las siguientes opciones:

1. **Agregar país**: Carga un nuevo registro (nombre, población, superficie, continente) y lo guarda en el CSV, sin borrar los datos previos.
2. **Actualizar datos del país**: Permite modificar la población y la superficie de un país existente.
3. **Buscar país por nombre**: Busca coincidencias parciales por nombre y muestra los datos del país elegido.
4. **Filtrar países**: Filtra por continente, población mínima, máxima y superficie mínima, máxima.
5. **Ordenar países**: Ordena por nombre (A-Z), población o superficie (ascendente/descendente).
6. **Mostrar estadísticas**: Muestra un dashboard con país de mayor y menor población, promedios de población y superficie, y cantidad de países por continente.
7. **Salir**: Cierra el progama

---

## Requisitos

- **Python 3.12** o superior.
- No requiere dependencias externas (solo usa la librería estándar, módulo **csv**).

---

## Uso

Ejecutar el programa desde la raíz del proyecto (importante, porque la ruta al CSV es relativa: **data/paises.csv**):

```bash
python3 main.py
```

Luego seguir las indicaciones del menú en pantalla ingresando el número de la opción deseada.

---

## Formato de datos

Los datos se almacenan en `data/paises.csv` con la siguiente estructura:

- **`nombre`**
  - Tipo: texto
  - Descripción: nombre del país
- **`poblacion`**
  - Tipo: número
  - Descripción: cantidad de habitantes
- **`superficie`**
  - Tipo: número
  - Descripción: superficie en km²
- **`continente`**
  - Tipo: texto
  - Descripción: continente al que pertenece el país

Ejemplo:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
España,47615034,505990,Europa
```


Dataset base de ejemplo:
 
```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
España,47615034,505990,Europa
Francia,67871925,551695,Europa
México,126705138,1964375,América
Canadá,38005238,9984670,América
```
 
---
 
## Ejemplos de uso
 
### Opción 1 – Agregar país
 
Pide los cuatro campos uno por uno, valida cada entrada y guarda el país al final del CSV.
 
```text
| 1: Agregar país   | 2: Actualizar Datos del País | 3: Buscar país por nombre | ---------- |
| 4: Filtrar países | 5: Ordenar países            | 6: Mostrar estadísticas   | 7: Salir   |

Elija la opción del Menú: 1

Ingrese el valor para el campo 'nombre': Argentina

Ingrese el valor para el campo 'poblacion': 45376763

Ingrese el valor para el campo 'superficie': 2780400

Ingrese el valor para el campo 'continente': América

[ NUEVO PAIS (Argentina) GUARDADO CORRECTAMENTE ]

```
 
El CSV queda con la nueva línea agregada al final:
 
```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
```
 
### Opción 2 – Actualizar datos del país
 
Muestra los países con un índice, pide elegir uno y permite actualizar (de forma opcional) la población y/o la superficie.
 
```text
| 1: Agregar país   | 2: Actualizar Datos del País | 3: Buscar país por nombre | ---------- |
| 4: Filtrar países | 5: Ordenar países            | 6: Mostrar estadísticas   | 7: Salir   |

Elija la opción del Menú: 2

[ DEBE ELEGIR UN PAIS Y ACTUALIZAR SUS DATOS ]
| Indice          | País            |
-----------------------------------
| 1               | Argentina       |
| 2               | España          |
| 3               | Francia         |
| 4               | México          |
| 5               | Canadá          |

Esperando indice del país: 1

¿Desea actualizar 'poblacion'? (Y/N): y

Ingrese el valor para el campo 'poblacion': 46000000

¿Desea actualizar 'superficie'? (Y/N): n

[ ÉXITO] - El registro de 'Argentina' ha sido actualizado correctamente

```
 
### Opción 3 – Buscar país por nombre
 
Busca coincidencias parciales sin distinguir mayúsculas. Si hay varias, las lista para elegir.
 
Búsqueda con una sola coincidencia:
 
```text
| 1: Agregar país   | 2: Actualizar Datos del País | 3: Buscar país por nombre | ---------- |
| 4: Filtrar países | 5: Ordenar países            | 6: Mostrar estadísticas   | 7: Salir   |

Elija la opción del Menú: 3

Ingrese el nombre del país: fra

Resultados encontrados:

1. Francia - Europa

========== DATOS DEL PAÍS ==========
Nombre: Francia
Población: 67871925
Superficie: 551695 KM cuadrados
Continente: Europa
====================================

```

### Opción 4 – Filtrar países
 
Pregunta por cada filtro disponible; los criterios activados se combinan (un país aparece solo si cumple todos).
 
```text
| 1: Agregar país   | 2: Actualizar Datos del País | 3: Buscar país por nombre | ---------- |
| 4: Filtrar países | 5: Ordenar países            | 6: Mostrar estadísticas   | 7: Salir   |

Elija la opción del Menú: 4

[ FILTRAR PAÍSES ]

¿Filtrar por continente? [Y/N]: y
Continente: América

¿Filtrar por población mínima? [Y/N]: n

¿Filtrar por población máxima? [Y/N]: n

¿Filtrar por superficie mínima? [Y/N]: n

¿Filtrar por superficie máxima? [Y/N]: n

==================================================
Resultados: 3 paises
==================================================
Argentina | Poblacion: 46000000 | Superficie: 2780400 km² | América
México | Poblacion: 126705138 | Superficie: 1964375 km² | América
Canadá | Poblacion: 38005238 | Superficie: 9984670 km² | América
==================================================
```
 
### Opción 5 – Ordenar países
 
Submenú con cinco criterios de ordenamiento (más la opción 0 para volver). Implementa bubble sort manual.
 
```text
| 1: Agregar país   | 2: Actualizar Datos del País | 3: Buscar país por nombre | ---------- |
| 4: Filtrar países | 5: Ordenar países            | 6: Mostrar estadísticas   | 7: Salir   |

Elija la opción del Menú: 5

===== ORDENAR PAÍSES =====
1. Nombre (A-Z)
2. Población (menor a mayor)
3. Población (mayor a menor)
4. Superficie (menor a mayor)
5. Superficie (mayor a menor)
0. Volver

Seleccione una opción: 2

Países ordenados por población (menor a mayor)

------------------------------------------------------------
Canadá - Población: 38005238 - Superficie: 9984670 km² - América
Argentina - Población: 46000000 - Superficie: 2780400 km² - América
España - Población: 47615034 - Superficie: 505990 km² - Europa
Francia - Población: 67871925 - Superficie: 551695 km² - Europa
México - Población: 126705138 - Superficie: 1964375 km² - América
------------------------------------------------------------

```
 
### Opción 6 – Mostrar estadísticas
 
```text
| 1: Agregar país   | 2: Actualizar Datos del País | 3: Buscar país por nombre | ---------- |
| 4: Filtrar países | 5: Ordenar países            | 6: Mostrar estadísticas   | 7: Salir   |

Elija la opción del Menú: 6

==================================================
      DASHBOARD DE ESTADÍSTICAS
==================================================

POBLACIÓN
Mayor población: México
Habitantes: 126705138
Menor población: Canadá
Habitantes: 38005238
Promedio de población: 65239467

SUPERFICIE
Promedio de superficie: 3157426 km²

PAÍSES POR CONTINENTE
América : 3 país(es)
Europa : 2 país(es)

==================================================

```
 
### Opción 7 – Salir
 
```text
 
| 1: Agregar país   | 2: Actualizar Datos del País | 3: Buscar país por nombre | ---------- |
| 4: Filtrar países | 5: Ordenar países            | 6: Mostrar estadísticas   | 7: Salir   |

Elija la opción del Menú: 7
[ CERRANDO PROGRAMA ...]
```
##
## Participación de los integrantes

El trabajo se organizó mediante control de versiones con Git y GitHub, utilizando ramas por funcionalidad (una rama por ticket de jira) e integrando los cambios mediante **pull requests** hacia las ramas **develop**

### Mario Muñoz

- Estructura inicial del proyecto (rama **UPT1-3**).
- Menú principal con validación de entradas (rama **UPT1-3**).
- Funcionalidad de agregar un nuevo país. Opción 1 (rama **UPT1-3**).
- Actualización de los campos de un país desde el CSV. Opción 2 (rama **UPT1-4**).
- Opción para salir del programa. Opción 7 (rama **feature/add-exit-option**).
- Ordenamiento de las opciones del menú (rama **fix/sort-menu-options**).
- Corrección del import en **menu.py** (rama **UPT1-13**).
- Tareas de integración: revisión y **merge** de los **pull requests** del equipo hacia **develop**.

>**Nota:** En el historial de Git, la rama **UPT1-6** figura con Mario Muñoz como autor, pero el desarrollo correspondió a Franco Santiago Ricardo. La autoría quedó registrada a nombre de Mario porque fue quien resolvió un conflicto de merge en GitHub sobre esa rama.

### Franco Santiago Ricardo

- Búsqueda de países por nombre. Opción 3 (rama **UPT1-5**).
- Ordenamiento de países. Opción 5 (rama **UPT1-7**).
- Muestra estadística / dashboard. Opción 6 (rama **UPT1-8**).
- Filtrado de países por continente y rangos de población y superficie. Opción 4 (rama **UPT1-6**).
- Refactorización en módulos y funciones de búsqueda, ordenamiento y estadísticas (ramas **UPT1-10**, **UPT1-11**, **UPT1-12**).
- Corrección de la opción 4 del menú y la solicitud de valores de parámetros (rama **UPT1-14**).

---

## Autores

- [ Franco Santiago Ricardo ]
- [ Mario Muñoz ]

---

## Enlaces

- Repositorio Pincipal: https://github.com/mariomunozutn/gestion_datos_paises
- Video demostrativo: https://www.youtube.com/watch?v=6F8w1sywF0A
- Documentación PDF: ./documentacion-tpi.pdf
