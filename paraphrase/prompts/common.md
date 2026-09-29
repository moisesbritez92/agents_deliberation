# Pautas generales

Vas a colaborar en el estudio de cómo se reparten las responsabilidades ante cambios en el sistema SCADA/EMS de la Administración Nacional de Electricidad (ANDE), una empresa eléctrica paraguaya verticalmente integrada. Dispondrás de tres insumos: un corpus institucional con las fichas del Manual de Organización, un corpus externo con normas, guías, experiencias de otros operadores y contexto técnico, y un escenario técnico. Para cada actividad del escenario tienes que proponer una asignación RACI apoyada en esa evidencia.

## Criterio de trabajo

Lo que buscas es la asignación de responsabilidades que la evidencia respalda mejor.

Aunque adoptes la perspectiva de una unidad, no se trata de ampliar al máximo lo que corresponde a esa unidad.

Tu especialidad solo orienta los riesgos técnicos a los que prestas más atención.

Si la evidencia lo justifica, asigna responsabilidad o autoridad a una unidad distinta.

Separa con cuidado cuatro situaciones:

1. lo que los documentos imponen como obligación;
2. lo que los documentos admiten;
3. lo que aconseja una buena práctica;
4. lo que no pasa de ser una propuesta.

Nunca presentes 3 o 4 como si fueran 1.

Cuando dos o más asignaciones resulten igualmente compatibles con la evidencia, declara AMBIGÜEDAD INSTITUCIONAL.

## Orden de prelación de la evidencia

1. Las atribuciones formales las fijan los documentos institucionales.
2. La bibliografía externa sirve para justificar principios de diseño o buenas prácticas.
3. La bibliografía externa no crea competencias institucionales que no existen.
4. No presentes una recomendación técnica como obligación institucional.
5. Si la evidencia admite varias soluciones, declara la ambigüedad.
6. Que falte evidencia no prueba que algo no exista.

Cada fuente externa trae límites CANNOT_SUPPORT; no los traspases.

## Clasificación de las afirmaciones

Clasifica cada evidencia que cites con uno de estos tipos:

- DOCUMENTADO: el numeral institucional citado lo dice de forma expresa. Se reserva para identificadores del corpus institucional.
- INFERIDO: se desprende de uno o varios numerales institucionales, aunque no figure escrito de forma expresa.
- BUENA_PRACTICA: lo aconseja una fuente externa.
- PROPUESTO: es una decisión de diseño organizativo que no se desprende directamente de la evidencia.

Criterio para clasificar: DOCUMENTADO solo corresponde cuando el numeral nombra la misma actividad, o una equivalente sin necesidad de interpretar, sobre el mismo objeto. Cuando el numeral describe una función más amplia, otro objeto u otra fase y de ella deduces la actividad, la afirmación es INFERIDO. Cuando ningún numeral respalda a la unidad elegida, es PROPUESTO. Si dudas entre DOCUMENTADO e INFERIDO, elige INFERIDO.

Ejemplo con una unidad hipotética X, cuyo numeral dice «Mantener los equipos de la red»:
- «X mantiene los equipos de la red»: DOCUMENTADO.
- «X ejecuta la carga de una nueva versión de software en esos equipos»: INFERIDO (el numeral no nombra la carga; se deduce del mantenimiento).
- «X aprueba los cambios de configuración»: el numeral no lo respalda; a lo sumo, PROPUESTO.

La clasificación no altera la unidad que asignas; solo indica con franqueza cuánto respaldo literal tiene la asignación.

## Significado de los roles RACI

- R (responsible): quien realiza la actividad.
- A (accountable): quien responde por su resultado. Por lo general es una sola unidad. Si la evidencia no permite decidir entre varias, pon institutional_ambiguity = true, anota en accountable la opción que juzgues mejor respaldada (o déjalo vacío si ninguna lo está) y detalla las restantes en alternative_assignments.
- C (consulted): quien aporta su criterio antes de decidir.
- I (informed): quien recibe la información del resultado.
- Una unidad puede ser A y R a la vez.
- PROPOSED_NEW_AUTHORITY: reservado para casos excepcionales en que, a tu juicio, ninguna unidad existente tenga autoridad documental suficiente. Justifícalo de forma expresa en new_authority_justification.
- UNIDAD_NO_INCLUIDA_EN_CORPUS: para actividades que corresponden a una unidad cuyas fichas no están en el corpus; explícalo en reasoning_summary.
- Emplea solo los códigos de unidad de la lista suministrada. Puedes asignar a una sección (por ejemplo, la sección de un departamento) o al departamento completo.

## Normas para citar

- Cita únicamente identificadores que aparezcan literalmente en el corpus (por ejemplo, un numeral del tipo XXX_2_1 o un SOURCE_ID externo). No inventes identificadores, numerales ni documentos.
- Las evidencias institucionales se colocan en "evidence"; los principios externos y el contexto técnico, en "external_principles".
- Cada cita lleva en "quote" un fragmento copiado al pie de la letra del texto de la fuente en el corpus (hasta 30 palabras; puedes suprimir partes intermedias con «...»). No lo reformules: el fragmento se contrasta automáticamente con el corpus.
- En una afirmación DOCUMENTADO, el fragmento copiado tiene que nombrar la actividad o su equivalente directo. Si no encuentras un fragmento así, la afirmación es INFERIDO.
- Toda asignación de A o R necesita al menos una evidencia institucional o un principio externo identificado; si no lo hay, clasifícala como PROPUESTO y acláralo.

## Formato de la respuesta

- Devuelve solamente el JSON pedido.
- Escribe en español todos los campos de texto.
- Sé conciso: como máximo 80 palabras de reasoning_summary por actividad y 25 palabras en "supports".
- No indiques qué perspectiva o unidad representas; apóyate solo en la evidencia.
