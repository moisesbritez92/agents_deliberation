# Control de paráfrasis de las instrucciones frente a los criterios preespecificados

Criterios fijados en BITACORA.md (29/09/2026, antes de ejecutar). `gpt-6-luna`, repeticiones 1-3, 30 corridas por condición.

| Criterio | Paráfrasis | Original (mismas repeticiones) | ¿Se cumple? |
|---|---|---|---|
| P1 efecto de la deliberación | 0.074 [0.038; 0.111]; control 0.014 [-0.010; 0.040] | 0.131 [0.109; 0.151] | sí |
| P2 cambios hacia la mayoría (≥ 70 %) | 87.0 % de 54 | 94.0 % de 50 | sí |
| P3 cinco robustas con igual A (≥ 60 % en F1 y F2) | 5/5: ACT04, ACT05, ACT10, ACT11, ACT15 | 5/5 | sí |
| P4 misma A modal en casos estables (≥ 80 %) | 39/41 (95.1 %) | — | sí |
| P5 fragmentos literales (≥ 95 %) | 99.7 % | — | sí |

## Descriptivo (sin criterio)

| Métrica | Paráfrasis | Original |
|---|---|---|
| Acuerdo F1 | 79.2 % | 78.8 % |
| Acuerdo control 2c | 80.7 % | 79.3 % |
| Acuerdo F2 | 88.2 % | 92.9 % |
| Ambigüedad agentes F1 | 69.0 % | 69.8 % |
| Árbitro AMBIGUOUS | 80.6 % | 84.5 % |
| Autoridad nueva F1 | 5.6 % | 4.5 % |
| DAS como A, F1 | 56.9 % | 59.7 % |

## Casos estables cuya A modal cambia con la paráfrasis

- S10 ACT01: ODC (60.0 %) → DAS (53.3 %)
- S08 ACT14: DAS (60.0 %) → NEW_AUTHORITY (53.3 %)
