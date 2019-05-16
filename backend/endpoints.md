# Endpoints

## Persona
| Método | URI                   | Descripción                  | Realizado          |
|--------|-----------------------|------------------------------|--------------------|
| GET    | /personas             | Devuelve todas las personas  |        si          |
| GET    | /personas/{documento} | Devuelve info de una persona |        si          |
| POST   | /personas             | Crea una persona             |        si          |
| PUT    | /personas/{documento} | Modifica una persona         |        si          |
| DELETE | /personas/{documento} | Borra una persona            |        si          |

| Método | URI                                | Descripción                                              | Realizado          | 
|--------|------------------------------------|----------------------------------------------------------|--------------------|
| GET    | /personas/{documento}/alumnos      | Devuelve todos los alumnos asociados a esa persona       |         ?          |
| GET    | /personas/{documento}/alumnos/{id} | Devuelve informacion de un alumno asociado a esa persona |                    |
| POST   | /personas/{documento}/alumnos      | Agrega un rol de alumno a la persona asociada            |         si         |
| PUT    | /personas/{documento}/alumnos/{id} | Modifica información del alumno asociado a esa persona   |                    |
| DELETE | /personas/{documento}/alumnos/{id} | Borra el rol alumno asociado a esa persona               |                    |

| Método | URI                                   | Descripción                                                | Realizado          |
|--------|---------------------------------------|------------------------------------------------------------|--------------------|
| GET    | /personas/{documento}/profesores      | Devuelve todos los profesores asociados a esa persona      |                    |
| GET    | /personas/{documento}/profesores/{id} | Devuelve informacion de un profesor asociado a esa persona |                    |
| POST   | /personas/{documento}/profesores      | Agrega un rol de profesor a la persona asociada            |         si         |
| PUT    | /personas/{documento}/profesores/{id} | Modifica información del profesor asociado a esa persona   |                    |
| DELETE | /personas/{documento}/profesores/{id} | Borra el rol profesor asociado a esa persona               |                    |

| Método | URI                                    | Descripción                                                  | Realizado          |
|--------|----------------------------------------|--------------------------------------------------------------|--------------------|
| GET    | /personas/{documento}/disertantes      | Devuelve todos los disertantes asociados a esa persona       |                    |
| GET    | /personas/{documento}/disertantes/{id} | Devuelve informacion de un disertante asociado a esa persona |                    |
| POST   | /personas/{documento}/disertantes      | Agrega un rol de disertante a la persona asociada            |        si          |
| PUT    | /personas/{documento}/disertantes/{id} | Modifica información del disertante asociado a esa persona   |                    |
| DELETE | /personas/{documento}/disertantes/{id} | Borra el rol disertante asociado a esa persona               |                    |

| Método | URI                                      | Descripción                                                   | Realizado          |
|--------|------------------------------------------|---------------------------------------------------------------|--------------------|
| GET    | /personas/{documento}/organizadores      | Devuelve todos los organizadores asociados a esa persona      |                    |
| GET    | /personas/{documento}/organizadores/{id} | Devuelve informacion de un organizador asociado a esa persona |                    |
| POST   | /personas/{documento}/organizadores      | Agrega un rol de organizador a la persona asociada            |        si          |
| PUT    | /personas/{documento}/organizadores/{id} | Modifica información del organizador asociado a esa persona   |                    |
| DELETE | /personas/{documento}/organizadores/{id} | Borra el rol organizador asociado a esa persona               |                    |

| Método | URI                                 | Descripción                                               | Realizado          |
|--------|-------------------------------------|-----------------------------------------------------------|--------------------|
| GET    | /personas/{documento}/usuarios      | Devuelve todos los usuarios asociados a esa persona       |                    |
| GET    | /personas/{documento}/usuarios/{id} | Devuelve informacion de un usuario asociado a esa persona |                    |
| POST   | /personas/{documento}/usuarios      | Agrega un usuario a la persona asociada                   |                    |
| PUT    | /personas/{documento}/usuarios/{id} | Modifica información de un usuario asociado a esa persona |                    |
| DELETE | /personas/{documento}/usuarios/{id} | Borra el usuario asociado a esa persona                   |                    |


## Alumnos
| Método | URI            | Descripción                        | Realizado          |
|--------|----------------|------------------------------------|--------------------|
| GET    | /alumnos       | Devuelve todos los alumnos         |         si         |
| GET    | /alumnos/{id}  | Devuelve informacion de un alumno  |         si         |
| POST   | /alumnos       | Crea un nuevo alumno               |         si         |
| PUT    | /alumnos/{id}  | Modifica información de un alumno  |                    |
| DELETE | /alumnos/{id}  | Borra el alumno                    |         si         |

## Profesores
| Método | URI               | Descripción                         | Realizado          |
|--------|-------------------|-------------------------------------|--------------------|
| GET    | /profesores       | Devuelve todos los profesores       |        si          |
| GET    | /profesores/{id}  | Devuelve informacion de un profesor |        si          |
| POST   | /profesores       | Crea un profesor                    |        si          |
| PUT    | /profesores/{id}  | Modifica información de un profesor |                    |
| DELETE | /profesores/{id}  | Borra el profesor                   |        si          |

## Disertantes
| Método | URI               | Descripción                           | Realizado          |
|--------|-------------------|---------------------------------------|--------------------|
| GET    | /diserantes       | Devuelve todos los diserantes         |        si          |
| GET    | /diserantes/{id}  | Devuelve informacion de un disertante |        si          |
| POST   | /disertantes      | Crea un disertante                    |        si          |
| PUT    | /diserantes/{id}  | Modifica información de un disertante |                    |
| DELETE | /diserantes/{id}  | Borra el disertante                   |        si          |


## Organizadores
| Método | URI                  | Descripción                            | Realizado          |
|--------|----------------------|----------------------------------------|--------------------|
| GET    | /organizadores       | Devuelve todos los organizadores       |         si         |
| GET    | /organizadores/{id}  | Devuelve informacion de un organizador |         si         |
| POST   | /organizadores       | Crea un organizador                    |         si         |
| PUT    | /organizadores/{id}  | Modifica información de un organizador |                    |
| DELETE | /organizadores/{id}  | Borra el organizador                   |         si         |

## Usuarios
| Método | URI            | Descripción                        | Realizado          |
|--------|----------------|------------------------------------|--------------------|
| GET    | /usuarios      | Devuelve todos los usuarios        |                    |
| GET    | /usuarios/{id} | Devuelve informacion de un usuario |                    |
| POST   | /usuarios      | Crea un usuario                    |                    |
| PUT    | /usuarios/{id} | Modifica información de un usuario |                    |
| DELETE | /usuarios/{id} | Borra el usuario                   |                    |

## Cursos
| Método | URI          | Descripción                      | Realizado          |
|--------|--------------|----------------------------------|--------------------|
| GET    | /cursos      | Devuelve todos los cursos        |         si         |
| GET    | /cursos/{id} | Devuelve información de un curso |         si         |
| POST   | /cursos      | Crea un nuevo curso              |         si         |
| PUT    | /cursos/{id} | Modifica información de un curso |         si         |
| DELETE | /cursos/{id} | Borra el curso                   |         si         |

| Método | URI                     | Descripción                       | Realizado          |
|--------|-------------------------|-----------------------------------|--------------------|
| GET    | /cursos/{id}/profesores | Devuelve los profesores del curso |       si           |
| GET    | /cursos/{id}/alumnos    | Devuelve los alumnos del curso    |       si           |
| GET    | /cursos/{id}/clases     | Devuelve las clases del curso     |       si           |

## Clases
| Método | URI          | Descripción                       | Realizado          |
|--------|--------------|-----------------------------------|--------------------|
| GET    | /clases      | Devuelve todos los clases         |        si          |
| GET    | /clases/{id} | Devuelve información de una clase |        si          |
| POST   | /clases      | Crea una nueva clase              |        si          |
| PUT    | /clases/{id} | Modifica información de una clase |        si          |
| DELETE | /clases/{id} | Borra la clase                    |        si          |

| Método | URI                     | Descripción                                 | Realizado          |
|--------|-------------------------|---------------------------------------------|--------------------|
| GET    | /clases/{id}/presentes  | Devuelve los alumnos presentes en la clase  |                    |

## Charla
| Método | URI          | Descripción                         | Realizado          |
|--------|--------------|-------------------------------------|--------------------|
| GET    | /charlas      | Devuelve todos los charlas         |        si          |
| GET    | /charlas/{id} | Devuelve información de una charla |        si          |
| POST   | /charlas      | Crea una nueva charla              |        si          |
| PUT    | /charlas/{id} | Modifica información de una charla |        si          |
| DELETE | /charlas/{id} | Borra la clase                     |        si          |

| Método | URI                       | Descripción                           | Realizado          |
|--------|---------------------------|---------------------------------------|--------------------|
| GET    | /charlas/{id}/disertantes | Devuelve los disertantes de la charla |                    |