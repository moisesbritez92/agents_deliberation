# Auditoría de pertinencia de citas: pilot

## 1. Control determinista (todas las citas de agentes, fases 1-2)

- Citas: 28188; institucionales: 17331; DOCUMENTADO institucionales: 16507
- DOCUMENTADO con fuente no institucional: 1.2 % [1.1, 1.3] (n = 28188)
- Cita institucional cuya unidad no figura en la asignación (A, R, C ni I): 0.5 % [0.4, 0.7] (n = 17331)
- DOCUMENTADO cuya unidad citada no es A ni R: 5.5 % [5.2, 5.9] (n = 16507)

El control determinista es un indicio, no un juicio: una cita de otra unidad puede justificar legítimamente que esa unidad no es la responsable.

## 2. Juez LLM ciego (gemini-3.1-pro-preview), muestra aleatoria estratificada

- SUPPORTS: 40.3 % [36.5, 44.3] (n = 600)
- PARTIAL: 38.2 % [34.4, 42.1] (n = 600)
- DOES_NOT_SUPPORT: 21.5 % [18.4, 25.0] (n = 600)
- Tipo de afirmación correcto: 59.7 % [55.7, 63.5] (n = 600)

| Grupo | Nivel | n | SUPPORTS | DOES_NOT_SUPPORT | Tipo correcto |
|---|---|---|---|---|---|
| tipo declarado | BUENA_PRACTICA | 218 | 43 % | 19 % | 82 % |
| tipo declarado | DOCUMENTADO | 357 | 40 % | 23 % | 45 % |
| tipo declarado | INFERIDO | 25 | 24 % | 24 % | 72 % |
| agente | DAS | 137 | 34 % | 21 % | 56 % |
| agente | ISC | 147 | 41 % | 22 % | 63 % |
| agente | MCO | 139 | 42 % | 29 % | 56 % |
| agente | NEUTRAL | 54 | 46 % | 20 % | 65 % |
| agente | ODC | 123 | 41 % | 13 % | 61 % |
| fuente | externa | 225 | 42 % | 20 % | 80 % |
| fuente | institucional | 375 | 39 % | 22 % | 47 % |

Nota: la muestra es proporcional por tipo declarado; las tasas por agente son descriptivas.

## 3. Doble codificación ciega (codificadores LLM, no humanos)

- Codificadores: ASTRA (2.ª pasada) (`audit_sheet_coder1_astra_v2.csv`, 99 ítems codificados) y Opus 5.5 (`audit_sheet_coder2_opus5.5.csv`, 99 ítems codificados), sobre 99 ítems de la muestra.

| Par | Pertinencia (SUPPORTS/PARTIAL/DOES_NOT_SUPPORT) | Tipo de afirmación correcto |
|---|---|---|
| ASTRA (2.ª pasada) – Opus 5.5 | κ = 0.70, acuerdo simple 83 % (n = 99) | κ = 0.64, acuerdo simple 82 % (n = 99) |
| ASTRA (2.ª pasada) – juez | κ = 0.36, acuerdo simple 60 % (n = 99) | κ = 0.52, acuerdo simple 76 % (n = 99) |
| Opus 5.5 – juez | κ = 0.50, acuerdo simple 68 % (n = 99) | κ = 0.55, acuerdo simple 78 % (n = 99) |

- Juez frente al consenso de ambos codificadores (ítems con acuerdo): κ = 0.48 (n = 82). Con κ < 0,60, las tasas del juez no deben reportarse como medida validada.
- ASTRA (2.ª pasada): SUPPORTS 49.5 % [39.9, 59.2] (n = 99); DOES_NOT_SUPPORT 5.1 % [2.2, 11.3] (n = 99)
- Opus 5.5: SUPPORTS 41.4 % [32.2, 51.3] (n = 99); DOES_NOT_SUPPORT 12.1 % [7.1, 20.0] (n = 99)
- Juez sobre los mismos ítems: SUPPORTS 38.4 % [29.4, 48.2] (n = 99); DOES_NOT_SUPPORT 26.3 % [18.6, 35.7] (n = 99)
- Consenso de ambos codificadores: SUPPORTS 48.8 % [38.3, 59.4] (n = 82)
