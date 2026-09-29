# Matriz RACI modal

Cada celda muestra el rol más frecuente de la unidad en la actividad y su frecuencia sobre todas las decisiones del grupo, acumulando los escenarios en que aparece la actividad. '?' marca una celda inestable (rol modal < 60 %); '·' indica sin rol. Rol por decisión: A/R > A > R > C > I. La matriz modal describe lo que el modelo produce con este corpus; no es la asignación correcta. El desglose por escenario está en `modal_raci.csv`.

Unidades: DAS, ISC y MCO agrupan sus secciones; TX_REG = departamentos regionales de Transmisión; NEW_AUTHORITY = PROPOSED_NEW_AUTHORITY; OTHER = unidad no incluida en el corpus.

## Especializados, fase 1 (independiente)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | OP | GERENCIA_TECNICA | n |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | C 56% ? | · 49% ? | · | A/R 51% ? | · | · | C 55% ? | · | · 56% ? | · | 160 |
| ACT02 Certificar los datos de la instalación (configur | · 56% ? | · 45% ? | · | · 47% ? | R 49% ? | A 36% ? | · | · 38% ? | · | · | 160 |
| ACT03 Especificar y aceptar la semántica del modelo (n | R 40% ? | C 32% ? | · | C 49% ? | · | · | C 36% ? | C 44% ? | · | · | 80 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · | · | I 51% ? | · | · | · 60% ? | C 68% | · | · | 240 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 72% | · | · | · 52% ? | · | · | C 40% ? | · 52% ? | · | · | 160 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 55% ? | · 33% ? | · 36% ? | I 55% ? | · | · | · | · | · | · | 320 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 94% | C 69% | · | I 74% | · | · | · | · | · | · | 80 |
| ACT08 Preparar el paquete de implementación | A/R 96% | · | C 59% ? | I 79% | · | · | · 57% ? | · | · | · | 80 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 60% ? | A/R 77% | · | C 75% | · | · | · | · | · | · | 240 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 81% | I 65% | · | · | · | · | · | · | 80 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 85% | · | · | C 56% ? | · | · | C 67% | · | · | · | 240 |
| ACT12 Verificar la correspondencia de mímicos y modelo | C 32% ? | · 59% ? | · | A 29% ? | · | · | · | · | · | · | 160 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | C 37% ? | · | · 50% ? | A 45% ? | · | · | C 42% ? | · | · | · | 160 |
| ACT14 Autorizar la liberación de la versión a producci | R 59% ? | · | · 47% ? | C 42% ? | · | · | C 52% ? | · | A 50% ? | · | 240 |
| ACT15 Habilitar o suspender la ventana de intervención | C 62% | · | · 52% ? | A/R 97% | · | · | · 37% ? | · | · | · | 320 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 78% | · | C 34% ? | I 55% ? | · | · | · | · | · | · | 160 |
| ACT17 Mantener el registro técnico de configuración | A/R 74% | C 34% ? | · | · | · | · | · | · | · | · | 80 |
| ACT18 Verificar el sistema después de la actualización | A/R 41% ? | · | · 42% ? | C 51% ? | · | · | I 45% ? | · | · | · | 160 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 54% ? | · | · 50% ? | C 54% ? | · | · | C 40% ? | · | A 61% | · | 160 |
| ACT20 Ejecutar la reversión | A/R 46% ? | · | · 46% ? | C 54% ? | · | · | · 46% ? | · | · | · | 160 |

Celdas inestables: 58 de 200.

## Neutral, fase 1

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | OP | GERENCIA_TECNICA | n |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | C 50% ? | · 50% ? | · | A/R 48% ? | · | · | R 45% ? | · | · 45% ? | · | 40 |
| ACT02 Certificar los datos de la instalación (configur | · | · | · | · | R 45% ? | A 38% ? | · | C 50% ? | · | · | 40 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A 25% ? | C 35% ? | · | C 45% ? | · | · | C 45% ? | C 50% ? | · | · | 20 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · 57% ? | · | · 53% ? | · | · | · | C 75% | · | · | 60 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 75% | · | · | · 57% ? | · | · | · 57% ? | C 55% ? | · | · | 40 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 56% ? | · 34% ? | C 35% ? | I 56% ? | · | · | · | · | · | · | 80 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 95% | C 60% | · 55% ? | I 85% | · | · | · | · | · | · | 20 |
| ACT08 Preparar el paquete de implementación | A/R 100% | · | C 80% | I 65% | · | · | · 55% ? | · | · | · | 20 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 58% ? | A/R 75% | · 52% ? | C 70% | · | · | · | · | · | · | 60 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 90% | I 65% | · | · | · | · | · | · | 20 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 82% | · | · | C 67% | · | · | C 68% | · | · | · | 60 |
| ACT12 Verificar la correspondencia de mímicos y modelo | C 32% ? | · | · | A 42% ? | · 45% ? | · | · | · | · | · | 40 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | C 50% ? | · | · 48% ? | R 38% ? | · | · | · 50% ? | · | · 40% ? | · | 40 |
| ACT14 Autorizar la liberación de la versión a producci | R 50% ? | · | · | C 52% ? | · | · | C 55% ? | · | A 63% | · | 60 |
| ACT15 Habilitar o suspender la ventana de intervención | C 60% | · | · 44% ? | A/R 95% | · | · | · 40% ? | · | · | · | 80 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 70% | · | · 32% ? | I 52% ? | · | · | · | · | · | · | 40 |
| ACT17 Mantener el registro técnico de configuración | A/R 70% | C 40% ? | · | I 50% ? | · | · | · | · | · | · | 20 |
| ACT18 Verificar el sistema después de la actualización | A/R 48% ? | · | · 52% ? | C 50% ? | · | · | I 38% ? | · | · | · | 40 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 60% | · | · 55% ? | C 50% ? | · | · | C 38% ? | · | A 75% | · | 40 |
| ACT20 Ejecutar la reversión | R 52% ? | · | · 50% ? | A 48% ? | · | · | · 45% ? | · | · 52% ? | · | 40 |

Celdas inestables: 55 de 200.

## Especializados, fase 2 (tras deliberación)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | OP | GERENCIA_TECNICA | n |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | C 71% | · 46% ? | · | A/R 62% | · | · | C 55% ? | · | I 51% ? | · | 160 |
| ACT02 Certificar los datos de la instalación (configur | · | C 50% ? | · | I 50% ? | R 61% | A 47% ? | · | A 30% ? | · | · | 160 |
| ACT03 Especificar y aceptar la semántica del modelo (n | R 42% ? | C 44% ? | · | I 54% ? | · | · | A 45% ? | C 59% ? | · | · | 80 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · | · | I 63% | · | · | · | C 76% | · | · | 240 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 86% | · | · | I 53% ? | · | · | C 59% ? | C 52% ? | · | · | 160 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 54% ? | A/R 32% ? | · 34% ? | I 52% ? | · | · | · | · | · | · | 320 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 100% | C 92% | · | I 85% | · | · | · | · | · | · | 80 |
| ACT08 Preparar el paquete de implementación | A/R 99% | · | C 85% | I 84% | · | · | · 55% ? | · | · | · | 80 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 76% | A/R 97% | · | C 87% | · | · | · | · | · | · | 240 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 96% | I 78% | · | · | · | · | · | · | 80 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 85% | · | · | C 71% | · | · | C 74% | · | · | · | 240 |
| ACT12 Verificar la correspondencia de mímicos y modelo | R 36% ? | · 52% ? | · 56% ? | A 41% ? | · 48% ? | · 57% ? | · | · | · | · | 160 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | C 48% ? | · | · 49% ? | A 44% ? | · | · | C 45% ? | · | · | · | 160 |
| ACT14 Autorizar la liberación de la versión a producci | R 78% | · | · 44% ? | C 54% ? | · | · | C 60% ? | · | A 58% ? | · | 240 |
| ACT15 Habilitar o suspender la ventana de intervención | C 76% | · | · 45% ? | A/R 99% | · | · | · 35% ? | · | · | · | 320 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 61% | · | R 39% ? | I 51% ? | · | · | · | · | · | · | 160 |
| ACT17 Mantener el registro técnico de configuración | A/R 65% | C 45% ? | · | · 56% ? | · | · | · | · | · | · | 80 |
| ACT18 Verificar el sistema después de la actualización | A/R 47% ? | · | · 46% ? | C 51% ? | · | · | I 55% ? | · | · | · | 160 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 64% | · | · | C 59% ? | · | · | C 57% ? | · | A 71% | · 59% ? | 160 |
| ACT20 Ejecutar la reversión | R 47% ? | · | · 46% ? | A 48% ? | · | · | C 36% ? | · | · | · | 160 |

Celdas inestables: 51 de 200.

## Especializados, fase 2c (control sin deliberación)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | OP | GERENCIA_TECNICA | n |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | C 56% ? | · 46% ? | · | A/R 49% ? | · | · | C 54% ? | · | · 54% ? | · | 160 |
| ACT02 Certificar los datos de la instalación (configur | · 55% ? | · 46% ? | · | · 48% ? | R 49% ? | A 36% ? | · | · 36% ? | · | · | 160 |
| ACT03 Especificar y aceptar la semántica del modelo (n | R 39% ? | C 34% ? | · | C 48% ? | · | · | C 36% ? | C 45% ? | · | · | 80 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · | · | I 51% ? | · | · | · 59% ? | C 69% | · | · | 240 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 74% | · | · | · 52% ? | · | · | C 40% ? | · 50% ? | · | · | 160 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 54% ? | · 30% ? | · 36% ? | I 55% ? | · | · | · | · | · | · | 320 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 96% | C 69% | · | I 75% | · | · | · | · | · | · | 80 |
| ACT08 Preparar el paquete de implementación | A/R 96% | · | C 60% | I 79% | · | · | · 56% ? | · | · | · | 80 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 62% | A/R 81% | · | C 76% | · | · | · | · | · | · | 240 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 80% | I 65% | · | · | · | · | · | · | 80 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 85% | · | · | C 56% ? | · | · | C 68% | · | · | · | 240 |
| ACT12 Verificar la correspondencia de mímicos y modelo | C 35% ? | · 56% ? | · 58% ? | C 30% ? | · 56% ? | · | · | · | · | · | 160 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | C 39% ? | · | · 51% ? | A 44% ? | · | · | C 43% ? | · | · | · | 160 |
| ACT14 Autorizar la liberación de la versión a producci | R 59% ? | · | · 50% ? | C 42% ? | · | · | C 51% ? | · | A 49% ? | · | 240 |
| ACT15 Habilitar o suspender la ventana de intervención | C 63% | · | · 51% ? | A/R 97% | · | · | · 37% ? | · | · | · | 320 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 78% | · | C 36% ? | I 55% ? | · | · | · | · | · | · | 160 |
| ACT17 Mantener el registro técnico de configuración | A/R 72% | C 35% ? | · | · | · | · | · | · | · | · | 80 |
| ACT18 Verificar el sistema después de la actualización | A/R 42% ? | · | · 42% ? | C 51% ? | · | · | I 44% ? | · | · | · | 160 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 54% ? | · | · 50% ? | C 53% ? | · | · | C 42% ? | · | A 62% | · | 160 |
| ACT20 Ejecutar la reversión | A/R 45% ? | · | · 43% ? | C 54% ? | · | · | · 46% ? | · | · | · | 160 |

Celdas inestables: 58 de 200.

## Árbitro, fase 3

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | OP | GERENCIA_TECNICA | n |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | C 75% | · 48% ? | · | A/R 60% | · | · | C 52% ? | · | I 55% ? | · | 40 |
| ACT02 Certificar los datos de la instalación (configur | · | · 50% ? | · | I 55% ? | R 65% | A 50% ? | · | C 35% ? | · | · | 40 |
| ACT03 Especificar y aceptar la semántica del modelo (n | R 40% ? | R 35% ? | · | C 65% | · | · | A 45% ? | C 70% | · | · | 20 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · | · | I 75% | · | · | · | C 80% | · | · | 60 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 92% | · | · | I 65% | · | · | C 68% | C 57% ? | · | · | 40 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 56% ? | A/R 36% ? | · 39% ? | C 56% ? | · | · | · | · | · | · | 80 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 100% | C 90% | · | I 90% | · | · | · | · | · | · | 20 |
| ACT08 Preparar el paquete de implementación | A/R 100% | · | C 90% | I 80% | · | · | · 55% ? | · | · | · | 20 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 77% | A/R 100% | · | C 88% | · | · | · | · | · | · | 60 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 100% | I 75% | · | · | · | · | · | · | 20 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 83% | · | · | C 80% | · | · | C 73% | · | · | · | 60 |
| ACT12 Verificar la correspondencia de mímicos y modelo | R 38% ? | · 52% ? | · 55% ? | A 45% ? | C 50% ? | · 57% ? | · | · | · | · | 40 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | C 45% ? | · | · 50% ? | A/R 52% ? | · | · | C 55% ? | · | · | · | 40 |
| ACT14 Autorizar la liberación de la versión a producci | R 88% | · | C 42% ? | C 58% ? | · | · | C 65% | · | A 60% | · | 60 |
| ACT15 Habilitar o suspender la ventana de intervención | C 80% | · | · 49% ? | A/R 100% | · | · | C 38% ? | · | · | · | 80 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 62% | · | R 40% ? | C 55% ? | · | · | · | · | · | · | 40 |
| ACT17 Mantener el registro técnico de configuración | A/R 55% ? | C 45% ? | · | I 60% | · | · | · | · | · | · | 20 |
| ACT18 Verificar el sistema después de la actualización | A/R 48% ? | · | · 50% ? | C 50% ? | · | · | I 62% | · | · | · | 40 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 62% | · | · | C 68% | · | · | C 57% ? | · | A 75% | · 52% ? | 40 |
| ACT20 Ejecutar la reversión | R 48% ? | · | · 52% ? | A 50% ? | · | · | C 40% ? | · | · | · | 40 |

Celdas inestables: 43 de 200.

## Comparación celda a celda con REFERENCE_RACI (post hoc)

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Columnas agrupadas como en el artículo: GT_SUPPORT = DOS, DEL, DEN, DDR; ORIGIN = TX_REG, DT, OTHER; NEW_AUTHORITY = Autoridad de Cambio. DEL y DOS se cuentan en GT_SUPPORT aunque el artículo también los admite como origen de parámetros (aproximación).

Formato: `=` coincide con la referencia; `≠ X (ref Y)` difiere, con el rol modal X y el de la referencia Y.

| Grupo | Celdas idénticas | Celdas A/R idénticas | A de la referencia recuperada | Celdas inestables |
|---|---|---|---|---|
| Especializados, fase 1 (independiente) | 20.0 % | 75.7 % | 40.0 % | 52 de 140 |
| Neutral, fase 1 | 19.3 % | 75.0 % | 40.0 % | 48 de 140 |
| Especializados, fase 2 (tras deliberación) | 21.4 % | 76.4 % | 45.0 % | 43 de 140 |
| Especializados, fase 2c (control sin deliberación) | 21.4 % | 76.4 % | 40.0 % | 51 de 140 |
| Árbitro, fase 3 | 23.6 % | 76.4 % | 45.0 % | 37 de 140 |

Celdas idénticas: mismo rol exacto. Celdas A/R idénticas: mismo rol ejecutivo (A/R, A, R), tratando C, I y sin rol como una misma clase. A recuperada: proporción de celdas A de la referencia en las que el rol modal incluye A.

### Especializados, fase 1 (independiente) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | ≠ C (ref A/R) ? | ≠ - (ref C) ? | ≠ - (ref C) | ≠ A/R (ref C) ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) ? | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref C) ? | = ? | = ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | ≠ R (ref A/R) ? | = ? | ≠ - (ref C) | = ? | ≠ A (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) | ≠ I (ref C) ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) | ≠ - (ref I) ? | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) ? | ≠ - (ref A/R) ? | ≠ - (ref R) ? | = ? | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ - (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ - (ref A/R) | ≠ C (ref R) ? | = | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = ? | = | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = ? | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ C (ref R) ? | ≠ - (ref C) ? | ≠ - (ref I) | ≠ A (ref C) ? | ≠ - (ref I) | ≠ C (ref A/R) ? | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | = ? | ≠ - (ref C) | ≠ - (ref C) ? | ≠ A (ref A/R) ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | = ? | ≠ - (ref C) | ≠ - (ref C) ? | = ? | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ - (ref R) ? | ≠ A/R (ref A) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | ≠ - (ref C) | ≠ C (ref A/R) ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ C (ref A/R) ? | ≠ - (ref R) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = ? | ≠ - (ref R) | ≠ - (ref R) ? | = ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = ? | ≠ - (ref C) | ≠ - (ref R) ? | = ? | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) ? | ≠ - (ref C) | ≠ - (ref A/R) ? | = ? | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |

### Neutral, fase 1 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | ≠ C (ref A/R) ? | ≠ - (ref C) ? | ≠ - (ref C) | ≠ A/R (ref C) ? | ≠ R (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref C) | = ? | = ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | ≠ A (ref A/R) ? | = ? | ≠ - (ref C) | = ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) ? | ≠ - (ref C) | ≠ - (ref C) ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) | ≠ - (ref I) ? | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) ? | ≠ - (ref A/R) ? | ≠ C (ref R) ? | = ? | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ - (ref R) ? | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ - (ref A/R) | ≠ C (ref R) | = | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = ? | = | ≠ - (ref C) ? | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ C (ref R) ? | ≠ - (ref C) | ≠ - (ref I) | ≠ A (ref C) ? | ≠ - (ref I) | ≠ C (ref A/R) ? | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | = ? | ≠ - (ref C) | ≠ - (ref C) ? | ≠ R (ref A/R) ? | ≠ - (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | = ? | ≠ - (ref C) | ≠ - (ref C) | = ? | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ - (ref R) ? | ≠ A/R (ref A) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | ≠ - (ref C) | ≠ - (ref A/R) ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ C (ref A/R) ? | ≠ - (ref R) | = ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = ? | ≠ - (ref R) | ≠ - (ref R) ? | = ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | ≠ - (ref C) | ≠ - (ref R) ? | = ? | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT20 Ejecutar la reversión | ≠ R (ref C) ? | ≠ - (ref C) | ≠ - (ref A/R) ? | ≠ A (ref C) ? | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |

### Especializados, fase 2 (tras deliberación) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | ≠ C (ref A/R) | ≠ - (ref C) ? | ≠ - (ref C) | ≠ A/R (ref C) | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | = ? | ≠ - (ref I) | ≠ I (ref C) ? | = ? | = ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | ≠ R (ref A/R) ? | = ? | ≠ - (ref C) | ≠ I (ref C) ? | ≠ A (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) | ≠ I (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) | = ? | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) ? | = ? | ≠ - (ref R) ? | = ? | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ - (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ - (ref A/R) | ≠ C (ref R) | = | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | = ? | ≠ - (ref C) ? | ≠ - (ref I) ? | ≠ A (ref C) ? | ≠ - (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | = ? | ≠ - (ref C) | ≠ - (ref C) ? | ≠ A (ref A/R) ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | = | ≠ - (ref C) | ≠ - (ref C) ? | = ? | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ - (ref R) ? | ≠ A/R (ref A) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | ≠ - (ref C) | ≠ R (ref A/R) ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ C (ref A/R) ? | ≠ - (ref R) | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = ? | ≠ - (ref R) | ≠ - (ref R) ? | = ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | ≠ - (ref C) | ≠ - (ref R) | = ? | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT20 Ejecutar la reversión | ≠ R (ref C) ? | ≠ - (ref C) | ≠ - (ref A/R) ? | ≠ A (ref C) ? | ≠ C (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |

### Especializados, fase 2c (control sin deliberación) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | ≠ C (ref A/R) ? | ≠ - (ref C) ? | ≠ - (ref C) | ≠ A/R (ref C) ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) ? | ≠ - (ref C) ? | ≠ - (ref I) | ≠ - (ref C) ? | = ? | = ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | ≠ R (ref A/R) ? | = ? | ≠ - (ref C) | = ? | ≠ A (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) | ≠ I (ref C) ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) | ≠ - (ref I) ? | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) ? | ≠ - (ref A/R) ? | ≠ - (ref R) ? | = ? | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ - (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ - (ref A/R) | ≠ C (ref R) | = | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = ? | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ C (ref R) ? | ≠ - (ref C) ? | ≠ - (ref I) ? | = ? | ≠ - (ref I) | ≠ C (ref A/R) ? | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | = ? | ≠ - (ref C) | ≠ - (ref C) ? | ≠ A (ref A/R) ? | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | = ? | ≠ - (ref C) | ≠ - (ref C) ? | = ? | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ - (ref R) ? | ≠ A/R (ref A) | = ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | ≠ - (ref C) | ≠ C (ref A/R) ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ C (ref A/R) ? | ≠ - (ref R) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = ? | ≠ - (ref R) | ≠ - (ref R) ? | = ? | ≠ I (ref C) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = ? | ≠ - (ref C) | ≠ - (ref R) ? | = ? | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) ? | ≠ - (ref C) | ≠ - (ref A/R) ? | = ? | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |

### Árbitro, fase 3 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | ≠ C (ref A/R) | ≠ - (ref C) ? | ≠ - (ref C) | ≠ A/R (ref C) | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ - (ref C) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ I (ref C) ? | = ? | = ? | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | ≠ R (ref A/R) ? | ≠ R (ref C) ? | ≠ - (ref C) | = | ≠ A (ref C) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) | ≠ I (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) ? | = ? | ≠ - (ref R) ? | ≠ C (ref I) ? | ≠ - (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ - (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ - (ref A/R) | ≠ C (ref R) | = | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ - (ref C) | = | ≠ - (ref C) | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | = ? | ≠ - (ref C) ? | ≠ - (ref I) ? | ≠ A (ref C) ? | ≠ - (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | = ? | ≠ - (ref C) | ≠ - (ref C) ? | = ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | = | ≠ - (ref C) | = ? | = ? | = | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ - (ref R) ? | ≠ A/R (ref A) | = ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | ≠ - (ref C) | ≠ R (ref A/R) ? | = ? | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) ? | ≠ C (ref A/R) ? | ≠ - (ref R) | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = ? | ≠ - (ref R) | ≠ - (ref R) ? | = ? | ≠ I (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | ≠ - (ref C) | ≠ - (ref R) | = | = ? | ≠ - (ref I) | ≠ - (ref A) |
| ACT20 Ejecutar la reversión | ≠ R (ref C) ? | ≠ - (ref C) | ≠ - (ref A/R) ? | ≠ A (ref C) ? | ≠ C (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |

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
