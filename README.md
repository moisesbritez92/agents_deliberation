# Experimento de deliberación multiagente: asignación RACI en SCADA/EMS

Pregunta: ¿hasta qué punto diferentes perspectivas técnicas, partiendo de un mismo corpus documental y con el mismo modelo de lenguaje, convergen en asignaciones de responsabilidad equivalentes, y cómo cambia esa convergencia después de una deliberación estructurada?

El desacuerdo persistente y la ambigüedad sistemática son resultados válidos. No se ajustan prompts ni escenarios para aumentar el acuerdo.

## Instalación y ejecución

```bash
pip install -r requirements.txt
export GEMINI_API_KEY="..."            # PowerShell: $env:GEMINI_API_KEY="..."

python build_corpus.py                 # corpus, inventario y REFERENCE_RACI aislada (sin API)
python experiment.py --label smoke --scenarios S01 --reps 1    # smoke test: 14 llamadas
python analysis.py --label smoke
python experiment.py --label pilot     # piloto: 10 escenarios x 20 repeticiones (~2800 llamadas)
python analysis.py --label pilot
python ver_corrida.py --label pilot --run 7 --scenario S03   # ver una corrida concreta
```

Opciones de `experiment.py`: `--workers N` (corridas en paralelo), `--resume` (continuar una ejecución interrumpida; se rechaza si cambiaron prompts, corpus o modelo), `--dry-run` (respuestas simuladas, sin coste, solo para probar el pipeline). Nunca se sobrescribe `results/<label>/raw_results.jsonl`.

**Otro modelo (réplica con otra familia).** `--model gpt-6-luna` usa la API Responses de OpenAI (`OPENAI_API_KEY` en `.env`; `pip install openai`). Mismo material, prompts y fases; esquema JSON en modo estricto (`strict_schema`: los campos opcionales se declaran anulables y los `null` se retiran, de modo que la salida tiene la misma forma que con Gemini); razonamiento `medium`; nivel de servicio `flex` (50 % del precio Standard). La API no admite semilla: `SEED_BASE + run_id` solo baraja el orden. El coste de cada llamada se calcula con el precio del modelo que la hizo (`config.PRICES`).

La configuración (modelo, thinking level, repeticiones, precios) está en `config.py`. Para un experimento de robustez con otro modelo basta cambiar `MODEL` y usar otra etiqueta.

## Archivos

| Archivo | Contenido |
|---|---|
| `config.py` | Modelo, parámetros, repeticiones, precios por millón de tokens |
| `build_corpus.py` | Extrae texto de todos los documentos, construye corpus y REFERENCE_RACI |
| `experiment.py` | Fases 1-3 y registro de cada llamada |
| `analysis.py` | Métricas, CSV e informe final |
| `ver_corrida.py` | Visor: reconstruye en Markdown la deliberación completa de una corrida (`--run N --scenario SXX` o `--all`) en `results/<label>/corridas/` |
| `citation_audit.py` | Auditoría de pertinencia de citas (control determinista, juez ciego, doble codificación humana) |
| `validacion_humana/` | Guía y plantillas de las tareas humanas (neutralidad del material antes del piloto, auditoría de citas después) |
| `BITACORA.md` | Registro fechado de decisiones, cambios y resultados del experimento |
| `corpus_institutional.md/.json` | 20 fichas, 135 numerales de atribución, más subordinación y organización; texto literal |
| `corpus_external.md/.json` | 37 fuentes externas y de contexto con CAN_SUPPORT / CANNOT_SUPPORT |
| `sources/external_sources.json` | Fuente curada del corpus externo |
| `activities.json` | Catálogo de 20 actividades del ciclo de cambio (nombres neutros) |
| `scenarios.json` | 10 escenarios con las actividades que cada uno exige asignar |
| `prompts/` | `common.md`, uno por agente, `arbiter.md` y plantillas de tarea por fase |
| `document_inventory.json`, `extracted/` | Inventario con SHA-256 y texto extraído de cada documento |
| `posthoc/reference_raci.json` | RACI del artículo. **Ningún agente la recibe** |
| `results/<label>/` | `raw_results.jsonl`, `decisions.csv`, `summary.csv`, `scenario_summary.csv`, `agent_changes.csv`, `evidence_usage.csv`, `posthoc_comparison.csv`, `final_report.md`, `experiment_config.json`, `prompt_samples/` |

## Control de contaminación

- Del artículo solo se tomaron hechos técnicos, normas y práctica internacional con localizador (`sources/external_sources.json`). Se excluyeron las reglas R1-R10, la matriz RACI, la Autoridad de Cambio, las atribuciones propuestas y toda frase de asignación.
- Quedan fuera del contexto de los agentes: la propuesta de procedimiento de DTE, ambos flujos, los resúmenes de correos, la guía RACI de `agente_junior`, la evaluación del artículo y `memory.md`. Son propuestas o posturas de las partes, no evidencia institucional.
- `build_corpus.py` y `experiment.py` buscan marcadores de la solución del artículo en todo el material preparado (system prompt, corpus, escenario y plantilla) antes de cada llamada y abortan si encuentran alguno. El texto generado por otros agentes en las fases 2 y 3 queda fuera de ese control.
- `experiment.py` no lee `posthoc/`. `analysis.py` carga la RACI de referencia solo al final.
- `prompt_samples/` guarda la primera petición completa de cada agente y fase para auditoría.

## Diseño

- **Unidad experimental:** la corrida, es decir, un escenario por una repetición. Cada corrida incluye 14 llamadas: 5 en la fase 1, 4 en la fase 2, 4 en la fase 2c (brazo control) y 1 del árbitro. Las decisiones de los agentes dentro de una corrida no son independientes, porque en la fase 2 cada uno ve a los demás, y no se tratan como réplicas.
- **Repeticiones:** 20 por escenario. Semilla `1000 + run_id`, la misma para todas las llamadas de la repetición.
- **Orden:** repetición externa y escenarios barajados con semilla dentro de cada repetición. Así, la deriva temporal del servicio no se confunde con el escenario. El orden de los agentes también se baraja en cada corrida.
- **Brazo control (fase 2c):** en cada corrida, los cuatro especializados reconsideran también su decisión inicial **sin** ver las propuestas ajenas, con una plantilla del mismo título y estructura. Es un diseño pareado dentro de la corrida: la diferencia de convergencia entre 2 y 2c separa el efecto de la información ajena del efecto de responder dos veces (regresión a la respuesta modal o complacencia del modelo). El árbitro solo evalúa la fase 2.
- **Cita textual verificable:** cada cita incluye un fragmento literal (`quote`) de la fuente. El script comprueba que exista, ignorando mayúsculas, puntuación y espacios. Esto hace objetiva la existencia del texto citado, no su pertinencia.
- **Anonimización:** en las fases 2 y 3, las propuestas se presentan como PROPUESTA A-D en orden aleatorio y sin campos de identidad. Los agentes tienen instrucción de no mencionar su perspectiva. La correspondencia entre etiqueta y agente se registra en `anonymization`.
- **Árbitro:** recibe `common.md` + `arbiter.md` y evalúa las propuestas finales de los cuatro especializados. El agente NEUTRAL no se incluye, para que siga siendo un control independiente.
- **Salida estructurada:** esquema JSON con listas cerradas de unidades y actividades. Los `source_id` son texto libre, para que la tasa de validez de las citas sea informativa. Además de las unidades del corpus, se admiten `PROPOSED_NEW_AUTHORITY` y `UNIDAD_NO_INCLUIDA_EN_CORPUS`.

## Plan de análisis (fijado antes del piloto)

- **Decisión principal:** conjunto de unidades A normalizado a departamento. Por ejemplo, GT/DAS1 pasa a DAS y DTE/ISC2 a ISC; los departamentos regionales de Transmisión se agrupan como TX_REG.
- **Acuerdo:** proporción de los 6 pares de especializados con igual decisión principal, promediada por actividad y escenario. **Consenso estricto:** los 4 coinciden.
- **CONVERGENCE_DELTA** = acuerdo después − acuerdo antes, con IC 95 % por bootstrap sobre corridas (2000 remuestreos).
- **POSITION_CHANGE_RATE:** proporción de decisiones cuyo A cambia de la fase 1 a la 2. También se informa la incoherencia entre la posición declarada (MAINTAIN/MODIFY) y el cambio real.
- **AMBIGUITY_RATE:** proporción de decisiones con `institutional_ambiguity`. En el árbitro, proporción de veredictos AMBIGUOUS.
- **DELIBERATION_EFFECT** = CONVERGENCE_DELTA − CONVERGENCE_DELTA_CONTROL, donde el control es el acuerdo en la fase 2c menos el de la fase 1. IC 95 % por bootstrap sobre las diferencias pareadas por corrida. **Es el estimador principal del efecto de la deliberación.** También se informa POSITION_CHANGE_RATE_CONTROL.
- **Entropía de A:** H = −Σ p log2 p sobre la distribución de A de los 4 especializados en las 20 repeticiones, por actividad, antes y después. Es descriptiva y no mide corrección.
- **Concordancia del neutral:** P(A neutral = A agente) en la fase 1.
- **Sesgo hacia la propia unidad:** P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL), en la fase 1.
- **EVIDENCE_VALIDITY_RATE:** citas cuyo `source_id` existe en el corpus sobre el total de citas.
- **QUOTE_VERIFIED_RATE:** citas cuyo fragmento literal existe en la fuente citada, en total y en afirmaciones DOCUMENTADO.
- **Tipo de afirmación:** la etiqueta que declara el agente (DOCUMENTADO, INFERIDO…) se registra, pero **no se usa como medida del respaldo**; el smoke test mostró que el modelo no la aplica bien (ver BITACORA.md). El respaldo se mide con la verificación textual, el juez ciego y la auditoría humana.
- **UNSUPPORTED_CLAIM_RATE:** decisiones con A o R sin ninguna cita válida. Se complementa con la tasa de A sin evidencia institucional válida y con la tasa de **violación de jerarquía**, es decir, afirmaciones DOCUMENTADO que citan una fuente no institucional.
- **Post hoc:** coincidencia del A con REFERENCE_RACI por actividad, en cuatro grupos: individual fase 1, neutral, post-debate y árbitro. La columna Origen de la referencia equivale a TX_REG, DT, DEL, DOS u OTHER; GT* equivale a DOS, DEL, DEN o DDR; AC equivale a PROPOSED_NEW_AUTHORITY. REFERENCE_RACI es una propuesta previa, no una verdad conocida.
- **Matriz RACI modal** (`modal_raci.md`, `modal_raci.csv`, `modal_raci_vs_reference.csv`): para cada grupo (especializados en la fase 1, neutral, deliberación, control y árbitro) y cada actividad, el rol modal de cada unidad, con su frecuencia. Rol por decisión: A/R > A > R > C > I > sin rol. Nivel principal: por actividad, acumulando escenarios; el desglose por escenario va en el CSV. Una celda es **inestable** si su rol modal no alcanza el 60 %. La comparación post hoc con REFERENCE_RACI se hace celda a celda en tres niveles: rol exacto, rol ejecutivo (A/R, A, R; C, I y sin rol como una misma clase) y A recuperada. La matriz modal describe lo que produce el modelo, no la asignación correcta.
- **Análisis exploratorio:** todo análisis adicional se informará por separado como exploratorio.

## Auditoría de pertinencia de citas (post hoc)

`EVIDENCE_VALIDITY_RATE` solo verifica que el identificador exista. La pertinencia se evalúa aparte con `citation_audit.py`, en tres capas:

1. **Control determinista** sobre todas las citas: DOCUMENTADO con fuente no institucional; numeral de una unidad que no figura en la asignación que sostiene.
2. **Juez LLM ciego** (`JUDGE_MODEL` en `config.py`, por defecto `gemini-3.1-pro-preview`, distinto del modelo evaluado). Evalúa una muestra aleatoria estratificada por tipo de afirmación. Recibe solo actividad, asignación, afirmación y texto literal de la fuente; no ve el agente ni REFERENCE_RACI. Clasifica SUPPORTS / PARTIAL / DOES_NOT_SUPPORT y si el tipo declarado es correcto.
3. **Auditoría humana**: dos codificadores independientes sobre una muestra de 100 citas, sin ver el agente. Se calculan el kappa entre codificadores y el kappa entre el juez y el consenso humano. Las tasas del juez solo se reportan si ese kappa es aceptable. La muestra humana siempre está incluida en la del juez.

```bash
python citation_audit.py extract --label pilot
python citation_audit.py sample  --label pilot --n 100     # audit_sheet_coder1.csv y coder2.csv
python citation_audit.py judge   --label pilot --n 600
python citation_audit.py report  --label pilot             # citation_audit_report.md
```

Los codificadores completan las dos últimas columnas de su planilla sin comunicarse. `audit_key.csv` vincula ítems y citas, y no se les entrega.

## Coste estimado del piloto

Cada llamada envía entre 19 000 y 28 000 tokens de entrada, casi todos del corpus. El smoke test v2 costó USD 0,13 por corrida con los precios provisionales, así que el piloto de 200 corridas (2800 llamadas) rondaría los USD 26, más reintentos, más unos USD 2-5 del juez sobre 600 citas. `analysis.py` calcula el coste real con los precios de `config.py`, que son **provisionales** y deben verificarse. El almacenamiento implícito en caché de Gemini puede reducir el coste de entrada; los tokens en caché se registran por separado.
# agents_deliberation
