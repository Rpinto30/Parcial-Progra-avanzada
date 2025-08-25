from questions import *

questions_list = [
    # Preguntas de eleccion multiple
    MultipleChoiceQuestion("¿Quién compuso la canción Luna de Xelajú?",
                           ["Miguel Angel Asturias", "Paco Pérez", "Ricardo Arjona"], 1),
    MultipleChoiceQuestion("¿Cuál es el tercer planeta del sistema solar?", ["Venus", "Tierra", "Marte"],
                           1),
    MultipleChoiceQuestion("¿Qué se celebra el 15 de septiembre en Guatemala?", ["Quema del diablo", "Semana Santa", "Independencia"],
                           2),
    MultipleChoiceQuestion("¿De quién es la canción Almohada?", ["José José", "Juan Gabriel", "Luis Miguel"],
                           0),
    MultipleChoiceQuestion("¿Cuál es el libro sagrado de los Mayas?", ["Popol Vuh", "Kik'aslemaal", "Ri tzij kek'iyik"],
                           0),
    # Preguntas de verdadero o falso
    MultipleChoiceQuestion("¿Guatemala tiene 21 departamentos?", ["Verdadero", "Falso"], 1),
    MultipleChoiceQuestion("¿El cuerpo de un adulto tiene 206 huesos?", ["Verdadero", "Falso"], 0),
    MultipleChoiceQuestion("¿El primer día de Semana Santa se llama domingo de resurrección ?",
                       ["Verdadero", "Falso"], 1),
    MultipleChoiceQuestion("¿Los fundadores de Microsoft son Bill Gates y Paul Allen?", ["Verdadero", "Falso"], 0),
    MultipleChoiceQuestion("¿El creador de la Odisea es Homero Simpson?", ["Verdadero", "Falso"], 1),
    # Preguntas de completar la frase
    WritingsQuestion("El sol es a día como Luna es a _____", "noche"),
    WritingsQuestion("Quien madruga Dios lo _____", "ayuda"),
    WritingsQuestion("Pescadito Ruiz es a ________ lo que Pelé es a Brasil", "guatemala"),
    WritingsQuestion("Kak ik es a comida como Marimba es a ______", "musica"),
    WritingsQuestion("Chofer es a Tuc Tuc como piloto a _____", "avion"),
    # Preguntas de respuesta directa
    WritingsQuestion("¿Cuál es el primer nombre del autor del Don Quijote de la Mancha?", "miguel"),
    WritingsQuestion("¿Cuál es el país más poblado del mundo?", "india"),
    WritingsQuestion("¿Qué país se le conoce como el “País del Sol Naciente”?", "japon"),
    WritingsQuestion("¿Cómo se llama el padre de todo en la mitología griega?", "zeus"),
    WritingsQuestion("¿Cómo se llama el ave nacional de Guatemala?", "quetzal")

]

