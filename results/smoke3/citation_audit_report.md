# Auditoría de pertinencia de citas: smoke3

## 1. Control determinista (todas las citas de agentes, fases 1-2)

- Citas: 167; institucionales: 106; DOCUMENTADO institucionales: 104
- DOCUMENTADO con fuente no institucional: 0.0 % [0.0, 2.2] (n = 167)
- Cita institucional cuya unidad no figura en la asignación (A, R, C ni I): 2.8 % [1.0, 8.0] (n = 106)
- DOCUMENTADO cuya unidad citada no es A ni R: 4.8 % [2.1, 10.8] (n = 104)

El control determinista es un indicio, no un juicio: una cita de otra unidad puede justificar legítimamente que esa unidad no es la responsable.

## 2. Juez LLM ciego (gemini-3.1-pro-preview), muestra aleatoria estratificada

- SUPPORTS: 41.7 % [30.1, 54.3] (n = 60)
- PARTIAL: 31.7 % [21.3, 44.2] (n = 60)
- DOES_NOT_SUPPORT: 26.7 % [17.1, 39.0] (n = 60)
- Tipo de afirmación correcto: 53.3 % [40.9, 65.4] (n = 60)

| Grupo | Nivel | n | SUPPORTS | DOES_NOT_SUPPORT | Tipo correcto |
|---|---|---|---|---|---|
| tipo declarado | BUENA_PRACTICA | 22 | 59 % | 23 % | 77 % |
| tipo declarado | DOCUMENTADO | 37 | 30 % | 30 % | 38 % |
| tipo declarado | INFERIDO | 1 | 100 % | 0 % | 100 % |
| agente | DAS | 13 | 38 % | 23 % | 46 % |
| agente | ISC | 14 | 50 % | 29 % | 50 % |
| agente | MCO | 14 | 29 % | 14 % | 64 % |
| agente | NEUTRAL | 6 | 50 % | 33 % | 50 % |
| agente | ODC | 13 | 46 % | 38 % | 54 % |
| fuente | externa | 22 | 59 % | 23 % | 77 % |
| fuente | institucional | 38 | 32 % | 29 % | 39 % |

Nota: la muestra es proporcional por tipo declarado; las tasas por agente son descriptivas.
