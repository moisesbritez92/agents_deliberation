# Informe del experimento: luna_ablation_swap

## 1. Configuración experimental

- Etiqueta: `luna_ablation_swap`; creada: 2026-09-28T15:12:38.858458+00:00
- Escenarios: 10 (S01, S02, S03, S04, S05, S06, S07, S08, S09, S10); repeticiones: 5
- Agentes: DAS, ISC, MCO, ODC, NEUTRAL, ARBITER
- Semillas: no enviada (la API Responses no la admite); SEED_BASE + run_id = 1000 + run_id solo baraja el orden
- Orden de ejecución: repetición externa; escenarios en orden barajado con semilla por repetición; orden de agentes barajado por corrida
- Parámetros de generación: `{"temperature": "default del modelo (no enviado)", "max_output_tokens": 16384, "response_mime_type": "application/json", "response_json_schema": "json_schema strict (strict_schema: opcionales anulables, null retirados)", "seed": "no enviada (la API Responses no la admite); SEED_BASE + run_id = 1000 + run_id solo baraja el orden", "top_p": "default del modelo (no enviado)", "store": false, "service_tier": "flex", "max_attempts_invalid_json": 3, "max_attempts_api_error": 8, "run_policy": "todo o nada: sin los 5 agentes de fase 1, los 4 de fase 2 y los 4 de fase 2c no se llama al árbitro"}`
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

- Llamadas registradas (incluidos reintentos): 250; previstas sin reintentos: 250
- Corridas completas (con árbitro): 50 de 50
- Errores de API: 0
- JSON válido: 100.0 %; actividades completas: 100.0 %
- Control de contaminación del material enviado: {'OK': 250}. REFERENCE_RACI no se envió a ningún agente (el script de ejecución no lee `posthoc/`).

## 5. Tokens consumidos

- Entrada: 4,547,225 (de ellos en caché: 3,741,105)
- Salida: 1,098,407 (razonamiento: 424,691)

## 6. Coste aproximado

USD 0.3437 con precios configurados para `gpt-6-luna` de 0.1 / 0.5 / 0.01 USD por millón (entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.

## 7. Decisiones iniciales (fase 1, especializados)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | NONE:9; DT:4; OTHER:4; MCO:3 | 26.7 % | 100.0 % | 1.858 |
| S01 | ACT04 | DAS:20 | 100.0 % | 80.0 % | -0.000 |
| S01 | ACT06 | MCO:20 | 100.0 % | 45.0 % | -0.000 |
| S01 | ACT09 | ISC:19; MCO:1 | 90.0 % | 100.0 % | 0.286 |
| S01 | ACT12 | MCO:16; ISC:4 | 66.7 % | 95.0 % | 0.722 |
| S02 | ACT02 | DEL:12; NONE:3; OTHER:2; DOS:2; DT:1 | 36.7 % | 100.0 % | 1.733 |
| S02 | ACT04 | DAS:20 | 100.0 % | 50.0 % | -0.000 |
| S02 | ACT05 | DAS:18; DEL:1; ISC:1 | 80.0 % | 85.0 % | 0.569 |
| S02 | ACT11 | DAS:19; DOS:1 | 90.0 % | 70.0 % | 0.286 |
| S03 | ACT06 | MCO:17; ISC:2; DAS:1 | 70.0 % | 40.0 % | 0.748 |
| S03 | ACT07 | DAS:14; ISC:5; MCO:1 | 46.7 % | 85.0 % | 1.076 |
| S03 | ACT09 | ISC:20 | 100.0 % | 95.0 % | -0.000 |
| S03 | ACT13 | ODC:12; MCO:8 | 40.0 % | 100.0 % | 0.971 |
| S04 | ACT06 | DAS:18; MCO:2 | 80.0 % | 80.0 % | 0.469 |
| S04 | ACT11 | DAS:20 | 100.0 % | 65.0 % | -0.000 |
| S04 | ACT17 | ISC:14; DAS:6 | 46.7 % | 65.0 % | 0.881 |
| S04 | ACT18 | DAS:19; MCO:1 | 90.0 % | 95.0 % | 0.286 |
| S05 | ACT01 | DAS:18; DOS:2 | 86.7 % | 80.0 % | 0.469 |
| S05 | ACT06 | MCO:18; DAS:2 | 80.0 % | 85.0 % | 0.469 |
| S05 | ACT09 | ISC:17; MCO:3 | 76.7 % | 100.0 % | 0.610 |
| S05 | ACT15 | ODC:20 | 100.0 % | 10.0 % | -0.000 |
| S06 | ACT03 | DAS:19; ISC:1 | 90.0 % | 95.0 % | 0.286 |
| S06 | ACT04 | DAS:20 | 100.0 % | 65.0 % | -0.000 |
| S06 | ACT05 | DAS:15; DOS:3; DEL:2 | 56.7 % | 95.0 % | 1.054 |
| S06 | ACT12 | MCO:20 | 100.0 % | 85.0 % | -0.000 |
| S06 | ACT13 | ODC:17; MCO:3 | 70.0 % | 90.0 % | 0.610 |
| S07 | ACT10 | DAS:20 | 100.0 % | 15.0 % | -0.000 |
| S07 | ACT11 | DAS:20 | 100.0 % | 75.0 % | -0.000 |
| S07 | ACT14 | DAS:15; NEW_AUTHORITY:4; MCO:1 | 63.3 % | 100.0 % | 0.992 |
| S07 | ACT19 | DAS:14; NEW_AUTHORITY:6 | 66.7 % | 100.0 % | 0.881 |
| S08 | ACT08 | DAS:15; MCO:5 | 50.0 % | 50.0 % | 0.811 |
| S08 | ACT14 | DAS:10; NEW_AUTHORITY:9; MCO:1 | 33.3 % | 100.0 % | 1.234 |
| S08 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT16 | MCO:20 | 100.0 % | 70.0 % | -0.000 |
| S09 | ACT15 | ODC:20 | 100.0 % | 5.0 % | -0.000 |
| S09 | ACT18 | DAS:19; MCO:1 | 90.0 % | 100.0 % | 0.286 |
| S09 | ACT19 | DAS:14; NEW_AUTHORITY:6 | 46.7 % | 95.0 % | 0.881 |
| S09 | ACT20 | DAS:10; MCO:10 | 40.0 % | 95.0 % | 1.000 |
| S10 | ACT01 | DAS:17; ODC:3 | 70.0 % | 50.0 % | 0.610 |
| S10 | ACT14 | DAS:11; MCO:4; NEW_AUTHORITY:4; ODC:1 | 23.3 % | 100.0 % | 1.619 |
| S10 | ACT15 | ODC:20 | 100.0 % | 5.0 % | -0.000 |
| S10 | ACT16 | DAS:12; MCO:8 | 46.7 % | 85.0 % | 0.971 |
| S10 | ACT20 | DAS:11; MCO:9 | 43.3 % | 90.0 % | 0.993 |

Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):

| Escenario | DAS | ISC | MCO | ODC |
|---|---|---|---|---|
| S01 | 76.0 % | 72.0 % | 76.0 % | 72.0 % |
| S02 | 65.0 % | 65.0 % | 60.0 % | 70.0 % |
| S03 | 55.0 % | 65.0 % | 85.0 % | 80.0 % |
| S04 | 85.0 % | 75.0 % | 90.0 % | 85.0 % |
| S05 | 60.0 % | 60.0 % | 70.0 % | 75.0 % |
| S06 | 96.0 % | 88.0 % | 84.0 % | 84.0 % |
| S07 | 90.0 % | 85.0 % | 90.0 % | 90.0 % |
| S08 | 100.0 % | 60.0 % | 85.0 % | 85.0 % |
| S09 | 80.0 % | 60.0 % | 85.0 % | 80.0 % |
| S10 | 80.0 % | 52.0 % | 64.0 % | 72.0 % |

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
| S01 | 76.7 % | [0.667, 0.853] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 64.0 % | n/d |
| S02 | 76.7 % | [0.708, 0.825] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 60.0 % | n/d |
| S03 | 64.2 % | [0.592, 0.692] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 35.0 % | n/d |
| S04 | 79.2 % | [0.675, 0.875] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 60.0 % | n/d |
| S05 | 85.8 % | [0.842, 0.875] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 75.0 % | n/d |
| S06 | 83.3 % | [0.787, 0.880] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 68.0 % | n/d |
| S07 | 82.5 % | [0.725, 0.925] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 70.0 % | n/d |
| S08 | 70.8 % | [0.683, 0.733] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 50.0 % | n/d |
| S09 | 69.2 % | [0.658, 0.725] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 45.0 % | n/d |
| S10 | 56.7 % | [0.520, 0.613] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 28.0 % | n/d |

Global: acuerdo 74.5 % → n/d; CONVERGENCE_DELTA = n/d (IC95 bootstrap sobre corridas [n/d, n/d]). Mayor consenso no implica mayor corrección.

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

- AMBIGUITY_RATE antes: 74.2 %; después: n/d
- Árbitro, veredicto AMBIGUOUS: n/d
- PROPOSED_NEW_AUTHORITY como A: 3.2 % de las decisiones de agentes

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

Media por actividad: 0.550 bits antes y n/d bits después. Entropía baja indica asignación estable; alta, sensible a la interpretación. No es una medida de corrección.

## 12. Cambios de posición

POSITION_CHANGE_RATE global: n/d.

| Agente | Escenario | n | Cambio de A | MAINTAIN | MODIFY | AMBIGUOUS | Declaración incoherente |
|---|---|---|---|---|---|---|---|

Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).

| Agente | P propia | P neutral | Diferencia | n |
|---|---|---|---|---|
| DAS | 54.4 % | 54.4 % | 0.000 | 215 |
| ISC | 12.1 % | 8.8 % | 0.033 | 215 |
| MCO | 20.5 % | 14.4 % | 0.060 | 215 |
| ODC | 15.8 % | 13.5 % | 0.023 | 215 |

## 13. Evidencia más utilizada

- EVIDENCE_VALIDITY_RATE: 100.0 % de 6215 citas
- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): 0.0 %
- A sin evidencia institucional válida: 0.1 %
- Violación de jerarquía (DOCUMENTADO con fuente no institucional): 0.9 %
- Cita textual verificada en la fuente: 99.5 % de 6215; en afirmaciones DOCUMENTADO: 99.6 % de 685
- Proporción de citas INFERIDO: 56.7 %
La verificación textual prueba que el fragmento existe en la fuente citada, no que nombre la actividad; la pertinencia se audita con citation_audit.py.

| source_id | kind | total | phase1 | phase2 |
|---|---|---|---|---|
| U01_2_4 | institucional | 534 | 534 | 0 |
| NIST_CM_01 | externa | 487 | 487 | 0 |
| U12_2_6 | institucional | 365 | 365 | 0 |
| U13_2_1 | institucional | 329 | 329 | 0 |
| U12_2_8 | institucional | 300 | 300 | 0 |
| U22_2_2 | institucional | 274 | 274 | 0 |
| U01_2_1 | institucional | 238 | 238 | 0 |
| NIST_OT_01 | externa | 235 | 235 | 0 |
| U10_2_1 | institucional | 218 | 218 | 0 |
| NIST_CM_02 | externa | 216 | 216 | 0 |
| IEC61970_456_01 | externa | 182 | 182 | 0 |
| U10_2_2 | institucional | 177 | 177 | 0 |
| U13_2_6 | institucional | 163 | 163 | 0 |
| ENISA_CHG_02 | externa | 160 | 160 | 0 |
| U08_2_4 | institucional | 142 | 142 | 0 |
| ERCOT_02 | externa | 113 | 113 | 0 |
| U01_2_2 | institucional | 112 | 112 | 0 |
| U08_2_3 | institucional | 105 | 105 | 0 |
| U15_2_7 | institucional | 104 | 104 | 0 |
| U22_2_1 | institucional | 93 | 93 | 0 |

## 14. Comparación post hoc con REFERENCE_RACI

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la correspondencia de columnas indicada en el README (Origen, GT*, AC).

| activity_id | activity | REFERENCE_A | match_individual_especializados_f1 | match_neutral_f1 | match_post_debate_f2 | match_control_sin_debate_f2c | match_arbitro_f3 |
|---|---|---|---|---|---|---|---|
| ACT01 | Definir el requisito y el alcance del cambio | DAS | 87.5 % | 70.0 % | n/d | n/d | n/d |
| ACT02 | Certificar los datos de la instalación (configuración física y parámetros) | ORIGIN | 62.5 % | 70.0 % | n/d | n/d | n/d |
| ACT03 | Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación) | DAS | 95.0 % | 100.0 % | n/d | n/d | n/d |
| ACT04 | Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros) | DAS | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT05 | Revisar la calidad topológica y de nomenclatura del modelo construido | ISC | 2.5 % | 0.0 % | n/d | n/d | n/d |
| ACT06 | Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones | ISC | 2.5 % | 5.0 % | n/d | n/d | n/d |
| ACT07 | Unificar modelo y adquisición en la base integrada | ISC | 25.0 % | 0.0 % | n/d | n/d | n/d |
| ACT08 | Preparar el paquete de implementación | ISC | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT09 | Aprobar las pruebas FAT/SAT y de integración | ISC | 93.3 % | 93.3 % | n/d | n/d | n/d |
| ACT10 | Administrar y actualizar los aplicativos EMS | DAS | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT11 | Validar el estimador de estado, el flujo de potencia y demás aplicaciones | DAS | 98.3 % | 100.0 % | n/d | n/d | n/d |
| ACT12 | Verificar la correspondencia de mímicos y modelo con la instalación física | ORIGIN | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT13 | Aceptar mímicos, alarmas y el uso operativo | ODC | 72.5 % | 80.0 % | n/d | n/d | n/d |
| ACT14 | Autorizar la liberación de la versión a producción | NEW_AUTHORITY | 28.3 % | 20.0 % | n/d | n/d | n/d |
| ACT15 | Habilitar o suspender la ventana de intervención en tiempo real | ODC | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT16 | Ejecutar el respaldo y la carga en producción | MCO | 70.0 % | 50.0 % | n/d | n/d | n/d |
| ACT17 | Mantener el registro técnico de configuración | ISC | 70.0 % | 60.0 % | n/d | n/d | n/d |
| ACT18 | Verificar el sistema después de la actualización y cerrar el cambio | DAS | 95.0 % | 100.0 % | n/d | n/d | n/d |
| ACT19 | Aprobar los criterios de reversión y su delegación | NEW_AUTHORITY | 30.0 % | 20.0 % | n/d | n/d | n/d |
| ACT20 | Ejecutar la reversión | MCO | 47.5 % | 10.0 % | n/d | n/d | n/d |

### Matriz RACI modal

Matrices completas por grupo (A, R, C, I por unidad, con frecuencia y celdas inestables) en `modal_raci.md` y `modal_raci.csv`. Resumen de la comparación celda a celda:

| Grupo | Celdas idénticas | Celdas A/R idénticas | A recuperada | Celdas inestables |
|---|---|---|---|---|
| especializados_f1 | 39.3 % | 79.3 % | 60.0 % | 33 de 140 |
| neutral_f1 | 34.3 % | 78.6 % | 60.0 % | 22 de 140 |

## 15. Limitaciones

- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de perspectivas es inducida por el prompt, no por conocimiento independiente.
- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad observada puede reflejar el marco institucional o la lectura del modelo.
- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede orientar la respuesta aunque no revele la asignación.
- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.
- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).
- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.
- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye la del servicio.
