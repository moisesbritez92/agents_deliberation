# Informe del experimento: luna_smoke

## 1. Configuración experimental

- Etiqueta: `luna_smoke`; creada: 2026-09-28T01:41:11.459929+00:00
- Escenarios: 1 (S01); repeticiones: 1
- Agentes: DAS, ISC, MCO, ODC, NEUTRAL, ARBITER
- Semillas: no enviada (la API Responses no la admite); SEED_BASE + run_id = 1000 + run_id solo baraja el orden
- Orden de ejecución: repetición externa; escenarios en orden barajado con semilla por repetición; orden de agentes barajado por corrida
- Parámetros de generación: `{"temperature": "default del modelo (no enviado)", "max_output_tokens": 16384, "response_mime_type": "application/json", "response_json_schema": "json_schema strict (strict_schema: opcionales anulables, null retirados)", "seed": "no enviada (la API Responses no la admite); SEED_BASE + run_id = 1000 + run_id solo baraja el orden", "top_p": "default del modelo (no enviado)", "store": false, "max_attempts_invalid_json": 3, "max_attempts_api_error": 8, "run_policy": "todo o nada: sin los 5 agentes de fase 1, los 4 de fase 2 y los 4 de fase 2c no se llama al árbitro"}`
- SDK: {'openai': '3.19.2', 'python': '3.13.13'}

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
- `agente_junior/resumen_resultados_ercot_nmms.md`: incluye una matriz RACI didáctica
- `evaluaciones_articulo.md`: revisión del artículo
- `flujo_actualizacion_bd_scada_ems_propuesto_DTE.pdf`: flujo organizativo propuesto
- `flujo_propuesto_inicial.pdf`: flujo organizativo propuesto
- `memory.md`: notas de trabajo con conclusiones del artículo
- `Propuesta_Procedimiento_Actualizacion_Base_SCADA_EMS_Version00 (003).docx`: propuesta organizativa de una de las partes
- `resumen_correos/01_Resumen_hilo_DTE_procedimiento_SCADA_EMS.md`: posturas de las partes, no evidencia
- `resumen_correos/02_Postura_GT_DAS_modelado_topologico.md`: posturas de las partes, no evidencia

## 3. Modelo

`gpt-6-luna`, thinking_level = `medium`. El mismo modelo para todos los agentes y el árbitro.

## 4. Número de llamadas e integridad

- Llamadas registradas (incluidos reintentos): 14; previstas sin reintentos: 14
- Corridas completas (con árbitro): 1 de 1
- Errores de API: 0
- JSON válido: 100.0 %; actividades completas: 100.0 %
- Control de contaminación del material enviado: {'OK': 14}. REFERENCE_RACI no se envió a ningún agente (el script de ejecución no lee `posthoc/`).

## 5. Tokens consumidos

- Entrada: 382,524 (de ellos en caché: 9,331)
- Salida: 75,922 (razonamiento: 23,966)

## 6. Coste aproximado

USD 0.0847 con precios configurados para `gpt-6-luna` de 0.1 / 0.5 / 0.01 USD por millón (entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.

## 7. Decisiones iniciales (fase 1, especializados)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:4 | 100.0 % | 100.0 % | -0.000 |
| S01 | ACT04 | DAS:4 | 100.0 % | 25.0 % | -0.000 |
| S01 | ACT06 | DAS:2; MCO:2 | 33.3 % | 100.0 % | 1.000 |
| S01 | ACT09 | ISC:4 | 100.0 % | 75.0 % | -0.000 |
| S01 | ACT12 | ISC:2; DAS:1; MCO:1 | 16.7 % | 100.0 % | 1.500 |

Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):

| Escenario | DAS | ISC | MCO | ODC |
|---|---|---|---|---|
| S01 | 100.0 % | 60.0 % | 80.0 % | 60.0 % |

## 8. Decisiones posteriores al debate (fase 2)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:4 | 100.0 % | 100.0 % | -0.000 |
| S01 | ACT04 | DAS:4 | 100.0 % | 0.0 % | -0.000 |
| S01 | ACT06 | DAS:2; MCO:2 | 33.3 % | 100.0 % | 1.000 |
| S01 | ACT09 | ISC:4 | 100.0 % | 100.0 % | -0.000 |
| S01 | ACT12 | ISC:2; DAS:1; MCO:1 | 16.7 % | 100.0 % | 1.500 |

## 9. Consenso

| Escenario | Acuerdo antes | IC95 antes | Acuerdo después | IC95 después | CONVERGENCE_DELTA | IC95 delta | Consenso estricto antes | Consenso estricto después |
|---|---|---|---|---|---|---|---|---|
| S01 | 70.0 % | [n/d, n/d] | 70.0 % | [n/d, n/d] | 0.000 | [n/d, n/d] | 60.0 % | 60.0 % |

Global: acuerdo 70.0 % → 70.0 %; CONVERGENCE_DELTA = 0.000 (IC95 bootstrap sobre corridas [n/d, n/d]). Mayor consenso no implica mayor corrección.

**Brazo control (fase 2c):** los mismos agentes reconsideran su decisión inicial sin ver propuestas ajenas. DELIBERATION_EFFECT = CONVERGENCE_DELTA − CONVERGENCE_DELTA_CONTROL estima la convergencia atribuible a la información de los demás, descontando la que produce el solo hecho de responder dos veces.

- Acuerdo en el control: 70.0 %; CONVERGENCE_DELTA_CONTROL = 0.000 (IC95 [n/d, n/d])
- DELIBERATION_EFFECT = 0.000 (IC95 [n/d, n/d])
- Cambio de A en el control: 5.0 % frente a 0.0 % con deliberación

| Escenario | Acuerdo control | Delta control | Efecto deliberación | IC95 efecto |
|---|---|---|---|---|
| S01 | 70.0 % | 0.000 | 0.000 | [n/d, n/d] |

## 10. Ambigüedad

- AMBIGUITY_RATE antes: 80.0 %; después: 80.0 %
- Árbitro, veredicto AMBIGUOUS: 80.0 %
- PROPOSED_NEW_AUTHORITY como A: 0.0 % de las decisiones de agentes

| Escenario | Actividad | Árbitro: consenso | Árbitro: A | Árbitro AMBIGUOUS |
|---|---|---|---|---|
| S01 | ACT02 | FULL:1 | DT:1 | 100.0 % |
| S01 | ACT04 | FULL:1 | DAS:1 | 0.0 % |
| S01 | ACT06 | NONE:1 | MCO:1 | 100.0 % |
| S01 | ACT09 | FULL:1 | ISC:1 | 100.0 % |
| S01 | ACT12 | NONE:1 | ISC:1 | 100.0 % |

## 11. Entropía de la autoridad (A)

Media por actividad: 0.500 bits antes y 0.500 bits después. Entropía baja indica asignación estable; alta, sensible a la interpretación. No es una medida de corrección.

## 12. Cambios de posición

POSITION_CHANGE_RATE global: 0.0 %.

| Agente | Escenario | n | Cambio de A | MAINTAIN | MODIFY | AMBIGUOUS | Declaración incoherente |
|---|---|---|---|---|---|---|---|
| DAS | S01 | 5 | 0.0 % | 1 | 0 | 4 | 0.0 % |
| ISC | S01 | 5 | 0.0 % | 4 | 0 | 1 | 0.0 % |
| MCO | S01 | 5 | 0.0 % | 1 | 0 | 4 | 0.0 % |
| ODC | S01 | 5 | 0.0 % | 1 | 0 | 4 | 0.0 % |

Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).

| Agente | P propia | P neutral | Diferencia | n |
|---|---|---|---|---|
| DAS | 60.0 % | 60.0 % | 0.000 | 5 |
| ISC | 40.0 % | 20.0 % | 0.200 | 5 |
| MCO | 0.0 % | 0.0 % | 0.000 | 5 |
| ODC | 0.0 % | 0.0 % | 0.000 | 5 |

## 13. Evidencia más utilizada

- EVIDENCE_VALIDITY_RATE: 100.0 % de 408 citas
- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): 0.0 %
- A sin evidencia institucional válida: 0.0 %
- Violación de jerarquía (DOCUMENTADO con fuente no institucional): 0.0 %
- Cita textual verificada en la fuente: 99.7 % de 390; en afirmaciones DOCUMENTADO: 100.0 % de 46
- Proporción de citas INFERIDO: 54.6 %
La verificación textual prueba que el fragmento existe en la fuente citada, no que nombre la actividad; la pertinencia se audita con citation_audit.py.

| source_id | kind | total | phase1 | phase2 |
|---|---|---|---|---|
| MCO_2_6 | institucional | 42 | 15 | 12 |
| DAS1_2_2 | institucional | 25 | 8 | 9 |
| DAS_2_1 | institucional | 24 | 10 | 6 |
| DAS2_2_1 | institucional | 20 | 7 | 6 |
| ISC2_2_4 | institucional | 19 | 5 | 8 |
| DAS_2_4 | institucional | 19 | 6 | 7 |
| NIST_CM_01 | externa | 18 | 6 | 7 |
| DT_2_4 | institucional | 18 | 5 | 7 |
| DAS1_2_1 | institucional | 14 | 5 | 3 |
| ISC2_2_3 | institucional | 14 | 5 | 4 |
| CTX_MIMICO | externa | 14 | 5 | 4 |
| PJM_01 | externa | 13 | 4 | 4 |
| DEL_2_5 | institucional | 13 | 5 | 3 |
| IEC61970_456_01 | externa | 13 | 5 | 4 |
| ERCOT_05 | externa | 13 | 5 | 4 |
| IEC61850_6_01 | externa | 11 | 4 | 4 |
| ERCOT_02 | externa | 11 | 4 | 3 |
| ISC2_2_2 | institucional | 11 | 2 | 4 |
| MCO_2_8 | institucional | 10 | 3 | 3 |
| CTX_UNIFILAR | externa | 9 | 4 | 2 |

## 14. Comparación post hoc con REFERENCE_RACI

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la correspondencia de columnas indicada en el README (Origen, GT*, AC).

| activity_id | activity | REFERENCE_A | match_individual_especializados_f1 | match_neutral_f1 | match_post_debate_f2 | match_control_sin_debate_f2c | match_arbitro_f3 |
|---|---|---|---|---|---|---|---|
| ACT02 | Certificar los datos de la instalación (configuración física y parámetros) | ORIGIN | 100.0 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT04 | Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros) | DAS | 100.0 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT06 | Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones | ISC | 0.0 % | 0.0 % | 0.0 % | 0.0 % | 0.0 % |
| ACT09 | Aprobar las pruebas FAT/SAT y de integración | ISC | 100.0 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT12 | Verificar la correspondencia de mímicos y modelo con la instalación física | ORIGIN | 0.0 % | 0.0 % | 0.0 % | 25.0 % | 0.0 % |

### Matriz RACI modal

Matrices completas por grupo (A, R, C, I por unidad, con frecuencia y celdas inestables) en `modal_raci.md` y `modal_raci.csv`. Resumen de la comparación celda a celda:

| Grupo | Celdas idénticas | Celdas A/R idénticas | A recuperada | Celdas inestables |
|---|---|---|---|---|
| especializados_f1 | 42.9 % | 80.0 % | 60.0 % | 10 de 35 |
| neutral_f1 | 40.0 % | 82.9 % | 60.0 % | 0 de 35 |
| deliberacion_f2 | 45.7 % | 80.0 % | 60.0 % | 6 de 35 |
| control_f2c | 42.9 % | 80.0 % | 60.0 % | 10 de 35 |
| arbitro_f3 | 42.9 % | 80.0 % | 60.0 % | 0 de 35 |

## 15. Limitaciones

- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de perspectivas es inducida por el prompt, no por conocimiento independiente.
- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad observada puede reflejar el marco institucional o la lectura del modelo.
- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede orientar la respuesta aunque no revele la asignación.
- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.
- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).
- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.
- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye la del servicio.
