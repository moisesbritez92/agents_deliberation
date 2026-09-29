# Preauditoría IA de las 99 citas del piloto

Fecha: 26 de septiembre de 2026. Autor: asistente IA OpenAI, modelo declarado por el entorno: gpt-6-astra.

## Naturaleza y uso de los archivos

Esta es una evaluación propuesta por un único modelo, con una justificación por ítem. Las dos copias CSV contienen exactamente los mismos juicios para facilitar su entrega a dos personas. No son dos codificaciones independientes, ni resultados de auditoría humana, ni una referencia de verdad.

Si se entregan antes de la codificación, el procedimiento pasa a ser revisión humana asistida por IA. Las coincidencias pueden reflejar anclaje en esta propuesta; no deben presentarse como validación humana ciega e independiente del juez. Para conservar esa validación, usar las planillas originales en blanco y reservar este material para después de la entrega inicial. No introducir estas copias como coder1/coder2 originales en el cálculo de kappa.

## Material y alcance

- Fuente de los ítems: results/pilot/audit_sheet_coder1.csv y audit_sheet_coder2.csv, comprobadas como idénticas al generar las copias.
- Se conservan las ocho columnas de contexto, el orden, los identificadores y A/R ocultos.
- Solo se completan support, claim_type_correct y note. No se consultó audit_key.csv ni los veredictos individuales del juez para decidir estas valoraciones.
- La evaluación documental se limita a source_text de cada fila. Las fuentes externas contienen resúmenes curados con PRINCIPLE, CAN_SUPPORT y CANNOT_SUPPORT: no se cotejaron aquí las publicaciones originales ni se certifica la fidelidad de esos resúmenes.
- La valoración no determina quién debe ocupar A o R. Tampoco convierte una afirmación general verdadera en prueba suficiente de toda la actividad.

## Regla aplicada y ambigüedad que deben conocer los auditores

Se siguen GUIA_VALIDACION_HUMANA.md, sección Instrucciones para los codificadores, y las definiciones de prompts/judge.md. Hay dos preguntas distintas:

1. **support:** ¿source_text respalda claim tal como está escrito? SUPPORTS exige respaldo completo; PARTIAL indica un núcleo pertinente con ampliaciones no justificadas; DOES_NOT_SUPPORT indica ausencia de respaldo para la proposición central. activity contextualiza afirmaciones elípticas, sin añadir automáticamente una RACI oculta.
2. **claim_type_correct:** ¿es correcta la etiqueta según el protocolo? Se aplica el criterio estricto de la guía: DOCUMENTADO requiere que la actividad específica esté expresa en una fuente institucional. INFERIDO exige una deducción razonable desde numerales institucionales. BUENA_PRACTICA exige que la fuente externa sostenga el principio alegado, sin crear competencias locales. PROPUESTO identifica una decisión de diseño sin apoyo directo.

**Por ello SUPPORTS + NO es posible.** Por ejemplo, H019 dice algo expresamente cierto sobre administrar la base, pero ese numeral no documenta construir el modelo eléctrico. H098 expresa correctamente la administración de aplicativos, sin documentar preparar paquetes. Un NO no demuestra que la asignación sea incorrecta: indica que su clasificación como respaldo expreso no cumple esta regla.

**Punto a acordar antes de codificar:** la planilla mezcla afirmaciones generales y actividades específicas. Si se pretendiera evaluar DOCUMENTADO solo sobre claim, ignorando activity, varios NO cambiarían. Debe fijarse una sola interpretación para los dos humanos y cualquier juez; no modificarla después de observar concordancias.

En H011 y H046, CTX_DOMINIOS es contexto técnico y no un numeral institucional: la etiqueta INFERIDO no cumple la definición estricta, aunque el contenido pueda ser razonable. La taxonomía no dispone de una categoría específica para contexto técnico. No se propone reemplazarla automáticamente por BUENA_PRACTICA.

Las decisiones PARTIAL/SUPPORTS en aplicaciones de principios generales son discutibles. Las notas explicitan el salto para permitir revisión; no se calculan intervalos, kappa ni conclusiones sobre todas las citas a partir de esta preauditoría.

## Resumen descriptivo de esta propuesta

| Valoración | Ítems | Porcentaje de 99 |
|---|---:|---:|
| SUPPORTS | 39 | 39.4% |
| PARTIAL | 55 | 55.6% |
| DOES_NOT_SUPPORT | 5 | 5.1% |

Tipo correcto: SI en 23 ítems; NO en 76. Estos recuentos describen únicamente esta lectura IA y su criterio estricto.

## Cómo trabajar con cada copia

1. Leer activity, claim y source_text antes de aceptar la propuesta.
2. Revisar especialmente las ampliaciones de alcance señaladas en note y los límites CANNOT_SUPPORT.
3. Si se discrepa, registrar el juicio humano y su motivo en una copia de trabajo identificada como asistida, conservando esta propuesta como referencia.
4. No completar A/R ni reconstruir asignaciones ocultas. No sustituir la lectura documental por conocimiento de cómo trabaja la empresa.
5. Las valoraciones de ambos humanos deben conservarse separadas antes de cualquier reunión de resolución. Documentar que recibieron la misma ayuda IA si fue el caso.

## Justificación completa por ítem

### H001: Definir el requisito y el alcance del cambio

- **Afirmación:** GT/DEN administra la relación comercial y técnica de los contratos de intercambio.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DEN_2_2`.
- **Texto evaluado:** GT/DEN (DEPARTAMENTO DE ESTUDIOS ENERGÉTICOS), numeral 2.2: Administrar los Contratos de compra, venta e intercambio de energía con las Empresas interconectadas.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Administrar contratos está expreso; administrar una relación técnica y comercial amplía el objeto. Tampoco se expresa definir el requisito del cambio.

### H002: Mantener el registro técnico de configuración

- **Afirmación:** Responsabilidad formal de mantener actualizada la documentación y archivos de configuración.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ISC3_2_5`.
- **Texto evaluado:** DTE/ISC3 (SECCIÓN INGENIERÍA DE MANTENIMIENTO DE SISTEMAS DE CONTROL), numeral 2.5: Mantener actualizada la Base de Datos referente a planos, archivos de configuración, arquitectura, etc. de los equipos y sistemas de tecnologías de operación.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** El numeral exige mantener actualizada la base de planos, archivos de configuración y arquitectura; coincide con mantener el registro técnico.

### H003: Aprobar los criterios de reversión y su delegación

- **Afirmación:** Vincula la reversión técnica a la estrategia general del sistema.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_02`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.3. PRINCIPLE: Verificar los respaldos y probar la restauración, integrando la recuperación con la gestión de cambios. CAN_SUPPORT: exigir respaldo verificable y restauración probada antes y después de un cambio. CANNOT_SUPPORT: asignar la ejecución del respaldo o de la restauración a una unidad concreta
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** La fuente vincula restauración y gestión de cambios; no establece una estrategia general del sistema ni aprobación o delegación de criterios.

### H004: Administrar y actualizar los aplicativos EMS

- **Afirmación:** Fundamenta la formalidad del proceso de actualización.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Documentar, probar y aprobar cambios antes del despliegue respalda la formalidad del proceso, sin asignar una unidad.

### H005: Administrar y actualizar los aplicativos EMS

- **Afirmación:** La responsabilidad de administrar los módulos del SCADA/EMS reside en el Departamento GT/DAS.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS_2_2`.
- **Texto evaluado:** GT/DAS (DEPARTAMENTO DE ADMINISTRACIÓN DEL SCADA/EMS), numeral 2.2: Administrar y gestionar los módulos de los aplicativos informáticos del SCADA/EMS.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Administrar y gestionar los módulos informáticos SCADA/EMS aparece expresamente como atribución de GT/DAS.

### H006: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** La separación entre la autoridad de administración de base (GT/DAS) y la ejecución técnica (DTE/ISC2) cumple la segregación de funciones.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Respalda separar modificación y aprobación; no identifica DAS o ISC2 ni equipara esa separación a administración de base frente a ejecución técnica.

### H007: Autorizar la liberación de la versión a producción

- **Afirmación:** GT/OP tiene la jerarquía necesaria para la autorización final de cambios relevantes.
- **Tipo declarado:** `INFERIDO`.
- **Fuente:** `OP_2_3`.
- **Texto evaluado:** GT/OP (DIVISIÓN DE OPERACIÓN), numeral 2.3: Coordinar la operación Eléctrica y Energética del Sistema de Potencia, propiciando su mejor desempeño.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Coordinar la operación proporciona un vínculo funcional, pero no demuestra jerarquía suficiente ni potestad de autorización final de versiones.

### H008: Aceptar mímicos, alarmas y el uso operativo

- **Afirmación:** La función operativa requiere validación del usuario para aceptar la puesta en servicio.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_13`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.13: Solicitar, proponer y/o recomendar la realización de estudios de operación para elaborar o actualizar los Reglamentos, Normas e Instrucciones de operación en función a constataciones o necesidades detectadas en la operación de tiempo real.
- **Propuesta:** `support = DOES_NOT_SUPPORT`; `claim_type_correct = NO`.
- **Justificación:** Solicitar estudios para reglamentos operativos no establece validación del usuario ni aceptación de puesta en servicio.

### H009: Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros)

- **Afirmación:** Ejecución técnica de la construcción del modelo en la base de datos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_1`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.1: Diseñar e implementar Base de Datos para almacenar y gestionar datos del SCADA.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Diseñar bases de datos respalda parte del trabajo técnico; construir el modelo eléctrico requiere una inferencia sobre el alcance de esa base.

### H010: Ejecutar la reversión

- **Afirmación:** ODC es la autoridad para revertir operaciones en el tiempo real.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_6`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.6: Autorizar y/o suspender en tiempo real, la ejecución de los trabajos de mantenimiento programados en función a la constatación o no der restricciones operativas.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Autorizar o suspender mantenimiento no equivale a autorizar una reversión de versión; existe relación operativa, pero no mandato expreso de reversión.

### H011: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** Separación técnica entre la configuración de comunicaciones y la base de datos.
- **Tipo declarado:** `INFERIDO`.
- **Fuente:** `CTX_DOMINIOS`.
- **Texto evaluado:** Contexto técnico del dominio SCADA/EMS. PRINCIPLE: Bajo la denominación general de 'base SCADA/EMS' coexisten seis dominios técnicos: (1) modelo eléctrico: topología, conectividad, parámetros de líneas y transformadores, equivalentes y estados operativos; (2) telemetría y telecontrol: puntos analógicos y digitales, calidad, escalas, comandos, alarmas, tiempos y correspondencia con equipos; (3) comunicaciones: RTU, IED, gateways, canales, direccionamiento, protocolos, ICCP/TASE.2 y sincronización; (4) aplicaciones EMS: estimador de estado, flujo de potencia, contingencias, control automático de generación y demás módulos; (5) plataforma técnica: servidores, almacenamiento, sistemas operativos, respaldo, virtualización, ambientes y herramientas del fabricante; (6) gobierno y seguridad: acceso, trazabilidad, configuración base, evidencias, aceptación, reversión y auditoría. CAN_SUPPORT: delimitar el objeto afectado por cada decisión; identificar competencias técnicas requeridas por dominio. CANNOT_SUPPORT: asignar dominios a unidades concretas
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** El contexto distingue comunicaciones, telemetría y modelo, respaldando la distinción técnica. INFERIDO se define en el protocolo como deducción institucional; esta fuente es contexto técnico.

### H012: Ejecutar el respaldo y la carga en producción

- **Afirmación:** DAS tiene la atribución formal sobre la administración del SCADA/EMS.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS_2_1`.
- **Texto evaluado:** GT/DAS (DEPARTAMENTO DE ADMINISTRACIÓN DEL SCADA/EMS), numeral 2.1: Administrar y gestionar la Base de Datos del Sistema Interconectado Nacional (SIN) obtenidos mediante el Sistema SCADA.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** La atribución se limita a la base de datos del SIN obtenida mediante SCADA; no abarca expresamente todo SCADA/EMS ni respaldo y carga.

### H013: Definir el requisito y el alcance del cambio

- **Afirmación:** Prioriza la disponibilidad operativa mediante la actualización del modelo.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_OT_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3 (2023), doi 10.6028/NIST.SP.800-82r3, visión general. PRINCIPLE: La protección de la tecnología operacional (OT) debe considerar sus requisitos particulares de disponibilidad, seguridad física, desempeño y confiabilidad. CAN_SUPPORT: priorizar la disponibilidad y la seguridad operacional al planificar intervenciones. CANNOT_SUPPORT: asignar responsabilidades a unidades concretas
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Disponibilidad y seguridad son prioridades expresas; la actualización del modelo como medio concreto no está establecida en el fragmento.

### H014: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** Necesidad de configuración y pruebas previas.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** La configuración base y las pruebas antes del despliegue están recogidas explícitamente como buena práctica.

### H015: Definir el requisito y el alcance del cambio

- **Afirmación:** La ODC representa a la ANDE en la interlocución técnica con entidades externas para la operación.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_15`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.15: Representar a la ANDE ante la Comisión Mixta de Operación y Coordinación de los Sistemas Interconectados de la ANDE-ITAIPÚ-ELETROBRAS (CMO), a través de la participación en Grupos de Estudio de dicha Comisión, así como ante otros organismos.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** La representación ante la CMO y otros organismos respalda la interlocución operativa, pero no documenta definir requisitos y alcance de cambios.

### H016: Mantener el registro técnico de configuración

- **Afirmación:** La gestión de cambios implica el registro y documentación de las modificaciones.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS_2_4`.
- **Texto evaluado:** GT/DAS (DEPARTAMENTO DE ADMINISTRACIÓN DEL SCADA/EMS), numeral 2.4: Gestionar los cambios para los nuevos requisitos del Sistema.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Gestionar cambios está expreso; registrar y documentar modificaciones es una concreción razonable que el numeral no enuncia.

### H017: Validar el estimador de estado, el flujo de potencia y demás aplicaciones

- **Afirmación:** El Departamento de Operación del Sistema es consultado por su rol en el soporte a la operación.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DOS_2_7`.
- **Texto evaluado:** GT/DOS (DEPARTAMENTO DE OPERACIÓN DEL SISTEMA), numeral 2.7: Proporcionar el soporte técnico a la Oficina de Despacho de Carga, para la utilización eficiente y eficaz de los recursos tecnológicos e informáticos utilizados en la operación en tiempo real del SIN.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** El soporte técnico a ODC está expreso; ser consultado en la validación de aplicaciones es una asignación adicional no enunciada.

### H018: Habilitar o suspender la ventana de intervención en tiempo real

- **Afirmación:** La urgencia operativa requiere la intervención de la instancia que garantiza la disponibilidad en tiempo real.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `ENISA_CHG_01`.
- **Texto evaluado:** ENISA, Technical implementation guidance, v1.0, junio 2025, apdo. 6.4.1. PRINCIPLE: Propone flujos de gestión de cambios diferenciados según criticidad y urgencia, y un comité de cambios cuando resulte apropiado ('where appropriate'). CAN_SUPPORT: diferenciar cambios ordinarios, urgentes y de emergencia; prever un órgano colegiado de cambios si la organización lo considera apropiado. CANNOT_SUPPORT: exigir un comité para todo cambio; designar a una unidad de ANDE como aprobadora; obligar a ANDE
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** La urgencia justifica diferenciar flujos; no se prescribe intervenir mediante la instancia que garantiza disponibilidad en tiempo real.

### H019: Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros)

- **Afirmación:** Asigna la responsabilidad sobre la base de datos SCADA al Departamento de Administración del SCADA/EMS.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS_2_1`.
- **Texto evaluado:** GT/DAS (DEPARTAMENTO DE ADMINISTRACIÓN DEL SCADA/EMS), numeral 2.1: Administrar y gestionar la Base de Datos del Sistema Interconectado Nacional (SIN) obtenidos mediante el Sistema SCADA.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** La responsabilidad sobre la base está expresamente indicada, pero identificarla con construir topología y parámetros del modelo es inferencial.

### H020: Ejecutar el respaldo y la carga en producción

- **Afirmación:** DTE/MCO actúa como soporte técnico especializado durante la carga del sistema en producción.
- **Tipo declarado:** `INFERIDO`.
- **Fuente:** `MCO_2_8`.
- **Texto evaluado:** DTE/MCO (DEPARTAMENTO DE MANTENIMIENTO DE SISTEMAS DE CONTROL), numeral 2.8: Administrar y mantener equipos y redes de los sistemas SCADA, EMS, DMS y de automatización de transmisión y distribución, como como las redes y dispositivos de tecnologías de operación asociados en los distintos Centros de Control Regional y Central.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Administrar y mantener equipos y redes SCADA/EMS permite inferir apoyo técnico durante una carga; no afirma una competencia exclusiva ni documentada.

### H021: Administrar y actualizar los aplicativos EMS

- **Afirmación:** La responsabilidad de administrar los aplicativos EMS reside en el Departamento de Administración del SCADA/EMS.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS_2_2`.
- **Texto evaluado:** GT/DAS (DEPARTAMENTO DE ADMINISTRACIÓN DEL SCADA/EMS), numeral 2.2: Administrar y gestionar los módulos de los aplicativos informáticos del SCADA/EMS.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** La administración de módulos de aplicativos SCADA/EMS coincide directamente con la afirmación y la actividad.

### H022: Validar el estimador de estado, el flujo de potencia y demás aplicaciones

- **Afirmación:** Define la responsabilidad técnica sobre el estimador de estado.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS2_2_1`.
- **Texto evaluado:** GT/DAS2 (SECCIÓN APLICATIVOS DEL SCADA/EMS), numeral 2.1: Administrar y gestionar el uso de aplicativos disponibles del SCADA/EMS, previsión de carga de barras, procesamiento de topología de red, estimador de estado, análisis de contingencias, flujo de potencia óptimo, etc.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** El estimador está nombrado y su administración está asignada; validar técnicamente sus resultados no aparece como actividad expresa.

### H023: Certificar los datos de la instalación (configuración física y parámetros)

- **Afirmación:** Responsabilidad del dueño del activo sobre la veracidad de los datos físicos.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `PJM_01`.
- **Texto evaluado:** PJM Manual 03A, rev. 27 (2026), sec. 3.1, p. 34. PRINCIPLE: El representante de cada propietario de transmisión ante el subcomité de operación responde por la información del modelo de su sistema. CAN_SUPPORT: responsabilidad de quien origina el dato sobre su exactitud. CANNOT_SUPPORT: asignar unidades de ANDE; transferir automáticamente el arreglo de un operador independiente
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** El fragmento atribuye responsabilidad por la información del modelo a quien origina el dato; respalda el principio sin transferir unidades a ANDE.

### H024: Ejecutar la reversión

- **Afirmación:** La reversión requiere la actualización/restauración de la Base de Datos a cargo del DAS.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_2`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.2: Mantener y actualizar las Bases de Datos existentes para asegurar el correcto funcionamiento y ajustes para nuevos requisitos del sistema.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Mantener y actualizar bases ofrece un vínculo técnico; restaurar o revertir una versión no se establece expresamente.

### H025: Aprobar los criterios de reversión y su delegación

- **Afirmación:** Vincula la reversión técnica a la estrategia operativa.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_02`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.3. PRINCIPLE: Verificar los respaldos y probar la restauración, integrando la recuperación con la gestión de cambios. CAN_SUPPORT: exigir respaldo verificable y restauración probada antes y después de un cambio. CANNOT_SUPPORT: asignar la ejecución del respaldo o de la restauración a una unidad concreta
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Se expresa integrar recuperación y gestión de cambios, no una estrategia operativa ni criterios de autoridad para reversión.

### H026: Certificar los datos de la instalación (configuración física y parámetros)

- **Afirmación:** La División de Estudios Eléctricos define los parámetros operativos técnicos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DEL_2_5`.
- **Texto evaluado:** GT/DEL (DEPARTAMENTO DE ESTUDIOS ELÉCTRICOS), numeral 2.5: Definir los criterios operativos de utilización de líneas y equipos del Sistema de Generación, Transmisión y Transformación.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** La fuente dice criterios operativos de utilización, no parámetros físicos certificados; además identifica un Departamento, no una División.

### H027: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** Asigna a MCO la administración de redes y dispositivos de tecnologías de operación asociados.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `MCO_2_8`.
- **Texto evaluado:** DTE/MCO (DEPARTAMENTO DE MANTENIMIENTO DE SISTEMAS DE CONTROL), numeral 2.8: Administrar y mantener equipos y redes de los sistemas SCADA, EMS, DMS y de automatización de transmisión y distribución, como como las redes y dispositivos de tecnologías de operación asociados en los distintos Centros de Control Regional y Central.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** La administración de redes y dispositivos OT es textual; configurar la correspondencia señal-modelo es una actividad más específica no explicitada.

### H028: Certificar los datos de la instalación (configuración física y parámetros)

- **Afirmación:** Responsabilidad del dueño del activo sobre sus datos.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `PJM_01`.
- **Texto evaluado:** PJM Manual 03A, rev. 27 (2026), sec. 3.1, p. 34. PRINCIPLE: El representante de cada propietario de transmisión ante el subcomité de operación responde por la información del modelo de su sistema. CAN_SUPPORT: responsabilidad de quien origina el dato sobre su exactitud. CANNOT_SUPPORT: asignar unidades de ANDE; transferir automáticamente el arreglo de un operador independiente
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** La responsabilidad del propietario por la información de su sistema está recogida como práctica de PJM, sin asignar una unidad local.

### H029: Aceptar mímicos, alarmas y el uso operativo

- **Afirmación:** El usuario final que acepta la operabilidad es el Despacho de Carga.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_1`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.1: Supervisar y controlar en tiempo real, la operación eléctrica y energética del sistema de potencia mediante el monitoreo de los parámetros eléctricos típicos, adoptando las medidas necesarias cuando los mismos se aparten de los valores aceptables o preestablecidos en las Instrucciones de Operación del Sistema (IOS) y en las Instrucciones de Operación de las Interconexiones (IOI). 2.1.1. Niveles de tensión en barras de todos los locales del SIN. 2.1.2. Niveles de cargas y corrientes en las líneas de transmisión, transformadores de potencia, compensadores estáticos, bancos de capacitores, reactores y generadores. 2.1.3. Frecuencia de la red a cargo de Itaipú y Yacyretá.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Supervisar la operación permite vincular ODC al uso del sistema; la aceptación formal de operabilidad no figura en el numeral.

### H030: Certificar los datos de la instalación (configuración física y parámetros)

- **Afirmación:** GT/DEL es responsable de los estudios eléctricos y parámetros del sistema.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DEL_2_1`.
- **Texto evaluado:** GT/DEL (DEPARTAMENTO DE ESTUDIOS ELÉCTRICOS), numeral 2.1: Elaborar estudios sobre la operación eléctrica del Sistema de Generación, Transmisión y Transformación de Energía Eléctrica, para la atención de cargas y optimización de confiabilidad y desempeño económico, así como las interconexiones y suministros especiales.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Elaborar estudios eléctricos está expreso; ser responsable de los parámetros y certificarlos añade un alcance no documentado.

### H031: Administrar y actualizar los aplicativos EMS

- **Afirmación:** La Sección Aplicativos del SCADA/EMS es responsable de la ejecución de la actualización.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS2_2_2`.
- **Texto evaluado:** GT/DAS2 (SECCIÓN APLICATIVOS DEL SCADA/EMS), numeral 2.2: Actualizar los aplicativos existentes del SCADA/EMS para asegurar el correcto funcionamiento ante nuevos requisitos del Sistema.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Actualizar aplicativos existentes ante nuevos requisitos coincide expresamente con la actividad y con la unidad citada.

### H032: Aceptar mímicos, alarmas y el uso operativo

- **Afirmación:** El operador (GT/ODC) debe validar y aceptar los cambios que afectan su capacidad de supervisión.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `IEC62443_2_1_01`.
- **Texto evaluado:** IEC 62443-2-1:2024 ed. 2.0, alcance público. PRINCIPLE: Especifica requisitos del programa de seguridad del propietario del activo para sistemas en operación; el rol de propietario del activo incluye al operador del sistema. Contempla medidas compensatorias ante limitaciones de sistemas heredados. CAN_SUPPORT: existencia de políticas y procedimientos de seguridad para sistemas en operación; medidas compensatorias cuando el sistema heredado no permite ciertos controles. CANNOT_SUPPORT: identificar qué unidad interna ejerce el rol de propietario del activo; demostrar requisitos detallados de aprobación de cambios
- **Propuesta:** `support = DOES_NOT_SUPPORT`; `claim_type_correct = NO`.
- **Justificación:** El alcance citado no prueba requisitos detallados de aprobación ni identifica ODC como propietario del activo; no sostiene el deber específico de aceptar cambios.

### H033: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** Segregación técnica y formal en la gestión de cambios.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** El fragmento admite segregación entre modificación y aprobación como principio general, sin nombrar unidades ni exigir una RACI particular.

### H034: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** Responsabilidad de la Sección Aplicativos sobre la lógica y correspondencia señal-modelo.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS2_2_1`.
- **Texto evaluado:** GT/DAS2 (SECCIÓN APLICATIVOS DEL SCADA/EMS), numeral 2.1: Administrar y gestionar el uso de aplicativos disponibles del SCADA/EMS, previsión de carga de barras, procesamiento de topología de red, estimador de estado, análisis de contingencias, flujo de potencia óptimo, etc.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Gestionar aplicaciones y procesamiento topológico es pertinente; la responsabilidad sobre lógica y correspondencia señal-modelo no está enunciada.

### H035: Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros)

- **Afirmación:** Separación entre modeladores y especialistas.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `EPRI_NMM_02`.
- **Texto evaluado:** EPRI 3002003053, caso A1, pp. 4-5 a 4-6. PRINCIPLE: En el caso de uso A1, modeladores EMS mantienen conectividad y esquemas, con aportes y revisión de especialistas de planificación y protecciones. El informe aclara que el reparto puede variar entre empresas y que varios grupos requieren controles de acceso y coordinación. CAN_SUPPORT: separación entre aportantes especializados y modeladores; controles de acceso y coordinación entre grupos. CANNOT_SUPPORT: constituir un organigrama obligatorio; identificar qué unidad de ANDE cumple el rol de modelador
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** El caso A1 distingue modeladores de aportantes y revisores especializados; respalda esa separación como práctica contextual, no organigrama obligatorio.

### H036: Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros)

- **Afirmación:** Asigna la ejecución de la actualización a la sección de Base de Datos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_2`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.2: Mantener y actualizar las Bases de Datos existentes para asegurar el correcto funcionamiento y ajustes para nuevos requisitos del sistema.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** Actualizar bases de datos está expreso; aplicarlo a la construcción o actualización del modelo eléctrico exige identificar objetos no explicitados.

### H037: Habilitar o suspender la ventana de intervención en tiempo real

- **Afirmación:** Justifica el rol de ODC en la autorización de ventanas críticas para la operación.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_OT_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3 (2023), doi 10.6028/NIST.SP.800-82r3, visión general. PRINCIPLE: La protección de la tecnología operacional (OT) debe considerar sus requisitos particulares de disponibilidad, seguridad física, desempeño y confiabilidad. CAN_SUPPORT: priorizar la disponibilidad y la seguridad operacional al planificar intervenciones. CANNOT_SUPPORT: asignar responsabilidades a unidades concretas
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** La seguridad de las intervenciones tiene respaldo; que ODC autorice ventanas es una asignación institucional que la fuente externa no establece.

### H038: Verificar el sistema después de la actualización y cerrar el cambio

- **Afirmación:** La responsabilidad de validar que el sistema operativamente correcto recae en el despacho.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_1`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.1: Supervisar y controlar en tiempo real, la operación eléctrica y energética del sistema de potencia mediante el monitoreo de los parámetros eléctricos típicos, adoptando las medidas necesarias cuando los mismos se aparten de los valores aceptables o preestablecidos en las Instrucciones de Operación del Sistema (IOS) y en las Instrucciones de Operación de las Interconexiones (IOI). 2.1.1. Niveles de tensión en barras de todos los locales del SIN. 2.1.2. Niveles de cargas y corrientes en las líneas de transmisión, transformadores de potencia, compensadores estáticos, bancos de capacitores, reactores y generadores. 2.1.3. Frecuencia de la red a cargo de Itaipú y Yacyretá.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** El monitoreo operativo respalda vigilancia del funcionamiento; no establece una validación formal posterior a actualización ni cierre del cambio.

### H039: Habilitar o suspender la ventana de intervención en tiempo real

- **Afirmación:** La autoridad para suspender intervenciones en tiempo real reside expresamente en la ODC.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_6`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.6: Autorizar y/o suspender en tiempo real, la ejecución de los trabajos de mantenimiento programados en función a la constatación o no der restricciones operativas.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Autorizar o suspender trabajos en tiempo real está expresamente atribuido a ODC, dentro del alcance de mantenimiento programado y restricciones operativas.

### H040: Aprobar los criterios de reversión y su delegación

- **Afirmación:** Necesidad de definir criterios de reversión antes de la liberación.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `ENISA_CHG_02`.
- **Texto evaluado:** ENISA, Technical implementation guidance, v1.0, junio 2025, apdos. 6.4.2-6.4.3. PRINCIPLE: Contempla aprobación, reversión y registro de evidencia de los cambios, incluidos los cambios excepcionales o de emergencia, que se documentan y revisan con posterioridad. CAN_SUPPORT: prever reversión y su evidencia; revisión posterior de cambios de emergencia. CANNOT_SUPPORT: asignar la reversión o su autorización a una unidad concreta; obligar a ANDE
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Se prevé reversión y evidencia, pero el fragmento no especifica criterios de reversión definidos antes de liberar; esa precisión debe justificarse aparte.

### H041: Definir el requisito y el alcance del cambio

- **Afirmación:** La ODC identifica la necesidad técnica en tiempo real.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_14`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.14: Solicitar, proponer y/o recomendar al Departamento de Operación del Sistema a través de la Sección Procesamiento de Datos de Operación el desarrollo de herramientas o aplicativos (programas o software) para la utilización eficiente y eficaz de los recursos tecnológicos e informáticos utilizados en la operación en tiempo real del SIN.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Solicitar herramientas para operación respalda identificar necesidades en general; definir el requisito técnico del cambio no está expresamente asignado.

### H042: Revisar la calidad topológica y de nomenclatura del modelo construido

- **Afirmación:** Verificación técnica necesaria previa a la producción.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `ERCOT_02`.
- **Texto evaluado:** Moseley et al., ERCOT NMMS, 2014, p. 15. PRINCIPLE: Cada solicitud de cambio atraviesa cinco niveles de validación: rangos y datos asociados; coherencia manual entre metadatos, cambio y documentación; estudio de impacto sobre el flujo de potencia del caso base; prueba conjunta de los cambios de un intervalo de energización; carga del modelo completo en todas las aplicaciones. El modelo temporal permite construir versiones con cambios futuros según su fecha de vigencia. CAN_SUPPORT: validación escalonada antes de producción; versiones con fecha de vigencia. CANNOT_SUPPORT: asignar niveles de validación a unidades de ANDE
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** La validación escalonada, incluida coherencia e impacto, respalda revisar técnicamente el modelo antes de producción.

### H043: Verificar el sistema después de la actualización y cerrar el cambio

- **Afirmación:** Verificación final del sistema en operación real.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_1`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.1: Supervisar y controlar en tiempo real, la operación eléctrica y energética del sistema de potencia mediante el monitoreo de los parámetros eléctricos típicos, adoptando las medidas necesarias cuando los mismos se aparten de los valores aceptables o preestablecidos en las Instrucciones de Operación del Sistema (IOS) y en las Instrucciones de Operación de las Interconexiones (IOI). 2.1.1. Niveles de tensión en barras de todos los locales del SIN. 2.1.2. Niveles de cargas y corrientes en las líneas de transmisión, transformadores de potencia, compensadores estáticos, bancos de capacitores, reactores y generadores. 2.1.3. Frecuencia de la red a cargo de Itaipú y Yacyretá.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Supervisar en tiempo real es pertinente, pero una verificación final posterior a actualización no aparece en el numeral.

### H044: Revisar la calidad topológica y de nomenclatura del modelo construido

- **Afirmación:** GT/DOS tiene el rol de asegurar la calidad de los recursos para el despacho.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DOS_2_7`.
- **Texto evaluado:** GT/DOS (DEPARTAMENTO DE OPERACIÓN DEL SISTEMA), numeral 2.7: Proporcionar el soporte técnico a la Oficina de Despacho de Carga, para la utilización eficiente y eficaz de los recursos tecnológicos e informáticos utilizados en la operación en tiempo real del SIN.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Proporcionar soporte para uso eficiente no equivale a asegurar calidad topológica o de nomenclatura; la atribución específica requiere inferencia.

### H045: Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación)

- **Afirmación:** GT/DAS gestiona los cambios para los nuevos requisitos del modelo.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS_2_4`.
- **Texto evaluado:** GT/DAS (DEPARTAMENTO DE ADMINISTRACIÓN DEL SCADA/EMS), numeral 2.4: Gestionar los cambios para los nuevos requisitos del Sistema.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** La gestión de cambios para nuevos requisitos está expresa; especificar y aceptar semántica del modelo no lo está.

### H046: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** La configuración requiere el ajuste técnico de múltiples dominios del EMS.
- **Tipo declarado:** `INFERIDO`.
- **Fuente:** `CTX_DOMINIOS`.
- **Texto evaluado:** Contexto técnico del dominio SCADA/EMS. PRINCIPLE: Bajo la denominación general de 'base SCADA/EMS' coexisten seis dominios técnicos: (1) modelo eléctrico: topología, conectividad, parámetros de líneas y transformadores, equivalentes y estados operativos; (2) telemetría y telecontrol: puntos analógicos y digitales, calidad, escalas, comandos, alarmas, tiempos y correspondencia con equipos; (3) comunicaciones: RTU, IED, gateways, canales, direccionamiento, protocolos, ICCP/TASE.2 y sincronización; (4) aplicaciones EMS: estimador de estado, flujo de potencia, contingencias, control automático de generación y demás módulos; (5) plataforma técnica: servidores, almacenamiento, sistemas operativos, respaldo, virtualización, ambientes y herramientas del fabricante; (6) gobierno y seguridad: acceso, trazabilidad, configuración base, evidencias, aceptación, reversión y auditoría. CAN_SUPPORT: delimitar el objeto afectado por cada decisión; identificar competencias técnicas requeridas por dominio. CANNOT_SUPPORT: asignar dominios a unidades concretas
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** El contexto enumera dominios y competencias; no dice que esta configuración requiera ajustar todos o varios. Además, INFERIDO exige base institucional en el protocolo.

### H047: Validar el estimador de estado, el flujo de potencia y demás aplicaciones

- **Afirmación:** Criterios técnicos para validar aplicativos EMS.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `PJM_04`.
- **Texto evaluado:** PJM Manual 03A, rev. 27, sec. 5.4, p. 65. PRINCIPLE: Antes de pasar un modelo a producción se aplica una prueba de estabilización de hasta cuatro semanas con telemetría real; durante los dos días previos se aplican criterios del estimador de estado (convergencia, soluciones consecutivas no convergentes, iteraciones, datos erróneos). Ante condiciones no previstas se analiza la situación y se documenta la decisión de continuar. CAN_SUPPORT: criterios objetivos de pase a producción; documentar la decisión de continuar ante desviaciones. CANNOT_SUPPORT: copiar umbrales sin calibración local; asignar unidades de ANDE
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Se describen pruebas y criterios del estimador de estado antes de producción; respalda criterios de validación sin importar umbrales automáticamente.

### H048: Mantener el registro técnico de configuración

- **Afirmación:** Recomienda la centralización del registro de cambios.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Centralizar seguimiento y documentación de cambios aparece expresamente en el fragmento externo.

### H049: Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros)

- **Afirmación:** Separación de roles entre quienes mantienen el modelo y quienes proveen los datos.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `EPRI_NMM_02`.
- **Texto evaluado:** EPRI 3002003053, caso A1, pp. 4-5 a 4-6. PRINCIPLE: En el caso de uso A1, modeladores EMS mantienen conectividad y esquemas, con aportes y revisión de especialistas de planificación y protecciones. El informe aclara que el reparto puede variar entre empresas y que varios grupos requieren controles de acceso y coordinación. CAN_SUPPORT: separación entre aportantes especializados y modeladores; controles de acceso y coordinación entre grupos. CANNOT_SUPPORT: constituir un organigrama obligatorio; identificar qué unidad de ANDE cumple el rol de modelador
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Modeladores que mantienen conectividad y especialistas que aportan datos y revisan respaldan la separación general descrita.

### H050: Habilitar o suspender la ventana de intervención en tiempo real

- **Afirmación:** La gestión de ventanas de tiempo es fundamental para la seguridad operacional.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** La fuente respalda gestionar cambios antes del despliegue, pero no menciona ventanas temporales ni su carácter fundamental para seguridad.

### H051: Definir el requisito y el alcance del cambio

- **Afirmación:** ODC es responsable de la coordinación de la operación basada en contratos externos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_2`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.2: Coordinar y controlar, de acuerdo a criterios técnicos y económicos, la operación electro energética del sistema de potencia desde el punto de vista de la generación eléctrica, considerando los recursos propios (Central Acaray) y los contratos de intercambio con entidades externas (Itaipú y Yacyretá).
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** Coordinar la operación considerando contratos externos es textual; no documenta por sí mismo definir el requisito y alcance de un cambio.

### H052: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** La Sección de Implementación ejecuta el montaje y puesta en servicio de equipos y sistemas SCADA.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ISC2_2_1`.
- **Texto evaluado:** DTE/ISC2 (SECCIÓN IMPLEMENTACIÓN DE SISTEMAS DE CONTROL), numeral 2.1: Realizar o supervisar trabajos relacionados al montaje, instalación, ampliación y puesta en servicio de los equipos y sistemas de supervisión, control y adquisición de datos (SCADA), de automatización de subestaciones (SAS) y de comunicación industrial y ciberseguridad correspondientes a las tecnologías de operación.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** Montaje y puesta en servicio SCADA están expresamente incluidos; la configuración señal-modelo y comunicaciones no queda enteramente documentada por ello.

### H053: Aceptar mímicos, alarmas y el uso operativo

- **Afirmación:** Validación operativa requerida antes de la entrada en servicio.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Probar y aprobar antes del despliegue respalda validación previa en el contexto OT; no prueba aceptación por un usuario o unidad particular.

### H054: Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación)

- **Afirmación:** Ejecución de la configuración del modelo de acuerdo a los criterios definidos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS_2_1`.
- **Texto evaluado:** GT/DAS (DEPARTAMENTO DE ADMINISTRACIÓN DEL SCADA/EMS), numeral 2.1: Administrar y gestionar la Base de Datos del Sistema Interconectado Nacional (SIN) obtenidos mediante el Sistema SCADA.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Administrar la base proporciona un vínculo general; ejecutar configuración conforme a criterios semánticos no aparece en el numeral.

### H055: Verificar el sistema después de la actualización y cerrar el cambio

- **Afirmación:** El operador en tiempo real verifica la calidad de señales y el desempeño del sistema.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_1`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.1: Supervisar y controlar en tiempo real, la operación eléctrica y energética del sistema de potencia mediante el monitoreo de los parámetros eléctricos típicos, adoptando las medidas necesarias cuando los mismos se aparten de los valores aceptables o preestablecidos en las Instrucciones de Operación del Sistema (IOS) y en las Instrucciones de Operación de las Interconexiones (IOI). 2.1.1. Niveles de tensión en barras de todos los locales del SIN. 2.1.2. Niveles de cargas y corrientes en las líneas de transmisión, transformadores de potencia, compensadores estáticos, bancos de capacitores, reactores y generadores. 2.1.3. Frecuencia de la red a cargo de Itaipú y Yacyretá.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Monitorear parámetros eléctricos no equivale expresamente a verificar calidad de señales o desempeño informático tras actualizar.

### H056: Ejecutar la reversión

- **Afirmación:** ODC es responsable de la vuelta a la normalidad operativa.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_7`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.7: Recomponer el sistema eléctrico posterior a la ocurrencia de perturbaciones originadas en las centrales de generación o en líneas de interconexión con las mismas.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Recomponer el sistema tras ciertas perturbaciones está expreso; no equivale a revertir una base de datos o una versión de software.

### H057: Validar el estimador de estado, el flujo de potencia y demás aplicaciones

- **Afirmación:** Recomienda la validación funcional ante cambios.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `PJM_03`.
- **Texto evaluado:** PJM Manual 03A, rev. 27, sec. 3.2, p. 44; sec. 4.1, p. 52. PRINCIPLE: Los propietarios revisan informes de diferencias preliminares y finales y validan que el modelo representa con exactitud sus sistemas. CAN_SUPPORT: revisión de diferencias respecto de la versión base; validación de la representación por quien origina el dato. CANNOT_SUPPORT: asignar unidades de ANDE
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Se valida la exactitud de la representación y diferencias del modelo; pruebas funcionales de aplicativos EMS exceden ese alcance.

### H058: Aceptar mímicos, alarmas y el uso operativo

- **Afirmación:** ODC define necesidad operativa.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_13`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.13: Solicitar, proponer y/o recomendar la realización de estudios de operación para elaborar o actualizar los Reglamentos, Normas e Instrucciones de operación en función a constataciones o necesidades detectadas en la operación de tiempo real.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Proponer estudios ante necesidades operativas permite inferir identificación de necesidades; no documenta su definición ni aceptación de mímicos.

### H059: Revisar la calidad topológica y de nomenclatura del modelo construido

- **Afirmación:** La Sección Aplicativos es la que gestiona la topología de red.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS2_2_1`.
- **Texto evaluado:** GT/DAS2 (SECCIÓN APLICATIVOS DEL SCADA/EMS), numeral 2.1: Administrar y gestionar el uso de aplicativos disponibles del SCADA/EMS, previsión de carga de barras, procesamiento de topología de red, estimador de estado, análisis de contingencias, flujo de potencia óptimo, etc.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** Se administra el aplicativo de procesamiento topológico; revisar calidad y nomenclatura del modelo no es una actividad expresamente enunciada.

### H060: Aprobar las pruebas FAT/SAT y de integración

- **Afirmación:** La responsabilidad de las pruebas está definida expresamente para la sección de implementación.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ISC2_2_3`.
- **Texto evaluado:** DTE/ISC2 (SECCIÓN IMPLEMENTACIÓN DE SISTEMAS DE CONTROL), numeral 2.3: Efectuar, analizar y aprobar pruebas de aceptación de fábrica (FAT) y de aceptación del sitio (SAT) de los equipos y sistemas de tecnologías de operación adquiridos.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Efectuar, analizar y aprobar FAT/SAT está expresamente asignado a ISC2; el respaldo se refiere a esas pruebas, no a toda integración posible.

### H061: Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros)

- **Afirmación:** La Sección GT/DAS1 es responsable de la actualización física de la BDD.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_2`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.2: Mantener y actualizar las Bases de Datos existentes para asegurar el correcto funcionamiento y ajustes para nuevos requisitos del sistema.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Mantener y actualizar bases está expreso; el carácter físico y la construcción del modelo eléctrico no se especifican.

### H062: Ejecutar el respaldo y la carga en producción

- **Afirmación:** La ejecución de la carga debe estar alineada con procedimientos de respaldo técnicos.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_02`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.3. PRINCIPLE: Verificar los respaldos y probar la restauración, integrando la recuperación con la gestión de cambios. CAN_SUPPORT: exigir respaldo verificable y restauración probada antes y después de un cambio. CANNOT_SUPPORT: asignar la ejecución del respaldo o de la restauración a una unidad concreta
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Verificar respaldos y probar restauración en gestión de cambios respalda alinear la carga con procedimientos de respaldo.

### H063: Validar el estimador de estado, el flujo de potencia y demás aplicaciones

- **Afirmación:** La responsabilidad técnica de los aplicativos EMS (incluyendo el estimador de estado) es de DAS2.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS2_2_1`.
- **Texto evaluado:** GT/DAS2 (SECCIÓN APLICATIVOS DEL SCADA/EMS), numeral 2.1: Administrar y gestionar el uso de aplicativos disponibles del SCADA/EMS, previsión de carga de barras, procesamiento de topología de red, estimador de estado, análisis de contingencias, flujo de potencia óptimo, etc.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** La administración de aplicativos, incluido el estimador, es expresa; la validación de resultados requiere una inferencia adicional.

### H064: Revisar la calidad topológica y de nomenclatura del modelo construido

- **Afirmación:** DAS1 tiene el rol de asegurar la calidad y validez de la base de datos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_3`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.3: Asegurar la Base de Datos en el cumplimiento de los requisitos de seguridad y mejora continua.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Se mencionan seguridad y mejora continua, no calidad topológica ni validez del contenido; la afirmación amplía el numeral.

### H065: Validar el estimador de estado, el flujo de potencia y demás aplicaciones

- **Afirmación:** Valida la necesidad de realizar pruebas técnicas exhaustivas.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Se requieren pruebas antes del despliegue, pero su carácter exhaustivo no está especificado; no debe darse por documentada esa intensidad.

### H066: Definir el requisito y el alcance del cambio

- **Afirmación:** La definición del requisito para el ICCP está ligada a la operación y generación binacional.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_2`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.2: Coordinar y controlar, de acuerdo a criterios técnicos y económicos, la operación electro energética del sistema de potencia desde el punto de vista de la generación eléctrica, considerando los recursos propios (Central Acaray) y los contratos de intercambio con entidades externas (Itaipú y Yacyretá).
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** La operación considerando intercambios está expresa; ICCP y la definición de sus requisitos no figuran en el fragmento.

### H067: Ejecutar el respaldo y la carga en producción

- **Afirmación:** La ejecución técnica recae en el departamento de administración de SCADA/EMS.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = DOES_NOT_SUPPORT`; `claim_type_correct = NO`.
- **Justificación:** El texto externo describe un proceso de cambios y no asigna la ejecución a DAS ni a un departamento equivalente de ANDE.

### H068: Mantener el registro técnico de configuración

- **Afirmación:** GT/DAS1 responsable de la base de datos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_2`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.2: Mantener y actualizar las Bases de Datos existentes para asegurar el correcto funcionamiento y ajustes para nuevos requisitos del sistema.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** La responsabilidad por mantener bases está expresa; no identifica esas bases con el registro técnico de configuración del cambio.

### H069: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** ISC es responsable de la ingeniería de redes de operación.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ISC_2_6`.
- **Texto evaluado:** DTE/ISC (DEPARTAMENTO DE INGENIERÍA DE SISTEMAS DE CONTROL), numeral 2.6: Elaborar, ejecutar y supervisar proyectos de relacionados a redes de comunicaciones (Red de Área Local -- LAN, Red de Área Amplia -- WAN, radio enlaces, etc.) utilizadas para las tecnologías de operación.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** Proyectos de redes OT respaldan la ingeniería de redes; no explicitan toda configuración de adquisición y correspondencia señal-modelo.

### H070: Habilitar o suspender la ventana de intervención en tiempo real

- **Afirmación:** ODC autoriza el uso de la ventana operativa en tiempo real.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_5`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.5: Supervisar, coordinar, ejecutar y autorizar maniobras de equipos en el sistema de potencia mediante el uso del SCADA o mediante orden de operación a los operadores de locales en los siguientes casos: 2.5.1. Trabajos programados por los sectores de mantenimiento y/o supervisión.   2.5.2. Situaciones de urgencia y/o emergencia en tiempo real. 2.5.3. Mantener los parámetros del sistema potencia dentro de valores adecuados.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Autorizar maniobras por mantenimiento o emergencia es pertinente; autorizar una ventana de intervención informática no es la misma actividad expresa.

### H071: Autorizar la liberación de la versión a producción

- **Afirmación:** La liberación a producción de una versión acumulada requiere autorización de la instancia de control operativo.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `ENISA_CHG_01`.
- **Texto evaluado:** ENISA, Technical implementation guidance, v1.0, junio 2025, apdo. 6.4.1. PRINCIPLE: Propone flujos de gestión de cambios diferenciados según criticidad y urgencia, y un comité de cambios cuando resulte apropiado ('where appropriate'). CAN_SUPPORT: diferenciar cambios ordinarios, urgentes y de emergencia; prever un órgano colegiado de cambios si la organización lo considera apropiado. CANNOT_SUPPORT: exigir un comité para todo cambio; designar a una unidad de ANDE como aprobadora; obligar a ANDE
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Se contemplan flujos de cambios y un comité cuando corresponde; no se exige que la autorización provenga de una instancia de control operativo.

### H072: Administrar y actualizar los aplicativos EMS

- **Afirmación:** Establece la necesidad de gestión de configuración y pruebas previas.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Configuración base, documentación y pruebas antes del despliegue respaldan la afirmación general de buena práctica.

### H073: Revisar la calidad topológica y de nomenclatura del modelo construido

- **Afirmación:** Justifica la necesidad de revisar los resultados de la topología antes de liberar.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `ERCOT_02`.
- **Texto evaluado:** Moseley et al., ERCOT NMMS, 2014, p. 15. PRINCIPLE: Cada solicitud de cambio atraviesa cinco niveles de validación: rangos y datos asociados; coherencia manual entre metadatos, cambio y documentación; estudio de impacto sobre el flujo de potencia del caso base; prueba conjunta de los cambios de un intervalo de energización; carga del modelo completo en todas las aplicaciones. El modelo temporal permite construir versiones con cambios futuros según su fecha de vigencia. CAN_SUPPORT: validación escalonada antes de producción; versiones con fecha de vigencia. CANNOT_SUPPORT: asignar niveles de validación a unidades de ANDE
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** La validación de coherencia y del caso de flujo antes de producción respalda revisar el resultado topológico, sin designar una unidad.

### H074: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** Responsabilidad sobre la configuración de las comunicaciones.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ISC2_2_2`.
- **Texto evaluado:** DTE/ISC2 (SECCIÓN IMPLEMENTACIÓN DE SISTEMAS DE CONTROL), numeral 2.2: Realizar o supervisar trabajos relacionados a redes de comunicaciones (Red de Área Local -- LAN, Red de Área Amplia -- WAN, radio enlaces, etc.) utilizadas para las tecnologías de operación.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Realizar trabajos de redes es una atribución general pertinente; responsabilidad específica de configuración no está expresamente descrita.

### H075: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** Segregación entre administración (accountable) y ejecución de configuración (responsible).
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Separar modificación y aprobación no establece necesariamente separar A y R, ni identifica administración con aprobación.

### H076: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** GT/DAS es responsable técnico de la configuración de datos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS_2_1`.
- **Texto evaluado:** GT/DAS (DEPARTAMENTO DE ADMINISTRACIÓN DEL SCADA/EMS), numeral 2.1: Administrar y gestionar la Base de Datos del Sistema Interconectado Nacional (SIN) obtenidos mediante el Sistema SCADA.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Administrar y gestionar bases es pertinente; la ejecución técnica de configuración de datos no se enuncia como función específica.

### H077: Aprobar las pruebas FAT/SAT y de integración

- **Afirmación:** Responsabilidad técnica directa en pruebas de aceptación.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ISC2_2_3`.
- **Texto evaluado:** DTE/ISC2 (SECCIÓN IMPLEMENTACIÓN DE SISTEMAS DE CONTROL), numeral 2.3: Efectuar, analizar y aprobar pruebas de aceptación de fábrica (FAT) y de aceptación del sitio (SAT) de los equipos y sistemas de tecnologías de operación adquiridos.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** Efectuar, analizar y aprobar FAT/SAT establece directamente responsabilidad técnica en esas pruebas de aceptación.

### H078: Habilitar o suspender la ventana de intervención en tiempo real

- **Afirmación:** Separa la ejecución técnica del despliegue de la ventana de operación real.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** La segregación modificación/aprobación es general; separar despliegue técnico y ventana en tiempo real es una regla adicional no enunciada.

### H079: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** Fundamenta la necesidad de centralizar la gestión de cambios de configuración en la unidad administradora.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Se centraliza seguimiento y documentación, no toda gestión de cambios en la unidad administradora; el fragmento impide deducir exclusividad de edición.

### H080: Certificar los datos de la instalación (configuración física y parámetros)

- **Afirmación:** GT/DEL define los parámetros técnicos oficiales para la operación.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DEL_2_1`.
- **Texto evaluado:** GT/DEL (DEPARTAMENTO DE ESTUDIOS ELÉCTRICOS), numeral 2.1: Elaborar estudios sobre la operación eléctrica del Sistema de Generación, Transmisión y Transformación de Energía Eléctrica, para la atención de cargas y optimización de confiabilidad y desempeño económico, así como las interconexiones y suministros especiales.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Elaborar estudios eléctricos es pertinente, pero definir parámetros técnicos oficiales no figura como competencia expresa.

### H081: Unificar modelo y adquisición en la base integrada

- **Afirmación:** Responsabilidad corporativa sobre la integridad de la base de datos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS_2_1`.
- **Texto evaluado:** GT/DAS (DEPARTAMENTO DE ADMINISTRACIÓN DEL SCADA/EMS), numeral 2.1: Administrar y gestionar la Base de Datos del Sistema Interconectado Nacional (SIN) obtenidos mediante el Sistema SCADA.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Administrar la base se relaciona con su integridad; responsabilidad corporativa de integración o unificación no está documentada expresamente.

### H082: Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros)

- **Afirmación:** La sección de base de datos ejecuta la construcción del modelo.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_1`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.1: Diseñar e implementar Base de Datos para almacenar y gestionar datos del SCADA.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Diseñar e implementar bases no nombra construir el modelo eléctrico; existe relación técnica pero falta especificación del objeto.

### H083: Ejecutar el respaldo y la carga en producción

- **Afirmación:** DAS1 es responsable de la carga de base de datos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_2`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.2: Mantener y actualizar las Bases de Datos existentes para asegurar el correcto funcionamiento y ajustes para nuevos requisitos del sistema.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Actualizar bases permite inferir tareas de carga, pero no explicita carga en producción ni su asignación como responsabilidad específica.

### H084: Verificar la correspondencia de mímicos y modelo con la instalación física

- **Afirmación:** DTE/ISC2 realiza la verificación final.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ISC2_2_4`.
- **Texto evaluado:** DTE/ISC2 (SECCIÓN IMPLEMENTACIÓN DE SISTEMAS DE CONTROL), numeral 2.4: Verificar de acuerdo a estándares internacionales y normas de ANDE, la correcta implementación y puesta en servicio de los equipos y sistemas de tecnologías de operación.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Verificar implementación y puesta en servicio está expreso; el carácter final y la correspondencia física de mímicos/modelo amplían ese alcance.

### H085: Definir el requisito y el alcance del cambio

- **Afirmación:** La segregación entre definición del requisito (DOS) y la rendición de cuentas (ODC) es necesaria.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** La segregación general tiene respaldo, pero separar requisito y rendición de cuentas entre DOS y ODC no se deriva de esta fuente externa.

### H086: Configurar la adquisición, la correspondencia señal-modelo y las comunicaciones

- **Afirmación:** La consulta a DTE/MCO es necesaria por su rol en el mantenimiento de equipos e integración al SCADA.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = DOES_NOT_SUPPORT`; `claim_type_correct = NO`.
- **Justificación:** El fragmento no describe MCO ni prescribe consultarlo; la justificación requiere atribuciones institucionales diferentes de esta cita.

### H087: Ejecutar la reversión

- **Afirmación:** La reversión de la base de datos es una función técnica de DAS1.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_2`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.2: Mantener y actualizar las Bases de Datos existentes para asegurar el correcto funcionamiento y ajustes para nuevos requisitos del sistema.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Mantener y actualizar bases respalda un vínculo funcional; revertirlas no aparece como competencia expresa de DAS1.

### H088: Aceptar mímicos, alarmas y el uso operativo

- **Afirmación:** El usuario operativo final debe ser quien apruebe el despliegue para asegurar la disponibilidad.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Aprobar cambios antes del despliegue está respaldado; que apruebe necesariamente el usuario operativo final no está establecido.

### H089: Construir o actualizar el modelo eléctrico (topología, conectividad, parámetros)

- **Afirmación:** Competencia central de GT/DAS sobre el modelo eléctrico.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS_2_1`.
- **Texto evaluado:** GT/DAS (DEPARTAMENTO DE ADMINISTRACIÓN DEL SCADA/EMS), numeral 2.1: Administrar y gestionar la Base de Datos del Sistema Interconectado Nacional (SIN) obtenidos mediante el Sistema SCADA.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** La base del SIN obtenida mediante SCADA está asignada a DAS; competencia central sobre todo el modelo eléctrico no está expresamente declarada.

### H090: Verificar el sistema después de la actualización y cerrar el cambio

- **Afirmación:** Responsabilidad sobre la administración de los aplicativos tras actualizaciones.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS_2_2`.
- **Texto evaluado:** GT/DAS (DEPARTAMENTO DE ADMINISTRACIÓN DEL SCADA/EMS), numeral 2.2: Administrar y gestionar los módulos de los aplicativos informáticos del SCADA/EMS.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** Administrar aplicativos es una atribución continua compatible con el periodo posterior; verificar y cerrar un cambio no está expresamente asignado.

### H091: Aprobar los criterios de reversión y su delegación

- **Afirmación:** Autoridad de decisión operativa ante eventos no deseados.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `ODC_2_1`.
- **Texto evaluado:** GT/ODC (OFICINA DE DESPACHO DE CARGA), numeral 2.1: Supervisar y controlar en tiempo real, la operación eléctrica y energética del sistema de potencia mediante el monitoreo de los parámetros eléctricos típicos, adoptando las medidas necesarias cuando los mismos se aparten de los valores aceptables o preestablecidos en las Instrucciones de Operación del Sistema (IOS) y en las Instrucciones de Operación de las Interconexiones (IOI). 2.1.1. Niveles de tensión en barras de todos los locales del SIN. 2.1.2. Niveles de cargas y corrientes en las líneas de transmisión, transformadores de potencia, compensadores estáticos, bancos de capacitores, reactores y generadores. 2.1.3. Frecuencia de la red a cargo de Itaipú y Yacyretá.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** Adoptar medidas ante parámetros fuera de rango respalda decisión operativa; aprobar criterios de reversión y delegarlos no figura expresamente.

### H092: Ejecutar la reversión

- **Afirmación:** Competencia técnica directa para restaurar la base de datos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_2`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.2: Mantener y actualizar las Bases de Datos existentes para asegurar el correcto funcionamiento y ajustes para nuevos requisitos del sistema.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Mantener y actualizar bases es pertinente a restauración, pero no documenta competencia directa para restaurar versiones.

### H093: Administrar y actualizar los aplicativos EMS

- **Afirmación:** Establece el marco de gestión de cambios para aplicaciones técnicas.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = SI`.
- **Justificación:** El fragmento describe documentación, pruebas, aprobación y seguimiento de cambios; respalda el marco general aplicado a aplicaciones.

### H094: Habilitar o suspender la ventana de intervención en tiempo real

- **Afirmación:** ODC, al tener la visión del sistema en tiempo real, es quien mejor garantiza la seguridad operacional.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_OT_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3 (2023), doi 10.6028/NIST.SP.800-82r3, visión general. PRINCIPLE: La protección de la tecnología operacional (OT) debe considerar sus requisitos particulares de disponibilidad, seguridad física, desempeño y confiabilidad. CAN_SUPPORT: priorizar la disponibilidad y la seguridad operacional al planificar intervenciones. CANNOT_SUPPORT: asignar responsabilidades a unidades concretas
- **Propuesta:** `support = DOES_NOT_SUPPORT`; `claim_type_correct = NO`.
- **Justificación:** La prioridad de seguridad OT no demuestra que ODC sea la unidad que mejor la garantiza; la comparación entre unidades carece de respaldo.

### H095: Preparar el paquete de implementación

- **Afirmación:** La sección base de datos es responsable de las actualizaciones de configuración.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_2`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.2: Mantener y actualizar las Bases de Datos existentes para asegurar el correcto funcionamiento y ajustes para nuevos requisitos del sistema.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Actualizar bases de datos está expreso; extenderlo a toda configuración y preparación de paquetes requiere inferencia adicional.

### H096: Revisar la calidad topológica y de nomenclatura del modelo construido

- **Afirmación:** El aseguramiento de la calidad del modelo es competencia de la unidad administradora de los datos.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_3`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.3: Asegurar la Base de Datos en el cumplimiento de los requisitos de seguridad y mejora continua.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Seguridad y mejora continua de la base no equivalen expresamente a aseguramiento de calidad del modelo topológico.

### H097: Especificar y aceptar la semántica del modelo (nomenclatura, identificadores, representación)

- **Afirmación:** La definición semántica formal requiere aprobación.
- **Tipo declarado:** `BUENA_PRACTICA`.
- **Fuente:** `NIST_CM_01`.
- **Texto evaluado:** NIST SP 800-82 Rev. 3, sec. 6.2.4.2. PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios. CAN_SUPPORT: segregación entre modificación y aprobación; trazabilidad; gestión de configuración; registro centralizado de cambios. CANNOT_SUPPORT: asignar la aprobación a una unidad concreta; deducir exclusividad departamental de edición a partir de la centralización del registro
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Aprobar cambios es una práctica expresa, pero aprobar específicamente una definición semántica requiere conectar esa definición con un cambio de configuración.

### H098: Preparar el paquete de implementación

- **Afirmación:** GT/DAS2 gestiona los aplicativos del SCADA/EMS.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS2_2_1`.
- **Texto evaluado:** GT/DAS2 (SECCIÓN APLICATIVOS DEL SCADA/EMS), numeral 2.1: Administrar y gestionar el uso de aplicativos disponibles del SCADA/EMS, previsión de carga de barras, procesamiento de topología de red, estimador de estado, análisis de contingencias, flujo de potencia óptimo, etc.
- **Propuesta:** `support = SUPPORTS`; `claim_type_correct = NO`.
- **Justificación:** La gestión de aplicativos SCADA/EMS es textual; preparar el paquete de implementación no está establecido en ese numeral.

### H099: Unificar modelo y adquisición en la base integrada

- **Afirmación:** La sección técnica de base de datos es la responsable de la unificación técnica.
- **Tipo declarado:** `DOCUMENTADO`.
- **Fuente:** `DAS1_2_1`.
- **Texto evaluado:** GT/DAS1 (SECCIÓN BASE DE DATOS DEL SCADA), numeral 2.1: Diseñar e implementar Base de Datos para almacenar y gestionar datos del SCADA.
- **Propuesta:** `support = PARTIAL`; `claim_type_correct = NO`.
- **Justificación:** Diseñar e implementar bases es pertinente; unificar modelo y adquisición no aparece como competencia específica expresa.

## Trazabilidad e integridad

SHA-256 de las planillas originales leídas, que permanecen sin cambios:

- `audit_sheet_coder1.csv`: `a2b14b4020e974c72cf2314bc1a300ecc448ac30bd71e3c7c1b249935f91c796`
- `audit_sheet_coder2.csv`: `a2b14b4020e974c72cf2314bc1a300ecc448ac30bd71e3c7c1b249935f91c796`

Archivos generados:

- `audit_sheet_coder1_preauditoria_IA.csv`: SHA-256 `6783ed4bbab6d8c1b2e461ad524e73cfac67bc75e94abf2b2e1054fe6430f207`
- `audit_sheet_coder2_preauditoria_IA.csv`: SHA-256 `6783ed4bbab6d8c1b2e461ad524e73cfac67bc75e94abf2b2e1054fe6430f207`

Codificación CSV: UTF-8 con BOM para facilitar su apertura en Excel; separador coma; 11 columnas; 99 ítems. Ambos CSV son copias idénticas de una única evaluación IA.
