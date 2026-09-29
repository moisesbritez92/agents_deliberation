# Matriz RACI modal

Cada celda muestra el rol más frecuente de la unidad en la actividad y su frecuencia sobre todas las decisiones del grupo, acumulando los escenarios en que aparece la actividad. '?' marca una celda inestable (rol modal < 60 %); '·' indica sin rol. Rol por decisión: A/R > A > R > C > I. La matriz modal describe lo que el modelo produce con este corpus; no es la asignación correcta. El desglose por escenario está en `modal_raci.csv`.

Unidades: DAS, ISC y MCO agrupan sus secciones; TX_REG = departamentos regionales de Transmisión; NEW_AUTHORITY = PROPOSED_NEW_AUTHORITY; OTHER = unidad no incluida en el corpus.

## Especializados, fase 1 (independiente)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | DEN | OP | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 62% | · 58% ? | C 50% ? | R 33% ? | · | · | C 79% | · | · | I 67% | · | 24 |
| ACT02 Certificar los datos de la instalación (configur | I 83% | · 54% ? | · | I 71% | · | A/R 83% | · 54% ? | C 67% | · | · | · | 24 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 83% | C 50% ? | I 58% ? | C 58% ? | · | C 58% ? | · 50% ? | C 92% | · | · | · | 12 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · 56% ? | · 50% ? | I 69% | · | C 72% | C 61% | C 97% | · | · | · | 36 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 88% | · | · | C 50% ? | · | C 62% | C 50% ? | C 75% | · | · | · | 24 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 60% | R 50% ? | R 44% ? | C 98% | · | · 58% ? | C 48% ? | · | · | · 58% ? | · | 48 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 67% | R 58% ? | C 50% ? | C 100% | · | · 58% ? | · | · | · | · | · | 12 |
| ACT08 Preparar el paquete de implementación | A/R 100% | C 67% | C 83% | C 67% | · | · | · 50% ? | · | · | · 58% ? | · | 12 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 78% | A/R 94% | R 67% | C 100% | · | · 47% ? | C 47% ? | · | · | I 50% ? | · | 36 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 92% | C 75% | · | · | C 67% | · | · | I 58% ? | · | 12 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 100% | · | · | C 100% | · | · | C 100% | · 56% ? | · | I 53% ? | · | 36 |
| ACT12 Verificar la correspondencia de mímicos y modelo | R 38% ? | R 58% ? | A/R 38% ? | C 83% | · | C 88% | C 38% ? | · | · | · | · | 24 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | R 79% | C 58% ? | R 88% | A/R 83% | · | C 67% | · 46% ? | · | · | I 58% ? | · | 24 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 67% | · 53% ? | C 81% | C 100% | · | · | C 58% ? | · | · | I 69% | · | 36 |
| ACT15 Habilitar o suspender la ventana de intervención | C 98% | · | C 75% | A/R 100% | · | · | C 85% | · | · | I 77% | · | 48 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 79% | C 50% ? | R 54% ? | C 100% | · | · | C 67% | · | · | I 83% | · | 24 |
| ACT17 Mantener el registro técnico de configuración | A/R 67% | A/R 33% ? | · 50% ? | · 42% ? | · | · | · 50% ? | · | · | · | · | 12 |
| ACT18 Verificar el sistema después de la actualización | A/R 79% | · 46% ? | C 50% ? | R 58% ? | · | · | C 79% | · | · | I 92% | · | 24 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 62% | · 54% ? | C 79% | C 83% | · | · | C 67% | · | · | I 88% | A 58% ? | 24 |
| ACT20 Ejecutar la reversión | A/R 96% | C 50% ? | R 54% ? | C 100% | · | · | C 79% | · | · | I 83% | · | 24 |

Celdas inestables: 52 de 220.

## Neutral, fase 1

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | DEN | OP | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 67% | C 50% ? | I 50% ? | C 50% ? | · | C 50% ? | C 100% | · | · | I 100% | · | 6 |
| ACT02 Certificar los datos de la instalación (configur | I 67% | · | · | I 67% | · | A/R 83% | C 50% ? | C 67% | · | · | · | 6 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 100% | R 67% | I 67% | C 67% | · | C 100% | C 33% ? | · | · | · | · | 3 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · | · 56% ? | I 78% | · | C 78% | C 78% | C 67% | · | · | · | 9 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 83% | · | · | C 50% ? | · | C 83% | C 67% | C 67% | · | · | · | 6 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 67% | R 67% | R 42% ? | C 92% | · | · | C 67% | · | · | I 75% | · | 12 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 100% | R 100% | C 100% | C 100% | · | · | C 67% | · | · | I 100% | · | 3 |
| ACT08 Preparar el paquete de implementación | A/R 100% | C 67% | C 100% | C 67% | · | · | · | · | · | I 67% | · | 3 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 89% | A/R 100% | R 78% | C 100% | · | · | C 56% ? | · | · | I 78% | · | 9 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 67% | C 100% | · | · | C 33% ? | · | · | I 67% | · | 3 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 100% | · | · | C 89% | · | · | C 89% | · 56% ? | · | I 78% | · | 9 |
| ACT12 Verificar la correspondencia de mímicos y modelo | C 50% ? | R 33% ? | A/R 50% ? | C 100% | · | C 67% | I 67% | · | · | · | · | 6 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | R 83% | C 67% | R 50% ? | A/R 50% ? | · | C 67% | C 67% | · | · | I 83% | · | 6 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 44% ? | C 56% ? | C 100% | C 100% | · | · | C 56% ? | · | · | I 89% | A 44% ? | 9 |
| ACT15 Habilitar o suspender la ventana de intervención | C 92% | · 58% ? | C 100% | A/R 100% | · | · | C 50% ? | · | · | I 100% | · | 12 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 100% | C 67% | R 83% | C 100% | · | · | C 33% ? | · | · | I 100% | · | 6 |
| ACT17 Mantener el registro técnico de configuración | A/R 100% | R 67% | C 67% | I 67% | · | · | · | · | · | I 67% | · | 3 |
| ACT18 Verificar el sistema después de la actualización | A/R 100% | · 50% ? | R 50% ? | R 50% ? | · | · | C 50% ? | · | · | I 100% | · | 6 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 83% | · 50% ? | C 100% | C 83% | · | · | · 50% ? | · | · | I 83% | A 83% | 6 |
| ACT20 Ejecutar la reversión | A/R 100% | C 67% | R 83% | C 100% | · | · | C 50% ? | · | · | I 100% | · | 6 |

Celdas inestables: 31 de 220.

## Especializados, fase 2 (tras deliberación)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | DEN | OP | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 67% | · | C 75% | R 58% ? | · | · | C 96% | · 58% ? | · | I 75% | · | 24 |
| ACT02 Certificar los datos de la instalación (configur | I 100% | · 54% ? | · | I 92% | C 83% | A/R 92% | C 54% ? | C 71% | · | · | · | 24 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 100% | C 75% | I 75% | C 75% | · | C 67% | C 75% | C 100% | · | · 58% ? | · | 12 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | C 53% ? | · 39% ? | I 58% ? | · | C 97% | C 92% | C 100% | · | · | · | 36 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 96% | · | · 58% ? | C 54% ? | · | C 100% | C 92% | C 88% | · | I 50% ? | · | 24 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 52% ? | R 60% | R 40% ? | C 100% | · | · 58% ? | C 67% | · | · | I 71% | · | 48 |
| ACT07 Unificar modelo y adquisición en la base integra | R 67% | A/R 67% | C 83% | C 100% | · | · | · | · | · | I 83% | · | 12 |
| ACT08 Preparar el paquete de implementación | A/R 100% | C 92% | C 100% | C 92% | · | · | I 67% | · | · | I 67% | · | 12 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | R 58% ? | A/R 97% | R 92% | C 100% | · | · 50% ? | C 64% | · | · | I 72% | · | 36 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 100% | C 100% | · | · | C 92% | · | · | I 92% | · | 12 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 100% | · | · | C 100% | · | · | C 100% | C 56% ? | · | I 69% | · | 36 |
| ACT12 Verificar la correspondencia de mímicos y modelo | R 42% ? | R 67% | A/R 62% | C 100% | · 58% ? | C 92% | I 42% ? | · | · | I 83% | · | 24 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | R 96% | C 100% | R 100% | A/R 100% | · | C 100% | C 58% ? | · | · | I 92% | · | 24 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 56% ? | C 67% | C 86% | C 100% | · | · | C 69% | · | · | I 100% | · 56% ? | 36 |
| ACT15 Habilitar o suspender la ventana de intervención | C 100% | · | C 100% | A/R 100% | · | · | C 98% | · | · | I 92% | · | 48 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 79% | C 100% | R 79% | C 100% | · | · | C 92% | · | · | I 96% | · | 24 |
| ACT17 Mantener el registro técnico de configuración | A/R 67% | A/R 33% ? | · 58% ? | I 50% ? | · | · | I 42% ? | · | · | I 67% | · | 12 |
| ACT18 Verificar el sistema después de la actualización | A/R 100% | C 67% | R 54% ? | R 100% | · | · | C 96% | · | · | I 100% | · | 24 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 79% | · 46% ? | C 79% | C 83% | · | · | C 96% | · | · | I 100% | A 79% | 24 |
| ACT20 Ejecutar la reversión | A/R 100% | C 83% | R 92% | C 100% | · | · | C 100% | · | · | I 96% | · | 24 |

Celdas inestables: 29 de 220.

## Especializados, fase 2c (control sin deliberación)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | DEN | OP | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 62% | · 50% ? | C 58% ? | R 42% ? | · | · 54% ? | C 79% | · | · | I 71% | · | 24 |
| ACT02 Certificar los datos de la instalación (configur | I 83% | · 58% ? | · | I 71% | C 50% ? | A/R 92% | · 50% ? | C 67% | · | · | · | 24 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 83% | C 67% | I 58% ? | C 58% ? | · | C 67% | · 50% ? | C 92% | · | · | · | 12 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · 53% ? | · 50% ? | I 69% | · | C 81% | C 61% | C 97% | · | · | · | 36 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 92% | · | · | C 54% ? | · | C 71% | C 54% ? | C 75% | · | · | · | 24 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 60% | R 56% ? | R 50% ? | C 100% | · | · 56% ? | C 54% ? | · | · | I 52% ? | · | 48 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 50% ? | A/R 50% ? | C 42% ? | C 100% | · | · 50% ? | · | · | · | · | · | 12 |
| ACT08 Preparar el paquete de implementación | A/R 100% | C 67% | C 83% | C 67% | · | · | · 50% ? | · | · | · 58% ? | · | 12 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 75% | A/R 92% | R 72% | C 97% | · | · 47% ? | C 44% ? | · | · | I 50% ? | · | 36 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 92% | C 75% | · | · | C 67% | · | · | I 58% ? | · | 12 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 97% | · | · | C 97% | · | · | C 94% | · 50% ? | · | I 58% ? | · | 36 |
| ACT12 Verificar la correspondencia de mímicos y modelo | R 46% ? | R 58% ? | A/R 42% ? | C 88% | · | C 71% | C 38% ? | · | · | · 58% ? | · | 24 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | R 79% | C 62% | R 92% | A/R 96% | · | C 75% | · 46% ? | · | · | I 67% | · | 24 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 75% | · 53% ? | C 92% | C 100% | · | · | C 58% ? | · | · | I 69% | · | 36 |
| ACT15 Habilitar o suspender la ventana de intervención | C 98% | · | C 79% | A/R 100% | · | · | C 85% | · | · | I 77% | · | 48 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 71% | C 50% ? | R 62% | C 100% | · | · | C 67% | · | · | I 83% | · | 24 |
| ACT17 Mantener el registro técnico de configuración | A/R 67% | C 42% ? | · 50% ? | C 42% ? | · | · | · 42% ? | · | · | · | · | 12 |
| ACT18 Verificar el sistema después de la actualización | A/R 96% | · 42% ? | C 50% ? | R 71% | · | · | C 83% | · | · | I 96% | · | 24 |
| ACT19 Aprobar los criterios de reversión y su delegaci | A/R 58% ? | · 46% ? | C 88% | C 92% | · | · | C 75% | · | · | I 88% | · 58% ? | 24 |
| ACT20 Ejecutar la reversión | A/R 92% | C 54% ? | R 75% | C 100% | · | · | C 79% | · | · | I 88% | · | 24 |

Celdas inestables: 50 de 220.

## Árbitro, fase 3

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | DEN | OP | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 83% | · 50% ? | C 67% | R 83% | · | · | C 100% | C 50% ? | · | I 83% | · | 6 |
| ACT02 Certificar los datos de la instalación (configur | I 100% | · | · | I 100% | C 100% | A/R 83% | C 50% ? | C 67% | · | · | · | 6 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 100% | C 100% | I 67% | C 100% | · | C 67% | C 100% | C 100% | · | I 67% | · | 3 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | C 67% | C 33% ? | I 56% ? | · | C 89% | C 100% | C 100% | · | · | · | 9 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 100% | · | · 50% ? | C 67% | · | C 100% | C 100% | C 100% | · | I 50% ? | · | 6 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 50% ? | R 67% | A/R 42% ? | C 100% | · | · | C 67% | · | · | I 83% | · | 12 |
| ACT07 Unificar modelo y adquisición en la base integra | R 67% | A/R 67% | C 100% | C 100% | · | · | · | · | · | I 100% | · | 3 |
| ACT08 Preparar el paquete de implementación | A/R 100% | C 100% | C 100% | C 100% | · | · | I 67% | · | · | I 100% | · | 3 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | R 56% ? | A/R 100% | R 89% | C 100% | · | · 56% ? | C 67% | · | · | I 89% | · | 9 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 100% | C 100% | · | · | C 100% | · | · | I 100% | · | 3 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 100% | · | · | C 100% | · | · | C 100% | C 56% ? | · | I 89% | · | 9 |
| ACT12 Verificar la correspondencia de mímicos y modelo | C 50% ? | R 67% | A/R 67% | C 100% | · | C 83% | C 50% ? | · | · | I 83% | · | 6 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | R 100% | C 100% | R 100% | A/R 100% | · | C 83% | C 67% | · 50% ? | · | I 100% | · | 6 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 56% ? | C 67% | C 89% | C 100% | · | · | C 67% | · | · | I 100% | · | 9 |
| ACT15 Habilitar o suspender la ventana de intervención | C 100% | · | C 100% | A/R 100% | · | · | C 100% | · | · | I 92% | · | 12 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 67% | C 100% | R 67% | C 100% | · | · | C 100% | · | · | I 100% | · | 6 |
| ACT17 Mantener el registro técnico de configuración | A/R 67% | A/R 33% ? | · | C 67% | · | · | C 33% ? | · | · | I 100% | · | 3 |
| ACT18 Verificar el sistema después de la actualización | A/R 100% | C 67% | R 50% ? | R 100% | · | · | C 100% | · | · | I 100% | · | 6 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 83% | · 50% ? | C 67% | C 83% | · | · | C 100% | · | · | I 100% | A 83% | 6 |
| ACT20 Ejecutar la reversión | A/R 100% | C 83% | R 100% | C 100% | · | · | C 100% | · | · | I 100% | · | 6 |

Celdas inestables: 20 de 220.

## Comparación celda a celda con REFERENCE_RACI (post hoc)

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Columnas agrupadas como en el artículo: GT_SUPPORT = DOS, DEL, DEN, DDR; ORIGIN = TX_REG, DT, OTHER; NEW_AUTHORITY = Autoridad de Cambio. DEL y DOS se cuentan en GT_SUPPORT aunque el artículo también los admite como origen de parámetros (aproximación).

Formato: `=` coincide con la referencia; `≠ X (ref Y)` difiere, con el rol modal X y el de la referencia Y.

| Grupo | Celdas idénticas | Celdas A/R idénticas | A de la referencia recuperada | Celdas inestables |
|---|---|---|---|---|
| Especializados, fase 1 (independiente) | 33.6 % | 77.1 % | 60.0 % | 41 de 140 |
| Neutral, fase 1 | 36.4 % | 77.1 % | 60.0 % | 30 de 140 |
| Especializados, fase 2 (tras deliberación) | 38.6 % | 78.6 % | 65.0 % | 22 de 140 |
| Especializados, fase 2c (control sin deliberación) | 32.9 % | 75.7 % | 55.0 % | 38 de 140 |
| Árbitro, fase 3 | 36.4 % | 77.1 % | 65.0 % | 14 de 140 |

Celdas idénticas: mismo rol exacto. Celdas A/R idénticas: mismo rol ejecutivo (A/R, A, R), tratando C, I y sin rol como una misma clase. A recuperada: proporción de celdas A de la referencia en las que el rol modal incluye A.

### Especializados, fase 1 (independiente) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = | ≠ - (ref C) ? | = ? | ≠ R (ref C) ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ I (ref C) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | = ? | ≠ I (ref C) ? | = ? | = | = ? | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) ? | ≠ - (ref C) ? | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) | ≠ C (ref I) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) | ≠ R (ref A/R) ? | = ? | ≠ C (ref I) | ≠ C (ref I) ? | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ R (ref A/R) ? | ≠ C (ref R) ? | = | ≠ - (ref C) | ≠ - (ref I) ? | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ C (ref R) | ≠ C (ref I) | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ R (ref C) | = | = ? | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | = ? | ≠ R (ref C) ? | ≠ A/R (ref I) ? | = | ≠ C (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ R (ref C) | = ? | ≠ R (ref C) | = | = ? | = | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) | ≠ - (ref C) ? | = | = | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ C (ref R) | ≠ A/R (ref A) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | = ? | ≠ R (ref A/R) ? | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | = ? | ≠ - (ref R) ? | ≠ - (ref I) ? | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = | ≠ - (ref R) ? | ≠ C (ref R) ? | ≠ R (ref C) ? | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | ≠ - (ref C) ? | ≠ C (ref R) | = | = | ≠ - (ref I) | = ? |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) | = ? | ≠ R (ref A/R) ? | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |

### Neutral, fase 1 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = | = ? | ≠ I (ref C) ? | = ? | = | = ? | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | ≠ R (ref C) | ≠ I (ref C) | = | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) ? | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) | ≠ C (ref I) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) | ≠ R (ref A/R) | = ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ R (ref A/R) | ≠ C (ref R) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ C (ref R) | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ R (ref C) | = | = ? | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | = ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ C (ref R) ? | ≠ R (ref C) ? | ≠ A/R (ref I) ? | = | = ? | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ R (ref C) | = | ≠ R (ref C) ? | = ? | = | = | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) ? | = ? | = | = | = ? | ≠ - (ref I) | = ? |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) ? | ≠ C (ref R) | ≠ A/R (ref A) | = ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | = | ≠ R (ref A/R) | = | ≠ C (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ R (ref A/R) | ≠ C (ref R) | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = | ≠ - (ref R) ? | = ? | ≠ R (ref C) ? | = ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | ≠ - (ref C) ? | ≠ C (ref R) | = | ≠ I (ref C) ? | ≠ - (ref I) | = |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) | = | ≠ R (ref A/R) | = | ≠ C (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |

### Especializados, fase 2 (tras deliberación) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = | ≠ - (ref C) | = | ≠ R (ref C) ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ I (ref C) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | = | ≠ I (ref C) | = | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | = ? | ≠ - (ref C) ? | ≠ I (ref C) ? | = | = | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) ? | ≠ C (ref I) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) ? | ≠ R (ref A/R) | = ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | = | = | ≠ C (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ C (ref R) | ≠ C (ref I) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | ≠ R (ref C) ? | = | ≠ R (ref C) | = | = | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | = ? | ≠ R (ref C) | ≠ A/R (ref I) | = | ≠ C (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ R (ref C) | = | ≠ R (ref C) | = | = ? | = | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) ? | = | = | = | = | ≠ - (ref I) | ≠ - (ref A) ? |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ C (ref R) | ≠ A/R (ref A) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | = | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | = ? | ≠ - (ref R) ? | = ? | = ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = | ≠ C (ref R) | = ? | ≠ R (ref C) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | ≠ - (ref C) ? | ≠ C (ref R) | = | = | ≠ - (ref I) | = |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) | = | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |

### Especializados, fase 2c (control sin deliberación) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = | ≠ - (ref C) ? | = ? | ≠ R (ref C) ? | = | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ I (ref C) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | = | ≠ I (ref C) ? | = ? | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) ? | ≠ - (ref C) ? | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) | ≠ C (ref I) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) | ≠ R (ref A/R) ? | = ? | ≠ C (ref I) | ≠ C (ref I) ? | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) ? | = ? | ≠ C (ref R) ? | = | ≠ - (ref C) | ≠ C (ref I) ? | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ C (ref R) | ≠ C (ref I) | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ R (ref C) | = | = ? | = ? | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | = ? | ≠ R (ref C) ? | ≠ A/R (ref I) ? | = | ≠ C (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ R (ref C) | = | ≠ R (ref C) | = | = ? | = | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) | ≠ - (ref C) ? | = | = | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ C (ref R) | ≠ A/R (ref A) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | = ? | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ C (ref A/R) ? | ≠ - (ref R) ? | ≠ C (ref I) ? | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = | ≠ - (ref R) ? | ≠ C (ref R) ? | ≠ R (ref C) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | ≠ A/R (ref R) ? | ≠ - (ref C) ? | ≠ C (ref R) | = | = | ≠ - (ref I) | ≠ - (ref A) ? |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) | = ? | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |

### Árbitro, fase 3 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = | ≠ - (ref C) ? | = | ≠ R (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | = | ≠ I (ref C) | = | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | = | = ? | ≠ I (ref C) ? | = | = | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) ? | ≠ R (ref A/R) | ≠ A/R (ref R) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | = | = | ≠ C (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ C (ref R) | ≠ C (ref I) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | ≠ R (ref C) ? | = | ≠ R (ref C) | = | = | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ C (ref R) ? | ≠ R (ref C) | ≠ A/R (ref I) | = | ≠ C (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ R (ref C) | = | ≠ R (ref C) | = | = | = | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) ? | = | = | = | = | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ C (ref R) | ≠ A/R (ref A) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | = | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | = ? | ≠ - (ref R) | ≠ C (ref I) | ≠ C (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = | ≠ C (ref R) | = ? | ≠ R (ref C) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | ≠ - (ref C) ? | ≠ C (ref R) | = | = | ≠ - (ref I) | = |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) | = | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |

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
