# Matriz RACI modal

Cada celda muestra el rol más frecuente de la unidad en la actividad y su frecuencia sobre todas las decisiones del grupo, acumulando los escenarios en que aparece la actividad. '?' marca una celda inestable (rol modal < 60 %); '·' indica sin rol. Rol por decisión: A/R > A > R > C > I. La matriz modal describe lo que el modelo produce con este corpus; no es la asignación correcta. El desglose por escenario está en `modal_raci.csv`.

Unidades: DAS, ISC y MCO agrupan sus secciones; TX_REG = departamentos regionales de Transmisión; NEW_AUTHORITY = PROPOSED_NEW_AUTHORITY; OTHER = unidad no incluida en el corpus.

## Especializados, fase 1 (independiente)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | OP | n |
|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | C 70% | · 52% ? | · | A/R 35% ? | · | · | C 28% ? | · | · | 40 |
| ACT02 Certificar los datos de la instalación (configur | · | · 50% ? | · | I 62% | C 32% ? | · 48% ? | C 48% ? | · 40% ? | · | 40 |
| ACT03 Especificar y aceptar la semántica del modelo (n | R 35% ? | A/R 25% ? | · | C 60% | · | · | C 65% | · | · | 20 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 97% | · | · | · 58% ? | · | · | · | · | · | 60 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 72% | · | · | · | · | · | · | · | · | 40 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 46% ? | C 28% ? | R 31% ? | I 65% | · | · | · | · | · | 80 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 95% | C 60% | C 70% | I 80% | · | · | · | · | · | 20 |
| ACT08 Preparar el paquete de implementación | A/R 100% | · | C 60% | I 85% | · | · | · | · | · | 20 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | · 43% ? | A/R 57% ? | C 43% ? | C 58% ? | · | · | · | · | · | 60 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 90% | I 90% | · | · | · | · | · | 20 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 85% | · | · | C 73% | · | · | C 62% | · | · | 60 |
| ACT12 Verificar la correspondencia de mímicos y modelo | · 48% ? | · 55% ? | A 35% ? | C 40% ? | · 42% ? | · | · | · | · | 40 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | · 38% ? | · | R 40% ? | A 55% ? | · | · | C 60% | · | · | 40 |
| ACT14 Autorizar la liberación de la versión a producci | R 48% ? | · | · | C 47% ? | · | · | · | · | · 50% ? | 60 |
| ACT15 Habilitar o suspender la ventana de intervención | C 40% ? | · | · 57% ? | A/R 99% | · | · | · 52% ? | · | · | 80 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 35% ? | · | R 42% ? | I 55% ? | · | · | · | · | · | 40 |
| ACT17 Mantener el registro técnico de configuración | A 50% ? | R 55% ? | · | · | · | · | · | · | · | 20 |
| ACT18 Verificar el sistema después de la actualización | A/R 35% ? | · | R 40% ? | C 52% ? | · | · | · | · | · | 40 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 40% ? | · 50% ? | · | C 72% | · | · 57% ? | · | · | · 42% ? | 40 |
| ACT20 Ejecutar la reversión | A/R 42% ? | · | R 52% ? | C 57% ? | · | · | · | · | · | 40 |

Celdas inestables: 47 de 180.

## Neutral, fase 1

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | OP | n |
|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | C 60% | · | · | C 50% ? | · | · | A/R 40% ? | · | · | 10 |
| ACT02 Certificar los datos de la instalación (configur | · | · 40% ? | · | · | A/R 30% ? | · | C 70% | · 40% ? | · | 10 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 40% ? | C 60% | · | I 60% | · | · | C 100% | · | · | 5 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 93% | · 53% ? | · | · | · | · | · | · 53% ? | · | 15 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 70% | · | · | · | · | · | · 40% ? | · | · | 10 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 40% ? | A/R 45% ? | · 40% ? | C 35% ? | · | · | · | · | · | 20 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 100% | · | · | I 80% | · | · | · | · | · | 5 |
| ACT08 Preparar el paquete de implementación | A/R 100% | C 60% | R 40% ? | I 80% | · | · | · | · | · | 5 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | I 33% ? | A/R 67% | C 33% ? | C 60% | · | · | · 40% ? | · | · | 15 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 60% | I 80% | · | · | · | · | · | 5 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 93% | · | · | C 73% | · | · | C 60% | · | · | 15 |
| ACT12 Verificar la correspondencia de mímicos y modelo | · 50% ? | · 50% ? | R 40% ? | · 40% ? | C 50% ? | · | · | · | · | 10 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | · 40% ? | · | C 50% ? | A/R 40% ? | · | · | · 50% ? | · | · | 10 |
| ACT14 Autorizar la liberación de la versión a producci | R 47% ? | · | · | C 60% | · | · | · | · | · | 15 |
| ACT15 Habilitar o suspender la ventana de intervención | I 50% ? | · | · | A/R 100% | · | · | · 50% ? | · | · | 20 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 50% ? | · | R 40% ? | C 50% ? | · | · | · | · | · | 10 |
| ACT17 Mantener el registro técnico de configuración | A 80% | R 80% | · | · | · | · | · | · | · | 5 |
| ACT18 Verificar el sistema después de la actualización | A/R 40% ? | · | R 50% ? | C 50% ? | · | · | · 50% ? | · | · | 10 |
| ACT19 Aprobar los criterios de reversión y su delegaci | A/R 40% ? | · 40% ? | · | C 80% | · | I 50% ? | · | · | · | 10 |
| ACT20 Ejecutar la reversión | R 50% ? | · | R 60% | A 50% ? | · | · | · | · | · | 10 |

Celdas inestables: 41 de 180.

## Comparación celda a celda con REFERENCE_RACI (post hoc)

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Columnas agrupadas como en el artículo: GT_SUPPORT = DOS, DEL, DEN, DDR; ORIGIN = TX_REG, DT, OTHER; NEW_AUTHORITY = Autoridad de Cambio. DEL y DOS se cuentan en GT_SUPPORT aunque el artículo también los admite como origen de parámetros (aproximación).

Formato: `=` coincide con la referencia; `≠ X (ref Y)` difiere, con el rol modal X y el de la referencia Y.

| Grupo | Celdas idénticas | Celdas A/R idénticas | A de la referencia recuperada | Celdas inestables |
|---|---|---|---|---|
| Especializados, fase 1 (independiente) | 17.9 % | 75.0 % | 35.0 % | 48 de 140 |
| Neutral, fase 1 | 20.7 % | 78.6 % | 50.0 % | 39 de 140 |

Celdas idénticas: mismo rol exacto. Celdas A/R idénticas: mismo rol ejecutivo (A/R, A, R), tratando C, I y sin rol como una misma clase. A recuperada: proporción de celdas A de la referencia en las que el rol modal incluye A.

### Especializados, fase 1 (independiente) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | ≠ C (ref A/R) | ≠ - (ref C) ? | ≠ - (ref C) | ≠ A/R (ref C) ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ I (ref C) | ≠ A/R (ref C) ? | ≠ C (ref A/R) ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | ≠ R (ref A/R) ? | ≠ A/R (ref C) ? | ≠ - (ref C) | = | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref C) ? | ≠ - (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) ? | ≠ C (ref A/R) ? | = ? | = | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ C (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ - (ref A/R) | ≠ C (ref R) | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | ≠ - (ref C) ? | = ? | = ? | = ? | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ - (ref R) ? | ≠ - (ref C) ? | ≠ A (ref I) ? | = ? | ≠ - (ref I) | ≠ C (ref A/R) ? | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ - (ref C) ? | ≠ - (ref C) | ≠ R (ref C) ? | ≠ A (ref A/R) ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | = ? | ≠ - (ref C) | ≠ - (ref C) | = ? | ≠ - (ref C) ? | ≠ - (ref I) ? | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = ? | ≠ - (ref I) | ≠ - (ref R) ? | ≠ A/R (ref A) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) ? | ≠ - (ref C) | ≠ R (ref A/R) ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A (ref C) ? | ≠ R (ref A/R) ? | ≠ - (ref R) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = ? | ≠ - (ref R) | = ? | = ? | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = ? | ≠ - (ref C) ? | ≠ - (ref R) | = | ≠ - (ref C) | ≠ - (ref I) ? | ≠ - (ref A) |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) ? | ≠ - (ref C) | ≠ R (ref A/R) ? | = ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |

### Neutral, fase 1 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | ≠ C (ref A/R) | ≠ - (ref C) | ≠ - (ref C) | = ? | ≠ A/R (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref C) | = | = ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = ? | = | ≠ - (ref C) | ≠ I (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) ? | ≠ - (ref C) | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) | ≠ - (ref I) | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) ? | = ? | ≠ - (ref R) ? | ≠ C (ref I) ? | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ - (ref A/R) | ≠ - (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ C (ref A/R) | = ? | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | ≠ I (ref C) ? | = | = ? | = | ≠ - (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ - (ref R) ? | ≠ - (ref C) ? | ≠ R (ref I) ? | ≠ - (ref C) ? | ≠ - (ref I) | ≠ C (ref A/R) ? | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ - (ref C) ? | ≠ - (ref C) | = ? | = ? | ≠ I (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | = ? | ≠ - (ref C) | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref R) | ≠ A/R (ref A) | = ? | ≠ - (ref I) ? | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) ? | ≠ - (ref C) | ≠ R (ref A/R) ? | = ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A (ref C) | ≠ R (ref A/R) | ≠ - (ref R) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = ? | ≠ - (ref R) | = ? | = ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | ≠ A/R (ref R) ? | ≠ - (ref C) ? | ≠ - (ref R) | = | ≠ - (ref C) | = ? | ≠ - (ref A) |
| ACT20 Ejecutar la reversión | ≠ R (ref C) ? | ≠ - (ref C) | ≠ R (ref A/R) | ≠ A (ref C) ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |

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
