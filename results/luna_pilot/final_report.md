# Informe del experimento: luna_pilot

## 1. Configuración experimental

- Etiqueta: `luna_pilot`; creada: 2026-09-28T11:35:41.620021+00:00
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

- Llamadas registradas (incluidos reintentos): 871; previstas sin reintentos: 700
- Corridas completas (con árbitro): 50 de 50
- Errores de API: 162
- JSON válido: 100.0 %; actividades completas: 100.0 %
- Control de contaminación del material enviado: {'OK': 871}. REFERENCE_RACI no se envió a ningún agente (el script de ejecución no lee `posthoc/`).

## 5. Tokens consumidos

- Entrada: 18,021,425 (de ellos en caché: 3,294,509)
- Salida: 3,132,025 (razonamiento: 1,048,598)

## 6. Coste aproximado

USD 1.7199 con precios configurados para `gpt-6-luna` de 0.1 / 0.5 / 0.01 USD por millón (entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.

## 7. Decisiones iniciales (fase 1, especializados)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:17; OTHER:2; NONE:1 | 73.3 % | 100.0 % | 0.748 |
| S01 | ACT04 | DAS:20 | 100.0 % | 45.0 % | -0.000 |
| S01 | ACT06 | MCO:10; DAS:7; ISC:3 | 26.7 % | 100.0 % | 1.441 |
| S01 | ACT09 | ISC:20 | 100.0 % | 85.0 % | -0.000 |
| S01 | ACT12 | DAS:15; MCO:3; ISC:2 | 53.3 % | 100.0 % | 1.054 |
| S02 | ACT02 | DT:20 | 100.0 % | 100.0 % | -0.000 |
| S02 | ACT04 | DAS:20 | 100.0 % | 30.0 % | -0.000 |
| S02 | ACT05 | DAS:16; DEL:2; DOS:2 | 63.3 % | 70.0 % | 0.922 |
| S02 | ACT11 | DAS:20 | 100.0 % | 40.0 % | -0.000 |
| S03 | ACT06 | DAS:13; MCO:4; ISC:3 | 43.3 % | 95.0 % | 1.279 |
| S03 | ACT07 | DAS:16; ISC:4 | 73.3 % | 85.0 % | 0.722 |
| S03 | ACT09 | ISC:20 | 100.0 % | 65.0 % | -0.000 |
| S03 | ACT13 | ODC:19; MCO:1 | 90.0 % | 100.0 % | 0.286 |
| S04 | ACT06 | DAS:20 | 100.0 % | 45.0 % | -0.000 |
| S04 | ACT11 | DAS:19; DOS:1 | 90.0 % | 45.0 % | 0.286 |
| S04 | ACT17 | DAS:17; ISC:3 | 70.0 % | 70.0 % | 0.610 |
| S04 | ACT18 | DAS:20 | 100.0 % | 70.0 % | -0.000 |
| S05 | ACT01 | DAS:15; ODC:5 | 56.7 % | 70.0 % | 0.811 |
| S05 | ACT06 | DAS:13; MCO:7 | 43.3 % | 95.0 % | 0.934 |
| S05 | ACT09 | ISC:15; MCO:4; DAS:1 | 70.0 % | 95.0 % | 0.992 |
| S05 | ACT15 | ODC:20 | 100.0 % | 10.0 % | -0.000 |
| S06 | ACT03 | DAS:19; ISC:1 | 90.0 % | 100.0 % | 0.286 |
| S06 | ACT04 | DAS:20 | 100.0 % | 40.0 % | -0.000 |
| S06 | ACT05 | DAS:15; DEL:3; DOS:2 | 56.7 % | 90.0 % | 1.054 |
| S06 | ACT12 | MCO:11; ISC:4; DAS:3; DT:2 | 33.3 % | 95.0 % | 1.681 |
| S06 | ACT13 | ODC:20 | 100.0 % | 95.0 % | -0.000 |
| S07 | ACT10 | DAS:20 | 100.0 % | 0.0 % | -0.000 |
| S07 | ACT11 | DAS:20 | 100.0 % | 50.0 % | -0.000 |
| S07 | ACT14 | DAS:14; NEW_AUTHORITY:5; ODC:1 | 50.0 % | 100.0 % | 1.076 |
| S07 | ACT19 | NEW_AUTHORITY:12; DAS:8 | 46.7 % | 100.0 % | 0.971 |
| S08 | ACT08 | DAS:20 | 100.0 % | 30.0 % | -0.000 |
| S08 | ACT14 | DAS:12; NEW_AUTHORITY:8 | 60.0 % | 100.0 % | 0.971 |
| S08 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT16 | DAS:12; MCO:8 | 53.3 % | 100.0 % | 0.971 |
| S09 | ACT15 | ODC:20 | 100.0 % | 20.0 % | -0.000 |
| S09 | ACT18 | DAS:20 | 100.0 % | 80.0 % | -0.000 |
| S09 | ACT19 | NEW_AUTHORITY:10; DAS:9; ODC:1 | 43.3 % | 95.0 % | 1.234 |
| S09 | ACT20 | DAS:20 | 100.0 % | 80.0 % | -0.000 |
| S10 | ACT01 | ODC:13; DAS:7 | 43.3 % | 80.0 % | 0.934 |
| S10 | ACT14 | DAS:18; ODC:2 | 80.0 % | 100.0 % | 0.469 |
| S10 | ACT15 | ODC:20 | 100.0 % | 5.0 % | -0.000 |
| S10 | ACT16 | DAS:20 | 100.0 % | 65.0 % | -0.000 |
| S10 | ACT20 | DAS:20 | 100.0 % | 70.0 % | -0.000 |

Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):

| Escenario | DAS | ISC | MCO | ODC |
|---|---|---|---|---|
| S01 | 84.0 % | 76.0 % | 72.0 % | 84.0 % |
| S02 | 100.0 % | 95.0 % | 90.0 % | 95.0 % |
| S03 | 95.0 % | 70.0 % | 75.0 % | 90.0 % |
| S04 | 100.0 % | 100.0 % | 80.0 % | 100.0 % |
| S05 | 70.0 % | 55.0 % | 80.0 % | 75.0 % |
| S06 | 80.0 % | 76.0 % | 68.0 % | 64.0 % |
| S07 | 75.0 % | 70.0 % | 75.0 % | 70.0 % |
| S08 | 75.0 % | 90.0 % | 80.0 % | 75.0 % |
| S09 | 80.0 % | 90.0 % | 85.0 % | 95.0 % |
| S10 | 92.0 % | 80.0 % | 84.0 % | 80.0 % |

## 8. Decisiones posteriores al debate (fase 2)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:20 | 100.0 % | 100.0 % | -0.000 |
| S01 | ACT04 | DAS:20 | 100.0 % | 40.0 % | -0.000 |
| S01 | ACT06 | MCO:18; DAS:2 | 86.7 % | 100.0 % | 0.469 |
| S01 | ACT09 | ISC:20 | 100.0 % | 100.0 % | -0.000 |
| S01 | ACT12 | DAS:16; MCO:2; ISC:1; NONE:1 | 60.0 % | 100.0 % | 1.022 |
| S02 | ACT02 | DT:20 | 100.0 % | 100.0 % | -0.000 |
| S02 | ACT04 | DAS:20 | 100.0 % | 20.0 % | -0.000 |
| S02 | ACT05 | DAS:20 | 100.0 % | 100.0 % | -0.000 |
| S02 | ACT11 | DAS:20 | 100.0 % | 90.0 % | -0.000 |
| S03 | ACT06 | DAS:17; MCO:2; ISC:1 | 83.3 % | 100.0 % | 0.748 |
| S03 | ACT07 | DAS:15; ISC:5 | 76.7 % | 100.0 % | 0.811 |
| S03 | ACT09 | ISC:20 | 100.0 % | 100.0 % | -0.000 |
| S03 | ACT13 | ODC:20 | 100.0 % | 100.0 % | -0.000 |
| S04 | ACT06 | DAS:20 | 100.0 % | 20.0 % | -0.000 |
| S04 | ACT11 | DAS:20 | 100.0 % | 65.0 % | -0.000 |
| S04 | ACT17 | DAS:19; ISC:1 | 90.0 % | 100.0 % | 0.286 |
| S04 | ACT18 | DAS:20 | 100.0 % | 90.0 % | -0.000 |
| S05 | ACT01 | DAS:17; ODC:3 | 90.0 % | 100.0 % | 0.610 |
| S05 | ACT06 | DAS:15; MCO:5 | 63.3 % | 100.0 % | 0.811 |
| S05 | ACT09 | ISC:15; MCO:4; NONE:1 | 70.0 % | 100.0 % | 0.992 |
| S05 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S06 | ACT03 | DAS:20 | 100.0 % | 100.0 % | -0.000 |
| S06 | ACT04 | DAS:20 | 100.0 % | 40.0 % | -0.000 |
| S06 | ACT05 | DAS:20 | 100.0 % | 100.0 % | -0.000 |
| S06 | ACT12 | MCO:15; ISC:4; DT:1 | 80.0 % | 100.0 % | 0.992 |
| S06 | ACT13 | ODC:20 | 100.0 % | 100.0 % | -0.000 |
| S07 | ACT10 | DAS:20 | 100.0 % | 5.0 % | -0.000 |
| S07 | ACT11 | DAS:20 | 100.0 % | 90.0 % | -0.000 |
| S07 | ACT14 | DAS:14; NEW_AUTHORITY:6 | 80.0 % | 100.0 % | 0.881 |
| S07 | ACT19 | NEW_AUTHORITY:15; DAS:5 | 70.0 % | 100.0 % | 0.811 |
| S08 | ACT08 | DAS:20 | 100.0 % | 25.0 % | -0.000 |
| S08 | ACT14 | DAS:11; NEW_AUTHORITY:9 | 76.7 % | 100.0 % | 0.993 |
| S08 | ACT15 | ODC:20 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT16 | MCO:11; DAS:9 | 90.0 % | 100.0 % | 0.993 |
| S09 | ACT15 | ODC:20 | 100.0 % | 45.0 % | -0.000 |
| S09 | ACT18 | DAS:20 | 100.0 % | 95.0 % | -0.000 |
| S09 | ACT19 | NEW_AUTHORITY:17; DAS:3 | 90.0 % | 100.0 % | 0.610 |
| S09 | ACT20 | DAS:20 | 100.0 % | 100.0 % | -0.000 |
| S10 | ACT01 | ODC:11; DAS:9 | 76.7 % | 100.0 % | 0.993 |
| S10 | ACT14 | DAS:20 | 100.0 % | 100.0 % | -0.000 |
| S10 | ACT15 | ODC:20 | 100.0 % | 5.0 % | -0.000 |
| S10 | ACT16 | DAS:20 | 100.0 % | 95.0 % | -0.000 |
| S10 | ACT20 | DAS:20 | 100.0 % | 95.0 % | -0.000 |

## 9. Consenso

| Escenario | Acuerdo antes | IC95 antes | Acuerdo después | IC95 después | CONVERGENCE_DELTA | IC95 delta | Consenso estricto antes | Consenso estricto después |
|---|---|---|---|---|---|---|---|---|
| S01 | 70.7 % | [0.587, 0.793] | 89.3 % | [0.820, 0.960] | 0.187 | [0.080, 0.300] | 56.0 % | 80.0 % |
| S02 | 90.8 % | [0.842, 0.975] | 100.0 % | [1.000, 1.000] | 0.092 | [0.025, 0.158] | 85.0 % | 100.0 % |
| S03 | 76.7 % | [0.617, 0.875] | 90.0 % | [0.750, 1.000] | 0.133 | [0.125, 0.150] | 60.0 % | 85.0 % |
| S04 | 90.0 % | [0.825, 0.975] | 97.5 % | [0.925, 1.000] | 0.075 | [0.000, 0.175] | 80.0 % | 95.0 % |
| S05 | 67.5 % | [0.617, 0.725] | 80.8 % | [0.733, 0.908] | 0.133 | [0.058, 0.200] | 40.0 % | 65.0 % |
| S06 | 76.0 % | [0.707, 0.833] | 96.0 % | [0.920, 1.000] | 0.200 | [0.140, 0.260] | 60.0 % | 92.0 % |
| S07 | 74.2 % | [0.692, 0.792] | 87.5 % | [0.800, 0.950] | 0.133 | [0.067, 0.217] | 55.0 % | 75.0 % |
| S08 | 78.3 % | [0.733, 0.842] | 91.7 % | [0.817, 1.000] | 0.133 | [0.075, 0.200] | 60.0 % | 85.0 % |
| S09 | 85.8 % | [0.842, 0.875] | 97.5 % | [0.925, 1.000] | 0.117 | [0.058, 0.158] | 75.0 % | 95.0 % |
| S10 | 84.7 % | [0.800, 0.893] | 95.3 % | [0.900, 1.000] | 0.107 | [0.033, 0.167] | 72.0 % | 92.0 % |

Global: acuerdo 79.5 % → 92.6 %; CONVERGENCE_DELTA = 0.131 (IC95 bootstrap sobre corridas [0.105, 0.157]). Mayor consenso no implica mayor corrección.

**Brazo control (fase 2c):** los mismos agentes reconsideran su decisión inicial sin ver propuestas ajenas. DELIBERATION_EFFECT = CONVERGENCE_DELTA − CONVERGENCE_DELTA_CONTROL estima la convergencia atribuible a la información de los demás, descontando la que produce el solo hecho de responder dos veces.

- Acuerdo en el control: 79.8 %; CONVERGENCE_DELTA_CONTROL = 0.003 (IC95 [-0.016, 0.022])
- DELIBERATION_EFFECT = 0.128 (IC95 [0.101, 0.156])
- Cambio de A en el control: 5.6 % frente a 9.5 % con deliberación

| Escenario | Acuerdo control | Delta control | Efecto deliberación | IC95 efecto |
|---|---|---|---|---|
| S01 | 66.0 % | -0.047 | 0.233 | [0.153, 0.307] |
| S02 | 97.5 % | 0.067 | 0.025 | [0.000, 0.075] |
| S03 | 67.5 % | -0.092 | 0.225 | [0.167, 0.283] |
| S04 | 90.0 % | 0.000 | 0.075 | [0.000, 0.175] |
| S05 | 66.7 % | -0.008 | 0.142 | [0.083, 0.200] |
| S06 | 76.7 % | 0.007 | 0.193 | [0.153, 0.240] |
| S07 | 81.7 % | 0.075 | 0.058 | [0.008, 0.117] |
| S08 | 82.5 % | 0.042 | 0.092 | [0.017, 0.175] |
| S09 | 85.0 % | -0.008 | 0.125 | [0.058, 0.167] |
| S10 | 84.0 % | -0.007 | 0.113 | [0.033, 0.173] |

## 10. Ambigüedad

- AMBIGUITY_RATE antes: 70.0 %; después: 79.5 %
- Árbitro, veredicto AMBIGUOUS: 84.7 %
- PROPOSED_NEW_AUTHORITY como A: 4.5 % de las decisiones de agentes

| Escenario | Actividad | Árbitro: consenso | Árbitro: A | Árbitro AMBIGUOUS |
|---|---|---|---|---|
| S01 | ACT02 | FULL:5 | DT:5 | 100.0 % |
| S01 | ACT04 | FULL:5 | DAS:5 | 80.0 % |
| S01 | ACT06 | FULL:4; NONE:1 | MCO:5 | 100.0 % |
| S01 | ACT09 | FULL:5 | ISC:5 | 100.0 % |
| S01 | ACT12 | MAJORITY:4; FULL:1 | DAS:4; ISC:1 | 100.0 % |
| S02 | ACT02 | FULL:5 | DT:5 | 100.0 % |
| S02 | ACT04 | FULL:5 | DAS:5 | 20.0 % |
| S02 | ACT05 | FULL:5 | DAS:5 | 100.0 % |
| S02 | ACT11 | FULL:4; NONE:1 | DAS:5 | 100.0 % |
| S03 | ACT06 | FULL:4; NONE:1 | DAS:4; ISC:1 | 100.0 % |
| S03 | ACT07 | FULL:3; NONE:2 | DAS:3; ISC:2 | 100.0 % |
| S03 | ACT09 | FULL:5 | ISC:5 | 100.0 % |
| S03 | ACT13 | FULL:5 | ODC:5 | 100.0 % |
| S04 | ACT06 | FULL:4; MAJORITY:1 | DAS:5 | 0.0 % |
| S04 | ACT11 | FULL:3; MAJORITY:2 | DAS:5 | 100.0 % |
| S04 | ACT17 | MAJORITY:3; FULL:2 | DAS:5 | 100.0 % |
| S04 | ACT18 | FULL:5 | DAS:5 | 100.0 % |
| S05 | ACT01 | FULL:4; MAJORITY:1 | DAS:4; ODC:1 | 100.0 % |
| S05 | ACT06 | NONE:2; FULL:2; MAJORITY:1 | DAS:3; MCO:2 | 100.0 % |
| S05 | ACT09 | MAJORITY:3; FULL:2 | ISC:4; MCO:1 | 100.0 % |
| S05 | ACT15 | FULL:5 | ODC:5 | 20.0 % |
| S06 | ACT03 | FULL:5 | DAS:5 | 100.0 % |
| S06 | ACT04 | FULL:5 | DAS:5 | 80.0 % |
| S06 | ACT05 | FULL:4; MAJORITY:1 | DAS:5 | 100.0 % |
| S06 | ACT12 | FULL:3; MAJORITY:2 | MCO:3; ISC:2 | 100.0 % |
| S06 | ACT13 | FULL:5 | ODC:5 | 100.0 % |
| S07 | ACT10 | FULL:5 | DAS:5 | 0.0 % |
| S07 | ACT11 | MAJORITY:3; FULL:2 | DAS:5 | 100.0 % |
| S07 | ACT14 | FULL:3; MAJORITY:2 | DAS:3; NEW_AUTHORITY:2 | 100.0 % |
| S07 | ACT19 | MAJORITY:3; FULL:2 | NEW_AUTHORITY:3; NONE:1; DAS:1 | 100.0 % |
| S08 | ACT08 | FULL:5 | DAS:5 | 0.0 % |
| S08 | ACT14 | FULL:3; NONE:1; MAJORITY:1 | NEW_AUTHORITY:3; DAS:2 | 100.0 % |
| S08 | ACT15 | FULL:5 | ODC:5 | 0.0 % |
| S08 | ACT16 | FULL:4; MAJORITY:1 | MCO:3; DAS:2 | 100.0 % |
| S09 | ACT15 | FULL:5 | ODC:5 | 100.0 % |
| S09 | ACT18 | FULL:5 | DAS:5 | 100.0 % |
| S09 | ACT19 | FULL:4; MAJORITY:1 | NEW_AUTHORITY:5 | 100.0 % |
| S09 | ACT20 | FULL:5 | DAS:5 | 100.0 % |
| S10 | ACT01 | FULL:3; MAJORITY:1; NONE:1 | ODC:3; DAS:2 | 100.0 % |
| S10 | ACT14 | FULL:5 | DAS:5 | 100.0 % |
| S10 | ACT15 | FULL:5 | ODC:5 | 40.0 % |
| S10 | ACT16 | FULL:5 | DAS:5 | 100.0 % |
| S10 | ACT20 | FULL:5 | DAS:5 | 100.0 % |

## 11. Entropía de la autoridad (A)

Media por actividad: 0.459 bits antes y 0.280 bits después. Entropía baja indica asignación estable; alta, sensible a la interpretación. No es una medida de corrección.

## 12. Cambios de posición

POSITION_CHANGE_RATE global: 9.5 %.

| Agente | Escenario | n | Cambio de A | MAINTAIN | MODIFY | AMBIGUOUS | Declaración incoherente |
|---|---|---|---|---|---|---|---|
| DAS | S01 | 25 | 4.0 % | 19 | 1 | 5 | 0.0 % |
| DAS | S02 | 20 | 0.0 % | 5 | 1 | 14 | 0.0 % |
| DAS | S03 | 20 | 10.0 % | 8 | 0 | 12 | 0.0 % |
| DAS | S04 | 20 | 0.0 % | 8 | 2 | 10 | 5.0 % |
| DAS | S05 | 20 | 10.0 % | 7 | 0 | 13 | 0.0 % |
| DAS | S06 | 25 | 4.0 % | 13 | 1 | 11 | 0.0 % |
| DAS | S07 | 20 | 5.0 % | 14 | 0 | 6 | 0.0 % |
| DAS | S08 | 20 | 20.0 % | 16 | 2 | 2 | 0.0 % |
| DAS | S09 | 20 | 15.0 % | 2 | 3 | 15 | 0.0 % |
| DAS | S10 | 25 | 8.0 % | 18 | 1 | 6 | 0.0 % |
| ISC | S01 | 25 | 20.0 % | 15 | 4 | 6 | 0.0 % |
| ISC | S02 | 20 | 5.0 % | 7 | 3 | 10 | 0.0 % |
| ISC | S03 | 20 | 20.0 % | 8 | 4 | 8 | 0.0 % |
| ISC | S04 | 20 | 0.0 % | 12 | 1 | 7 | 0.0 % |
| ISC | S05 | 20 | 10.0 % | 6 | 2 | 12 | 0.0 % |
| ISC | S06 | 25 | 12.0 % | 12 | 2 | 11 | 0.0 % |
| ISC | S07 | 20 | 10.0 % | 11 | 1 | 8 | 0.0 % |
| ISC | S08 | 20 | 10.0 % | 14 | 1 | 5 | 0.0 % |
| ISC | S09 | 20 | 10.0 % | 3 | 1 | 16 | 0.0 % |
| ISC | S10 | 25 | 16.0 % | 11 | 5 | 9 | 0.0 % |
| MCO | S01 | 25 | 28.0 % | 13 | 8 | 4 | 0.0 % |
| MCO | S02 | 20 | 10.0 % | 9 | 2 | 9 | 5.0 % |
| MCO | S03 | 20 | 5.0 % | 12 | 3 | 5 | 5.0 % |
| MCO | S04 | 20 | 15.0 % | 11 | 3 | 6 | 0.0 % |
| MCO | S05 | 20 | 10.0 % | 14 | 0 | 6 | 0.0 % |
| MCO | S06 | 25 | 16.0 % | 13 | 4 | 8 | 0.0 % |
| MCO | S07 | 20 | 15.0 % | 11 | 6 | 3 | 0.0 % |
| MCO | S08 | 20 | 5.0 % | 12 | 0 | 8 | 0.0 % |
| MCO | S09 | 20 | 10.0 % | 12 | 1 | 7 | 0.0 % |
| MCO | S10 | 25 | 4.0 % | 22 | 1 | 2 | 0.0 % |
| ODC | S01 | 25 | 12.0 % | 17 | 3 | 5 | 0.0 % |
| ODC | S02 | 20 | 5.0 % | 8 | 0 | 12 | 0.0 % |
| ODC | S03 | 20 | 5.0 % | 12 | 2 | 6 | 5.0 % |
| ODC | S04 | 20 | 0.0 % | 10 | 1 | 9 | 0.0 % |
| ODC | S05 | 20 | 5.0 % | 8 | 0 | 12 | 0.0 % |
| ODC | S06 | 25 | 16.0 % | 10 | 2 | 13 | 0.0 % |
| ODC | S07 | 20 | 15.0 % | 8 | 3 | 9 | 0.0 % |
| ODC | S08 | 20 | 5.0 % | 11 | 0 | 9 | 0.0 % |
| ODC | S09 | 20 | 0.0 % | 14 | 0 | 6 | 0.0 % |
| ODC | S10 | 25 | 4.0 % | 11 | 0 | 14 | 0.0 % |

Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).

| Agente | P propia | P neutral | Diferencia | n |
|---|---|---|---|---|
| DAS | 63.3 % | 63.3 % | 0.000 | 215 |
| ISC | 9.3 % | 6.5 % | 0.028 | 215 |
| MCO | 3.3 % | 4.2 % | -0.009 | 215 |
| ODC | 17.7 % | 14.0 % | 0.037 | 215 |

## 13. Evidencia más utilizada

- EVIDENCE_VALIDITY_RATE: 100.0 % de 16300 citas
- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): 0.0 %
- A sin evidencia institucional válida: 0.0 %
- Violación de jerarquía (DOCUMENTADO con fuente no institucional): 0.6 %
- Cita textual verificada en la fuente: 99.6 % de 15563; en afirmaciones DOCUMENTADO: 99.8 % de 1150
- Proporción de citas INFERIDO: 59.1 %
La verificación textual prueba que el fragmento existe en la fuente citada, no que nombre la actividad; la pertinencia se audita con citation_audit.py.

| source_id | kind | total | phase1 | phase2 |
|---|---|---|---|---|
| DAS_2_4 | institucional | 1671 | 581 | 496 |
| NIST_CM_01 | externa | 1069 | 409 | 319 |
| DAS1_2_2 | institucional | 1063 | 357 | 348 |
| ODC_2_1 | institucional | 1015 | 342 | 322 |
| DAS2_2_1 | institucional | 698 | 231 | 223 |
| MCO_2_6 | institucional | 690 | 229 | 201 |
| NIST_OT_01 | externa | 659 | 236 | 220 |
| DAS2_2_2 | institucional | 639 | 219 | 204 |
| MCO_2_8 | institucional | 631 | 206 | 200 |
| IEC61970_456_01 | externa | 572 | 214 | 194 |
| NIST_CM_02 | externa | 542 | 206 | 158 |
| DAS_2_1 | institucional | 540 | 194 | 160 |
| ODC_2_6 | institucional | 452 | 157 | 137 |
| ENISA_CHG_02 | externa | 406 | 153 | 123 |
| ERCOT_02 | externa | 380 | 152 | 97 |
| DEL_2_5 | institucional | 295 | 102 | 91 |
| DOS_2_7 | institucional | 289 | 115 | 75 |
| ISC2_2_3 | institucional | 259 | 88 | 77 |
| DAS_2_2 | institucional | 258 | 91 | 78 |
| DAS1_2_1 | institucional | 253 | 96 | 65 |

## 14. Comparación post hoc con REFERENCE_RACI

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la correspondencia de columnas indicada en el README (Origen, GT*, AC).

| activity_id | activity | REFERENCE_A | match_individual_especializados_f1 | match_neutral_f1 | match_post_debate_f2 | match_control_sin_debate_f2c | match_arbitro_f3 |
|---|---|---|---|---|---|---|---|
| ACT01 | Definir el requisito y el alcance del cambio | DAS | 55.0 % | 80.0 % | 65.0 % | 57.5 % | 60.0 % |
| ACT02 | Certificar los datos de la instalación (configuración física y parámetros) | ORIGIN | 97.5 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT03 | Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación) | DAS | 95.0 % | 80.0 % | 100.0 % | 95.0 % | 100.0 % |
| ACT04 | Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros) | DAS | 100.0 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT05 | Revisar la calidad topológica y de nomenclatura del modelo construido | ISC | 0.0 % | 0.0 % | 0.0 % | 0.0 % | 0.0 % |
| ACT06 | Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones | ISC | 7.5 % | 5.0 % | 1.2 % | 7.5 % | 5.0 % |
| ACT07 | Unificar modelo y adquisición en la base integrada | ISC | 20.0 % | 0.0 % | 25.0 % | 45.0 % | 40.0 % |
| ACT08 | Preparar el paquete de implementación | ISC | 0.0 % | 0.0 % | 0.0 % | 0.0 % | 0.0 % |
| ACT09 | Aprobar las pruebas FAT/SAT y de integración | ISC | 91.7 % | 86.7 % | 91.7 % | 88.3 % | 93.3 % |
| ACT10 | Administrar y actualizar los aplicativos EMS | DAS | 100.0 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT11 | Validar el estimador de estado, el flujo de potencia y demás aplicaciones | DAS | 98.3 % | 100.0 % | 100.0 % | 98.3 % | 100.0 % |
| ACT12 | Verificar la correspondencia de mímicos y modelo con la instalación física | ORIGIN | 5.0 % | 10.0 % | 2.5 % | 15.0 % | 0.0 % |
| ACT13 | Aceptar mímicos, alarmas y el uso operativo | ODC | 97.5 % | 80.0 % | 100.0 % | 97.5 % | 100.0 % |
| ACT14 | Autorizar la liberación de la versión a producción | NEW_AUTHORITY | 21.7 % | 33.3 % | 25.0 % | 16.7 % | 33.3 % |
| ACT15 | Habilitar o suspender la ventana de intervención en tiempo real | ODC | 100.0 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT16 | Ejecutar el respaldo y la carga en producción | MCO | 20.0 % | 0.0 % | 27.5 % | 32.5 % | 30.0 % |
| ACT17 | Mantener el registro técnico de configuración | ISC | 15.0 % | 0.0 % | 5.0 % | 15.0 % | 0.0 % |
| ACT18 | Verificar el sistema después de la actualización y cerrar el cambio | DAS | 100.0 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT19 | Aprobar los criterios de reversión y su delegación | NEW_AUTHORITY | 55.0 % | 80.0 % | 80.0 % | 50.0 % | 80.0 % |
| ACT20 | Ejecutar la reversión | MCO | 0.0 % | 0.0 % | 0.0 % | 0.0 % | 0.0 % |

### Matriz RACI modal

Matrices completas por grupo (A, R, C, I por unidad, con frecuencia y celdas inestables) en `modal_raci.md` y `modal_raci.csv`. Resumen de la comparación celda a celda:

| Grupo | Celdas idénticas | Celdas A/R idénticas | A recuperada | Celdas inestables |
|---|---|---|---|---|
| especializados_f1 | 31.4 % | 77.1 % | 55.0 % | 32 de 140 |
| neutral_f1 | 33.6 % | 77.1 % | 55.0 % | 15 de 140 |
| deliberacion_f2 | 35.7 % | 76.4 % | 55.0 % | 15 de 140 |
| control_f2c | 32.1 % | 77.1 % | 55.0 % | 33 de 140 |
| arbitro_f3 | 35.7 % | 75.7 % | 55.0 % | 12 de 140 |

## 15. Limitaciones

- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de perspectivas es inducida por el prompt, no por conocimiento independiente.
- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad observada puede reflejar el marco institucional o la lectura del modelo.
- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede orientar la respuesta aunque no revele la asignación.
- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.
- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).
- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.
- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye la del servicio.
