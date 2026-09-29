# Informe del smoke test

Fecha: 24/09/2026. Modelo `gemini-3.1-flash-lite`, thinking_level `medium`. Escenario S01 (nueva subestación de 220 kV), 1 repetición, semilla 1001. Métricas completas en `final_report.md`.

## Verificaciones exigidas

| Verificación | Resultado |
|---|---|
| JSON válido | 10/10 llamadas, al primer intento |
| Actividades completas (5 por respuesta, sin duplicados) | 10/10 |
| Referencias existentes (EVIDENCE_VALIDITY_RATE) | 100 %. Ningún `source_id` inventado |
| Unidades fuera de la lista admitida | 0 |
| Ningún agente recibió REFERENCE_RACI | Control de contaminación OK en 10/10 peticiones; `experiment.py` no lee `posthoc/`. Peticiones completas en `prompt_samples/` |
| Filtración de identidad en fases 2-3 | No se encontraron menciones a la propia perspectiva |
| Favoritismo automático hacia la unidad representada | No sistemático, con n = 5 decisiones por agente (ver abajo) |

## Observaciones sobre el favoritismo (n = 5, solo indicativo)

- DAS asigna la A a DAS solo en construir el modelo (ACT04), igual que los otros cinco participantes. Asigna FAT/SAT y adquisición a ISC.
- ODC se asigna la verificación de mímicos (ACT12), igual que NEUTRAL y MCO.
- MCO se asigna la adquisición (ACT06); en la fase 2 lo corrige a ISC.
- ISC se asigna la certificación de datos de la instalación (ACT02) y la verificación de mímicos (ACT12), con citas débiles: `ISC_2_1`, marcado como DOCUMENTADO, no menciona la certificación de datos. Es el único indicio de sesgo hacia la propia unidad (HOME_BIAS_ISC = 0,6 con n = 5). Hay que vigilarlo en el piloto.

## Comportamiento de las fases

- Acuerdo entre especializados: de 63 % a 87 %; consenso estricto: de 2/5 a 4/5 actividades.
- El árbitro declaró AMBIGUOUS en ACT02 (Transmisión frente a ISC) y ACT12 (ODC frente a DAS), con la decisión institucional que falta. Resolvió ACT04, ACT06 y ACT09 por consenso pleno.
- Ningún agente usó PROPOSED_NEW_AUTHORITY en este escenario.

## Hallazgos técnicos corregidos durante el smoke test

1. El primer intento (`results/smoke_intento1_503/`, conservado) sufrió errores 503 (demanda alta del servicio) en 4 de los 5 agentes, y la corrida continuó con un solo agente. Se corrigió: los errores de API tienen ahora 8 reintentos con espera exponencial, y la corrida es todo o nada (sin los 5 + 4 agentes no se llama al árbitro; `--resume` la repite). El análisis solo usa corridas completas.
2. Con la misma semilla, la respuesta de MCO en la fase 1 fue idéntica en ambos intentos: la semilla es efectiva.
3. `analysis.py` no contaba las citas del árbitro (`disagreement_evidence`); corregido.

## Limitación detectada

La validez de las citas se verifica por existencia del identificador, no por pertinencia. Hay citas existentes clasificadas como DOCUMENTADO cuyo texto no respalda lo afirmado (ejemplo de ISC arriba). Para el artículo convendría una auditoría manual de una muestra aleatoria de citas del piloto (p. ej., 100), con doble codificación.

## Auditoría de pertinencia (añadida tras el smoke test)

Se implementó `citation_audit.py` (ver README) y se aplicó a las 124 citas de agentes de esta corrida:

- Control determinista: 0 % de DOCUMENTADO con fuente externa; en el 9 % de las citas DOCUMENTADO, la unidad citada no es A ni R.
- Juez ciego `gemini-3.1-pro-preview`, muestra de 60 citas: SUPPORTS 67 % [54, 77], PARTIAL 17 %, DOES_NOT_SUPPORT 17 % [9, 28]; tipo de afirmación correcto 72 %. Informe completo: `citation_audit_report.md`; veredictos: `judge_results.csv`.
- Los rechazos se concentran en ACT02 (certificar datos) y ACT12 (verificar mímicos), que carecen de numeral expreso en las fichas y que el árbitro declaró AMBIGUOUS. Los agentes tienden a etiquetar como DOCUMENTADO lo que es INFERIDO: sobreestiman el respaldo literal justamente donde el marco institucional calla.
- Validación humana del juez: planillas de 20 ítems generadas (`audit_sheet_coder1.csv`, `audit_sheet_coder2.csv`), pendientes de codificar.

## Coste y proyección

- Corrida: 236 238 tokens de entrada y 27 385 de salida (incluidos 9 850 de razonamiento). Unos 19 000 tokens de entrada por llamada en la fase 1 y 28 000 en las fases 2-3.
- Coste con los precios provisionales de `config.py`: USD 0,10 por corrida. Piloto de 200 corridas: **unos USD 20** (≈ 47 M de tokens de entrada, 5,5 M de salida), más reintentos.
- No se registró caché implícita (`cached_content_token_count` vacío).
- Tiempo: unos 100 s por corrida en secuencia; con `--workers 4`, el piloto tardaría unas 1,5-2 h si el servicio no devuelve 503.
