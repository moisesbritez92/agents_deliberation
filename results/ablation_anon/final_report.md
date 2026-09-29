# Informe del experimento: ablation_anon

## 1. Configuración experimental

- Etiqueta: `ablation_anon`; creada: 2026-09-26T21:30:53.928802+00:00
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

- Llamadas registradas (incluidos reintentos): 1000; previstas sin reintentos: 1000
- Corridas completas (con árbitro): 200 de 200
- Errores de API: 0
- JSON válido: 100.0 %; actividades completas: 100.0 %
- Control de contaminación del material enviado: {'OK': 1000}. REFERENCE_RACI no se envió a ningún agente (el script de ejecución no lee `posthoc/`).

## 5. Tokens consumidos

- Entrada: 18,691,900 (de ellos en caché: 6,568,015)
- Salida: 2,605,019 (razonamiento: 926,394)

## 6. Coste aproximado

USD 7.1027 con precios configurados de 0.25 / 1.5 / 0.025 USD por millón (entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.

## 7. Decisiones iniciales (fase 1, especializados)

| Escenario | Actividad | Distribución de A | Acuerdo | Ambigüedad | H(A) bits |
|---|---|---|---|---|---|
| S01 | ACT02 | ISC:53; MCO:12; TX_REG:9; DT:3; DOS:3 | 45.8 % | 2.5 % | 1.514 |
| S01 | ACT04 | DAS:73; MCO:7 | 82.5 % | 1.2 % | 0.428 |
| S01 | ACT06 | MCO:76; ISC:4 | 90.0 % | 0.0 % | 0.286 |
| S01 | ACT09 | ISC:43; MCO:37 | 50.8 % | 0.0 % | 0.996 |
| S01 | ACT12 | MCO:49; ODC:17; DAS:11; DT:1; ISC:1; TX_REG:1 | 40.8 % | 2.5 % | 1.539 |
| S02 | ACT02 | DEL:45; ISC:11; DOS:10; OP:9; TX_REG:3; MCO:2 | 37.5 % | 5.0 % | 1.901 |
| S02 | ACT04 | DAS:76; MCO:4 | 91.7 % | 0.0 % | 0.286 |
| S02 | ACT05 | DAS:66; MCO:9; ISC:3; DOS:2 | 71.7 % | 0.0 % | 0.894 |
| S02 | ACT11 | DAS:74; MCO:4; OP:1; DOS:1 | 86.7 % | 0.0 % | 0.478 |
| S03 | ACT06 | MCO:52; ISC:28 | 51.7 % | 0.0 % | 0.934 |
| S03 | ACT07 | DAS:53; MCO:27 | 55.8 % | 0.0 % | 0.922 |
| S03 | ACT09 | MCO:51; ISC:29 | 49.2 % | 0.0 % | 0.945 |
| S03 | ACT13 | ODC:53; MCO:25; OP:2 | 51.7 % | 3.8 % | 1.051 |
| S04 | ACT06 | MCO:44; DAS:36 | 51.7 % | 0.0 % | 0.993 |
| S04 | ACT11 | DAS:77; MCO:3 | 92.5 % | 0.0 % | 0.231 |
| S04 | ACT17 | ISC:35; MCO:23; DAS:22 | 34.2 % | 1.2 % | 1.551 |
| S04 | ACT18 | ODC:35; MCO:33; DAS:8; OP:4 | 35.0 % | 1.2 % | 1.597 |
| S05 | ACT01 | OP:33; DOS:26; ODC:16; DAS:3; MCO:1; ISC:1 | 32.5 % | 0.0 % | 1.854 |
| S05 | ACT06 | MCO:65; DAS:8; ISC:7 | 69.2 % | 0.0 % | 0.883 |
| S05 | ACT09 | MCO:54; ISC:22; DAS:3; OP:1 | 54.2 % | 0.0 % | 1.152 |
| S05 | ACT15 | ODC:80 | 100.0 % | 0.0 % | -0.000 |
| S06 | ACT03 | ISC:43; DAS:21; DOS:7; MCO:6; OP:3 | 35.8 % | 0.0 % | 1.753 |
| S06 | ACT04 | DAS:69; MCO:10; ISC:1 | 75.0 % | 0.0 % | 0.638 |
| S06 | ACT05 | DAS:61; MCO:17; ISC:2 | 60.0 % | 0.0 % | 0.906 |
| S06 | ACT12 | MCO:41; ISC:19; DAS:12; ODC:4; TX_REG:1; DT:1; DOS:1; OP:1 | 38.3 % | 27.5 % | 1.930 |
| S06 | ACT13 | ODC:57; MCO:15; OP:5; DAS:3 | 54.2 % | 0.0 % | 1.229 |
| S07 | ACT10 | DAS:80 | 100.0 % | 0.0 % | -0.000 |
| S07 | ACT11 | DAS:66; DOS:10; MCO:2; ODC:2 | 68.3 % | 1.2 % | 0.870 |
| S07 | ACT14 | OP:34; DAS:19; MCO:12; ODC:12; DT:3 | 23.3 % | 2.5 % | 2.016 |
| S07 | ACT19 | OP:36; DAS:20; MCO:12; ODC:5; DT:4; ISC:2; NEW_AUTHORITY:1 | 25.0 % | 3.8 % | 2.107 |
| S08 | ACT08 | DAS:48; MCO:32 | 48.3 % | 0.0 % | 0.971 |
| S08 | ACT14 | MCO:43; OP:14; ODC:11; DAS:10; DT:2 | 32.5 % | 1.2 % | 1.823 |
| S08 | ACT15 | ODC:78; OP:1; DT:1 | 95.0 % | 0.0 % | 0.194 |
| S08 | ACT16 | MCO:76; DAS:4 | 91.7 % | 0.0 % | 0.286 |
| S09 | ACT15 | ODC:79; MCO:1 | 97.5 % | 0.0 % | 0.097 |
| S09 | ACT18 | MCO:63; DAS:17 | 62.5 % | 1.2 % | 0.746 |
| S09 | ACT19 | OP:32; MCO:32; ODC:7; DAS:5; ISC:4 | 35.0 % | 11.2 % | 1.831 |
| S09 | ACT20 | MCO:65; DAS:14; ODC:1 | 67.5 % | 0.0 % | 0.762 |
| S10 | ACT01 | ODC:63; DAS:7; DOS:5; OP:4; MCO:1 | 61.7 % | 0.0 % | 1.124 |
| S10 | ACT14 | ODC:70; OP:6; MCO:3; DOS:1 | 77.5 % | 1.2 % | 0.705 |
| S10 | ACT15 | ODC:80 | 100.0 % | 0.0 % | -0.000 |
| S10 | ACT16 | MCO:59; DAS:21 | 60.8 % | 2.5 % | 0.830 |
| S10 | ACT20 | ODC:50; MCO:26; DAS:4 | 50.0 % | 0.0 % | 1.167 |

Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):

| Escenario | DAS | ISC | MCO | ODC |
|---|---|---|---|---|
| S01 | 61.0 % | 60.0 % | 62.0 % | 63.0 % |
| S02 | 65.0 % | 61.3 % | 57.5 % | 56.2 % |
| S03 | 48.8 % | 43.8 % | 47.5 % | 43.8 % |
| S04 | 51.2 % | 67.5 % | 56.2 % | 45.0 % |
| S05 | 52.5 % | 62.5 % | 63.7 % | 66.2 % |
| S06 | 64.0 % | 58.0 % | 54.0 % | 57.0 % |
| S07 | 55.0 % | 52.5 % | 62.5 % | 45.0 % |
| S08 | 67.5 % | 76.2 % | 73.8 % | 62.5 % |
| S09 | 67.5 % | 71.2 % | 71.2 % | 65.0 % |
| S10 | 65.0 % | 66.0 % | 72.0 % | 71.0 % |

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
| S01 | 62.0 % | [0.578, 0.660] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 36.0 % | n/d |
| S02 | 71.9 % | [0.631, 0.796] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 57.5 % | n/d |
| S03 | 52.1 % | [0.465, 0.579] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 17.5 % | n/d |
| S04 | 53.3 % | [0.485, 0.583] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 27.5 % | n/d |
| S05 | 64.0 % | [0.573, 0.702] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 45.0 % | n/d |
| S06 | 52.7 % | [0.480, 0.570] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 26.0 % | n/d |
| S07 | 54.2 % | [0.506, 0.579] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 37.5 % | n/d |
| S08 | 66.9 % | [0.633, 0.706] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 46.2 % | n/d |
| S09 | 65.6 % | [0.592, 0.725] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 42.5 % | n/d |
| S10 | 70.0 % | [0.660, 0.740] | n/d | [n/d, n/d] | n/d | [n/d, n/d] | 48.0 % | n/d |

Global: acuerdo 61.3 % → n/d; CONVERGENCE_DELTA = n/d (IC95 bootstrap sobre corridas [n/d, n/d]). Mayor consenso no implica mayor corrección.

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

- AMBIGUITY_RATE antes: 1.6 %; después: n/d
- Árbitro, veredicto AMBIGUOUS: n/d
- PROPOSED_NEW_AUTHORITY como A: 0.1 % de las decisiones de agentes

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

Media por actividad: 0.987 bits antes y n/d bits después. Entropía baja indica asignación estable; alta, sensible a la interpretación. No es una medida de corrección.

## 12. Cambios de posición

POSITION_CHANGE_RATE global: n/d.

| Agente | Escenario | n | Cambio de A | MAINTAIN | MODIFY | AMBIGUOUS | Declaración incoherente |
|---|---|---|---|---|---|---|---|

Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).

| Agente | P propia | P neutral | Diferencia | n |
|---|---|---|---|---|
| DAS | 36.5 % | 27.4 % | 0.091 | 860 |
| ISC | 10.1 % | 8.1 % | 0.020 | 860 |
| MCO | 35.3 % | 33.8 % | 0.015 | 860 |
| ODC | 24.4 % | 20.2 % | 0.042 | 860 |

## 13. Evidencia más utilizada

- EVIDENCE_VALIDITY_RATE: 99.5 % de 11337 citas
- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): 0.0 %
- A sin evidencia institucional válida: 0.8 %
- Violación de jerarquía (DOCUMENTADO con fuente no institucional): 0.7 %
- Cita textual verificada en la fuente: 98.1 % de 11337; en afirmaciones DOCUMENTADO: 98.3 % de 6887
- Proporción de citas INFERIDO: 4.0 %
La verificación textual prueba que el fragmento existe en la fuente citada, no que nombre la actividad; la pertinencia se audita con citation_audit.py.

| source_id | kind | total | phase1 | phase2 |
|---|---|---|---|---|
| NIST_CM_01 | externa | 1255 | 1255 | 0 |
| U01_2_8 | institucional | 746 | 746 | 0 |
| U12_2_1 | institucional | 569 | 569 | 0 |
| U13_2_5 | institucional | 529 | 529 | 0 |
| U12_2_2 | institucional | 508 | 508 | 0 |
| U13_2_6 | institucional | 423 | 423 | 0 |
| U10_2_1 | institucional | 387 | 387 | 0 |
| U01_2_4 | institucional | 343 | 343 | 0 |
| NIST_OT_01 | externa | 339 | 339 | 0 |
| ENISA_CHG_02 | externa | 330 | 330 | 0 |
| U08_2_3 | institucional | 301 | 301 | 0 |
| U12_2_4 | institucional | 297 | 297 | 0 |
| NIST_CM_02 | externa | 273 | 273 | 0 |
| U01_2_6 | institucional | 269 | 269 | 0 |
| U10_2_2 | institucional | 223 | 223 | 0 |
| U13_2_1 | institucional | 216 | 216 | 0 |
| ERCOT_04 | externa | 215 | 215 | 0 |
| ENISA_CHG_01 | externa | 212 | 212 | 0 |
| PJM_04 | externa | 204 | 204 | 0 |
| ERCOT_03 | externa | 202 | 202 | 0 |

## 14. Comparación post hoc con REFERENCE_RACI

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la correspondencia de columnas indicada en el README (Origen, GT*, AC).

| activity_id | activity | REFERENCE_A | match_individual_especializados_f1 | match_neutral_f1 | match_post_debate_f2 | match_control_sin_debate_f2c | match_arbitro_f3 |
|---|---|---|---|---|---|---|---|
| ACT01 | Definir el requisito y el alcance del cambio | DAS | 6.2 % | 5.0 % | n/d | n/d | n/d |
| ACT02 | Certificar los datos de la instalación (configuración física y parámetros) | ORIGIN | 45.6 % | 50.0 % | n/d | n/d | n/d |
| ACT03 | Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación) | DAS | 26.2 % | 30.0 % | n/d | n/d | n/d |
| ACT04 | Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros) | DAS | 90.8 % | 93.3 % | n/d | n/d | n/d |
| ACT05 | Revisar la calidad topológica y de nomenclatura del modelo construido | ISC | 3.1 % | 5.0 % | n/d | n/d | n/d |
| ACT06 | Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones | ISC | 12.2 % | 13.8 % | n/d | n/d | n/d |
| ACT07 | Unificar modelo y adquisición en la base integrada | ISC | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT08 | Preparar el paquete de implementación | ISC | 0.0 % | 0.0 % | n/d | n/d | n/d |
| ACT09 | Aprobar las pruebas FAT/SAT y de integración | ISC | 39.2 % | 36.7 % | n/d | n/d | n/d |
| ACT10 | Administrar y actualizar los aplicativos EMS | DAS | 100.0 % | 90.0 % | n/d | n/d | n/d |
| ACT11 | Validar el estimador de estado, el flujo de potencia y demás aplicaciones | DAS | 90.4 % | 86.7 % | n/d | n/d | n/d |
| ACT12 | Verificar la correspondencia de mímicos y modelo con la instalación física | ORIGIN | 3.1 % | 2.5 % | n/d | n/d | n/d |
| ACT13 | Aceptar mímicos, alarmas y el uso operativo | ODC | 68.8 % | 67.5 % | n/d | n/d | n/d |
| ACT14 | Autorizar la liberación de la versión a producción | NEW_AUTHORITY | 0.0 % | 1.7 % | n/d | n/d | n/d |
| ACT15 | Habilitar o suspender la ventana de intervención en tiempo real | ODC | 99.1 % | 100.0 % | n/d | n/d | n/d |
| ACT16 | Ejecutar el respaldo y la carga en producción | MCO | 84.4 % | 75.0 % | n/d | n/d | n/d |
| ACT17 | Mantener el registro técnico de configuración | ISC | 43.8 % | 60.0 % | n/d | n/d | n/d |
| ACT18 | Verificar el sistema después de la actualización y cerrar el cambio | DAS | 15.6 % | 10.0 % | n/d | n/d | n/d |
| ACT19 | Aprobar los criterios de reversión y su delegación | NEW_AUTHORITY | 0.6 % | 5.0 % | n/d | n/d | n/d |
| ACT20 | Ejecutar la reversión | MCO | 56.9 % | 60.0 % | n/d | n/d | n/d |

### Matriz RACI modal

Matrices completas por grupo (A, R, C, I por unidad, con frecuencia y celdas inestables) en `modal_raci.md` y `modal_raci.csv`. Resumen de la comparación celda a celda:

| Grupo | Celdas idénticas | Celdas A/R idénticas | A recuperada | Celdas inestables |
|---|---|---|---|---|
| especializados_f1 | 17.9 % | 75.0 % | 35.0 % | 58 de 140 |
| neutral_f1 | 17.1 % | 75.0 % | 40.0 % | 58 de 140 |

## 15. Limitaciones

- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de perspectivas es inducida por el prompt, no por conocimiento independiente.
- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad observada puede reflejar el marco institucional o la lectura del modelo.
- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede orientar la respuesta aunque no revele la asignación.
- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.
- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).
- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.
- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye la del servicio.
