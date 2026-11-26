# S4
## En local
Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Tiene hasta 60 días calendario desde la fecha de la operación para reclamar una operación no reconocida. Para reclamos por cobros de comisiones o intereses, el plazo es de 1 año desde el cobro.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
  (primer texto en 8076 ms, respuesta completa en 8280 ms, 932 tokens de entrada, 325 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: Si es por fraude (operación no reconocida): tiene hasta 60 días calendario desde la fecha de la operación para presentar el reclamo. El banco responde todo reclamo en un máximo de 15 días hábiles; las operaciones no reconocidas con tarjeta se resuelven en un máximo de 10 días hábiles.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿En cuánto tiempo me responden?
   [3] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta
  (primer texto en 13576 ms, respuesta completa en 13841 ms, 1194 tokens de entrada, 1323 de salida)
Tú: ¿Qué es un contracargo?
  Agente [product_question]: No hay una definición de “contracargo” en los fragmentos proporcionados.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta
   [3] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿Cuánto tiempo tengo para reclamar un cargo?
   [4] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿En cuánto tiempo me responden?
   [5] response-times.csv · response-times
  (primer texto en 14322 ms, respuesta completa en 14454 ms, 1449 tokens de entrada, 1372 de salida)
Tú: ¿Qué decía la política de bloqueo de 2022?
  Agente [product_question]: La política indicaba que el titular no asume las operaciones no reconocidas realizadas después del reporte de bloqueo. Las operaciones realizadas antes del reporte se evalúan según el reglamento de atención de reclamos.
  Fuentes:
   [1] card-blocking-policy.docx · Política de bloqueo de tarjetas > Responsabilidad por operaciones
  (primer texto en 10430 ms, respuesta completa en 10606 ms, 1532 tokens de entrada, 1061 de salida)
Tú: ¿A cuánto está el dólar hoy?
  Agente [out_of_scope]: Lo siento, eso está fuera de mi área. No puedo proporcionar cotizaciones del dólar. Consulta la página web o la app del banco, o fuentes oficiales como el Banco Central (BCR) para la cotización del día.
  (primer texto en 7140 ms, respuesta completa en 7370 ms, 1515 tokens de entrada, 609 de salida)

## Comparacion
### SEARCH_TOP_K = 2
(agent) PS D:\github\agent-scratch> uv run python dev/chat.py                                         
Conversación con el agente. Escribe "nueva" para otra sesión o "salir" para terminar.
Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Tiene hasta 60 días calendario desde la fecha de la operación para reclamar una operación no reconocida. Para reclamos por cobros de comisiones o intereses, el plazo es de 1 año desde el cobro. Si el reclamo es por un cobro duplicado del propio banco, el plazo no se amplía. Si no entrega la información mínima, el plazo se suspende hasta que la complete por un máximo de 5 días hábiles; pasado ese plazo el reclamo se archiva y puede presentarlo nuevamente.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 4. Plazos de respuesta > 4.2 Excepciones
  (primer texto en 11322 ms, respuesta completa en 11612 ms, 690 tokens de entrada, 647 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: Para casos de fraude (operación no reconocida) tiene hasta 60 días calendario desde la fecha de la operación para presentar el reclamo.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿Cuánto tiempo tengo para reclamar un cargo?
  (primer texto en 11729 ms, respuesta completa en 11875 ms, 1047 tokens de entrada, 985 de salida)

### SEARCH_TOP_K = 10
Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Para operaciones no reconocidas tienes hasta 60 días calendario desde la fecha de la operación para presentar el reclamo. Para reclamos por cobros de comisiones o intereses, el plazo es de 1 año desde el cobro.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
  (primer texto en 11677 ms, respuesta completa en 11841 ms, 1372 tokens de entrada, 456 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: El cliente tiene hasta 60 días calendario, contados desde la fecha de la operación, para reclamar una operación no reconocida (fraude).
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿Cuánto tiempo tengo para reclamar un cargo?
  (primer texto en 11964 ms, respuesta completa en 12101 ms, 1763 tokens de entrada, 1160 de salida)

## Contra AI Search
  Tú: ¿Cuál es el plazo para presentar un reclamo?
  Agente [product_question]: Tienes hasta 60 días calendario, contados desde la fecha de la operación, para presentar un reclamo por una operación no reconocida. Para reclamos sobre cobros de comisiones o intereses, el plazo es de 1 año desde el cobro.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿Cuánto tiempo tengo para reclamar un cargo?
  (primer texto en 8863 ms, respuesta completa en 9024 ms, 915 tokens de entrada, 400 de salida)
Tú: ¿y si es por fraude?
  Agente [product_question]: Si es por fraude (operación no reconocida) tienes hasta 60 días calendario desde la fecha de la operación para presentar el reclamo. El banco responde en un plazo máximo de 10 días hábiles para operaciones no reconocidas con tarjeta; ese plazo puede ampliarse una vez por 15 días hábiles si depende de la marca o del comercio.
  Fuentes:
   [1] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo > 3.1 Plazo para presentar
   [2] fraud-and-claims-faq.md · Preguntas frecuentes: fraude y reclamos > ¿Me robaron la tarjeta, qué hago primero? > ¿En cuánto tiempo me responden?
   [3] response-times.csv · response-times
  (primer texto en 13066 ms, respuesta completa en 13240 ms, 1289 tokens de entrada, 1390 de salida)
Tú: ¿Qué es un contracargo?
  Agente [product_question]: Un contracargo es la devolución de una compra con tarjeta que el banco gestiona ante la marca de la tarjeta cuando el comercio no entregó el producto, cobró un monto distinto o la operación no fue autorizada por el titular.
  Fuentes:
   [1] credit-card-chargebacks.html · Contracargos con tarjeta de crédito > Qué es un contracargo
  (primer texto en 13376 ms, respuesta completa en 13524 ms, 1533 tokens de entrada, 1204 de salida)
Tú: ¿Qué decía la política de bloqueo de 2022?
  Agente [product_question]: No encontré la “política de bloqueo de 2022” en los fragmentos proporcionados. Si quieres, indica qué aspecto te interesa (bloqueo preventivo, plazos, requisitos) o sube el documento y lo reviso.
  (primer texto en 11913 ms, respuesta completa en 12120 ms, 1778 tokens de entrada, 1152 de salida)
Tú: ¿A cuánto está el dólar hoy?
  Agente [out_of_scope]: No puedo proporcionar cotizaciones en tiempo real. Para conocer el tipo de cambio hoy, revisa la web o la app del Banco Demo, la página del Banco Central de Reserva del Perú o consulta una casa de cambio autorizada.
  (primer texto en 7840 ms, respuesta completa en 7999 ms, 1687 tokens de entrada, 610 de salida) 

# S5
## Línea base (S5)
Resumen de 30 casos (juez local):
  recall@5: 1.00   intención: 0.93   fuentes: 0.97   hechos: 0.93
  apoyo: 5.0/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 1
  tokens: 28589 de entrada, 15210 de salida
Detalle de cada caso: D:\github\agent-scratch\data\eval\fraud-20261110-103547.json

## Línea base + 3 preguntas
Resumen de 33 casos (juez local):
  recall@5: 0.97   intención: 1.00   fuentes: 0.94   hechos: 0.80
  apoyo: 5.0/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 1
  tokens: 31144 de entrada, 18452 de salida
Detalle de cada caso: D:\github\agent-scratch\data\eval\fraud-20261110-105557.json

## Resultado del juez
Resumen de 33 casos (juez azure_evaluation):
  recall@5: 0.97   intención: 1.00   fuentes: 0.94   hechos: 0.83
  apoyo: 4.9/5   relevancia: 5.0/5   cita correcta: 1.0
  fugas de datos personales: 0   citas de fuentes prohibidas: 1
  tokens: 31191 de entrada, 17916 de salida
Detalle de cada caso: D:\github\agent-scratch\data\eval\fraud-20261113-085356.json

# S6
## Sesión 6 — Tools del MCP en el chat

Dominio: `fraud`. MCP: el mock (`http://127.0.0.1:8200/mcp`) y, si ya tienes `MCP_URL`, el compartido (`https://ca-mcp-server.icybush-2ea2dfc1.eastus2.azurecontainerapps.io/mcp`).

### Tools de tu dominio

| MCP | Tools que lista `dev/mcp/mcp_tools.py` |
|---|---|
| Mock | block_card¬ acción sensible¬ card_id, reason ; file_claim¬ acción sensible¬ customer_id, transaction_id, reason ; get_claim_status¬ consulta¬ claim_id ; get_transactions¬ consulta¬ customer_id, limit |
| Compartido | get_transactions, get_claim_status, block_card, file_claim |

### Conversación en `dev/chat.py` (paso 12)

| Prueba | Mensaje | Tool pedida (`→`) | Qué pasó | Primer texto / respuesta completa (ms) |
|---|---|---|---|---|
| Consulta de tu dominio | Soy CUS-1001, ¿puedo subir la línea de mi tarjeta CRD-2001 a 4000? | → get_transactions(customer_id=CUS-1001, limit=10) | La respuesta se clasifica como sensitive_action, el agente identifica que ha visto dos cargos en el supermercado SUPERMERCADO DEMO SAN ISIDRO (TRX-3001 y TRX-3002) | 17974 ms / 19749 ms |
| Acción confirmada | Sí, registra el reclamo por el cargo duplicado | No invoca a ninguna tool | Pide confirmar por cuál transacción se ingresará el reclamo (TRX-3001 y TRX-3002), indica lo que ocurrirá y cita las fuentes consultadas | 18089 ms / 18491 ms |
| Acción confirmada | Confirmo que deseo reclamar la transacción TRX-3002. El motivo es que me cobraron dos veces en el supermercado. Solicito registrar el reclamo. | → file_claim(customer_id=CUS-1001, transaction_id=TRX-3002, reason=Me cobraron dos veces en el supermercado; solicito reclamo por cargo duplicado.) | Respuesta NO SE EJECUTA, pendiente de aprobacion. Devuelve un json con status pendiente_aporbacion e indica que ha solicitado el reigstro delreclamo y queda pendinete aprobación por un asesor. | 25334 ms / 25481 ms |
| Sin tool que la resuelva | ¿Cuál es el saldo de mi cuenta de ahorros? | No invoca a ninguna tool | Indica que no puede ver saldos y se marca como out_of_scope. Cita la fuente service-channels.html | 12806 ms / 13062 ms |
| Tool de otro dominio | Soy CUS-1001, quiero solicitar un préstamo personal de S/ 20,000 a 24 meses. ¿Cuánto pagaría mensualmente? | El agente responde out_of_scope, indica que el alcance de este canal es fraude, bloqueo y reclamos. | No invoca a ninguna tool | 12911 ms / 13728 ms |

### ¿El modelo inventó algún dato cuando ninguna tool lo resolvía?

No. Al consultar el saldo de una cuenta de ahorros, el agente identificó correctamente que la solicitud estaba fuera de las capacidades disponibles para el dominio fraud y clasificó la respuesta como out_of_scope.

No inventó un saldo ni intentó obtenerlo mediante una tool que no correspondía. En su lugar, explicó la limitación y orientó al usuario hacia los canales bancarios disponibles, citando como fuente el documento service-channels.html.

### Conclusión

Las pruebas realizadas permitieron verificar la integración del agente con las tools MCP del dominio fraud, tanto en el servidor mock como en el compartido.

El agente utilizó correctamente get_transactions para identificar dos cargos duplicados (TRX-3001 y TRX-3002), correspondientes a un consumo de S/ 186.40 en SUPERMERCADO DEMO SAN ISIDRO.

Ante la solicitud de registrar un reclamo, el agente solicitó identificar la transacción afectada y proporcionar una descripción del problema antes de continuar. No ejecutó ninguna acción sensible durante la conversación observada.

Asimismo, frente a una consulta que no podía resolver, como el saldo de una cuenta de ahorros, reconoció sus limitaciones sin inventar información y proporcionó orientación respaldada por el corpus documental.

En general, el comportamiento observado demuestra que el agente puede consultar información mediante MCP, conservar el contexto conversacional y reconocer solicitudes fuera de su alcance.

# S7
## Con AGENT_RUNTIME=react
Tú: Soy CUS-1001, me cobraron dos veces en el supermercado
  → get_transactions(customer_id=CUS-1001, limit=10)
    resultado: {"result": [{"id": "TRX-3001", "date": "2026-10-20", "description": "SUPERMERCADO DEMO SAN ISIDRO", "amount": -186.4, "currency": "PEN", "card_id": "CRD-2001", 
  Agente [sensitive_action]: Veo dos cargos idénticos: TRX-3001 y TRX-3002 por S/186.40 el 2026-10-20 en SUPERMERCADO DEMO SAN ISIDRO (tarjeta CRD-2001). ¿Cuál de esos quiere reclamar como cobro duplicado? Si confirma, procedo a registrar el reclamo a su nombre. Nota: registrar el reclamo requiere su confirmación y quedará pendiente de aprobación por un asesor; no bloquearemos la tarjeta salvo que usted lo solicite.
  (primer texto en 15698 ms, respuesta completa en 15981 ms, 3705 tokens de entrada, 1575 de salida)
Tú: Sí, registra el reclamo por el cargo duplicado
  Agente [sensitive_action]: Para proceder necesito que confirme cuál(es) movimiento(s) desea reclamar: TRX-3001, TRX-3002 o ambos. Al confirmar, registraré el reclamo y quedará pendiente de aprobación por un asesor. No bloquearemos la tarjeta salvo que usted lo solicite. ¿Cuál opción elige?
  (primer texto en 14015 ms, respuesta completa en 14850 ms, 2540 tokens de entrada, 1638 de salida)
Tú: ¿Cuál es el saldo de mi cuenta de ahorros?
  Agente [out_of_scope]: No puedo consultar saldos aquí. Para ver su saldo use la banca móvil/web o llame al (01) 555-0200 (lun-sáb 8:00–20:00). También puede consultar en un cajero o en una agencia.
  Fuentes:
   [1] service-channels.html · Canales de atención para fraude y reclamos > Banca por teléfono
   [2] service-channels.html · Canales de atención para fraude y reclamos > Aplicación móvil
  (primer texto en 15318 ms, respuesta completa en 15465 ms, 2695 tokens de entrada, 1437 de salida)
Tú: ¿Qué movimientos estaban duplicados?
  Agente [data_query]: Los movimientos duplicados son TRX-3001 y TRX-3002: ambos por S/186.40 el 2026-10-20 en SUPERMERCADO DEMO SAN ISIDRO (tarjeta CRD-2001). ¿Desea que registre el reclamo por TRX-3001, TRX-3002 o por ambos?
  (primer texto en 14952 ms, respuesta completa en 15909 ms, 3021 tokens de entrada, 1464 de salida)

## Con AGENT_RUNTIME=agent_framework
Tú: Soy CUS-1001, me cobraron dos veces en el supermercado
  → get_transactions(customer_id=CUS-1001, limit=10)
    resultado: {"result": [{"id": "TRX-3001", "date": "2026-10-20", "description": "SUPERMERCADO DEMO SAN ISIDRO", "amount": -186.4, "currency": "PEN", "card_id": "CRD-2001", 
  Agente [sensitive_action]: He visto dos cargos iguales: TRX-3001 y TRX-3002 (20-10-2026) por S/186.40 en SUPERMERCADO DEMO SAN ISIDRO con la tarjeta CRD-2001. Puedo registrar un reclamo por cargo duplicado (código 13.4). Esta acción requiere tu confirmación y quedará pendiente de aprobación por un asesor. ¿Confirmas que registre el reclamo por TRX-3002? Responde “sí” para proceder.
  Fuentes:
   [1] chargeback-form.md · Formulario de Solicitud de Contracargo y Desconocimiento de Operaciones > 4. Clasificación del Motivo del Contracargo (Tipos de Fraude)
   [2] credit-card-chargebacks.html · Contracargos con tarjeta de crédito > Casos que aplican
   [3] chargeback-form.md · Formulario de Solicitud de Contracargo y Desconocimiento de Operaciones > 3. Detalles de la Transacción en Disputa
  (primer texto en 19271 ms, respuesta completa en 19503 ms, 3705 tokens de entrada, 1449 de salida)
Tú: Sí, registra el reclamo por el cargo duplicado
  → file_claim(customer_id=CUS-1001, transaction_id=TRX-3002, reason=Cobro duplicado en supermercado: me cobraron dos veces en SUPERMERCADO DEMO SAN ISIDRO (veo TRX-3001 y TRX-3002). Solicito reclamo por cargo duplicado.)
    NO SE EJECUTA, pendiente de aprobación: {"status": "pendiente_aprobacion", "detail": "Acción sensible: no se ejecutó ni se registró todavía. Dile al cliente que la pediste y que un asesor la va a revi
  Agente [sensitive_action]: He solicitado el reclamo por TRX-3002 (cargo duplicado en SUPERMERCADO DEMO SAN ISIDRO). La solicitud quedó pendiente de aprobación por un asesor; no está resuelta aún. Cuando el reclamo quede registrado recibirás un código (formato RC-AAAA-NNNNNN) y podrás seguir el estado en la app (Reclamos > Mis reclamos) o por teléfono. Un asesor revisará el caso y te contactará si necesita más información.
  Fuentes:
   [1] unrecognized-charges-procedure.md · Procedimiento ante cargos no reconocidos > Paso 4: seguimiento
   [2] claims-regulation.pdf · Reglamento de atención de reclamos - Banco Demo > 3. Presentación del reclamo
  (primer texto en 25953 ms, respuesta completa en 27218 ms, 4650 tokens de entrada, 2586 de salida)
Tú: ¿Cuál es el saldo de mi cuenta de ahorros?
  Agente [out_of_scope]: Eso está fuera del alcance de este servicio (fraude, bloqueo y reclamos). Para ver el saldo de tu cuenta de ahorros, usa la app móvil, un cajero automático o llama a Banca por teléfono al (01) 555-0200 (lun-sáb 8:00–20:00). Si necesitas ayuda con un cargo no reconocido o bloquear una tarjeta, dime.
  Fuentes:
   [1] service-channels.html · Canales de atención para fraude y reclamos > Banca por teléfono
  (primer texto en 14660 ms, respuesta completa en 14914 ms, 3221 tokens de entrada, 1232 de salida)
Tú: ¿Qué movimientos estaban duplicados?
  Agente [data_query]: Los movimientos duplicados son TRX-3001 y TRX-3002 (20-10-2026), ambos por S/186.40 en SUPERMERCADO DEMO SAN ISIDRO con la tarjeta CRD-2001.
  (primer texto en 12975 ms, respuesta completa en 13011 ms, 3453 tokens de entrada, 1122 de salida)

## Sesión 7 — Skills, memoria de trabajo y Agent Framework

Dominio: `fraud`. La misma conversación con los dos runtimes (paso 7).

| | `react` | `agent_framework` |
|---|---|---|
| Tools pedidas en la consulta | get_transactions | get_transactions, file_claim |
| La acción sensible quedó **NO SE EJECUTA** | No se ejecutó ninguna acción sensible | Se invocó a file_claim, pero el harness devolvió No SE EJECUTA, pendiente de aprobación. |
| Pregunta de memoria respondida sin `→` | Sí. Identificó TRX-3001 y TRX-3002 sin consultar nuevamente las tools. | Sí. Identificó TRX-3001 y TRX-3002 sin consultar nuevamente las tools. |
| Primer texto (ms) | 59983ms | 72859ms |
| Respuesta completa (ms) | 62205ms | 74646ms |
| Tokens (entrada / salida) | 11961/6114 | 15029/6389 |

*Nota: Las métricas de tiempo en ms y tokes se obtuvo con la sumatoria de las 4 preguntas en cada caso.

### ¿La skill frenó la tool de otro dominio?

Mensaje: ¿Cuál es el saldo de mi cuenta de ahorros?. Respuesta:Ambos runtimes clasificaron la consulta como `out_of_scope` e indicaron que consultar saldos estaba fuera del alcance del servicio de fraude y reclamos. Recomendaron utilizar la banca móvil, un cajero automático o los canales de atención del banco..

### Diferencias entre los dos runtimes

`react` solicitó una confirmación adicional para identificar el movimiento que debía reclamarse, sin invocar `file_claim`. En cambio, `agent_framework` había propuesto reclamar TRX-3002 y, tras recibir la confirmación, invocó `file_claim`. El harness interceptó la solicitud y devolvió `NO SE EJECUTA`, manteniendo la operación pendiente de aprobación humana.

Ir por Agent Framework tiene tiempos de respuesta y utilización de tokens más alto.

### Conclusión

La diferencia principal se observó en el tratamiento de la acción sensible. Con `agent_framework`, se verificó que `file_claim` fue interceptada por el harness y quedó pendiente de aprobación humana, sin registrar efectivamente el reclamo.

# S8
## Sesión 8 — Aprobación humana, validación y reintentos

Dominio: `<dominio>` (paso 6).

| Caso | Runtime | Mensaje | Qué pasó | Resultado o ID |
|---|---|---|---|---|
| Aprobar | `agent_framework` | Soy CUS-1001, me cobraron dos veces en el supermercado¬ Sí, registra el reclamo por el cargo duplicado TRX-3002¬ s | Sigue el flujo al igual que las sesiones anteriores, con la excepción de que confirma con el asesor la aprobación de la transacción. Una vez aprobado da el resultado con el código de reclamo generado. | Tu reclamo quedó registrado con código CLM-9002 |
| Rechazar | `react` | Soy CUS-1001, me cobraron dos veces en el supermercado¬ Sí, registra el reclamo por el cargo duplicado TRX-3002¬ n | Cada mensaje da el mismo resultado, con diferencia de que el asesor rechaza el registro. | El asesor rechazó la solicitud de reclamo |
| Error de negocio (`CUS-9999`) | `react` | Soy CUS-9999, me cobraron dos veces en el supermercado | Invoca a la tool get_transactions; pero ésta devuelve que El cliente CUS-9999 no existe. Pide confirmar si es el cdigo correcto y explica el flujo para registrar el reclamo citando las fuentes. | {"error": "El cliente CUS-9999 no existe"} |
| Input inválido | `react` | Mi número de cliente es 9999, ¿qué cobros duplicados tengo? | Se clasifica el mensaje como `data_query` y pide un formato válido CUS-#### | Puedo revisar tus movimientos. Necesito tu código de cliente en formato CUS-#### (por ejemplo CUS-9999); con “9999” solo no puedo consultar. ¿Deseas que busque únicamente cobros duplicados o todos los movimientos de los últimos 60 días? |

### La trayectoria en el log

Línea 127: INFO agent.application.chat_service: trayectoria 8160769b-2d7a-4ee4-97e6-42e21fa96907: get_transactions ok → respuesta sensitive_action
Línea 167: INFO agent.application.chat_service: trayectoria 8160769b-2d7a-4ee4-97e6-42e21fa96907: file_claim pending_approval → respuesta sensitive_action
Línea 171: INFO agent.application.chat_service: trayectoria 8160769b-2d7a-4ee4-97e6-42e21fa96907: decisión del asesor → file_claim ok

Línea 122: INFO agent.application.chat_service: trayectoria ae64de51-69c1-4eaa-ac0a-8481f6270396: get_transactions ok → respuesta sensitive_action
Línea 153: INFO agent.application.chat_service: trayectoria ae64de51-69c1-4eaa-ac0a-8481f6270396: file_claim pending_approval → respuesta sensitive_action
Línea 154: INFO agent.application.chat_service: trayectoria ae64de51-69c1-4eaa-ac0a-8481f6270396: decisión del asesor → file_claim rejected

Línea 188: INFO agent.application.chat_service: trayectoria ac48e37f-200e-45a5-9b57-dc0c39cb19ed: get_transactions error → respuesta sensitive_action

Línea 215: INFO agent.application.chat_service: trayectoria 5fe0826c-22c4-46e0-af83-951d765a108c: sin tools → respuesta data_query

### ¿Algo se ejecutó sin que lo aprobaras?

No. En las pruebas realizadas, las acciones sensibles respetaron el flujo de aprobación humana (HITL).

- Aprobación: file_claim quedó inicialmente en estado pending_approval y solo se ejecutó después de que el asesor respondió s. Se registró correctamente el reclamo CLM-9002.

- Rechazo: al responder n, la acción pasó a estado rejected y no se registró ningún reclamo.

### Conclusión

Se comprobó el funcionamiento del control humano sobre las acciones sensibles del agente. El registro de reclamos requiere aprobación del asesor antes de ejecutarse, mientras que un rechazo impide la operación.

También se verificó que el agente maneja errores de negocio y entradas inválidas sin interrumpir la conversación ni ejecutar operaciones innecesarias. Las trayectorias registradas en los logs permiten identificar las tools utilizadas, sus estados y la decisión del asesor.

En conclusión, las pruebas realizadas confirman que el flujo de aprobación humana, la validación de entradas y el registro de trayectorias funcionan correctamente en los escenarios evaluados. Queda pendiente comprobar el comportamiento de los reintentos ante errores transitorios de conexión, ya que estos no se presentaron en las pruebas documentadas.

# S9
## Sesión 9 — Despliegue en Azure

Equipo: `team-03`. Dominio: `fraud`.

| Comprobación | Resultado |
|---|---|
| Tests en el contenedor (paso 3) | Una vez se hace el build del archivo Dockerfile y se ejecutan los test, se muestra ........................................................................ [ 50%]
............................sssss....................................... [100%]
139 passed, 5 skipped in 10.07s|
| Acción aprobada después de reiniciar `uvicorn` (paso 2, Cosmos DB) | Efectivamente, recupera la sesión de la conversación, se validó mediante la consulta a cosmos: {'id': '643d7bf8-acbe-4e4c-9e43-c80141520fd6', 'messages': 8, 'pending': None} |
| Imagen desplegada (`team-03/agent:<sha>`) | Resultado obtenido: IMAGE: acrworkshopjsu3.azurecr.io/team-03/agent:cefca1838dfb8f412b6883eb3d1e31c6be2b1f95 |
| Revisión activa y duración del job `deploy` | El JOB duró 2m 9s, se puede validar en el enlace: https://github.com/jaguilar96-dev/agent-scratch/actions/runs/45732485041/job/139617879541 |
| `/health` del agente desplegado | Agente en https://ca-agent-chat-03.icybush-2ea2dfc1.eastus2.azurecontainerapps.io: ok |
| Respuesta con `Fuentes:` contra Azure (y su tiempo en ms) | Primer mensaje: 53473 ms, Segundo mensaje: 16720 ms. Fuentes: [1] chargeback-form.md y [2] unrecognized-charges-procedure.md |
| Acción aprobada contra Azure, con su `resultado:` | El resutlado se cortó en la consola, lo que se muestra es resultado: {"id": "CLM-9001", "customer_id": "CUS-1001", "transaction_id": "TRX-3002", "reason": "Cargo duplicado en supermercado, solicito reclamo por TRX-3002", "status"
  Agente [sensitive_action]: Su reclamo quedó registrado con código CLM-9001; fue abierto el 2026-10-28 y la fecha límite de respuesta es 2026-11-27. La solicitud está registrada para que el banco la procese; no está aplicada aún. |

### Qué pone Azure y qué pone la imagen

Las variables de Azure:
AZURE_OPENAI_ENDPOINT
AZURE_CLIENT_ID
COSMOS_ENDPOINT
COSMOS_DATABASE
COSMOS_CONTAINER
SEARCH_ENDPOINT
SEARCH_INDEX
MCP_URL
MCP_SCOPE
TEAM_ID
KEY_VAULT_URI

Mientras que la imagen:
DOMAIN
FOUNDRY_AUTH_PROVIDER
KNOWLEDGE_BASE
AGENT_RUNTIME
PATH

### Problemas que encontraste y cómo los resolviste

En realidad siguiendo la guía paso a paso no he presentado problemas o errores durante la compilación o despliegue del agente.

### Conclusión

El agente se desplegó correctamente en Azure y respondió a las consultas de la misma forma que cuando hacíamos pruebas locales. También se verificó que las acciones sensibles requieren aprobación humana y que el historial se conserva gracias a la integración con Cosmos DB. Las pruebas realizadas confirmaron el funcionamiento esperado del despliegue a través de los Actions de Github.
