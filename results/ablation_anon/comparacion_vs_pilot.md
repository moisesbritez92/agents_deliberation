# Ablación de nombres: `ablation_anon` frente a `pilot` (fase 1)

Decisiones pareadas: 4300 (mismo run, escenario, actividad y agente) en 200 corridas. Solo cambia el nombre de las unidades (códigos neutros en la variante). IC 95 % por bootstrap pareado sobre corridas (4000 remuestreos). pp = puntos porcentuales.

## Estimando principal

Proporción de decisiones con DAS como A (5 agentes): **43.3 % → 28.5 %**, diferencia **-14.8 pp** [-17.2 pp, -12.4 pp].

## Proporción de decisiones en que cada unidad recibe la A

| Unidad | Base | Sin nombres | Diferencia | IC 95 % | Excluye 0 |
|---|---|---|---|---|---|
| DAS | 43.3 % | 28.5 % | -14.8 pp | [-17.2 pp, -12.4 pp] | sí |
| ISC | 10.4 % | 8.8 % | -1.6 pp | [-2.8 pp, -0.3 pp] | sí |
| MCO | 3.2 % | 32.2 % | +29.0 pp | [+26.6 pp, +31.4 pp] | sí |
| ODC | 25.5 % | 20.8 % | -4.7 pp | [-5.9 pp, -3.5 pp] | sí |
| OP | 9.6 % | 5.4 % | -4.2 pp | [-5.5 pp, -2.9 pp] | sí |
| DT | 2.4 % | 0.4 % | -2.0 pp | [-2.8 pp, -1.3 pp] | sí |
| TX_REG | 0.3 % | 0.4 % | +0.2 pp | [-0.1 pp, +0.4 pp] | no |
| DEL | 2.3 % | 1.2 % | -1.1 pp | [-1.5 pp, -0.7 pp] | sí |
| DOS | 2.7 % | 2.1 % | -0.6 pp | [-1.4 pp, +0.2 pp] | no |
| DEN | 0.0 % | 0.0 % | -0.0 pp | [-0.1 pp, +0.0 pp] | no |
| NEW_AUTHORITY | 0.0 % | 0.1 % | +0.1 pp | [-0.0 pp, +0.2 pp] | no |
| GERENCIA_TECNICA | 0.2 % | 0.0 % | -0.2 pp | [-0.4 pp, -0.1 pp] | sí |
| OTHER | 0.0 % | 0.0 % | -0.0 pp | [-0.1 pp, +0.0 pp] | no |

## DAS como A, por agente

| Agentes | Base | Sin nombres | Diferencia | IC 95 % |
|---|---|---|---|---|
| especializados | 43.4 % | 28.8 % | -14.6 pp | [-17.1 pp, -12.1 pp] |
| neutral | 43.3 % | 27.4 % | -15.8 pp | [-19.6 pp, -12.0 pp] |
| DAS | 51.4 % | 36.5 % | -14.9 pp | [-19.1 pp, -10.9 pp] |
| ISC | 41.0 % | 25.1 % | -15.9 pp | [-19.5 pp, -12.4 pp] |
| MCO | 40.0 % | 27.1 % | -12.9 pp | [-16.5 pp, -9.2 pp] |
| ODC | 41.0 % | 26.5 % | -14.5 pp | [-18.0 pp, -11.2 pp] |

## Por escenario y actividad

| Esc. | Actividad | A modal base | A modal sin nombres | DAS base | DAS sin nombres | Δ DAS | Misma A (pareado) |
|---|---|---|---|---|---|---|---|
| S01 | ACT02 Certificar los datos de la instalación | DT (67 %) | ISC (60 %) | 2.0 % | 0.0 % | -2.0 pp | 15.0 % |
| S01 | ACT04 Construir o actualizar el modelo eléct | DAS (100 %) | DAS (93 %) | 100.0 % | 93.0 % | -7.0 pp | 93.0 % |
| S01 | ACT06 Configurar la adquisición, la correspo | ISC (48 %) | MCO (95 %) | 43.0 % | 1.0 % | -42.0 pp | 12.0 % |
| S01 | ACT09 Aprobar las pruebas FAT/SAT y de integ | ISC (89 %) | ISC (52 %) | 3.0 % | 0.0 % | -3.0 pp | 46.0 % |
| S01 | ACT12 Verificar la correspondencia de mímico | ODC (68 %) | MCO (60 %) | 15.0 % | 15.0 % | +0.0 pp | 23.0 % |
| S02 | ACT02 Certificar los datos de la instalación | DEL (66 %) | DEL (52 %) | 0.0 % | 0.0 % | +0.0 pp | 38.0 % |
| S02 | ACT04 Construir o actualizar el modelo eléct | DAS (99 %) | DAS (92 %) | 99.0 % | 92.0 % | -7.0 pp | 91.0 % |
| S02 | ACT05 Revisar la calidad topológica y de nom | DAS (73 %) | DAS (79 %) | 73.0 % | 79.0 % | +6.0 pp | 61.0 % |
| S02 | ACT11 Validar el estimador de estado, el flu | DAS (88 %) | DAS (93 %) | 88.0 % | 93.0 % | +5.0 pp | 84.0 % |
| S03 | ACT06 Configurar la adquisición, la correspo | ISC (49 %) | MCO (61 %) | 37.0 % | 0.0 % | -37.0 pp | 34.0 % |
| S03 | ACT07 Unificar modelo y adquisición en la ba | DAS (98 %) | DAS (66 %) | 98.0 % | 66.0 % | -32.0 pp | 66.0 % |
| S03 | ACT09 Aprobar las pruebas FAT/SAT y de integ | ISC (81 %) | MCO (65 %) | 3.0 % | 0.0 % | -3.0 pp | 36.0 % |
| S03 | ACT13 Aceptar mímicos, alarmas y el uso oper | ODC (63 %) | ODC (65 %) | 4.0 % | 0.0 % | -4.0 pp | 44.0 % |
| S04 | ACT06 Configurar la adquisición, la correspo | DAS (100 %) | MCO (59 %) | 100.0 % | 41.0 % | -59.0 pp | 41.0 % |
| S04 | ACT11 Validar el estimador de estado, el flu | DAS (100 %) | DAS (96 %) | 100.0 % | 96.0 % | -4.0 pp | 96.0 % |
| S04 | ACT17 Mantener el registro técnico de config | DAS (84 %) | ISC (47 %) | 84.0 % | 23.0 % | -61.0 pp | 27.0 % |
| S04 | ACT18 Verificar el sistema después de la act | ODC (45 %) | MCO (48 %) | 43.0 % | 8.0 % | -35.0 pp | 21.0 % |
| S05 | ACT01 Definir el requisito y el alcance del  | ODC (78 %) | OP (39 %) | 1.0 % | 3.0 % | +2.0 pp | 30.0 % |
| S05 | ACT06 Configurar la adquisición, la correspo | DAS (76 %) | MCO (83 %) | 76.0 % | 10.0 % | -66.0 pp | 17.0 % |
| S05 | ACT09 Aprobar las pruebas FAT/SAT y de integ | ISC (62 %) | MCO (66 %) | 14.0 % | 3.0 % | -11.0 pp | 24.0 % |
| S05 | ACT15 Habilitar o suspender la ventana de in | ODC (97 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 97.0 % |
| S06 | ACT03 Especificar y aceptar la semántica del | DOS (32 %) | ISC (55 %) | 22.0 % | 27.0 % | +5.0 pp | 17.0 % |
| S06 | ACT04 Construir o actualizar el modelo eléct | DAS (100 %) | DAS (89 %) | 100.0 % | 89.0 % | -11.0 pp | 89.0 % |
| S06 | ACT05 Revisar la calidad topológica y de nom | DAS (80 %) | DAS (77 %) | 80.0 % | 77.0 % | -3.0 pp | 62.0 % |
| S06 | ACT12 Verificar la correspondencia de mímico | MCO (22 %) | MCO (54 %) | 18.0 % | 17.0 % | -1.0 pp | 27.0 % |
| S06 | ACT13 Aceptar mímicos, alarmas y el uso oper | ODC (75 %) | ODC (72 %) | 1.0 % | 3.0 % | +2.0 pp | 54.0 % |
| S07 | ACT10 Administrar y actualizar los aplicativ | DAS (100 %) | DAS (98 %) | 100.0 % | 98.0 % | -2.0 pp | 98.0 % |
| S07 | ACT11 Validar el estimador de estado, el flu | DAS (68 %) | DAS (80 %) | 68.0 % | 80.0 % | +12.0 pp | 63.0 % |
| S07 | ACT14 Autorizar la liberación de la versión  | OP (85 %) | OP (43 %) | 2.0 % | 24.0 % | +22.0 pp | 45.0 % |
| S07 | ACT19 Aprobar los criterios de reversión y s | OP (83 %) | OP (45 %) | 5.0 % | 24.0 % | +19.0 pp | 42.0 % |
| S08 | ACT08 Preparar el paquete de implementación | DAS (100 %) | DAS (60 %) | 100.0 % | 60.0 % | -40.0 pp | 60.0 % |
| S08 | ACT14 Autorizar la liberación de la versión  | OP (70 %) | MCO (58 %) | 11.0 % | 10.0 % | -1.0 pp | 16.0 % |
| S08 | ACT15 Habilitar o suspender la ventana de in | ODC (97 %) | ODC (98 %) | 0.0 % | 0.0 % | +0.0 pp | 95.0 % |
| S08 | ACT16 Ejecutar el respaldo y la carga en pro | DAS (81 %) | MCO (94 %) | 81.0 % | 6.0 % | -75.0 pp | 23.0 % |
| S09 | ACT15 Habilitar o suspender la ventana de in | ODC (100 %) | ODC (99 %) | 0.0 % | 0.0 % | +0.0 pp | 99.0 % |
| S09 | ACT18 Verificar el sistema después de la act | DAS (79 %) | MCO (79 %) | 79.0 % | 21.0 % | -58.0 pp | 21.0 % |
| S09 | ACT19 Aprobar los criterios de reversión y s | OP (53 %) | OP (39 %) | 9.0 % | 7.0 % | -2.0 pp | 23.0 % |
| S09 | ACT20 Ejecutar la reversión | DAS (78 %) | MCO (82 %) | 78.0 % | 17.0 % | -61.0 pp | 19.0 % |
| S10 | ACT01 Definir el requisito y el alcance del  | ODC (88 %) | ODC (78 %) | 6.0 % | 9.0 % | +3.0 pp | 68.0 % |
| S10 | ACT14 Autorizar la liberación de la versión  | ODC (86 %) | ODC (88 %) | 1.0 % | 0.0 % | -1.0 pp | 76.0 % |
| S10 | ACT15 Habilitar o suspender la ventana de in | ODC (99 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 99.0 % |
| S10 | ACT16 Ejecutar el respaldo y la carga en pro | DAS (95 %) | MCO (71 %) | 95.0 % | 29.0 % | -66.0 pp | 32.0 % |
| S10 | ACT20 Ejecutar la reversión | ODC (71 %) | ODC (61 %) | 25.0 % | 6.0 % | -19.0 pp | 47.0 % |

## Estabilidad y acuerdo

- Decisiones pareadas con la misma A en ambas versiones: 50.5 %.
- Acuerdo entre especializados (pares con igual A): base 68.6 %, sin nombres 61.3 %.

## Sesgo hacia la propia unidad (frente al neutral)

En la variante, el agente conoce su foco técnico, pero no el nombre ni el código de su unidad.

| Agente | Base | Sin nombres |
|---|---|---|
| DAS | +0.081 | +0.091 |
| ISC | +0.074 | +0.020 |
| MCO | +0.023 | +0.015 |
| ODC | +0.088 | +0.042 |

## Coincidencia con la A de REFERENCE_RACI (post hoc)

- Base: 45.1 %; sin nombres: 42.9 %.

## Lectura

- Si la proporción de DAS baja de forma clara al quitar los nombres, parte de la concentración en DAS del piloto se explica por el nombre de la unidad y no por el contenido de sus atribuciones.
- Si no cambia (IC que incluye 0 y diferencia pequeña), la concentración se sostiene en el contenido de las fichas.
- La variante no elimina toda pista: el contenido funcional (p. ej., «administrar la base de datos del SCADA») sigue identificando a cada unidad. Mide el efecto del nombre, no el de la función.
