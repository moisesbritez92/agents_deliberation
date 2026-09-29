# Ablación de nombres: `order_reversed` frente a `pilot` (fase 1)

Decisiones pareadas: 1075 (mismo run, escenario, actividad y agente) en 50 corridas. Solo cambia el nombre de las unidades (códigos neutros en la variante). IC 95 % por bootstrap pareado sobre corridas (4000 remuestreos). pp = puntos porcentuales.

## Estimando principal

Proporción de decisiones con DAS como A (5 agentes): **44.1 % → 46.2 %**, diferencia **+2.1 pp** [-0.4 pp, +4.7 pp].

## Proporción de decisiones en que cada unidad recibe la A

| Unidad | Base | Sin nombres | Diferencia | IC 95 % | Excluye 0 |
|---|---|---|---|---|---|
| DAS | 44.1 % | 46.2 % | +2.1 pp | [-0.4 pp, +4.7 pp] | no |
| ISC | 9.7 % | 16.1 % | +6.4 pp | [+4.4 pp, +8.7 pp] | sí |
| MCO | 3.3 % | 2.8 % | -0.6 pp | [-2.1 pp, +1.1 pp] | no |
| ODC | 24.9 % | 17.5 % | -7.4 pp | [-9.9 pp, -5.0 pp] | sí |
| OP | 10.0 % | 12.5 % | +2.5 pp | [+0.6 pp, +4.4 pp] | sí |
| DT | 2.6 % | 1.1 % | -1.5 pp | [-2.5 pp, -0.6 pp] | sí |
| TX_REG | 0.6 % | 0.0 % | -0.6 pp | [-1.0 pp, -0.2 pp] | sí |
| DEL | 2.2 % | 1.3 % | -0.9 pp | [-1.6 pp, -0.4 pp] | sí |
| DOS | 2.2 % | 2.3 % | +0.1 pp | [-1.7 pp, +1.9 pp] | no |
| DEN | 0.1 % | 0.2 % | +0.1 pp | [+0.0 pp, +0.3 pp] | no |
| GERENCIA_TECNICA | 0.3 % | 0.0 % | -0.3 pp | [-0.7 pp, +0.0 pp] | no |

## DAS como A, por agente

| Agentes | Base | Sin nombres | Diferencia | IC 95 % |
|---|---|---|---|---|
| especializados | 44.5 % | 46.9 % | +2.3 pp | [-0.1 pp, +4.9 pp] |
| neutral | 42.3 % | 43.7 % | +1.4 pp | [-5.6 pp, +8.1 pp] |
| DAS | 51.6 % | 57.7 % | +6.0 pp | [+2.4 pp, +9.7 pp] |
| ISC | 42.3 % | 38.6 % | -3.7 pp | [-9.6 pp, +1.9 pp] |
| MCO | 39.1 % | 43.7 % | +4.7 pp | [-1.4 pp, +10.7 pp] |
| ODC | 45.1 % | 47.4 % | +2.3 pp | [-2.8 pp, +7.7 pp] |

## Por escenario y actividad

| Esc. | Actividad | A modal base | A modal sin nombres | DAS base | DAS sin nombres | Δ DAS | Misma A (pareado) |
|---|---|---|---|---|---|---|---|
| S01 | ACT02 Certificar los datos de la instalación | DT (68 %) | ISC (52 %) | 4.0 % | 0.0 % | -4.0 pp | 20.0 % |
| S01 | ACT04 Construir o actualizar el modelo eléct | DAS (100 %) | DAS (96 %) | 100.0 % | 96.0 % | -4.0 pp | 96.0 % |
| S01 | ACT06 Configurar la adquisición, la correspo | DAS (44 %) | DAS (44 %) | 44.0 % | 44.0 % | +0.0 pp | 56.0 % |
| S01 | ACT09 Aprobar las pruebas FAT/SAT y de integ | ISC (88 %) | ISC (92 %) | 4.0 % | 0.0 % | -4.0 pp | 80.0 % |
| S01 | ACT12 Verificar la correspondencia de mímico | ODC (68 %) | ISC (28 %) | 12.0 % | 8.0 % | -4.0 pp | 32.0 % |
| S02 | ACT02 Certificar los datos de la instalación | DEL (56 %) | DEL (52 %) | 0.0 % | 8.0 % | +8.0 pp | 28.0 % |
| S02 | ACT04 Construir o actualizar el modelo eléct | DAS (100 %) | DAS (100 %) | 100.0 % | 100.0 % | +0.0 pp | 100.0 % |
| S02 | ACT05 Revisar la calidad topológica y de nom | DAS (68 %) | DAS (96 %) | 68.0 % | 96.0 % | +28.0 pp | 64.0 % |
| S02 | ACT11 Validar el estimador de estado, el flu | DAS (96 %) | DAS (96 %) | 96.0 % | 96.0 % | +0.0 pp | 92.0 % |
| S03 | ACT06 Configurar la adquisición, la correspo | ISC (52 %) | ISC (52 %) | 40.0 % | 28.0 % | -12.0 pp | 64.0 % |
| S03 | ACT07 Unificar modelo y adquisición en la ba | DAS (96 %) | DAS (100 %) | 96.0 % | 100.0 % | +4.0 pp | 96.0 % |
| S03 | ACT09 Aprobar las pruebas FAT/SAT y de integ | ISC (64 %) | ISC (88 %) | 8.0 % | 8.0 % | +0.0 pp | 60.0 % |
| S03 | ACT13 Aceptar mímicos, alarmas y el uso oper | ODC (60 %) | OP (48 %) | 0.0 % | 0.0 % | +0.0 pp | 56.0 % |
| S04 | ACT06 Configurar la adquisición, la correspo | DAS (100 %) | DAS (92 %) | 100.0 % | 92.0 % | -8.0 pp | 92.0 % |
| S04 | ACT11 Validar el estimador de estado, el flu | DAS (100 %) | DAS (100 %) | 100.0 % | 100.0 % | +0.0 pp | 100.0 % |
| S04 | ACT17 Mantener el registro técnico de config | DAS (84 %) | DAS (76 %) | 84.0 % | 76.0 % | -8.0 pp | 68.0 % |
| S04 | ACT18 Verificar el sistema después de la act | DAS (52 %) | DAS (44 %) | 52.0 % | 44.0 % | -8.0 pp | 40.0 % |
| S05 | ACT01 Definir el requisito y el alcance del  | ODC (76 %) | DOS (44 %) | 0.0 % | 16.0 % | +16.0 pp | 16.0 % |
| S05 | ACT06 Configurar la adquisición, la correspo | DAS (80 %) | DAS (72 %) | 80.0 % | 72.0 % | -8.0 pp | 60.0 % |
| S05 | ACT09 Aprobar las pruebas FAT/SAT y de integ | ISC (60 %) | ISC (76 %) | 16.0 % | 16.0 % | +0.0 pp | 44.0 % |
| S05 | ACT15 Habilitar o suspender la ventana de in | ODC (100 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 100.0 % |
| S06 | ACT03 Especificar y aceptar la semántica del | DAS (32 %) | ISC (68 %) | 32.0 % | 32.0 % | +0.0 pp | 28.0 % |
| S06 | ACT04 Construir o actualizar el modelo eléct | DAS (100 %) | DAS (100 %) | 100.0 % | 100.0 % | +0.0 pp | 100.0 % |
| S06 | ACT05 Revisar la calidad topológica y de nom | DAS (80 %) | DAS (80 %) | 80.0 % | 80.0 % | +0.0 pp | 68.0 % |
| S06 | ACT12 Verificar la correspondencia de mímico | ISC (32 %) | ISC (56 %) | 24.0 % | 20.0 % | -4.0 pp | 32.0 % |
| S06 | ACT13 Aceptar mímicos, alarmas y el uso oper | ODC (68 %) | ODC (52 %) | 4.0 % | 4.0 % | +0.0 pp | 44.0 % |
| S07 | ACT10 Administrar y actualizar los aplicativ | DAS (100 %) | DAS (100 %) | 100.0 % | 100.0 % | +0.0 pp | 100.0 % |
| S07 | ACT11 Validar el estimador de estado, el flu | DAS (76 %) | DAS (88 %) | 76.0 % | 88.0 % | +12.0 pp | 80.0 % |
| S07 | ACT14 Autorizar la liberación de la versión  | OP (88 %) | OP (92 %) | 0.0 % | 4.0 % | +4.0 pp | 80.0 % |
| S07 | ACT19 Aprobar los criterios de reversión y s | OP (76 %) | OP (96 %) | 8.0 % | 4.0 % | -4.0 pp | 72.0 % |
| S08 | ACT08 Preparar el paquete de implementación | DAS (100 %) | DAS (84 %) | 100.0 % | 84.0 % | -16.0 pp | 84.0 % |
| S08 | ACT14 Autorizar la liberación de la versión  | OP (80 %) | OP (80 %) | 0.0 % | 8.0 % | +8.0 pp | 72.0 % |
| S08 | ACT15 Habilitar o suspender la ventana de in | ODC (100 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 100.0 % |
| S08 | ACT16 Ejecutar el respaldo y la carga en pro | DAS (88 %) | DAS (88 %) | 88.0 % | 88.0 % | +0.0 pp | 84.0 % |
| S09 | ACT15 Habilitar o suspender la ventana de in | ODC (100 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 100.0 % |
| S09 | ACT18 Verificar el sistema después de la act | DAS (76 %) | DAS (92 %) | 76.0 % | 92.0 % | +16.0 pp | 68.0 % |
| S09 | ACT19 Aprobar los criterios de reversión y s | OP (52 %) | OP (84 %) | 4.0 % | 8.0 % | +4.0 pp | 52.0 % |
| S09 | ACT20 Ejecutar la reversión | DAS (76 %) | DAS (92 %) | 76.0 % | 92.0 % | +16.0 pp | 68.0 % |
| S10 | ACT01 Definir el requisito y el alcance del  | ODC (80 %) | ODC (56 %) | 8.0 % | 16.0 % | +8.0 pp | 44.0 % |
| S10 | ACT14 Autorizar la liberación de la versión  | ODC (84 %) | ODC (72 %) | 0.0 % | 0.0 % | +0.0 pp | 64.0 % |
| S10 | ACT15 Habilitar o suspender la ventana de in | ODC (96 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 96.0 % |
| S10 | ACT16 Ejecutar el respaldo y la carga en pro | DAS (96 %) | DAS (100 %) | 96.0 % | 100.0 % | +4.0 pp | 96.0 % |
| S10 | ACT20 Ejecutar la reversión | ODC (72 %) | DAS (68 %) | 20.0 % | 68.0 % | +48.0 pp | 44.0 % |

## Estabilidad y acuerdo

- Decisiones pareadas con la misma A en ambas versiones: 68.4 %.
- Acuerdo entre especializados (pares con igual A): base 68.4 %, sin nombres 68.7 %.

## Sesgo hacia la propia unidad (frente al neutral)

En la variante, el agente conoce su foco técnico, pero no el nombre ni el código de su unidad.

| Agente | Base | Sin nombres |
|---|---|---|
| DAS | +0.093 | +0.140 |
| ISC | +0.074 | +0.098 |
| MCO | +0.019 | +0.060 |
| ODC | +0.093 | +0.093 |

## Coincidencia con la A de REFERENCE_RACI (post hoc)

- Base: 45.1 %; sin nombres: 44.6 %.

## Lectura

- Si la proporción de DAS baja de forma clara al quitar los nombres, parte de la concentración en DAS del piloto se explica por el nombre de la unidad y no por el contenido de sus atribuciones.
- Si no cambia (IC que incluye 0 y diferencia pequeña), la concentración se sostiene en el contenido de las fichas.
- La variante no elimina toda pista: el contenido funcional (p. ej., «administrar la base de datos del SCADA») sigue identificando a cada unidad. Mide el efecto del nombre, no el de la función.
