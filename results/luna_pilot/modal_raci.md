# Matriz RACI modal

Cada celda muestra el rol más frecuente de la unidad en la actividad y su frecuencia sobre todas las decisiones del grupo, acumulando los escenarios en que aparece la actividad. '?' marca una celda inestable (rol modal < 60 %); '·' indica sin rol. Rol por decisión: A/R > A > R > C > I. La matriz modal describe lo que el modelo produce con este corpus; no es la asignación correcta. El desglose por escenario está en `modal_raci.csv`.

Unidades: DAS, ISC y MCO agrupan sus secciones; TX_REG = departamentos regionales de Transmisión; NEW_AUTHORITY = PROPOSED_NEW_AUTHORITY; OTHER = unidad no incluida en el corpus.

## Especializados, fase 1 (independiente)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | DEN | OP | GERENCIA_TECNICA | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 55% ? | · 50% ? | C 62% | A/R 42% ? | · | · | C 75% | · | · | I 72% | · | · | 40 |
| ACT02 Certificar los datos de la instalación (configur | I 78% | · | · | I 65% | · | A/R 90% | · 48% ? | C 60% | · | · | · | · | 40 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 95% | C 45% ? | I 55% ? | I 75% | · | C 80% | C 80% | C 85% | · | · | · | · | 20 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · 55% ? | · 45% ? | I 73% | · | C 77% | C 75% | C 90% | · | · | · | · | 60 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 72% | · | · 55% ? | C 50% ? | · | C 78% | C 72% | C 68% | · | · | · | · | 40 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 66% | R 54% ? | R 41% ? | C 96% | · | · | C 52% ? | · | · | I 61% | · | · | 80 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 80% | R 55% ? | C 70% | C 100% | · | · | · | · | · | I 80% | · | · | 20 |
| ACT08 Preparar el paquete de implementación | A/R 100% | C 60% | C 100% | C 80% | · | · | · | · | · | I 80% | · | · | 20 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 77% | A/R 90% | R 67% | C 98% | · | · | C 45% ? | · | · | I 78% | · | · | 60 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 85% | C 80% | · | · | I 60% | · | · | · | · | · | 20 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 98% | · | · | C 97% | · | · | C 90% | · | · | · | · | · | 60 |
| ACT12 Verificar la correspondencia de mímicos y modelo | A/R 45% ? | R 38% ? | C 38% ? | C 90% | · | C 80% | I 38% ? | · | · | I 50% ? | · | · | 40 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | R 78% | C 52% ? | R 82% | A/R 78% | · | C 60% | C 55% ? | · | · | I 78% | · | · | 40 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 73% | · 48% ? | C 88% | C 95% | · | · | C 63% | · | · | I 78% | · | · | 60 |
| ACT15 Habilitar o suspender la ventana de intervención | C 92% | · | C 79% | A/R 98% | · | · | C 72% | · | · | I 82% | · | · | 80 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 80% | C 52% ? | R 52% ? | C 100% | · | · | C 62% | · | · | I 82% | · | · | 40 |
| ACT17 Mantener el registro técnico de configuración | A/R 85% | C 45% ? | · 55% ? | · 45% ? | · | · | · 45% ? | · | · | · | · | · | 20 |
| ACT18 Verificar el sistema después de la actualización | A/R 100% | · 50% ? | R 40% ? | R 65% | · | · | C 80% | · | · | I 88% | · | · | 40 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 55% ? | · 52% ? | C 88% | C 88% | · | · | C 62% | · | · | I 88% | · | A 52% ? | 40 |
| ACT20 Ejecutar la reversión | A/R 100% | C 48% ? | R 70% | C 100% | · | · | C 70% | · | · | I 88% | · | · | 40 |

Celdas inestables: 35 de 240.

## Neutral, fase 1

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | DEN | OP | GERENCIA_TECNICA | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 70% | · | C 70% | C 50% ? | · | · | C 80% | · | · | I 90% | · | · | 10 |
| ACT02 Certificar los datos de la instalación (configur | I 80% | · | · | I 70% | · | A/R 100% | C 50% ? | C 70% | · | · | · | · | 10 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 80% | C 60% | · | I 60% | · | C 60% | C 80% | C 80% | · | · | · | · | 5 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · | · | I 60% | · | C 73% | C 100% | C 100% | · | · | · | · | 15 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 80% | · | · | C 60% | · | C 70% | C 80% | C 70% | · | · | · | · | 10 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 85% | R 55% ? | R 60% | C 100% | · | · | C 65% | · | · | I 70% | · | · | 20 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 100% | R 80% | C 60% | C 100% | · | · | · | · | · | I 100% | · | · | 5 |
| ACT08 Preparar el paquete de implementación | A/R 100% | · | C 100% | C 60% | · | · | · | · | · | I 80% | · | · | 5 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 67% | A/R 87% | R 73% | C 100% | · | · 47% ? | C 60% | · | · | I 80% | · | · | 15 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 80% | C 100% | · | · | C 40% ? | · | · | I 80% | · | · | 5 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 100% | · | · 53% ? | C 93% | · | · | C 93% | · 53% ? | · | I 53% ? | · | · | 15 |
| ACT12 Verificar la correspondencia de mímicos y modelo | A/R 50% ? | C 50% ? | A/R 40% ? | C 100% | · | C 40% ? | C 60% | · 50% ? | · | · | · | · | 10 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | R 90% | C 50% ? | R 70% | A/R 70% | · | C 60% | · 50% ? | · | · | I 70% | · | · | 10 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 67% | · | C 93% | C 100% | · | · | C 60% | · | · | I 87% | · | · | 15 |
| ACT15 Habilitar o suspender la ventana de intervención | C 80% | · | C 90% | A/R 95% | · | · | C 75% | · | · | I 85% | · | · | 20 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 100% | C 70% | R 60% | C 100% | · | · | C 60% | · | · | I 100% | · | · | 10 |
| ACT17 Mantener el registro técnico de configuración | A/R 100% | R 40% ? | · | C 40% ? | · | · | C 80% | · | · | · | · | · | 5 |
| ACT18 Verificar el sistema después de la actualización | A/R 100% | C 50% ? | C 50% ? | R 80% | · | · | C 90% | · | · | I 90% | · | · | 10 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 70% | C 60% | C 100% | C 100% | · | · | C 70% | · | · | I 100% | · | A 70% | 10 |
| ACT20 Ejecutar la reversión | A/R 100% | C 60% | R 60% | C 100% | · | · | C 90% | · | · | I 100% | · | · | 10 |

Celdas inestables: 19 de 240.

## Especializados, fase 2 (tras deliberación)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | DEN | OP | GERENCIA_TECNICA | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 65% | C 55% ? | C 80% | R 62% | · | · | C 92% | · | C 50% ? | I 90% | · | · | 40 |
| ACT02 Certificar los datos de la instalación (configur | I 92% | · 50% ? | · | I 90% | C 78% | A/R 98% | C 57% ? | C 82% | · | · | · | · | 40 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 100% | C 85% | I 65% | I 70% | · | C 85% | C 100% | C 100% | · | · | · | · | 20 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | C 47% ? | C 35% ? | I 70% | · | C 97% | C 98% | C 100% | · | · | · | · | 60 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 100% | · | · 48% ? | C 75% | · | C 98% | C 90% | C 90% | · | · | · | · | 40 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 68% | R 71% | R 38% ? | C 100% | · | · | C 78% | · | · | I 94% | · | · | 80 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 75% | R 70% | C 75% | C 100% | · | · | · | · | · | I 100% | · | · | 20 |
| ACT08 Preparar el paquete de implementación | A/R 100% | C 80% | C 100% | C 100% | · | · | · | · | · | I 100% | · | · | 20 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 63% | A/R 92% | R 90% | C 98% | · | · | C 72% | · | · | I 98% | · | · | 60 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 100% | C 100% | · | · | C 60% | · | · | I 50% ? | · | · | 20 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 100% | · | · | C 98% | · | · | C 98% | C 50% ? | · | I 65% | · | · | 60 |
| ACT12 Verificar la correspondencia de mímicos y modelo | C 45% ? | R 55% ? | A/R 42% ? | C 100% | · 52% ? | C 80% | I 40% ? | · 55% ? | · | I 82% | · | · | 40 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | R 98% | C 82% | R 100% | A/R 98% | · | C 80% | C 65% | · | · | I 95% | · | · | 40 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 75% | C 55% ? | C 93% | C 100% | · | · | C 77% | · | · | I 97% | · | · | 60 |
| ACT15 Habilitar o suspender la ventana de intervención | C 94% | · | C 94% | A/R 100% | · | · | C 88% | · | · | I 99% | · | · | 80 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 72% | C 88% | R 68% | C 100% | · | · | C 70% | · | · | I 100% | · | · | 40 |
| ACT17 Mantener el registro técnico de configuración | A/R 95% | C 70% | · | C 50% ? | · | · | C 50% ? | · | · | I 80% | · | · | 20 |
| ACT18 Verificar el sistema después de la actualización | A/R 100% | C 57% ? | R 50% ? | R 95% | · | · | C 92% | · | · | I 100% | · | · | 40 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 80% | C 57% ? | C 92% | C 98% | · | · | C 82% | · | · | I 100% | · | A 80% | 40 |
| ACT20 Ejecutar la reversión | A/R 100% | C 72% | R 90% | C 100% | · | · | C 92% | · | · | I 100% | · | · | 40 |

Celdas inestables: 22 de 240.

## Especializados, fase 2c (control sin deliberación)

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | DEN | OP | GERENCIA_TECNICA | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 57% ? | · 48% ? | C 72% | A/R 42% ? | · | · | C 82% | · | · 55% ? | I 80% | · | · | 40 |
| ACT02 Certificar los datos de la instalación (configur | I 82% | · | · | I 68% | C 60% | A/R 92% | · 45% ? | C 65% | · | · | · | · | 40 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 95% | C 45% ? | I 55% ? | I 75% | · | C 90% | C 85% | C 90% | · | · | · | · | 20 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | · 48% ? | · 43% ? | I 73% | · | C 85% | C 77% | C 92% | · | · | · | · | 60 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 85% | · | · 52% ? | C 50% ? | · | C 82% | C 72% | C 80% | · | · | · | · | 40 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 68% | R 61% | R 41% ? | C 99% | · | · | C 54% ? | · | · | I 66% | · | · | 80 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 55% ? | A/R 45% ? | C 70% | C 100% | · | · | · | · | · | I 85% | · | · | 20 |
| ACT08 Preparar el paquete de implementación | A/R 100% | C 55% ? | C 95% | C 80% | · | · | · | · | · | I 80% | · | · | 20 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 73% | A/R 88% | R 72% | C 98% | · | · | C 52% ? | · | · | I 82% | · | · | 60 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 80% | C 80% | · | · | I 60% | · | · | · | · | · | 20 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 98% | · | · | C 93% | · | · | C 88% | · 58% ? | · | · | · | · | 60 |
| ACT12 Verificar la correspondencia de mímicos y modelo | R 40% ? | A/R 32% ? | C 38% ? | C 90% | · 57% ? | C 72% | · 35% ? | · | · | I 55% ? | · | · | 40 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | R 78% | C 57% ? | R 82% | A/R 92% | · | C 68% | C 55% ? | · | · | I 80% | · | · | 40 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 78% | C 48% ? | C 87% | C 95% | · | · | C 67% | · | · | I 80% | · | · | 60 |
| ACT15 Habilitar o suspender la ventana de intervención | C 94% | · | C 81% | A/R 96% | · | · | C 72% | · | · | I 84% | · | · | 80 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 68% | C 50% ? | R 55% ? | C 100% | · | · | C 62% | · | · | I 88% | · | · | 40 |
| ACT17 Mantener el registro técnico de configuración | A/R 85% | C 55% ? | · | · 40% ? | · | · | · 50% ? | · | · | · | · | · | 20 |
| ACT18 Verificar el sistema después de la actualización | A/R 100% | · 50% ? | R 52% ? | R 68% | · | · | C 82% | · | · | I 88% | · | · | 40 |
| ACT19 Aprobar los criterios de reversión y su delegaci | A/R 50% ? | · 52% ? | C 85% | C 88% | · | · | C 68% | · | · | I 90% | · | · 50% ? | 40 |
| ACT20 Ejecutar la reversión | A/R 100% | C 52% ? | R 88% | C 100% | · | · | C 72% | · | · | I 92% | · | · | 40 |

Celdas inestables: 38 de 240.

## Árbitro, fase 3

| Actividad | DAS | ISC | MCO | ODC | TX_REG | DT | DOS | DEL | DEN | OP | GERENCIA_TECNICA | NEW_AUTHORITY | n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del cambio | A/R 60% | · | C 70% | R 50% ? | · | · | C 90% | · | C 50% ? | I 90% | · | · | 10 |
| ACT02 Certificar los datos de la instalación (configur | I 100% | C 50% ? | · | I 90% | C 90% | A/R 90% | C 60% | C 70% | · | · | · | · | 10 |
| ACT03 Especificar y aceptar la semántica del modelo (n | A/R 100% | C 100% | · | I 100% | · | C 60% | C 100% | C 100% | · | · | · | · | 5 |
| ACT04 Construir o actualizar el modelo eléctrico (topo | A/R 100% | C 60% | C 47% ? | I 73% | · | C 93% | C 100% | C 100% | · | I 53% ? | · | · | 15 |
| ACT05 Revisar la calidad topológica y de nomenclatura  | A/R 100% | · | · 50% ? | C 80% | · | C 80% | C 90% | C 100% | · | · | · | · | 10 |
| ACT06 Configurar la adquisición, la correspondencia se | A/R 60% | R 70% | A/R 30% ? | C 100% | · | · | C 75% | · | · | I 100% | · | · | 20 |
| ACT07 Unificar modelo y adquisición en la base integra | A/R 60% | R 60% | C 80% | C 100% | · | · | · | · | · | I 100% | · | · | 5 |
| ACT08 Preparar el paquete de implementación | A/R 100% | C 80% | C 100% | C 100% | · | · | · | · | · | I 100% | · | · | 5 |
| ACT09 Aprobar las pruebas FAT/SAT y de integración | C 73% | A/R 93% | R 87% | C 100% | · | · | C 73% | · | · | I 100% | · | · | 15 |
| ACT10 Administrar y actualizar los aplicativos EMS | A/R 100% | · | C 100% | C 100% | · | · | C 60% | · | · | I 60% | · | · | 5 |
| ACT11 Validar el estimador de estado, el flujo de pote | A/R 100% | · | · | C 100% | · | · | C 100% | · 53% ? | · | I 80% | · | · | 15 |
| ACT12 Verificar la correspondencia de mímicos y modelo | C 50% ? | R 40% ? | R 50% ? | C 100% | C 50% ? | C 80% | C 40% ? | C 50% ? | · | I 90% | · | · | 10 |
| ACT13 Aceptar mímicos, alarmas y el uso operativo | R 100% | C 100% | R 100% | A/R 100% | · | C 70% | C 60% | · | · | I 100% | · | · | 10 |
| ACT14 Autorizar la liberación de la versión a producci | A/R 67% | C 53% ? | C 87% | C 100% | · | · | C 67% | · | · | I 100% | · | · | 15 |
| ACT15 Habilitar o suspender la ventana de intervención | C 100% | · | C 100% | A/R 100% | · | · | C 90% | · | · | I 100% | · | · | 20 |
| ACT16 Ejecutar el respaldo y la carga en producción | A/R 70% | C 90% | R 70% | C 100% | · | · | C 70% | · | · | I 100% | · | · | 10 |
| ACT17 Mantener el registro técnico de configuración | A/R 100% | C 100% | · | I 60% | · | · | · | · | · | I 80% | · | · | 5 |
| ACT18 Verificar el sistema después de la actualización | A/R 100% | C 50% ? | R 50% ? | R 100% | · | · | C 90% | · | · | I 100% | · | · | 10 |
| ACT19 Aprobar los criterios de reversión y su delegaci | R 90% | C 50% ? | C 80% | C 100% | · | · | C 80% | · | · | I 100% | · | A 80% | 10 |
| ACT20 Ejecutar la reversión | A/R 100% | C 80% | R 100% | C 100% | · | · | C 90% | · | · | I 100% | · | · | 10 |

Celdas inestables: 18 de 240.

## Comparación celda a celda con REFERENCE_RACI (post hoc)

REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Columnas agrupadas como en el artículo: GT_SUPPORT = DOS, DEL, DEN, DDR; ORIGIN = TX_REG, DT, OTHER; NEW_AUTHORITY = Autoridad de Cambio. DEL y DOS se cuentan en GT_SUPPORT aunque el artículo también los admite como origen de parámetros (aproximación).

Formato: `=` coincide con la referencia; `≠ X (ref Y)` difiere, con el rol modal X y el de la referencia Y.

| Grupo | Celdas idénticas | Celdas A/R idénticas | A de la referencia recuperada | Celdas inestables |
|---|---|---|---|---|
| Especializados, fase 1 (independiente) | 31.4 % | 77.1 % | 55.0 % | 32 de 140 |
| Neutral, fase 1 | 33.6 % | 77.1 % | 55.0 % | 15 de 140 |
| Especializados, fase 2 (tras deliberación) | 35.7 % | 76.4 % | 55.0 % | 15 de 140 |
| Especializados, fase 2c (control sin deliberación) | 32.1 % | 77.1 % | 55.0 % | 33 de 140 |
| Árbitro, fase 3 | 35.7 % | 75.7 % | 55.0 % | 12 de 140 |

Celdas idénticas: mismo rol exacto. Celdas A/R idénticas: mismo rol ejecutivo (A/R, A, R), tratando C, I y sin rol como una misma clase. A recuperada: proporción de celdas A de la referencia en las que el rol modal incluye A.

### Especializados, fase 1 (independiente) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = ? | ≠ - (ref C) ? | = | ≠ A/R (ref C) ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | = ? | ≠ I (ref C) ? | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) ? | ≠ - (ref C) ? | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) ? | ≠ C (ref I) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) | ≠ R (ref A/R) ? | = ? | ≠ C (ref I) | ≠ C (ref I) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ R (ref A/R) ? | ≠ C (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ C (ref R) | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ R (ref C) | = | = ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | ≠ I (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ A/R (ref R) ? | ≠ R (ref C) ? | ≠ C (ref I) ? | = | ≠ C (ref I) ? | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ R (ref C) | = ? | ≠ R (ref C) | = | = | = | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) | ≠ - (ref C) ? | = | = | = | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ C (ref R) | ≠ A/R (ref A) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | = ? | ≠ R (ref A/R) ? | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ C (ref A/R) ? | ≠ - (ref R) ? | ≠ - (ref I) ? | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = | ≠ - (ref R) ? | = ? | ≠ R (ref C) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = ? | ≠ - (ref C) ? | ≠ C (ref R) | = | = | ≠ - (ref I) | = ? |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) | = ? | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |

### Neutral, fase 1 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = | ≠ - (ref C) | = | = ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | = | ≠ - (ref C) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) | ≠ - (ref C) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) | ≠ C (ref I) | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) | ≠ R (ref A/R) ? | = | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ R (ref A/R) | ≠ C (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ - (ref A/R) | ≠ C (ref R) | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ R (ref C) | = | = | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | = ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) ? | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ A/R (ref R) ? | = ? | ≠ A/R (ref I) ? | = | ≠ C (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ R (ref C) | = ? | ≠ R (ref C) | = | = ? | = | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) | ≠ - (ref C) | = | = | = | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ C (ref R) | ≠ A/R (ref A) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | = | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ R (ref A/R) ? | ≠ - (ref R) | ≠ C (ref I) ? | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = | ≠ C (ref R) ? | ≠ C (ref R) ? | ≠ R (ref C) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | = | ≠ C (ref R) | = | = | ≠ - (ref I) | = |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) | = | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |

### Especializados, fase 2 (tras deliberación) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = | = ? | = | ≠ R (ref C) | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ I (ref C) | ≠ - (ref C) ? | ≠ - (ref I) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | = | ≠ I (ref C) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | = ? | = ? | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) | ≠ R (ref A/R) | = ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ R (ref A/R) | ≠ C (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ C (ref R) | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ R (ref C) | = | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ C (ref R) ? | ≠ R (ref C) ? | ≠ A/R (ref I) ? | = | ≠ C (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ R (ref C) | = | ≠ R (ref C) | = | = | = | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) | = ? | = | = | = | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ C (ref R) | ≠ A/R (ref A) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | = | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ C (ref A/R) | ≠ - (ref R) | ≠ C (ref I) ? | ≠ C (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = | ≠ C (ref R) ? | = ? | ≠ R (ref C) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | = ? | ≠ C (ref R) | = | = | ≠ - (ref I) | = |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) | = | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |

### Especializados, fase 2c (control sin deliberación) frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = ? | ≠ - (ref C) ? | = | ≠ A/R (ref C) ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ I (ref C) | ≠ - (ref C) | ≠ - (ref I) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | = ? | ≠ I (ref C) ? | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | ≠ - (ref C) ? | ≠ - (ref C) ? | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) ? | ≠ C (ref I) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) | ≠ R (ref A/R) | = ? | ≠ C (ref I) | ≠ C (ref I) ? | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) ? | = ? | ≠ C (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ C (ref A/R) ? | ≠ C (ref R) | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ R (ref C) | = | = ? | ≠ - (ref C) ? | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | ≠ I (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | = ? | ≠ A/R (ref C) ? | ≠ C (ref I) ? | = | ≠ C (ref I) ? | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ R (ref C) | = ? | ≠ R (ref C) | = | = | = | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) | = ? | = | = | = | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ C (ref R) | ≠ A/R (ref A) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | = ? | ≠ R (ref A/R) ? | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ C (ref A/R) ? | ≠ - (ref R) | ≠ - (ref I) ? | ≠ - (ref I) ? | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = | ≠ - (ref R) ? | = ? | ≠ R (ref C) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | ≠ A/R (ref R) ? | ≠ - (ref C) ? | ≠ C (ref R) | = | = | ≠ - (ref I) | ≠ - (ref A) ? |
| ACT20 Ejecutar la reversión | ≠ A/R (ref C) | = ? | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |

### Árbitro, fase 3 frente a REFERENCE_RACI

| Actividad | DAS | ISC | MCO | ODC | GT_SUPPORT | ORIGIN | NEW_AUTHORITY |
|---|---|---|---|---|---|---|---|
| ACT01 Definir el requisito y el alcance del ca | = | ≠ - (ref C) | = | ≠ R (ref C) ? | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT02 Certificar los datos de la instalación ( | ≠ I (ref C) | = ? | ≠ - (ref I) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT03 Especificar y aceptar la semántica del m | = | = | ≠ - (ref C) | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT04 Construir o actualizar el modelo eléctri | = | = | = ? | ≠ I (ref C) | = | = | ≠ - (ref I) |
| ACT05 Revisar la calidad topológica y de nomen | ≠ A/R (ref C) | ≠ - (ref A/R) | ≠ - (ref I) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref I) |
| ACT06 Configurar la adquisición, la correspond | ≠ A/R (ref C) | ≠ R (ref A/R) | ≠ A/R (ref R) ? | ≠ C (ref I) | ≠ C (ref I) | ≠ - (ref C) | ≠ - (ref I) |
| ACT07 Unificar modelo y adquisición en la base | ≠ A/R (ref R) | ≠ R (ref A/R) | ≠ C (ref R) | = | ≠ - (ref C) | ≠ - (ref I) | ≠ - (ref I) |
| ACT08 Preparar el paquete de implementación | ≠ A/R (ref R) | ≠ C (ref A/R) | ≠ C (ref R) | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT09 Aprobar las pruebas FAT/SAT y de integra | = | = | ≠ R (ref C) | = | = | ≠ - (ref C) | ≠ - (ref I) |
| ACT10 Administrar y actualizar los aplicativos | = | ≠ - (ref C) | ≠ C (ref R) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT11 Validar el estimador de estado, el flujo | = | ≠ - (ref C) | ≠ - (ref C) | = | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT12 Verificar la correspondencia de mímicos  | ≠ C (ref R) ? | ≠ R (ref C) ? | ≠ R (ref I) ? | = | ≠ C (ref I) | ≠ C (ref A/R) | ≠ - (ref I) |
| ACT13 Aceptar mímicos, alarmas y el uso operat | ≠ R (ref C) | = | ≠ R (ref C) | = | = | = | ≠ - (ref I) |
| ACT14 Autorizar la liberación de la versión a  | ≠ A/R (ref R) | = ? | = | = | = | ≠ - (ref I) | ≠ - (ref A) |
| ACT15 Habilitar o suspender la ventana de inte | = | ≠ - (ref I) | ≠ C (ref R) | ≠ A/R (ref A) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT16 Ejecutar el respaldo y la carga en produ | ≠ A/R (ref C) | = | ≠ R (ref A/R) | = | ≠ C (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT17 Mantener el registro técnico de configur | ≠ A/R (ref C) | ≠ C (ref A/R) | ≠ - (ref R) | = | ≠ - (ref I) | ≠ - (ref I) | ≠ - (ref I) |
| ACT18 Verificar el sistema después de la actua | = | ≠ C (ref R) ? | = ? | ≠ R (ref C) | = | ≠ - (ref I) | ≠ - (ref I) |
| ACT19 Aprobar los criterios de reversión y su  | = | = ? | ≠ C (ref R) | = | = | ≠ - (ref I) | = |
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
