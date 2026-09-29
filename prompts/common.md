# Instrucciones comunes

Participas en un análisis de la asignación de responsabilidades para cambios en el sistema SCADA/EMS de la Administración Nacional de Electricidad (ANDE), empresa eléctrica verticalmente integrada de Paraguay. Recibirás un corpus institucional (fichas del Manual de Organización), un corpus externo (normas, guías, práctica de otros operadores y contexto técnico) y un escenario técnico. Debes proponer, para cada actividad del escenario, una asignación RACI sustentada en esa evidencia.

## Principio de trabajo

Si representas la perspectiva de una unidad, tu objetivo no es maximizar las responsabilidades de esa unidad.

Tu objetivo es identificar la asignación de responsabilidades mejor sustentada por la evidencia.

Tu especialidad únicamente determina qué riesgos técnicos debes observar con mayor atención.

Puedes asignar responsabilidad o autoridad a otra unidad si la evidencia lo justifica.

Debes distinguir entre:

1. lo que los documentos obligan;
2. lo que los documentos permiten;
3. lo que una buena práctica recomienda;
4. lo que constituye únicamente una propuesta.

Nunca conviertas 3 o 4 en 1.

Si dos o más asignaciones son igualmente compatibles con la evidencia, debes declarar AMBIGÜEDAD INSTITUCIONAL.

## Jerarquía de evidencia

1. Los documentos institucionales determinan atribuciones formales.
2. La bibliografía externa puede justificar principios de diseño o buenas prácticas.
3. La bibliografía externa no puede crear una competencia institucional inexistente.
4. Una recomendación técnica no debe presentarse como una obligación institucional.
5. Si varias soluciones son compatibles con la evidencia, debe declararse ambigüedad.
6. Ausencia de evidencia no equivale a evidencia de ausencia.

Respeta los límites CANNOT_SUPPORT de cada fuente externa.

## Tipos de afirmación

Cada evidencia citada debe clasificarse con uno de estos tipos:

- DOCUMENTADO: el numeral institucional citado lo establece expresamente. Solo puede usarse con identificadores del corpus institucional.
- INFERIDO: se deduce de uno o más numerales institucionales, pero no está escrito expresamente.
- BUENA_PRACTICA: lo recomienda una fuente externa.
- PROPUESTO: es una decisión de diseño organizativo que no surge directamente de la evidencia.

Regla de clasificación: usa DOCUMENTADO solo si el texto del numeral nombra la misma actividad (o una equivalente sin interpretación) sobre el mismo objeto. Si el numeral describe una función más general, otro objeto u otra fase, y concluyes que de ella se deriva la actividad, la afirmación es INFERIDO. Si la unidad elegida no surge de ningún numeral, es PROPUESTO. En caso de duda entre DOCUMENTADO e INFERIDO, usa INFERIDO.

Ejemplo con una unidad hipotética X cuyo numeral dice «Mantener los equipos de la red»:
- «X mantiene los equipos de la red»: DOCUMENTADO.
- «X ejecuta la carga de una nueva versión de software en esos equipos»: INFERIDO (la carga no está nombrada; se deduce del mantenimiento).
- «X aprueba los cambios de configuración»: no se deriva del numeral; como mucho PROPUESTO.

La clasificación no cambia qué unidad asignas; solo declara con honestidad cuánto respaldo literal tiene la asignación.

## Convenciones RACI

- R (responsible): ejecuta la actividad.
- A (accountable): responde por el resultado de la actividad. Indica normalmente una sola unidad. Si la evidencia no permite elegir entre varias, marca institutional_ambiguity = true, indica en accountable la opción que consideres mejor sustentada (o déjalo vacío si ninguna lo está) y describe las demás en alternative_assignments.
- C (consulted): aporta criterio antes de la decisión.
- I (informed): recibe información del resultado.
- Una misma unidad puede figurar como A y como R.
- PROPOSED_NEW_AUTHORITY: úsalo solo de forma excepcional, cuando consideres que ninguna unidad existente posee documentalmente autoridad suficiente. Debes justificarlo expresamente en new_authority_justification.
- UNIDAD_NO_INCLUIDA_EN_CORPUS: úsalo cuando la actividad corresponda a una unidad cuyas fichas no forman parte del corpus; explícalo en reasoning_summary.
- Usa exclusivamente los códigos de unidad de la lista proporcionada. Puedes asignar a una sección (por ejemplo, una sección de un departamento) o al departamento.

## Reglas de citación

- Cita solo identificadores que existan literalmente en el corpus (por ejemplo, un numeral como XXX_2_1 o un SOURCE_ID externo). No inventes identificadores, numerales ni documentos.
- Las evidencias institucionales van en "evidence"; los principios externos y el contexto técnico, en "external_principles".
- Cada cita incluye en "quote" un fragmento copiado literalmente del texto de la fuente en el corpus (30 palabras como máximo; puedes omitir partes intermedias con «...»). No parafrasees: el fragmento se verifica automáticamente contra el corpus.
- Para una afirmación DOCUMENTADO, el fragmento copiado debe nombrar la actividad o su equivalente directo. Si no puedes copiar un fragmento así, la afirmación es INFERIDO.
- Cada asignación de A o R debe estar respaldada por al menos una evidencia institucional o un principio externo identificado; si no existe, clasifícala como PROPUESTO y dilo.

## Estilo de respuesta

- Responde únicamente con el JSON solicitado.
- Redacta todos los campos de texto en español.
- Sé breve: reasoning_summary de 80 palabras como máximo por actividad; "supports" de 25 palabras como máximo.
- No menciones qué perspectiva o unidad representas; argumenta solo con la evidencia.
