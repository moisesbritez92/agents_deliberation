# Auditoría de pertinencia de citas: smoke2

## 1. Control determinista (todas las citas de agentes, fases 1-2)

- Citas: 116; institucionales: 73; DOCUMENTADO institucionales: 72
- DOCUMENTADO con fuente no institucional: 0.0 % [0.0, 3.2] (n = 116)
- Cita institucional cuya unidad no figura en la asignación (A, R, C ni I): 0.0 % [0.0, 5.0] (n = 73)
- DOCUMENTADO cuya unidad citada no es A ni R: 4.2 % [1.4, 11.5] (n = 72)

El control determinista es un indicio, no un juicio: una cita de otra unidad puede justificar legítimamente que esa unidad no es la responsable.

## 2. Juez LLM ciego (gemini-3.1-pro-preview), muestra aleatoria estratificada

- SUPPORTS: 73.3 % [61.0, 82.9] (n = 60)
- PARTIAL: 13.3 % [6.9, 24.2] (n = 60)
- DOES_NOT_SUPPORT: 13.3 % [6.9, 24.2] (n = 60)
- Tipo de afirmación correcto: 78.3 % [66.4, 86.9] (n = 60)

| Grupo | Nivel | n | SUPPORTS | DOES_NOT_SUPPORT | Tipo correcto |
|---|---|---|---|---|---|
| tipo declarado | BUENA_PRACTICA | 22 | 95 % | 5 % | 100 % |
| tipo declarado | DOCUMENTADO | 37 | 62 % | 19 % | 65 % |
| tipo declarado | INFERIDO | 1 | 0 % | 0 % | 100 % |
| agente | DAS | 10 | 70 % | 10 % | 70 % |
| agente | ISC | 12 | 75 % | 8 % | 83 % |
| agente | MCO | 9 | 67 % | 11 % | 67 % |
| agente | NEUTRAL | 11 | 64 % | 27 % | 73 % |
| agente | ODC | 18 | 83 % | 11 % | 89 % |
| fuente | externa | 22 | 95 % | 5 % | 100 % |
| fuente | institucional | 38 | 61 % | 18 % | 66 % |

Nota: la muestra es proporcional por tipo declarado; las tasas por agente son descriptivas.
