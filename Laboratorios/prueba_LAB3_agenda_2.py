from Laboratorio_2_y_3.Clases.agenda import Agenda

agenda = Agenda(5)
agenda.import_Data("Agenda.txt")

for usuario in agenda.registro:
    print(usuario)

ident = 75708115
agenda.eliminar(ident)
agenda.toFile("Agenda2.txt")