# Guía de validación humana

Esta guía explica cómo realizar las tareas en las que intervienen personas. Ninguna de ellas decide la matriz RACI: la matriz sale solo de los agentes. Las personas verifican dos cosas:

1. que el material entregado a los agentes no incline la balanza (antes del piloto);
2. que las citas de los agentes digan lo que afirman (después del piloto).

Hay una tercera tarea, opcional, que mide el sesgo humano en lugar de usarlo como referencia.

## Calendario

| Parte | Cuándo | Por qué en ese momento |
|---|---|---|
| A. Revisión de neutralidad del material | **Antes del piloto** | Después, el material queda congelado; cambiarlo invalida las repeticiones |
| B. Auditoría de citas | **Después del piloto** | Necesita las citas que producen los agentes |
| C. Línea base humana (opcional) | Antes de mostrar resultados a los participantes | Si ven lo que respondieron los agentes, sus respuestas se contaminan |

## Quiénes pueden participar

Regla general: **nadie de las unidades en disputa** (GT/DAS, DTE/ISC, DTE/MCO, GT/ODC) ni de sus jefaturas directas, y nadie que haya participado en la redacción del artículo.

Perfiles adecuados:

- personal técnico de otra gerencia con conocimiento de SCADA/EMS o de sistemas de control;
- un académico de ingeniería eléctrica o de sistemas;
- un profesional habituado a leer normativa (asesoría jurídica, organización y métodos).

Se necesitan **2 personas** para la parte B y **1 o 2** para la parte A. Pueden ser las mismas.

Registrar en la bitácora el perfil de cada participante (cargo genérico, área, relación con las unidades en disputa), sin datos personales.

---

## Parte A. Revisión de neutralidad del material (antes del piloto)

### Qué se revisa

- `scenarios.json`: los 10 escenarios.
- `activities.json`: el catálogo de 20 actividades.
- `corpus_external.md`: las 37 fuentes externas y su CAN_SUPPORT / CANNOT_SUPPORT.

No se entrega la RACI del artículo ni ningún resultado de los agentes.

### Qué debe responder el revisor

**Importante:** el revisor no asigna unidades. Si responde «ISC» o «MCO», está haciendo otra tarea (asignación). Antes de entregar la plantilla, explicar la diferencia entre una pista técnica (aceptable) y una pista prescriptiva (a corregir), con los ejemplos de la plantilla. La primera revisión recibida (ver BITACORA, 2026-09-25) confundió ambas tareas.

Para cada escenario:

1. ¿La descripción menciona o sugiere qué unidad debe hacer algo? (sí / no; indicar la frase)
2. ¿El riesgo descrito enfatiza la perspectiva de alguna unidad en particular? (sí / no; cuál)
3. ¿Falta algún hecho técnico necesario para decidir, o sobra alguno que empuje hacia una respuesta?

Para el catálogo de actividades:

4. ¿Alguna actividad está redactada de forma que ya implique quién la hace?
5. ¿Hay actividades que deberían separarse o unirse porque la división actual presupone una solución?

Para el corpus externo:

6. ¿Alguna fuente, o su CAN_SUPPORT, favorece a una unidad concreta?
7. ¿Falta alguna fuente relevante que apoyaría otra lectura?

### Qué hacer con las observaciones

- Cada observación se registra en la bitácora con su respuesta: aceptada (se corrige el material) o rechazada (con motivo).
- Si se corrige el material, se repite el smoke test y se registra la nueva versión con sus hashes.
- Esta revisión solo puede quitar sesgo de redacción. No se usa para cambiar escenarios con el fin de obtener más o menos acuerdo.

Plantilla: `plantilla_revision_neutralidad.md`, en esta carpeta.

---

## Parte B. Auditoría de citas (después del piloto)

### Paso 1. Preparar las planillas (coordinador)

Desde `experimento/`:

```bash
python citation_audit.py extract --label pilot
python citation_audit.py sample  --label pilot --n 100 --hide-assignment
```

Se generan en `results/pilot/`:

- `audit_sheet_coder1.csv` y `audit_sheet_coder2.csv`: idénticas, una para cada codificador;
- `audit_key.csv`: correspondencia entre ítems y citas. **No se entrega a los codificadores.**

`--hide-assignment` oculta las columnas A y R. El texto de la afirmación puede mencionar unidades; es inevitable y no invalida la tarea, porque lo que se juzga es la relación entre afirmación y texto.

La muestra es aleatoria y estratificada por tipo de afirmación, con semilla fija (2026). No se eligen citas a mano.

### Paso 2. Entregar a cada codificador

Entregar por separado:

- su planilla (`audit_sheet_coder1.csv` o `audit_sheet_coder2.csv`), abierta en Excel o LibreOffice;
- la sección «Instrucciones para los codificadores» de esta guía (copiarla en un documento aparte).

No entregar nada más: ni el artículo, ni la RACI, ni resultados, ni la bitácora.

### Paso 3. Codificación

Cada codificador trabaja **solo**, sin hablar con el otro hasta que ambos entreguen. Tiempo estimado: 2-3 horas para 100 citas. Puede hacerse en varias sesiones.

### Paso 4. Calcular la concordancia (coordinador)

1. Guardar las planillas completadas en `results/pilot/` con los mismos nombres.
2. Opcional, si se quiere calibrar al juez automático sobre las mismas citas:

   ```bash
   python citation_audit.py judge --label pilot --n 600
   ```

   El juez siempre incluye los 100 ítems humanos.
3. Ejecutar:

   ```bash
   python citation_audit.py report --label pilot
   ```

Resultado en `citation_audit_report.md`:

- kappa entre codificadores para la pertinencia y para el tipo de afirmación;
- kappa entre el juez y el consenso humano;
- tasa de citas que respaldan lo afirmado, con intervalo de Wilson.

### Paso 5. Interpretar

| Kappa | Lectura habitual |
|---|---|
| < 0,40 | Acuerdo débil: revisar si las instrucciones son ambiguas antes de usar los resultados |
| 0,40-0,60 | Moderado |
| 0,60-0,80 | Sustancial |
| > 0,80 | Casi perfecto |

- Si el kappa entre humanos es bajo, el problema está en la tarea, no en los agentes: se revisan las instrucciones y se recodifica una muestra nueva.
- Si el kappa entre juez y humanos es aceptable (≥ 0,60), las tasas del juez sobre 600 citas pueden reportarse en el artículo como medida validada.
- Si es bajo, se reportan solo las tasas humanas (100 citas) y el juez queda como limitación.

### Paso 6. Resolver desacuerdos (después de calcular el kappa)

Los ítems en que los codificadores difieren se discuten en una reunión breve, y se registra la resolución. El kappa se calcula **antes** de esta reunión; la reunión no lo modifica.

### Alternativa si no hay codificadores neutrales

Si no se consiguen dos personas ajenas al conflicto, no se hace la codificación humana. Se sustituye por dos jueces LLM de modelos distintos, con su concordancia, y se declara como limitación. Es preferible a usar codificadores de las unidades en disputa.

---

## Instrucciones para los codificadores

*(Copiar esta sección en un documento aparte y entregarla con la planilla.)*

Recibirás una planilla con citas. Cada fila contiene:

- **activity**: una actividad del proceso de cambio de un sistema SCADA/EMS;
- **claim_type**: cómo clasificó el autor su afirmación (DOCUMENTADO, INFERIDO, BUENA_PRACTICA o PROPUESTO);
- **claim**: la afirmación del autor;
- **source_id** y **source_text**: la fuente citada y su texto literal.

No sabrás quién hizo la afirmación. No necesitas saberlo.

**Tu tarea es juzgar solo si el texto de la fuente respalda la afirmación.** No juzgues si la asignación de responsabilidades te parece buena, conveniente o justa.

Completa dos columnas en cada fila:

**1. support**, con uno de estos valores:

- `SUPPORTS`: el texto respalda la afirmación tal como está formulada.
- `PARTIAL`: la respalda solo en parte, o la afirmación dice más de lo que dice el texto.
- `DOES_NOT_SUPPORT`: el texto no respalda la afirmación o trata otro asunto.

**2. claim_type_correct**, con `SI` o `NO`: ¿la clasificación del autor es correcta?

- DOCUMENTADO es correcto solo si el texto dice **expresamente** la actividad. Si hay que interpretar, no es DOCUMENTADO.
- INFERIDO: se deduce razonablemente del texto, sin estar escrito.
- BUENA_PRACTICA: lo recomienda una fuente externa (norma, guía, práctica de otra empresa).
- PROPUESTO: es una decisión de diseño que no surge del texto.

La columna **note** es opcional: usa una frase si dudas o si el caso es límite.

Reglas:

1. Juzga solo con el texto que aparece en la fila. No uses tu conocimiento de cómo se trabaja en la empresa para completar lo que el texto no dice.
2. Sé estricto con DOCUMENTADO. Ejemplo: «coordinar la operación de las instalaciones» no documenta «certificar los datos de la instalación».
3. No modifiques las demás columnas ni el orden de las filas.
4. No consultes a la otra persona que codifica, ni documentos externos, hasta haber entregado.
5. Si una fila te resulta imposible de juzgar, déjala vacía y explica por qué en note.

---

## Parte C. Línea base humana (opcional)

### Objetivo

Medir el sesgo de defensa de la propia unidad, **no** obtener la respuesta correcta. Si los expertos de cada unidad se asignan más responsabilidad a sí mismos que el agente con su misma perspectiva, esa diferencia cuantifica el sesgo departamental.

### Procedimiento

1. Un experto por unidad (DAS, ISC, MCO, ODC), más uno ajeno como equivalente del agente neutral.
2. Cada uno resuelve los mismos 3 o 4 escenarios con el mismo formato que los agentes: A, R, C e I por actividad, más el numeral que lo justifica. Recibe solo el corpus institucional y los escenarios.
3. Responde por escrito y por separado, sin deliberación y sin conocer los resultados de los agentes.
4. Se compara con los agentes de la fase 1:
   - frecuencia con que cada experto se asigna la A frente a su agente;
   - concordancia entre expertos frente a concordancia entre agentes.

### Cautelas

- Con un experto por unidad, el resultado es un estudio de casos, no una estimación estadística.
- Participación voluntaria, respuestas anónimas en el informe y consentimiento de las jefaturas. Las respuestas no deben usarse para evaluar a las personas ni a las unidades.

---

## Registro

Cada paso realizado se anota en `../BITACORA.md` con fecha, etiqueta [VALIDACIÓN], participantes (solo perfil), archivos generados y resultados.
