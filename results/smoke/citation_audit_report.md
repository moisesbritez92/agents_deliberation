# Auditoría de pertinencia de citas: smoke

## 1. Control determinista (todas las citas de agentes, fases 1-2)

- Citas: 124; institucionales: 78; DOCUMENTADO institucionales: 77
- DOCUMENTADO con fuente no institucional: 0.0 % [0.0, 3.0] (n = 124)
- Cita institucional cuya unidad no figura en la asignación (A, R, C ni I): 2.6 % [0.7, 8.9] (n = 78)
- DOCUMENTADO cuya unidad citada no es A ni R: 9.1 % [4.5, 17.6] (n = 77)

El control determinista es un indicio, no un juicio: una cita de otra unidad puede justificar legítimamente que esa unidad no es la responsable.

## 2. Juez LLM ciego (gemini-3.1-pro-preview), muestra aleatoria estratificada

- SUPPORTS: 66.7 % [54.1, 77.3] (n = 60)
- PARTIAL: 16.7 % [9.3, 28.0] (n = 60)
- DOES_NOT_SUPPORT: 16.7 % [9.3, 28.0] (n = 60)
- Tipo de afirmación correcto: 71.7 % [59.2, 81.5] (n = 60)

| Grupo | Nivel | n | SUPPORTS | DOES_NOT_SUPPORT | Tipo correcto |
|---|---|---|---|---|---|
| tipo declarado | BUENA_PRACTICA | 22 | 100 % | 0 % | 100 % |
| tipo declarado | DOCUMENTADO | 37 | 49 % | 24 % | 57 % |
| tipo declarado | INFERIDO | 1 | 0 % | 100 % | 0 % |
| agente | DAS | 10 | 60 % | 10 % | 70 % |
| agente | ISC | 15 | 80 % | 20 % | 80 % |
| agente | MCO | 17 | 65 % | 24 % | 71 % |
| agente | NEUTRAL | 6 | 50 % | 17 % | 50 % |
| agente | ODC | 12 | 67 % | 8 % | 75 % |
| fuente | externa | 22 | 100 % | 0 % | 100 % |
| fuente | institucional | 38 | 47 % | 26 % | 55 % |

Nota: la muestra es proporcional por tipo declarado; las tasas por agente son descriptivas.

## 3. Auditoría humana (doble codificación ciega)

Planillas generadas, todavía sin codificar.
