# Informe del experimento: pilot

## 1. Configuración experimental

- Etiqueta: `pilot`; creada: 2026-09-26T11:35:21.693089+00:00
- Escenarios: 10 (S01, S02, S03, S04, S05, S06, S07, S08, S09, S10); repeticiones: 20
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

- Llamadas registradas (incluidos reintentos): 2800; previstas sin reintentos: 2000
- Corridas completas (con árbitro): 200 de 200
- Errores de API: 0
- JSON válido: 100.0 %; actividades completas: 100.0 %
- Control de contaminación del material enviado: {'OK': 2800}. REFERENCE_RACI no se envió a ningún agente (el script de ejecución no lee `posthoc/`).

## 5. Tokens consumidos

- Entrada: 64,853,440 (de ellos en caché: 17,894,381)
- Salida: 6,817,256 (razonamiento: 1,898,428)

## 6. Coste aproximado

USD 22.413 con precios configurados de 0.25 / 1.5 / 0.025 USD por millón (entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.

## 7. Decisiones iniciales (fase 1, especializados)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:56; ISC:14; DEL:3; TX_REG:2; DAS:2; DOS:2; GERENCIA_TECNICA:1 | 51.7 % | 8.8 % | 1.456 |
| S01 | ACT04 | DAS:80 | 100.0 % | 0.0 % | -0.000 |
| S01 | ACT06 | ISC:38; DAS:35; MCO:7 | 35.8 % | 0.0 % | 1.339 |
| S01 | ACT09 | ISC:72; MCO:5; DAS:2; ODC:1 | 82.5 % | 0.0 % | 0.599 |
| S01 | ACT12 | ODC:53; DAS:12; OP:5; ISC:4; MCO:3; DT:2; DOS:1 | 45.8 % | 11.2 % | 1.660 |
| S02 | ACT02 | DEL:53; DT:16; TX_REG:4; ISC:3; DOS:3; OP:1 | 43.3 % | 22.5 % | 1.508 |
| S02 | ACT04 | DAS:79; OP:1 | 97.5 % | 0.0 % | 0.097 |
| S02 | ACT05 | DAS:60; DOS:8; DEL:6; ISC:5; OP:1 | 57.5 % | 0.0 % | 1.253 |
| S02 | ACT11 | DAS:70; DOS:6; ODC:3; OP:1 | 78.3 % | 1.2 % | 0.705 |
| S03 | ACT06 | ISC:41; DAS:27; MCO:12 | 43.3 % | 1.2 % | 1.434 |
| S03 | ACT07 | DAS:78; ISC:1; MCO:1 | 95.0 % | 1.2 % | 0.194 |
| S03 | ACT09 | ISC:65; MCO:12; DAS:2; OP:1 | 66.7 % | 1.2 % | 0.866 |
| S03 | ACT13 | ODC:52; OP:25; DAS:3 | 49.2 % | 1.2 % | 1.106 |
| S04 | ACT06 | DAS:80 | 100.0 % | 1.2 % | -0.000 |
| S04 | ACT11 | DAS:80 | 100.0 % | 0.0 % | -0.000 |
| S04 | ACT17 | DAS:67; ISC:13 | 72.5 % | 7.5 % | 0.640 |
| S04 | ACT18 | DAS:36; ODC:35; OP:7; MCO:1; DOS:1 | 35.8 % | 0.0 % | 1.506 |
| S05 | ACT01 | ODC:66; OP:8; DOS:4; DEN:1; DAS:1 | 65.8 % | 1.2 % | 0.935 |
| S05 | ACT06 | DAS:62; ISC:10; MCO:8 | 57.5 % | 5.0 % | 0.992 |
| S05 | ACT09 | ISC:50; DAS:12; MCO:9; ODC:9 | 37.5 % | 0.0 % | 1.544 |
| S05 | ACT15 | ODC:78; OP:2 | 95.0 % | 0.0 % | 0.169 |
| S06 | ACT03 | DOS:31; ISC:18; DAS:15; DEL:15; OP:1 | 22.5 % | 0.0 % | 1.999 |
| S06 | ACT04 | DAS:80 | 100.0 % | 0.0 % | -0.000 |
| S06 | ACT05 | DAS:62; DOS:10; ISC:6; MCO:1; DEL:1 | 61.7 % | 1.2 % | 1.098 |
| S06 | ACT12 | MCO:19; ISC:17; DAS:13; ODC:12; DT:9; DOS:6; TX_REG:3; OTHER:1 | 12.5 % | 22.5 % | 2.695 |
| S06 | ACT13 | ODC:61; OP:14; DOS:5 | 66.7 % | 0.0 % | 0.988 |
| S07 | ACT10 | DAS:80 | 100.0 % | 2.5 % | -0.000 |
| S07 | ACT11 | DAS:56; DOS:15; ISC:5; OP:2; MCO:1; ODC:1 | 53.3 % | 8.8 % | 1.354 |
| S07 | ACT14 | OP:66; ODC:13; DAS:1 | 69.2 % | 8.8 % | 0.734 |
| S07 | ACT19 | OP:65; ODC:8; DAS:3; DOS:2; GERENCIA_TECNICA:1; NEW_AUTHORITY:1 | 67.5 % | 5.0 % | 1.044 |
| S08 | ACT08 | DAS:80 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT14 | OP:53; ODC:17; DAS:9; GERENCIA_TECNICA:1 | 46.7 % | 15.0 % | 1.302 |
| S08 | ACT15 | ODC:78; OP:2 | 95.0 % | 0.0 % | 0.169 |
| S08 | ACT16 | DAS:67; MCO:13 | 70.8 % | 10.0 % | 0.640 |
| S09 | ACT15 | ODC:80 | 100.0 % | 0.0 % | -0.000 |
| S09 | ACT18 | DAS:63; ODC:9; MCO:8 | 60.0 % | 11.2 % | 0.958 |
| S09 | ACT19 | OP:40; ODC:28; DAS:7; GERENCIA_TECNICA:4; DOS:1 | 37.5 % | 17.5 % | 1.633 |
| S09 | ACT20 | DAS:65; ODC:8; MCO:6; OP:1 | 70.0 % | 1.2 % | 0.935 |
| S10 | ACT01 | ODC:71; DAS:6; DOS:2; OP:1 | 79.2 % | 0.0 % | 0.645 |
| S10 | ACT14 | ODC:71; OP:8; DAS:1 | 77.5 % | 3.8 % | 0.564 |
| S10 | ACT15 | ODC:80 | 100.0 % | 0.0 % | -0.000 |
| S10 | ACT16 | DAS:76; MCO:3; ODC:1 | 90.0 % | 1.2 % | 0.327 |
| S10 | ACT20 | ODC:57; DAS:20; MCO:2; OP:1 | 60.8 % | 0.0 % | 1.061 |

Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):

| Escenario | DAS | ISC | MCO | ODC |
|---|---|---|---|---|
| S01 | 64.0 % | 61.0 % | 56.0 % | 63.0 % |
| S02 | 71.2 % | 68.8 % | 70.0 % | 67.5 % |
| S03 | 70.0 % | 66.2 % | 61.3 % | 58.8 % |
| S04 | 80.0 % | 73.8 % | 77.5 % | 77.5 % |
| S05 | 63.7 % | 62.5 % | 58.8 % | 67.5 % |
| S06 | 49.0 % | 52.0 % | 55.0 % | 51.0 % |
| S07 | 81.2 % | 75.0 % | 76.2 % | 70.0 % |
| S08 | 76.2 % | 78.8 % | 80.0 % | 76.2 % |
| S09 | 71.2 % | 65.0 % | 60.0 % | 58.8 % |
| S10 | 74.0 % | 80.0 % | 78.0 % | 82.0 % |

## 8. Decisiones posteriores al debate (fase 2)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | DT:73; ISC:4; TX_REG:3 | 85.8 % | 11.2 % | 0.514 |
| S01 | ACT04 | DAS:80 | 100.0 % | 0.0 % | -0.000 |
| S01 | ACT06 | ISC:53; DAS:22; MCO:5 | 72.5 % | 7.5 % | 1.156 |
| S01 | ACT09 | ISC:79; MCO:1 | 97.5 % | 0.0 % | 0.097 |
| S01 | ACT12 | ODC:75; DAS:2; DAS+ODC:2; ISC:1 | 90.8 % | 36.2 % | 0.432 |
| S02 | ACT02 | DEL:71; DT:9 | 92.5 % | 27.5 % | 0.507 |
| S02 | ACT04 | DAS:80 | 100.0 % | 0.0 % | -0.000 |
| S02 | ACT05 | DAS:65; DEL:7; DOS:6; ISC:2 | 80.0 % | 22.5 % | 0.964 |
| S02 | ACT11 | DAS:71; DOS:6; ODC:3 | 95.0 % | 1.2 % | 0.611 |
| S03 | ACT06 | ISC:50; DAS:25; MCO:5 | 78.3 % | 1.2 % | 1.198 |
| S03 | ACT07 | DAS:80 | 100.0 % | 1.2 % | -0.000 |
| S03 | ACT09 | ISC:78; MCO:2 | 96.7 % | 2.5 % | 0.169 |
| S03 | ACT13 | ODC:68; OP:12 | 83.3 % | 17.5 % | 0.610 |
| S04 | ACT06 | DAS:80 | 100.0 % | 0.0 % | -0.000 |
| S04 | ACT11 | DAS:80 | 100.0 % | 0.0 % | -0.000 |
| S04 | ACT17 | DAS:68; ISC:11; DAS+ISC:1 | 77.5 % | 25.0 % | 0.672 |
| S04 | ACT18 | ODC:56; DAS:20; OP:2; DAS+ODC:1; DOS:1 | 69.2 % | 3.8 % | 1.151 |
| S05 | ACT01 | ODC:79; DOS:1 | 97.5 % | 1.2 % | 0.097 |
| S05 | ACT06 | DAS:72; MCO:4; ISC:3; DAS+MCO:1 | 84.2 % | 15.0 % | 0.610 |
| S05 | ACT09 | ISC:76; DAS:2; MCO:1; ODC:1 | 90.0 % | 0.0 % | 0.361 |
| S05 | ACT15 | ODC:80 | 100.0 % | 0.0 % | -0.000 |
| S06 | ACT03 | DOS:38; ISC:21; DAS:11; DEL:10 | 54.2 % | 15.0 % | 1.785 |
| S06 | ACT04 | DAS:80 | 100.0 % | 0.0 % | -0.000 |
| S06 | ACT05 | DAS:74; DOS:4; ISC:2 | 86.7 % | 3.8 % | 0.453 |
| S06 | ACT12 | MCO:36; ISC:16; DT:11; DAS:8; ODC:6; DOS:2; TX_REG:1 | 60.0 % | 42.5 % | 2.201 |
| S06 | ACT13 | ODC:70; OP:9; DOS:1 | 83.3 % | 0.0 % | 0.602 |
| S07 | ACT10 | DAS:80 | 100.0 % | 1.2 % | -0.000 |
| S07 | ACT11 | DAS:53; DOS:23; DAS+DOS:2; ISC:1; ODC:1 | 73.3 % | 23.8 % | 1.202 |
| S07 | ACT14 | OP:75; ODC:5 | 90.8 % | 23.8 % | 0.337 |
| S07 | ACT19 | OP:71; DOS:5; ODC:4 | 81.7 % | 11.2 % | 0.619 |
| S08 | ACT08 | DAS:80 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT14 | OP:67; ODC:10; DAS:2; GERENCIA_TECNICA:1 | 80.0 % | 43.8 % | 0.801 |
| S08 | ACT15 | ODC:80 | 100.0 % | 0.0 % | -0.000 |
| S08 | ACT16 | DAS:55; MCO:25 | 72.5 % | 41.2 % | 0.896 |
| S09 | ACT15 | ODC:80 | 100.0 % | 0.0 % | -0.000 |
| S09 | ACT18 | DAS:75; ODC:2; DAS+ODC:1; MCO:1; DAS+MCO:1 | 88.3 % | 32.5 % | 0.457 |
| S09 | ACT19 | OP:43; ODC:24; DAS:6; DOS:4; GERENCIA_TECNICA:2; ODC+OP:1 | 64.2 % | 56.2 % | 1.711 |
| S09 | ACT20 | DAS:75; ODC:4; DAS+MCO:1 | 89.2 % | 3.8 % | 0.382 |
| S10 | ACT01 | ODC:80 | 100.0 % | 0.0 % | -0.000 |
| S10 | ACT14 | ODC:79; OP:1 | 97.5 % | 2.5 % | 0.097 |
| S10 | ACT15 | ODC:80 | 100.0 % | 0.0 % | -0.000 |
| S10 | ACT16 | DAS:79; MCO:1 | 97.5 % | 6.2 % | 0.097 |
| S10 | ACT20 | ODC:73; DAS:6; MCO:1 | 92.5 % | 1.2 % | 0.480 |

## 9. Consenso

| Escenario | Acuerdo antes | IC95 antes | Acuerdo después | IC95 después | CONVERGENCE_DELTA | IC95 delta | Consenso estricto antes | Consenso estricto después |
|---|---|---|---|---|---|---|---|---|
| S01 | 63.2 % | [0.582, 0.683] | 89.3 % | [0.852, 0.928] | 0.262 | [0.203, 0.322] | 42.0 % | 82.0 % |
| S02 | 69.2 % | [0.633, 0.750] | 91.9 % | [0.877, 0.963] | 0.227 | [0.169, 0.292] | 50.0 % | 85.0 % |
| S03 | 63.5 % | [0.592, 0.681] | 89.6 % | [0.858, 0.931] | 0.260 | [0.206, 0.308] | 35.0 % | 81.2 % |
| S04 | 77.1 % | [0.731, 0.806] | 86.7 % | [0.819, 0.908] | 0.096 | [0.050, 0.146] | 63.7 % | 77.5 % |
| S05 | 64.0 % | [0.590, 0.685] | 92.9 % | [0.885, 0.969] | 0.290 | [0.231, 0.348] | 36.2 % | 87.5 % |
| S06 | 52.7 % | [0.482, 0.568] | 76.8 % | [0.720, 0.815] | 0.242 | [0.193, 0.292] | 35.0 % | 63.0 % |
| S07 | 72.5 % | [0.656, 0.794] | 86.5 % | [0.810, 0.917] | 0.140 | [0.079, 0.206] | 53.8 % | 77.5 % |
| S08 | 78.1 % | [0.727, 0.833] | 88.1 % | [0.835, 0.925] | 0.100 | [0.052, 0.152] | 62.5 % | 78.8 % |
| S09 | 66.9 % | [0.615, 0.727] | 85.4 % | [0.787, 0.921] | 0.185 | [0.119, 0.254] | 47.5 % | 76.2 % |
| S10 | 81.5 % | [0.768, 0.860] | 97.5 % | [0.950, 0.995] | 0.160 | [0.108, 0.217] | 66.0 % | 95.0 % |

Global: acuerdo 68.9 % → 88.5 %; CONVERGENCE_DELTA = 0.196 (IC95 bootstrap sobre corridas [0.176, 0.217]). Mayor consenso no implica mayor corrección.

**Brazo control (fase 2c):** los mismos agentes reconsideran su decisión inicial sin ver propuestas ajenas. DELIBERATION_EFFECT = CONVERGENCE_DELTA − CONVERGENCE_DELTA_CONTROL estima la convergencia atribuible a la información de los demás, descontando la que produce el solo hecho de responder dos veces.

- Acuerdo en el control: 69.3 %; CONVERGENCE_DELTA_CONTROL = 0.005 (IC95 [-0.003, 0.012])
- DELIBERATION_EFFECT = 0.191 (IC95 [0.171, 0.212])
- Cambio de A en el control: 2.6 % frente a 17.1 % con deliberación

| Escenario | Acuerdo control | Delta control | Efecto deliberación | IC95 efecto |
|---|---|---|---|---|
| S01 | 63.0 % | -0.002 | 0.263 | [0.218, 0.307] |
| S02 | 70.4 % | 0.013 | 0.215 | [0.144, 0.290] |
| S03 | 65.2 % | 0.017 | 0.244 | [0.190, 0.298] |
| S04 | 77.9 % | 0.008 | 0.088 | [0.042, 0.135] |
| S05 | 66.2 % | 0.023 | 0.267 | [0.210, 0.327] |
| S06 | 53.2 % | 0.005 | 0.237 | [0.187, 0.287] |
| S07 | 71.5 % | -0.010 | 0.150 | [0.085, 0.217] |
| S08 | 76.5 % | -0.017 | 0.117 | [0.073, 0.163] |
| S09 | 66.5 % | -0.004 | 0.190 | [0.125, 0.256] |
| S10 | 83.0 % | 0.015 | 0.145 | [0.095, 0.198] |

## 10. Ambigüedad

- AMBIGUITY_RATE antes: 4.0 %; después: 11.2 %
- Árbitro, veredicto AMBIGUOUS: 17.7 %
- PROPOSED_NEW_AUTHORITY como A: 0.0 % de las decisiones de agentes

| Escenario | Actividad | Árbitro: consenso | Árbitro: A | Árbitro AMBIGUOUS |
|---|---|---|---|---|
| S01 | ACT02 | FULL:12; MAJORITY:7; NONE:1 | DT:19; TX_REG:1 | 10.0 % |
| S01 | ACT04 | FULL:19; MAJORITY:1 | DAS:20 | 0.0 % |
| S01 | ACT06 | MAJORITY:9; FULL:6; NONE:5 | ISC:15; DAS:5 | 25.0 % |
| S01 | ACT09 | FULL:18; MAJORITY:2 | ISC:20 | 0.0 % |
| S01 | ACT12 | MAJORITY:10; NONE:7; FULL:3 | ODC:19; DAS:1 | 40.0 % |
| S02 | ACT02 | MAJORITY:14; FULL:3; NONE:3 | DEL:18; DT:2 | 25.0 % |
| S02 | ACT04 | FULL:20 | DAS:20 | 0.0 % |
| S02 | ACT05 | NONE:8; MAJORITY:7; FULL:5 | DAS:18; DOS:1; DEL:1 | 40.0 % |
| S02 | ACT11 | FULL:16; MAJORITY:3; NONE:1 | DAS:18; DOS:2 | 5.0 % |
| S03 | ACT06 | MAJORITY:12; FULL:8 | ISC:14; DAS:6 | 0.0 % |
| S03 | ACT07 | FULL:20 | DAS:20 | 0.0 % |
| S03 | ACT09 | FULL:15; MAJORITY:3; NONE:2 | ISC:20 | 5.0 % |
| S03 | ACT13 | MAJORITY:10; NONE:7; FULL:3 | ODC:17; OP:3 | 40.0 % |
| S04 | ACT06 | FULL:13; MAJORITY:7 | DAS:20 | 0.0 % |
| S04 | ACT11 | FULL:16; MAJORITY:4 | DAS:20 | 0.0 % |
| S04 | ACT17 | NONE:13; MAJORITY:7 | DAS:17; ISC:3 | 65.0 % |
| S04 | ACT18 | MAJORITY:13; FULL:4; NONE:3 | ODC:15; DAS:5 | 15.0 % |
| S05 | ACT01 | MAJORITY:10; FULL:9; NONE:1 | ODC:20 | 0.0 % |
| S05 | ACT06 | MAJORITY:8; FULL:7; NONE:5 | DAS:18; DAS+MCO:2 | 25.0 % |
| S05 | ACT09 | FULL:11; MAJORITY:9 | ISC:20 | 0.0 % |
| S05 | ACT15 | FULL:20 | ODC:20 | 0.0 % |
| S06 | ACT03 | MAJORITY:13; NONE:6; FULL:1 | DOS:9; ISC:5; DAS:3; DEL:3 | 35.0 % |
| S06 | ACT04 | FULL:20 | DAS:20 | 0.0 % |
| S06 | ACT05 | FULL:14; MAJORITY:6 | DAS:19; DOS:1 | 5.0 % |
| S06 | ACT12 | NONE:11; MAJORITY:7; FULL:2 | MCO:11; DT:3; ISC:3; ODC:2; DAS:1 | 65.0 % |
| S06 | ACT13 | MAJORITY:11; FULL:9 | ODC:20 | 0.0 % |
| S07 | ACT10 | FULL:20 | DAS:20 | 0.0 % |
| S07 | ACT11 | MAJORITY:15; NONE:4; FULL:1 | DAS:10; DOS:8; DAS+DOS:2 | 35.0 % |
| S07 | ACT14 | FULL:10; MAJORITY:7; NONE:3 | OP:19; ODC:1 | 30.0 % |
| S07 | ACT19 | MAJORITY:9; NONE:6; FULL:5 | OP:16; DOS:4 | 35.0 % |
| S08 | ACT08 | FULL:20 | DAS:20 | 0.0 % |
| S08 | ACT14 | MAJORITY:10; FULL:6; NONE:4 | OP:18; ODC:2 | 50.0 % |
| S08 | ACT15 | FULL:20 | ODC:20 | 0.0 % |
| S08 | ACT16 | NONE:9; MAJORITY:8; FULL:3 | DAS:14; MCO:4; NONE:1; DAS+MCO:1 | 55.0 % |
| S09 | ACT15 | FULL:20 | ODC:20 | 0.0 % |
| S09 | ACT18 | MAJORITY:12; NONE:6; FULL:2 | DAS:19; DAS+MCO:1 | 50.0 % |
| S09 | ACT19 | NONE:12; MAJORITY:6; FULL:2 | OP:14; ODC:3; GERENCIA_TECNICA:1; DOS:1; NONE:1 | 70.0 % |
| S09 | ACT20 | MAJORITY:11; FULL:8; NONE:1 | DAS:19; ODC:1 | 5.0 % |
| S10 | ACT01 | FULL:13; MAJORITY:7 | ODC:20 | 0.0 % |
| S10 | ACT14 | MAJORITY:9; FULL:9; NONE:2 | ODC:20 | 10.0 % |
| S10 | ACT15 | FULL:20 | ODC:20 | 0.0 % |
| S10 | ACT16 | MAJORITY:9; FULL:8; NONE:3 | DAS:20 | 15.0 % |
| S10 | ACT20 | FULL:10; MAJORITY:9; NONE:1 | ODC:19; DAS:1 | 5.0 % |

## 11. Entropía de la autoridad (A)

Media por actividad: 0.841 bits antes y 0.495 bits después. Entropía baja indica asignación estable; alta, sensible a la interpretación. No es una medida de corrección.

## 12. Cambios de posición

POSITION_CHANGE_RATE global: 17.1 %.

| Agente | Escenario | n | Cambio de A | MAINTAIN | MODIFY | AMBIGUOUS | Declaración incoherente |
|---|---|---|---|---|---|---|---|
| DAS | S01 | 100 | 21.0 % | 66 | 29 | 5 | 2.0 % |
| DAS | S02 | 80 | 17.5 % | 53 | 24 | 3 | 1.2 % |
| DAS | S03 | 80 | 16.2 % | 61 | 17 | 2 | 5.0 % |
| DAS | S04 | 80 | 12.5 % | 55 | 23 | 2 | 11.2 % |
| DAS | S05 | 80 | 18.8 % | 56 | 24 | 0 | 1.2 % |
| DAS | S06 | 100 | 26.0 % | 71 | 24 | 5 | 8.0 % |
| DAS | S07 | 80 | 10.0 % | 61 | 11 | 8 | 1.2 % |
| DAS | S08 | 80 | 15.0 % | 52 | 20 | 8 | 2.5 % |
| DAS | S09 | 80 | 12.5 % | 55 | 20 | 5 | 1.2 % |
| DAS | S10 | 100 | 15.0 % | 76 | 24 | 0 | 1.0 % |
| ISC | S01 | 100 | 25.0 % | 67 | 28 | 5 | 6.0 % |
| ISC | S02 | 80 | 22.5 % | 53 | 22 | 5 | 5.0 % |
| ISC | S03 | 80 | 17.5 % | 53 | 25 | 2 | 2.5 % |
| ISC | S04 | 80 | 21.2 % | 50 | 29 | 1 | 7.5 % |
| ISC | S05 | 80 | 18.8 % | 51 | 25 | 4 | 1.2 % |
| ISC | S06 | 100 | 19.0 % | 74 | 21 | 5 | 5.0 % |
| ISC | S07 | 80 | 12.5 % | 60 | 10 | 10 | 3.8 % |
| ISC | S08 | 80 | 20.0 % | 50 | 23 | 7 | 0.0 % |
| ISC | S09 | 80 | 21.2 % | 51 | 22 | 7 | 3.8 % |
| ISC | S10 | 100 | 6.0 % | 77 | 21 | 2 | 0.0 % |
| MCO | S01 | 100 | 24.0 % | 65 | 30 | 5 | 3.0 % |
| MCO | S02 | 80 | 11.2 % | 63 | 12 | 5 | 1.2 % |
| MCO | S03 | 80 | 18.8 % | 60 | 14 | 6 | 10.0 % |
| MCO | S04 | 80 | 6.2 % | 57 | 20 | 3 | 1.2 % |
| MCO | S05 | 80 | 22.5 % | 54 | 25 | 1 | 3.8 % |
| MCO | S06 | 100 | 26.0 % | 67 | 25 | 8 | 3.0 % |
| MCO | S07 | 80 | 11.2 % | 53 | 19 | 8 | 2.5 % |
| MCO | S08 | 80 | 10.0 % | 54 | 18 | 8 | 3.8 % |
| MCO | S09 | 80 | 21.2 % | 53 | 14 | 13 | 3.8 % |
| MCO | S10 | 100 | 10.0 % | 83 | 14 | 3 | 1.0 % |
| ODC | S01 | 100 | 18.0 % | 69 | 23 | 8 | 3.0 % |
| ODC | S02 | 80 | 18.8 % | 53 | 21 | 6 | 7.5 % |
| ODC | S03 | 80 | 22.5 % | 49 | 30 | 1 | 3.8 % |
| ODC | S04 | 80 | 6.2 % | 59 | 18 | 3 | 5.0 % |
| ODC | S05 | 80 | 17.5 % | 54 | 26 | 0 | 7.5 % |
| ODC | S06 | 100 | 27.0 % | 63 | 29 | 8 | 3.0 % |
| ODC | S07 | 80 | 18.8 % | 57 | 19 | 4 | 3.8 % |
| ODC | S08 | 80 | 15.0 % | 45 | 32 | 3 | 3.8 % |
| ODC | S09 | 80 | 22.5 % | 51 | 26 | 3 | 2.5 % |
| ODC | S10 | 100 | 5.0 % | 82 | 18 | 0 | 1.0 % |

Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).

| Agente | P propia | P neutral | Diferencia | n |
|---|---|---|---|---|
| DAS | 51.4 % | 43.3 % | 0.081 | 860 |
| ISC | 17.2 % | 9.8 % | 0.074 | 860 |
| MCO | 5.6 % | 3.3 % | 0.023 | 860 |
| ODC | 32.4 % | 23.6 % | 0.088 | 860 |

## 13. Evidencia más utilizada

- EVIDENCE_VALIDITY_RATE: 98.6 % de 28743 citas
- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): 0.1 %
- A sin evidencia institucional válida: 2.2 %
- Violación de jerarquía (DOCUMENTADO con fuente no institucional): 2.1 %
- Cita textual verificada en la fuente: 97.2 % de 28188; en afirmaciones DOCUMENTADO: 96.9 % de 16843
- Proporción de citas INFERIDO: 4.3 %
La verificación textual prueba que el fragmento existe en la fuente citada, no que nombre la actividad; la pertinencia se audita con citation_audit.py.

| source_id | kind | total | phase1 | phase2 |
|---|---|---|---|---|
| NIST_CM_01 | externa | 3285 | 1261 | 1016 |
| DAS_2_1 | institucional | 1998 | 745 | 620 |
| DAS2_2_1 | institucional | 1393 | 527 | 435 |
| ODC_2_6 | institucional | 1276 | 480 | 387 |
| ODC_2_1 | institucional | 1210 | 458 | 340 |
| DAS1_2_2 | institucional | 1123 | 438 | 321 |
| DAS_2_2 | institucional | 1085 | 399 | 346 |
| ENISA_CHG_02 | externa | 871 | 335 | 265 |
| ISC2_2_3 | institucional | 820 | 303 | 253 |
| NIST_OT_01 | externa | 813 | 304 | 256 |
| ODC_2_5 | institucional | 748 | 310 | 194 |
| NIST_CM_02 | externa | 735 | 280 | 232 |
| MCO_2_8 | institucional | 732 | 263 | 224 |
| ERCOT_03 | externa | 711 | 258 | 240 |
| DAS1_2_1 | institucional | 691 | 259 | 212 |
| ENISA_CHG_01 | externa | 633 | 248 | 200 |
| ERCOT_04 | externa | 572 | 218 | 178 |
| DAS_2_4 | institucional | 508 | 193 | 151 |
| OP_2_1 | institucional | 484 | 179 | 147 |
| PJM_04 | externa | 438 | 170 | 136 |

## 14. Comparación post hoc con REFERENCE_RACI

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la correspondencia de columnas indicada en el README (Origen, GT*, AC).

| activity_id | activity | REFERENCE_A | match_individual_especializados_f1 | match_neutral_f1 | match_post_debate_f2 | match_control_sin_debate_f2c | match_arbitro_f3 |
|---|---|---|---|---|---|---|---|
| ACT01 | Definir el requisito y el alcance del cambio | DAS | 4.4 % | 0.0 % | 0.0 % | 4.4 % | 0.0 % |
| ACT02 | Certificar los datos de la instalación (configuración física y parámetros) | ORIGIN | 86.9 % | 80.0 % | 97.5 % | 85.0 % | 100.0 % |
| ACT03 | Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación) | DAS | 18.8 % | 35.0 % | 13.8 % | 18.8 % | 15.0 % |
| ACT04 | Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros) | DAS | 99.6 % | 100.0 % | 100.0 % | 99.6 % | 100.0 % |
| ACT05 | Revisar la calidad topológica y de nomenclatura del modelo construido | ISC | 6.9 % | 5.0 % | 2.5 % | 6.9 % | 0.0 % |
| ACT06 | Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones | ISC | 27.8 % | 25.0 % | 33.1 % | 28.1 % | 36.2 % |
| ACT07 | Unificar modelo y adquisición en la base integrada | ISC | 1.2 % | 0.0 % | 0.0 % | 0.0 % | 0.0 % |
| ACT08 | Preparar el paquete de implementación | ISC | 0.0 % | 0.0 % | 0.0 % | 0.0 % | 0.0 % |
| ACT09 | Aprobar las pruebas FAT/SAT y de integración | ISC | 77.9 % | 75.0 % | 97.1 % | 81.7 % | 100.0 % |
| ACT10 | Administrar y actualizar los aplicativos EMS | DAS | 100.0 % | 100.0 % | 100.0 % | 100.0 % | 100.0 % |
| ACT11 | Validar el estimador de estado, el flujo de potencia y demás aplicaciones | DAS | 85.8 % | 83.3 % | 85.0 % | 85.4 % | 80.0 % |
| ACT12 | Verificar la correspondencia de mímicos y modelo con la instalación física | ORIGIN | 13.8 % | 10.0 % | 8.8 % | 15.6 % | 7.5 % |
| ACT13 | Aceptar mímicos, alarmas y el uso operativo | ODC | 70.6 % | 62.5 % | 86.2 % | 73.8 % | 92.5 % |
| ACT14 | Autorizar la liberación de la versión a producción | NEW_AUTHORITY | 0.0 % | 0.0 % | 0.0 % | 0.0 % | 0.0 % |
| ACT15 | Habilitar o suspender la ventana de intervención en tiempo real | ODC | 98.8 % | 96.2 % | 100.0 % | 98.8 % | 100.0 % |
| ACT16 | Ejecutar el respaldo y la carga en producción | MCO | 10.0 % | 15.0 % | 16.2 % | 11.2 % | 10.0 % |
| ACT17 | Mantener el registro técnico de configuración | ISC | 16.2 % | 15.0 % | 13.8 % | 13.8 % | 15.0 % |
| ACT18 | Verificar el sistema después de la actualización y cerrar el cambio | DAS | 61.9 % | 57.5 % | 59.4 % | 61.9 % | 60.0 % |
| ACT19 | Aprobar los criterios de reversión y su delegación | NEW_AUTHORITY | 0.6 % | 0.0 % | 0.0 % | 0.0 % | 0.0 % |
| ACT20 | Ejecutar la reversión | MCO | 5.0 % | 5.0 % | 0.6 % | 5.0 % | 0.0 % |

### Matriz RACI modal

Matrices completas por grupo (A, R, C, I por unidad, con frecuencia y celdas inestables) en `modal_raci.md` y `modal_raci.csv`. Resumen de la comparación celda a celda:

| Grupo | Celdas idénticas | Celdas A/R idénticas | A recuperada | Celdas inestables |
|---|---|---|---|---|
| especializados_f1 | 20.0 % | 75.7 % | 40.0 % | 52 de 140 |
| neutral_f1 | 19.3 % | 75.0 % | 40.0 % | 48 de 140 |
| deliberacion_f2 | 21.4 % | 76.4 % | 45.0 % | 43 de 140 |
| control_f2c | 21.4 % | 76.4 % | 40.0 % | 51 de 140 |
| arbitro_f3 | 23.6 % | 76.4 % | 45.0 % | 37 de 140 |

## 15. Limitaciones

- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de perspectivas es inducida por el prompt, no por conocimiento independiente.
- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad observada puede reflejar el marco institucional o la lectura del modelo.
- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede orientar la respuesta aunque no revele la asignación.
- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.
- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).
- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.
- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye la del servicio.
