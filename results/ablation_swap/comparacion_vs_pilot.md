# Ablación de nombres: `ablation_swap` frente a `pilot` (fase 1)

Decisiones pareadas: 1075 (mismo run, escenario, actividad y agente) en 50 corridas. Solo cambia el nombre de las unidades (códigos neutros en la variante). IC 95 % por bootstrap pareado sobre corridas (4000 remuestreos). pp = puntos porcentuales.

## Estimando principal

Proporción de decisiones con DAS como A (5 agentes): **44.1 % → 45.1 %**, diferencia **+1.0 pp** [-2.2 pp, +4.2 pp].

## Proporción de decisiones en que cada unidad recibe la A

| Unidad | Base | Sin nombres | Diferencia | IC 95 % | Excluye 0 |
|---|---|---|---|---|---|
| DAS | 44.1 % | 45.1 % | +1.0 pp | [-2.2 pp, +4.2 pp] | no |
| ISC | 9.7 % | 10.6 % | +0.9 pp | [-0.8 pp, +2.8 pp] | no |
| MCO | 3.3 % | 8.8 % | +5.5 pp | [+3.2 pp, +7.8 pp] | sí |
| ODC | 24.9 % | 22.2 % | -2.7 pp | [-5.3 pp, -0.1 pp] | sí |
| OP | 10.0 % | 4.2 % | -5.8 pp | [-8.4 pp, -3.4 pp] | sí |
| DT | 2.6 % | 2.3 % | -0.3 pp | [-1.9 pp, +1.2 pp] | no |
| TX_REG | 0.6 % | 0.8 % | +0.3 pp | [-0.3 pp, +1.0 pp] | no |
| DEL | 2.2 % | 1.6 % | -0.7 pp | [-1.4 pp, +0.1 pp] | no |
| DOS | 2.2 % | 4.2 % | +2.0 pp | [+0.0 pp, +4.1 pp] | no |
| DEN | 0.1 % | 0.0 % | -0.1 pp | [-0.3 pp, +0.0 pp] | no |
| GERENCIA_TECNICA | 0.3 % | 0.0 % | -0.3 pp | [-0.7 pp, +0.0 pp] | no |
| OTHER | 0.0 % | 0.1 % | +0.1 pp | [+0.0 pp, +0.3 pp] | no |

## DAS como A, por agente

| Agentes | Base | Sin nombres | Diferencia | IC 95 % |
|---|---|---|---|---|
| especializados | 44.5 % | 44.5 % | +0.0 pp | [-3.1 pp, +3.1 pp] |
| neutral | 42.3 % | 47.4 % | +5.1 pp | [-0.9 pp, +11.3 pp] |
| DAS | 51.6 % | 52.6 % | +0.9 pp | [-4.6 pp, +6.7 pp] |
| ISC | 42.3 % | 41.4 % | -0.9 pp | [-7.0 pp, +4.6 pp] |
| MCO | 39.1 % | 40.9 % | +1.9 pp | [-6.0 pp, +9.3 pp] |
| ODC | 45.1 % | 43.3 % | -1.9 pp | [-7.5 pp, +4.1 pp] |

## Por escenario y actividad

| Esc. | Actividad | A modal base | A modal sin nombres | DAS base | DAS sin nombres | Δ DAS | Misma A (pareado) |
|---|---|---|---|---|---|---|---|
| S01 | ACT02 Certificar los datos de la instalación | DT (68 %) | DT (36 %) | 4.0 % | 0.0 % | -4.0 pp | 24.0 % |
| S01 | ACT04 Construir o actualizar el modelo eléct | DAS (100 %) | DAS (100 %) | 100.0 % | 100.0 % | +0.0 pp | 100.0 % |
| S01 | ACT06 Configurar la adquisición, la correspo | DAS (44 %) | DAS (40 %) | 44.0 % | 40.0 % | -4.0 pp | 40.0 % |
| S01 | ACT09 Aprobar las pruebas FAT/SAT y de integ | ISC (88 %) | ISC (96 %) | 4.0 % | 0.0 % | -4.0 pp | 84.0 % |
| S01 | ACT12 Verificar la correspondencia de mímico | ODC (68 %) | MCO (36 %) | 12.0 % | 4.0 % | -8.0 pp | 32.0 % |
| S02 | ACT02 Certificar los datos de la instalación | DEL (56 %) | DEL (68 %) | 0.0 % | 0.0 % | +0.0 pp | 40.0 % |
| S02 | ACT04 Construir o actualizar el modelo eléct | DAS (100 %) | DAS (96 %) | 100.0 % | 96.0 % | -4.0 pp | 96.0 % |
| S02 | ACT05 Revisar la calidad topológica y de nom | DAS (68 %) | DAS (88 %) | 68.0 % | 88.0 % | +20.0 pp | 64.0 % |
| S02 | ACT11 Validar el estimador de estado, el flu | DAS (96 %) | DAS (92 %) | 96.0 % | 92.0 % | -4.0 pp | 88.0 % |
| S03 | ACT06 Configurar la adquisición, la correspo | ISC (52 %) | ISC (60 %) | 40.0 % | 12.0 % | -28.0 pp | 40.0 % |
| S03 | ACT07 Unificar modelo y adquisición en la ba | DAS (96 %) | DAS (96 %) | 96.0 % | 96.0 % | +0.0 pp | 92.0 % |
| S03 | ACT09 Aprobar las pruebas FAT/SAT y de integ | ISC (64 %) | ISC (64 %) | 8.0 % | 0.0 % | -8.0 pp | 56.0 % |
| S03 | ACT13 Aceptar mímicos, alarmas y el uso oper | ODC (60 %) | ODC (80 %) | 0.0 % | 0.0 % | +0.0 pp | 48.0 % |
| S04 | ACT06 Configurar la adquisición, la correspo | DAS (100 %) | DAS (92 %) | 100.0 % | 92.0 % | -8.0 pp | 92.0 % |
| S04 | ACT11 Validar el estimador de estado, el flu | DAS (100 %) | DAS (96 %) | 100.0 % | 96.0 % | -4.0 pp | 96.0 % |
| S04 | ACT17 Mantener el registro técnico de config | DAS (84 %) | DAS (76 %) | 84.0 % | 76.0 % | -8.0 pp | 68.0 % |
| S04 | ACT18 Verificar el sistema después de la act | DAS (52 %) | ODC (44 %) | 52.0 % | 36.0 % | -16.0 pp | 36.0 % |
| S05 | ACT01 Definir el requisito y el alcance del  | ODC (76 %) | DOS (76 %) | 0.0 % | 8.0 % | +8.0 pp | 8.0 % |
| S05 | ACT06 Configurar la adquisición, la correspo | DAS (80 %) | DAS (88 %) | 80.0 % | 88.0 % | +8.0 pp | 68.0 % |
| S05 | ACT09 Aprobar las pruebas FAT/SAT y de integ | ISC (60 %) | ISC (40 %) | 16.0 % | 36.0 % | +20.0 pp | 24.0 % |
| S05 | ACT15 Habilitar o suspender la ventana de in | ODC (100 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 100.0 % |
| S06 | ACT03 Especificar y aceptar la semántica del | DAS (32 %) | ISC (40 %) | 32.0 % | 36.0 % | +4.0 pp | 24.0 % |
| S06 | ACT04 Construir o actualizar el modelo eléct | DAS (100 %) | DAS (92 %) | 100.0 % | 92.0 % | -8.0 pp | 92.0 % |
| S06 | ACT05 Revisar la calidad topológica y de nom | DAS (80 %) | DAS (84 %) | 80.0 % | 84.0 % | +4.0 pp | 68.0 % |
| S06 | ACT12 Verificar la correspondencia de mímico | ISC (32 %) | MCO (68 %) | 24.0 % | 4.0 % | -20.0 pp | 16.0 % |
| S06 | ACT13 Aceptar mímicos, alarmas y el uso oper | ODC (68 %) | ODC (92 %) | 4.0 % | 0.0 % | -4.0 pp | 68.0 % |
| S07 | ACT10 Administrar y actualizar los aplicativ | DAS (100 %) | DAS (100 %) | 100.0 % | 100.0 % | +0.0 pp | 100.0 % |
| S07 | ACT11 Validar el estimador de estado, el flu | DAS (76 %) | DAS (76 %) | 76.0 % | 76.0 % | +0.0 pp | 60.0 % |
| S07 | ACT14 Autorizar la liberación de la versión  | OP (88 %) | OP (48 %) | 0.0 % | 16.0 % | +16.0 pp | 40.0 % |
| S07 | ACT19 Aprobar los criterios de reversión y s | OP (76 %) | OP (32 %) | 8.0 % | 24.0 % | +16.0 pp | 20.0 % |
| S08 | ACT08 Preparar el paquete de implementación | DAS (100 %) | DAS (100 %) | 100.0 % | 100.0 % | +0.0 pp | 100.0 % |
| S08 | ACT14 Autorizar la liberación de la versión  | OP (80 %) | DAS (56 %) | 0.0 % | 56.0 % | +56.0 pp | 12.0 % |
| S08 | ACT15 Habilitar o suspender la ventana de in | ODC (100 %) | ODC (96 %) | 0.0 % | 0.0 % | +0.0 pp | 96.0 % |
| S08 | ACT16 Ejecutar el respaldo y la carga en pro | DAS (88 %) | DAS (52 %) | 88.0 % | 52.0 % | -36.0 pp | 56.0 % |
| S09 | ACT15 Habilitar o suspender la ventana de in | ODC (100 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 100.0 % |
| S09 | ACT18 Verificar el sistema después de la act | DAS (76 %) | DAS (80 %) | 76.0 % | 80.0 % | +4.0 pp | 60.0 % |
| S09 | ACT19 Aprobar los criterios de reversión y s | OP (52 %) | DAS (44 %) | 4.0 % | 44.0 % | +40.0 pp | 8.0 % |
| S09 | ACT20 Ejecutar la reversión | DAS (76 %) | DAS (76 %) | 76.0 % | 76.0 % | +0.0 pp | 60.0 % |
| S10 | ACT01 Definir el requisito y el alcance del  | ODC (80 %) | ODC (84 %) | 8.0 % | 12.0 % | +4.0 pp | 68.0 % |
| S10 | ACT14 Autorizar la liberación de la versión  | ODC (84 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 84.0 % |
| S10 | ACT15 Habilitar o suspender la ventana de in | ODC (96 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 96.0 % |
| S10 | ACT16 Ejecutar el respaldo y la carga en pro | DAS (96 %) | DAS (88 %) | 96.0 % | 88.0 % | -8.0 pp | 84.0 % |
| S10 | ACT20 Ejecutar la reversión | ODC (72 %) | ODC (56 %) | 20.0 % | 40.0 % | +20.0 pp | 36.0 % |

## Estabilidad y acuerdo

- Decisiones pareadas con la misma A en ambas versiones: 61.5 %.
- Acuerdo entre especializados (pares con igual A): base 68.4 %, sin nombres 64.8 %.

## Sesgo hacia la propia unidad (frente al neutral)

En la variante, el agente conoce su foco técnico, pero no el nombre ni el código de su unidad.

| Agente | Base | Sin nombres |
|---|---|---|
| DAS | +0.093 | +0.051 |
| ISC | +0.074 | +0.019 |
| MCO | +0.019 | +0.084 |
| ODC | +0.093 | +0.051 |

## Coincidencia con la A de REFERENCE_RACI (post hoc)

- Base: 45.1 %; sin nombres: 46.4 %.

## Lectura

- Si la proporción de DAS baja de forma clara al quitar los nombres, parte de la concentración en DAS del piloto se explica por el nombre de la unidad y no por el contenido de sus atribuciones.
- Si no cambia (IC que incluye 0 y diferencia pequeña), la concentración se sostiene en el contenido de las fichas.
- La variante no elimina toda pista: el contenido funcional (p. ej., «administrar la base de datos del SCADA») sigue identificando a cada unidad. Mide el efecto del nombre, no el de la función.
