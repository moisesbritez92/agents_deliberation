# Réplica con `gpt-6-luna` frente a los criterios preespecificados

Criterios fijados en BITACORA.md (28/09/2026, antes de ejecutar). Repeticiones 1-5; 50 corridas por condición. La regla de clasificación reproduce exactamente la clasificación publicada de Gemini (verificado).

| Hipótesis | Resultado | ¿Se cumple? |
|---|---|---|
| H1 efecto de la deliberación | 0.128 [0.108; 0.149] (estratificado); control 0.003 [-0.011; 0.018]; positivo en 10/10 escenarios | sí |
| H2 cambios hacia la mayoría (≥ 70 %) | 92.7 % de 82 cambios | sí |
| H3a orden inverso con nombres, DAS (|Δ| < 5 pp o IC con 0) | 60.0 % → 59.1 %, Δ -0.9 pp [-4.1; +2.2] | sí |
| H3b saliencia sin nombres: DAS sube en la cruzada | 39.7 % → 49.7 %, Δ +10.0 pp [+6.6; +13.5] | |
| H3b saliencia sin nombres: MCO sube en la anónima | 18.9 % → 26.1 %, Δ +7.3 pp [+4.5; +10.3] | sí |
| H4a robustas con igual A (≥ 4/5) | 5/5: ACT04, ACT05, ACT10, ACT11, ACT15 | sí |
| H4b no robustas siguen no robustas (≥ 7/9) | 8/9 | sí |
| H4c acuerdo de clase entre modelos (descriptivo) | κ = 0.30; misma A modal tras deliberar en 15/20 | — |
| H5 fragmentos literales (≥ 95 %) | 99.6 % | sí |

## Clasificación por actividad

| Actividad | Gemini: clase | Gemini: A modal F2 | Luna: clase | Luna: A modal F2 |
|---|---|---|---|---|
| ACT01 | Sensible al orden | ODC (99 %) | Sensible al orden | DAS (65 %) |
| ACT02 | Sensible al orden | DT (51 %) | Depende de la denominación | DT (100 %) |
| ACT03 | Sensible al orden | DOS (48 %) | Robusta | DAS (100 %) |
| ACT04 | Robusta | DAS (100 %) | Robusta | DAS (100 %) |
| ACT05 | Robusta | DAS (87 %) | Robusta | DAS (100 %) |
| ACT06 | Sensible al orden | DAS (62 %) | Sensible al orden | DAS (68 %) |
| ACT07 | Depende de la denominación | DAS (100 %) | Robusta | DAS (75 %) |
| ACT08 | Depende de la denominación | DAS (100 %) | Disputada DAS/MCO | DAS (100 %) |
| ACT09 | Depende de la denominación | ISC (97 %) | Robusta | ISC (92 %) |
| ACT10 | Robusta | DAS (100 %) | Robusta | DAS (100 %) |
| ACT11 | Robusta | DAS (85 %) | Robusta | DAS (100 %) |
| ACT12 | Sensible al orden | ODC (51 %) | Sensible al orden | MCO (42 %) |
| ACT13 | Sensible al orden | ODC (86 %) | Depende de la denominación | ODC (100 %) |
| ACT14 | Depende de la denominación | OP (60 %) | Sensible al orden | DAS (75 %) |
| ACT15 | Robusta | ODC (100 %) | Robusta | ODC (100 %) |
| ACT16 | Disputada DAS/MCO | DAS (84 %) | Sensible al orden | DAS (72 %) |
| ACT17 | Depende de la denominación | DAS (85 %) | Depende de la denominación | DAS (95 %) |
| ACT18 | Sensible al orden | DAS (59 %) | Depende de la denominación | DAS (100 %) |
| ACT19 | Sensible al orden | OP (71 %) | Sensible al orden | NEW_AUTHORITY (80 %) |
| ACT20 | Sensible al orden | DAS (51 %) | Disputada DAS/MCO | DAS (100 %) |

## Efecto por escenario (Luna)

| Escenario | Efecto |
|---|---|
| S01 | 0.233 |
| S02 | 0.025 |
| S03 | 0.225 |
| S04 | 0.075 |
| S05 | 0.142 |
| S06 | 0.193 |
| S07 | 0.058 |
| S08 | 0.092 |
| S09 | 0.125 |
| S10 | 0.113 |

## Otras métricas de `luna_pilot` (summary.csv)

- AGREEMENT_BEFORE: 0.7946666666666666
- AGREEMENT_AFTER: 0.9256666666666666
- AGREEMENT_CONTROL: 0.7975
- POSITION_CHANGE_RATE: 0.09534883720930232
- POSITION_CHANGE_RATE_CONTROL: 0.05581395348837209
- ARBITER_AMBIGUOUS_RATE: 0.8465116279069768
- EVIDENCE_VALIDITY_RATE: 0.9995092024539878
- estimated_cost_usd: 1.7199
