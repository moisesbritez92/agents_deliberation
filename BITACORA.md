# Bitácora del experimento

Registro cronológico de decisiones de diseño, cambios en el material, ejecuciones y resultados. Cada entrada indica qué se hizo, por qué, y qué efecto tiene sobre la comparabilidad. No se borran entradas: las correcciones se añaden como entradas nuevas.

Convención: **[DISEÑO]** decisión metodológica; **[MATERIAL]** cambio en prompts, corpus o escenarios (cambia los hashes); **[EJECUCIÓN]** corrida con la API; **[CÓDIGO]** cambio en scripts sin efecto sobre lo que ven los agentes; **[HALLAZGO]** resultado relevante.

---

## 2026-09-24

### [DISEÑO] Planteamiento inicial

- Pregunta: convergencia de asignaciones RACI entre perspectivas DAS, ISC, MCO y ODC, más un agente NEUTRAL de control, con el mismo modelo (`gemini-3.1-flash-lite`, thinking `medium`), antes y después de una ronda de deliberación, con árbitro final.
- Unidad experimental: la corrida (escenario × repetición). IC por bootstrap sobre corridas, porque los agentes de una corrida no son independientes en la fase 2.
- Orden: repetición externa, escenarios barajados con semilla dentro de cada repetición, agentes barajados por corrida. Semilla `1000 + run_id`.
- Plan de análisis fijado en README antes del piloto.

### [MATERIAL] Construcción del corpus y de los escenarios

- Corpus institucional parseado automáticamente de `atribuciones_gt.md` y `atribuciones_dte.md`: 20 fichas y 135 numerales de atribución, recuento idéntico al del artículo. Texto literal.
- Corpus externo curado a mano en `sources/external_sources.json`: 37 entradas con CAN_SUPPORT / CANNOT_SUPPORT. Excluidos R1-R10, la RACI, la Autoridad de Cambio y las atribuciones propuestas.
- Excluidos del contexto de los agentes: propuesta de procedimiento de DTE, ambos flujos, resúmenes de correos, `agente_junior`, evaluación del artículo y `memory.md`.
- REFERENCE_RACI extraída de la Tabla `tab:raci` de `main.tex` a `posthoc/reference_raci.json` (20 filas, que corresponden a ACT01-ACT20).
- 10 escenarios (S01-S10), de 4 o 5 actividades cada uno, que cubren las 20 actividades.
- Limitación conocida: el catálogo de actividades reproduce la descomposición de la RACI del artículo (ver Rigor, abajo).

### [CÓDIGO] Pipeline verificado en simulación

- `--dry-run` de 30 corridas y 300 llamadas: el pipeline completo funciona; la validación de citas detecta los identificadores inventados que genera el simulador.
- Corrección: el control de contaminación se aplica solo al material preparado por el experimentador, no al texto generado por agentes, que puede usar libremente términos como «A/R».
- Corrección: el árbitro recibe también `common.md` (jerarquía de evidencia).

### [EJECUCIÓN] Smoke test, intento 1 (`results/smoke_intento1_503/`, conservado)

- 4 de los 5 agentes de la fase 1 fallaron con error 503 (demanda alta del servicio) tras 3 reintentos. La corrida continuó con un solo agente: el resultado no es válido.
- Confirmado: el identificador `gemini-3.1-flash-lite` existe y la clave funciona.

### [CÓDIGO] Robustez ante errores del servicio

- Presupuestos de reintento separados: 8 por error de API (espera exponencial, máximo 120 s) y 3 por JSON inválido.
- Corridas todo o nada: sin todos los agentes de una fase no se continúa; `--resume` repite la corrida. El análisis solo usa corridas completas.

### [EJECUCIÓN] Smoke test (`results/smoke/`), material v1

- 10/10 JSON válidos, 100 % de identificadores existentes, contaminación OK.
- Con la misma semilla, la respuesta de MCO en la fase 1 fue idéntica a la del intento 1: la semilla es efectiva.
- Acuerdo de los especializados: de 63 % a 87 %. Árbitro AMBIGUOUS en ACT02 (certificar datos) y ACT12 (verificar mímicos).
- Coste: USD 0,10 por corrida con precios provisionales.

### [CÓDIGO] Auditoría de pertinencia de citas (`citation_audit.py`)

- Motivo: la existencia del identificador no prueba que la fuente respalde lo afirmado.
- Tres capas: control determinista (unidad citada frente a asignación), juez LLM ciego (`gemini-3.1-pro-preview`, distinto del modelo evaluado, sobre una muestra estratificada) y doble codificación humana ciega con kappa, que también valida al juez.
- `prompts/judge.md` se excluye del hash de material del experimento, porque es post hoc.
- Smoke v1, 60 citas: SUPPORTS 67 %, PARTIAL 17 %, DOES_NOT_SUPPORT 17 %; tipo correcto 72 %.

### [HALLAZGO] La falta de respaldo se concentra donde las fichas no tienen numeral expreso

Los rechazos del juez se concentran en ACT02 y ACT12, las mismas actividades que el árbitro declaró ambiguas. Los agentes etiquetan como DOCUMENTADO lo que es inferencia desde numerales generales.

### [MATERIAL] v1.1: regla DOCUMENTADO/INFERIDO en `common.md`

- Añadida una regla de clasificación con ejemplo de una unidad hipotética X, para no orientar ninguna asignación.
- Smoke `results/smoke2/`: tipo correcto de 72 % a 78 % (IC solapados); las citas institucionales siguen siendo DOCUMENTADO en el 99 % de los casos. Efecto insuficiente.

### [DISEÑO] Evaluación de rigor y cambios adoptados

Evaluación: sólido como estudio exploratorio y reproducible (unos 7/10). Amenazas principales:

1. Sin control, la convergencia podía deberse a responder dos veces y no a la deliberación.
2. Circularidad con el artículo: catálogo, escenarios y corpus externo preparados por los autores de la RACI de referencia.
3. Validez de constructo: un solo LLM con encuadres distintos, sin línea base humana.
4. Robustez: un modelo y una redacción de prompts.
5. Etiquetado de evidencia no fiable.

El usuario aprobó implementar las recomendaciones 1 (brazo control) y 3 (cita textual verificable). Quedan pendientes, a cargo del usuario o del equipo:

- revisión independiente de escenarios y catálogo, con variante sin corpus externo;
- robustez con otro modelo y con una paráfrasis de los prompts;
- línea base humana (un experto por unidad, 3 o 4 escenarios).

### [MATERIAL] v2: brazo control y cita textual

- **Fase 2c (brazo control):** cada especializado reconsidera su decisión inicial sin ver propuestas ajenas (`prompts/task_phase2_control.md`, mismo título que la deliberación). Diseño pareado dentro de la corrida. Nuevas métricas: `CONVERGENCE_DELTA_CONTROL` y `DELIBERATION_EFFECT` (delta con deliberación menos delta control). Llamadas por corrida: de 10 a 14.
- **Cita textual:** campo obligatorio `quote` en cada cita. `verify_quote()` comprueba su existencia en la fuente, normalizando mayúsculas, puntuación y espacios y admitiendo «...» entre fragmentos. Nuevas métricas: `QUOTE_VERIFIED_RATE`, `DOCUMENTADO_QUOTE_VERIFIED_RATE` e `INFERIDO_SHARE`.
- `common.md`: cada cita con fragmento literal; DOCUMENTADO exige que el fragmento nombre la actividad.
- Hashes v2 (12 primeros caracteres): common.md `88f5a2abbdfe`, task_phase2_control.md `9676418b4126`, task_phase2.md `88aaceb1b763`, corpus_institutional.md `42570c7fb590`, corpus_external.md `e648a363f326`, scenarios.json `cd195c4caf20`, activities.json `013ea39a4874`. Lista completa en `results/smoke3/experiment_config.json`.
- **Comparabilidad:** los smoke v1, v1.1 y v2 no son comparables entre sí. El piloto debe correrse íntegro con v2.

### [EJECUCIÓN] Smoke test v2 (`results/smoke3/`)

- 14/14 JSON válidos, sin errores de API. Coste: USD 0,13 por corrida; aparece caché implícita (75 000 tokens).
- Acuerdo: 53 % antes, 90 % con deliberación y 53 % en el control. CONVERGENCE_DELTA = 0,37; DELTA_CONTROL = 0,00; DELIBERATION_EFFECT = 0,37. Cambio de A: 20 % con deliberación y 0 % en el control. Con una sola corrida es indicativo, pero muestra que el control discrimina.
- Cita textual verificada: 96 % del total y 100 % de las DOCUMENTADO. INFERIDO: 1 % de las citas.
- Juez (60 citas): SUPPORTS 42 %, PARTIAL 32 %, DOES_NOT_SUPPORT 27 %; tipo correcto 53 %. El juez es más severo que en v1, probablemente porque ahora recibe el fragmento literal y la distancia entre fragmento y afirmación queda a la vista. No es comparable con el smoke v1 (otra corrida, otro material y otra información para el juez).

### [DISEÑO] La etiqueta de tipo de afirmación declarada por el agente no se usa como medida

- Evidencia: los agentes copian fragmentos reales (96 %) de numerales generales («administrar la base de datos», «coordinar la operación») y los etiquetan DOCUMENTADO para actividades específicas. Esto pasa pese a la regla explícita y al ejemplo.
- Decisión: no seguir ajustando el prompt (sería ajustar a medida del resultado). La etiqueta se registra como variable descriptiva del comportamiento del modelo. El grado de respaldo se mide con la verificación textual, el juez ciego y la auditoría humana.
- Implicación sustantiva, a confirmar en el piloto: la mayoría de las asignaciones se apoyan en inferencias desde numerales generales, no en texto expreso. Esto es coherente con que ninguna ficha nombre el modelo eléctrico del EMS.

### [CÓDIGO] Matriz RACI modal (`analysis.py`)

- Motivo: el análisis solo comparaba la A con REFERENCE_RACI y no producía una matriz comparable a la del artículo.
- Implementado sin cambios en el material de los agentes ni coste de API; se aplica a resultados ya guardados.
- Criterios fijados antes del piloto:
  - rol por decisión y unidad: A/R > A > R > C > I > sin rol;
  - celda: rol modal y su frecuencia; inestable si es menor que 60 %;
  - nivel principal: actividad acumulando escenarios; desglose por escenario en CSV;
  - cinco grupos: especializados en la fase 1, neutral, deliberación (2), control (2c) y árbitro.
- Comparación post hoc celda a celda en tres niveles: rol exacto, rol ejecutivo (A/R, A, R, con C, I y sin rol como una misma clase) y A recuperada. Columnas agrupadas como en el artículo: GT_SUPPORT = DOS, DEL, DEN, DDR; ORIGIN = TX_REG, DT, OTHER. Aproximación: DEL y DOS van solo en GT_SUPPORT.
- Verificación: con datos aleatorios del simulador, la coincidencia es baja (A recuperada del 5 al 35 %) y la mayoría de las celdas sale inestable. La métrica no infla la concordancia.
- Smoke3 (1 corrida, 5 actividades, solo indicativo): rol ejecutivo idéntico en el 86-91 % de las celdas y A recuperada en el 80 %. La coincidencia exacta es baja (23-34 %) porque la referencia asigna C o I a casi todas las unidades y los agentes no. La discrepancia principal está en ACT12: los agentes dan la A a ODC; la referencia, al origen (Transmisión).

### [DISEÑO] Papel de las personas y sesgo departamental

- Preocupación del usuario: el sesgo humano (resistencia de cada departamento a cambiar su forma de trabajar) es justamente lo que el experimento con agentes busca sacar de la matriz.
- Decisión: **ninguna persona decide la matriz RACI.** Las personas solo verifican la neutralidad del material (antes del piloto) y la lectura de las citas (después), y deben ser ajenas a GT/DAS, DTE/ISC, DTE/MCO y GT/ODC.
- Si no hay codificadores neutrales, la auditoría humana se sustituye por dos jueces LLM de modelos distintos, declarando la limitación.
- La línea base humana es opcional y serviría para medir el sesgo departamental, no como referencia de lo correcto.

### [CÓDIGO] Guía de validación humana y cegamiento estricto

- Nueva carpeta `validacion_humana/`:
  - `GUIA_VALIDACION_HUMANA.md`: calendario, perfiles, parte A (neutralidad del material, **antes del piloto**), parte B (auditoría de citas, **después del piloto**), instrucciones para codificadores y parte C opcional;
  - `plantilla_revision_neutralidad.md`.
- `citation_audit.py sample --hide-assignment`: oculta A y R en las planillas de los codificadores. El texto de la afirmación puede seguir mencionando unidades.

### Estado al cierre del día

- Material v2 congelado para el piloto.
- Piloto (10 × 20 = 200 corridas, 2800 llamadas, unos USD 26) **no lanzado**; requiere pedido expreso del usuario.
- Auditoría humana: planillas de prueba en `results/smoke/`; para el piloto, `citation_audit.py sample --n 100`.

## 2026-09-25

### [CÓDIGO] Visor de corridas (`ver_corrida.py`)

- Reconstruye en Markdown una corrida completa a partir de `raw_results.jsonl`, sin API: escenario, tabla resumen de la A por actividad y fase (fase 1, deliberación, control y árbitro), detalle de cada agente con citas y verificación literal (✓/✗), propuestas vistas por cada agente con su autor real, y el veredicto del árbitro.
- Uso: `python ver_corrida.py --label <label> --run N --scenario SXX` o `--all`. Salida: `results/<label>/corridas/`.
- Prueba: `results/smoke3/corridas/run01_S01.md` (866 líneas).
- Lo que no se guarda: el texto completo de cada petición (se reconstruye desde corpus, plantilla y anonimización; hay muestras en `prompt_samples/`) y el razonamiento interno del modelo (solo su cantidad de tokens). El resumen del razonamiento (`include_thoughts`) queda como opción no activada.

### [HALLAZGO] Lectura de la corrida smoke3 con el visor

- En ACT09, MCO cambia su A a ISC solo tras la deliberación; en el control la mantiene. En ACT02, ISC y MCO convergen en DT solo con deliberación. Ejemplos concretos del efecto que mide DELIBERATION_EFFECT.
- Algunos agentes declaran MODIFY sin cambiar la A porque cambiaron R o C.
- El árbitro redactó parte de su razonamiento en inglés.

### [CÓDIGO] Corrección de la métrica de incoherencia de posición

- Antes: MODIFY sin cambio de A contaba como incoherente.
- Ahora: es incoherente declarar MAINTAIN con cambio de A, o MODIFY sin ningún cambio en A, R, C ni I. Los MODIFY que solo cambian R, C o I se informan en la columna `modify_R_C_I_only` de `agent_changes.csv`.
- Smoke3: la incoherencia pasa de lo que antes se contaba como incoherente a 0 %; 3 de los 6 MODIFY cambiaron solo R, C o I.

### [DISEÑO] Pendiente de decisión: idioma de las respuestas

- El árbitro respondió parte en inglés. Añadir «Responde en español» a `common.md` cambiaría el hash del material y obligaría a repetir el smoke test antes del piloto. No aplicado; pendiente de decisión del usuario.

### [VALIDACIÓN] Primera revisión de neutralidad recibida (`validacion_humana/sebastian_formulario.xlsx`)

- Revisor: persona del entorno EMS (no ajena al conflicto según la guía). Completó escenarios y actividades; no señaló sesgo en el corpus externo.
- **Interpretación:** en las preguntas 1, 2 y 4 respondió con una unidad por escenario o actividad (S01 → ISC, S07 → MCO, S10 → DEL, ACT15/16/19/20 → MCO, ACT18 → DAS2…), es decir, asignó responsabilidades en vez de revisar la redacción. Las frases que cita son hechos técnicos (RTU, IEC 104, servidores), no frases prescriptivas. No aporta evidencia de sesgo prescriptivo, pero tampoco cuenta como revisión de neutralidad válida (tarea malinterpretada y revisor no externo).
- **Causa:** la pregunta de la plantilla era ambigua. Plantilla y guía corregidas: distinción entre pista técnica (aceptable) y pista prescriptiva (a corregir), con ejemplo de respuesta correcta e incorrecta. No afecta al material de los agentes.
- **Hechos que faltan (columnas D-E), propuestas de cambio al material, pendientes de decisión del usuario:**
  - aceptar: S01 plazo de incorporación; S02 origen de los parámetros **sin nombrar unidad**; S04 explicitar que se requiere corregir; S06 si el interruptor tiene señalización de estado; S09 relevancia del estimador en la zona; ACT13 definir «mímico» en el contexto técnico;
  - rechazar como hecho: S10 validación previa en simulación, porque es una solución y no un dato; como máximo «se dispone de herramienta de simulación».
- **Uso de su mapeo:** propuesto guardarlo en `posthoc/` como «mapeo experto, 1 persona del entorno EMS», solo para comparación post hoc con procedencia declarada. Nunca como material de los agentes.
- Sigue pendiente una revisión de neutralidad por una persona ajena al conflicto, con la plantilla corregida.

### [MATERIAL] v3: aportes de la revisión E1 filtrados, definición de mímico e idioma

Aprobado por el usuario. Cambios:

- `scenarios.json`, hechos añadidos a la descripción técnica sin nombrar unidades:
  - S01: energización en 15 días hábiles;
  - S02: los parámetros constan en el informe de la obra y en el estudio de límites;
  - S04: se requiere corregir, registrar la causa y verificar;
  - S06: el interruptor tiene señalización de estado y mando remoto;
  - S09: la zona incluye transformadores supervisados por contingencias que dependen del estimador;
  - S10: se dispone de un ambiente de simulación fuera de línea (solo el hecho; se rechazó como actividad prescrita «validar antes en simulación»).
- `sources/external_sources.json`: nueva entrada `CTX_MIMICO` (definición de mímico y sus dependencias; CANNOT_SUPPORT: asignar su construcción, verificación o aceptación). Corpus externo: 38 fuentes.
- `prompts/common.md`: «Redacta todos los campos de texto en español».
- `posthoc/expert_mapping_E1.json`: mapeo del experto E1 (entorno EMS) con procedencia y advertencias. Solo para comparación post hoc; `experiment.py` no lee `posthoc/`.
- Control de contaminación: OK.
- Hashes v3 (12 primeros caracteres): common.md `7a5af01749c3`, scenarios.json `c9853f0cd492`, corpus_external.md `94c05ae61fd3`, corpus_institutional.md `42570c7fb590` (sin cambio), activities.json `013ea39a4874` (sin cambio). Lista completa en `results/smoke4/experiment_config.json`.
- **Comparabilidad:** v3 sustituye a v2. El piloto debe correrse íntegro con v3.

### [EJECUCIÓN] Smoke test v3 (`results/smoke4/`, S01 y S10, 1 repetición)

- 28/28 respuestas válidas, sin errores de API, todas en español. Coste: USD 0,24 (2 corridas).
- Acuerdo: 70 % antes, 85 % con deliberación y 67 % en el control; DELIBERATION_EFFECT = 0,18. Cambio de A: 22,5 % con deliberación y 5 % en el control.
- Citas literales verificadas: 98 % (DOCUMENTADO: 99 %).
- Fichas: `results/smoke4/corridas/run01_S01.md` y `run01_S10.md`.

### [HALLAZGO] S10 (cambio urgente), a confirmar con el piloto

- Todos los agentes y el neutral asignan a ODC la A de autorizar la liberación en emergencia (ACT14). El artículo propone una autoridad nueva.
- Todos asignan la carga (ACT16) a DAS; el artículo, a MCO. El árbitro la declaró AMBIGUOUS.
- En la reversión (ACT20), DAS y ODC pasan a ODC solo con deliberación; en el control mantienen DAS.
- La etiqueta «consensus» del árbitro no siempre coincide con el acuerdo sobre la A (ACT16: NONE con 4/4 en DAS); puede referirse a toda la asignación o a la calidad de la evidencia. El análisis calcula el consenso desde los datos, no desde esa etiqueta.

## 2026-09-26

### [VALIDACIÓN] Revisión de neutralidad del material v3 (`validacion_humana/gd_evaluacion.md`)

- **Revisora:** ingeniera civil, sin relación con GT/DAS, DTE/ISC, DTE/MCO ni GT/ODC. Fecha: 25/09/2026. Versión revisada: v3 (hash de `scenarios.json` `c9853f0cd492`, coincide con el registrado).
- **Método declarado:** revisión asistida por IA y validada por la revisora. Pendiente: registrar la herramienta usada y el alcance de su intervención personal (lectura completa, modificaciones).
- **Resultado:**
  - ninguna frase prescriptiva ni riesgo redactado desde una sola unidad en S01-S10;
  - ninguna palabra que asigne actividades a unidades en ACT01-ACT20;
  - ninguna fuente externa que favorezca a una unidad; los CANNOT_SUPPORT limitan la asignación;
  - confirma como pertinentes y neutrales los hechos añadidos en v3 (S01, S02, S04, S06, S09, S10).
- **Decisión:** se acepta como la revisión de neutralidad (parte A) de la guía. **El material v3 queda aprobado sin cambios y congelado para el piloto.**
- **Limitaciones a declarar:** asistencia de IA en la revisión (menor independencia que una lectura humana directa); revisora sin especialidad SCADA/EMS. Suficiente para detectar redacción prescriptiva; podría no detectar pistas técnicas sutiles.
- **Sugerencias no aplicadas:**
  - dividir ACT07 (modelo / adquisición), ACT09 (FAT / SAT / integración), ACT13 (mímicos / alarmas / uso operativo), ACT16 (respaldo / carga) y ACT20 (decisión / ejecución de la reversión). La revisora indica que no afectan a la neutralidad; dividirlas rompería la correspondencia 1:1 con las 20 filas de REFERENCE_RACI, necesaria para la comparación post hoc. Queda como mejora para un estudio posterior de mayor granularidad;
  - incorporar documentación local de permisos efectivos, flujo formal de cambios y autoridad de emergencia: no existe como documento aprobado; los flujos disponibles se excluyeron por ser propuestas de las partes. Se mantiene como limitación declarada.

### Estado

- Parte A (neutralidad): completada.
- Piloto con material v3: listo para lanzar; requiere pedido expreso del usuario.
- Parte B (auditoría de citas): después del piloto.

### [CÓDIGO] Tope de presupuesto

- `config.MAX_BUDGET_USD = 30.0` (crédito disponible: USD 38 en AI Studio, según el usuario; margen reservado para el juez de citas). `experiment.py` acumula el coste estimado de cada llamada, incluidos los reintentos y las ejecuciones previas si se reanuda, y no inicia corridas nuevas al superar el tope. Las omitidas se completan con `--resume`. El coste se calcula con los precios provisionales de `config.py`; el consumo real debe verificarse en AI Studio.
- Sin efecto sobre el material de los agentes.

### [EJECUCIÓN] Lanzamiento del piloto (`results/pilot/`)

- Autorizado por el usuario: «Lanza el piloto». Herramienta de IA de la revisora de neutralidad: declarada por el usuario, pendiente de transcribir en este registro.
- Comando: `python experiment.py --label pilot --workers 4 > results/pilot_run.log 2>&1`
- Material v3 (hashes en `results/pilot/experiment_config.json`), 10 escenarios × 20 repeticiones = 200 corridas, 14 llamadas por corrida (≈ 2800).
- Inicio: 2026-09-26T11:35:21+00:00

### [EJECUCIÓN] Piloto completado (`results/pilot/`)

- Fin: 2026-09-26T13:09:10+00:00 (unas 2,5 h con 4 corridas en paralelo).
- 200/200 corridas completas; 2800 llamadas; 0 errores de API; 0 reintentos por JSON inválido; JSON válido 100 %; control de contaminación OK en las 2800 peticiones.
- Tokens: 64,85 M de entrada (17,89 M en caché implícita) y 6,82 M de salida (1,90 M de razonamiento). **Coste estimado: USD 22,41** con los precios provisionales de `config.py`; pendiente contrastar con el consumo real en AI Studio.
- Salidas: `final_report.md`, `summary.csv`, `scenario_summary.csv`, `agent_changes.csv`, `evidence_usage.csv`, `posthoc_comparison.csv`, `modal_raci.md/.csv`, `modal_raci_vs_reference.csv`, `decisions.csv` y 200 fichas en `corridas/`.

### [HALLAZGO] Resultados principales del piloto (análisis preespecificado)

- **Convergencia:** acuerdo de 68,9 % a 88,5 % con deliberación; en el control, 69,3 %. CONVERGENCE_DELTA = 0,196 [0,176; 0,217]; CONVERGENCE_DELTA_CONTROL = 0,005 [−0,003; 0,012]; **DELIBERATION_EFFECT = 0,191 [0,171; 0,212]**. Consenso estricto: de 49 % a 80 %. Cambio de A: 17,1 % con deliberación y 2,6 % en el control. Responder dos veces casi no produce convergencia; la información ajena, sí.
- **Entropía media de A:** de 0,84 a 0,49 bits. Actividades estables (H = 0 en ambas fases): construir el modelo (ACT04), administrar aplicativos (ACT10), unificar (S03-ACT07), paquete (ACT08) y ventana en tiempo real (ACT15). Las más inestables tras deliberar: verificar mímicos en S06 (H = 2,20), semántica del modelo (S06-ACT03, H = 1,79), criterios de reversión en S09 (H = 1,71), adquisición (S01, S03, H ≈ 1,2).
- **Ambigüedad:** declarada por los agentes en el 4 % de las decisiones antes y en el 11 % después; el árbitro, AMBIGUOUS en el 17,7 %. Máximos del árbitro: S09-ACT19 (70 %), S04-ACT17 y S06-ACT12 (65 %), S08-ACT16 (55 %), S08-ACT14 y S09-ACT18 (50 %).
- **Sesgo hacia la propia unidad** (fase 1, frente al neutral): DAS +0,08, ISC +0,07, MCO +0,02, ODC +0,09. Pequeño y de magnitud similar en las cuatro perspectivas.
- **Evidencia:** identificadores existentes 98,6 %; citas literales verificadas 97,2 %; asignación sin ninguna cita válida 0,1 %; A sin evidencia institucional 2,2 %; DOCUMENTADO con fuente externa 2,1 %; INFERIDO 4,3 % de las citas; PROPOSED_NEW_AUTHORITY prácticamente nunca (0,01 %).

### [HALLAZGO] Dirección de los cambios en la deliberación (exploratorio)

- De 589 cambios de A en la fase 2: el 89 % va hacia la opción más frecuente entre las propuestas vistas, el 7 % hacia una minoritaria vista y el 3 % hacia una que nadie propuso.
- El brazo control demuestra que la convergencia se debe a la información ajena, pero **no distingue persuasión por evidencia de conformidad con la mayoría**. Ambas son compatibles con estos datos. Debe declararse en el artículo; no presentar la convergencia como acuerdo por mérito de la evidencia.

### [HALLAZGO] Comparación post hoc con REFERENCE_RACI (análisis exploratorio, al final)

- A de la referencia recuperada: 40 % (fase 1), 45 % (deliberación y árbitro). Rol ejecutivo idéntico: unas 76 % de las celdas. Celdas inestables: de 52 a 43 de 140 con deliberación; 37 en el árbitro.
- **Coinciden** (≥ 78 % tras la deliberación): certificar datos por el origen (ACT02: DT/TX_REG; DEL en S02), construir el modelo por DAS (ACT04), FAT/SAT por ISC (ACT09), aplicativos (ACT10) y validación (ACT11) por DAS, aceptación operativa (ACT13) y ventana (ACT15) por ODC.
- **Difieren sistemáticamente:**
  - revisión de calidad del modelo (ACT05): los agentes asignan A/R a DAS (86 %), es decir, al mismo autor; la referencia exige revisión independiente de ISC (R5);
  - unificación (ACT07), paquete (ACT08) y registro técnico (ACT17): DAS en lugar de ISC;
  - carga (ACT16) y reversión (ACT20): DAS/ODC en lugar de MCO;
  - liberación (ACT14) y criterios de reversión (ACT19): los agentes asignan la A a GT/OP (división común), no a una autoridad nueva; en emergencia (S10), a ODC;
  - requisito (ACT01): ODC, no DAS; verificación de mímicos (ACT12): ODC u otros, no el origen.
- **Interpretación provisional:**
  - los agentes no aplican espontáneamente la segregación entre autoría y revisión, pese a disponer de NIST AC-5 y ERCOT_03: la regla R5 del artículo es una decisión de diseño, no una lectura de las fichas;
  - los agentes resuelven la autoridad de liberación con la jerarquía existente (OP) en lugar de crear una instancia nueva;
  - la concentración en DAS (también en el neutral) puede reflejar la lectura amplia de «administrar y gestionar la base de datos» o un **efecto de nombre**: la unidad se llama «Administración del SCADA/EMS». No se puede separar con este diseño; una ablación con nombres de unidades anonimizados lo permitiría.

### Pendiente tras el piloto

- Contrastar el coste real en AI Studio.
- Auditoría de citas (parte B): `citation_audit.py extract`, `sample --n 100 --hide-assignment` y `judge --n 600` (coste estimado del juez: USD 2-5, pendiente de autorización).
- Ablación opcional con nombres de unidades anonimizados, para probar el efecto de nombre.

### [DISEÑO] Ablación de nombres de unidades (preespecificada antes de ejecutar)

- Motivo: en el piloto, la A se concentra en DAS en muchas actividades, también en el agente neutral. Hipótesis alternativas: lectura amplia de «administrar y gestionar la base de datos» o **efecto de nombre** (la unidad se llama «Administración del SCADA/EMS»). Aprobada por el usuario; gasto acumulado según AI Studio: USD 22,4.
- Tratamiento (`build_ablation.py` → `ablation_anon/`):
  - nombres y siglas de las 20 unidades con ficha, Gerencia Técnica y División de Sistemas de Comunicación sustituidos por códigos U01-U22 asignados al azar (semilla 20260926), también en los identificadores (p. ej., `DAS1_2_1` → `U22_2_1`) y en la lista de unidades admitidas;
  - fichas en orden aleatorio; secciones sin ficha y unidades externas como «sin ficha en el corpus»;
  - en `CTX_UNIFILAR`, los departamentos regionales como códigos;
  - en los prompts de perspectiva, «no implica favorecer a GT/DAS…» → «a ninguna unidad en particular».
- Se conserva: el texto funcional de cada numeral, las resoluciones, las fechas, la subordinación (con códigos), los escenarios y las actividades.
- Restos revisados y aceptados como contenido funcional: «Operación del Sistema» (actividad), «Instrucciones de Operación del Sistema», «Centros de Despacho Regional» (instalaciones). En `das.md`, el foco técnico «administración del SCADA/EMS» es igual que en el piloto; la ablación prueba el nombre dentro del corpus.
- La correspondencia está en `ablation_anon/material.json`; no se envía a los agentes y se usa solo para validar y analizar.
- Diseño: solo fase 1 (5 agentes); 10 escenarios × 20 repeticiones con las **mismas semillas** que el piloto (pareado); `--budget 8`.
- **Estimando principal:** diferencia (variante − piloto) en la proporción de decisiones de fase 1 con DAS como A, con IC 95 % por bootstrap pareado sobre corridas.
- **Secundarios:** proporción de A por unidad; DAS como A por agente; A modal por escenario y actividad; misma A pareada; acuerdo entre especializados; sesgo hacia la propia unidad; coincidencia con REFERENCE_RACI.
- **Lectura prevista:** una baja clara indica efecto de nombre; sin cambio, la concentración se sostiene en el contenido. La ablación mide el nombre, no la función, que sigue siendo identificable.
- Hashes del material de la variante: corpus_institutional.md `8c636ca95b1f`, corpus_external.md `d30a60daf0f1`, common.md `c48db4a5dd90` (idéntico al base: `c48db4a5dd90`).
- Código: `experiment.py` con `--material`, `--phases 1` y `--budget`; `analysis.py` y `ver_corrida.py` leen el material de `experiment_config.json`; nuevo `compare_ablation.py`. El piloto base se recalculó sin cambios.

### [EJECUCIÓN] Ablación de nombres completada (`results/ablation_anon/`)

- 200/200 corridas (solo fase 1), 1000 llamadas, 0 errores, JSON válido 100 %, contaminación OK. Coste estimado: USD 7,10 (acumulado estimado del proyecto: unos USD 29,5).
- Comparación pareada con el piloto: `results/ablation_anon/comparacion_vs_pilot.md` y `.csv` (4300 decisiones pareadas, 200 corridas).

### [HALLAZGO] Resultado de la ablación (estimando preespecificado)

- **DAS como A: 43,3 % → 28,5 %, diferencia −14,8 pp [−17,2; −12,4].** La caída es similar en todos los agentes, incluido el neutral (−15,8 pp).
- **MCO como A: 3,2 % → 32,2 % (+29,0 pp [+26,6; +31,4]).** Gana, entre otras, la adquisición (ACT06), la carga (ACT16), la reversión (ACT20), la verificación posterior (ACT18) y parte de FAT/SAT (ACT09). ODC −4,7 pp; OP −4,2 pp; ISC −1,6 pp.
- **Estables** con o sin nombres (contenido explícito): construir el modelo (ACT04, DAS 89-93 %), aplicativos (ACT10, 98 %), validar el estimador (ACT11), ventana en tiempo real (ACT15, ODC 98-100 %), revisión de calidad (ACT05, DAS).
- Misma A en el 50,5 % de las decisiones pareadas; acuerdo entre especializados: 68,6 % → 61,3 %. Coincidencia con REFERENCE_RACI: 45,1 % → 42,9 %.

### [HALLAZGO] Posible artefacto de código y posición: la ablación no es concluyente por sí sola

- El sorteo asignó a MCO el código **U01** (el más bajo; segunda ficha en el corpus y en la lista de unidades) y a DAS el **U12** (penúltima posición). Los LLM pueden preferir códigos bajos o posiciones tempranas.
- Con una sola asignación de códigos no se puede separar el efecto del nombre del efecto del código o de la posición. **No se afirma todavía un efecto de nombre.**
- Recomendación: réplica con otra semilla de códigos y otro orden de fichas (p. ej., 10 escenarios × 5 repeticiones, unos USD 1,8). Si MCO sube y DAS baja también con otros códigos, el efecto es de nombre y contenido; si la ganancia sigue al código U01 o a la posición, es un artefacto. Pendiente de autorización del usuario.

### [DISEÑO] Réplica cruzada de la ablación (preespecificada antes de ejecutar)

- Aprobada por el usuario («hagamos la réplica para confirmar el nombre»).
- Material `ablation_anon_swap/` (`python build_ablation.py --swap`): idéntico a `ablation_anon` salvo que **DAS y MCO intercambian código y posición**. DAS pasa a U01 en la posición 2; MCO, a U12 en la posición 19. Verificado: textos del corpus institucional idénticos salvo códigos; corpus externo idéntico; resto de códigos y orden sin cambios.
- Ejecución: solo fase 1; 10 escenarios × 5 repeticiones (run 1-5, mismas semillas que el piloto y la ablación); `--budget 2.5`; etiqueta `ablation_swap`.
- **Predicciones:**
  - artefacto de código o posición: la unidad en la casilla «U01, posición 2» (ahora DAS) gana mucho; DAS muy por encima del 28,5 % y MCO cerca del 3 %;
  - efecto de nombre y contenido: DAS cerca del 28,5 % y MCO cerca del 32 %, como en `ablation_anon`.
- **Comparación principal:** proporción de A para DAS y MCO en `ablation_swap` frente a `ablation_anon`, pareada en los runs 1-5, con IC por bootstrap.
- Inicio: 2026-09-26T23:19:59+00:00

### [EJECUCIÓN] Réplica cruzada completada (`results/ablation_swap/`)

- 50/50 corridas (solo fase 1), 250 llamadas, 0 errores, JSON válido 100 %. Coste estimado: USD 1,83 (acumulado estimado del proyecto: unos USD 31,3).
- Comparaciones: `results/ablation_swap/comparacion_vs_ablation_anon.md` (pareada, runs 1-5) y `comparacion_vs_pilot.md`.

### [HALLAZGO] El efecto de la ablación era de código y posición, no de nombre

- Frente a `ablation_anon` (runs 1-5), al pasar DAS a la casilla «U01, posición 2»: **DAS 29,1 % → 45,1 % (+16,0 pp [+10,9; +21,1]); MCO 33,4 % → 8,8 % (−24,6 pp [−29,4; −19,7])**. Se cumple la predicción de artefacto.
- Frente al piloto con nombres: DAS 44,1 % → 45,1 % (+1,0 pp [−2,2; +4,2]); sin nombre, pero en la casilla favorable, DAS recupera su nivel del piloto.
- **Actividades en disputa que siguen a la casilla U01:** adquisición (ACT06 en S01, S04, S05), paquete (ACT08), carga (ACT16), verificación posterior (ACT18) y reversión (ACT20). **Estables con independencia del código:** construir el modelo (ACT04), FAT/SAT (ACT09 en S01 y S03, ISC) y ventana (ACT15), es decir, actividades con numeral expreso.
- **Conclusión:** no hay evidencia de un efecto del nombre de DAS. El efecto dominante es la **saliencia de presentación** (código más bajo o posición temprana en la lista). Cuando el contenido no discrimina entre DAS y MCO, el modelo desempata por saliencia.
- **Implicación para el piloto:** en el piloto, DAS estaba en la posición 7 y MCO en la 20 (última). La concentración en DAS en las actividades disputadas (ACT07, ACT08, ACT16, ACT17, ACT20) y la baja presencia de MCO pueden deberse en parte al orden de presentación. Esas asignaciones del piloto no deben leerse como preferencia del corpus por DAS, sino como **indiferencia del contenido entre DAS (2.1; DAS1 2.2) y MCO (2.8)**, coherente con la concurrencia que describe el artículo (C3 y C4).
- Las asignaciones con numeral expreso (ACT04, ACT09, ACT10, ACT11, ACT15) son robustas a nombre, código y posición.
- **Recomendación:** control de orden en el piloto con nombres (material base con las fichas en orden inverso, solo fase 1, 10 × 5, unos USD 1,8) para cuantificar la sensibilidad de la matriz del piloto al orden de presentación. Pendiente de autorización y de verificar el crédito real.

### [DISEÑO] Control de orden con nombres (preespecificado antes de ejecutar)

- Aprobado por el usuario («haz el control de orden»).
- Material `order_reversed/` (`build_order_control.py`): material base v3 con nombres reales y las 20 fichas en **orden inverso** en el corpus y en la lista de unidades admitidas. MCO pasa de la posición 20 a la 1; ISC y sus secciones, a las 2-5; DAS, de la 7 a la 14; OP, de la 1 a la 20. Verificado: texto de las fichas idéntico; corpus externo, escenarios, actividades y prompts idénticos byte a byte.
- Ejecución: solo fase 1; 10 escenarios × 5 repeticiones (runs 1-5, mismas semillas que el piloto); `--budget 2.5`; etiqueta `order_reversed`.
- **Comparación:** con la fase 1 del piloto, pareada en los runs 1-5 (`compare_ablation.py --base pilot --variant order_reversed`).
- **Predicciones:**
  - sensibilidad al orden: MCO (y quizá ISC) sube y DAS baja, sobre todo en las actividades disputadas (ACT06, ACT07, ACT08, ACT16, ACT17, ACT18, ACT20);
  - robustez: proporciones similares al piloto.
- Las actividades con numeral expreso (ACT04, ACT09, ACT10, ACT11, ACT15) deberían mantenerse en ambos casos.
- Inicio: 2026-09-26T23:34:37+00:00

### [EJECUCIÓN] Control de orden completado (`results/order_reversed/`)

- 50/50 corridas (solo fase 1), 250 llamadas, 0 errores, JSON válido 100 %. Coste estimado: USD 1,76 (acumulado estimado del proyecto: unos USD 33,1 sobre un crédito de 38).
- Comparación pareada con el piloto (runs 1-5): `results/order_reversed/comparacion_vs_pilot.md`. (La plantilla del informe llama «sin nombres» a la variante; aquí la variante conserva los nombres y solo invierte el orden.)

### [HALLAZGO] Con nombres, la matriz es robusta al orden en las actividades DAS/MCO

- **DAS como A: 44,1 % → 46,2 % (+2,1 pp [−0,4; +4,7]); MCO: 3,3 % → 2,8 % (−0,6 pp [−2,1; +1,1]).** MCO, ahora primera ficha, no gana nada. Se cumple la predicción de robustez.
- Las actividades disputadas siguen en DAS con el orden inverso: carga (ACT16: 88-100 %), reversión (S09-ACT20: 92 %), paquete (ACT08: 84 %), unificación (ACT07: 100 %), registro (ACT17: 76 %), adquisición (S04, S05: 72-92 %).
- **Hay sensibilidad moderada al orden en otras actividades:** ISC +6,4 pp (subió al segundo puesto) y ODC −7,4 pp (bajó al 19). Cambian de A modal: certificar datos en S01 (DT → ISC), verificar mímicos en S01 (ODC → ISC), aceptar mímicos en S03 (ODC → OP), requisito en S05 (ODC → DOS), semántica en S06 (DAS → ISC) y reversión en emergencia en S10 (ODC → DAS). Son las actividades de mayor entropía en el piloto: donde el corpus es ambiguo, la presentación influye.
- Misma A pareada: 68,4 %; acuerdo entre especializados sin cambio (68,4 % → 68,7 %). Falta una referencia de la variabilidad pareada ante una perturbación neutra del prompt, lo que limita la lectura de esa cifra.

### [HALLAZGO] Síntesis de las tres variantes (piloto, sin nombres, cruzada y orden inverso)

| Condición | Pista de identidad | DAS | MCO |
|---|---|---|---|
| Piloto (fase 1) | nombres; DAS en la posición 7 y MCO en la 20 | 44 % | 3 % |
| Orden inverso | nombres; MCO en la 1 y DAS en la 14 | 46 % | 3 % |
| Sin nombres | códigos; MCO = U01 (posición 2), DAS = U12 (posición 19) | 29 % | 32 % |
| Cruzada | códigos; DAS = U01 (posición 2), MCO = U12 (posición 19) | 45 % | 9 % |

Interpretación:
1. **Actividades con numeral expreso** (construir el modelo, aplicativos, validar el estimador, FAT/SAT, ventana): estables en las cuatro condiciones. El contenido decide.
2. **Actividades disputadas entre DAS y MCO** (adquisición, paquete, carga, verificación posterior, reversión, registro técnico): **el texto de las atribuciones no las decide.** Sin nombres, van a la unidad más saliente por código o posición; con nombres, van a DAS en cualquier orden. Lo que las inclina hacia DAS es la **denominación de la unidad** («Administración del SCADA/EMS» frente a «Mantenimiento de Sistemas de Control»), no un numeral. La conclusión anterior («no hay efecto de nombre») se corrige: la réplica cruzada descartó que la **caída** de DAS en la ablación fuera efecto de nombre, pero este control muestra que, con nombres, **el nombre fija la asignación de las actividades disputadas** frente al orden. Ambos hallazgos son compatibles: sin nombres domina la saliencia; con nombres domina la denominación.
3. **Actividades ambiguas de otro tipo** (certificar datos, mímicos, requisito, semántica): sensibles al orden incluso con nombres, coherente con su alta entropía y con la ambigüedad declarada por el árbitro.

Implicaciones para el artículo:
- las filas del piloto que asignan a DAS la carga, la reversión, el paquete, la unificación y el registro se apoyan en la denominación de la unidad, no en el texto de sus atribuciones; deben presentarse como concurrencia DAS-MCO no resuelta por el manual;
- la etiqueta DOCUMENTADO que los agentes ponen en esas filas es especialmente engañosa.

### [EJECUCIÓN] Auditoría de citas del piloto: extracción, muestra humana y juez

- El usuario amplió el crédito en USD 5 (total: 43) y autorizó el juez completo.
- `citation_audit.py extract`: 28 743 citas (fase 1: 10 867; fase 2: 8687; fase 2c: 8634; árbitro: 555).
- `sample --n 100 --hide-assignment`: **99** citas por redondeo del reparto proporcional (59 DOCUMENTADO, 36 BUENA_PRACTICA, 4 INFERIDO); A y R ocultos. Planillas `results/pilot/audit_sheet_coder1.csv` y `coder2.csv`; clave `audit_key.csv`, que no se entrega a los codificadores.
- `judge --n 600` (`gemini-3.1-pro-preview`, thinking low, ciego): 600 veredictos en 40 lotes, sin reintentos; incluye los 99 ítems humanos. Tokens: 152 942 de entrada y 57 461 de salida; coste aproximado USD 1,0 (precios de Pro no verificados). Acumulado estimado del proyecto: unos USD 34,1.
- Informe: `results/pilot/citation_audit_report.md`; veredictos: `judge_results.csv`.

### [HALLAZGO] Pertinencia de las citas (juez no validado todavía por humanos)

- Control determinista sobre las 28 188 citas de agentes: DOCUMENTADO con fuente externa 1,2 %; unidad citada ausente de la asignación 0,5 %; DOCUMENTADO cuya unidad no es A ni R 5,5 %.
- Juez sobre 600 citas: **SUPPORTS 40,3 % [36,5; 44,3], PARTIAL 38,2 %, DOES_NOT_SUPPORT 21,5 % [18,4; 25,0]**. Tipo de afirmación correcto: 59,7 %; en DOCUMENTADO, solo **45 %**; en BUENA_PRACTICA, 82 %.
- Sin diferencias apreciables entre agentes (SUPPORTS del 34 % en DAS al 46 % en el neutral).

### [HALLAZGO] Convergencia entre medidas independientes (exploratorio)

Pertinencia según el juez, por grupo de actividades definido en los controles de nombre y orden:

| Grupo de actividades | n | SUPPORTS (todas) | SUPPORTS (DOCUMENTADO institucional) | Tipo DOCUMENTADO correcto |
|---|---|---|---|---|
| Con numeral expreso: ACT04, 09, 10, 11, 15 (robustas) | 188 | 63 % [56; 70] | 75 % [66; 82] | 80 % |
| Disputadas DAS/MCO: ACT06, 07, 08, 16, 17, 18, 20 | 191 | 35 % [29; 42] | 33 % [26; 42] | 40 % |
| Ambiguas, sensibles al orden: ACT01, 02, 03, 12, 13 | 130 | 22 % [16; 30] | 16 % [10; 26] | 20 % |
| Otras: QC, liberación, criterios de reversión (ACT05, 14, 19) | 91 | 30 % [21; 40] | 21 % [11; 35] | 28 % |

Tres medidas obtenidas por vías distintas coinciden en el mismo gradiente:

1. estabilidad ante nombre, código y orden;
2. ambigüedad declarada por el árbitro;
3. respaldo textual según el juez.

Donde las fichas tienen texto expreso, la asignación es estable y las citas la sostienen (75 %). Donde las fichas no deciden, la asignación depende de la presentación y la mayoría de las citas DOCUMENTADO no respaldan lo afirmado (16-33 %). Es la evidencia experimental más fuerte de que la ambigüedad reside en el marco institucional y no en la lectura de una parte.

Queda pendiente validar el juez con la codificación humana antes de reportar sus tasas como medida definitiva.

### [VALIDACIÓN] Codificador 2 de la auditoría de citas: juez LLM Claude (2026-09-27)

- Vía «Alternativa si no hay codificadores neutrales» de `validacion_humana/GUIA_VALIDACION_HUMANA.md`: el segundo codificador es un LLM de modelo distinto al del codificador 1, para tener dos jueces de familias diferentes.
- Codificador: Claude Opus 5.5 (`claude-opus-5-5`, Anthropic), en sesión de Claude Code, codificación manual ítem por ítem (sin API ni script de juicio).
- Ceguera: solo se leyó `results/pilot/audit_sheet_coder2.csv` y la guía (sección de instrucciones para los codificadores). **No se abrieron** `audit_sheet_coder1.csv`, `audit_sheet_coder1_revisado.csv`, `audit_key.csv`, `judge_results.*`, `citation_audit_report.md` ni esta bitácora antes de terminar la codificación.
- Criterio de claim_type_correct para DOCUMENTADO: SI solo si el texto nombra expresamente la actividad de la fila, no solo la afirmación (regla 2 de la guía).
- Resultado (99 ítems): SUPPORTS 41, PARTIAL 46, DOES_NOT_SUPPORT 12. Tipo correcto: SI 33, NO 66; por tipo: DOCUMENTADO 7/59 SI, BUENA_PRACTICA 23/36, INFERIDO 3/4. Sin ítems vacíos.
- Las columnas no codificables quedaron intactas (verificado contra copia previa). Pendiente: `python citation_audit.py report --label pilot` para el kappa entre codificadores.

## 2026-09-27

### [VALIDACIÓN] Doble codificación de citas con dos LLM (plan B de la guía; no humana)

- Planillas recibidas: `results/pilot/audit_sheet_coder1_astra.csv` (LLM «ASTRA», procedencia a documentar) y `audit_sheet_coder2_opus5.5.csv` (Claude Opus 5.5). Ambas sobre los 99 ítems ciegos (A y R ocultos).
- **Incidencia en ASTRA:** la planilla se guardó con «;» como separador y los textos de fuente que contenían «;» quedaron truncados en el primer punto y coma. ASTRA dejó 32 ítems sin codificar, casi todos fuentes externas (su texto lista CAN/CANNOT_SUPPORT con «;»). La ausencia no es aleatoria; las comparaciones con ASTRA usan 67 ítems. Opus 5.5 codificó los 99 sin alterar ningún ítem.
- Código: `citation_audit.py report` acepta `--coders`, `--coder-names` y `--coder-kind`; lee CSV con «,» o «;» y BOM; empareja por ítem; informa κ y acuerdo simple entre cada par (codificador-codificador y codificador-juez).

### [HALLAZGO] Concordancia entre codificadores LLM y juez

| Par | Pertinencia, 3 niveles | Tipo correcto | Pertinencia binaria (exploratoria) |
|---|---|---|---|
| ASTRA – Opus 5.5 (n = 67) | κ 0,69 (84 %) | κ 0,83 (96 %) | κ 0,75 |
| ASTRA – juez Gemini (n = 67) | κ 0,32 (60 %) | κ 0,39 (75 %) | κ 0,51 |
| Opus 5.5 – juez Gemini (n = 99) | κ 0,50 (68 %) | κ 0,55 (78 %) | κ 0,68 |

- Juez frente al consenso de ambos codificadores: κ = 0,43 (n = 56). **En la escala de 3 niveles, el juez no alcanza el umbral preespecificado (κ ≥ 0,60).**
- **El desacuerdo se concentra en la frontera PARTIAL / DOES_NOT_SUPPORT:** el juez es más severo (DOES_NOT_SUPPORT 26 % en estos ítems, frente a 3 % de ASTRA y 12 % de Opus; 14 ítems PARTIAL según Opus son DOES_NOT_SUPPORT para el juez). La proporción de **SUPPORTS coincide** entre las tres fuentes: juez 38 %, Opus 41 %, ASTRA 36 %, consenso 38 %.
- En tipo de afirmación, los codificadores son más estrictos que el juez: marcan correcto el 13 % (ASTRA) y el 33 % (Opus), frente al 60 % del juez.
- **Decisión de reporte:**
  - reportar la tasa de **respaldo pleno (SUPPORTS) ≈ 40 %**, respaldada por tres modelos de familias distintas y con concordancia binaria sustancial Opus-juez (κ 0,68), como resultado principal de pertinencia;
  - no reportar como validada la tasa DOES_NOT_SUPPORT del juez (21,5 %); indicar el rango 3-26 % según el evaluador;
  - el análisis binario no estaba preespecificado y se declara exploratorio.
- **Limitaciones a declarar:**
  - la validación es entre LLM, no humana;
  - Opus 5.5 pertenece a la misma familia del asistente que diseñó el experimento (sin acceso a los resultados al codificar, pero con posible sesgo compartido);
  - falta documentar la procedencia de ASTRA;
  - ASTRA perdió 32 ítems no aleatorios por un problema de formato.
- Opcional: reenviar a ASTRA los 32 ítems en un formato seguro para completar la muestra.

### [VALIDACIÓN] Preparación de la recodificación de ASTRA

- Confirmado: los 32 ítems perdidos por ASTRA son exactamente los que tienen «;» en `source_text`.
- Generada `results/pilot/audit_sheet_coder1_excel_es.csv`: mismos 99 ítems en el mismo orden, separador «;», todos los campos entre comillas, UTF-8 con BOM. Verificado que al releerla es idéntica al original.
- Plan: ASTRA recodifica los 99 ítems en una sesión nueva, sin acceso a su codificación anterior, a la de Opus ni a la del juez. Salida: `audit_sheet_coder1_astra_v2.csv`. Se conserva `audit_sheet_coder1_astra.csv` (primera pasada) para medir la consistencia test-retest en los 67 ítems comunes.

### [VALIDACIÓN] Segunda pasada de ASTRA (`results/pilot/audit_sheet_coder1_astra_v2.csv`)

- Verificación independiente: 99 filas; ningún campo de ítem alterado respecto de la planilla original; 99 ítems codificados; H004 íntegro (499 caracteres, 6 «;»). Según ASTRA, sesión sin acceso a codificaciones previas.
- Distribución: SUPPORTS 49, PARTIAL 45, DOES_NOT_SUPPORT 5; tipo correcto SI 49 / NO 50.
- **Consistencia de ASTRA consigo mismo** (67 ítems comunes con la primera pasada): pertinencia κ 0,68 (84 %), estable; tipo de afirmación κ 0,34 (70 %), inestable (de 13 % a unos 49 % de SI).
- Informe regenerado con la segunda pasada: `results/pilot/citation_audit_report.md`.

### [HALLAZGO] Concordancia final (ASTRA 2.ª pasada, Opus 5.5, juez Gemini; n = 99)

| Par | Pertinencia, 3 niveles | Binaria SUPPORTS/no (exploratoria) | Tipo correcto |
|---|---|---|---|
| ASTRA – Opus | κ 0,70 (83 %) | κ 0,80 | κ 0,64 (82 %) |
| ASTRA – juez | κ 0,36 (60 %) | κ 0,57 | κ 0,52 (76 %) |
| Opus – juez | κ 0,50 (68 %) | κ 0,68 | κ 0,55 (78 %) |

- Juez frente al consenso de los codificadores: κ = 0,48 (n = 82). En 3 niveles sigue por debajo de 0,60: **el juez no queda validado en la escala fina**.
- Respaldo pleno (SUPPORTS): juez 38 %, Opus 41 %, ASTRA 49,5 %, consenso 49 % [38; 59]. El juez es el más conservador.
- DOES_NOT_SUPPORT: juez 26 %, Opus 12 %, ASTRA 5 %. El juez es más severo, sobre todo con las citas institucionales (12 de 61, frente a 3 y 1).
- **Decisión de reporte (sustituye a la anterior):**
  - respaldo pleno de las citas entre el **38 % y el 50 %** según el evaluador, con el juez como cota inferior;
  - «no respalda» entre el 5 % y el 26 %; no se reporta una cifra única;
  - el gradiente por grupo de actividades (numeral expreso 75 %, disputadas 33 %, ambiguas 16 %) procede del juez sobre 600 citas; al ser el juez conservador, los niveles absolutos pueden estar subestimados, pero el orden relativo es la conclusión relevante;
  - la corrección del tipo de afirmación no se reporta como medida fiable: la consistencia del propio ASTRA es baja (κ 0,34).
- Limitaciones: validación entre LLM, no humana; Opus 5.5 es de la misma familia del asistente que diseñó el experimento; falta documentar la procedencia de ASTRA.

### [CÓDIGO] Reporte técnico en LaTeX (`reporte/`)

- `reporte/reporte_experimento.tex` y `.pdf` (14 páginas; compila sin errores ni desbordes). Contenido: propósito, diseño, resultados del piloto, controles de presentación, pertinencia de citas, clasificación de actividades, implicaciones para la matriz RACI, limitaciones, conclusiones y anexos (detalle por escenario y reproducibilidad).
- `reporte/generar_datos.py` genera 4 figuras (convergencia por escenario, entropía por actividad, controles de presentación y pertinencia por grupo), las tablas y 60 macros con todas las cifras a partir de `results/`. Paleta categórica validada con el validador de dataviz; las etiquetas directas compensan el contraste bajo del amarillo y el aqua.
- **Criterio de clasificación** (post hoc, explícito), sobre las repeticiones 1-5 y un umbral de A modal del 60 %: *robusta* (misma A en piloto, orden inverso, sin nombres y cruzada); *depende de la denominación* (estable con nombres en ambos órdenes, cambia sin nombres); *disputada DAS/MCO* (subtipo: con nombres DAS o MCO, sin nombres oscila con la casilla U01); *sensible al orden* (cambia con nombres al invertir el orden o no alcanza el 60 %). Cada actividad toma la clasificación más débil de sus escenarios.
- **Dictamen sobre la matriz de referencia:**
  - fortalecidas: ACT04, ACT10, ACT11, ACT15;
  - coincide apoyada en la denominación: ACT09;
  - discrepancia estable (decisión de diseño R5): ACT05;
  - discrepa apoyada en la denominación: ACT07, ACT08, ACT14, ACT17;
  - concurrencia DAS/MCO: ACT16;
  - ambiguas: ACT01, ACT02, ACT03, ACT06, ACT12, ACT13, ACT18, ACT19, ACT20.
- Correcciones durante la redacción: el pie de la figura 3 decía «215 decisiones»; son 1075 por condición (verificado en `decisions.csv`). Se evitaron guiones largos en tablas y texto.

### [REVISIÓN] Informe del revisor externo sobre el reporte (Major Revision, 80/100) y bloque A de respuesta

- Problemas señalados: (1) conclusión «solo numeral expreso → estabilidad» incompatible con ACT05 (robusta sin numeral) y ACT09 (numeral expreso, depende de la denominación); (2) el juez de citas no alcanzó κ ≥ 0,60 y aun así sostenía el gradiente 75/33/16 %; (3) taxonomía post hoc con 5 repeticiones; (4) un solo modelo; (5) semilla ambigua; (6) bootstrap no estratificado; (7) «conformidad» sin mecanismo demostrado; (8) estado del arte débil.
- Decisiones del usuario: destino = apoyo al artículo RACI; réplica confirmatoria de la taxonomía preparada, **no lanzada**; sin codificadores humanos por ahora (gradiente exploratorio); se habilitará una API de OpenAI para una réplica parcial.
- **Desviación del plan detectada:** el README (auditoría, punto 3) decía que las tasas del juez solo se reportarían con κ aceptable. Se declara en el reporte; las tasas del juez y el gradiente pasan a exploratorios.
- Respaldos: `reporte/reporte_experimento_v1.tex.bak`, `reporte_experimento_v1.pdf.bak`, `generar_datos_v1.py.bak`.
- `generar_datos.py`: efecto de la deliberación por escenario con IC (tabla `efecto_escenario.tex`), bootstrap estratificado por escenario y por conglomerados de escenario (B = 4000, semilla 23); macros de validez formal frente a pertinencia; etiqueta de dictamen «Fortalecida» → «Estable con apoyo textual».
- **Resultados nuevos (sensibilidad, exploratorio):** efecto 0,191; estratificado [0,173; 0,210]; por conglomerados [0,152; 0,229]; por escenario 0,09 (S04) a 0,27 (S05), IC > 0 en los 10. De 589 citas auditadas con identificador existente y fragmento literal, el juez da SUPPORTS 41 % y DOES_NOT_SUPPORT 21 %.
- Semilla verificada en el código: `1000 + run` fija el barajado y se envía como `seed` de la API; temperature y top_p no se envían (valores por defecto); max_output_tokens 16 384.
- Reporte v2 (18 páginas, compila sin errores ni desbordes): resumen y conclusiones reescritos (estabilidad ≠ sustento ≠ corrección); §1.1 Trabajos relacionados con 11 referencias verificadas en la web; §2.7 y Tabla 3 de estatus (confirmatorio / preespecificado secuencial / exploratorio); Tabla 4 por escenario; §5.1 validez formal frente a pertinencia; §6 exploratoria con el párrafo sobre ACT05/ACT09; limitaciones ampliadas.
- Verificado en el corpus: ningún numeral nombra la revisión de calidad topológica (lo más cercano, ISC 2.4 e ISC2 2.4).
- Carta de respuesta: `reporte/respuesta_revisor.md`.
- Pendiente: bloque B (preespecificación y material de la réplica, runs 6-10, unos USD 5,4, no lanzar sin autorización), muestra estratificada para codificación humana, diseño de la réplica con OpenAI.

### [MATERIAL] Referencias del estado del arte cargadas en el cuaderno `LLMs_debate`

- A pedido del usuario, las 11 referencias de §1.1 del reporte v2 se cargaron como fuentes en el cuaderno NotebookLM `LLMs_debate` (ID `5e7b7613-2bc9-4161-a3ac-59a717f46436`) con el CLI `nlm` (el MCP de cuadernos solo está configurado para opencode).
- Se usó el PDF de texto completo de cada una (ACL Anthology o arXiv). Du et al. y Smit et al. se cargaron desde arXiv (2305.14325, 2311.17371) porque los PDF de PMLR quedaron vacíos; Zheng et al. desde arXiv 2309.03882 porque OpenReview devolvió una página de verificación del navegador. Las fuentes vacías o inválidas se borraron.
- Verificado: 11 fuentes, todas con texto; títulos renombrados a «Autor año - título (venue)».
- Regla vigente: el cuaderno no se menciona en el cuerpo científico del reporte ni del artículo.

### [CÓDIGO] Soporte de un segundo proveedor: OpenAI `gpt-6-luna`

- Decisiones del usuario: réplica parcial con `gpt-6-luna` en dos partes. (a) Núcleo de la deliberación: fases 1, 2, 2c y árbitro, 10 escenarios × 5 repeticiones. (b) Los controles de presentación en fase 1. Crédito OpenAI de hasta USD 10 (tope del script: 8). Autorizados la implementación y una prueba corta; la réplica completa espera visto bueno.
- Modelo verificado con `GET /v1/models`. Precio verificado en la página oficial el 27/09/2026: USD 0,10 de entrada / 0,01 en caché / 0,125 de escritura en caché / 0,50 de salida por millón. Flex y Batch cuestan el 50 %.
- `config.py`:
  - `PRICES` y `prices_for()` por modelo;
  - `OPENAI_MODELS`, `OPENAI_REASONING_EFFORT = "medium"` y `OPENAI_SERVICE_TIER = "flex"` con `SERVICE_TIER_FACTOR`.
- `experiment.py`:
  - opción `--model`;
  - `OpenAICaller` sobre la API Responses, con `store=False` y `max_retries=0` (los reintentos los hace Runner) y `timeout=900`;
  - `strict_schema()`: `additionalProperties` false y todo requerido; los opcionales (`new_authority_justification`, `best_supported_proposals`) pasan a anulables;
  - `drop_nulls()` retira los null para que la salida tenga la misma forma que con Gemini;
  - `record_cost()` aplica el precio del modelo, la escritura en caché y el factor del nivel de servicio;
  - la configuración guardada registra el proveedor, el nivel de servicio y que la semilla **no se envía** (la API Responses no la admite; `SEED_BASE + run_id` solo baraja el orden).
- `analysis.py`: `costs()` también usa el precio de cada modelo.
- Regresión: el coste del piloto recalculado sigue siendo USD 22,413 (sin cambios). Los tres esquemas estrictos quedan bien formados. El modo simulado con `--model gpt-6-luna` pasa de punta a punta. SDK `openai` 3.19.2 instalado y añadido a `requirements.txt`.

### [EJECUCIÓN] Prueba corta con `gpt-6-luna` (`results/luna_smoke/`, `results/luna_smoke_flex/`)

- `luna_smoke`: S01, 1 repetición, todas las fases, nivel Standard.
  - 14/14 llamadas aceptadas, 0 errores, `finish_reason` completed; 99,7 % de fragmentos literales verificados (389/390); 0 identificadores inválidos; 0 unidades inválidas.
  - Coste: USD 0,085 por corrida. Tokens: entrada 382 524, de ellos 373 151 como escritura en caché (1,25×, no reutilizada, porque el prefijo cambia por agente); salida 75 922, de ellos 23 966 de razonamiento. Frente a Gemini en S01 genera unas 2 veces más salida por corrida.
  - Latencia media: 37 s por llamada.
  - Indicios con n = 1, sin valor inferencial: acuerdo 0,70 en F1, F2 y F2c; árbitro AMBIGUOUS en 4 de 5 actividades (Gemini: 17,7 % en el piloto).
- `luna_smoke_flex`: S01, 1 repetición, solo fase 1, nivel Flex. 5/5 aceptadas; la API devolvió `service_tier = flex`. Coste: USD 0,013 frente a 0,025 en Standard. Latencia: 24 s.
- Gasto acumulado estimado en OpenAI: unos USD 0,10.
- **Presupuesto de la réplica con Flex:** (a) unos USD 2,1 (50 corridas completas); (b) unos USD 1,9 (orden inverso, sin nombres y cruzada, 50 corridas de fase 1 cada una; la condición con nombres sale de la fase 1 de (a)). Total: unos **USD 4,0**. Pendiente: la preespecificación de predicciones y el visto bueno del usuario.

## 2026-09-28

### [DISEÑO] Réplica con otra familia de modelos: `gpt-6-luna` (PREESPECIFICADA ANTES DE EJECUTAR)

- Aprobada por el usuario («visto bueno») el 28/09/2026. Fecha y hora de este registro: 2026-09-28T11:35:27Z, anterior a cualquier corrida de la réplica. Las pruebas cortas `luna_smoke` y `luna_smoke_flex` (S01, run 1) no se usan en el análisis.
- **Pregunta:** ¿los fenómenos observados con `gemini-3.1-flash-lite` se repiten con un modelo de otra familia? Responde al punto 6 del revisor (un solo modelo) y a su prioridad 3.
- **Modelo:** `gpt-6-luna`, razonamiento `medium`, nivel de servicio Flex, sin semilla (la API no la admite). Material, prompts, escenarios y actividades idénticos byte a byte a los de Gemini (mismos hashes).
- **Ejecuciones:**
  - (a) `results/luna_pilot/`: material base, todas las fases, 10 escenarios × repeticiones 1-5 (50 corridas);
  - (b) `results/luna_order_reversed/`, `results/luna_ablation_anon/` y `results/luna_ablation_swap/`: material `order_reversed`, `ablation_anon` y `ablation_anon_swap`, solo fase 1, repeticiones 1-5 (50 corridas cada una);
  - la condición «con nombres, orden original» de (b) es la fase 1 de (a).
- Presupuesto: tope de USD 3 para (a) y de USD 1 para cada control; total estimado unos USD 4.

**Hipótesis y criterios de decisión** (fijados ahora; se aplican tal cual):

H1. **Efecto de la deliberación.** DELIBERATION_EFFECT > 0, con un IC 95 % por bootstrap estratificado por escenario que excluya el 0. El control F2c no converge: su delta tiene un IC que incluye el 0 o un valor absoluto < 0,03.
- *Se replica* si se cumplen ambas condiciones.
- Secundario: efecto > 0 en al menos 8 de 10 escenarios.

H2. **Dirección de los cambios.** Al menos el 70 % de los cambios de A en la fase 2 se dirigen a la opción más frecuente entre las propuestas vistas (Gemini: 89 %).
- Sin valor inferencial si hay menos de 30 cambios.

H3. **Controles de presentación.** Estimandos: proporción de decisiones de fase 1 con DAS y con MCO como A; comparaciones pareadas por corrida en las repeticiones 1-5, con IC por bootstrap (`compare_ablation.py`).
- H3a, con nombres: invertir el orden cambia la proporción de DAS menos de 5 pp (el IC contiene el 0 o |Δ| < 5 pp).
- H3b, sin nombres: la unidad en la casilla saliente (U01, posición 2) gana. La proporción de DAS es mayor en `ablation_swap` que en `ablation_anon`, y la de MCO es mayor en `ablation_anon` que en `ablation_swap`, ambas con IC que excluyen el 0.
  - Si no se cumple, el efecto de saliencia de código y posición es propio de Gemini y no del corpus. Es un resultado informativo en cualquier caso.

H4. **Taxonomía de actividades.** Se aplica sin cambios `classify_cell()` de `reporte/generar_datos.py`: umbral del 60 %, repeticiones 1-5; la estabilidad tras la deliberación se mide con la fase 2 de (a).
- H4a: de las cinco actividades robustas con Gemini, al menos 4 son robustas con Luna y con la misma A modal. Predicción: ACT04 DAS, ACT05 DAS, ACT10 DAS, ACT11 DAS, ACT15 ODC.
- H4b: de las nueve actividades no robustas con Gemini (sensibles al orden: ACT01, 02, 03, 06, 12, 13, 18, 19 y 20), al menos 7 no son robustas con Luna.
- H4c, descriptivo: acuerdo en la clase de cada actividad entre modelos (20 actividades, 4 clases), con κ de Cohen; y coincidencia de la A modal tras la deliberación entre modelos.
- *La taxonomía se replica* si se cumplen H4a y H4b.

H5. **Validez formal de las citas.** Al menos el 95 % de los fragmentos citados es literal (Gemini: 97,2 %).

**Lectura prevista:**
- Replicación de H1 y H4 con fallo de H3b: la deliberación y la separación entre actividades estables e inestables serían propiedades del corpus y del protocolo, y el mecanismo de desempate por saliencia sería propio del modelo.
- Fallo de H4a: la estabilidad observada con Gemini reflejaría en parte priores de ese modelo, lo que reforzaría la distinción entre estabilidad y respaldo documental.
- Ninguno de los resultados se interpreta como prueba de corrección institucional.

**Exploratorio** (no forma parte de los criterios): ambigüedad del árbitro por actividad; sesgo hacia la propia unidad; coincidencia con REFERENCE_RACI; auditoría de pertinencia de citas (no se ejecuta ahora).

### [EJECUCIÓN] Réplica `gpt-6-luna`: lanzamiento e incidencia de límite de velocidad

- Primer lanzamiento a las 11:36 UTC, con (a) y (b) en paralelo y 5 hilos cada uno. Se detuvo a los pocos minutos: la organización tiene un límite de **200 000 tokens por minuto** para `gpt-6-luna`, y cada llamada usa unos 27 000. La mayoría de las llamadas recibió un 429.
- Los 429 se registran como errores de API y no generan coste. Solo se completaron algunas llamadas; ninguna corrida quedó a medias en el análisis, porque la política es de todo o nada.
- Relanzamiento en secuencia: (a) primero, luego los tres controles, con 3 hilos, `--resume` y salida sin búfer. El diseño preespecificado no cambia. Duración estimada: unas 4 horas.
- Script de evaluación `replica_luna.py`, escrito antes de ver los datos de Luna, que aplica H1-H5 tal como se preespecificaron. Verificado sobre los datos de Gemini:
  - la regla de clasificación reproduce exactamente la clasificación publicada;
  - el efecto de la deliberación es 0,191 [0,173; 0,210];
  - los cambios hacia la mayoría son el 89,5 % de 589.

### [EJECUCIÓN] Réplica `gpt-6-luna` completada

- `luna_pilot`: 50/50 corridas completas, todas las fases, USD 1,72; incluye unos 0,04 del lanzamiento abortado.
- `luna_order_reversed`, `luna_ablation_anon`, `luna_ablation_swap`: 50/50 cada una, solo fase 1; USD 0,38, 0,36 y 0,34.
- Ninguna corrida quedó incompleta. Gasto total estimado en OpenAI con las pruebas: unos USD 2,9.
- `analysis.py` se ejecutó en las cuatro. La evaluación está en `results/luna_pilot/replica_vs_gemini.md` y `.json` (`replica_luna.py`).

### [HALLAZGO] Resultado de la réplica frente a los criterios preespecificados: se cumplen H1-H5

| Hipótesis | Luna | Gemini | ¿Se cumple? |
|---|---|---|---|
| H1 efecto de la deliberación (estratificado) | 0,128 [0,108; 0,149]; control 0,003 [−0,011; 0,018]; > 0 en 10/10 escenarios | 0,191 | sí |
| H2 cambios hacia la mayoría | 92,7 % de 82 cambios | 89,5 % de 589 | sí |
| H3a con nombres, orden inverso, DAS | 60,0 % → 59,1 % (−0,9 pp [−4,1; +2,2]) | 44 → 46 % | sí |
| H3b saliencia sin nombres | DAS +10,0 pp [+6,6; +13,5] en la cruzada; MCO +7,3 pp [+4,5; +10,3] en la anónima | +16 / +25 pp | sí (efecto menor) |
| H4a robustas con igual A | 5/5 (ACT04, 05, 10 y 11 DAS; ACT15 ODC) | — | sí |
| H4b no robustas siguen no robustas | 8/9 (ACT03 pasa a robusta, DAS 100 %) | — | sí |
| H4c clase entre modelos (descriptivo) | κ = 0,30; misma A modal en 15/20 | — | — |
| H5 fragmentos literales | 99,6 % | 97,2 % | sí |

**Lectura (las diferencias son exploratorias):**
- **Se generaliza** lo que la réplica pretendía probar. Hay un efecto de la deliberación frente a un control que no converge. Los cambios siguen a la mayoría vista. Con nombres, el orden no mueve a DAS. Sin nombres, la casilla saliente gana. Las cinco asignaciones robustas se mantienen con la misma A. En particular, ACT05 (revisión de calidad) sigue asignada a DAS por ambos modelos (0 % de coincidencia con la referencia ISC en Luna), lo que refuerza que R5 es una decisión de diseño.
- **Es propio del modelo:**
  - la magnitud: Luna parte de más acuerdo (79,5 % frente a 68,9 %), cambia menos (9,5 % frente a 17,1 %) y su efecto de saliencia es menor;
  - la taxonomía fina: κ = 0,30. Luna es más estable, con 8 actividades robustas frente a 5; la separación robusta / no robusta se conserva, pero las categorías intermedias (denominación, disputada, orden) no se replican una a una;
  - **la ambigüedad declarada**: agentes 70-80 % frente a 4-11 %; árbitro 84,7 % frente a 17,7 %. La ambigüedad del árbitro no es una medida estable entre modelos y no debe usarse sola como evidencia de ambigüedad institucional. Esto debilita el argumento de las «tres medidas convergentes» del reporte;
  - la autoridad nueva: Luna la propone en el 4,5 % de las decisiones (Gemini en el 0,01 %). En ACT19 (criterios de reversión) es la A modal (80 %), coincidente con la referencia (AC nueva);
  - el sesgo hacia la propia unidad: Luna tiene menos (0 a +0,04, frente a +0,02 a +0,09).
- La A modal difiere en ACT01 (Gemini ODC; Luna DAS, que coincide con la referencia), ACT03 (DOS; DAS), ACT12 (ODC; MCO), ACT14 (OP; DAS) y ACT19 (OP; autoridad nueva).

### [CÓDIGO] Reporte v3: incorporación de la réplica con `gpt-6-luna`

- Redacción con la skill `redactor-tesis`: registro impersonal, sin rayas y con conectores entre párrafos. Se dividieron las frases de más de 32 palabras; solo quedan enumeraciones justificadas.
- Respaldos de la v2: `reporte/reporte_experimento_v2.tex.bak` y `.pdf.bak`, `generar_datos_v2.py.bak`, `respuesta_revisor_v2.md.bak`.
- `generar_datos.py`, sección 7:
  - métricas de ambos modelos con las mismas repeticiones (1-5) y el mismo cálculo (`modelos_metricas.tex`);
  - clasificación por actividad en ambos modelos (`modelos_clases.tex`);
  - figura de controles con los dos modelos (`controles_dos_modelos.pdf`);
  - tabla de dictamen con la A de Luna y la coincidencia con la referencia para cada modelo;
  - 40 macros nuevas; 124 en total, ninguna escrita a mano.
- Gemini con las repeticiones 1-5: efecto de la deliberación 0,186 [0,157; 0,214]; cambios hacia la mayoría 91 % (146); árbitro AMBIGUOUS 16 %. El 17,7 % del reporte corresponde a las 20 repeticiones.
- Reporte v3 (23 páginas; compila sin errores, sin desbordes ni referencias indefinidas):
  - nueva §7 con cuatro subsecciones;
  - resumen en dos párrafos y resumen ejecutivo con dos ítems nuevos (réplica; ambigüedad dependiente del modelo);
  - §1 (contribución), §1.1 (heterogeneidad), §2.2 y tabla de estatus (H1-H5 como confirmatorias);
  - §5.2: la ambigüedad del árbitro no tiene un nivel absoluto interpretable;
  - §6: división robustas/inestables replicada, categorías intermedias no;
  - §8: cada grupo de filas leído con los dos modelos;
  - limitaciones (diferencias técnicas de la réplica, predicciones del mismo equipo, ambigüedad), conclusiones y reproducibilidad.
- Carta `reporte/respuesta_revisor.md` actualizada: versión v3, numeración §8, punto 6 con la réplica ejecutada y tabla de resultados, taxonomía con H4a/H4b y κ, pendientes nuevos (paráfrasis de las instrucciones; réplica con Gemini 6-10 opcional).

## 2026-09-29

### [REVISIÓN] Segunda evaluación del revisor sobre el reporte v3: 92/100, revisión menor

- Da por resueltos los problemas mayores y valora la réplica preespecificada, «que confirma unas cosas y contradice otras».
- Pide cuatro cosas antes de enviar:
  1. codificación humana de las citas;
  2. una paráfrasis de las instrucciones como control pequeño;
  3. compactar el reporte (23 páginas es demasiado para la sección experimental de un artículo) y mover tablas a un suplemento;
  4. poner como eje de la introducción la contribución metodológica (perturbaciones contrafactuales).
- Decisiones del usuario: reporte compacto más suplemento; paráfrasis con Luna; codificación humana, más adelante.

### [DISEÑO] Control de paráfrasis de las instrucciones (PREESPECIFICADO ANTES DE EJECUTAR)

- Registro: 2026-09-29T11:21:57Z, antes de cualquier corrida con el material parafraseado.
- **Pregunta:** ¿los resultados principales dependen de la redacción literal de las instrucciones?
- **Material `paraphrase/`** (`build_paraphrase.py`):
  - los 11 archivos de instrucciones se reescribieron a mano con el mismo contenido y otra formulación;
  - el 86 % de las frases cambió (119/139); las idénticas son ítems de listas de riesgos y el ejemplo de la unidad X;
  - verificación automática: se conservan todos los códigos, campos del esquema, marcadores `{{...}}`, cifras y siglas; no hay marcadores prohibidos;
  - el corpus, los escenarios y las actividades son idénticos byte a byte.
- **Ejecución:** `results/luna_paraphrase/`, `gpt-6-luna` (Flex), todas las fases, 10 escenarios × repeticiones 1-3 (30 corridas), tope de USD 1,5. Se compara con `luna_pilot` en las repeticiones 1-3.
- Se eligió Luna porque es el modelo más barato y el que ya se usó en la réplica. No se parafrasea el material anonimizado: la saliencia depende de la presentación del corpus, no de la redacción de las instrucciones.

**Hipótesis y criterios de decisión:**
- P1. DELIBERATION_EFFECT > 0, con un IC 95 % estratificado por escenario que excluya el 0; el delta del control tiene un IC que incluye el 0 o un valor absoluto < 0,03.
- P2. Al menos el 70 % de los cambios de A en la fase 2 van hacia la mayoría vista. Sin valor inferencial si hay menos de 30 cambios.
- P3. Las cinco actividades robustas mantienen la misma A modal, con al menos el 60 %, en la fase 1 y en la fase 2: ACT04, ACT05, ACT10 y ACT11 con DAS; ACT15 con ODC.
- P4. En los casos escenario × actividad cuya A modal de fase 1 en `luna_pilot` (repeticiones 1-3) alcanza al menos el 60 %, la paráfrasis tiene la misma A modal en al menos el 80 % de ellos.
- P5. Al menos el 95 % de los fragmentos citados es literal.
- **La paráfrasis no altera los resultados principales** si se cumplen P1, P3 y P4. P2 y P5 son secundarias.
- **Descriptivo, sin criterio:** diferencia de acuerdo en F1 y del efecto frente a `luna_pilot` (repeticiones 1-3); ambigüedad declarada por agentes y árbitro (¿depende también de la redacción?); proporción de DAS como A; autoridad nueva.

### [EJECUCIÓN] Control de paráfrasis completado (`results/luna_paraphrase/`)

- 30/30 corridas completas, ninguna incompleta, 0 errores de API; USD 1,05. Gasto acumulado estimado en OpenAI: unos USD 4,0.
- Evaluación (`paraphrase_eval.py`, escrita antes de ver los datos): `results/luna_paraphrase/paraphrase_eval.md` y `.json`. Se corrigió un error de importación (`sys.path` con PYTHONSAFEPATH) que no afecta a la lógica.

### [HALLAZGO] La paráfrasis no altera los resultados principales: se cumplen P1-P5

| Criterio | Paráfrasis | Original (repeticiones 1-3) | ¿Se cumple? |
|---|---|---|---|
| P1 efecto de la deliberación (estratificado) | 0,074 [0,038; 0,111]; control 0,014 [−0,010; 0,040] | 0,131 [0,109; 0,151] | sí |
| P2 cambios hacia la mayoría | 87 % de 54 | 94 % de 50 | sí |
| P3 cinco robustas con igual A | 5/5 | 5/5 | sí |
| P4 misma A modal en casos estables | 39/41 (95 %) | — | sí |
| P5 fragmentos literales | 99,7 % | — | sí |

- Los dos casos que cambiaron estaban en el umbral: S10-ACT01 (ODC 60 % → DAS 53 %) y S08-ACT14 (DAS 60 % → autoridad nueva 53 %).
- **Exploratorio:**
  - la **magnitud** del efecto es sensible a la redacción. El acuerdo F1 es casi igual (79,2 % frente a 78,8 %), pero F2 queda en 88,2 % frente a 92,9 %;
  - la **ambigüedad declarada no depende de la redacción** (agentes 69,0 % frente a 69,8 %; árbitro 80,6 % frente a 84,5 %): es una propiedad del modelo;
  - la autoridad nueva y la proporción de DAS casi no varían.

### [CÓDIGO] Reporte v4: compacto con suplemento

- Respaldos de la v3: `reporte/reporte_experimento_v3.tex.bak` y `.pdf.bak`, `respuesta_revisor_v3.md.bak`.
- `reporte_experimento.tex` reescrito (13 páginas):
  - subtítulo «Un protocolo contrafactual para distinguir contenido documental y señales de presentación»;
  - resumen reescrito con la contribución primero;
  - §1 con las cuatro preguntas y las tres propiedades (estabilidad / respaldo documental / corrección);
  - §2 Método condensado; §3 Resultados: deliberación, perturbaciones en los dos modelos, estabilidad por actividad, réplica, paráfrasis (§3.5) y citas;
  - §4 Discusión, con §4.1 sobre las tres propiedades y las formulaciones del revisor, y §4.2 con las implicaciones para la matriz; limitaciones; conclusiones con la formulación del resultado central que propuso el revisor;
  - siglas desarrolladas (SCADA/EMS, ANDE, RACI, DAS, ISC, MCO, ODC).
- `reporte_suplemento.tex` nuevo (9 páginas): S1 material; S2 resultados complementarios; S3 clasificación con Gemini; S4 concordancia de los evaluadores y gradiente; S5 réplica; S6 paráfrasis; SA detalle por escenario; SB reproducibilidad. Referencias cruzadas con `xr-hyper` y numeración S con `tocloft`.
- `generar_datos.py`, sección 8: macros y tablas de la paráfrasis (`parafrasis_tabla.tex`, `parafrasis_desc.tex`, `parafrasis_cambios.tex`); 151 macros en total.
- Compilación: sin errores, sin desbordes, sin referencias indefinidas y sin rayas. `reporte_experimento.pdf` estaba abierto en un visor y bloqueado; se compiló primero como `reporte_experimento_v4.pdf` para verificar y, al liberarse, con el nombre definitivo; los archivos provisionales se borraron. Orden: suplemento, principal, suplemento, principal.
- Carta: se agregó la respuesta a la segunda ronda (cuatro puntos). La de la primera ronda se conserva, marcada como referida a la v3.

### [CÓDIGO] Artículo para *Group Decision and Negotiation* (`articulo_gdn/`)

- 2026-09-29. Decisiones del usuario: inglés; revista *Group Decision and Negotiation* (Springer Nature, plantilla `sn-jnl`, estilo autor-año `sn-basic`); autor Moises Britez (ANDE); **organización anonimizada** con seudónimos de unidades (DAS→ADM, ISC→ENG, MCO→MNT, ODC→DSP, GT/OP→OPD, DOS→SOD, DEL/DEN/DDR→OD1-OD3, GT/DT→TRD).
- Fuente: reporte v4 y su suplemento. No se añadió ninguna cifra nueva; todas proceden de `reporte/tablas/macros.tex` y `reporte/tablas/*.tex`.
- `main.tex` (21 páginas, ~6400 palabras, 8 tablas, 2 figuras): enfoque GDN (conformidad y deliberación grupal, Delphi, información compartida) sobre el protocolo contrafactual; nueva subsección de recomendaciones para usar la deliberación con LLM como apoyo a la decisión.
- `online_resource_1.tex` (8 páginas): material, efecto por escenario, entropía, clasificación en ambos modelos, concordancia de evaluadores de citas, réplica, paráfrasis, detalle por caso y reproducibilidad.
- `make_figures.py` ejecuta `generar_datos.py` sin tocar los cálculos (solo etiquetas en inglés y seudónimos); `make_esm_tables.py` traduce las tablas del reporte.
- `references.bib`: las 11 referencias verificadas del reporte más 21 clásicas (Asch, Janis, Stasser y Titus, Sunstein, Dalkey y Helmer, Kerr y Tindale, Kilgour y Eden, NIST 800-53/82, etc.), pendientes de cotejo de volumen y páginas.
- Correcciones respecto del reporte: el juez se describe como «otra versión del modelo» (no «otra familia», pues también es Gemini); el rango de respaldo pleno de los tres evaluadores es 38-49 % (el reporte decía 38-50 %).
- Pendientes (en rojo en el PDF): financiación, unidad del autor en conflicto de intereses, autorización institucional, repositorio de datos y código, declaración de uso de IA, agradecimientos. La filiación identifica a la organización pese a la anonimización.
- 2026-09-29, ajuste del usuario: filiación y correo pasan a la Facultad de Ciencias y Tecnologías, UNCA (moisesbritez92@fctunca.edu.py), en el artículo y en el suplemento; financiación propia (costes de la API pagados por el autor); el usuario confirma la declaración de uso de IA. Pendientes restantes: unidad del autor en el conflicto de intereses, autorización institucional, repositorio de datos y código, agradecimientos.

### [REVISIÓN] Artículo GDN frente a la guía de autores de la revista

- 2026-09-29. Guía consultada: link.springer.com/journal/10726/submission-guidelines.
- Incumplimientos encontrados y corregidos:
  - resumen de 281 palabras (límite 150-250): se redujo a 245;
  - revisión **doble ciego**: `main.tex` compila una versión anónima (`manuscript_anonymized.pdf`, sin autor, filiación, agradecimientos ni declaraciones identificatorias) y una `title_page.tex` aparte; el suplemento `ESM_1.pdf` también quedó anonimizado; metadatos PDF vacíos;
  - tablas citadas fuera de orden (Tabla 8 en §3.2; Tablas 5 y 7 en §4.4): ahora se citan en orden consecutivo;
  - DOI obligatorios: 21 DOI añadidos, verificados en api.crossref.org (título, revista, volumen y páginas). Correcciones de Crossref: Horton et al. (2023) tiene tres autores; Efron y Tibshirani con DOI de la edición de 1994 (Chapman and Hall/CRC); páginas de Choi, Wang, Liang, Zheng y Park. Sin DOI por no existir: ICML, ICLR, arXiv, Janis y PMBOK;
  - revistas abreviadas según la lista ISSN;
  - política de LLM: el uso de asistencia de IA pasa a Métodos (§4.7);
  - figuras: Arial de 8 pt o más, 174 mm de ancho, archivos `Fig1`/`Fig2` en EPS y PDF;
  - siglas definidas en la primera mención (CI, DMS, JSON, NIST, ENISA);
  - extensión: se condensaron la hoja de ruta de la introducción, §6.3 y las conclusiones; unas 8300 palabras de PDF con tablas (≈7500 sin tablas).
- `build.sh` genera los cuatro PDF. Pendientes: ORCID, unidad del autor, autorización institucional, repositorio anónimo de datos y código, agradecimientos.
