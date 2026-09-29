# Matriz RACI modal

Cada celda muestra el rol más frecuente de la unidad en la actividad y su frecuencia sobre todas las decisiones del grupo, acumulando los escenarios en que aparece la actividad. '?' marca una celda inestable (rol modal < 60 %); '·' indica sin rol. Rol por decisión: A/R > A > R > C > I. La matriz modal describe lo que el modelo produce con este corpus; no es la asignación correcta. El desglose por escenario está en `modal_raci.csv`.

Unidades: DAS, ISC y MCO agrupan sus secciones; TX_REG = departamentos regionales de Transmisión; NEW_AUTHORITY = PROPOSED_NEW_AUTHORITY; OTHER = unidad no incluida en el corpus.

## Especializados, fase 1 (independiente)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DOS | DEL | DDR | OP | n |
|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | · 39% ? | · 54% ? | C 46% ? | A/R 38% ? | · | C 38% ? | · | · | · 38% ? | 160 |
| ACT02 Certificar los datos de la instalación (configur | · | A/R 33% ? | · 56% ? | I 44% ? | · 51% ? | C 42% ? | · 50% ? | · | · | 160 |
| ACT03 Especificar y aceptar la semántica del modelo (n | R 24% ? | A/R 31% ? | · 34% ? | C 75% | · | C 51% ? | · | · | · | 80 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 90% | · 51% ? | · 38% ? | · 58% ? | · | · | · | · | · | 240 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 76% | · | · 51% ? | · 52% ? | · | · | · | · | · | 160 |
| ACT06 Configurar la adquisición, la correspondencia se | C 32% ? | R 37% ? | A 45% ? | I 63% | · | · | · | · | · | 320 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 59% ? | C 42% ? | C 45% ? | I 70% | · | · | · | · | · | 80 |
| ACT08 Preparar el paquete de implementación | A/R 55% ? | C 46% ? | C 42% ? | I 69% | · | · | · | · | · | 80 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | · | R 55% ? | A 54% ? | C 62% | · | · | · | · | · | 240 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 74% | I 59% ? | · | · | · | · | · | 80 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 88% | · | · | C 72% | · | · 42% ? | · | · | · | 240 |
| ACT12 Verificar la correspondencia de mímicos y modelo | · 42% ? | · 34% ? | A 40% ? | I 33% ? | C 43% ? | · | · | · | · | 160 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | · 42% ? | · | R 36% ? | A 46% ? | · | · 48% ? | · | · | · | 160 |
| ACT14 Autorizar la liberación de la versión a producci | R 35% ? | · | C 27% ? | C 55% ? | · | · | · | · | · 42% ? | 240 |
| ACT15 Habilitar o suspender la ventana de intervención | · | · | C 51% ? | A/R 96% | · | · | · | · | · | 320 |
| ACT16 Ejecutar el respaldo y la carga en producción | C 42% ? | · | A/R 66% | I 62% | · | · | · | · | · | 160 |
| ACT17 Mantener el registro técnico de configuración | C 35% ? | R 54% ? | C 38% ? | · | · | · | · | · | · | 80 |
| ACT18 Verificar el sistema después de la actualización | C 40% ? | · | A 35% ? | C 58% ? | · | · | · | · | · | 160 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 37% ? | · | C 28% ? | C 78% | · | · | · | · | A 36% ? | 160 |
| ACT20 Ejecutar la reversión | R 51% ? | · | A/R 35% ? | C 59% ? | · | · | · | · | · | 160 |

Celdas inestables: 61 de 180.

## Neutral, fase 1

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DOS | DEL | DDR | OP | n |
|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | C 40% ? | · 57% ? | C 38% ? | A/R 38% ? | · | C 32% ? | · | · | · 52% ? | 40 |
| ACT02 Certificar los datos de la instalación (configur | · | · 32% ? | · 48% ? | I 45% ? | · 40% ? | · 40% ? | · 52% ? | · | · | 40 |
| ACT03 Especificar y aceptar la semántica del modelo (n | C 30% ? | A/R 35% ? | C 45% ? | C 55% ? | · | C 50% ? | · | · | · | 20 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 92% | · 53% ? | I 35% ? | · | · | · | · | · | · | 60 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 70% | · | · 57% ? | · | · | · | · | · | · | 40 |
| ACT06 Configurar la adquisición, la correspondencia se | C 31% ? | R 35% ? | A 45% ? | I 52% ? | · | · | · | · | · | 80 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 50% ? | C 50% ? | A 35% ? | I 80% | · | · | · | · | · | 20 |
| ACT08 Preparar el paquete de implementación | A/R 60% | · 55% ? | C 55% ? | I 75% | · | · | · | · | · | 20 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | · | R 55% ? | A 53% ? | C 55% ? | · | · | · | · | · | 60 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 90% | · | C 70% | I 75% | · | · | · | · | · | 20 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 85% | · | · 53% ? | C 62% | · | C 50% ? | · | · | · | 60 |
| ACT12 Verificar la correspondencia de mímicos y modelo | · 35% ? | · 40% ? | A 40% ? | · 30% ? | C 40% ? | · | · | · | · | 40 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | · 50% ? | · | R 35% ? | A 45% ? | · | · | · | · | · | 40 |
| ACT14 Autorizar la liberación de la versión a producci | C 32% ? | · | A/R 27% ? | C 57% ? | · | · | · | · | · 42% ? | 60 |
| ACT15 Habilitar o suspender la ventana de intervención | · | · | C 49% ? | A/R 99% | · | · | · | · | · | 80 |
| ACT16 Ejecutar el respaldo y la carga en producción | C 42% ? | · | A/R 55% ? | I 65% | · | · | · | · | · | 40 |
| ACT17 Mantener el registro técnico de configuración | C 55% ? | A/R 60% | C 35% ? | · | · | · | · | · | · | 20 |
| ACT18 Verificar el sistema después de la actualización | C 38% ? | · | A/R 45% ? | C 65% | · | · | · | · | · | 40 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 38% ? | · | C 35% ? | C 78% | · | · | · | · | A 30% ? | 40 |
| ACT20 Ejecutar la reversión | R 60% | · | A/R 40% ? | C 65% | · | · | · | · | · | 40 |

Celdas inestables: 57 de 180.

## Comparación celda a celda con REFERENCE_RACI (post hoc)

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Columnas agrupadas como en el artículo: GT_SUPPORT = DOS, DEL, DEN, DDR; ORIGIN = TX_REG, DT, OTHER; NEW_AUTHORITY = Autoridad de Cambio. DEL y DOS se cuentan en GT_SUPPORT aunque el artículo también los admite como origen de parámetros (aproximación).

Formato: `=` coincide con la referencia; `≠ X (ref Y)` difiere, con el rol modal X y el de la referencia Y.

| Grupo | Celdas idénticas | Celdas A/R idénticas | A de la referencia recuperada | Celdas inestables |
|---|---|---|---|---|
| Especializados, fase 1 (independiente) | 17.9 % | 75.0 % | 35.0 % | 58 de 140 |
| Neutral, fase 1 | 17.1 % | 75.0 % | 40.0 % | 58 de 140 |

Celdas idénticas: mismo rol exacto. Celdas A/R idénticas: mismo rol ejecutivo (A/R, A, R), tratando C, I y sin rol como una misma clase. A recuperada: proporción de celdas A de la referencia en las que el rol modal incluye A.

### Especializados, fase 1 (independiente) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | ≠ - (ref A/R) ? | ≠ - (ref C) ? | = ? | ≠ A/R (ref C) ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | ≠ A/R (ref C) ? | ≠ - (ref I) ? | ≠ I (ref C) ? | ≠ - (ref C) ? | ≠ - (ref A/R) ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | ≠ R (ref A/R) ? | ≠ A/R (ref C) ? | ≠ - (ref C) ? | = | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) ? | ≠ - (ref C) ? | ≠ - (ref C) ? | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) ? | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | = ? | ≠ R (ref A/R) ? | ≠ A (ref R) ? | = | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) ? | ≠ C (ref A/R) ? | ≠ C (ref R) ? | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) ? | ≠ C (ref A/R) ? | ≠ C (ref R) ? | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | ≠ - (ref C) | ≠ R (ref A/R) ? | ≠ A (ref C) ? | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | ≠ I (ref C) ? | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ - (ref R) ? | ≠ - (ref C) ? | ≠ A (ref I) ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ C (ref A/R) ? | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ - (ref C) ? | ≠ - (ref C) | ≠ R (ref C) ? | ≠ A (ref A/R) ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | = ? | ≠ - (ref C) | = ? | = ? | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | ≠ - (ref C) | ≠ - (ref I) | ≠ C (ref R) ? | ≠ A/R (ref A) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | = ? | ≠ - (ref C) | = | ≠ I (ref C) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | = ? | ≠ R (ref A/R) ? | ≠ C (ref R) ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | ≠ C (ref A/R) ? | ≠ - (ref R) | ≠ A (ref R) ? | = ? | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = ? | ≠ - (ref C) | ≠ C (ref R) ? | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref A) |
| ACT20 Ejecutar la reversión | ≠ R (ref C) ? | ≠ - (ref C) | = ? | = ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |

### Neutral, fase 1 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | ≠ C (ref A/R) ? | ≠ - (ref C) ? | = ? | ≠ A/R (ref C) ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | ≠ - (ref C) ? | ≠ - (ref I) ? | ≠ I (ref C) ? | ≠ - (ref C) ? | ≠ C (ref A/R) ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | ≠ C (ref A/R) ? | ≠ A/R (ref C) ? | = ? | = ? | = ? | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) ? | ≠ I (ref C) ? | ≠ - (ref C) | ≠ - (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | = ? | ≠ R (ref A/R) ? | ≠ A (ref R) ? | = ? | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) ? | ≠ C (ref A/R) ? | ≠ A (ref R) ? | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ - (ref A/R) ? | ≠ C (ref R) ? | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | ≠ - (ref C) | ≠ R (ref A/R) ? | ≠ A (ref C) ? | = ? | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) ? | = | = ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ - (ref R) ? | ≠ - (ref C) ? | ≠ A (ref I) ? | ≠ - (ref C) ? | ≠ - (ref I) | ≠ C (ref A/R) ? | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ - (ref C) ? | ≠ - (ref C) | ≠ R (ref C) ? | ≠ A (ref A/R) ? | ≠ - (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ C (ref R) ? | ≠ - (ref C) | ≠ A/R (ref C) ? | = ? | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | ≠ - (ref C) | ≠ - (ref I) | ≠ C (ref R) ? | ≠ A/R (ref A) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | = ? | ≠ - (ref C) | = ? | ≠ I (ref C) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | = ? | = | ≠ C (ref R) ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | ≠ C (ref A/R) ? | ≠ - (ref R) | ≠ A/R (ref R) ? | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = ? | ≠ - (ref C) | ≠ C (ref R) ? | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref A) |
| ACT20 Ejecutar la reversión | ≠ R (ref C) | ≠ - (ref C) | = ? | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |

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
