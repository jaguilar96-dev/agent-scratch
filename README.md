# agent-scratch

Agente conversacional bancario del **Banco Demo** (ficticio), construido paso a paso en el Workshop IA Engineers.
Cada equipo lo adapta a su dominio y lo hace crecer sesión a sesión hasta la v1.0.

## Objetivo

Un agente que atiende a los clientes del banco por consola y por API:

- **Conversa (T1):** entiende la intención del cliente y responde con un contrato tipado, con memoria por sesión.
- **Sabe (T2):** responde con el conocimiento del banco (RAG sobre el corpus de su dominio) y cita sus fuentes.
- **Actúa (T3):** consulta datos con tools MCP y ejecuta la acción sensible de su dominio solo con aprobación humana.
- **Opera (T4):** desplegado en Azure, observable, evaluado y protegido.

Dominios: `fraud`, `fees`, `cards`, `loans` y `support` (variable `DOMAIN`).

## En qué va

| Versión | Qué hace el agente | Estado |
|---|---|---|
| `main` | arquetipo: capas, contratos y `TODO` por sesión | ✅ |
| `t1-s1` | `/chat` con respuesta tipada contra el mock de Foundry | ⏳ |
| `t1-s2` = `t1-v0.1` | historial por sesión, errores tipados, consumo por turno y Entra ID | ⏳ |
| `t2-s3` | ingesta del corpus del dominio e índice local | ⏳ |
| `t2-s4` | retrieval híbrido y RAG con citas en `/chat` | ⏳ |
| `t2-s5` = `t2-v0.2` | evaluación del RAG y Azure AI Search | ⏳ |
| `t3-*` → `t3-v0.3` | tools MCP, memoria y aprobación humana | ⏳ |
| `t4-*` → `t4-v0.4` | despliegue, trazas, evaluaciones y guardrails | ⏳ |
| `v1.0` | integración final | ⏳ |

Esta copia está en `main` (el arquetipo de partida). Para saber en qué versión está la tuya: `git describe --tags`.

## Requisitos

| Herramienta | Desde |
|---|---|
| Python 3.12, [uv](https://docs.astral.sh/uv/) y Git | la sesión 1 |
| Azure CLI y acceso a Microsoft Foundry (`gpt-5-mini`, `text-embedding-3-small`) | la sesión 2 |
| Azure AI Search | la sesión 5 |
| Docker | el tema 4 |

## Levantarlo

```bash
copy .env.example .env
uv sync
uv run pytest
uv run python dev/mock_foundry.py
uv run uvicorn agent.infrastructure.bootstrap:create_app --factory
uv run python dev/chat.py
```

El mock de Foundry, el agente y el chat corren cada uno en su propia terminal. `.env.example` apunta al mock, así que no hace falta Azure.

El paso a paso de cada sesión (configuración, ejecución, pruebas y problemas frecuentes) está en el repo de labs del workshop.

## Arquitectura

```
src/agent/
├── domain/          contratos y puertos; no importa nada externo
├── application/     casos de uso; solo conocen los puertos
└── infrastructure/  API, Foundry, búsqueda, persistencia, configuración y bootstrap
dev/                 herramientas locales: mock de Foundry y cliente de consola
devops/              contenedor y compose
```

Las dependencias van `infrastructure → application → domain`, nunca al revés.



Conversación con el agente. Escribe "nueva" para otra sesión o "salir" para terminar.
Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Depende del tipo de reclamo: para una operación no reconocida tiene hasta 60 días calendario desde la fecha de la operación; para reclamos por cobros de comisiones o intereses el plazo es de 1 año desde el cobro.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
  (primer texto en 10546 ms, respuesta completa en 10716 ms, 932 tokens de entrada, 459 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: Si se trata de fraude (operación no reconocida), tienes hasta 60 días calendario desde la fecha de la operación para presentar el reclamo. El banco responde en un máximo de 10 días hábiles para operaciones no reconocidas con tarjeta; si el caso depende de un comercio del exterior, el plazo puede ampliarse una vez por 15 días hábiles.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿En cuánto tiempo me responden?
  (primer texto en 14287 ms, respuesta completa en 14546 ms, 1234 tokens de entrada, 1315 de salida)  
Tú: ¿Qué es un contracargo?
  Agente [product_question]: Un contracargo es la devolución de una compra con tarjeta que el banco gestiona ante la marca de la tarjeta, cuando el comercio no entregó el producto, cobró un monto distinto o la operación no fue autorizada por el titular.
  Fuentes:
   [1] credit-card-chargebacks.html · Contracargos con tarjeta de crédito > Qué es un contracargo     
  (primer texto en 9430 ms, respuesta completa en 9595 ms, 1477 tokens de entrada, 813 de salida)     
Tú: ¿Qué decía la política de bloqueo de 2022?
  Agente [product_question]: La política indicaba, en resumen: confirmación obligatoria antes de ejecutar un bloqueo definitivo; existencia de bloqueo temporal (se activa/desactiva desde la app) y bloqueo definitivo (no reversible, requiere reposición y se aplica por robo, clonación o fraude confirmado); canales disponibles (app, línea telefónica 24h y agencias); el titular no asume operaciones realizadas después del reporte; las operaciones anteriores se evalúan mediante reclamo; la tarjeta se bloquea de inmediato ante reporte de robo, pérdida, clonación u operación no reconocida, y el banco puede bloquear preventivamente contactando al titular.
  Fuentes:
   [1] card-blocking-policy.docx · Política de bloqueo de tarjetas > Confirmación obligatoria
   [2] card-blocking-policy.docx · Política de bloqueo de tarjetas > Tipos de bloqueo
   [3] card-blocking-policy.docx · Política de bloqueo de tarjetas > Canales de bloqueo
   [4] card-blocking-policy.docx · Política de bloqueo de tarjetas > Responsabilidad por operaciones  
   [5] card-blocking-policy.docx · Política de bloqueo de tarjetas > Cuándo se bloquea una tarjeta    
  (primer texto en 11667 ms, respuesta completa en 11992 ms, 1506 tokens de entrada, 1083 de salida)  
Tú: ¿A cuánto está el dólar hoy?
  Agente [out_of_scope]: Esa consulta está fuera del ámbito de fraude, bloqueo y reclamos del Banco Demo. No puedo dar la cotización del dólar. Consulta la web o la app del banco, el portal del BCRP o tu casa de cambio para la tasa del día.
  (primer texto en 6776 ms, respuesta completa en 6941 ms, 1773 tokens de entrada, 552 de salida) 