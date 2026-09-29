# Informe del experimento: luna_ablation_anon

## 1. Configuración experimental

- Etiqueta: `luna_ablation_anon`; creada: 2026-09-28T14:34:55.749110+00:00
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

- Entrada: 4,547,225 (de ellos en caché: 3,637,180)
- Salida: 1,121,579 (razonamiento: 424,317)

## 6. Coste aproximado

USD 0.3554 con precios configurados para `gpt-6-luna` de 0.1 / 0.5 / 0.01 USD por millón (entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.

## 7. Decisiones iniciales (fase 1, especializados)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | MCO:9; NONE:4; OTHER:3; NEW_AUTHORITY:1; ISC:1; TX_REG:1; DT:1 | 23.3 % | 95.0 % | 2.258 |
| S01 | ACT04 | DAS:18; MCO:2 | 80.0 % | 90.0 % | 0.469 |
| S01 | ACT06 | MCO:20 | 100.0 % | 30.0 % | -0.000 |
| S01 | ACT09 | ISC:20 | 100.0 % | 95.0 % | -0.000 |
| S01 | ACT12 | MCO:16; ISC:4 | 60.0 % | 100.0 % | 0.722 |
| S02 | ACT02 | DEL:7; DOS:6; DT:4; NONE:3 | 30.0 % | 100.0 % | 1.926 |
| S02 | ACT04 | DAS:20 | 100.0 % | 65.0 % | -0.000 |
| S02 | ACT05 | DAS:19; DEL:1 | 90.0 % | 95.0 % | 0.286 |
| S02 | ACT11 | DAS:19; ODC:1 | 90.0 % | 45.0 % | 0.286 |
| S03 | ACT06 | MCO:16; ISC:4 | 73.3 % | 55.0 % | 0.722 |
| S03 | ACT07 | DAS:15; MCO:3; ISC:2 | 53.3 % | 100.0 % | 1.054 |
| S03 | ACT09 | ISC:20 | 100.0 % | 100.0 % | -0.000 |
| S03 | ACT13 | ODC:10; MCO:10 | 66.7 % | 100.0 % | 1.000 |
| S04 | ACT06 | DAS:16; MCO:4 | 66.7 % | 95.0 % | 0.722 |
| S04 | ACT11 | DAS:20 | 100.0 % | 45.0 % | -0.000 |
| S04 | ACT17 | ISC:19; DAS:1 | 90.0 % | 55.0 % | 0.286 |
| S04 | ACT18 | DAS:9; MCO:7; ODC:4 | 20.0 % | 100.0 % | 1.513 |
| S05 | ACT01 | DAS:17; DOS:3 | 70.0 % | 65.0 % | 0.610 |
| S05 | ACT06 | MCO:20 | 100.0 % | 85.0 % | -0.000 |
| S05 | ACT09 | ISC:18; MCO:2 | 80.0 % | 100.0 % | 0.469 |
| S05 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S06 | ACT03 | DAS:19; ISC:1 | 90.0 % | 100.0 % | 0.286 |
| S06 | ACT04 | DAS:19; MCO:1 | 90.0 % | 100.0 % | 0.286 |
| S06 | ACT05 | DAS:15; MCO:3; DEL:1; ODC:1 | 53.3 % | 100.0 % | 1.154 |
| S06 | ACT12 | MCO:14; ISC:6 | 53.3 % | 80.0 % | 0.881 |
| S06 | ACT13 | ODC:17; MCO:3 | 70.0 % | 100.0 % | 0.610 |
| S07 | ACT10 | DAS:20 | 100.0 % | 15.0 % | -0.000 |
| S07 | ACT11 | DAS:19; ODC:1 | 90.0 % | 85.0 % | 0.286 |
| S07 | ACT14 | DAS:14; NEW_AUTHORITY:6 | 53.3 % | 100.0 % | 0.881 |
| S07 | ACT19 | NEW_AUTHORITY:12; DAS:8 | 46.7 % | 95.0 % | 0.971 |
| S08 | ACT08 | MCO:13; DAS:7 | 70.0 % | 85.0 % | 0.934 |
| S08 | ACT14 | NEW_AUTHORITY:10; DAS:6; MCO:4 | 40.0 % | 100.0 % | 1.485 |
| S08 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT16 | MCO:20 | 100.0 % | 90.0 % | -0.000 |
| S09 | ACT15 | ODC:20 | 100.0 % | 5.0 % | -0.000 |
| S09 | ACT18 | DAS:10; MCO:10 | 46.7 % | 100.0 % | 1.000 |
| S09 | ACT19 | NEW_AUTHORITY:10; DAS:8; ODC:2 | 30.0 % | 85.0 % | 1.361 |
| S09 | ACT20 | MCO:18; DAS:2 | 80.0 % | 100.0 % | 0.469 |
| S10 | ACT01 | DAS:13; ODC:7 | 43.3 % | 75.0 % | 0.934 |
| S10 | ACT14 | DAS:14; MCO:3; ODC:2; NEW_AUTHORITY:1 | 46.7 % | 100.0 % | 1.319 |
| S10 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S10 | ACT16 | MCO:12; DAS:8 | 46.7 % | 95.0 % | 0.971 |
| S10 | ACT20 | MCO:14; DAS:6 | 46.7 % | 95.0 % | 0.881 |

Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):

| Escenario | DAS | ISC | MCO | ODC |
|---|---|---|---|---|
| S01 | 84.0 % | 88.0 % | 76.0 % | 68.0 % |
| S02 | 65.0 % | 70.0 % | 75.0 % | 60.0 % |
| S03 | 60.0 % | 45.0 % | 70.0 % | 75.0 % |
| S04 | 75.0 % | 70.0 % | 95.0 % | 65.0 % |
| S05 | 80.0 % | 85.0 % | 70.0 % | 80.0 % |
| S06 | 72.0 % | 80.0 % | 88.0 % | 76.0 % |
| S07 | 60.0 % | 75.0 % | 80.0 % | 60.0 % |
| S08 | 75.0 % | 75.0 % | 75.0 % | 75.0 % |
| S09 | 85.0 % | 55.0 % | 90.0 % | 75.0 % |
| S10 | 64.0 % | 72.0 % | 84.0 % | 60.0 % |

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
| S01 | 72.7 % | [0.647, 0.820] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 56.0 % | n/d |
| S02 | 77.5 % | [0.717, 0.833] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 65.0 % | n/d |
| S03 | 73.3 % | [0.692, 0.767] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 55.0 % | n/d |
| S04 | 69.2 % | [0.592, 0.792] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 55.0 % | n/d |
| S05 | 87.5 % | [0.775, 0.975] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 75.0 % | n/d |
| S06 | 71.3 % | [0.593, 0.840] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 48.0 % | n/d |
| S07 | 72.5 % | [0.642, 0.808] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 50.0 % | n/d |
| S08 | 77.5 % | [0.708, 0.842] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 60.0 % | n/d |
| S09 | 64.2 % | [0.567, 0.717] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 40.0 % | n/d |
| S10 | 56.7 % | [0.527, 0.600] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 24.0 % | n/d |

Global: acuerdo 72.2 % → n/d; CONVERGENCE_DELTA = n/d (IC95 bootstrap sobre corridas [n/d, n/d]). Mayor consenso no implica mayor corrección.

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

- AMBIGUITY_RATE antes: 77.2 %; después: n/d
- Árbitro, veredicto AMBIGUOUS: n/d
- PROPOSED_NEW_AUTHORITY como A: 5.0 % de las decisiones de agentes

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

Media por actividad: 0.629 bits antes y n/d bits después. Entropía baja indica asignación estable; alta, sensible a la interpretación. No es una medida de corrección.

## 12. Cambios de posición

POSITION_CHANGE_RATE global: n/d.

| Agente | Escenario | n | Cambio de A | MAINTAIN | MODIFY | AMBIGUOUS | Declaración incoherente |
|---|---|---|---|---|---|---|---|

Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).

| Agente | P propia | P neutral | Diferencia | n |
|---|---|---|---|---|
| DAS | 47.4 % | 39.5 % | 0.079 | 215 |
| ISC | 11.2 % | 10.7 % | 0.005 | 215 |
| MCO | 25.1 % | 26.5 % | -0.014 | 215 |
| ODC | 18.6 % | 12.6 % | 0.060 | 215 |

## 13. Evidencia más utilizada

- EVIDENCE_VALIDITY_RATE: 99.9 % de 6314 citas
- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): 0.0 %
- A sin evidencia institucional válida: 0.0 %
- Violación de jerarquía (DOCUMENTADO con fuente no institucional): 1.1 %
- Cita textual verificada en la fuente: 99.4 % de 6314; en afirmaciones DOCUMENTADO: 99.6 % de 667
- Proporción de citas INFERIDO: 56.3 %
La verificación textual prueba que el fragmento existe en la fuente citada, no que nombre la actividad; la pertinencia se audita con citation_audit.py.

| source_id | kind | total | phase1 | phase2 |
|---|---|---|---|---|
| U12_2_4 | institucional | 487 | 487 | 0 |
| NIST_CM_01 | externa | 467 | 467 | 0 |
| U01_2_8 | institucional | 409 | 409 | 0 |
| U01_2_6 | institucional | 304 | 304 | 0 |
| U13_2_1 | institucional | 302 | 302 | 0 |
| U12_2_1 | institucional | 287 | 287 | 0 |
| U10_2_1 | institucional | 235 | 235 | 0 |
| NIST_OT_01 | externa | 232 | 232 | 0 |
| NIST_CM_02 | externa | 210 | 210 | 0 |
| IEC61970_456_01 | externa | 208 | 208 | 0 |
| U10_2_2 | institucional | 189 | 189 | 0 |
| ENISA_CHG_02 | externa | 168 | 168 | 0 |
| U13_2_6 | institucional | 166 | 166 | 0 |
| U22_2_2 | institucional | 166 | 166 | 0 |
| U08_2_4 | institucional | 133 | 133 | 0 |
| ERCOT_02 | externa | 130 | 130 | 0 |
| U12_2_2 | institucional | 115 | 115 | 0 |
| U08_2_3 | institucional | 103 | 103 | 0 |
| U13_2_5 | institucional | 100 | 100 | 0 |
| CTX_MIMICO | externa | 92 | 92 | 0 |

## 14. Comparación post hoc con REFERENCE_RACI

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la correspondencia de columnas indicada en el README (Origen, GT*, AC).

| activity_id | activity | REFERENCE_A | match_individual_especializados_f1 | match_neutral_f1 | match_post_debate_f2 | match_control_sin_debate_f2c | match_arbitro_f3 |
|---|---|---|---|---|---|---|---|
| ACT01 | Definir el requisito y el alcance del cambio | DAS | 75.0 % | 100.0 % | n/d | n/d | n/d |
| ACT02 | Certificar los datos de la instalación (configuración física y parámetros) | ORIGIN | 55.0 % | 50.0 % | n/d | n/d | n/d |
| ACT03 | Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación) | DAS | 95.0 % | 100.0 % | n/d | n/d | n/d |
| ACT04 | Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros) | DAS | 95.0 % | 100.0 % | n/d | n/d | n/d |
| ACT05 | Revisar la calidad topológica y de nomenclatura del modelo construido | ISC | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT06 | Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones | ISC | 5.0 % | 10.0 % | n/d | n/d | n/d |
| ACT07 | Unificar modelo y adquisición en la base integrada | ISC | 10.0 % | 20.0 % | n/d | n/d | n/d |
| ACT08 | Preparar el paquete de implementación | ISC | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT09 | Aprobar las pruebas FAT/SAT y de integración | ISC | 96.7 % | 93.3 % | n/d | n/d | n/d |
| ACT10 | Administrar y actualizar los aplicativos EMS | DAS | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT11 | Validar el estimador de estado, el flujo de potencia y demás aplicaciones | DAS | 96.7 % | 100.0 % | n/d | n/d | n/d |
| ACT12 | Verificar la correspondencia de mímicos y modelo con la instalación física | ORIGIN | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT13 | Aceptar mímicos, alarmas y el uso operativo | ODC | 67.5 % | 70.0 % | n/d | n/d | n/d |
| ACT14 | Autorizar la liberación de la versión a producción | NEW_AUTHORITY | 28.3 % | 46.7 % | n/d | n/d | n/d |
| ACT15 | Habilitar o suspender la ventana de intervención en tiempo real | ODC | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT16 | Ejecutar el respaldo y la carga en producción | MCO | 80.0 % | 100.0 % | n/d | n/d | n/d |
| ACT17 | Mantener el registro técnico de configuración | ISC | 95.0 % | 100.0 % | n/d | n/d | n/d |
| ACT18 | Verificar el sistema después de la actualización y cerrar el cambio | DAS | 47.5 % | 70.0 % | n/d | n/d | n/d |
| ACT19 | Aprobar los criterios de reversión y su delegación | NEW_AUTHORITY | 55.0 % | 60.0 % | n/d | n/d | n/d |
| ACT20 | Ejecutar la reversión | MCO | 80.0 % | 100.0 % | n/d | n/d | n/d |

### Matriz RACI modal

Matrices completas por grupo (A, R, C, I por unidad, con frecuencia y celdas inestables) en `modal_raci.md` y `modal_raci.csv`. Resumen de la comparación celda a celda:

| Grupo | Celdas idénticas | Celdas A/R idénticas | A recuperada | Celdas inestables |
|---|---|---|---|---|
| especializados_f1 | 37.1 % | 80.0 % | 65.0 % | 36 de 140 |
| neutral_f1 | 33.6 % | 81.4 % | 70.0 % | 14 de 140 |

## 15. Limitaciones

- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de perspectivas es inducida por el prompt, no por conocimiento independiente.
- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad observada puede reflejar el marco institucional o la lectura del modelo.
- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede orientar la respuesta aunque no revele la asignación.
- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.
- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).
- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.
- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye la del servicio.
