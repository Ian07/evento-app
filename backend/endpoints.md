# Endpoints

## Persona
| Método | URI                   | Descripción                  |
|--------|-----------------------|------------------------------|
| GET    | /personas             | Devuelve todas las personas  |
| GET    | /personas/{documento} | Devuelve info de una persona |
| POST   | /personas             | Crea una persona             |
| PUT    | /personas/{documento} | Modifica una persona         |
| DELETE | /personas/{documento} | Borra una persona            |

| Método | URI                                | Descripción                                              |
|--------|------------------------------------|----------------------------------------------------------|
| GET    | /personas/{documento}/alumnos      | Devuelve todos los alumnos asociados a esa persona       |
| GET    | /personas/{documento}/alumnos/{id} | Devuelve informacion de un alumno asociado a esa persona |
| POST   | /personas/{documento}/alumnos      | Agrega un rol de alumno a la persona asociada            |
| PUT    | /personas/{documento}/alumnos/{id} | Modifica información del alumno asociado a esa persona   |
| DELETE | /personas/{documento}/alumnos/{id} | Borra el rol alumno asociado a esa persona               |

| Método | URI                                   | Descripción                                                |
|--------|---------------------------------------|------------------------------------------------------------|
| GET    | /personas/{documento}/profesores      | Devuelve todos los profesores asociados a esa persona      |
| GET    | /personas/{documento}/profesores/{id} | Devuelve informacion de un profesor asociado a esa persona |
| POST   | /personas/{documento}/profesores      | Agrega un rol de profesor a la persona asociada            |
| PUT    | /personas/{documento}/profesores/{id} | Modifica información del profesor asociado a esa persona   |
| DELETE | /personas/{documento}/profesores/{id} | Borra el rol profesor asociado a esa persona               |

| Método | URI                                    | Descripción                                                  |
|--------|----------------------------------------|--------------------------------------------------------------|
| GET    | /personas/{documento}/disertantes      | Devuelve todos los disertantes asociados a esa persona       |
| GET    | /personas/{documento}/disertantes/{id} | Devuelve informacion de un disertante asociado a esa persona |
| POST   | /personas/{documento}/disertantes      | Agrega un rol de disertante a la persona asociada            |
| PUT    | /personas/{documento}/disertantes/{id} | Modifica información del disertante asociado a esa persona   |
| DELETE | /personas/{documento}/disertantes/{id} | Borra el rol disertante asociado a esa persona               |

| Método | URI                                      | Descripción                                                   |
|--------|------------------------------------------|---------------------------------------------------------------|
| GET    | /personas/{documento}/organizadores      | Devuelve todos los organizadores asociados a esa persona      |
| GET    | /personas/{documento}/organizadores/{id} | Devuelve informacion de un organizador asociado a esa persona |
| POST   | /personas/{documento}/organizadores      | Agrega un rol de organizador a la persona asociada            |
| PUT    | /personas/{documento}/organizadores/{id} | Modifica información del organizador asociado a esa persona   |
| DELETE | /personas/{documento}/organizadores/{id} | Borra el rol organizador asociado a esa persona               |

| Método | URI                                 | Descripción                                               |
|--------|-------------------------------------|-----------------------------------------------------------|
| GET    | /personas/{documento}/usuarios      | Devuelve todos los usuarios asociados a esa persona       |
| GET    | /personas/{documento}/usuarios/{id} | Devuelve informacion de un usuario asociado a esa persona |
| POST   | /personas/{documento}/usuarios      | Agrega un usuario a la persona asociada                   |
| PUT    | /personas/{documento}/usuarios/{id} | Modifica información de un usuario asociado a esa persona |
| DELETE | /personas/{documento}/usuarios/{id} | Borra el usuario asociado a esa persona                   |


## Alumnos
| Método | URI            | Descripción                        |
|--------|----------------|------------------------------------|
| GET    | /alumnos       | Devuelve todos los alumnos         |
| GET    | /alumnos/{id}  | Devuelve informacion de un alumno  |
| POST   | /alumnos       | Crea un nuevo alumno               |
| PUT    | /alumnos/{id}  | Modifica información de un alumno  |
| DELETE | /alumnos/{id}  | Borra el alumno                    |

## Profesores
| Método | URI               | Descripción                         |
|--------|-------------------|-------------------------------------|
| GET    | /profesores       | Devuelve todos los profesores       |
| GET    | /profesores/{id}  | Devuelve informacion de un profesor |
| POST   | /profesores       | Crea un profesor                    |
| PUT    | /profesores/{id}  | Modifica información de un profesor |
| DELETE | /profesores/{id}  | Borra el profesor                   |

## Disertantes
| Método | URI               | Descripción                           |
|--------|-------------------|---------------------------------------|
| GET    | /diserantes       | Devuelve todos los diserantes         |
| GET    | /diserantes/{id}  | Devuelve informacion de un disertante |
| POST   | /disertantes      | Crea un disertante                    |
| PUT    | /diserantes/{id}  | Modifica información de un disertante |
| DELETE | /diserantes/{id}  | Borra el disertante                   |


## Organizadores
| Método | URI                  | Descripción                            |
|--------|----------------------|----------------------------------------|
| GET    | /organizadores       | Devuelve todos los organizadores       |
| GET    | /organizadores/{id}  | Devuelve informacion de un organizador |
| POST   | /organizadores       | Crea un organizador                    |
| PUT    | /organizadores/{id}  | Modifica información de un organizador |
| DELETE | /organizadores/{id}  | Borra el organizador                   |

## Usuarios
| Método | URI            | Descripción                        |
|--------|----------------|------------------------------------|
| GET    | /usuarios      | Devuelve todos los usuarios        |
| GET    | /usuarios/{id} | Devuelve informacion de un usuario |
| POST   | /usuarios      | Crea un usuario                    |
| PUT    | /usuarios/{id} | Modifica información de un usuario |
| DELETE | /usuarios/{id} | Borra el usuario                   |

## Cursos
| Método | URI          | Descripción                      |
|--------|--------------|----------------------------------|
| GET    | /cursos      | Devuelve todos los cursos        |
| GET    | /cursos/{id} | Devuelve información de un curso |
| POST   | /cursos      | Crea un nuevo curso              |
| PUT    | /cursos/{id} | Modifica información de un curso |
| DELETE | /cursos/{id} | Borra el curso                   |

| Método | URI                     | Descripción                       |
|--------|-------------------------|-----------------------------------|
| GET    | /cursos/{id}/profesores | Devuelve los profesores del curso |
| GET    | /cursos/{id}/alumnos    | Devuelve los alumnos del curso    |
| GET    | /cursos/{id}/clases     | Devuelve las clases del curso     |

## Clases
| Método | URI          | Descripción                       |
|--------|--------------|-----------------------------------|
| GET    | /clases      | Devuelve todos los clases         |
| GET    | /clases/{id} | Devuelve información de una clase |
| POST   | /clases      | Crea una nueva clase              |
| PUT    | /clases/{id} | Modifica información de una clase |
| DELETE | /clases/{id} | Borra la clase                    |

| Método | URI                     | Descripción                                 |
|--------|-------------------------|---------------------------------------------|
| GET    | /clases/{id}/presentes  | Devuelve los alumnoes presentes en la clase |

## Charla
| Método | URI          | Descripción                         |
|--------|--------------|-------------------------------------|
| GET    | /charlas      | Devuelve todos los charlas         |
| GET    | /charlas/{id} | Devuelve información de una charla |
| POST   | /charlas      | Crea una nueva charla              |
| PUT    | /charlas/{id} | Modifica información de una charla |
| DELETE | /charlas/{id} | Borra la clase                     |

| Método | URI                       | Descripción                           |
|--------|---------------------------|---------------------------------------|
| GET    | /charlas/{id}/disertantes | Devuelve los disertantes de la charla |