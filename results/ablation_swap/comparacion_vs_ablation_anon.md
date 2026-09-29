# Ablación de nombres: `ablation_swap` frente a `ablation_anon` (fase 1)

Decisiones pareadas: 1075 (mismo run, escenario, actividad y agente) en 50 corridas. Solo cambia el nombre de las unidades (códigos neutros en la variante). IC 95 % por bootstrap pareado sobre corridas (4000 remuestreos). pp = puntos porcentuales.

## Estimando principal

Proporción de decisiones con DAS como A (5 agentes): **29.1 % → 45.1 %**, diferencia **+16.0 pp** [+10.9 pp, +21.1 pp].

## Proporción de decisiones en que cada unidad recibe la A

| Unidad | Base | Sin nombres | Diferencia | IC 95 % | Excluye 0 |
|---|---|---|---|---|---|
| DAS | 29.1 % | 45.1 % | +16.0 pp | [+10.9 pp, +21.1 pp] | sí |
| ISC | 8.7 % | 10.6 % | +2.0 pp | [-0.2 pp, +4.3 pp] | no |
| MCO | 33.4 % | 8.8 % | -24.6 pp | [-29.4 pp, -19.7 pp] | sí |
| ODC | 19.9 % | 22.2 % | +2.3 pp | [+0.6 pp, +4.1 pp] | sí |
| OP | 5.1 % | 4.2 % | -0.9 pp | [-2.9 pp, +1.0 pp] | no |
| DT | 0.4 % | 2.3 % | +2.0 pp | [+0.9 pp, +3.2 pp] | sí |
| TX_REG | 0.2 % | 0.8 % | +0.7 pp | [+0.2 pp, +1.3 pp] | sí |
| DEL | 1.3 % | 1.6 % | +0.3 pp | [-0.3 pp, +0.9 pp] | no |
| DOS | 2.0 % | 4.2 % | +2.2 pp | [+1.0 pp, +3.5 pp] | sí |
| OTHER | 0.0 % | 0.1 % | +0.1 pp | [+0.0 pp, +0.3 pp] | no |

## DAS como A, por agente

| Agentes | Base | Sin nombres | Diferencia | IC 95 % |
|---|---|---|---|---|
| especializados | 29.9 % | 44.5 % | +14.7 pp | [+9.5 pp, +19.9 pp] |
| neutral | 26.0 % | 47.4 % | +21.4 pp | [+13.3 pp, +30.2 pp] |
| DAS | 40.9 % | 52.6 % | +11.6 pp | [+2.3 pp, +21.3 pp] |
| ISC | 25.1 % | 41.4 % | +16.3 pp | [+8.4 pp, +24.4 pp] |
| MCO | 27.9 % | 40.9 % | +13.0 pp | [+5.0 pp, +20.6 pp] |
| ODC | 25.6 % | 43.3 % | +17.7 pp | [+10.8 pp, +24.3 pp] |

## Por escenario y actividad

| Esc. | Actividad | A modal base | A modal sin nombres | DAS base | DAS sin nombres | Δ DAS | Misma A (pareado) |
|---|---|---|---|---|---|---|---|
| S01 | ACT02 Certificar los datos de la instalación | ISC (68 %) | DT (36 %) | 0.0 % | 0.0 % | +0.0 pp | 24.0 % |
| S01 | ACT04 Construir o actualizar el modelo eléct | DAS (88 %) | DAS (100 %) | 88.0 % | 100.0 % | +12.0 pp | 88.0 % |
| S01 | ACT06 Configurar la adquisición, la correspo | MCO (96 %) | DAS (40 %) | 0.0 % | 40.0 % | +40.0 pp | 28.0 % |
| S01 | ACT09 Aprobar las pruebas FAT/SAT y de integ | MCO (52 %) | ISC (96 %) | 0.0 % | 0.0 % | +0.0 pp | 52.0 % |
| S01 | ACT12 Verificar la correspondencia de mímico | MCO (72 %) | MCO (36 %) | 12.0 % | 4.0 % | -8.0 pp | 28.0 % |
| S02 | ACT02 Certificar los datos de la instalación | DEL (56 %) | DEL (68 %) | 0.0 % | 0.0 % | +0.0 pp | 40.0 % |
| S02 | ACT04 Construir o actualizar el modelo eléct | DAS (92 %) | DAS (96 %) | 92.0 % | 96.0 % | +4.0 pp | 96.0 % |
| S02 | ACT05 Revisar la calidad topológica y de nom | DAS (84 %) | DAS (88 %) | 84.0 % | 88.0 % | +4.0 pp | 80.0 % |
| S02 | ACT11 Validar el estimador de estado, el flu | DAS (96 %) | DAS (92 %) | 96.0 % | 92.0 % | -4.0 pp | 92.0 % |
| S03 | ACT06 Configurar la adquisición, la correspo | MCO (68 %) | ISC (60 %) | 0.0 % | 12.0 % | +12.0 pp | 28.0 % |
| S03 | ACT07 Unificar modelo y adquisición en la ba | DAS (56 %) | DAS (96 %) | 56.0 % | 96.0 % | +40.0 pp | 60.0 % |
| S03 | ACT09 Aprobar las pruebas FAT/SAT y de integ | MCO (64 %) | ISC (64 %) | 0.0 % | 0.0 % | +0.0 pp | 48.0 % |
| S03 | ACT13 Aceptar mímicos, alarmas y el uso oper | ODC (56 %) | ODC (80 %) | 0.0 % | 0.0 % | +0.0 pp | 40.0 % |
| S04 | ACT06 Configurar la adquisición, la correspo | MCO (60 %) | DAS (92 %) | 40.0 % | 92.0 % | +52.0 pp | 48.0 % |
| S04 | ACT11 Validar el estimador de estado, el flu | DAS (96 %) | DAS (96 %) | 96.0 % | 96.0 % | +0.0 pp | 92.0 % |
| S04 | ACT17 Mantener el registro técnico de config | ISC (48 %) | DAS (76 %) | 24.0 % | 76.0 % | +52.0 pp | 32.0 % |
| S04 | ACT18 Verificar el sistema después de la act | MCO (48 %) | ODC (44 %) | 8.0 % | 36.0 % | +28.0 pp | 36.0 % |
| S05 | ACT01 Definir el requisito y el alcance del  | DOS (36 %) | DOS (76 %) | 8.0 % | 8.0 % | +0.0 pp | 40.0 % |
| S05 | ACT06 Configurar la adquisición, la correspo | MCO (76 %) | DAS (88 %) | 16.0 % | 88.0 % | +72.0 pp | 24.0 % |
| S05 | ACT09 Aprobar las pruebas FAT/SAT y de integ | MCO (60 %) | ISC (40 %) | 4.0 % | 36.0 % | +32.0 pp | 32.0 % |
| S05 | ACT15 Habilitar o suspender la ventana de in | ODC (100 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 100.0 % |
| S06 | ACT03 Especificar y aceptar la semántica del | ISC (56 %) | ISC (40 %) | 32.0 % | 36.0 % | +4.0 pp | 28.0 % |
| S06 | ACT04 Construir o actualizar el modelo eléct | DAS (88 %) | DAS (92 %) | 88.0 % | 92.0 % | +4.0 pp | 80.0 % |
| S06 | ACT05 Revisar la calidad topológica y de nom | DAS (88 %) | DAS (84 %) | 88.0 % | 84.0 % | -4.0 pp | 80.0 % |
| S06 | ACT12 Verificar la correspondencia de mímico | MCO (48 %) | MCO (68 %) | 24.0 % | 4.0 % | -20.0 pp | 44.0 % |
| S06 | ACT13 Aceptar mímicos, alarmas y el uso oper | ODC (60 %) | ODC (92 %) | 8.0 % | 0.0 % | -8.0 pp | 52.0 % |
| S07 | ACT10 Administrar y actualizar los aplicativ | DAS (92 %) | DAS (100 %) | 92.0 % | 100.0 % | +8.0 pp | 92.0 % |
| S07 | ACT11 Validar el estimador de estado, el flu | DAS (76 %) | DAS (76 %) | 76.0 % | 76.0 % | +0.0 pp | 52.0 % |
| S07 | ACT14 Autorizar la liberación de la versión  | DAS (32 %) | OP (48 %) | 32.0 % | 16.0 % | -16.0 pp | 16.0 % |
| S07 | ACT19 Aprobar los criterios de reversión y s | OP (28 %) | OP (32 %) | 28.0 % | 24.0 % | -4.0 pp | 8.0 % |
| S08 | ACT08 Preparar el paquete de implementación | DAS (52 %) | DAS (100 %) | 52.0 % | 100.0 % | +48.0 pp | 52.0 % |
| S08 | ACT14 Autorizar la liberación de la versión  | MCO (52 %) | DAS (56 %) | 8.0 % | 56.0 % | +48.0 pp | 16.0 % |
| S08 | ACT15 Habilitar o suspender la ventana de in | ODC (100 %) | ODC (96 %) | 0.0 % | 0.0 % | +0.0 pp | 96.0 % |
| S08 | ACT16 Ejecutar el respaldo y la carga en pro | MCO (92 %) | DAS (52 %) | 8.0 % | 52.0 % | +44.0 pp | 40.0 % |
| S09 | ACT15 Habilitar o suspender la ventana de in | ODC (100 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 100.0 % |
| S09 | ACT18 Verificar el sistema después de la act | MCO (80 %) | DAS (80 %) | 20.0 % | 80.0 % | +60.0 pp | 24.0 % |
| S09 | ACT19 Aprobar los criterios de reversión y s | OP (44 %) | DAS (44 %) | 8.0 % | 44.0 % | +36.0 pp | 20.0 % |
| S09 | ACT20 Ejecutar la reversión | MCO (84 %) | DAS (76 %) | 16.0 % | 76.0 % | +60.0 pp | 20.0 % |
| S10 | ACT01 Definir el requisito y el alcance del  | ODC (76 %) | ODC (84 %) | 12.0 % | 12.0 % | +0.0 pp | 64.0 % |
| S10 | ACT14 Autorizar la liberación de la versión  | ODC (84 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 84.0 % |
| S10 | ACT15 Habilitar o suspender la ventana de in | ODC (100 %) | ODC (100 %) | 0.0 % | 0.0 % | +0.0 pp | 100.0 % |
| S10 | ACT16 Ejecutar el respaldo y la carga en pro | MCO (68 %) | DAS (88 %) | 32.0 % | 88.0 % | +56.0 pp | 36.0 % |
| S10 | ACT20 Ejecutar la reversión | ODC (56 %) | ODC (56 %) | 4.0 % | 40.0 % | +36.0 pp | 36.0 % |

## Estabilidad y acuerdo

- Decisiones pareadas con la misma A en ambas versiones: 52.3 %.
- Acuerdo entre especializados (pares con igual A): base 59.5 %, sin nombres 64.8 %.

## Sesgo hacia la propia unidad (frente al neutral)

En la variante, el agente conoce su foco técnico, pero no el nombre ni el código de su unidad.

| Agente | Base | Sin nombres |
|---|---|---|
| DAS | +0.149 | +0.051 |
| ISC | -0.019 | +0.019 |
| MCO | -0.009 | +0.084 |
| ODC | +0.070 | +0.051 |

## Coincidencia con la A de REFERENCE_RACI (post hoc)

- Base: 42.3 %; sin nombres: 46.4 %.

## Lectura

- Si la proporción de DAS baja de forma clara al quitar los nombres, parte de la concentración en DAS del piloto se explica por el nombre de la unidad y no por el contenido de sus atribuciones.
- Si no cambia (IC que incluye 0 y diferencia pequeña), la concentración se sostiene en el contenido de las fichas.
- La variante no elimina toda pista: el contenido funcional (p. ej., «administrar la base de datos del SCADA») sigue identificando a cada unidad. Mide el efecto del nombre, no el de la función.
