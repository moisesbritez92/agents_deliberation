# Informe del experimento: order_reversed

## 1. Configuración experimental

- Etiqueta: `order_reversed`; creada: 2026-09-26T23:34:37.507619+00:00
- Escenarios: 10 (S01, S02, S03, S04, S05, S06, S07, S08, S09, S10); repeticiones: 5
- Agentes: DAS, ISC, MCO, ODC, NEUTRAL, ARBITER
- Semillas: SEED_BASE + run_id = 1000 + run_id
- Orden de ejecución: repetición externa; escenarios en orden barajado con semilla por repetición; orden de agentes barajado por corrida
- Parámetros de generación: `{"temperature": "default del modelo (no enviado)", "max_output_tokens": 16384, "response_mime_type": "application/json", "response_json_schema": true, "seed": "SEED_BASE + run_id = 1000 + run_id", "max_attempts_invalid_json": 3, "max_attempts_api_error": 8, "run_policy": "todo o nada: sin los 5 agentes de fase 1, los 4 de fase 2 y los 4 de fase 2c no se llama al árbitro"}`
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

- Llamadas registradas (incluidos reintentos): 250; previstas sin reintentos: 250
- Corridas completas (con árbitro): 50 de 50
- Errores de API: 0
- JSON válido: 100.0 %; actividades completas: 100.0 %
- Control de contaminación del material enviado: {'OK': 250}. REFERENCE_RACI no se envió a ningún agente (el script de ejecución no lee `posthoc/`).

## 5. Tokens consumidos

- Entrada: 4,881,625 (de ellos en caché: 1,865,823)
- Salida: 637,031 (razonamiento: 222,149)

## 6. Coste aproximado

USD 1.7561 con precios configurados de 0.25 / 1.5 / 0.025 USD por millón (entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.

## 7. Decisiones iniciales (fase 1, especializados)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | ISC:11; DT:7; MCO:2 | 33.3 % | 20.0 % | 1.337 |
| S01 | ACT04 | DAS:19; ISC:1 | 90.0 % | 0.0 % | 0.286 |
| S01 | ACT06 | DAS:10; ISC:7; MCO:3 | 26.7 % | 0.0 % | 1.441 |
| S01 | ACT09 | ISC:18; MCO:1; OP:1 | 80.0 % | 0.0 % | 0.569 |
| S01 | ACT12 | ODC:7; ISC:6; MCO:5; DAS:1; OP:1 | 23.3 % | 15.0 % | 1.983 |
| S02 | ACT02 | DEL:10; ISC:8; DAS:1; DT:1 | 33.3 % | 10.0 % | 1.461 |
| S02 | ACT04 | DAS:20 | 100.0 % | 0.0 % | -0.000 |
| S02 | ACT05 | DAS:20 | 100.0 % | 5.0 % | -0.000 |
| S02 | ACT11 | DAS:19; DOS:1 | 90.0 % | 0.0 % | 0.286 |
| S03 | ACT06 | ISC:10; DAS:6; MCO:4 | 33.3 % | 0.0 % | 1.485 |
| S03 | ACT07 | DAS:20 | 100.0 % | 0.0 % | -0.000 |
| S03 | ACT09 | ISC:17; DAS:2; MCO:1 | 70.0 % | 0.0 % | 0.748 |
| S03 | ACT13 | OP:9; ODC:9; MCO:2 | 33.3 % | 0.0 % | 1.369 |
| S04 | ACT06 | DAS:18; ISC:1; MCO:1 | 80.0 % | 0.0 % | 0.569 |
| S04 | ACT11 | DAS:20 | 100.0 % | 0.0 % | -0.000 |
| S04 | ACT17 | DAS:15; ISC:5 | 56.7 % | 0.0 % | 0.811 |
| S04 | ACT18 | DAS:8; ODC:6; OP:6 | 30.0 % | 0.0 % | 1.571 |
| S05 | ACT01 | DOS:7; DAS:4; ODC:4; DEN:2; OP:2; ISC:1 | 20.0 % | 0.0 % | 2.339 |
| S05 | ACT06 | DAS:15; ISC:5 | 56.7 % | 0.0 % | 0.811 |
| S05 | ACT09 | ISC:14; DAS:4; ODC:1; OP:1 | 46.7 % | 0.0 % | 1.257 |
| S05 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S06 | ACT03 | ISC:13; DAS:7 | 56.7 % | 5.0 % | 0.934 |
| S06 | ACT04 | DAS:20 | 100.0 % | 5.0 % | -0.000 |
| S06 | ACT05 | DAS:16; ISC:4 | 66.7 % | 0.0 % | 0.722 |
| S06 | ACT12 | ISC:9; DAS:5; MCO:4; ODC:1; DT:1 | 26.7 % | 20.0 % | 1.915 |
| S06 | ACT13 | ODC:10; OP:8; DAS:1; DOS:1 | 33.3 % | 0.0 % | 1.461 |
| S07 | ACT10 | DAS:20 | 100.0 % | 0.0 % | -0.000 |
| S07 | ACT11 | DAS:19; DOS:1 | 90.0 % | 0.0 % | 0.286 |
| S07 | ACT14 | OP:19; ODC:1 | 90.0 % | 5.0 % | 0.286 |
| S07 | ACT19 | OP:19; DAS:1 | 90.0 % | 0.0 % | 0.286 |
| S08 | ACT08 | DAS:17; ISC:3 | 70.0 % | 0.0 % | 0.610 |
| S08 | ACT14 | OP:15; ODC:3; DAS:2 | 56.7 % | 5.0 % | 1.054 |
| S08 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT16 | DAS:17; MCO:2; ISC:1 | 70.0 % | 10.0 % | 0.748 |
| S09 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S09 | ACT18 | DAS:19; ISC:1 | 90.0 % | 10.0 % | 0.286 |
| S09 | ACT19 | OP:16; DAS:2; ISC:1; DOS:1 | 70.0 % | 10.0 % | 1.022 |
| S09 | ACT20 | DAS:19; MCO:1 | 90.0 % | 5.0 % | 0.286 |
| S10 | ACT01 | ODC:11; DOS:7; DAS:2 | 46.7 % | 0.0 % | 1.337 |
| S10 | ACT14 | ODC:15; OP:5 | 56.7 % | 0.0 % | 0.811 |
| S10 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S10 | ACT16 | DAS:20 | 100.0 % | 0.0 % | -0.000 |
| S10 | ACT20 | DAS:14; ODC:6 | 46.7 % | 0.0 % | 0.881 |

Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):

| Escenario | DAS | ISC | MCO | ODC |
|---|---|---|---|---|
| S01 | 56.0 % | 48.0 % | 48.0 % | 48.0 % |
| S02 | 85.0 % | 80.0 % | 80.0 % | 70.0 % |
| S03 | 60.0 % | 70.0 % | 75.0 % | 65.0 % |
| S04 | 80.0 % | 65.0 % | 65.0 % | 85.0 % |
| S05 | 60.0 % | 75.0 % | 55.0 % | 50.0 % |
| S06 | 60.0 % | 76.0 % | 60.0 % | 72.0 % |
| S07 | 85.0 % | 80.0 % | 80.0 % | 80.0 % |
| S08 | 85.0 % | 70.0 % | 85.0 % | 85.0 % |
| S09 | 90.0 % | 75.0 % | 80.0 % | 85.0 % |
| S10 | 68.0 % | 68.0 % | 76.0 % | 64.0 % |

## 8. Decisiones posteriores al debate (fase 2)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 |  | n/d | n/d | n/d |
| S01 | ACT04 |  | n/d | n/d | n/d |
| S01 | ACT06 |  | n/d | n/d | n/d |
| S01 | ACT09 |  | n/d | n/d | n/d |
| S01 | ACT12 |  | n/d | n/d | n/d |
| S02 | ACT02 |  | n/d | n/d | n/d |
| S02 | ACT04 |  | n/d | n/d | n/d |
| S02 | ACT05 |  | n/d | n/d | n/d |
| S02 | ACT11 |  | n/d | n/d | n/d |
| S03 | ACT06 |  | n/d | n/d | n/d |
| S03 | ACT07 |  | n/d | n/d | n/d |
| S03 | ACT09 |  | n/d | n/d | n/d |
| S03 | ACT13 |  | n/d | n/d | n/d |
| S04 | ACT06 |  | n/d | n/d | n/d |
| S04 | ACT11 |  | n/d | n/d | n/d |
| S04 | ACT17 |  | n/d | n/d | n/d |
| S04 | ACT18 |  | n/d | n/d | n/d |
| S05 | ACT01 |  | n/d | n/d | n/d |
| S05 | ACT06 |  | n/d | n/d | n/d |
| S05 | ACT09 |  | n/d | n/d | n/d |
| S05 | ACT15 |  | n/d | n/d | n/d |
| S06 | ACT03 |  | n/d | n/d | n/d |
| S06 | ACT04 |  | n/d | n/d | n/d |
| S06 | ACT05 |  | n/d | n/d | n/d |
| S06 | ACT12 |  | n/d | n/d | n/d |
| S06 | ACT13 |  | n/d | n/d | n/d |
| S07 | ACT10 |  | n/d | n/d | n/d |
| S07 | ACT11 |  | n/d | n/d | n/d |
| S07 | ACT14 |  | n/d | n/d | n/d |
| S07 | ACT19 |  | n/d | n/d | n/d |
| S08 | ACT08 |  | n/d | n/d | n/d |
| S08 | ACT14 |  | n/d | n/d | n/d |
| S08 | ACT15 |  | n/d | n/d | n/d |
| S08 | ACT16 |  | n/d | n/d | n/d |
| S09 | ACT15 |  | n/d | n/d | n/d |
| S09 | ACT18 |  | n/d | n/d | n/d |
| S09 | ACT19 |  | n/d | n/d | n/d |
| S09 | ACT20 |  | n/d | n/d | n/d |
| S10 | ACT01 |  | n/d | n/d | n/d |
| S10 | ACT14 |  | n/d | n/d | n/d |
| S10 | ACT15 |  | n/d | n/d | n/d |
| S10 | ACT16 |  | n/d | n/d | n/d |
| S10 | ACT20 |  | n/d | n/d | n/d |

## 9. Consenso

| Escenario | Acuerdo antes | IC95 antes | Acuerdo después | IC95 después | CONVERGENCE_DELTA | IC95 delta | Consenso estricto antes | Consenso estricto después |
|---|---|---|---|---|---|---|---|---|
| S01 | 50.7 % | [0.440, 0.553] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 28.0 % | n/d |
| S02 | 80.8 % | [0.733, 0.867] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 70.0 % | n/d |
| S03 | 59.2 % | [0.492, 0.708] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 40.0 % | n/d |
| S04 | 66.7 % | [0.558, 0.783] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 45.0 % | n/d |
| S05 | 55.8 % | [0.442, 0.675] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 35.0 % | n/d |
| S06 | 56.7 % | [0.500, 0.633] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 32.0 % | n/d |
| S07 | 92.5 % | [0.875, 0.975] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 85.0 % | n/d |
| S08 | 74.2 % | [0.675, 0.817] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 50.0 % | n/d |
| S09 | 87.5 % | [0.725, 1.000] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 80.0 % | n/d |
| S10 | 70.0 % | [0.660, 0.753] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 44.0 % | n/d |

Global: acuerdo 69.4 % → n/d; CONVERGENCE_DELTA = n/d (IC95 bootstrap sobre corridas [n/d, n/d]). Mayor consenso no implica mayor corrección.

**Brazo control (fase 2c):** los mismos agentes reconsideran su decisión inicial sin ver propuestas ajenas. DELIBERATION_EFFECT = CONVERGENCE_DELTA − CONVERGENCE_DELTA_CONTROL estima la convergencia atribuible a la información de los demás, descontando la que produce el solo hecho de responder dos veces.

- Acuerdo en el control: n/d; CONVERGENCE_DELTA_CONTROL = n/d (IC95 [n/d, n/d])
- DELIBERATION_EFFECT = n/d (IC95 [n/d, n/d])
- Cambio de A en el control: n/d frente a n/d con deliberación

| Escenario | Acuerdo control | Delta control | Efecto deliberación | IC95 efecto |
|---|---|---|---|---|
| S01 | n/d | n/d | n/d | [n/d, n/d] |
| S02 | n/d | n/d | n/d | [n/d, n/d] |
| S03 | n/d | n/d | n/d | [n/d, n/d] |
| S04 | n/d | n/d | n/d | [n/d, n/d] |
| S05 | n/d | n/d | n/d | [n/d, n/d] |
| S06 | n/d | n/d | n/d | [n/d, n/d] |
| S07 | n/d | n/d | n/d | [n/d, n/d] |
| S08 | n/d | n/d | n/d | [n/d, n/d] |
| S09 | n/d | n/d | n/d | [n/d, n/d] |
| S10 | n/d | n/d | n/d | [n/d, n/d] |

## 10. Ambigüedad

- AMBIGUITY_RATE antes: 2.9 %; después: n/d
- Árbitro, veredicto AMBIGUOUS: n/d
- PROPOSED_NEW_AUTHORITY como A: 0.0 % de las decisiones de agentes

| Escenario | Actividad | Árbitro: consenso | Árbitro: A | Árbitro AMBIGUOUS |
|---|---|---|---|---|
| S01 | ACT02 |  |  | n/d |
| S01 | ACT04 |  |  | n/d |
| S01 | ACT06 |  |  | n/d |
| S01 | ACT09 |  |  | n/d |
| S01 | ACT12 |  |  | n/d |
| S02 | ACT02 |  |  | n/d |
| S02 | ACT04 |  |  | n/d |
| S02 | ACT05 |  |  | n/d |
| S02 | ACT11 |  |  | n/d |
| S03 | ACT06 |  |  | n/d |
| S03 | ACT07 |  |  | n/d |
| S03 | ACT09 |  |  | n/d |
| S03 | ACT13 |  |  | n/d |
| S04 | ACT06 |  |  | n/d |
| S04 | ACT11 |  |  | n/d |
| S04 | ACT17 |  |  | n/d |
| S04 | ACT18 |  |  | n/d |
| S05 | ACT01 |  |  | n/d |
| S05 | ACT06 |  |  | n/d |
| S05 | ACT09 |  |  | n/d |
| S05 | ACT15 |  |  | n/d |
| S06 | ACT03 |  |  | n/d |
| S06 | ACT04 |  |  | n/d |
| S06 | ACT05 |  |  | n/d |
| S06 | ACT12 |  |  | n/d |
| S06 | ACT13 |  |  | n/d |
| S07 | ACT10 |  |  | n/d |
| S07 | ACT11 |  |  | n/d |
| S07 | ACT14 |  |  | n/d |
| S07 | ACT19 |  |  | n/d |
| S08 | ACT08 |  |  | n/d |
| S08 | ACT14 |  |  | n/d |
| S08 | ACT15 |  |  | n/d |
| S08 | ACT16 |  |  | n/d |
| S09 | ACT15 |  |  | n/d |
| S09 | ACT18 |  |  | n/d |
| S09 | ACT19 |  |  | n/d |
| S09 | ACT20 |  |  | n/d |
| S10 | ACT01 |  |  | n/d |
| S10 | ACT14 |  |  | n/d |
| S10 | ACT15 |  |  | n/d |
| S10 | ACT16 |  |  | n/d |
| S10 | ACT20 |  |  | n/d |

## 11. Entropía de la autoridad (A)

Media por actividad: 0.727 bits antes y n/d bits después. Entropía baja indica asignación estable; alta, sensible a la interpretación. No es una medida de corrección.

## 12. Cambios de posición

POSITION_CHANGE_RATE global: n/d.

| Agente | Escenario | n | Cambio de A | MAINTAIN | MODIFY | AMBIGUOUS | Declaración incoherente |
|---|---|---|---|---|---|---|---|

Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).

| Agente | P propia | P neutral | Diferencia | n |
|---|---|---|---|---|
| DAS | 57.7 % | 43.7 % | 0.140 | 215 |
| ISC | 27.0 % | 17.2 % | 0.098 | 215 |
| MCO | 7.9 % | 1.9 % | 0.060 | 215 |
| ODC | 25.1 % | 15.8 % | 0.093 | 215 |

## 13. Evidencia más utilizada

- EVIDENCE_VALIDITY_RATE: 90.7 % de 2790 citas
- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): 1.0 %
- A sin evidencia institucional válida: 14.3 %
- Violación de jerarquía (DOCUMENTADO con fuente no institucional): 13.8 %
- Cita textual verificada en la fuente: 89.3 % de 2790; en afirmaciones DOCUMENTADO: 85.5 % de 1644
- Proporción de citas INFERIDO: 5.6 %
La verificación textual prueba que el fragmento existe en la fuente citada, no que nombre la actividad; la pertinencia se audita con citation_audit.py.

| source_id | kind | total | phase1 | phase2 |
|---|---|---|---|---|
| NIST_CM_01 | externa | 316 | 316 | 0 |
| DAS_2_2 | institucional | 123 | 123 | 0 |
| DAS_2_4 | institucional | 119 | 119 | 0 |
| DAS1_2_2 | institucional | 114 | 114 | 0 |
| ODC_2_6 | institucional | 104 | 104 | 0 |
| DAS_2_1 | institucional | 97 | 97 | 0 |
| NIST_OT_01 | externa | 87 | 87 | 0 |
| ENISA_CHG_02 | externa | 82 | 82 | 0 |
| ODC_2_1 | institucional | 81 | 81 | 0 |
| ISC2_2_3 | institucional | 78 | 78 | 0 |
| ERCOT_03 | externa | 74 | 74 | 0 |
| GT/DAS | INEXISTENTE | 73 | 73 | 0 |
| DAS1_2_1 | institucional | 72 | 72 | 0 |
| NIST_CM_02 | externa | 69 | 69 | 0 |
| ENISA_CHG_01 | externa | 67 | 67 | 0 |
| DAS2_2_1 | institucional | 65 | 65 | 0 |
| OP_2_3 | institucional | 63 | 63 | 0 |
| PJM_04 | externa | 51 | 51 | 0 |
| GT/DAS2 | INEXISTENTE | 50 | 50 | 0 |
| ERCOT_02 | externa | 49 | 49 | 0 |

## 14. Comparación post hoc con REFERENCE_RACI

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la correspondencia de columnas indicada en el README (Origen, GT*, AC).

| activity_id | activity | REFERENCE_A | match_individual_especializados_f1 | match_neutral_f1 | match_post_debate_f2 | match_control_sin_debate_f2c | match_arbitro_f3 |
|---|---|---|---|---|---|---|---|
| ACT01 | Definir el requisito y el alcance del cambio | DAS | 15.0 % | 20.0 % | n/d | n/d | n/d |
| ACT02 | Certificar los datos de la instalación (configuración física y parámetros) | ORIGIN | 45.0 % | 60.0 % | n/d | n/d | n/d |
| ACT03 | Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación) | DAS | 35.0 % | 20.0 % | n/d | n/d | n/d |
| ACT04 | Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros) | DAS | 98.3 % | 100.0 % | n/d | n/d | n/d |
| ACT05 | Revisar la calidad topológica y de nomenclatura del modelo construido | ISC | 10.0 % | 0.0 % | n/d | n/d | n/d |
| ACT06 | Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones | ISC | 28.7 % | 30.0 % | n/d | n/d | n/d |
| ACT07 | Unificar modelo y adquisición en la base integrada | ISC | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT08 | Preparar el paquete de implementación | ISC | 15.0 % | 20.0 % | n/d | n/d | n/d |
| ACT09 | Aprobar las pruebas FAT/SAT y de integración | ISC | 81.7 % | 100.0 % | n/d | n/d | n/d |
| ACT10 | Administrar y actualizar los aplicativos EMS | DAS | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT11 | Validar el estimador de estado, el flujo de potencia y demás aplicaciones | DAS | 96.7 % | 86.7 % | n/d | n/d | n/d |
| ACT12 | Verificar la correspondencia de mímicos y modelo con la instalación física | ORIGIN | 2.5 % | 0.0 % | n/d | n/d | n/d |
| ACT13 | Aceptar mímicos, alarmas y el uso operativo | ODC | 47.5 % | 50.0 % | n/d | n/d | n/d |
| ACT14 | Autorizar la liberación de la versión a producción | NEW_AUTHORITY | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT15 | Habilitar o suspender la ventana de intervención en tiempo real | ODC | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT16 | Ejecutar el respaldo y la carga en producción | MCO | 5.0 % | 0.0 % | n/d | n/d | n/d |
| ACT17 | Mantener el registro técnico de configuración | ISC | 25.0 % | 20.0 % | n/d | n/d | n/d |
| ACT18 | Verificar el sistema después de la actualización y cerrar el cambio | DAS | 67.5 % | 70.0 % | n/d | n/d | n/d |
| ACT19 | Aprobar los criterios de reversión y su delegación | NEW_AUTHORITY | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT20 | Ejecutar la reversión | MCO | 2.5 % | 0.0 % | n/d | n/d | n/d |

### Matriz RACI modal

Matrices completas por grupo (A, R, C, I por unidad, con frecuencia y celdas inestables) en `modal_raci.md` y `modal_raci.csv`. Resumen de la comparación celda a celda:

| Grupo | Celdas idénticas | Celdas A/R idénticas | A recuperada | Celdas inestables |
|---|---|---|---|---|
| especializados_f1 | 19.3 % | 75.0 % | 30.0 % | 37 de 140 |
| neutral_f1 | 20.7 % | 75.0 % | 35.0 % | 26 de 140 |

## 15. Limitaciones

- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de perspectivas es inducida por el prompt, no por conocimiento independiente.
- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad observada puede reflejar el marco institucional o la lectura del modelo.
- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede orientar la respuesta aunque no revele la asignación.
- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.
- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).
- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.
- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye la del servicio.
