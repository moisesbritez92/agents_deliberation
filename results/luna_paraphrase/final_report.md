# Informe del experimento: luna_paraphrase

## 1. Configuración experimental

- Etiqueta: `luna_paraphrase`; creada: 2026-09-29T11:22:03.348534+00:00
- Escenarios: 10 (S01, S02, S03, S04, S05, S06, S07, S08, S09, S10); repeticiones: 3
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

- Llamadas registradas (incluidos reintentos): 420; previstas sin reintentos: 420
- Corridas completas (con árbitro): 30 de 30
- Errores de API: 0
- JSON válido: 100.0 %; actividades completas: 100.0 %
- Control de contaminación del material enviado: {'OK': 420}. REFERENCE_RACI no se envió a ningún agente (el script de ejecución no lee `posthoc/`).

## 5. Tokens consumidos

- Entrada: 10,605,067 (de ellos en caché: 1,038,806)
- Salida: 1,779,183 (razonamiento: 623,716)

## 6. Coste aproximado

USD 1.0479 con precios configurados para `gpt-6-luna` de 0.1 / 0.5 / 0.01 USD por millón (entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.

## 7. Decisiones iniciales (fase 1, especializados)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:11; NONE:1 | 83.3 % | 100.0 % | 0.414 |
| S01 | ACT04 | DAS:12 | 100.0 % | 50.0 % | -0.000 |
| S01 | ACT06 | MCO:10; ISC:1; DAS:1 | 66.7 % | 83.3 % | 0.817 |
| S01 | ACT09 | ISC:12 | 100.0 % | 66.7 % | -0.000 |
| S01 | ACT12 | DAS:5; MCO:4; ISC:3 | 27.8 % | 100.0 % | 1.555 |
| S02 | ACT02 | DT:12 | 100.0 % | 100.0 % | -0.000 |
| S02 | ACT04 | DAS:12 | 100.0 % | 16.7 % | -0.000 |
| S02 | ACT05 | DAS:12 | 100.0 % | 66.7 % | -0.000 |
| S02 | ACT11 | DAS:12 | 100.0 % | 41.7 % | -0.000 |
| S03 | ACT06 | DAS:7; ISC:3; MCO:1; TX_REG:1 | 27.8 % | 83.3 % | 1.551 |
| S03 | ACT07 | DAS:8; ISC:4 | 44.4 % | 100.0 % | 0.918 |
| S03 | ACT09 | ISC:12 | 100.0 % | 91.7 % | -0.000 |
| S03 | ACT13 | ODC:11; MCO:1 | 83.3 % | 100.0 % | 0.414 |
| S04 | ACT06 | DAS:12 | 100.0 % | 58.3 % | -0.000 |
| S04 | ACT11 | DAS:12 | 100.0 % | 25.0 % | -0.000 |
| S04 | ACT17 | DAS:8; ISC:4 | 44.4 % | 58.3 % | 0.918 |
| S04 | ACT18 | DAS:10; MCO:1; ODC:1 | 66.7 % | 91.7 % | 0.817 |
| S05 | ACT01 | DAS:9; ODC:3 | 61.1 % | 66.7 % | 0.811 |
| S05 | ACT06 | DAS:9; MCO:3 | 61.1 % | 91.7 % | 0.811 |
| S05 | ACT09 | ISC:10; MCO:1; DAS:1 | 66.7 % | 91.7 % | 0.817 |
| S05 | ACT15 | ODC:12 | 100.0 % | 0.0 % | -0.000 |
| S06 | ACT03 | DAS:10; DOS:1; ISC:1 | 66.7 % | 100.0 % | 0.817 |
| S06 | ACT04 | DAS:12 | 100.0 % | 25.0 % | -0.000 |
| S06 | ACT05 | DAS:10; DOS:2 | 66.7 % | 91.7 % | 0.650 |
| S06 | ACT12 | MCO:10; DAS:1; DT:1 | 66.7 % | 100.0 % | 0.817 |
| S06 | ACT13 | ODC:12 | 100.0 % | 91.7 % | -0.000 |
| S07 | ACT10 | DAS:12 | 100.0 % | 0.0 % | -0.000 |
| S07 | ACT11 | DAS:12 | 100.0 % | 58.3 % | -0.000 |
| S07 | ACT14 | DAS:9; NEW_AUTHORITY:3 | 61.1 % | 83.3 % | 0.811 |
| S07 | ACT19 | DAS:8; NEW_AUTHORITY:4 | 66.7 % | 83.3 % | 0.918 |
| S08 | ACT08 | DAS:12 | 100.0 % | 25.0 % | -0.000 |
| S08 | ACT14 | DAS:6; NEW_AUTHORITY:6 | 44.4 % | 100.0 % | 1.000 |
| S08 | ACT15 | ODC:12 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT16 | DAS:7; MCO:5 | 38.9 % | 83.3 % | 0.980 |
| S09 | ACT15 | ODC:12 | 100.0 % | 8.3 % | -0.000 |
| S09 | ACT18 | DAS:11; MCO:1 | 83.3 % | 91.7 % | 0.414 |
| S09 | ACT19 | NEW_AUTHORITY:11; DAS:1 | 83.3 % | 91.7 % | 0.414 |
| S09 | ACT20 | DAS:11; MCO:1 | 83.3 % | 91.7 % | 0.414 |
| S10 | ACT01 | DAS:6; ODC:6 | 44.4 % | 91.7 % | 1.000 |
| S10 | ACT14 | DAS:10; NEW_AUTHORITY:2 | 66.7 % | 100.0 % | 0.650 |
| S10 | ACT15 | ODC:12 | 100.0 % | 16.7 % | -0.000 |
| S10 | ACT16 | DAS:12 | 100.0 % | 66.7 % | -0.000 |
| S10 | ACT20 | DAS:12 | 100.0 % | 83.3 % | -0.000 |

Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):

| Escenario | DAS | ISC | MCO | ODC |
|---|---|---|---|---|
| S01 | 86.7 % | 73.3 % | 73.3 % | 60.0 % |
| S02 | 91.7 % | 91.7 % | 91.7 % | 91.7 % |
| S03 | 66.7 % | 75.0 % | 33.3 % | 58.3 % |
| S04 | 100.0 % | 75.0 % | 83.3 % | 91.7 % |
| S05 | 75.0 % | 66.7 % | 91.7 % | 83.3 % |
| S06 | 93.3 % | 86.7 % | 80.0 % | 80.0 % |
| S07 | 66.7 % | 58.3 % | 75.0 % | 58.3 % |
| S08 | 75.0 % | 83.3 % | 75.0 % | 91.7 % |
| S09 | 91.7 % | 75.0 % | 91.7 % | 83.3 % |
| S10 | 80.0 % | 86.7 % | 80.0 % | 73.3 % |

## 8. Decisiones posteriores al debate (fase 2)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:11; NONE:1 | 83.3 % | 100.0 % | 0.414 |
| S01 | ACT04 | DAS:12 | 100.0 % | 41.7 % | -0.000 |
| S01 | ACT06 | MCO:12 | 100.0 % | 100.0 % | -0.000 |
| S01 | ACT09 | ISC:12 | 100.0 % | 91.7 % | -0.000 |
| S01 | ACT12 | DAS:4; MCO:4; ISC:4 | 66.7 % | 100.0 % | 1.585 |
| S02 | ACT02 | DT:12 | 100.0 % | 100.0 % | -0.000 |
| S02 | ACT04 | DAS:12 | 100.0 % | 8.3 % | -0.000 |
| S02 | ACT05 | DAS:12 | 100.0 % | 100.0 % | -0.000 |
| S02 | ACT11 | DAS:12 | 100.0 % | 83.3 % | -0.000 |
| S03 | ACT06 | ISC:6; MCO:3; DAS:3 | 66.7 % | 100.0 % | 1.500 |
| S03 | ACT07 | ISC:8; DAS:4 | 66.7 % | 100.0 % | 0.918 |
| S03 | ACT09 | ISC:12 | 100.0 % | 100.0 % | -0.000 |
| S03 | ACT13 | ODC:12 | 100.0 % | 100.0 % | -0.000 |
| S04 | ACT06 | DAS:12 | 100.0 % | 50.0 % | -0.000 |
| S04 | ACT11 | DAS:12 | 100.0 % | 41.7 % | -0.000 |
| S04 | ACT17 | DAS:8; ISC:4 | 66.7 % | 100.0 % | 0.918 |
| S04 | ACT18 | DAS:12 | 100.0 % | 83.3 % | -0.000 |
| S05 | ACT01 | DAS:10; ODC:2 | 66.7 % | 100.0 % | 0.650 |
| S05 | ACT06 | DAS:10; MCO:2 | 77.8 % | 100.0 % | 0.650 |
| S05 | ACT09 | ISC:11; MCO:1 | 83.3 % | 100.0 % | 0.414 |
| S05 | ACT15 | ODC:12 | 100.0 % | 0.0 % | -0.000 |
| S06 | ACT03 | DAS:12 | 100.0 % | 100.0 % | -0.000 |
| S06 | ACT04 | DAS:12 | 100.0 % | 16.7 % | -0.000 |
| S06 | ACT05 | DAS:11; DOS:1 | 83.3 % | 100.0 % | 0.414 |
| S06 | ACT12 | MCO:12 | 100.0 % | 100.0 % | -0.000 |
| S06 | ACT13 | ODC:12 | 100.0 % | 100.0 % | -0.000 |
| S07 | ACT10 | DAS:12 | 100.0 % | 0.0 % | -0.000 |
| S07 | ACT11 | DAS:12 | 100.0 % | 100.0 % | -0.000 |
| S07 | ACT14 | DAS:7; NEW_AUTHORITY:5 | 38.9 % | 100.0 % | 0.980 |
| S07 | ACT19 | NEW_AUTHORITY:7; DAS:5 | 61.1 % | 100.0 % | 0.980 |
| S08 | ACT08 | DAS:12 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT14 | NEW_AUTHORITY:8; DAS:4 | 66.7 % | 100.0 % | 0.918 |
| S08 | ACT15 | ODC:12 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT16 | DAS:7; MCO:5 | 38.9 % | 100.0 % | 0.980 |
| S09 | ACT15 | ODC:12 | 100.0 % | 16.7 % | -0.000 |
| S09 | ACT18 | DAS:12 | 100.0 % | 100.0 % | -0.000 |
| S09 | ACT19 | NEW_AUTHORITY:12 | 100.0 % | 100.0 % | -0.000 |
| S09 | ACT20 | DAS:12 | 100.0 % | 100.0 % | -0.000 |
| S10 | ACT01 | DAS:6; ODC:6 | 44.4 % | 100.0 % | 1.000 |
| S10 | ACT14 | DAS:9; NEW_AUTHORITY:3 | 83.3 % | 100.0 % | 0.811 |
| S10 | ACT15 | ODC:12 | 100.0 % | 8.3 % | -0.000 |
| S10 | ACT16 | DAS:12 | 100.0 % | 100.0 % | -0.000 |
| S10 | ACT20 | DAS:12 | 100.0 % | 100.0 % | -0.000 |

## 9. Consenso

| Escenario | Acuerdo antes | IC95 antes | Acuerdo después | IC95 después | CONVERGENCE_DELTA | IC95 delta | Consenso estricto antes | Consenso estricto después |
|---|---|---|---|---|---|---|---|---|
| S01 | 75.6 % | [0.733, 0.767] | 90.0 % | [0.800, 1.000] | 0.144 | [0.033, 0.233] | 60.0 % | 80.0 % |
| S02 | 100.0 % | [1.000, 1.000] | 100.0 % | [1.000, 1.000] | 0.000 | [0.000, 0.000] | 100.0 % | 100.0 % |
| S03 | 63.9 % | [0.500, 0.750] | 83.3 % | [0.750, 0.875] | 0.194 | [0.000, 0.375] | 41.7 % | 66.7 % |
| S04 | 77.8 % | [0.708, 0.875] | 91.7 % | [0.875, 1.000] | 0.139 | [0.000, 0.250] | 58.3 % | 83.3 % |
| S05 | 72.2 % | [0.625, 0.833] | 81.9 % | [0.750, 0.875] | 0.097 | [0.000, 0.167] | 50.0 % | 66.7 % |
| S06 | 80.0 % | [0.700, 0.900] | 96.7 % | [0.900, 1.000] | 0.167 | [0.100, 0.200] | 60.0 % | 93.3 % |
| S07 | 81.9 % | [0.708, 1.000] | 75.0 % | [0.667, 0.833] | -0.069 | [-0.250, 0.125] | 66.7 % | 58.3 % |
| S08 | 70.8 % | [0.667, 0.750] | 76.4 % | [0.708, 0.833] | 0.056 | [0.000, 0.125] | 50.0 % | 58.3 % |
| S09 | 87.5 % | [0.750, 1.000] | 100.0 % | [1.000, 1.000] | 0.125 | [0.000, 0.250] | 75.0 % | 100.0 % |
| S10 | 82.2 % | [0.767, 0.900] | 85.6 % | [0.767, 0.900] | 0.033 | [0.000, 0.100] | 66.7 % | 73.3 % |

Global: acuerdo 79.2 % → 88.1 %; CONVERGENCE_DELTA = 0.089 (IC95 bootstrap sobre corridas [0.046, 0.131]). Mayor consenso no implica mayor corrección.

**Brazo control (fase 2c):** los mismos agentes reconsideran su decisión inicial sin ver propuestas ajenas. DELIBERATION_EFFECT = CONVERGENCE_DELTA − CONVERGENCE_DELTA_CONTROL estima la convergencia atribuible a la información de los demás, descontando la que produce el solo hecho de responder dos veces.

- Acuerdo en el control: 80.6 %; CONVERGENCE_DELTA_CONTROL = 0.014 (IC95 [-0.016, 0.044])
- DELIBERATION_EFFECT = 0.074 (IC95 [0.029, 0.124])
- Cambio de A en el control: 6.2 % frente a 10.5 % con deliberación

| Escenario | Acuerdo control | Delta control | Efecto deliberación | IC95 efecto |
|---|---|---|---|---|
| S01 | 82.2 % | 0.067 | 0.078 | [-0.033, 0.167] |
| S02 | 95.8 % | -0.042 | 0.042 | [0.000, 0.125] |
| S03 | 65.3 % | 0.014 | 0.181 | [0.000, 0.375] |
| S04 | 86.1 % | 0.083 | 0.056 | [0.000, 0.167] |
| S05 | 69.4 % | -0.028 | 0.125 | [0.000, 0.250] |
| S06 | 83.3 % | 0.033 | 0.133 | [0.000, 0.200] |
| S07 | 87.5 % | 0.056 | -0.125 | [-0.250, -0.042] |
| S08 | 75.0 % | 0.042 | 0.014 | [-0.125, 0.125] |
| S09 | 79.2 % | -0.083 | 0.208 | [0.000, 0.375] |
| S10 | 82.2 % | 0.000 | 0.033 | [-0.033, 0.100] |

## 10. Ambigüedad

- AMBIGUITY_RATE antes: 69.0 %; después: 77.7 %
- Árbitro, veredicto AMBIGUOUS: 80.6 %
- PROPOSED_NEW_AUTHORITY como A: 5.3 % de las decisiones de agentes

| Escenario | Actividad | Árbitro: consenso | Árbitro: A | Árbitro AMBIGUOUS |
|---|---|---|---|---|
| S01 | ACT02 | FULL:2; MAJORITY:1 | DT:2; NONE:1 | 100.0 % |
| S01 | ACT04 | FULL:3 | DAS:3 | 0.0 % |
| S01 | ACT06 | FULL:3 | MCO:3 | 100.0 % |
| S01 | ACT09 | FULL:3 | ISC:3 | 100.0 % |
| S01 | ACT12 | MAJORITY:2; FULL:1 | DAS:1; ISC:1; MCO:1 | 100.0 % |
| S02 | ACT02 | FULL:3 | DT:3 | 100.0 % |
| S02 | ACT04 | FULL:3 | DAS:3 | 0.0 % |
| S02 | ACT05 | FULL:3 | DAS:3 | 100.0 % |
| S02 | ACT11 | FULL:2; NONE:1 | DAS:3 | 100.0 % |
| S03 | ACT06 | MAJORITY:3 | MCO:1; DAS:1; ISC:1 | 100.0 % |
| S03 | ACT07 | MAJORITY:2; FULL:1 | ISC:2; DAS:1 | 100.0 % |
| S03 | ACT09 | FULL:3 | ISC:3 | 100.0 % |
| S03 | ACT13 | FULL:3 | ODC:3 | 100.0 % |
| S04 | ACT06 | FULL:3 | DAS:3 | 33.3 % |
| S04 | ACT11 | FULL:2; MAJORITY:1 | DAS:3 | 66.7 % |
| S04 | ACT17 | MAJORITY:2; FULL:1 | DAS:2; ISC:1 | 100.0 % |
| S04 | ACT18 | FULL:3 | DAS:3 | 66.7 % |
| S05 | ACT01 | MAJORITY:2; FULL:1 | DAS:3 | 100.0 % |
| S05 | ACT06 | FULL:2; NONE:1 | DAS:2; MCO:1 | 100.0 % |
| S05 | ACT09 | FULL:2; MAJORITY:1 | ISC:3 | 100.0 % |
| S05 | ACT15 | FULL:3 | ODC:3 | 0.0 % |
| S06 | ACT03 | FULL:3 | DAS:3 | 100.0 % |
| S06 | ACT04 | FULL:3 | DAS:3 | 66.7 % |
| S06 | ACT05 | MAJORITY:2; FULL:1 | DAS:3 | 100.0 % |
| S06 | ACT12 | FULL:3 | MCO:3 | 100.0 % |
| S06 | ACT13 | FULL:3 | ODC:3 | 100.0 % |
| S07 | ACT10 | FULL:3 | DAS:3 | 0.0 % |
| S07 | ACT11 | FULL:2; MAJORITY:1 | DAS:3 | 100.0 % |
| S07 | ACT14 | NONE:2; MAJORITY:1 | DAS:2; NEW_AUTHORITY:1 | 100.0 % |
| S07 | ACT19 | MAJORITY:1; NONE:1; FULL:1 | NEW_AUTHORITY:2; DAS:1 | 100.0 % |
| S08 | ACT08 | FULL:3 | DAS:3 | 0.0 % |
| S08 | ACT14 | MAJORITY:2; FULL:1 | NONE:1; NEW_AUTHORITY:1; DAS:1 | 100.0 % |
| S08 | ACT15 | FULL:3 | ODC:3 | 0.0 % |
| S08 | ACT16 | NONE:2; MAJORITY:1 | MCO:2; DAS:1 | 100.0 % |
| S09 | ACT15 | FULL:3 | ODC:3 | 100.0 % |
| S09 | ACT18 | FULL:3 | DAS:3 | 100.0 % |
| S09 | ACT19 | FULL:3 | NEW_AUTHORITY:3 | 100.0 % |
| S09 | ACT20 | FULL:3 | DAS:3 | 100.0 % |
| S10 | ACT01 | MAJORITY:2; NONE:1 | DAS:2; ODC:1 | 100.0 % |
| S10 | ACT14 | FULL:2; MAJORITY:1 | DAS:2; NEW_AUTHORITY:1 | 100.0 % |
| S10 | ACT15 | FULL:3 | ODC:3 | 33.3 % |
| S10 | ACT16 | FULL:3 | DAS:3 | 100.0 % |
| S10 | ACT20 | FULL:3 | DAS:3 | 100.0 % |

## 11. Entropía de la autoridad (A)

Media por actividad: 0.436 bits antes y 0.305 bits después. Entropía baja indica asignación estable; alta, sensible a la interpretación. No es una medida de corrección.

## 12. Cambios de posición

POSITION_CHANGE_RATE global: 10.5 %.

| Agente | Escenario | n | Cambio de A | MAINTAIN | MODIFY | AMBIGUOUS | Declaración incoherente |
|---|---|---|---|---|---|---|---|
| DAS | S01 | 15 | 6.7 % | 7 | 0 | 8 | 0.0 % |
| DAS | S02 | 12 | 0.0 % | 4 | 0 | 8 | 0.0 % |
| DAS | S03 | 12 | 25.0 % | 2 | 3 | 7 | 0.0 % |
| DAS | S04 | 12 | 0.0 % | 5 | 1 | 6 | 0.0 % |
| DAS | S05 | 12 | 16.7 % | 3 | 1 | 8 | 0.0 % |
| DAS | S06 | 15 | 6.7 % | 8 | 0 | 7 | 0.0 % |
| DAS | S07 | 12 | 0.0 % | 3 | 1 | 8 | 0.0 % |
| DAS | S08 | 12 | 25.0 % | 6 | 0 | 6 | 0.0 % |
| DAS | S09 | 12 | 0.0 % | 3 | 0 | 9 | 0.0 % |
| DAS | S10 | 15 | 6.7 % | 11 | 0 | 4 | 0.0 % |
| ISC | S01 | 15 | 0.0 % | 4 | 0 | 11 | 0.0 % |
| ISC | S02 | 12 | 0.0 % | 5 | 1 | 6 | 0.0 % |
| ISC | S03 | 12 | 25.0 % | 6 | 2 | 4 | 0.0 % |
| ISC | S04 | 12 | 16.7 % | 7 | 3 | 2 | 0.0 % |
| ISC | S05 | 12 | 8.3 % | 5 | 0 | 7 | 0.0 % |
| ISC | S06 | 15 | 6.7 % | 12 | 3 | 0 | 0.0 % |
| ISC | S07 | 12 | 0.0 % | 5 | 1 | 6 | 0.0 % |
| ISC | S08 | 12 | 0.0 % | 8 | 0 | 4 | 0.0 % |
| ISC | S09 | 12 | 16.7 % | 3 | 2 | 7 | 0.0 % |
| ISC | S10 | 15 | 13.3 % | 11 | 1 | 3 | 0.0 % |
| MCO | S01 | 15 | 13.3 % | 4 | 2 | 9 | 0.0 % |
| MCO | S02 | 12 | 0.0 % | 2 | 0 | 10 | 0.0 % |
| MCO | S03 | 12 | 16.7 % | 3 | 2 | 7 | 0.0 % |
| MCO | S04 | 12 | 0.0 % | 2 | 0 | 10 | 0.0 % |
| MCO | S05 | 12 | 0.0 % | 4 | 0 | 8 | 0.0 % |
| MCO | S06 | 15 | 13.3 % | 5 | 2 | 8 | 0.0 % |
| MCO | S07 | 12 | 25.0 % | 6 | 4 | 2 | 0.0 % |
| MCO | S08 | 12 | 8.3 % | 8 | 0 | 4 | 0.0 % |
| MCO | S09 | 12 | 0.0 % | 9 | 0 | 3 | 0.0 % |
| MCO | S10 | 15 | 6.7 % | 6 | 1 | 8 | 0.0 % |
| ODC | S01 | 15 | 40.0 % | 1 | 3 | 11 | 0.0 % |
| ODC | S02 | 12 | 0.0 % | 6 | 0 | 6 | 0.0 % |
| ODC | S03 | 12 | 33.3 % | 8 | 3 | 1 | 0.0 % |
| ODC | S04 | 12 | 16.7 % | 6 | 1 | 5 | 0.0 % |
| ODC | S05 | 12 | 16.7 % | 5 | 1 | 6 | 0.0 % |
| ODC | S06 | 15 | 6.7 % | 4 | 0 | 11 | 0.0 % |
| ODC | S07 | 12 | 33.3 % | 4 | 5 | 3 | 0.0 % |
| ODC | S08 | 12 | 0.0 % | 6 | 0 | 6 | 0.0 % |
| ODC | S09 | 12 | 8.3 % | 8 | 0 | 4 | 0.0 % |
| ODC | S10 | 15 | 6.7 % | 7 | 1 | 7 | 0.0 % |

Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).

| Agente | P propia | P neutral | Diferencia | n |
|---|---|---|---|---|
| DAS | 65.1 % | 58.1 % | 0.070 | 129 |
| ISC | 11.6 % | 7.8 % | 0.039 | 129 |
| MCO | 8.5 % | 6.2 % | 0.023 | 129 |
| ODC | 17.1 % | 14.0 % | 0.031 | 129 |

## 13. Evidencia más utilizada

- EVIDENCE_VALIDITY_RATE: 100.0 % de 9266 citas
- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): 0.0 %
- A sin evidencia institucional válida: 0.0 %
- Violación de jerarquía (DOCUMENTADO con fuente no institucional): 0.4 %
- Cita textual verificada en la fuente: 99.7 % de 8827; en afirmaciones DOCUMENTADO: 99.7 % de 1013
- Proporción de citas INFERIDO: 56.4 %
La verificación textual prueba que el fragmento existe en la fuente citada, no que nombre la actividad; la pertinencia se audita con citation_audit.py.

| source_id | kind | total | phase1 | phase2 |
|---|---|---|---|---|
| DAS_2_4 | institucional | 886 | 313 | 265 |
| NIST_CM_01 | externa | 644 | 233 | 213 |
| DAS1_2_2 | institucional | 627 | 205 | 210 |
| ODC_2_1 | institucional | 594 | 197 | 187 |
| DAS2_2_1 | institucional | 468 | 155 | 148 |
| MCO_2_6 | institucional | 418 | 146 | 125 |
| NIST_OT_01 | externa | 387 | 139 | 131 |
| DAS2_2_2 | institucional | 352 | 119 | 117 |
| MCO_2_8 | institucional | 323 | 101 | 103 |
| IEC61970_456_01 | externa | 320 | 121 | 105 |
| NIST_CM_02 | externa | 277 | 107 | 79 |
| DAS_2_1 | institucional | 273 | 95 | 86 |
| ODC_2_6 | institucional | 261 | 92 | 75 |
| ENISA_CHG_02 | externa | 228 | 85 | 68 |
| ISC2_2_4 | institucional | 197 | 63 | 58 |
| ERCOT_02 | externa | 188 | 74 | 47 |
| DEL_2_5 | institucional | 168 | 58 | 51 |
| DOS_2_7 | institucional | 162 | 66 | 38 |
| DAS1_2_1 | institucional | 152 | 58 | 42 |
| ISC2_2_3 | institucional | 146 | 52 | 41 |

## 14. Comparación post hoc con REFERENCE_RACI

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la correspondencia de columnas indicada en el README (Origen, GT*, AC).

| activity_id | activity | REFERENCE_A | match_individual_especializados_f1 | match_neutral_f1 | match_post_debate_f2 | match_control_sin_debate_f2c | match_arbitro_f3 |
|---|---|---|---|---|---|---|---|
| ACT01 | Definir el requisito y el alcance del cambio | DAS | 62.5 % | 66.7 % | 66.7 % | 62.5 % | 83.3 % |
| ACT02 | Certificar los datos de la instalación (configuración física y parámetros) | ORIGIN | 95.8 % | 100.0 % | 95.8 % | 100.0 % | 83.3 % |
| ACT03 | Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación) | DAS | 83.3 % | 100.0 % | 100.0 % | 83.3 % | 100.0 % |
| ACT04 | Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros) | DAS | 100.0 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT05 | Revisar la calidad topológica y de nomenclatura del modelo construido | ISC | 0.0 % | 0.0 % | 0.0 % | 0.0 % | 0.0 % |
| ACT06 | Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones | ISC | 8.3 % | 8.3 % | 12.5 % | 10.4 % | 8.3 % |
| ACT07 | Unificar modelo y adquisición en la base integrada | ISC | 33.3 % | 0.0 % | 66.7 % | 50.0 % | 66.7 % |
| ACT08 | Preparar el paquete de implementación | ISC | 0.0 % | 0.0 % | 0.0 % | 0.0 % | 0.0 % |
| ACT09 | Aprobar las pruebas FAT/SAT y de integración | ISC | 94.4 % | 100.0 % | 97.2 % | 91.7 % | 100.0 % |
| ACT10 | Administrar y actualizar los aplicativos EMS | DAS | 100.0 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT11 | Validar el estimador de estado, el flujo de potencia y demás aplicaciones | DAS | 100.0 % | 100.0 % | 100.0 % | 97.2 % | 100.0 % |
| ACT12 | Verificar la correspondencia de mímicos y modelo con la instalación física | ORIGIN | 4.2 % | 16.7 % | 0.0 % | 4.2 % | 0.0 % |
| ACT13 | Aceptar mímicos, alarmas y el uso operativo | ODC | 95.8 % | 66.7 % | 100.0 % | 95.8 % | 100.0 % |
| ACT14 | Autorizar la liberación de la versión a producción | NEW_AUTHORITY | 30.6 % | 55.6 % | 44.4 % | 22.2 % | 33.3 % |
| ACT15 | Habilitar o suspender la ventana de intervención en tiempo real | ODC | 100.0 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT16 | Ejecutar el respaldo y la carga en producción | MCO | 20.8 % | 0.0 % | 20.8 % | 29.2 % | 33.3 % |
| ACT17 | Mantener el registro técnico de configuración | ISC | 33.3 % | 0.0 % | 33.3 % | 33.3 % | 33.3 % |
| ACT18 | Verificar el sistema después de la actualización y cerrar el cambio | DAS | 87.5 % | 100.0 % | 100.0 % | 95.8 % | 100.0 % |
| ACT19 | Aprobar los criterios de reversión y su delegación | NEW_AUTHORITY | 62.5 % | 83.3 % | 79.2 % | 41.7 % | 83.3 % |
| ACT20 | Ejecutar la reversión | MCO | 4.2 % | 0.0 % | 0.0 % | 8.3 % | 0.0 % |

### Matriz RACI modal

Matrices completas por grupo (A, R, C, I por unidad, con frecuencia y celdas inestables) en `modal_raci.md` y `modal_raci.csv`. Resumen de la comparación celda a celda:

| Grupo | Celdas idénticas | Celdas A/R idénticas | A recuperada | Celdas inestables |
|---|---|---|---|---|
| especializados_f1 | 33.6 % | 77.1 % | 60.0 % | 41 de 140 |
| neutral_f1 | 36.4 % | 77.1 % | 60.0 % | 30 de 140 |
| deliberacion_f2 | 38.6 % | 78.6 % | 65.0 % | 22 de 140 |
| control_f2c | 32.9 % | 75.7 % | 55.0 % | 38 de 140 |
| arbitro_f3 | 36.4 % | 77.1 % | 65.0 % | 14 de 140 |

## 15. Limitaciones

- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de perspectivas es inducida por el prompt, no por conocimiento independiente.
- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad observada puede reflejar el marco institucional o la lectura del modelo.
- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede orientar la respuesta aunque no revele la asignación.
- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.
- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).
- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.
- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye la del servicio.
