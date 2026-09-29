"""Configuración única del experimento. Modificar aquí, no en la lógica.

Cambiar MODEL permite repetir el experimento con otro modelo (robustez)
sin tocar experiment.py ni analysis.py.
"""

# Modelo: el mismo para todos los agentes y el árbitro.
MODEL = "gemini-3.1-flash-lite"
THINKING_LEVEL = "medium"          # minimal | low | medium | high

# Parámetros de generación. TEMPERATURE = None deja el valor por defecto del
# modelo (recomendado por Google para la familia Gemini 3). Se registra igual.
TEMPERATURE = None
MAX_OUTPUT_TOKENS = 16384

# Repeticiones del piloto. Semilla de cada repetición: SEED_BASE + run_id.
N_REPETITIONS = 20
SEED_BASE = 1000

# Reintentos. Todos los intentos se registran en raw_results.jsonl.
MAX_ATTEMPTS = 3          # respuestas con JSON inválido o actividades incompletas
MAX_API_ATTEMPTS = 8      # errores transitorios del servicio (503, 429, 500)
MAX_BACKOFF_S = 120       # espera máxima entre reintentos por error de API

# Precios en USD por millón de tokens. VERIFICAR en la página oficial de
# precios de Gemini API antes de reportar costes; son valores provisionales.
INPUT_PRICE_PER_MILLION = 0.25
OUTPUT_PRICE_PER_MILLION = 1.50      # incluye tokens de razonamiento (thoughts)
CACHED_INPUT_PRICE_PER_MILLION = 0.025

# Precios por modelo (USD por millón): entrada, salida (incluye razonamiento), entrada en caché,
# escritura en caché. El coste de cada llamada se calcula con el modelo que la hizo, de modo que
# las ejecuciones con Gemini conservan sus cifras. gpt-6-luna verificado el 27/09/2026 en
# https://developers.openai.com/api/docs/models/gpt-6-luna (tarifa Standard, prompts < 272K).
PRICES = {
    "gemini-3.1-flash-lite": {"input": INPUT_PRICE_PER_MILLION, "output": OUTPUT_PRICE_PER_MILLION,
                              "cached_input": CACHED_INPUT_PRICE_PER_MILLION, "cache_write": INPUT_PRICE_PER_MILLION},
    "gpt-6-luna": {"input": 0.10, "output": 0.50, "cached_input": 0.01, "cache_write": 0.125},
}


def prices_for(model):
    return PRICES.get(model, PRICES["gemini-3.1-flash-lite"])


# Modelos de OpenAI (réplica con otra familia). REASONING_EFFORT equivale al nivel medio de Gemini.
# La API Responses no admite semilla; temperature y top_p no se envían (valores por defecto),
# igual que con Gemini.
OPENAI_MODELS = {"gpt-6-luna"}
OPENAI_REASONING_EFFORT = "medium"
# Nivel de servicio: "flex" cuesta el 50 % de Standard (mismo modelo, mayor latencia); None = Standard.
OPENAI_SERVICE_TIER = "flex"
SERVICE_TIER_FACTOR = {"flex": 0.5, "batch": 0.5}

# Tope de gasto: no se inician corridas nuevas al superar este coste estimado (precios de arriba).
# Crédito disponible: USD 38; se reserva margen para el juez de citas.
MAX_BUDGET_USD = 30.0

# Juez de pertinencia de citas (citation_audit.py). Modelo distinto del evaluado para
# reducir el sesgo de autoevaluación. Solo se usa en el análisis post hoc.
JUDGE_MODEL = "gemini-3.1-pro-preview"
JUDGE_THINKING_LEVEL = "low"

# Agentes especializados (deliberan) y control neutral (no delibera).
SPECIALIZED_AGENTS = ["DAS", "ISC", "MCO", "ODC"]
CONTROL_AGENT = "NEUTRAL"
