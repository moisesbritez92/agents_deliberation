# CORPUS EXTERNO

Evidencia externa y contexto técnico. Puede justificar principios de diseño o buenas prácticas; no puede crear competencias institucionales. Cada entrada indica qué puede sustentar (CAN_SUPPORT) y qué no (CANNOT_SUPPORT).

SOURCE_ID: IEC61970_456_01
SOURCE_TYPE: norma_internacional
REFERENCE: IEC 61970-456:2018 ed. 2, sec. 5, pp. 8-13 (pasajes disponibles públicamente)
PRINCIPLE: La norma distingue equipos y conectividad, condiciones de entrada (estados de maniobra, mediciones), topología procesada y variables de estado. Los terminales vinculan equipos conductores con nodos de conectividad. En una representación nodo-interruptor, el procesamiento de topología utiliza la conectividad y los estados de maniobra para formar los nodos topológicos de cálculo. Las variables de estado describen resultados de flujo de potencia o de estimación.
CAN_SUPPORT:
  - distinguir técnicamente la edición de la conectividad, la configuración del procesador de topología y la validación de sus resultados
  - identificar dependencias entre modelo eléctrico, mediciones y aplicaciones EMS
CANNOT_SUPPORT:
  - asignar cualquiera de esas actividades a una unidad organizativa concreta
  - demostrar que la herramienta instalada permite o impide la edición concurrente

SOURCE_ID: IEC61970_456_02
SOURCE_TYPE: norma_internacional
REFERENCE: IEC 61970-456:2018 ed. 2, sec. 5, pp. 8-10
PRINCIPLE: Los datos de red se organizan en perfiles de información y en particiones bajo una Model Authority, responsable de sus datos; esas particiones se denominan Model Authority Sets (MAS).
CAN_SUPPORT:
  - asociar responsabilidad sobre conjuntos de datos definidos del modelo
  - delimitar objetos por partición y no por sistema completo
CANNOT_SUPPORT:
  - designar qué unidad de ANDE es Model Authority
  - equiparar el MAS de IEC con un paquete propietario del fabricante denominado MAS

SOURCE_ID: IEC61970_301_01
SOURCE_TYPE: norma_internacional
REFERENCE: IEC 61970-301:2020 ed. 7 (identificación bibliográfica) e IEC 61970-456:2018, p. 6
PRINCIPLE: El Modelo de Información Común (CIM) es un modelo abstracto de los objetos necesarios para representar aspectos operativos de una empresa eléctrica. El nivel semántico no especifica por sí solo el esquema físico de una base de datos ni los permisos de una herramienta comercial.
CAN_SUPPORT:
  - usar una semántica común para identificar objetos del modelo
CANNOT_SUPPORT:
  - resolver el organigrama
  - determinar permisos de acceso de la plataforma instalada

SOURCE_ID: IEC61850_6_01
SOURCE_TYPE: norma_internacional
REFERENCE: IEC 61850-6 (alcance)
PRINCIPLE: IEC 61850 normaliza modelos de datos y servicios de comunicación para la automatización de sistemas eléctricos. La Parte 6 define el lenguaje de descripción de configuración (SCL) para el intercambio entre herramientas de ingeniería de IED, lo que favorece la trazabilidad entre proceso, IED, estación y centro de control.
CAN_SUPPORT:
  - trazabilidad de la configuración de IED y de la señal desde el campo hasta el centro de control
CANNOT_SUPPORT:
  - concluir qué unidad debe mantener el modelo eléctrico del EMS
  - asignar pruebas o configuración a una unidad concreta

SOURCE_ID: IEC62443_01
SOURCE_TYPE: norma_internacional
REFERENCE: ISA, visión general de la serie ISA/IEC 62443
PRINCIPLE: La serie ISA/IEC 62443 establece requisitos y procesos para proteger sistemas de automatización y control industrial. Su enfoque comprende al propietario del activo, integradores, proveedores de productos y prestadores de servicios, y se basa en la responsabilidad compartida entre ellos.
CAN_SUPPORT:
  - participación de varios roles en la seguridad del sistema de control
  - responsabilidad compartida en seguridad OT
CANNOT_SUPPORT:
  - asignar a una unidad concreta el control de configuración
  - equiparar un rol de la norma con un departamento

SOURCE_ID: IEC62443_2_1_01
SOURCE_TYPE: norma_internacional
REFERENCE: IEC 62443-2-1:2024 ed. 2.0, alcance público
PRINCIPLE: Especifica requisitos del programa de seguridad del propietario del activo para sistemas en operación; el rol de propietario del activo incluye al operador del sistema. Contempla medidas compensatorias ante limitaciones de sistemas heredados.
CAN_SUPPORT:
  - existencia de políticas y procedimientos de seguridad para sistemas en operación
  - medidas compensatorias cuando el sistema heredado no permite ciertos controles
CANNOT_SUPPORT:
  - identificar qué unidad interna ejerce el rol de propietario del activo
  - demostrar requisitos detallados de aprobación de cambios

SOURCE_ID: IEC62443_3_2_01
SOURCE_TYPE: norma_internacional
REFERENCE: IEC 62443-3-2 (alcance)
PRINCIPLE: Aborda la evaluación de riesgos de seguridad y el diseño del sistema de automatización y control industrial.
CAN_SUPPORT:
  - evaluar el riesgo de seguridad de un cambio según su criticidad
CANNOT_SUPPORT:
  - asignar responsabilidades organizativas específicas

SOURCE_ID: ISA95_01
SOURCE_TYPE: norma_internacional
REFERENCE: IEC 62264 / ISA-95, visión general
PRINCIPLE: Define modelos y terminología para integrar sistemas empresariales y sistemas de control de manufactura mediante niveles funcionales.
CAN_SUPPORT:
  - distinguir niveles funcionales de un sistema integrado
CANNOT_SUPPORT:
  - hacer corresponder un nivel funcional con una dependencia de una empresa eléctrica

SOURCE_ID: NIST_OT_01
SOURCE_TYPE: guia_tecnica
REFERENCE: NIST SP 800-82 Rev. 3 (2023), doi 10.6028/NIST.SP.800-82r3, visión general
PRINCIPLE: La protección de la tecnología operacional (OT) debe considerar sus requisitos particulares de disponibilidad, seguridad física, desempeño y confiabilidad.
CAN_SUPPORT:
  - priorizar la disponibilidad y la seguridad operacional al planificar intervenciones
CANNOT_SUPPORT:
  - asignar responsabilidades a unidades concretas

SOURCE_ID: NIST_CM_01
SOURCE_TYPE: guia_tecnica
REFERENCE: NIST SP 800-82 Rev. 3, sec. 6.2.4.2
PRINCIPLE: Documentar la configuración base aprobada; documentar, probar y aprobar los cambios antes de su despliegue; centralizar el seguimiento y la documentación de los cambios.
CAN_SUPPORT:
  - segregación entre modificación y aprobación
  - trazabilidad
  - gestión de configuración
  - registro centralizado de cambios
CANNOT_SUPPORT:
  - asignar la aprobación a una unidad concreta
  - deducir exclusividad departamental de edición a partir de la centralización del registro

SOURCE_ID: NIST_CM_02
SOURCE_TYPE: guia_tecnica
REFERENCE: NIST SP 800-82 Rev. 3, sec. 6.2.4.3
PRINCIPLE: Verificar los respaldos y probar la restauración, integrando la recuperación con la gestión de cambios.
CAN_SUPPORT:
  - exigir respaldo verificable y restauración probada antes y después de un cambio
CANNOT_SUPPORT:
  - asignar la ejecución del respaldo o de la restauración a una unidad concreta

SOURCE_ID: NIST_AC_01
SOURCE_TYPE: guia_tecnica
REFERENCE: NIST SP 800-82 Rev. 3, sec. 6.2.1.1
PRINCIPLE: El control de acceso basado en roles asigna a cada persona los privilegios necesarios, con niveles diferenciados para consultar, utilizar y alterar datos o funciones.
CAN_SUPPORT:
  - mínimo privilegio
  - diferenciar permisos de lectura, uso y modificación
CANNOT_SUPPORT:
  - asignar roles a departamentos concretos

SOURCE_ID: NIST_SOD_01
SOURCE_TYPE: guia_tecnica
REFERENCE: NIST SP 800-82 Rev. 3, apéndice F, AC-5 (separación de funciones)
PRINCIPLE: En OT debe considerarse cuidadosamente la acumulación de roles críticos en una misma persona; se contemplan controles compensatorios de personal y de auditoría cuando la separación completa no es posible.
CAN_SUPPORT:
  - separación entre autoría y revisión a nivel de personas
  - controles compensatorios
CANNOT_SUPPORT:
  - exigir que funciones separadas residan en departamentos distintos
  - asignar funciones a unidades concretas

SOURCE_ID: NIST_TEAM_01
SOURCE_TYPE: guia_tecnica
REFERENCE: NIST SP 800-82 Rev. 3, sec. 3.3.2
PRINCIPLE: Recomienda un equipo multidisciplinario y coordinación entre seguridad OT, TI y gestión de riesgos.
CAN_SUPPORT:
  - participación interáreas en la seguridad OT
CANNOT_SUPPORT:
  - considerar ese equipo como un órgano que aprueba cada actualización del modelo
  - asignar autoridad de aprobación a una unidad concreta

SOURCE_ID: NERC_CIP010_01
SOURCE_TYPE: norma_sectorial_extranjera
REFERENCE: NERC CIP-010-4
PRINCIPLE: Establece controles de gestión de cambios de configuración y evaluación de vulnerabilidades para los sistemas cibernéticos aplicables dentro de su ámbito regulatorio norteamericano.
CAN_SUPPORT:
  - referencia sectorial de gestión de cambios de configuración
CANNOT_SUPPORT:
  - obligar a ANDE, que no está en su ámbito regulatorio
  - asignar responsabilidades a unidades concretas

SOURCE_ID: ENISA_ROLES_01
SOURCE_TYPE: guia_tecnica
REFERENCE: ENISA, Technical implementation guidance, v1.0, junio 2025, apdos. 1.2.4-1.2.5
PRINCIPLE: Distingue funciones incompatibles e independencia del auditor, y admite asignar responsabilidades adicionales a roles existentes según el tamaño y los recursos de la organización.
CAN_SUPPORT:
  - identificar funciones incompatibles
  - acumular roles compatibles en organizaciones con recursos limitados
  - independencia de la auditoría
CANNOT_SUPPORT:
  - obligar a ANDE (guía no vinculante para entidades digitales de la UE)
  - asignar funciones a unidades concretas

SOURCE_ID: ENISA_CHG_01
SOURCE_TYPE: guia_tecnica
REFERENCE: ENISA, Technical implementation guidance, v1.0, junio 2025, apdo. 6.4.1
PRINCIPLE: Propone flujos de gestión de cambios diferenciados según criticidad y urgencia, y un comité de cambios cuando resulte apropiado ('where appropriate').
CAN_SUPPORT:
  - diferenciar cambios ordinarios, urgentes y de emergencia
  - prever un órgano colegiado de cambios si la organización lo considera apropiado
CANNOT_SUPPORT:
  - exigir un comité para todo cambio
  - designar a una unidad de ANDE como aprobadora
  - obligar a ANDE

SOURCE_ID: ENISA_CHG_02
SOURCE_TYPE: guia_tecnica
REFERENCE: ENISA, Technical implementation guidance, v1.0, junio 2025, apdos. 6.4.2-6.4.3
PRINCIPLE: Contempla aprobación, reversión y registro de evidencia de los cambios, incluidos los cambios excepcionales o de emergencia, que se documentan y revisan con posterioridad.
CAN_SUPPORT:
  - prever reversión y su evidencia
  - revisión posterior de cambios de emergencia
CANNOT_SUPPORT:
  - asignar la reversión o su autorización a una unidad concreta
  - obligar a ANDE

SOURCE_ID: ISACA_RACI_01
SOURCE_TYPE: articulo_profesional
REFERENCE: P. C. Tessin, 'RA(CI) Light', ISACA Now, 21/05/2020 (COBIT 2019)
PRINCIPLE: Las matrices RACI de COBIT son una vista inicial y orientativa que cada organización debe adaptar a su contexto.
CAN_SUPPORT:
  - adaptar una matriz RACI a la organización
CANNOT_SUPPORT:
  - atribuir a una unidad concreta la aprobación de cambios
  - constituir una norma organizativa

SOURCE_ID: ERCOT_01
SOURCE_TYPE: practica_de_operador
REFERENCE: Moseley et al., ERCOT NMMS, 2014, p. 14
PRINCIPLE: Antes de su sistema de gestión del modelo (NMMS), los propietarios enviaban documentos y correos a varios grupos internos de ERCOT, cada uno con fuentes de datos independientes; la carga manual impedía saber quién había modificado un dato, por qué y cuándo. ERCOT diseñó una solicitud de cambio del modelo (NOMCR) formada por un archivo CIM incremental y metadatos, con una aplicación de seguimiento que registra revisión, pruebas y carga.
CAN_SUPPORT:
  - trazabilidad de quién, qué, cuándo, dónde y por qué de cada cambio
  - evitar fuentes de datos paralelas
CANNOT_SUPPORT:
  - asignar unidades de ANDE
  - demostrar la práctica actual de ERCOT

SOURCE_ID: ERCOT_02
SOURCE_TYPE: practica_de_operador
REFERENCE: Moseley et al., ERCOT NMMS, 2014, p. 15
PRINCIPLE: Cada solicitud de cambio atraviesa cinco niveles de validación: rangos y datos asociados; coherencia manual entre metadatos, cambio y documentación; estudio de impacto sobre el flujo de potencia del caso base; prueba conjunta de los cambios de un intervalo de energización; carga del modelo completo en todas las aplicaciones. El modelo temporal permite construir versiones con cambios futuros según su fecha de vigencia.
CAN_SUPPORT:
  - validación escalonada antes de producción
  - versiones con fecha de vigencia
CANNOT_SUPPORT:
  - asignar niveles de validación a unidades de ANDE

SOURCE_ID: ERCOT_03
SOURCE_TYPE: practica_de_operador
REFERENCE: Moseley et al., ERCOT NMMS, 2014, p. 15
PRINCIPLE: Cuando los mismos departamentos que mantienen una aplicación gestionan también sus datos, aparecen divergencias de datos entre aplicaciones y defectos de la lógica de la aplicación enmascarados por manipulación de los datos. ERCOT respondió con un conjunto de datos único para todas las aplicaciones.
CAN_SUPPORT:
  - separar quien modifica datos de quien valida la aplicación que los usa
  - un conjunto de datos único para todas las aplicaciones
CANNOT_SUPPORT:
  - asignar esas funciones a unidades concretas de ANDE
  - demostrar la práctica actual de ERCOT

SOURCE_ID: ERCOT_04
SOURCE_TYPE: practica_de_operador
REFERENCE: Moseley et al., ERCOT NMMS, 2014, p. 19
PRINCIPLE: Tras la implantación, dar a los propietarios de los equipos acceso a los datos de sus propios equipos facilitó que detectaran y corrigieran errores.
CAN_SUPPORT:
  - participación de quien conoce la instalación física en la verificación de su representación
CANNOT_SUPPORT:
  - asignar unidades de ANDE

SOURCE_ID: ERCOT_05
SOURCE_TYPE: practica_de_operador
REFERENCE: Moseley et al., ERCOT NMMS, 2014, pp. 16-17
PRINCIPLE: Los diagramas unifilares del EMS se actualizaban manualmente a partir de documentos; se omitían cambios y los errores solían ser descubiertos por los operadores durante una maniobra.
CAN_SUPPORT:
  - riesgo de la transcripción manual de documentos a mímicos y modelo
  - necesidad de verificar la correspondencia con la instalación
CANNOT_SUPPORT:
  - asignar la verificación a una unidad concreta

SOURCE_ID: ERCOT_06
SOURCE_TYPE: practica_de_operador
REFERENCE: Moseley et al., ERCOT NMMS, 2014, p. 12
PRINCIPLE: ERCOT es un operador independiente que no posee los equipos que modela; la interfaz principal es entre el operador y propietarios que son empresas distintas.
CAN_SUPPORT:
  - advertir los límites de transferir su arreglo a una empresa verticalmente integrada
CANNOT_SUPPORT:
  - demostrar qué arreglo interno conviene a una empresa verticalmente integrada

SOURCE_ID: PJM_01
SOURCE_TYPE: practica_de_operador
REFERENCE: PJM Manual 03A, rev. 27 (2026), sec. 3.1, p. 34
PRINCIPLE: El representante de cada propietario de transmisión ante el subcomité de operación responde por la información del modelo de su sistema.
CAN_SUPPORT:
  - responsabilidad de quien origina el dato sobre su exactitud
CANNOT_SUPPORT:
  - asignar unidades de ANDE
  - transferir automáticamente el arreglo de un operador independiente

SOURCE_ID: PJM_02
SOURCE_TYPE: practica_de_operador
REFERENCE: PJM Manual 03A, rev. 27, sec. 3.1, p. 35
PRINCIPLE: El personal de PJM interpreta y codifica los datos recibidos para preparar las actualizaciones del EMS, con cuatro actualizaciones programadas por año.
CAN_SUPPORT:
  - separación entre quien aporta el dato y quien lo codifica en el modelo
  - calendario programado de versiones
CANNOT_SUPPORT:
  - asignar unidades de ANDE

SOURCE_ID: PJM_03
SOURCE_TYPE: practica_de_operador
REFERENCE: PJM Manual 03A, rev. 27, sec. 3.2, p. 44; sec. 4.1, p. 52
PRINCIPLE: Los propietarios revisan informes de diferencias preliminares y finales y validan que el modelo representa con exactitud sus sistemas.
CAN_SUPPORT:
  - revisión de diferencias respecto de la versión base
  - validación de la representación por quien origina el dato
CANNOT_SUPPORT:
  - asignar unidades de ANDE

SOURCE_ID: PJM_04
SOURCE_TYPE: practica_de_operador
REFERENCE: PJM Manual 03A, rev. 27, sec. 5.4, p. 65
PRINCIPLE: Antes de pasar un modelo a producción se aplica una prueba de estabilización de hasta cuatro semanas con telemetría real; durante los dos días previos se aplican criterios del estimador de estado (convergencia, soluciones consecutivas no convergentes, iteraciones, datos erróneos). Ante condiciones no previstas se analiza la situación y se documenta la decisión de continuar.
CAN_SUPPORT:
  - criterios objetivos de pase a producción
  - documentar la decisión de continuar ante desviaciones
CANNOT_SUPPORT:
  - copiar umbrales sin calibración local
  - asignar unidades de ANDE

SOURCE_ID: EPRI_NMM_01
SOURCE_TYPE: informe_tecnico
REFERENCE: EPRI 3002003053, Network Model Manager Technical Market Requirements, 2014
PRINCIPLE: Especifica requisitos para una función de gestión de modelos con repositorio maestro, registro de objetos y espacios de trabajo.
CAN_SUPPORT:
  - repositorio maestro único
  - espacios de trabajo separados para preparar cambios
CANNOT_SUPPORT:
  - demostrar capacidades del software instalado
  - asignar unidades de ANDE

SOURCE_ID: EPRI_NMM_02
SOURCE_TYPE: informe_tecnico
REFERENCE: EPRI 3002003053, caso A1, pp. 4-5 a 4-6
PRINCIPLE: En el caso de uso A1, modeladores EMS mantienen conectividad y esquemas, con aportes y revisión de especialistas de planificación y protecciones. El informe aclara que el reparto puede variar entre empresas y que varios grupos requieren controles de acceso y coordinación.
CAN_SUPPORT:
  - separación entre aportantes especializados y modeladores
  - controles de acceso y coordinación entre grupos
CANNOT_SUPPORT:
  - constituir un organigrama obligatorio
  - identificar qué unidad de ANDE cumple el rol de modelador

SOURCE_ID: EPRI_NMM_03
SOURCE_TYPE: informe_tecnico
REFERENCE: EPRI 3002003053, requisito R2, pp. 6-21 a 6-22
PRINCIPLE: Contempla registros de correspondencia entre identificadores CIM (mRID) y estructuras de identificación locales; un mRID no es necesariamente idéntico a una clave propietaria.
CAN_SUPPORT:
  - documentar clase, identificador, origen y correspondencias de cada objeto
CANNOT_SUPPORT:
  - asignar unidades de ANDE

SOURCE_ID: ENTSOE_CGMES_01
SOURCE_TYPE: practica_de_operador
REFERENCE: ENTSO-E, CGMES
PRINCIPLE: ENTSO-E adoptó el estándar CGMES, basado en CIM, para el intercambio de modelos entre operadores.
CAN_SUPPORT:
  - intercambio estructurado de modelos basado en CIM
CANNOT_SUPPORT:
  - asignar unidades de ANDE

SOURCE_ID: CTX_DOMINIOS
SOURCE_TYPE: contexto_tecnico
REFERENCE: Contexto técnico del dominio SCADA/EMS
PRINCIPLE: Bajo la denominación general de 'base SCADA/EMS' coexisten seis dominios técnicos: (1) modelo eléctrico: topología, conectividad, parámetros de líneas y transformadores, equivalentes y estados operativos; (2) telemetría y telecontrol: puntos analógicos y digitales, calidad, escalas, comandos, alarmas, tiempos y correspondencia con equipos; (3) comunicaciones: RTU, IED, gateways, canales, direccionamiento, protocolos, ICCP/TASE.2 y sincronización; (4) aplicaciones EMS: estimador de estado, flujo de potencia, contingencias, control automático de generación y demás módulos; (5) plataforma técnica: servidores, almacenamiento, sistemas operativos, respaldo, virtualización, ambientes y herramientas del fabricante; (6) gobierno y seguridad: acceso, trazabilidad, configuración base, evidencias, aceptación, reversión y auditoría.
CAN_SUPPORT:
  - delimitar el objeto afectado por cada decisión
  - identificar competencias técnicas requeridas por dominio
CANNOT_SUPPORT:
  - asignar dominios a unidades concretas

SOURCE_ID: CTX_CICLO
SOURCE_TYPE: contexto_tecnico
REFERENCE: Contexto técnico del ciclo de cambio
PRINCIPLE: El ciclo de un cambio de la base SCADA/EMS comprende las fases de planificación, requisito, construcción, integración, prueba, aceptación, liberación, despliegue, operación y registro. Los tipos de intervención posibles incluyen ejecutar, supervisar, revisar, aprobar, administrar, autorizar en tiempo real, coordinar, apoyar, solicitar y definir criterios.
CAN_SUPPORT:
  - ubicar cada decisión en una fase del ciclo
  - distinguir tipos de intervención sobre una misma fase
CANNOT_SUPPORT:
  - asignar fases o tipos de intervención a unidades concretas

SOURCE_ID: CTX_MIMICO
SOURCE_TYPE: contexto_tecnico
REFERENCE: Contexto técnico del dominio SCADA/EMS
PRINCIPLE: Un mímico es la representación gráfica de una instalación en las consolas del SCADA/EMS: diagrama unifilar con los equipos, sus estados (abierto/cerrado), mediciones, alarmas y, cuando existen, los puntos de mando. Se vincula a los puntos de telemetría y telecontrol y a los objetos del modelo eléctrico; un mímico correcto requiere que ambas correspondencias reflejen la instalación física.
CAN_SUPPORT:
  - delimitar el objeto 'mímico' y sus dependencias con telemetría y modelo
CANNOT_SUPPORT:
  - asignar la construcción, verificación o aceptación de mímicos a una unidad concreta

SOURCE_ID: CTX_UNIFILAR
SOURCE_TYPE: practica_local_descrita
REFERENCE: Práctica descrita por personal de ANDE para este trabajo; no figura en ninguna ficha del Manual de Organización
PRINCIPLE: Según la práctica descrita, las unidades regionales a cargo de las instalaciones de transmisión en servicio (U18, U16, U21, U20, U11) no editan el SCADA: publican el diagrama unifilar oficial de cada instalación como archivo PDF en la red corporativa de TI, y los mímicos y el modelo se construyen a partir de ese documento.
CAN_SUPPORT:
  - identificar el documento de origen de la configuración física
  - reconocer el riesgo de transcripción manual
CANNOT_SUPPORT:
  - constituir una atribución formal de ninguna unidad

SOURCE_ID: CTX_CORPUS
SOURCE_TYPE: contexto_documental
REFERENCE: Estado del corpus institucional
PRINCIPLE: El corpus contiene fichas del Manual de Organización aprobadas por tres resoluciones distintas (P/N.º 34954 de 15/07/2014; P/N.º 48658 de 29/12/2023; P/N.º 50060 de 06/01/2025). No se dispone de las resoluciones completas ni de eventuales disposiciones modificatorias. Ninguna ficha del corpus contiene una disposición expresa que derogue o modifique atribuciones de otra ficha. Tampoco se dispone del inventario de objetos, de los permisos efectivos de la plataforma ni de la documentación del fabricante.
CAN_SUPPORT:
  - declarar límites de la evidencia disponible
CANNOT_SUPPORT:
  - presumir derogaciones o modificaciones no documentadas
