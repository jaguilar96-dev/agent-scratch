### agent_framework

Tú: Soy CUS-1001, me cobraron dos veces en el supermercado, puedes registrar el reclamo
  → get_transactions(customer_id=CUS-1001, limit=10)
    resultado: {"result": [{"id": "TRX-3001", "date": "2026-10-20", "description": "SUPERMERCADO DEMO SAN ISIDRO", "amount": -186.4, "currency": "PEN", "card_id": "CRD-2001", 
  Agente [sensitive_action]: He encontrado dos cargos en SUPERMERCADO DEMO: TRX-3001 y TRX-3002 (ambos -186.40 PEN, 20/10/2026) con la misma tarjeta. Antes de registrar el reclamo debemos bloquear la tarjeta asociada. El bloqueo es definitivo y requiere su confirmación antes de ejecutarlo. ¿Confirma que proceda a bloquear la tarjeta de forma definitiva y luego registre el reclamo por cuál(s) movimiento(s): TRX-3001, TRX-3002 o ambos?
  (primer texto en 19776 ms, respuesta completa en 20064 ms, 3325 tokens de entrada, 1961 de salida)
Tú: ambos
  → block_card(card_id=CRD-2001, reason=fraude)
    NO SE EJECUTA, pendiente de aprobación: {"status": "pendiente_aprobacion", "action_id": "call-903b6b79", "detail": "Acción sensible: no se ejecutó ni se registró todavía. Dile al cliente que la pedist  
  → file_claim(customer_id=CUS-1001, transaction_id=TRX-3001, reason=Cobro duplicado en SUPERMERCADO DEMO SAN ISIDRO; me cobraron dos veces.)
  → file_claim(customer_id=CUS-1001, transaction_id=TRX-3002, reason=Cobro duplicado en SUPERMERCADO DEMO SAN ISIDRO; me cobraron dos veces.)
    error: {"error": "Ya hay una acción esperando la decisión del asesor: no se pide otra hasta que la decida."}
    error: {"error": "Ya hay una acción esperando la decisión del asesor: no se pide otra hasta que la decida."}
  Agente [sensitive_action]: He solicitado el bloqueo definitivo de su tarjeta; la solicitud está pendiente de revisión por un asesor. El bloqueo es irreversible. No pude registrar los reclamos aún porque solo puede haber una acción sensible en espera; en cuanto el asesor apruebe el bloqueo registraré los reclamos por ambos cargos duplicados y le informaré los códigos de reclamo y el plazo de respuesta.      
  (primer texto en 35225 ms, respuesta completa en 35242 ms, 6874 tokens de entrada, 3989 de salida)   
  Asesor: ¿apruebas block_card(card_id=CRD-2001, reason=fraude)? [s/n]: s
    resultado: {"id": "CRD-2001", "customer_id": "CUS-1001", "product": "Visa Clásica", "last4": "4417", "status": "blocked", "currency": "PEN"}
  Agente [sensitive_action]: La tarjeta Visa Clásica (CRD-2001, terminada en 4417) fue bloqueada.



INFO agent.infrastructure.llm.agent_framework_runtime: llm AgentFramework {'models': ['gpt-5-mini'], 'llm_calls': 3, 'latency_ms': 26872, 'prompt_tokens': 6294, 'completion_tokens': 3270}
INFO agent.application.chat_service: trayectoria 8ab4f253-feda-4295-a4cf-8d5b37606d2e: block_card pending_approval → file_claim error → file_claim error → respuesta sensitive_action
INFO agent.infrastructure.llm.agent_framework_runtime: llm AgentFramework {'models':['gpt-5-mini'], 'llm_calls': 1, 'latency_ms': 19499, 'prompt_tokens': 1709,'completion_tokens': 2546}


### react:

Tú: Soy CUS-1001, me cobraron dos veces en el supermercado
  → get_transactions(customer_id=CUS-1001, limit=10)
    resultado: {"result": [{"id": "TRX-3001", "date": "2026-10-20", "description": "SUPERMERCADO DEMO SAN ISIDRO", "amount": -186.4, "currency": "PEN", "card_id": "CRD-2001", 
  Agente [sensitive_action]: He encontrado dos cargos iguales en tus movimientos:
- TRX-3001: 2026-10-20, SUPERMERCADO DEMO SAN ISIDRO, -186.40 PEN (tarjeta CRD-2001)
- TRX-3002: 2026-10-20, SUPERMERCADO DEMO SAN ISIDRO, -186.40 PEN (tarjeta CRD-2001)
¿Confirmas que quieres que inicie un reclamo por cargos duplicados para TRX-3001 y TRX-3002 con el motivo “Me cobraron dos veces en el supermercado”? Si confirmas, registraré el/los reclamo(s) y quedarán pendientes de aprobación de un asesor.
  (primer texto en 15948 ms, respuesta completa en 17530 ms, 3725 tokens de entrada, 1619 de salida)
Tú: si por favor
  → file_claim(customer_id=CUS-1001, transaction_id=TRX-3001, reason=Me cobraron dos veces en el supermercado (cargo duplicado).)
    NO SE EJECUTA, pendiente de aprobación: {"status": "pendiente_aprobacion", "action_id": "call_OlBVlKztwxcVB2HYQ5kPFth8", "detail": "Acción sensible: no se ejecutó ni se registró todavía. Dile al clien
  → file_claim(customer_id=CUS-1001, transaction_id=TRX-3002, reason=Me cobraron dos veces en el supermercado (cargo duplicado).)
    error: {"error": "Ya hay una acción esperando la decisión del asesor: no se pide otra hasta que la decida."}
  Agente [sensitive_action]: He solicitado el reclamo por TRX-3001 con motivo “Me cobraron dos veces en el supermercado”. La solicitud quedó pendiente de aprobación por un asesor; te avisaremos cuando la revisen. No pude registrar TRX-3002 porque ya hay una acción pendiente de decisión (solo puede haber una a la vez). ¿Deseas que espere la resolución para luego registrar el segundo reclamo, o prefieres que cancele este pendiente para intentar registrar ambos ahora?
  (primer texto en 22247 ms, respuesta completa en 22558 ms, 5275 tokens de entrada, 2376 de salida)
  Asesor: ¿apruebas file_claim(customer_id=CUS-1001, transaction_id=TRX-3001, reason=Me cobraron dos veces en el supermercado (cargo duplicado).)? [s/n]: n
    rechazada por el asesor: {"status": "rechazada", "detail": "El asesor rechazó la acción: no se ejecutó."}
  Agente [sensitive_action]: El asesor rechazó la acción; no se ejecutó.


INFO agent.infrastructure.llm.foundry_chat_model: llm ToolRequest {'models': ['gpt-5-mini-2025-08-07'], 'llm_calls': 1, 'latency_ms': 4801, 'prompt_tokens': 2223, 'completion_tokens': 495}
INFO agent.infrastructure.llm.foundry_chat_model: llm AgentReply {'models': ['gpt-5-mini-2025-08-07'], 'llm_calls': 1, 'latency_ms': 10734, 'prompt_tokens': 2437, 'completion_tokens': 1273}
INFO agent.application.chat_service: trayectoria 4b30a7c1-87ee-45f9-84ad-bcfc9cde81ff: file_claim pending_approval → file_claim error → respuesta sensitive_action
INFO agent.application.chat_service: trayectoria 4b30a7c1-87ee-45f9-84ad-bcfc9cde81ff: decisión del asesor → file_claim rejected
INFO agent.infrastructure.llm.foundry_chat_model: llm AgentReply {'models': ['gpt-5-mini-2025-08-07'], 'llm_calls': 1, 'latency_ms': 7966, 'prompt_tokens': 1703, 'completion_tokens': 869}


### error de negocio:
Tú: Soy CUS-9999, ¿qué comisiones me cobraron?
  → get_transactions(customer_id=CUS-9999, limit=50)
    error: {"error": "El cliente CUS-9999 no existe"}
  Agente [data_query]: No encuentro ese código de cliente en el sistema. Confirma por favor tu código de cliente correcto (sin enviar números de tarjeta ni claves) o dime si prefieres que te indique cómo ver las comisiones desde la app/estado de cuenta. Cuando me confirmes el código correcto, consulto tus movimientos y te indico las comisiones.
  (primer texto en 14317 ms, respuesta completa en 14470 ms, 3652 tokens de entrada, 892 de salida)

INFO agent.infrastructure.llm.agent_framework_runtime: llm AgentFramework {'models': ['gpt-5-mini'], 'llm_calls': 2, 'latency_ms': 10510, 'prompt_tokens': 3652, 'completion_tokens': 892}
INFO agent.application.chat_service: trayectoria 2451dade-79d3-47fe-bb6b-fd19bd9842f2: get_transactions error → respuesta data_query


## Sesión 8 — Aprobación humana, validación y reintentos

Dominio: `fraud` (paso 6).

| Caso | Runtime | Mensaje | Qué pasó | Resultado o ID |
|---|---|---|---|---|
| Aprobar | `agent_framework` | - Usuario: *"Soy CUS-1001, me cobraron dos veces en el supermercado, puedes registrar el reclamo"*<br>- Confirmación: *"ambos"*<br>- Asesor: *"s"* | El agente consultó `get_transactions`, detectó los cobros duplicados TRX-3001 y TRX-3002 en CRD-2001 y solicitó confirmación advirtiendo que el bloqueo es definitivo. Al recibir "ambos", invocó la tool sensible `block_card`, la cual quedó detenida en `pendiente_aprobacion`. Al intentar registrar simultáneamente `file_claim`, se bloqueó por regla de negocio (máximo una acción sensible esperando). El asesor aprobó la acción (`s`) y recién ahí se ejecutó el bloqueo en el sistema. | `action_id: call-903b6b79`<br>Resultado: `{"id": "CRD-2001", "customer_id": "CUS-1001", "product": "Visa Clásica", "last4": "4417", "status": "blocked", "currency": "PEN"}` |
| Rechazar | `react` | - Usuario: *"Soy CUS-1001, me cobraron dos veces en el supermercado"*<br>- Confirmación: *"si por favor"*<br>- Asesor: *"n"* | El agente consultó movimientos, detectó los dos cargos y preguntó si confirmaba iniciar reclamo. Ante el "si por favor", intentó registrar `file_claim` para TRX-3001, quedando en `pendiente_aprobacion`. El intento inmediato de registrar TRX-3002 falló por ya existir una acción en espera. El asesor rechazó la acción (`n`), impidiendo su ejecución en el backend y notificando al cliente del rechazo. | `action_id: call_OlBVlKztwxcVB2HYQ5kPFth8`<br>Resultado: `{"status": "rechazada", "detail": "El asesor rechazó la acción: no se ejecutó."}` |
| Error de negocio (`CUS-9999`) | `agent_framework` | *"Soy CUS-9999, ¿qué comisiones me cobraron?"* | El agente ejecutó `get_transactions(customer_id="CUS-9999", limit=50)`. El servicio retornó un error de negocio: `{"error": "El cliente CUS-9999 no existe"}`. El modelo manejó el error dentro del diálogo sin abortar, solicitándole al cliente confirmar su código correcto de forma segura. | Error controlado: `{"error": "El cliente CUS-9999 no existe"}`<br>Intención: `data_query` |
| Input inválido | `agent_framework` / `react` | Invocaciones concurrentes de `file_claim` mientras `block_card` o `file_claim` estaban pendientes de asesor | El agente intentó solicitar una o dos acciones sensibles adicionales (`file_claim` para TRX-3001 y TRX-3002) teniendo ya una acción en cola. La capa de aplicación (`ChatService._run`) validó las precondiciones y rechazó las llamadas antes de enviarlas al MCP, devolviendo un error tipado para que el LLM informe al usuario sin romper el flujo. | Error de validación: `{"error": "Ya hay una acción esperando la decisión del asesor: no se pide otra hasta que la decida."}` |

### La trayectoria en el log

```text
INFO agent.application.chat_service: trayectoria 8ab4f253-feda-4295-a4cf-8d5b37606d2e: block_card pending_approval → file_claim error → file_claim error → respuesta sensitive_action
INFO agent.application.chat_service: trayectoria 4b30a7c1-87ee-45f9-84ad-bcfc9cde81ff: file_claim pending_approval → file_claim error → respuesta sensitive_action
INFO agent.application.chat_service: trayectoria 4b30a7c1-87ee-45f9-84ad-bcfc9cde81ff: decisión del asesor → file_claim rejected
INFO agent.application.chat_service: trayectoria 2451dade-79d3-47fe-bb6b-fd19bd9842f2: get_transactions error → respuesta data_query
```

### ¿Algo se ejecutó sin que lo aprobaras?

**No, ninguna acción sensible fue ejecutada sin aprobación explícita.**

1. En el flujo con `agent_framework`, `block_card(card_id="CRD-2001", reason="fraude")` se detuvo de inmediato en estado `NO SE EJECUTA, pendiente de aprobación` (`call-903b6b79`). La tarjeta solo cambió a estado `blocked` luego de ingresar `s` en la consola de asesor.
2. En el flujo con `react`, `file_claim` se detuvo en estado `pendiente_aprobacion` (`call_OlBVlKztwxcVB2HYQ5kPFth8`). Al ingresar `n`, fue marcada como rechazada (`rejected`) y nunca se ejecutó en el sistema.
3. Las llamadas paralelas adicionales a `file_claim` fueron bloqueadas por el guardrail de la aplicación ("solo una acción pendiente a la vez").
4. Las únicas herramientas que se ejecutaron sin intervención humana fueron las de consulta de solo lectura (`get_transactions`), las cuales tienen el flag `sensitive=False`.

### Conclusión

1. **Garantía Human-in-the-Loop (HITL):** El desacoplamiento entre la solicitud de la herramienta por parte del modelo y la ejecución real en `ChatService` previene eficazmente cualquier mutación o efecto secundario sensible en el sistema sin la autorización expresa del asesor humano.
2. **Resiliencia ante errores de negocio e inputs inválidos:** Tanto los errores del backend (por ejemplo, cliente inexistente `CUS-9999`) como las violaciones de invariantes operativas (como solicitar dos acciones sensibles a la vez) son capturados y devueltos limpiamente como contexto de la tool. El modelo se recupera sin romperse y ofrece una respuesta guiada y clara al cliente.
3. **Consistencia entre runtimes:** Tanto `agent_framework` como `react` respetan uniformemente los mismos puertos, interceptores de seguridad, memoria de trabajo de herramientas y límites de turnos.
4. **Trazabilidad completa:** La emisión de líneas estructuradas de `trayectoria` en el log permite auditar con precisión la secuencia de eventos (`pending_approval`, `error`, `rejected`, `ok`) para observabilidad, análisis forense y cumplimiento regulatorio bancario.

------------------------------------------------------------------------------------
## Sesión 9 — Despliegue en Azure

Equipo: `team-03`. Dominio: `fraud`.

| Comprobación | Resultado |
|---|---|
| Tests en el contenedor (paso 3) | `docker run --rm agent:test` → `139 passed, 5 skipped in 10.07s` (los 5 skipped son los golden sets de otros dominios; en mi máquina `uv run pytest` pasó con 140 passed, 4 skipped). |
| Acción aprobada después de reiniciar `uvicorn` (paso 2, Cosmos DB) | Sí, funcionó al toque. Dejé `file_claim` colgado en `NO SE EJECUTA`, maté uvicorn sin piedad, lo volví a levantar y al mandarle `s` aprobó como si nada con `CLM-9001`. Cosmos DB (`workshop/team-03`) guardó la sesión sin perder nada. |
| Imagen desplegada (`team-NN/agent:<sha>`) | `acrworkshopjsu3.azurecr.io/team-03/agent:bb682483ed0b1c7e929a1f3b731cb8e1c0cfaa6f` (repo `team-03/agent:bb682483ed0b1c7e929a1f3b731cb8e1c0cfaa6f`). |
| Revisión activa y duración del job `deploy` | Revisión `ca-agent-chat-03--0000003` en Running (réplica `ca-agent-chat-03--0000003-767f558ccf-p54z2`). En GitHub Actions: job `test` tardó 37s y el `deploy` 2m 9s. |
| `/health` del agente desplegado | `Agente en https://ca-agent-chat-03.icybush-2ea2dfc1.eastus2.azurecontainerapps.io: ok` (200 OK cantado en los logs: `"GET /health HTTP/1.1" 200 OK`). |
| Respuesta con `Fuentes:` contra Azure (y su tiempo en ms) | Le pregunté *"¿Cuál es el plazo para presentar un reclamo?"* y me tiró los 60 días para fraude / 1 año para comisiones, citando `claims-regulation.pdf` [3.1] y `fraud-and-claims-faq.md`. Primer texto en 6117 ms y respuesta completa en 6280 ms (1610 tokens in / 457 out). |
| Acción aprobada contra Azure, con su `resultado:` | Corrí el flujo en Azure: consultó `get_transactions`, pidió registrar reclamo para TRX-3002, se frenó en `NO SE EJECUTA, pendiente de aprobación`, le metí `s` de asesor y soltó `resultado: {"id": "CLM-9001", "customer_id": "CUS-1001", "transaction_id": "TRX-3002", "reason": "Cargo duplicado en supermercado, solicito reclamo por TRX-3002", "status": "registered"}`. |

### Qué pone Azure y qué pone la imagen

**Azure (vía Terraform en la Container App):**
`APPLICATIONINSIGHTS_CONNECTION_STRING`, `AZURE_CLIENT_ID`, `AZURE_OPENAI_ENDPOINT`, `COSMOS_CONTAINER`, `COSMOS_DATABASE`, `COSMOS_ENDPOINT`, `FOUNDRY_PROJECT_ENDPOINT`, `KEY_VAULT_URI`, `MCP_SCOPE`, `MCP_URL`, `SEARCH_ENDPOINT`, `SEARCH_INDEX`, `TEAM_ID`.
Cero contraseñas o api keys en texto plano; son puros endpoints, nombres de recursos y la Managed Identity para que Azure se entienda solo.

**La imagen (`runtime`):**
Ya viene cocinada con lo que no cambia: `DOMAIN` (fraud), `FOUNDRY_AUTH_PROVIDER` (entra_id), `KNOWLEDGE_BASE` (azure_search), `AGENT_RUNTIME` (agent_framework), `PYTHONUNBUFFERED=1` y `PATH`.

En los logs de arranque del contenedor se ve clarito cómo levanta todo de una:
- `agent.infrastructure.bootstrap: Telemetría: App Insights del equipo`
- `agent.infrastructure.bootstrap: Foundry auth provider: entra_id`
- `agent.infrastructure.bootstrap: Knowledge base: azure_search · https://srch-workshop-jsu3.search.windows.net (índice idx-team-03) · 57 chunks`
- `agent.infrastructure.bootstrap: Conversation store: Cosmos DB workshop/team-03`
- `agent.infrastructure.bootstrap: MCP: https://ca-mcp-server.icybush-2ea2dfc1.eastus2.azurecontainerapps.io/mcp · 4 tools: get_transactions, get_claim_status, block_card, file_claim`
- `agent.infrastructure.bootstrap: Agent runtime: agent_framework`
- `Uvicorn running on http://0.0.0.0:8000`

### Problemas que encontraste y cómo los resolviste

- **Timeout en el primer `/health` (cold start):** Al probar contra Azure por primera vez se quedó pensando y dio timeout. No toqué nada de código: era solo el contenedor despertándose del frío. Esperé unos segundos, volví a tirar la petición y ya respondió en 200 ms.
- **Error 401 en la consola:** Al correr `dev/chat.py` contra Azure me rebotó de una con 401. Me faltaba setear la variable `AGENT_SCOPE` en el entorno. Le puse el scope de la ficha, corrí `az login` para refrescar mi token de Entra ID y pasó directo.
- **Reiniciar el server no pierde la sesión:** En las sesiones anteriores si reiniciaba `uvicorn` se borraba la acción pendiente de memoria y moría en 404. Ahora con Cosmos DB (`workshop/team-03`) puedo matar el proceso, ir por un café, volver a prenderlo y el asesor aprueba sin broncas.

### Conclusión

- Lo mejor de este despliegue es no tener que renegar con secretos ni rotar API keys. Con Managed Identity y OIDC en GitHub Actions todo se conecta solo sin meter credenciales en variables de entorno.
- En Azure corre exactamente igual que en local. No hubo sorpresas raras de dependencias y el RAG con búsqueda híbrida responde bastante rápido (~6s trayendo fuentes reales de la normativa).
- Cosmos DB resuelve de verdad el dolor de cabeza del human-in-the-loop: el contenedor puede reiniciarse o escalar y la conversación sigue viva. Menos cosas de qué preocuparse en producción.

------------------------------------------------------------------------------------

## Sesión 10 — Trazas por turno y dashboard

Equipo: `team-03`. App Insights: `appi-team-03`. Los cuatro casos contra el agente desplegado (paso 8).

| Caso | `operation_Id` | Latencia (ms) | Tokens de entrada | Tokens de salida | Tools | Error | Observaciones |
|---|---|---|---|---|---|---|---|
| Saludo | `acd721545a98cf77931881815abfe8b3` | 10379 | 1512 | 132 | — | — | Sin tools; latencia de 10.4s (4921 ms en LLM gpt-5-mini, primer token en 8.4s) |
| Consulta con retrieval | `8ab830c0abc0d5b032b10b8683e0a54a` | 14529 | 1570 | 746 | — | — | Retrieval con embeddings (4 fuentes); 8130 ms en LLM gpt-5-mini, primer token en 11.6s |
| Llamada a tool | `65753a3f9c11a8c61128a902c58e658f` | 25245 | 3651 | 1540 | get_transactions | — | 2 llamadas a LLM (16.9s) + get_transactions vía MCP (2.9s); primer token en 22.0s |
| Error controlado | `1fe9b9ad6db0b8a0dd0d2cab679cb900` | 60 | — | — | — | 404 Not Found | Acción inexistente rechazada (POST /chat/actions falla con not_found) |

En **Observaciones**, una línea: lo que llamó la atención de la traza (qué se llevó el tiempo, la dependencia que falló, si el
error permite ubicar el turno). En **Tools**, `—` si el turno no llamó ninguna.

### Lo que dice el workbook

| Panel | Lo que viste |
|---|---|
| Latencia p95 por intención | `data_query` es la más lenta con p95 de 41.7s, seguida de `sensitive_action` (25.2s). Hasta un simple `greeting` se demora 10.3s. |
| Tokens por turno | Se fueron ~16.6k tokens de entrada y ~5.6k de salida en 7 turnos. El context/system prompt infla la entrada en cada interacción. |
| Dónde se va el tiempo de un turno | Casi todo se lo traga `Foundry - chat` (70.3s total, ~11.4s p95). Cosmos DB suma 21.1s porque mete 53 llamadas, y el MCP se lleva 19.7s. |
| Tools con error | 1 fallo en `chat.decision` con `not_found` (la prueba del action_id inventado). En MCP hubo 1 error controlado en `get_transactions`. |

### ¿Qué optimizarías primero y por qué?

Las llamadas a `Foundry - chat` y los viajes a Cosmos DB. 10 segundos para responder un "hola" es lentísimo; se necesita recortar el system prompt o revisar la latencia del deployment. Y meter 53 llamadas a Cosmos para solo 7 turnos es demasiado: metería una caché en memoria para no pegarle a la BD en cada paso intermedio.

### Conclusión

El agente resuelve bien el flujo, las tools y los errores controlados sin caerse, pero está bastante pesado de latencia. Si se optimizan las consultas a Cosmos y se aligera el prompt para que el LLM responda más rápido, queda listo.
