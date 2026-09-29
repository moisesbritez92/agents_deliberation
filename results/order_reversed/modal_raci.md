# Matriz RACI modal

Cada celda muestra el rol más frecuente de la unidad en la actividad y su frecuencia sobre todas las decisiones del grupo, acumulando los escenarios en que aparece la actividad. '?' marca una celda inestable (rol modal < 60 %); '·' indica sin rol. Rol por decisión: A/R > A > R > C > I. La matriz modal describe lo que el modelo produce con este corpus; no es la asignación correcta. El desglose por escenario está en `modal_raci.csv`.

Unidades: DAS, ISC y MCO agrupan sus secciones; TX_REG = departamentos regionales de Transmisión; NEW_AUTHORITY = PROPOSED_NEW_AUTHORITY; OTHER = unidad no incluida en el corpus.

## Especializados, fase 1 (independiente)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | OP | GERENCIA_TECNICA | n |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | C 52% ? | · 52% ? | · | C 38% ? | · | · | C 35% ? | · | I 78% | · | 40 |
| ACT02 Certificar los datos de la instalación (configur | · 35% ? | C 35% ? | · | I 45% ? | · | · 48% ? | · | · 45% ? | · | · | 40 |
| ACT03 Especificar y aceptar la semántica del modelo (n | C 50% ? | A/R 55% ? | · | C 75% | · | · | · 55% ? | · | · 55% ? | · | 20 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 93% | C 75% | · | I 68% | · | · | · | · | · | · | 60 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 80% | · 48% ? | · | · | · | · | · | · | · | · | 40 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 54% ? | · 28% ? | · 51% ? | I 60% | · | · | · | · | · | · | 80 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 95% | C 70% | · | I 65% | · | · | · | · | · | · | 20 |
| ACT08 Preparar el paquete de implementación | A/R 85% | · 45% ? | · | I 70% | · | · | · | · | · | · | 20 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 60% | A/R 78% | · | C 82% | · | · | · | · | · | · | 60 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | · | I 65% | · | · | C 75% | · | I 55% ? | · | 20 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 97% | · | · | I 57% ? | · | · | · 50% ? | C 70% | · | · | 60 |
| ACT12 Verificar la correspondencia de mímicos y modelo | C 38% ? | A/R 30% ? | · 55% ? | I 40% ? | · | · | · | · | · | · | 40 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | R 38% ? | · 50% ? | · 45% ? | R 40% ? | · | · | · | · | A 42% ? | · | 40 |
| ACT14 Autorizar la liberación de la versión a producci | R 67% | · | · | C 42% ? | · | · | C 60% | · | A 62% | · | 60 |
| ACT15 Habilitar o suspender la ventana de intervención | C 72% | · | · | A/R 96% | · | · | · 54% ? | · | · 49% ? | · | 80 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 88% | · | · | C 57% ? | · | · | · | · | · | · | 40 |
| ACT17 Mantener el registro técnico de configuración | A/R 75% | C 35% ? | · | · | · | · | · | · | · | · | 20 |
| ACT18 Verificar el sistema después de la actualización | A/R 52% ? | · | · | C 55% ? | · | · | · | · | I 57% ? | · | 40 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 60% | · | · | C 65% | · | · | C 32% ? | · | A 85% | · | 40 |
| ACT20 Ejecutar la reversión | A/R 82% | · | · | C 80% | · | · | · | · | I 68% | · | 40 |

Celdas inestables: 39 de 200.

## Neutral, fase 1

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | OP | GERENCIA_TECNICA | n |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | R 40% ? | · 50% ? | · | R 30% ? | · | · | C 40% ? | · | I 50% ? | · | 10 |
| ACT02 Certificar los datos de la instalación (configur | · | C 50% ? | · | · | · 40% ? | · | · | · 40% ? | · | · | 10 |
| ACT03 Especificar y aceptar la semántica del modelo (n | C 40% ? | A/R 60% | · | C 60% | · | · | C 100% | · | · | · | 5 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | C 80% | · | · | · | · | · | · | · | · | 15 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 80% | · 50% ? | · | · 50% ? | · | · | · | C 40% ? | · | · | 10 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 45% ? | A/R 30% ? | · 45% ? | I 70% | · | · | · | · | · | · | 20 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 100% | C 80% | · | I 100% | · | · | · | · | · | · | 5 |
| ACT08 Preparar el paquete de implementación | A/R 80% | C 40% ? | · | I 40% ? | · | · | · | · | I 60% | · | 5 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 87% | A/R 100% | · | C 67% | · | · | · | · | · | · | 15 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | · | I 40% ? | · | · | C 100% | · | I 80% | · | 5 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 87% | · | · | I 67% | · | · | C 73% | C 60% | · | · | 15 |
| ACT12 Verificar la correspondencia de mímicos y modelo | C 60% | A/R 40% ? | · | R 30% ? | · | · | · | · | · 50% ? | · | 10 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | C 70% | · | · 50% ? | R 40% ? | · | · | · 50% ? | · | A 50% ? | · | 10 |
| ACT14 Autorizar la liberación de la versión a producci | R 60% | · | · | C 40% ? | · | · | C 60% | · | A 67% | · | 15 |
| ACT15 Habilitar o suspender la ventana de intervención | C 75% | · | · | A/R 100% | · | · | · | · | I 45% ? | · | 20 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 100% | · | · | C 70% | · | · | · | · | · | · | 10 |
| ACT17 Mantener el registro técnico de configuración | A/R 80% | · | · | · | · | · | · | · | · | · | 5 |
| ACT18 Verificar el sistema después de la actualización | A/R 50% ? | · | · | C 60% | · | · | · | · | I 60% | · | 10 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 70% | · | · | C 50% ? | · | · | C 50% ? | · | A 90% | · | 10 |
| ACT20 Ejecutar la reversión | A/R 70% | · | · | C 80% | · | · | · | · | I 60% | · | 10 |

Celdas inestables: 30 de 200.

## Comparación celda a celda con REFERENCE_RACI (post hoc)

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Columnas agrupadas como en el artículo: GT_SUPPORT = DOS, DEL, DEN, DDR; ORIGIN = TX_REG, DT, OTHER; NEW_AUTHORITY = Autoridad de Cambio. DEL y DOS se cuentan en GT_SUPPORT aunque el artículo también los admite como origen de parámetros (aproximación).

Formato: `=` coincide con la referencia; `≠ X (ref Y)` difiere, con el rol modal X y el de la referencia Y.

| Grupo | Celdas idénticas | Celdas A/R idénticas | A de la referencia recuperada | Celdas inestables |
|---|---|---|---|---|
| Especializados, fase 1 (independiente) | 19.3 % | 75.0 % | 30.0 % | 37 de 140 |
| Neutral, fase 1 | 20.7 % | 75.0 % | 35.0 % | 26 de 140 |

Celdas idénticas: mismo rol exacto. Celdas A/R idénticas: mismo rol ejecutivo (A/R, A, R), tratando C, I y sin rol como una misma clase. A recuperada: proporción de celdas A de la referencia en las que el rol modal incluye A.

### Especializados, fase 1 (independiente) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | ≠ C (ref A/R) ? | ≠ - (ref C) ? | ≠ - (ref C) | = ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) ? | = ? | ≠ - (ref I) | ≠ I (ref C) ? | ≠ - (ref C) ? | ≠ - (ref A/R) ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | ≠ C (ref A/R) ? | ≠ A/R (ref C) ? | ≠ - (ref C) | = | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | = | ≠ - (ref C) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) ? | ≠ - (ref I) | ≠ - (ref I) | ≠ C (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) ? | ≠ - (ref A/R) ? | ≠ - (ref R) ? | = | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ - (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ - (ref A/R) ? | ≠ - (ref R) | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ - (ref R) | ≠ I (ref C) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | ≠ I (ref C) ? | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ C (ref R) ? | ≠ A/R (ref C) ? | ≠ - (ref I) ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref A/R) ? | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ R (ref C) ? | ≠ - (ref C) ? | ≠ - (ref C) ? | ≠ R (ref A/R) ? | ≠ - (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | = | ≠ - (ref C) | ≠ - (ref C) | = ? | = | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ - (ref R) | ≠ A/R (ref A) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | ≠ - (ref C) | ≠ - (ref A/R) | = ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ C (ref A/R) ? | ≠ - (ref R) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = ? | ≠ - (ref R) | ≠ - (ref R) | = ? | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | ≠ - (ref C) | ≠ - (ref R) | = | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) | ≠ - (ref C) | ≠ - (ref A/R) | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |

### Neutral, fase 1 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | ≠ R (ref A/R) ? | ≠ - (ref C) ? | ≠ - (ref C) | ≠ R (ref C) ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | = ? | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref C) ? | ≠ - (ref A/R) ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | ≠ C (ref A/R) ? | ≠ A/R (ref C) | ≠ - (ref C) | = | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) ? | ≠ - (ref I) | ≠ - (ref I) ? | ≠ C (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) ? | = ? | ≠ - (ref R) ? | = | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ - (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ C (ref A/R) ? | ≠ - (ref R) | = ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ - (ref R) | ≠ I (ref C) ? | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | ≠ I (ref C) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ C (ref R) | ≠ A/R (ref C) ? | ≠ - (ref I) | ≠ R (ref C) ? | ≠ - (ref I) | ≠ C (ref A/R) ? | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | = | ≠ - (ref C) | ≠ - (ref C) ? | ≠ R (ref A/R) ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | = | ≠ - (ref C) | ≠ - (ref C) | = ? | = | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ - (ref R) | ≠ A/R (ref A) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | ≠ - (ref C) | ≠ - (ref A/R) | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref R) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = ? | ≠ - (ref R) | ≠ - (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | ≠ - (ref C) | ≠ - (ref R) | = ? | = | ≠ - (ref I) | ≠ - (ref A) |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) | ≠ - (ref C) | ≠ - (ref A/R) | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |

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
