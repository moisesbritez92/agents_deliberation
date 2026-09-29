# Informe del experimento: luna_order_reversed

## 1. Configuración experimental

- Etiqueta: `luna_order_reversed`; creada: 2026-09-28T11:35:41.705539+00:00
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

- Llamadas registradas (incluidos reintentos): 273; previstas sin reintentos: 250
- Corridas completas (con árbitro): 50 de 50
- Errores de API: 12
- JSON válido: 100.0 %; actividades completas: 100.0 %
- Control de contaminación del material enviado: {'OK': 273}. REFERENCE_RACI no se envió a ningún agente (el script de ejecución no lee `posthoc/`).

## 5. Tokens consumidos

- Entrada: 5,083,404 (de ellos en caché: 3,894,940)
- Salida: 1,135,828 (razonamiento: 428,699)

## 6. Coste aproximado

USD 0.3777 con precios configurados para `gpt-6-luna` de 0.1 / 0.5 / 0.01 USD por millón (entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.

## 7. Decisiones iniciales (fase 1, especializados)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:18; OTHER:1; NONE:1 | 80.0 % | 100.0 % | 0.569 |
| S01 | ACT04 | DAS:20 | 100.0 % | 65.0 % | -0.000 |
| S01 | ACT06 | MCO:12; ISC:4; DAS:4 | 53.3 % | 70.0 % | 1.371 |
| S01 | ACT09 | ISC:20 | 100.0 % | 75.0 % | -0.000 |
| S01 | ACT12 | MCO:16; DAS:3; ISC:1 | 60.0 % | 100.0 % | 0.884 |
| S02 | ACT02 | DT:17; DEL:2; NONE:1 | 70.0 % | 95.0 % | 0.748 |
| S02 | ACT04 | DAS:20 | 100.0 % | 15.0 % | -0.000 |
| S02 | ACT05 | DAS:20 | 100.0 % | 65.0 % | -0.000 |
| S02 | ACT11 | DAS:20 | 100.0 % | 30.0 % | -0.000 |
| S03 | ACT06 | ISC:9; DAS:6; MCO:5 | 26.7 % | 75.0 % | 1.539 |
| S03 | ACT07 | DAS:18; ISC:2 | 86.7 % | 80.0 % | 0.469 |
| S03 | ACT09 | ISC:20 | 100.0 % | 55.0 % | -0.000 |
| S03 | ACT13 | ODC:12; MCO:8 | 40.0 % | 100.0 % | 0.971 |
| S04 | ACT06 | DAS:20 | 100.0 % | 55.0 % | -0.000 |
| S04 | ACT11 | DAS:20 | 100.0 % | 35.0 % | -0.000 |
| S04 | ACT17 | DAS:11; ISC:9 | 70.0 % | 90.0 % | 0.993 |
| S04 | ACT18 | DAS:19; MCO:1 | 90.0 % | 85.0 % | 0.286 |
| S05 | ACT01 | DAS:19; OP:1 | 90.0 % | 50.0 % | 0.286 |
| S05 | ACT06 | DAS:15; MCO:5 | 56.7 % | 100.0 % | 0.811 |
| S05 | ACT09 | ISC:16; DAS:2; MCO:2 | 60.0 % | 100.0 % | 0.922 |
| S05 | ACT15 | ODC:20 | 100.0 % | 15.0 % | -0.000 |
| S06 | ACT03 | DAS:13; ISC:7 | 50.0 % | 100.0 % | 0.934 |
| S06 | ACT04 | DAS:20 | 100.0 % | 35.0 % | -0.000 |
| S06 | ACT05 | DAS:18; ISC:2 | 80.0 % | 85.0 % | 0.469 |
| S06 | ACT12 | MCO:18; DAS:1; DT:1 | 80.0 % | 70.0 % | 0.569 |
| S06 | ACT13 | ODC:15; MCO:4; ISC:1 | 56.7 % | 100.0 % | 0.992 |
| S07 | ACT10 | DAS:20 | 100.0 % | 0.0 % | -0.000 |
| S07 | ACT11 | DAS:20 | 100.0 % | 55.0 % | -0.000 |
| S07 | ACT14 | DAS:17; NEW_AUTHORITY:3 | 76.7 % | 95.0 % | 0.610 |
| S07 | ACT19 | DAS:13; NEW_AUTHORITY:7 | 43.3 % | 100.0 % | 0.934 |
| S08 | ACT08 | DAS:20 | 100.0 % | 35.0 % | -0.000 |
| S08 | ACT14 | DAS:18; NEW_AUTHORITY:2 | 80.0 % | 100.0 % | 0.469 |
| S08 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT16 | DAS:12; MCO:8 | 40.0 % | 100.0 % | 0.971 |
| S09 | ACT15 | ODC:20 | 100.0 % | 5.0 % | -0.000 |
| S09 | ACT18 | DAS:20 | 100.0 % | 95.0 % | -0.000 |
| S09 | ACT19 | NEW_AUTHORITY:14; DAS:6 | 53.3 % | 100.0 % | 0.881 |
| S09 | ACT20 | DAS:19; MCO:1 | 90.0 % | 95.0 % | 0.286 |
| S10 | ACT01 | DAS:14; ODC:6 | 46.7 % | 80.0 % | 0.881 |
| S10 | ACT14 | DAS:18; NEW_AUTHORITY:1; ODC:1 | 80.0 % | 100.0 % | 0.569 |
| S10 | ACT15 | ODC:20 | 100.0 % | 10.0 % | -0.000 |
| S10 | ACT16 | DAS:19; MCO:1 | 90.0 % | 85.0 % | 0.286 |
| S10 | ACT20 | DAS:20 | 100.0 % | 95.0 % | -0.000 |

Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):

| Escenario | DAS | ISC | MCO | ODC |
|---|---|---|---|---|
| S01 | 76.0 % | 84.0 % | 84.0 % | 84.0 % |
| S02 | 90.0 % | 95.0 % | 100.0 % | 100.0 % |
| S03 | 70.0 % | 75.0 % | 70.0 % | 70.0 % |
| S04 | 85.0 % | 95.0 % | 90.0 % | 100.0 % |
| S05 | 80.0 % | 85.0 % | 90.0 % | 85.0 % |
| S06 | 92.0 % | 64.0 % | 84.0 % | 88.0 % |
| S07 | 90.0 % | 95.0 % | 80.0 % | 75.0 % |
| S08 | 95.0 % | 85.0 % | 70.0 % | 100.0 % |
| S09 | 85.0 % | 85.0 % | 90.0 % | 85.0 % |
| S10 | 92.0 % | 80.0 % | 76.0 % | 76.0 % |

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
| S01 | 78.7 % | [0.707, 0.867] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 60.0 % | n/d |
| S02 | 92.5 % | [0.875, 0.975] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 85.0 % | n/d |
| S03 | 63.3 % | [0.542, 0.700] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 45.0 % | n/d |
| S04 | 90.0 % | [0.825, 0.975] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 80.0 % | n/d |
| S05 | 76.7 % | [0.692, 0.842] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 55.0 % | n/d |
| S06 | 73.3 % | [0.640, 0.833] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 48.0 % | n/d |
| S07 | 80.0 % | [0.717, 0.867] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 65.0 % | n/d |
| S08 | 80.0 % | [0.742, 0.850] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 65.0 % | n/d |
| S09 | 85.8 % | [0.842, 0.875] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 75.0 % | n/d |
| S10 | 83.3 % | [0.787, 0.880] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 68.0 % | n/d |

Global: acuerdo 80.4 % → n/d; CONVERGENCE_DELTA = n/d (IC95 bootstrap sobre corridas [n/d, n/d]). Mayor consenso no implica mayor corrección.

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

- AMBIGUITY_RATE antes: 69.7 %; después: n/d
- Árbitro, veredicto AMBIGUOUS: n/d
- PROPOSED_NEW_AUTHORITY como A: 3.0 % de las decisiones de agentes

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

Media por actividad: 0.435 bits antes y n/d bits después. Entropía baja indica asignación estable; alta, sensible a la interpretación. No es una medida de corrección.

## 12. Cambios de posición

POSITION_CHANGE_RATE global: n/d.

| Agente | Escenario | n | Cambio de A | MAINTAIN | MODIFY | AMBIGUOUS | Declaración incoherente |
|---|---|---|---|---|---|---|---|

Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).

| Agente | P propia | P neutral | Diferencia | n |
|---|---|---|---|---|
| DAS | 65.6 % | 60.5 % | 0.051 | 215 |
| ISC | 14.9 % | 9.3 % | 0.056 | 215 |
| MCO | 13.5 % | 10.2 % | 0.033 | 215 |
| ODC | 14.9 % | 13.5 % | 0.014 | 215 |

## 13. Evidencia más utilizada

- EVIDENCE_VALIDITY_RATE: 100.0 % de 5731 citas
- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): 0.0 %
- A sin evidencia institucional válida: 0.0 %
- Violación de jerarquía (DOCUMENTADO con fuente no institucional): 0.9 %
- Cita textual verificada en la fuente: 99.7 % de 5731; en afirmaciones DOCUMENTADO: 99.7 % de 693
- Proporción de citas INFERIDO: 53.2 %
La verificación textual prueba que el fragmento existe en la fuente citada, no que nombre la actividad; la pertinencia se audita con citation_audit.py.

| source_id | kind | total | phase1 | phase2 |
|---|---|---|---|---|
| DAS_2_4 | institucional | 501 | 501 | 0 |
| DAS1_2_2 | institucional | 483 | 483 | 0 |
| NIST_CM_01 | externa | 439 | 439 | 0 |
| MCO_2_8 | institucional | 298 | 298 | 0 |
| ODC_2_1 | institucional | 291 | 291 | 0 |
| DAS2_2_2 | institucional | 237 | 237 | 0 |
| DAS_2_1 | institucional | 234 | 234 | 0 |
| IEC61970_456_01 | externa | 226 | 226 | 0 |
| MCO_2_6 | institucional | 226 | 226 | 0 |
| NIST_CM_02 | externa | 218 | 218 | 0 |
| NIST_OT_01 | externa | 215 | 215 | 0 |
| ENISA_CHG_02 | externa | 161 | 161 | 0 |
| DAS2_2_1 | institucional | 154 | 154 | 0 |
| ODC_2_6 | institucional | 153 | 153 | 0 |
| ERCOT_02 | externa | 144 | 144 | 0 |
| DAS_2_2 | institucional | 118 | 118 | 0 |
| ISC2_2_4 | institucional | 102 | 102 | 0 |
| DOS_2_7 | institucional | 97 | 97 | 0 |
| CTX_MIMICO | externa | 84 | 84 | 0 |
| ISC2_2_3 | institucional | 83 | 83 | 0 |

## 14. Comparación post hoc con REFERENCE_RACI

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la correspondencia de columnas indicada en el README (Origen, GT*, AC).

| activity_id | activity | REFERENCE_A | match_individual_especializados_f1 | match_neutral_f1 | match_post_debate_f2 | match_control_sin_debate_f2c | match_arbitro_f3 |
|---|---|---|---|---|---|---|---|
| ACT01 | Definir el requisito y el alcance del cambio | DAS | 82.5 % | 90.0 % | n/d | n/d | n/d |
| ACT02 | Certificar los datos de la instalación (configuración física y parámetros) | ORIGIN | 95.0 % | 90.0 % | n/d | n/d | n/d |
| ACT03 | Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación) | DAS | 65.0 % | 80.0 % | n/d | n/d | n/d |
| ACT04 | Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros) | DAS | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT05 | Revisar la calidad topológica y de nomenclatura del modelo construido | ISC | 5.0 % | 0.0 % | n/d | n/d | n/d |
| ACT06 | Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones | ISC | 16.2 % | 15.0 % | n/d | n/d | n/d |
| ACT07 | Unificar modelo y adquisición en la base integrada | ISC | 10.0 % | 0.0 % | n/d | n/d | n/d |
| ACT08 | Preparar el paquete de implementación | ISC | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT09 | Aprobar las pruebas FAT/SAT y de integración | ISC | 93.3 % | 100.0 % | n/d | n/d | n/d |
| ACT10 | Administrar y actualizar los aplicativos EMS | DAS | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT11 | Validar el estimador de estado, el flujo de potencia y demás aplicaciones | DAS | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT12 | Verificar la correspondencia de mímicos y modelo con la instalación física | ORIGIN | 2.5 % | 0.0 % | n/d | n/d | n/d |
| ACT13 | Aceptar mímicos, alarmas y el uso operativo | ODC | 67.5 % | 80.0 % | n/d | n/d | n/d |
| ACT14 | Autorizar la liberación de la versión a producción | NEW_AUTHORITY | 10.0 % | 13.3 % | n/d | n/d | n/d |
| ACT15 | Habilitar o suspender la ventana de intervención en tiempo real | ODC | 100.0 % | 100.0 % | n/d | n/d | n/d |
| ACT16 | Ejecutar el respaldo y la carga en producción | MCO | 22.5 % | 0.0 % | n/d | n/d | n/d |
| ACT17 | Mantener el registro técnico de configuración | ISC | 45.0 % | 20.0 % | n/d | n/d | n/d |
| ACT18 | Verificar el sistema después de la actualización y cerrar el cambio | DAS | 97.5 % | 100.0 % | n/d | n/d | n/d |
| ACT19 | Aprobar los criterios de reversión y su delegación | NEW_AUTHORITY | 52.5 % | 30.0 % | n/d | n/d | n/d |
| ACT20 | Ejecutar la reversión | MCO | 2.5 % | 0.0 % | n/d | n/d | n/d |

### Matriz RACI modal

Matrices completas por grupo (A, R, C, I por unidad, con frecuencia y celdas inestables) en `modal_raci.md` y `modal_raci.csv`. Resumen de la comparación celda a celda:

| Grupo | Celdas idénticas | Celdas A/R idénticas | A recuperada | Celdas inestables |
|---|---|---|---|---|
| especializados_f1 | 35.0 % | 78.6 % | 60.0 % | 37 de 140 |
| neutral_f1 | 37.1 % | 77.1 % | 50.0 % | 21 de 140 |

## 15. Limitaciones

- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de perspectivas es inducida por el prompt, no por conocimiento independiente.
- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad observada puede reflejar el marco institucional o la lectura del modelo.
- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede orientar la respuesta aunque no revele la asignación.
- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.
- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).
- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.
- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye la del servicio.
