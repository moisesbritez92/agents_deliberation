# Informe del experimento: ablation_swap

## 1. Configuración experimental

- Etiqueta: `ablation_swap`; creada: 2026-09-26T23:19:59.618308+00:00
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

- Entrada: 4,672,975 (de ellos en caché: 1,451,300)
- Salida: 659,870 (razonamiento: 238,216)

## 6. Coste aproximado

USD 1.8315 con precios configurados de 0.25 / 1.5 / 0.025 USD por millón (entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.

## 7. Decisiones iniciales (fase 1, especializados)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:8; ISC:5; TX_REG:4; DOS:2; OP:1 | 20.0 % | 15.0 % | 2.041 |
| S01 | ACT04 | DAS:20 | 100.0 % | 0.0 % | -0.000 |
| S01 | ACT06 | DAS:10; MCO:7; ISC:3 | 36.7 % | 0.0 % | 1.441 |
| S01 | ACT09 | ISC:19; MCO:1 | 90.0 % | 0.0 % | 0.286 |
| S01 | ACT12 | MCO:9; ODC:7; DOS:2; DT:1; ISC:1 | 50.0 % | 10.0 % | 1.813 |
| S02 | ACT02 | DEL:13; DOS:4; DT:2; OP:1 | 43.3 % | 10.0 % | 1.417 |
| S02 | ACT04 | DAS:20 | 100.0 % | 0.0 % | -0.000 |
| S02 | ACT05 | DAS:19; MCO:1 | 90.0 % | 0.0 % | 0.286 |
| S02 | ACT11 | DAS:18; DOS:2 | 80.0 % | 0.0 % | 0.469 |
| S03 | ACT06 | ISC:11; MCO:6; DAS:3 | 33.3 % | 0.0 % | 1.406 |
| S03 | ACT07 | DAS:19; MCO:1 | 90.0 % | 0.0 % | 0.286 |
| S03 | ACT09 | ISC:12; MCO:8 | 53.3 % | 0.0 % | 0.971 |
| S03 | ACT13 | ODC:17; MCO:1; DOS:1; OP:1 | 70.0 % | 0.0 % | 0.848 |
| S04 | ACT06 | DAS:18; MCO:2 | 80.0 % | 5.0 % | 0.469 |
| S04 | ACT11 | DAS:19; MCO:1 | 90.0 % | 0.0 % | 0.286 |
| S04 | ACT17 | DAS:15; ISC:4; MCO:1 | 50.0 % | 5.0 % | 0.992 |
| S04 | ACT18 | ODC:10; DAS:6; OP:3; DOS:1 | 30.0 % | 5.0 % | 1.648 |
| S05 | ACT01 | DOS:15; OP:2; DAS:2; ODC:1 | 53.3 % | 0.0 % | 1.192 |
| S05 | ACT06 | DAS:18; MCO:2 | 80.0 % | 0.0 % | 0.469 |
| S05 | ACT09 | ISC:9; DAS:6; MCO:5 | 40.0 % | 0.0 % | 1.539 |
| S05 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S06 | ACT03 | ISC:9; DAS:6; DOS:4; OP:1 | 23.3 % | 0.0 % | 1.720 |
| S06 | ACT04 | DAS:18; MCO:1; ISC:1 | 80.0 % | 0.0 % | 0.569 |
| S06 | ACT05 | DAS:16; MCO:2; ISC:2 | 66.7 % | 0.0 % | 0.922 |
| S06 | ACT12 | MCO:15; ISC:2; OTHER:1; TX_REG:1; DAS:1 | 53.3 % | 45.0 % | 1.292 |
| S06 | ACT13 | ODC:19; OP:1 | 90.0 % | 0.0 % | 0.286 |
| S07 | ACT10 | DAS:20 | 100.0 % | 0.0 % | -0.000 |
| S07 | ACT11 | DAS:15; DOS:5 | 50.0 % | 0.0 % | 0.811 |
| S07 | ACT14 | OP:10; DAS:3; ODC:3; DT:3; DOS:1 | 20.0 % | 5.0 % | 1.948 |
| S07 | ACT19 | OP:7; DAS:4; ISC:4; DT:3; DOS:1; ODC:1 | 13.3 % | 0.0 % | 2.302 |
| S08 | ACT08 | DAS:20 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT14 | DAS:10; ODC:5; OP:3; ISC:2 | 26.7 % | 0.0 % | 1.743 |
| S08 | ACT15 | ODC:19; OP:1 | 90.0 % | 0.0 % | 0.286 |
| S08 | ACT16 | DAS:10; MCO:10 | 53.3 % | 0.0 % | 1.000 |
| S09 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S09 | ACT18 | DAS:15; MCO:5 | 56.7 % | 0.0 % | 0.811 |
| S09 | ACT19 | DAS:9; ODC:4; ISC:3; OP:3; DT:1 | 23.3 % | 5.0 % | 2.020 |
| S09 | ACT20 | DAS:15; MCO:4; ODC:1 | 56.7 % | 0.0 % | 0.992 |
| S10 | ACT01 | ODC:17; DAS:2; DOS:1 | 76.7 % | 0.0 % | 0.748 |
| S10 | ACT14 | ODC:20 | 100.0 % | 5.0 % | -0.000 |
| S10 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S10 | ACT16 | DAS:17; MCO:3 | 76.7 % | 5.0 % | 0.610 |
| S10 | ACT20 | ODC:10; DAS:9; MCO:1 | 50.0 % | 0.0 % | 1.234 |

Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):

| Escenario | DAS | ISC | MCO | ODC |
|---|---|---|---|---|
| S01 | 52.0 % | 52.0 % | 44.0 % | 48.0 % |
| S02 | 65.0 % | 80.0 % | 70.0 % | 70.0 % |
| S03 | 65.0 % | 75.0 % | 60.0 % | 70.0 % |
| S04 | 70.0 % | 40.0 % | 90.0 % | 70.0 % |
| S05 | 80.0 % | 55.0 % | 55.0 % | 70.0 % |
| S06 | 64.0 % | 56.0 % | 56.0 % | 60.0 % |
| S07 | 55.0 % | 50.0 % | 55.0 % | 60.0 % |
| S08 | 60.0 % | 75.0 % | 70.0 % | 60.0 % |
| S09 | 70.0 % | 75.0 % | 65.0 % | 60.0 % |
| S10 | 80.0 % | 80.0 % | 72.0 % | 80.0 % |

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
| S01 | 59.3 % | [0.520, 0.673] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 40.0 % | n/d |
| S02 | 78.3 % | [0.700, 0.900] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 65.0 % | n/d |
| S03 | 61.7 % | [0.558, 0.675] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 35.0 % | n/d |
| S04 | 62.5 % | [0.558, 0.667] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 35.0 % | n/d |
| S05 | 68.3 % | [0.608, 0.742] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 45.0 % | n/d |
| S06 | 62.7 % | [0.467, 0.780] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 40.0 % | n/d |
| S07 | 45.8 % | [0.408, 0.508] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 25.0 % | n/d |
| S08 | 67.5 % | [0.567, 0.783] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 50.0 % | n/d |
| S09 | 59.2 % | [0.500, 0.692] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 35.0 % | n/d |
| S10 | 80.7 % | [0.740, 0.873] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 64.0 % | n/d |

Global: acuerdo 64.6 % → n/d; CONVERGENCE_DELTA = n/d (IC95 bootstrap sobre corridas [n/d, n/d]). Mayor consenso no implica mayor corrección.

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

- AMBIGUITY_RATE antes: 2.7 %; después: n/d
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

Media por actividad: 0.864 bits antes y n/d bits después. Entropía baja indica asignación estable; alta, sensible a la interpretación. No es una medida de corrección.

## 12. Cambios de posición

POSITION_CHANGE_RATE global: n/d.

| Agente | Escenario | n | Cambio de A | MAINTAIN | MODIFY | AMBIGUOUS | Declaración incoherente |
|---|---|---|---|---|---|---|---|

Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).

| Agente | P propia | P neutral | Diferencia | n |
|---|---|---|---|---|
| DAS | 52.6 % | 47.4 % | 0.051 | 215 |
| ISC | 14.4 % | 12.6 % | 0.019 | 215 |
| MCO | 12.6 % | 4.2 % | 0.084 | 215 |
| ODC | 26.0 % | 20.9 % | 0.051 | 215 |

## 13. Evidencia más utilizada

- EVIDENCE_VALIDITY_RATE: 99.7 % de 2832 citas
- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): 0.0 %
- A sin evidencia institucional válida: 0.4 %
- Violación de jerarquía (DOCUMENTADO con fuente no institucional): 0.4 %
- Cita textual verificada en la fuente: 98.5 % de 2832; en afirmaciones DOCUMENTADO: 98.6 % de 1749
- Proporción de citas INFERIDO: 4.0 %
La verificación textual prueba que el fragmento existe en la fuente citada, no que nombre la actividad; la pertinencia se audita con citation_audit.py.

| source_id | kind | total | phase1 | phase2 |
|---|---|---|---|---|
| NIST_CM_01 | externa | 291 | 291 | 0 |
| U01_2_2 | institucional | 151 | 151 | 0 |
| U01_2_1 | institucional | 137 | 137 | 0 |
| U13_2_5 | institucional | 124 | 124 | 0 |
| U22_2_2 | institucional | 123 | 123 | 0 |
| U10_2_1 | institucional | 121 | 121 | 0 |
| U12_2_8 | institucional | 114 | 114 | 0 |
| U13_2_6 | institucional | 110 | 110 | 0 |
| NIST_OT_01 | externa | 91 | 91 | 0 |
| ENISA_CHG_02 | externa | 83 | 83 | 0 |
| NIST_CM_02 | externa | 73 | 73 | 0 |
| U10_2_2 | institucional | 70 | 70 | 0 |
| U08_2_3 | institucional | 69 | 69 | 0 |
| U01_2_4 | institucional | 65 | 65 | 0 |
| ERCOT_03 | externa | 64 | 64 | 0 |
| U13_2_1 | institucional | 61 | 61 | 0 |
| U22_2_1 | institucional | 57 | 57 | 0 |
| ENISA_CHG_01 | externa | 54 | 54 | 0 |
| PJM_04 | externa | 53 | 53 | 0 |
| U12_2_6 | institucional | 48 | 48 | 0 |

## 14. Comparación post hoc con REFERENCE_RACI

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la correspondencia de columnas indicada en el README (Origen, GT*, AC).

| activity_id | activity | REFERENCE_A | match_individual_especializados_f1 | match_neutral_f1 | match_post_debate_f2 | match_control_sin_debate_f2c | match_arbitro_f3 |
|---|---|---|---|---|---|---|---|
| ACT01 | Definir el requisito y el alcance del cambio | DAS | 10.0 % | 10.0 % | n/d | n/d | n/d |
| ACT02 | Certificar los datos de la instalación (configuración física y parámetros) | ORIGIN | 82.5 % | 80.0 % | n/d | n/d | n/d |
| ACT03 | Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación) | DAS | 30.0 % | 60.0 % | n/d | n/d | n/d |
| ACT04 | Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros) | DAS | 96.7 % | 93.3 % | n/d | n/d | n/d |
| ACT05 | Revisar la calidad topológica y de nomenclatura del modelo construido | ISC | 5.0 % | 0.0 % | n/d | n/d | n/d |
| ACT06 | Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones | ISC | 17.5 % | 50.0 % | n/d | n/d | n/d |
| ACT07 | Unificar modelo y adquisición en la base integrada | ISC | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT08 | Preparar el paquete de implementación | ISC | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT09 | Aprobar las pruebas FAT/SAT y de integración | ISC | 66.7 % | 66.7 % | n/d | n/d | n/d |
| ACT10 | Administrar y actualizar los aplicativos EMS | DAS | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT11 | Validar el estimador de estado, el flujo de potencia y demás aplicaciones | DAS | 86.7 % | 93.3 % | n/d | n/d | n/d |
| ACT12 | Verificar la correspondencia de mímicos y modelo con la instalación física | ORIGIN | 12.5 % | 40.0 % | n/d | n/d | n/d |
| ACT13 | Aceptar mímicos, alarmas y el uso operativo | ODC | 90.0 % | 70.0 % | n/d | n/d | n/d |
| ACT14 | Autorizar la liberación de la versión a producción | NEW_AUTHORITY | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT15 | Habilitar o suspender la ventana de intervención en tiempo real | ODC | 98.8 % | 100.0 % | n/d | n/d | n/d |
| ACT16 | Ejecutar el respaldo y la carga en producción | MCO | 32.5 % | 20.0 % | n/d | n/d | n/d |
| ACT17 | Mantener el registro técnico de configuración | ISC | 20.0 % | 20.0 % | n/d | n/d | n/d |
| ACT18 | Verificar el sistema después de la actualización y cerrar el cambio | DAS | 52.5 % | 80.0 % | n/d | n/d | n/d |
| ACT19 | Aprobar los criterios de reversión y su delegación | NEW_AUTHORITY | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT20 | Ejecutar la reversión | MCO | 12.5 % | 0.0 % | n/d | n/d | n/d |

### Matriz RACI modal

Matrices completas por grupo (A, R, C, I por unidad, con frecuencia y celdas inestables) en `modal_raci.md` y `modal_raci.csv`. Resumen de la comparación celda a celda:

| Grupo | Celdas idénticas | Celdas A/R idénticas | A recuperada | Celdas inestables |
|---|---|---|---|---|
| especializados_f1 | 17.9 % | 75.0 % | 35.0 % | 48 de 140 |
| neutral_f1 | 20.7 % | 78.6 % | 50.0 % | 39 de 140 |

## 15. Limitaciones

- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de perspectivas es inducida por el prompt, no por conocimiento independiente.
- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad observada puede reflejar el marco institucional o la lectura del modelo.
- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede orientar la respuesta aunque no revele la asignación.
- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.
- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).
- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.
- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye la del servicio.
