# Matriz RACI modal

Cada celda muestra el rol más frecuente de la unidad en la actividad y su frecuencia sobre todas las decisiones del grupo, acumulando los escenarios en que aparece la actividad. '?' marca una celda inestable (rol modal < 60 %); '·' indica sin rol. Rol por decisión: A/R > A > R > C > I. La matriz modal describe lo que el modelo produce con este corpus; no es la asignación correcta. El desglose por escenario está en `modal_raci.csv`.

Unidades: DAS, ISC y MCO agrupan sus secciones; TX_REG = departamentos regionales de Transmisión; NEW_AUTHORITY = PROPOSED_NEW_AUTHORITY; OTHER = unidad no incluida en el corpus.

## Especializados, fase 1 (independiente)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DEL | OP | DIV_SIST_COM | n |
|---|---|---|---|---|---|---|---|---|---|---|
| ACT02 Certificar los datos de la instalación (configur | · | C 50% ? | · | I 50% ? | R 75% | A 50% ? | C 50% ? | · | · | 4 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · | · | I 100% | · | · | C 100% | · | · | 4 |
| ACT06 Configurar la adquisición, la correspondencia se | C 50% ? | A/R 50% ? | · | I 100% | · | · | · | · | · | 4 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 75% | A/R 75% | · | C 75% | · | · | · | · | · | 4 |
| ACT12 Verificar la correspondencia de mímicos y modelo | R 50% ? | · 50% ? | · | A 50% ? | · | C 50% ? | · | I 50% ? | · | 4 |

Celdas inestables: 11 de 45.

## Neutral, fase 1

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DEL | OP | DIV_SIST_COM | n |
|---|---|---|---|---|---|---|---|---|---|---|
| ACT02 Certificar los datos de la instalación (configur | · | · | · | · | R 100% | A 100% | C 100% | I 100% | · | 1 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · | · | · | · | · | C 100% | I 100% | · | 1 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 100% | · | C 100% | I 100% | · | · | · | · | C 100% | 1 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | I 100% | A/R 100% | · | C 100% | · | · | · | · | · | 1 |
| ACT12 Verificar la correspondencia de mímicos y modelo | R 100% | · | · | A 100% | C 100% | · | · | I 100% | · | 1 |

Celdas inestables: 0 de 45.

## Especializados, fase 2 (tras deliberación)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DEL | OP | DIV_SIST_COM | n |
|---|---|---|---|---|---|---|---|---|---|---|
| ACT02 Certificar los datos de la instalación (configur | · | C 50% ? | · | · | R 100% | A 100% | C 75% | I 50% ? | · | 4 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · | · | I 100% | · | · | C 100% | · | · | 4 |
| ACT06 Configurar la adquisición, la correspondencia se | R 50% ? | A/R 50% ? | · | I 100% | · | · | · | · | · | 4 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 75% | A/R 100% | · | C 100% | · | · | · | I 50% ? | · | 4 |
| ACT12 Verificar la correspondencia de mímicos y modelo | R 50% ? | R 50% ? | · | A 100% | · | C 100% | · | I 75% | · | 4 |

Celdas inestables: 7 de 45.

## Especializados, fase 2c (control sin deliberación)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DEL | OP | DIV_SIST_COM | n |
|---|---|---|---|---|---|---|---|---|---|---|
| ACT02 Certificar los datos de la instalación (configur | · | C 50% ? | · | I 50% ? | R 75% | A 50% ? | C 50% ? | · | · | 4 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · | · | I 100% | · | · | C 100% | · | · | 4 |
| ACT06 Configurar la adquisición, la correspondencia se | C 50% ? | A/R 50% ? | · | I 100% | · | · | · | · | · | 4 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 75% | A/R 75% | · | C 75% | · | · | · | · | · | 4 |
| ACT12 Verificar la correspondencia de mímicos y modelo | R 50% ? | · 50% ? | · | A 50% ? | · | C 50% ? | · | I 50% ? | · | 4 |

Celdas inestables: 11 de 45.

## Árbitro, fase 3

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DEL | OP | DIV_SIST_COM | n |
|---|---|---|---|---|---|---|---|---|---|---|
| ACT02 Certificar los datos de la instalación (configur | · | C 100% | · | · | R 100% | A 100% | C 100% | I 100% | · | 1 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · | · | I 100% | · | · | C 100% | · | · | 1 |
| ACT06 Configurar la adquisición, la correspondencia se | R 100% | A/R 100% | · | I 100% | · | · | · | · | · | 1 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 100% | A/R 100% | · | C 100% | · | · | · | I 100% | · | 1 |
| ACT12 Verificar la correspondencia de mímicos y modelo | R 100% | R 100% | · | A 100% | · | C 100% | · | I 100% | · | 1 |

Celdas inestables: 0 de 45.

## Comparación celda a celda con REFERENCE_RACI (post hoc)

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Columnas agrupadas como en el artículo: GT_SUPPORT = DOS, DEL, DEN, DDR; ORIGIN = TX_REG, DT, OTHER; NEW_AUTHORITY = Autoridad de Cambio. DEL y DOS se cuentan en GT_SUPPORT aunque el artículo también los admite como origen de parámetros (aproximación).

Formato: `=` coincide con la referencia; `≠ X (ref Y)` difiere, con el rol modal X y el de la referencia Y.

| Grupo | Celdas idénticas | Celdas A/R idénticas | A de la referencia recuperada | Celdas inestables |
|---|---|---|---|---|
| Especializados, fase 1 (independiente) | 34.3 % | 91.4 % | 80.0 % | 8 de 35 |
| Neutral, fase 1 | 22.9 % | 85.7 % | 60.0 % | 0 de 35 |
| Especializados, fase 2 (tras deliberación) | 31.4 % | 85.7 % | 80.0 % | 5 de 35 |
| Especializados, fase 2c (control sin deliberación) | 34.3 % | 91.4 % | 80.0 % | 8 de 35 |
| Árbitro, fase 3 | 31.4 % | 85.7 % | 80.0 % | 0 de 35 |

Celdas idénticas: mismo rol exacto. Celdas A/R idénticas: mismo rol ejecutivo (A/R, A, R), tratando C, I y sin rol como una misma clase. A recuperada: proporción de celdas A de la referencia en las que el rol modal incluye A.

### Especializados, fase 1 (independiente) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | = ? | ≠ - (ref I) | ≠ I (ref C) ? | = ? | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) | ≠ I (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | = ? | = ? | ≠ - (ref R) | = | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | = ? | ≠ - (ref C) ? | ≠ - (ref I) | ≠ A (ref C) ? | ≠ - (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |

### Neutral, fase 1 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref C) | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ C (ref R) | = | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | ≠ I (ref C) | = | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | = | ≠ - (ref C) | ≠ - (ref I) | ≠ A (ref C) | ≠ - (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |

### Especializados, fase 2 (tras deliberación) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | = ? | ≠ - (ref I) | ≠ - (ref C) | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) | ≠ I (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ R (ref C) ? | = ? | ≠ - (ref R) | = | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | = ? | ≠ R (ref C) ? | ≠ - (ref I) | ≠ A (ref C) | ≠ - (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |

### Especializados, fase 2c (control sin deliberación) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | = ? | ≠ - (ref I) | ≠ I (ref C) ? | = ? | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) | ≠ I (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | = ? | = ? | ≠ - (ref R) | = | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | = ? | ≠ - (ref C) ? | ≠ - (ref I) | ≠ A (ref C) ? | ≠ - (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |

### Árbitro, fase 3 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | = | ≠ - (ref I) | ≠ - (ref C) | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) | ≠ I (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ R (ref C) | = | ≠ - (ref R) | = | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | = | ≠ R (ref C) | ≠ - (ref I) | ≠ A (ref C) | ≠ - (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |

### REFERENCE_RACI (artículo), en las mismas columnas

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT02 Certificar los datos de la instalación ( | C | C | I | C | C | A/R | I |
| ACT04 Construir o actualizar el modelo eléctri | A/R | C | C | C | C | C | I |
| ACT06 Configurar la adquisición, la correspond | C | A/R | R | I | I | C | I |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | C | A/R | C | C | C | C | I |
| ACT12 Verificar la correspondencia de mímicos  | R | C | I | C | I | A/R | I |
