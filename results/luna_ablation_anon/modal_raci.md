# Matriz RACI modal

Cada celda muestra el rol más frecuente de la unidad en la actividad y su frecuencia sobre todas las decisiones del grupo, acumulando los escenarios en que aparece la actividad. '?' marca una celda inestable (rol modal < 60 %); '·' indica sin rol. Rol por decisión: A/R > A > R > C > I. La matriz modal describe lo que el modelo produce con este corpus; no es la asignación correcta. El desglose por escenario está en `modal_raci.csv`.

Unidades: DAS, ISC y MCO agrupan sus secciones; TX_REG = departamentos regionales de Transmisión; NEW_AUTHORITY = PROPOSED_NEW_AUTHORITY; OTHER = unidad no incluida en el corpus.

## Especializados, fase 1 (independiente)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DOS | DEL | DEN | DDR | OP | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 72% | · | C 75% | C 55% ? | · | C 70% | · | · | · | · 42% ? | · | 40 |
| ACT02 Certificar los datos de la instalación (configur | I 57% ? | · 50% ? | · 42% ? | I 68% | C 57% ? | C 42% ? | · 42% ? | · | · | · | · | 40 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 85% | C 60% | C 50% ? | C 85% | · | C 95% | C 65% | · | · | · | · | 20 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 90% | C 55% ? | C 60% | C 53% ? | · | C 90% | C 85% | · | · | · | · | 60 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 82% | C 40% ? | C 48% ? | C 72% | · | C 98% | C 72% | · | · | · | · | 40 |
| ACT06 Configurar la adquisición, la correspondencia se | R 38% ? | R 65% | A/R 50% ? | C 96% | · | C 42% ? | · | · | · | · | · | 80 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 75% | R 60% | C 45% ? | C 100% | · | · | · | · | · | · | · | 20 |
| ACT08 Preparar el paquete de implementación | R 50% ? | C 75% | A/R 65% | I 75% | · | · | · | · | · | · | · | 20 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 73% | A/R 97% | R 78% | C 98% | · | C 48% ? | · | · | · | · 53% ? | · | 60 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 65% | C 60% | · | · | · | · | · | · | · | 20 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 97% | · | C 70% | C 95% | · | C 88% | · | · | · | · 55% ? | · | 60 |
| ACT12 Verificar la correspondencia de mímicos y modelo | C 48% ? | R 70% | A 48% ? | C 98% | C 82% | C 48% ? | · | · | · | · | · | 40 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | C 82% | R 60% | R 55% ? | A/R 60% | · | C 80% | · | · | · | I 55% ? | · | 40 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 50% ? | C 50% ? | C 67% | C 88% | · | · 50% ? | · | · | · | I 62% | · | 60 |
| ACT15 Habilitar o suspender la ventana de intervención | C 72% | · | C 89% | A/R 100% | · | C 62% | · | · | · | I 62% | · | 80 |
| ACT16 Ejecutar el respaldo y la carga en producción | R 62% | C 70% | A/R 78% | C 100% | · | · | · | · | · | I 62% | · | 40 |
| ACT17 Mantener el registro técnico de configuración | C 65% | A/R 95% | C 100% | I 55% ? | · | · | · | · | · | · | · | 20 |
| ACT18 Verificar el sistema después de la actualización | A/R 42% ? | C 72% | R 55% ? | C 52% ? | · | · 52% ? | · | · | · | I 68% | · | 40 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 52% ? | · 57% ? | C 65% | C 95% | · | · 55% ? | · | · | · | I 85% | A 52% ? | 40 |
| ACT20 Ejecutar la reversión | R 75% | C 57% ? | A/R 80% | C 100% | · | · | · | · | · | I 72% | · | 40 |

Celdas inestables: 39 de 220.

## Neutral, fase 1

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DOS | DEL | DEN | DDR | OP | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 90% | · | C 90% | C 70% | · | C 70% | · | · | · | · | · | 10 |
| ACT02 Certificar los datos de la instalación (configur | · | · | C 30% ? | I 80% | C 50% ? | C 70% | C 50% ? | · | · | · | · | 10 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 100% | · | C 80% | I 60% | · | C 100% | C 80% | · | · | · | · | 5 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 93% | · | C 53% ? | I 67% | · | C 93% | C 87% | · | · | · | · | 15 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 60% | · | I 40% ? | C 60% | · | C 100% | C 70% | · | · | · | · | 10 |
| ACT06 Configurar la adquisición, la correspondencia se | C 45% ? | R 60% | A/R 60% | C 95% | · | C 45% ? | · | · | · | I 50% ? | · | 20 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 80% | R 80% | C 100% | C 100% | · | · | · | · | · | I 60% | · | 5 |
| ACT08 Preparar el paquete de implementación | R 60% | C 80% | A/R 80% | C 80% | · | · | · | · | · | I 60% | · | 5 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 73% | A/R 93% | R 80% | C 100% | · | C 67% | · | · | · | I 53% ? | · | 15 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 100% | C 60% | · | · | · | · | · | · | · | 5 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 100% | · | C 80% | C 93% | · | C 80% | C 53% ? | · | · | I 67% | · | 15 |
| ACT12 Verificar la correspondencia de mímicos y modelo | C 40% ? | R 100% | A/R 90% | C 90% | C 80% | C 60% | · | · | · | · | · | 10 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | C 80% | R 70% | R 70% | A/R 60% | · 50% ? | C 70% | · | · | · | I 60% | · | 10 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 33% ? | · | C 53% ? | C 100% | · | · | · | · | · | I 60% | · 53% ? | 15 |
| ACT15 Habilitar o suspender la ventana de intervención | C 70% | · | C 90% | A/R 100% | · | C 60% | · | · | · | I 75% | · | 20 |
| ACT16 Ejecutar el respaldo y la carga en producción | R 90% | · 40% ? | A/R 100% | C 100% | · | · | · | · | · | I 70% | · | 10 |
| ACT17 Mantener el registro técnico de configuración | C 100% | A/R 100% | C 100% | · | · | · | · | · | · | · | · | 5 |
| ACT18 Verificar el sistema después de la actualización | A/R 60% | C 60% | R 70% | C 80% | · | · | · | · | · | I 90% | · | 10 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 50% ? | · | C 80% | C 100% | · | · | · | · | · | I 90% | A 50% ? | 10 |
| ACT20 Ejecutar la reversión | R 100% | · | A/R 100% | C 100% | · | · | · | · | · | I 90% | · | 10 |

Celdas inestables: 18 de 220.

## Comparación celda a celda con REFERENCE_RACI (post hoc)

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Columnas agrupadas como en el artículo: GT_SUPPORT = DOS, DEL, DEN, DDR; ORIGIN = TX_REG, DT, OTHER; NEW_AUTHORITY = Autoridad de Cambio. DEL y DOS se cuentan en GT_SUPPORT aunque el artículo también los admite como origen de parámetros (aproximación).

Formato: `=` coincide con la referencia; `≠ X (ref Y)` difiere, con el rol modal X y el de la referencia Y.

| Grupo | Celdas idénticas | Celdas A/R idénticas | A de la referencia recuperada | Celdas inestables |
|---|---|---|---|---|
| Especializados, fase 1 (independiente) | 37.1 % | 80.0 % | 65.0 % | 36 de 140 |
| Neutral, fase 1 | 33.6 % | 81.4 % | 70.0 % | 14 de 140 |

Celdas idénticas: mismo rol exacto. Celdas A/R idénticas: mismo rol ejecutivo (A/R, A, R), tratando C, I y sin rol como una misma clase. A recuperada: proporción de celdas A de la referencia en las que el rol modal incluye A.

### Especializados, fase 1 (independiente) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = | ≠ - (ref C) | = | = ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ I (ref C) ? | ≠ - (ref C) ? | ≠ - (ref I) ? | ≠ I (ref C) | = ? | ≠ C (ref A/R) ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | = | = ? | = | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | = ? | = | = ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ C (ref A/R) ? | ≠ C (ref I) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ R (ref C) ? | ≠ R (ref A/R) | ≠ A/R (ref R) ? | ≠ C (ref I) | ≠ C (ref I) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ R (ref A/R) | ≠ C (ref R) ? | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | = ? | ≠ C (ref A/R) | ≠ A/R (ref R) | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ R (ref C) | = | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | = | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ C (ref R) ? | ≠ R (ref C) | ≠ A (ref I) ? | = | ≠ C (ref I) ? | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | = | ≠ R (ref C) | ≠ R (ref C) ? | = | = | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) ? | = ? | = | = | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ C (ref R) | ≠ A/R (ref A) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ R (ref C) | = | = | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | = | = | ≠ C (ref R) | = ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = ? | ≠ C (ref R) | = ? | = ? | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = ? | ≠ - (ref C) ? | ≠ C (ref R) | = | ≠ - (ref C) ? | ≠ - (ref I) | = ? |
| ACT20 Ejecutar la reversión | ≠ R (ref C) | = ? | = | = | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |

### Neutral, fase 1 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = | ≠ - (ref C) | = | = | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | ≠ - (ref C) | ≠ C (ref I) ? | ≠ I (ref C) | = | = ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | ≠ - (ref C) | = | ≠ I (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | = ? | ≠ I (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | = ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | = ? | ≠ R (ref A/R) | ≠ A/R (ref R) | ≠ C (ref I) | ≠ C (ref I) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ R (ref A/R) | ≠ C (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | = | ≠ C (ref A/R) | ≠ A/R (ref R) | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ R (ref C) | = | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | = | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ C (ref R) ? | ≠ R (ref C) | ≠ A/R (ref I) | = | ≠ C (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | = | ≠ R (ref C) | ≠ R (ref C) | = | = | = ? | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) ? | ≠ - (ref C) | = ? | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref A) ? |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ C (ref R) | ≠ A/R (ref A) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ R (ref C) | ≠ - (ref C) ? | = | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | = | = | ≠ C (ref R) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = | ≠ C (ref R) | = | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = ? | ≠ - (ref C) | ≠ C (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | = ? |
| ACT20 Ejecutar la reversión | ≠ R (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |

### REFERENCE_RACI (artículo), en las mismas columnas

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | A/R | C | C | C | C | C | I |
| ACT02 Certificar los datos de la instalación ( | C | C | I | C | C | A/R | I |
| ACT03 Especificar y aceptar la semántica del m | A/R | C | C | C | C | C | I |
| ACT04 Construir o actualizar el modelo eléctri | A/R | C | C | C | C | C | I |
| ACT05 Revisar la calidad topológica y de nomen | C | A/R | I | I | I | I | I |
| ACT06 Configurar la adquisición, la correspond | C | A/R | R | I | I | C | I |
| ACT07 Unificar modelo y adquisición en la base | R | A/R | R | C | C | I | I |
| ACT08 Preparar el paquete de implementación | R | A/R | R | I | I | I | I |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | C | A/R | C | C | C | C | I |
| ACT10 Administrar y actualizar los aplicativos | A/R | C | R | C | C | I | I |
| ACT11 Validar el estimador de estado, el flujo | A/R | C | C | C | C | I | I |
| ACT12 Verificar la correspondencia de mímicos  | R | C | I | C | I | A/R | I |
| ACT13 Aceptar mímicos, alarmas y el uso operat | C | C | C | A/R | C | C | I |
| ACT14 Autorizar la liberación de la versión a  | R | C | C | C | C | I | A |
| ACT15 Habilitar o suspender la ventana de inte | C | I | R | A | C | I | I |
| ACT16 Ejecutar el respaldo y la carga en produ | C | C | A/R | C | I | I | I |
| ACT17 Mantener el registro técnico de configur | C | A/R | R | I | I | I | I |
| ACT18 Verificar el sistema después de la actua | A/R | R | R | C | C | I | I |
| ACT19 Aprobar los criterios de reversión y su  | R | C | R | C | C | I | A |
| ACT20 Ejecutar la reversión | C | C | A/R | C | I | I | I |
