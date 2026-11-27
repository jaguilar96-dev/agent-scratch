Resultado: HTTP 422 - Unprocessable Entity.

La API rechaza correctamente las entradas inválidas.

## Observaciones

- Las pruebas automatizadas se ejecutan sin depender de servicios externos, mediante FakeChatModel.
- La integración funcional utiliza el mock local de Foundry, sin consumir recursos de Azure.
- Se validó la separación de responsabilidades mediante arquitectura hexagonal e inversión de dependencias.
- El laboratorio fue desarrollado desde la base histórica correspondiente a la sesión 1.
- Debido al avance del equipo, el PR se presenta como evidencia individual, sin realizar merge sobre la rama equipo-03.

## Entrega

- Participante: AIE-18HD.
- Rama: s1_AIE_18HD.
- Commit de implementación: 9632d46.
- Fecha de ejecución: 26/11/2026.
- Estado técnico: completado.



 # Sesión 2
 ##  laboratorio 2

- Participante: AIE-18HD
- Equipo: 03
- Dominio: fraud
- Rama: s2_AIE_18HD
- Fecha de ejecución: 27/11/2026

# Descripción

Se realizaron todos los cambios correspondiendes en el modelo, el manejo de errores, las pruebas, y todos los archivos .py relacionados para ahora usar microsoft foundry. 

# Pruebas:
 se utilizó el comando uv run pytest -q

Resultado final: 32 passed.

## 5. Resultados de conversaciones reales

Las cinco conversaciones se ejecutaron de manera
independiente contra el deployment gpt-5-mini.

| Mensaje | Intención | latency_ms | prompt_tokens | completion_tokens |
|---|---|---:|---:|---:|
| Hola, buenos días | greeting | 2485 | 381 | 113 |
| ¿Cuál es el plazo para presentar un reclamo? | product_question | 6147 | 388 | 686 |
| Quiero ver mis movimientos de ayer | data_query | 9128 | 384 | 766 |
| Me robaron la tarjeta, bloquéala | sensitive_action | 7056 | 387 | 917 |
| ¿A cuánto está el dólar hoy? | out_of_scope | 3275 | 385 | 287 |
| Total | | 28091 | 1925 | 2769 |

### Indicadores consolidados

- Clasificaciones correctas: 5 de 5.
- Exactitud en la muestra: 100%.
- Latencia promedio: 5618.2 ms.
- Latencia mínima: 2485 ms.
- Latencia máxima: 9128 ms.
- Tokens de entrada totales: 1925.
- Tokens de salida totales: 2769.
- Consumo total: 4694 tokens.
- Consumo promedio por consulta: 938.8 tokens.

# dos trade-offs de modelo y costo para el gate

¿ gpt-5-mini o gpt-5-nano para clasificar intención? ¿Qué pasa con la latencia y
la calidad? : gpt-5-nano para tareas simples, como la clasificación de intenciones, gpt-5-mini para consultas que requieran mayor capacidad de razonamiento como por ejemplo una descripción de operacion fraudulenta en algun producto puntual del cliente. Esa estrategia puede reducir latencia y costos. 


¿Cuánto cuesta por mes un MAX_TURNS=10  frente a MAX_TURNS=4 , con el tráfico
esperado? No disminuye tanto como se pudiera creer, se envian menos mensajes al LLM, con el tráfico esperado puede disminuir el costo un 10%. Es mejor dejar el MAX_TURNS=10

¿Conviene un modelo chico para greeting y out_of_scope , y uno grande solo
para el resto? Si conviene pero hay que tener muy clara la sensitive_action del usuario, de lo contrario tendriamos problemas de latencia que no deberían ocurrir y no habría mejora en los costos. 