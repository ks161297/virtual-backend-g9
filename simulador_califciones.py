from faker import Faker
from faker.providers import person

fake = Faker()
fake.add_provider(person)

for alumno in range(1, 51):
    nombre = fake.first_name()
    apellido = fake.last_name()
    correo = fake.email()
    query = f"INSERT INTO ALUMNOS(nombre, apellidos, correo) VALUES ('{nombre}','{apellido}','{correo}');"
    print(query)

for alumno_curso in range(75):
    curso = fake.random_int(1, 5)
    alumno = fake.random_int(1,51)
    query1 = f"INSERT INTO ALUMNOS_CURSO(idAlumno, idCurso) VALUES ('{alumno}','{curso}');"
    print(query1)