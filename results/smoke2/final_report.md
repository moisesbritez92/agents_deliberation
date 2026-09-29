# Informe del experimento: smoke2

## 1. Configuración experimental

- Etiqueta: `smoke2`; creada: 2026-09-24T16:34:54.492009+00:00
- Escenarios: 1 (S01); repeticiones: 1
- Agentes: DAS, ISC, MCO, ODC, NEUTRAL, ARBITER
- Semillas: SEED_BASE + run_id = 1000 + run_id
- Orden de ejecución: repetición externa; escenarios en orden barajado con semilla por repetición; orden de agentes barajado por corrida
- Parámetros de generación: `{"temperature": "default del modelo (no enviado)", "max_output_tokens": 16384, "response_mime_type": "application/json", "response_json_schema": true, "seed": "SEED_BASE + run_id = 1000 + run_id", "max_attempts_invalid_json": 3, "max_attempts_api_error": 8, "run_policy": "todo o nada: sin los 5 agentes de fase 1 y los 4 de fase 2 no se llama al árbitro"}`
- SDK: {'google-genai': '2.25.0', 'python': '3.13.13'}

## 2. Documentos utilizados

- `articulo_atribuciones_scada_ems/evidencia_gobernanza.md`: trazabilidad de evidencia externa (consulta del curador, no se envía a agentes)
- `articulo_atribuciones_scada_ems/main.pdf`: artículo compilado (no usado; se usa main.tex)
- `articulo_atribuciones_scada_ems/main.tex`: artículo: contexto técnico curado en sources/external_sources.json; RACI extraída a posthoc/
- `atribuciones_dte/atribuciones_dte.md`: institucional (fichas DTE; se usa la transcripción .md)
- `atribuciones_dte/DTE-ISC.pdf`: institucional (fichas DTE; se usa la transcripción .md)
- `atribuciones_dte/DTE-ISC1.pdf`: institucional (fichas DTE; se usa la transcripción .md)
- `atribuciones_dte/DTE-ISC2.pdf`: institucional (fichas DTE; se usa la transcripción .md)
- `atribuciones_dte/DTE-ISC3.pdf`: institucional (fichas DTE; se usa la transcripción .md)
- `atribuciones_dte/DTE-MCO.pdf`: institucional (fichas DTE; se usa la transcripción .md)
- `atribuciones_gt/atribuciones_gt.md`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-DAS.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-DAS1.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-DAS2.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-DDR.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-DEL.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-DEN.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-DOS.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-DT.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-NAC.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-ODC.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-OP.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-TCE.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-TES.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-TMB.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `atribuciones_gt/GT-TSU.pdf`: institucional (fichas GT; se usa la transcripción .md)
- `casos/06963585.pdf`: bibliografía de casos (contenido resumido en corpus_external)
- `casos/Lessons_and_Experiences_in_the_Implementation_of_a_Consolidated_Transmission_Modeling_Data_System_at_ERCOT.md`: bibliografía de casos (contenido resumido en corpus_external)
- `casos/OntologyMatching_CIM-IEC61850_IEEE-SGridComm10.pdf`: bibliografía de casos (contenido resumido en corpus_external)
- `casos/pjm_m03a_rev27_2026-03-04.pdf`: bibliografía de casos (contenido resumido en corpus_external)

Documentos inspeccionados y excluidos del contexto de los agentes:

- `agente_junior/matriz_raci_scada_ems.md`: incluye una matriz RACI didáctica
- `agente_junior/matriz_raci_scada_ems.pdf`: incluye una matriz RACI didáctica
- `agente_junior/resumen_resultados_ercot_nmms.md`: incluye una matriz RACI didáctica
- `evaluaciones_articulo.md`: revisión del artículo
- `flujo_actualizacion_bd_scada_ems_propuesto_DTE.pdf`: flujo organizativo propuesto
- `flujo_propuesto_inicial.pdf`: flujo organizativo propuesto
- `memory.md`: notas de trabajo con conclusiones del artículo
- `Propuesta_Procedimiento_Actualizacion_Base_SCADA_EMS_Version00 (003).docx`: propuesta organizativa de una de las partes
- `resumen_correos/01_Resumen_hilo_DTE_procedimiento_SCADA_EMS.md`: posturas de las partes, no evidencia
- `resumen_correos/02_Postura_GT_DAS_modelado_topologico.md`: posturas de las partes, no evidencia

## 3. Modelo

`gemini-3.1-flash-lite`, thinking_level = `medium`. El mismo modelo para todos los agentes y el árbitro.

## 4. Número de llamadas e integridad

- Llamadas registradas (incluidos reintentos): 10; previstas sin reintentos: 10
- Corridas completas (con árbitro): 1 de 1
- Errores de API: 0
- JSON válido: 100.0 %; actividades completas: 100.0 %
- Control de contaminación del material enviado: {'OK': 10}. REFERENCE_RACI no se envió a ningún agente (el script de ejecución no lee `posthoc/`).

## 5. Tokens consumidos

- Entrada: 236,296 (de ellos en caché: 0)
- Salida: 25,972 (razonamiento: 9,094)

## 6. Coste aproximado

USD 0.098 con precios configurados de 0.25 / 1.5 / 0.025 USD por millón (entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.

## 7. Decisiones iniciales (fase 1, especializados)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:3; ISC:1 | 50.0 % | 25.0 % | 0.811 |
| S01 | ACT04 | DAS:4 | 100.0 % | 0.0 % | -0.000 |
| S01 | ACT06 | ISC:2; DAS:2 | 33.3 % | 0.0 % | 1.000 |
| S01 | ACT09 | ISC:4 | 100.0 % | 0.0 % | -0.000 |
| S01 | ACT12 | ODC:2; DAS:1; MCO:1 | 16.7 % | 0.0 % | 1.500 |

Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):

| Escenario | DAS | ISC | MCO | ODC |
|---|---|---|---|---|
| S01 | 60.0 % | 60.0 % | 100.0 % | 80.0 % |

## 8. Decisiones posteriores al debate (fase 2)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:4 | 100.0 % | 75.0 % | -0.000 |
| S01 | ACT04 | DAS:4 | 100.0 % | 0.0 % | -0.000 |
| S01 | ACT06 | ISC:3; DAS:1 | 50.0 % | 0.0 % | 0.811 |
| S01 | ACT09 | ISC:4 | 100.0 % | 0.0 % | -0.000 |
| S01 | ACT12 | ODC:4 | 100.0 % | 25.0 % | -0.000 |

## 9. Consenso

| Escenario | Acuerdo antes | IC95 antes | Acuerdo después | IC95 después | CONVERGENCE_DELTA | IC95 delta | Consenso estricto antes | Consenso estricto después |
|---|---|---|---|---|---|---|---|---|
| S01 | 60.0 % | [n/d, n/d] | 90.0 % | [n/d, n/d] | 0.300 | [n/d, n/d] | 40.0 % | 80.0 % |

Global: acuerdo 60.0 % → 90.0 %; CONVERGENCE_DELTA = 0.300 (IC95 bootstrap sobre corridas [n/d, n/d]). Mayor consenso no implica mayor corrección.

## 10. Ambigüedad

- AMBIGUITY_RATE antes: 5.0 %; después: 20.0 %
- Árbitro, veredicto AMBIGUOUS: 20.0 %
- PROPOSED_NEW_AUTHORITY como A: 0.0 % de las decisiones de agentes

| Escenario | Actividad | Árbitro: consenso | Árbitro: A | Árbitro AMBIGUOUS |
|---|---|---|---|---|
| S01 | ACT02 | MAJORITY:1 | DT:1 | 100.0 % |
| S01 | ACT04 | FULL:1 | DAS:1 | 0.0 % |
| S01 | ACT06 | MAJORITY:1 | ISC:1 | 0.0 % |
| S01 | ACT09 | FULL:1 | ISC:1 | 0.0 % |
| S01 | ACT12 | MAJORITY:1 | ODC:1 | 0.0 % |

## 11. Entropía de la autoridad (A)

Media por actividad: 0.662 bits antes y 0.162 bits después. Entropía baja indica asignación estable; alta, sensible a la interpretación. No es una medida de corrección.

## 12. Cambios de posición

POSITION_CHANGE_RATE global: 20.0 %.

| Agente | Escenario | n | Cambio de A | MAINTAIN | MODIFY | AMBIGUOUS | Declaración incoherente |
|---|---|---|---|---|---|---|---|
| DAS | S01 | 5 | 20.0 % | 2 | 2 | 1 | 40.0 % |
| ISC | S01 | 5 | 20.0 % | 3 | 2 | 0 | 20.0 % |
| MCO | S01 | 5 | 20.0 % | 4 | 1 | 0 | 0.0 % |
| ODC | S01 | 5 | 20.0 % | 3 | 2 | 0 | 60.0 % |

Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).

| Agente | P propia | P neutral | Diferencia | n |
|---|---|---|---|---|
| DAS | 40.0 % | 40.0 % | 0.000 | 5 |
| ISC | 40.0 % | 20.0 % | 0.200 | 5 |
| MCO | 0.0 % | 0.0 % | 0.000 | 5 |
| ODC | 20.0 % | 20.0 % | 0.000 | 5 |

## 13. Evidencia más utilizada

- EVIDENCE_VALIDITY_RATE: 100.0 % de 120 citas
- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): 0.0 %
- A sin evidencia institucional válida: 0.0 %
- Violación de jerarquía (DOCUMENTADO con fuente no institucional): 0.0 %

| source_id | kind | total | phase1 | phase2 |
|---|---|---|---|---|
| PJM_01 | externa | 9 | 5 | 4 |
| ISC2_2_3 | institucional | 9 | 5 | 4 |
| DT_2_1 | institucional | 8 | 3 | 4 |
| EPRI_NMM_02 | externa | 8 | 4 | 4 |
| NIST_CM_01 | externa | 8 | 4 | 4 |
| DAS_2_1 | institucional | 7 | 4 | 3 |
| MCO_2_6 | institucional | 7 | 3 | 3 |
| ODC_2_1 | institucional | 7 | 3 | 4 |
| ERCOT_05 | externa | 7 | 3 | 4 |
| DAS1_2_1 | institucional | 7 | 3 | 4 |
| IEC61850_6_01 | externa | 6 | 2 | 4 |
| ISC2_2_1 | institucional | 5 | 2 | 3 |
| DAS_2_2 | institucional | 4 | 2 | 1 |
| DAS1_2_2 | institucional | 3 | 2 | 1 |
| TMB_2_1 | institucional | 3 | 1 | 1 |
| ISC2_2_2 | institucional | 3 | 1 | 2 |
| ISC_2_4 | institucional | 2 | 1 | 1 |
| DAS2_2_1 | institucional | 2 | 2 | 0 |
| ISC_2_5 | institucional | 2 | 1 | 1 |
| MCO_2_8 | institucional | 2 | 2 | 0 |

## 14. Comparación post hoc con REFERENCE_RACI

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la correspondencia de columnas indicada en el README (Origen, GT*, AC).

| activity_id | activity | REFERENCE_A | match_individual_especializados_f1 | match_neutral_f1 | match_post_debate_f2 | match_arbitro_f3 |
|---|---|---|---|---|---|---|
| ACT02 | Certificar los datos de la instalación (configuración física y parámetros) | ORIGIN | 75.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT04 | Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros) | DAS | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT06 | Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones | ISC | 50.0 % | 0.0 % | 75.0 % | 100.0 % |
| ACT09 | Aprobar las pruebas FAT/SAT y de integración | ISC | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT12 | Verificar la correspondencia de mímicos y modelo con la instalación física | ORIGIN | 0.0 % | 0.0 % | 0.0 % | 0.0 % |

## 15. Limitaciones

- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de perspectivas es inducida por el prompt, no por conocimiento independiente.
- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad observada puede reflejar el marco institucional o la lectura del modelo.
- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede orientar la respuesta aunque no revele la asignación.
- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.
- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).
- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.
- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye la del servicio.
