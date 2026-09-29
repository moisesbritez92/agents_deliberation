# Artículo sobre atribuciones SCADA/EMS

Documento técnico en formato IEEE para analizar y proponer la distribución de responsabilidades entre GT/DAS y las unidades técnicas de telecomunicaciones y plataforma OT.

## Archivos

- `main.tex`: manuscrito principal.
- `referencias.bib`: bibliografía en formato BibTeX.
- `compilar.ps1`: compilación reproducible con MiKTeX.
- `evidencia_gobernanza.md`: trazabilidad de fuentes del cuaderno, localizadores verificados, correcciones a las síntesis y límites de uso.
- `suplemento/`: suplemento S1, matriz de extracción y codificación de los 135 numerales (CSV y Markdown) y el script que la genera (`python suplemento/generar_matriz.py`).

## Compilación

Desde PowerShell:

```powershell
.\compilar.ps1
```

El script utiliza `pdflatex` y `bibtex` directamente porque la instalación local de `latexmk` no dispone del intérprete Perl requerido.

## Estado

La versión revisada incorpora catorce fichas: DTE/ISC, ISC1, ISC2, ISC3 y MCO (Resolución 48658, 29-12-2023), GT/DAS, DAS1 y DAS2 (Resolución 50060, 06-01-2025), y GT/OP, ODC, DOS, DEL, DEN y DDR (Resolución 34954, 15-07-2014). Integra bibliografía de gobierno, seguridad OT y modelos de red: NIST, ISACA, ENISA, IEC 61970-456 y EPRI. Es una propuesta de coordinación, no un dictamen de exclusividad ni una auditoría de conformidad normativa.

PDF compilado (24/09/2026): **15 páginas**, 38 referencias citadas, 20 fichas y 135 numerales codificados, 20 actividades RACI trazadas a diez reglas de diseño. Sin citas indefinidas ni desbordamientos de cajas; BibTeX sin advertencias.

## Revisión del 23/09/2026 (respuesta al revisor)

- Contribución reformulada como método de descomposición objeto–fase–tipo de autoridad, con preguntas de investigación.
- Codificación completa de 135 numerales de 20 fichas, incluidas GT/DT y sus cinco departamentos regionales (suplemento S1), y Fig. 1 con la cadena analítica.
- Práctica internacional basada en Moseley et al. (ERCOT, 2014) y PJM Manual 3A rev. 27 (2026), con tabla comparativa.
- Reglas R1–R10, alternativas descartadas y columna de regla en la RACI.
- Protocolo de validación retrospectiva especificado, no ejecutado.
- CIP-010-4 fechada con el historial oficial de versiones.

## Cambios de la revisión

- DAS1 tiene atribuciones expresas de diseño, implementación, mantenimiento y actualización. Se revisó el reparto anterior para reconocer construcción coordinada, además de aceptación funcional.
- DAS2 administra y actualiza aplicativos, incluido procesamiento de topología. No se confunde esta atribución con exclusividad sobre toda la conectividad.
- Nuevo apartado IEC 61970: conectividad, topología procesada, resultados, Model Authority y límites de equivalencia entre MAS normativo y paquete propietario.
- EPRI se utiliza como referencia de requisitos y escenarios de gestión integrada; no como prueba de funciones multiusuario de e-terra.
- Método redactado como revisión documental y bibliográfica; la única mención de NotebookLM en el manuscrito está en la declaración de uso de IA al final, después de las referencias.
- Los archivos de `resumen_correos` se leyeron solo como contexto. No integran el corpus probatorio, las citas ni la argumentación factual del artículo.

- Introducción centrada en operación del SIN y concurrencia de mandatos, sin presuponer transferencia indebida.
- Distinción entre subordinación documentada a División de Operación y relación funcional con Despacho de Carga.
- Tabla de concurrencias con numerales y reconocimiento de la elaboración/unificación de bases por ISC2 2.5.
- RACI con autoridad de cambio visible y una A por fila; diferencia aprobación técnica, aceptación funcional y liberación.
- Reconocimiento del visto bueno de GT/DAS ya incluido en el borrador de procedimiento.
- Incorporación de la concurrencia DOS–DAS en soporte y de las unidades de estudios y despacho regional según el objeto del cambio.
- Separación entre liberación de versión por AC y habilitación de ventana en tiempo real por ODC, esta última como propuesta a formalizar.
- Autoridad interáreas con delegación institucional, decisor identificable, suplencias y emergencias preautorizadas.
- Segregación entre personas, roles y permisos, sin deducirla automáticamente del organigrama.
- NIST citado por secciones y AC-5; RACI adaptable de ISACA; ENISA con alcance y carácter no vinculante explícitos.

## Evidencia pendiente

- Resoluciones completas y disposiciones modificatorias; las fichas GT ya se incorporaron y cotejaron con los PDF.
- Inventario de bases y aplicaciones, arquitectura y manuales del fabricante; especialmente SUBTOP/RTUTOP, MAS y DBSEQ.
- Verificación de cláusulas completas de normas IEC y metadatos/versiones de referencias externas. Las fichas de alcance público no equivalen a revisión integral de las normas.
- Ejecución del protocolo de validación: expedientes de 10 a 20 cambios históricos, segundo codificador y panel de expertos.
- Texto completo de trabajos sobre gestión de modelos EMS citados por el revisor (CAISO, NSTAR, AEP/PJM 2024) antes de incorporarlos.
- Se revisaron fuentes seleccionadas de gobierno y del nuevo repositorio IEC 61970. El extracto 61970-301:2020 contiene portada e índice; el de 61970-456:2018 sí permite revisar introducción, alcance y sección 5. No se ha comprobado el texto íntegro ni que sean las últimas ediciones aplicables al sistema.
